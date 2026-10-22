"""Validate JSON values against the portable JSON Schema files in ``schemas/``.

Standard library only. The schemas are the portable contract; this module enforces
them so ``evidence_tool.py`` checks every structural rule before computing grades,
scores or decisions. It implements exactly the JSON Schema 2020-12 keywords those
schemas use. A schema that uses any other keyword, format or reference form is
rejected when it is loaded, so the contract and this validator cannot drift apart
silently.

JSON semantics are kept: ``true``/``false`` are never integers or numbers, ``1`` and
``1.0`` are the same number, and ``enum``/``const``/``uniqueItems`` compare by JSON
value rather than by Python equality (where ``True == 1``).
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


JSON_TYPES = ("null", "boolean", "object", "array", "number", "integer", "string")
SUPPORTED_KEYWORDS = {
    "$schema",
    "$id",
    "$comment",
    "$defs",
    "$ref",
    "title",
    "description",
    "type",
    "enum",
    "const",
    "properties",
    "required",
    "additionalProperties",
    "items",
    "minItems",
    "maxItems",
    "uniqueItems",
    "minLength",
    "pattern",
    "format",
    "minimum",
    "maximum",
    "allOf",
    "anyOf",
    "oneOf",
    "if",
    "then",
    "else",
}
SUPPORTED_FORMATS = {"date", "uri"}
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
URI_RE = re.compile(r"[A-Za-z][A-Za-z0-9+.\-]*:\S+")

# (path, message); path is "" for the instance root, else e.g. "a.b[0].c".
SchemaError = Tuple[str, str]


class SchemaDefinitionError(ValueError):
    """The schema file itself uses something this validator does not implement."""


def json_type(value: Any) -> str:
    """JSON type name of a value produced by ``json.loads``."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "integer" if value.is_integer() else "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def is_json_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def matches_type(value: Any, name: str) -> bool:
    if name == "number":
        return is_json_number(value)
    return json_type(value) == name


def json_equal(left: Any, right: Any) -> bool:
    """Equality by JSON value: booleans are not numbers, 1 equals 1.0."""
    if isinstance(left, bool) or isinstance(right, bool):
        return isinstance(left, bool) and isinstance(right, bool) and left == right
    if is_json_number(left) or is_json_number(right):
        return is_json_number(left) and is_json_number(right) and left == right
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(json_equal(a, b) for a, b in zip(left, right))
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(json_equal(left[key], right[key]) for key in left)
    return type(left) is type(right) and left == right


def show(value: Any, limit: int = 60) -> str:
    text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return text if len(text) <= limit else text[: limit - 1] + "…"


def child_path(path: str, key: str) -> str:
    return f"{path}.{key}" if path else key


def item_path(path: str, index: int) -> str:
    return f"{path}[{index}]"


class Schema:
    """One schema document; ``errors`` returns every violation of an instance."""

    def __init__(self, document: Any, name: str) -> None:
        if not isinstance(document, dict):
            raise SchemaDefinitionError(f"{name}: schema root must be an object")
        self.document = document
        self.name = name
        self._patterns: Dict[str, "re.Pattern[str]"] = {}
        self._check(document, "#")

    # -- schema definition checks -------------------------------------------------

    def _check(self, schema: Any, where: str) -> None:
        if isinstance(schema, bool):
            return
        if not isinstance(schema, dict):
            raise SchemaDefinitionError(f"{self.name} {where}: subschema must be an object or boolean")
        unsupported = sorted(set(schema) - SUPPORTED_KEYWORDS)
        if unsupported:
            raise SchemaDefinitionError(
                f"{self.name} {where}: unsupported keyword(s) {', '.join(unsupported)}"
            )
        types = schema.get("type")
        if types is not None:
            names = types if isinstance(types, list) else [types]
            if not names or any(name not in JSON_TYPES for name in names):
                raise SchemaDefinitionError(f"{self.name} {where}: invalid type {types!r}")
        if "format" in schema and schema["format"] not in SUPPORTED_FORMATS:
            raise SchemaDefinitionError(f"{self.name} {where}: unsupported format {schema['format']!r}")
        if "pattern" in schema:
            try:
                self._patterns[schema["pattern"]] = re.compile(schema["pattern"])
            except (re.error, TypeError) as exc:
                raise SchemaDefinitionError(f"{self.name} {where}: invalid pattern: {exc}") from exc
        if "enum" in schema and not isinstance(schema["enum"], list):
            raise SchemaDefinitionError(f"{self.name} {where}: enum must be an array")
        if "required" in schema and not all(isinstance(key, str) for key in schema["required"]):
            raise SchemaDefinitionError(f"{self.name} {where}: required must list strings")
        if "$ref" in schema:
            self._resolve(schema["$ref"], where)
        for keyword in ("properties", "$defs"):
            for key, subschema in schema.get(keyword, {}).items():
                self._check(subschema, f"{where}/{keyword}/{key}")
        for keyword in ("items", "additionalProperties", "if", "then", "else"):
            if keyword in schema:
                self._check(schema[keyword], f"{where}/{keyword}")
        for keyword in ("allOf", "anyOf", "oneOf"):
            if keyword in schema:
                branches = schema[keyword]
                if not isinstance(branches, list) or not branches:
                    raise SchemaDefinitionError(f"{self.name} {where}: {keyword} must be a non-empty array")
                for index, subschema in enumerate(branches):
                    self._check(subschema, f"{where}/{keyword}/{index}")

    def _resolve(self, reference: Any, where: str) -> Any:
        if not isinstance(reference, str) or not reference.startswith("#"):
            raise SchemaDefinitionError(f"{self.name} {where}: only local $ref is supported")
        target: Any = self.document
        for token in reference[1:].split("/")[1:]:
            token = token.replace("~1", "/").replace("~0", "~")
            if not isinstance(target, dict) or token not in target:
                raise SchemaDefinitionError(f"{self.name} {where}: unresolvable $ref {reference}")
            target = target[token]
        return target

    # -- instance validation ------------------------------------------------------

    def errors(self, instance: Any) -> List[SchemaError]:
        return self._validate(self.document, instance, "")

    def is_valid(self, schema: Any, instance: Any) -> bool:
        return not self._validate(schema, instance, "")

    def _validate(self, schema: Any, instance: Any, path: str) -> List[SchemaError]:
        if schema is True:
            return []
        if schema is False:
            return [(path, "is not allowed")]
        errors: List[SchemaError] = []
        if "$ref" in schema:
            errors.extend(self._validate(self._resolve(schema["$ref"], "#"), instance, path))
        types = schema.get("type")
        if types is not None:
            names = types if isinstance(types, list) else [types]
            if not any(matches_type(instance, name) for name in names):
                errors.append((path, f"must be {' or '.join(names)} (got {json_type(instance)})"))
                return errors
        if "const" in schema and not json_equal(instance, schema["const"]):
            errors.append((path, f"is invalid: must be {show(schema['const'])} (got {show(instance)})"))
        if "enum" in schema and not any(json_equal(instance, option) for option in schema["enum"]):
            options = ", ".join(show(option) for option in schema["enum"])
            errors.append((path, f"is invalid: must be one of {options} (got {show(instance)})"))
        if isinstance(instance, dict):
            errors.extend(self._validate_object(schema, instance, path))
        elif isinstance(instance, list):
            errors.extend(self._validate_array(schema, instance, path))
        elif isinstance(instance, str):
            errors.extend(self._validate_string(schema, instance, path))
        elif is_json_number(instance):
            if "minimum" in schema and instance < schema["minimum"]:
                errors.append((path, f"must be >= {schema['minimum']} (got {show(instance)})"))
            if "maximum" in schema and instance > schema["maximum"]:
                errors.append((path, f"must be <= {schema['maximum']} (got {show(instance)})"))
        for subschema in schema.get("allOf", []):
            failed = self._validate(subschema, instance, path)
            if failed and isinstance(subschema, dict) and "description" in subschema:
                # A described rule reads better as one sentence than as its parts.
                errors.append((path, subschema["description"]))
            else:
                errors.extend(failed)
        if "anyOf" in schema:
            errors.extend(self._validate_alternatives(schema["anyOf"], instance, path, exactly_one=False))
        if "oneOf" in schema:
            errors.extend(self._validate_alternatives(schema["oneOf"], instance, path, exactly_one=True))
        if "if" in schema:
            branch = "then" if self.is_valid(schema["if"], instance) else "else"
            if branch in schema:
                errors.extend(self._validate(schema[branch], instance, path))
        return errors

    def _validate_object(self, schema: Dict[str, Any], instance: Dict[str, Any], path: str) -> List[SchemaError]:
        errors: List[SchemaError] = []
        missing = sorted(key for key in schema.get("required", []) if key not in instance)
        if missing:
            errors.append((path, f"missing fields: {', '.join(missing)}"))
        properties = schema.get("properties", {})
        for key, subschema in properties.items():
            if key in instance:
                errors.extend(self._validate(subschema, instance[key], child_path(path, key)))
        additional = schema.get("additionalProperties", True)
        extra = sorted(key for key in instance if key not in properties)
        if additional is False:
            if extra:
                errors.append((path, f"unknown fields: {', '.join(extra)}"))
        elif additional is not True:
            for key in extra:
                errors.extend(self._validate(additional, instance[key], child_path(path, key)))
        return errors

    def _validate_array(self, schema: Dict[str, Any], instance: List[Any], path: str) -> List[SchemaError]:
        errors: List[SchemaError] = []
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append((path, f"must have at least {schema['minItems']} item(s)"))
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append((path, f"must have at most {schema['maxItems']} item(s)"))
        if schema.get("uniqueItems") and any(
            json_equal(instance[i], instance[j])
            for i in range(len(instance))
            for j in range(i + 1, len(instance))
        ):
            errors.append((path, "must not contain duplicate items"))
        if "items" in schema:
            for index, item in enumerate(instance):
                errors.extend(self._validate(schema["items"], item, item_path(path, index)))
        return errors

    def _validate_string(self, schema: Dict[str, Any], instance: str, path: str) -> List[SchemaError]:
        errors: List[SchemaError] = []
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append((path, f"must have at least {schema['minLength']} character(s)"))
        if "pattern" in schema and not self._patterns[schema["pattern"]].search(instance):
            errors.append((path, f"does not match pattern {schema['pattern']} (got {show(instance)})"))
        fmt = schema.get("format")
        if fmt == "date" and not is_date(instance):
            errors.append((path, f"must be a YYYY-MM-DD date (got {show(instance)})"))
        elif fmt == "uri" and not URI_RE.fullmatch(instance):
            errors.append((path, f"must be an absolute URI (got {show(instance)})"))
        return errors

    def _validate_alternatives(
        self, branches: Sequence[Any], instance: Any, path: str, exactly_one: bool
    ) -> List[SchemaError]:
        results = [self._validate(branch, instance, path) for branch in branches]
        passing = sum(1 for errors in results if not errors)
        if exactly_one and passing > 1:
            return [(path, "matches more than one oneOf alternative")]
        if passing:
            return []
        # Report the alternative written for this JSON type (e.g. the object branch of
        # "null or object"), so a malformed object shows its own field errors.
        typed = [
            errors
            for branch, errors in zip(branches, results)
            if isinstance(branch, dict) and branch_accepts_type(branch, instance)
        ]
        if len(typed) == 1:
            return typed[0]
        names = [name for branch in branches for name in branch_types(branch)]
        if names and not typed:
            return [(path, f"must be {' or '.join(dict.fromkeys(names))} (got {json_type(instance)})")]
        return [(path, "does not match any allowed alternative")]


def branch_types(branch: Any) -> List[str]:
    if not isinstance(branch, dict) or "type" not in branch:
        return []
    types = branch["type"]
    return list(types) if isinstance(types, list) else [types]


def branch_accepts_type(branch: Dict[str, Any], instance: Any) -> bool:
    names = branch_types(branch)
    return bool(names) and any(matches_type(instance, name) for name in names)


def is_date(value: Any) -> bool:
    """Strict YYYY-MM-DD calendar date (``date.fromisoformat`` alone also accepts 20260710)."""
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def load_schema(path: Path) -> Schema:
    """Load and check a schema file; an unsupported schema raises SchemaDefinitionError."""
    return Schema(json.loads(path.read_text(encoding="utf-8")), path.name)


def format_errors(label: str, errors: Sequence[SchemaError]) -> List[str]:
    """``label path message`` lines; root errors read ``label message``."""
    return [f"{label} {path} {message}" if path else f"{label} {message}" for path, message in errors]
