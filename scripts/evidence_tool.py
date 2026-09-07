#!/usr/bin/env python3
"""Render and validate App Idea Research Agent v4.0 outputs.

Uses only the Python standard library. JSON Schema files are the portable contract;
this tool enforces the same required fields plus cross-file business rules.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse


METHODOLOGY_VERSION = "4.0"
GRADE_VALUE = {"D": 1, "C": 2, "B": 3, "A": 4}
LEVEL_VALUE = {"E0": 0, "E1": 1, "E2": 2, "E3": 3, "E4": 4}

ARCHETYPE_WEIGHTS = {
    "consumer_utility": {
        "problem_demand": 25,
        "monetization_economics": 15,
        "competitive_wedge": 20,
        "distribution_access": 25,
        "repeat_value_retention": 5,
        "timing": 10,
        "liquidity_cold_start": 0,
    },
    "consumer_subscription": {
        "problem_demand": 20,
        "monetization_economics": 20,
        "competitive_wedge": 15,
        "distribution_access": 20,
        "repeat_value_retention": 20,
        "timing": 5,
        "liquidity_cold_start": 0,
    },
    "b2b_prosumer": {
        "problem_demand": 25,
        "monetization_economics": 25,
        "competitive_wedge": 15,
        "distribution_access": 15,
        "repeat_value_retention": 15,
        "timing": 5,
        "liquidity_cold_start": 0,
    },
    "marketplace_network": {
        "problem_demand": 20,
        "monetization_economics": 10,
        "competitive_wedge": 10,
        "distribution_access": 20,
        "repeat_value_retention": 10,
        "timing": 5,
        "liquidity_cold_start": 25,
    },
}

FATAL_CODES = {
    "LEGAL_BLOCKED",
    "CORE_FEASIBILITY_BLOCKED",
    "PLATFORM_BLOCKED",
    "SAFETY_ETHICS_BLOCKED",
}
FATAL_STATUSES = {"clear", "blocked", "unknown"}
EVIDENCE_LEVELS = set(LEVEL_VALUE)
CLAIM_GRADES = set(GRADE_VALUE)
OBSERVATION_QUALITIES = {"direct", "estimated", "inferred"}
CLAIM_RELEVANCES = {"direct", "supporting", "weak"}
DIRECTIONS = {"supports", "contradicts", "neutral"}
EVIDENCE_STATUSES = {
    "observed",
    "not_found_after_protocol",
    "structurally_unobservable",
    "not_applicable",
}
SOURCE_TYPES = {
    "official_primary",
    "marketplace_primary",
    "first_party",
    "third_party_estimate",
    "community",
    "interview",
    "experiment",
    "user_input",
    "local_artifact",
    "synthetic",
}
WEB_SOURCE_TYPES = {
    "official_primary",
    "marketplace_primary",
    "third_party_estimate",
    "community",
}
MODES = {"quick", "standard", "deep", "compare"}
STAGES = {"desk_research", "prebuild_validation", "post_mvp"}
DECISIONS = {
    "ELENDIR",
    "BELIRSIZ",
    "TESTE_DEGER",
    "TEST_ONCELIKLI",
    "KILL",
    "PIVOT",
    "BUILD_SMALL",
    "TESTE_DEVAM",
    "SCALE",
    "ITERATE",
    "STOP",
}
STATUSES = {
    "DESK_RESEARCH_COMPLETE",
    "PREBUILD_PENDING",
    "PREBUILD_PASSED",
    "BUILDING",
    "POSTLAUNCH",
    "KILLED",
    "ARCHIVED",
    "LEGACY",
}
RISK_CATEGORIES = {
    "value",
    "usability",
    "technical_feasibility",
    "business_viability",
    "retention",
    "distribution",
    "regulation_safety",
    "liquidity",
}

ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


@dataclass
class ValidationResult:
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def merge(self, other: "ValidationResult", prefix: str = "") -> None:
        self.errors.extend(prefix + item for item in other.errors)
        self.warnings.extend(prefix + item for item in other.warnings)


def is_iso_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def is_url(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def round_score(value: float) -> int:
    return int(value + 0.5)


def load_json(path: Path, result: ValidationResult) -> Optional[Dict[str, Any]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        result.error(f"missing file: {path}")
        return None
    except json.JSONDecodeError as exc:
        result.error(f"invalid JSON {path}: {exc}")
        return None
    if not isinstance(value, dict):
        result.error(f"JSON root must be an object: {path}")
        return None
    return value


def load_jsonl(path: Path, result: ValidationResult) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        result.error(f"missing file: {path}")
        return records
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            result.error(f"invalid JSONL {path}:{line_number}: {exc}")
            continue
        if not isinstance(value, dict):
            result.error(f"JSONL record must be an object: {path}:{line_number}")
            continue
        value["__line__"] = line_number
        records.append(value)
    return records


def validate_evidence_records(records: Sequence[Dict[str, Any]]) -> ValidationResult:
    result = ValidationResult()
    required = {
        "evidence_id",
        "claim_id",
        "idea_id",
        "phase",
        "source_type",
        "source_title",
        "source_url",
        "source_ref",
        "artifact_path",
        "independence_root",
        "collected_at",
        "data_period",
        "geo",
        "storefront",
        "platform",
        "status",
        "observation",
        "value",
        "unit",
        "evidence_level",
        "observation_quality",
        "claim_relevance",
        "direction",
        "sample_n",
        "denominator",
        "limitations",
        "search_queries",
        "attempted_sources",
    }
    seen: set = set()
    for index, record in enumerate(records, 1):
        line = record.get("__line__", index)
        label = f"evidence line {line}"
        missing = sorted(required - set(record))
        extra = sorted(set(record) - required - {"__line__"})
        if missing:
            result.error(f"{label}: missing fields: {', '.join(missing)}")
            continue
        if extra:
            result.error(f"{label}: unknown fields: {', '.join(extra)}")
        evidence_id = record["evidence_id"]
        if not isinstance(evidence_id, str) or not ID_RE.match(evidence_id):
            result.error(f"{label}: invalid evidence_id")
        elif evidence_id in seen:
            result.error(f"{label}: duplicate evidence_id {evidence_id}")
        seen.add(evidence_id)
        for key in ("claim_id", "idea_id"):
            if not isinstance(record[key], str) or not ID_RE.match(record[key]):
                result.error(f"{label}: invalid {key}")
        if record["source_type"] not in SOURCE_TYPES:
            result.error(f"{label}: invalid source_type {record['source_type']!r}")
        if record["status"] not in EVIDENCE_STATUSES:
            result.error(f"{label}: invalid status {record['status']!r}")
        if record["evidence_level"] not in EVIDENCE_LEVELS:
            result.error(f"{label}: invalid evidence_level")
        if record["observation_quality"] not in OBSERVATION_QUALITIES:
            result.error(f"{label}: invalid observation_quality")
        if record["claim_relevance"] not in CLAIM_RELEVANCES:
            result.error(f"{label}: invalid claim_relevance")
        if record["direction"] not in DIRECTIONS:
            result.error(f"{label}: invalid direction")
        if not is_iso_date(record["collected_at"]):
            result.error(f"{label}: collected_at must be YYYY-MM-DD")
        else:
            collected = date.fromisoformat(record["collected_at"])
            age_days = (date.today() - collected).days
            if age_days < -1:
                result.error(f"{label}: collected_at cannot be in the future")
            elif age_days > 183 and record["source_type"] in WEB_SOURCE_TYPES:
                result.warn(f"{label}: time-sensitive web evidence is older than 6 months")
        if not isinstance(record["source_title"], str) or not record["source_title"].strip():
            result.error(f"{label}: source_title is required")
        if not isinstance(record["independence_root"], str) or not record["independence_root"].strip():
            result.error(f"{label}: independence_root is required")
        if not isinstance(record["observation"], str) or not record["observation"].strip():
            result.error(f"{label}: observation is required")
        if record["source_type"] in WEB_SOURCE_TYPES and not is_url(record["source_url"]):
            result.error(f"{label}: web evidence requires an http(s) source_url")
        if record["source_url"] is not None and not is_url(record["source_url"]):
            result.error(f"{label}: source_url must be an http(s) URL or null")
        if not any(record.get(key) for key in ("source_url", "source_ref", "artifact_path")):
            result.error(f"{label}: source_url, source_ref or artifact_path is required")
        if record["source_type"] == "synthetic" and record["evidence_level"] != "E0":
            result.error(f"{label}: synthetic evidence must be E0")
        if record["status"] == "not_found_after_protocol":
            if not record["search_queries"] or not record["attempted_sources"]:
                result.error(f"{label}: not_found_after_protocol requires searches and attempted sources")
        if not isinstance(record["limitations"], list):
            result.error(f"{label}: limitations must be an array")
        if record["sample_n"] is not None:
            if not isinstance(record["sample_n"], int) or record["sample_n"] < 0:
                result.error(f"{label}: sample_n must be a non-negative integer or null")
            elif record["sample_n"] > 0 and record["denominator"] is None:
                result.warn(f"{label}: sample_n is set but denominator is missing")
    for claim_id, claim_records in group_by_claim(records).items():
        for root, base, split in grade_inflating_roots(claim_records):
            result.warn(
                f"claim {claim_id}: root {root} spans multiple URLs that would grade "
                f"{split} instead of {base} if counted as independent; confirm the root"
            )
    return result


def group_by_claim(records: Iterable[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    claims: Dict[str, List[Dict[str, Any]]] = {}
    for record in records:
        claims.setdefault(record.get("claim_id", ""), []).append(record)
    return claims


def compute_claim_grade(records: Sequence[Dict[str, Any]]) -> str:
    usable = [
        record
        for record in records
        if record.get("status") == "observed"
        and record.get("source_type") != "synthetic"
        and record.get("claim_relevance") != "weak"
    ]
    strong_counter = any(
        record.get("direction") == "contradicts"
        and LEVEL_VALUE.get(record.get("evidence_level"), 0) >= 3
        for record in usable
    )
    supports = [record for record in usable if record.get("direction") == "supports"]
    direct_e3_roots = {
        record.get("independence_root")
        for record in supports
        if record.get("evidence_level") == "E3" and record.get("claim_relevance") == "direct"
    }
    if strong_counter:
        return "D"
    if any(record.get("evidence_level") == "E4" for record in supports):
        return "A"
    if len(direct_e3_roots) >= 2:
        return "A"
    e3_roots = {
        record.get("independence_root")
        for record in supports
        if LEVEL_VALUE.get(record.get("evidence_level"), 0) >= 3
    }
    e2_roots = {
        record.get("independence_root")
        for record in supports
        if record.get("evidence_level") == "E2"
    }
    if any(root not in e3_roots for root in e2_roots) and e3_roots:
        return "B"
    if len(e2_roots) >= 3:
        return "B"
    e1_roots = {
        record.get("independence_root")
        for record in supports
        if record.get("evidence_level") == "E1"
    }
    if e3_roots or e2_roots or len(e1_roots) >= 2:
        return "C"
    return "D"


def split_root_records(
    records: Sequence[Dict[str, Any]], root: str
) -> List[Dict[str, Any]]:
    """Copy of ``records`` in which every URL under ``root`` becomes its own root."""
    split: List[Dict[str, Any]] = []
    for record in records:
        url = record.get("source_url")
        if record.get("independence_root") != root or url is None:
            split.append(record)
            continue
        clone = dict(record)
        clone["independence_root"] = f"{root} #url={url}"
        split.append(clone)
    return split


def grade_inflating_roots(
    records: Sequence[Dict[str, Any]],
) -> List[Tuple[str, str, str]]:
    """Roots whose several URLs would lift the claim grade if counted as independent.

    A conservative root legitimately spans several URLs: publisher granularity for a
    vendor asserting its own capability, or one collection protocol run over several
    feeds. That only misleads a reader when splitting the root would raise the grade,
    which is also the shape of echoed coverage (one primary report behind many URLs).
    """
    urls_by_root: Dict[str, set] = {}
    for record in records:
        url = record.get("source_url")
        if url is not None:
            urls_by_root.setdefault(record.get("independence_root", ""), set()).add(url)
    base = compute_claim_grade(records)
    inflating: List[Tuple[str, str, str]] = []
    for root, urls in sorted(urls_by_root.items()):
        if not root or len(urls) < 2:
            continue
        split = compute_claim_grade(split_root_records(records, root))
        if GRADE_VALUE[split] > GRADE_VALUE[base]:
            inflating.append((root, base, split))
    return inflating


def has_strong_counter(records: Sequence[Dict[str, Any]]) -> bool:
    return any(
        record.get("status") == "observed"
        and record.get("direction") == "contradicts"
        and record.get("claim_relevance") != "weak"
        and LEVEL_VALUE.get(record.get("evidence_level"), 0) >= 3
        for record in records
    )


def expected_overall_grade(
    assumptions: Sequence[Dict[str, Any]], computed_grades: Dict[str, str]
) -> str:
    ranked = sorted(
        assumptions,
        key=lambda item: (item.get("impact", 0) * item.get("uncertainty", 0)),
        reverse=True,
    )[:3]
    grades = [computed_grades.get(item.get("claim_id"), "D") for item in ranked]
    while len(grades) < 3:
        grades.append("D")
    return min(grades, key=lambda grade: GRADE_VALUE[grade])


def compute_opportunity(
    archetype: str, dimensions: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    weights = ARCHETYPE_WEIGHTS[archetype]
    for key, weight in weights.items():
        if weight and dimensions.get(key) is None:
            return None
    scores: Dict[str, int] = {}
    for bound in ("low", "base", "high"):
        total = 0.0
        for key, weight in weights.items():
            dimension = dimensions.get(key)
            if weight and dimension is not None:
                total += weight * dimension[bound] / 5.0
        scores[bound] = round_score(total)
    if scores["high"] < 40:
        classification = "weak"
    elif scores["low"] >= 60:
        classification = "attractive"
    else:
        classification = "borderline"
    scores["classification"] = classification
    return scores


def validate_assessment(
    assessment: Dict[str, Any], records: Sequence[Dict[str, Any]]
) -> ValidationResult:
    result = ValidationResult()
    required = {
        "methodology_version",
        "idea_id",
        "analysis_date",
        "mode",
        "stage",
        "target_segment",
        "target_geos",
        "primary_archetype",
        "risk_modifiers",
        "dimensions",
        "opportunity",
        "fatal_gates",
        "riskiest_assumptions",
        "overall_evidence_grade",
        "decision",
        "status",
        "next_test",
        "stopping_rule",
        "post_mvp_result",
    }
    missing = sorted(required - set(assessment))
    extra = sorted(set(assessment) - required)
    if missing:
        result.error(f"assessment missing fields: {', '.join(missing)}")
        return result
    if extra:
        result.error(f"assessment has unknown fields: {', '.join(extra)}")
    if assessment["methodology_version"] != METHODOLOGY_VERSION:
        result.error("assessment methodology_version must be 4.0")
    if not is_iso_date(assessment["analysis_date"]):
        result.error("assessment analysis_date must be YYYY-MM-DD")
    if assessment["mode"] not in MODES:
        result.error("assessment mode is invalid")
    if assessment["stage"] not in STAGES:
        result.error("assessment stage is invalid")
    archetype = assessment["primary_archetype"]
    if archetype not in ARCHETYPE_WEIGHTS:
        result.error("assessment primary_archetype is invalid")
        return result
    if assessment["decision"] not in DECISIONS:
        result.error("assessment decision is invalid")
    if assessment["status"] not in STATUSES:
        result.error("assessment status is invalid")
    if assessment["overall_evidence_grade"] not in CLAIM_GRADES:
        result.error("assessment overall_evidence_grade is invalid")
    if not isinstance(assessment["target_segment"], str) or not assessment["target_segment"].strip():
        result.error("assessment target_segment is required")
    if not isinstance(assessment["target_geos"], list) or not assessment["target_geos"]:
        result.error("assessment target_geos requires at least one geo")
    allowed_modifiers = {
        "regulated",
        "sensitive_data",
        "ai_variable_cost",
        "hardware_dependency",
        "children",
        "platform_dependency",
    }
    modifiers = assessment["risk_modifiers"]
    if not isinstance(modifiers, list) or len(modifiers) != len(set(modifiers)):
        result.error("assessment risk_modifiers must be a unique array")
    elif any(modifier not in allowed_modifiers for modifier in modifiers):
        result.error("assessment risk_modifiers contains an invalid modifier")

    evidence_ids = {record.get("evidence_id") for record in records}
    claim_groups = group_by_claim(records)
    computed_grades = {
        claim_id: compute_claim_grade(claim_records)
        for claim_id, claim_records in claim_groups.items()
    }

    dimensions = assessment["dimensions"]
    if not isinstance(dimensions, dict):
        result.error("assessment dimensions must be an object")
        return result
    for key in ARCHETYPE_WEIGHTS[archetype]:
        if key not in dimensions:
            result.error(f"assessment missing dimension {key}")
            continue
        dimension = dimensions[key]
        if dimension is None:
            continue
        if not isinstance(dimension, dict):
            result.error(f"dimension {key} must be object or null")
            continue
        if not all(name in dimension for name in ("low", "base", "high", "claim_ids")):
            result.error(f"dimension {key} is incomplete")
            continue
        low, base, high = dimension["low"], dimension["base"], dimension["high"]
        if not all(isinstance(value, int) and 1 <= value <= 5 for value in (low, base, high)):
            result.error(f"dimension {key} scores must be integers 1..5")
        elif not low <= base <= high:
            result.error(f"dimension {key} must satisfy low <= base <= high")
        if not dimension["claim_ids"]:
            result.error(f"dimension {key} requires at least one claim_id")
        for claim_id in dimension["claim_ids"]:
            if claim_id not in claim_groups:
                result.error(f"dimension {key} references unknown claim_id {claim_id}")

    expected_opportunity = compute_opportunity(archetype, dimensions)
    if assessment["opportunity"] != expected_opportunity:
        result.error(
            "assessment opportunity does not match arketype weights/dimensions: "
            f"expected {expected_opportunity!r}"
        )

    gates = assessment["fatal_gates"]
    if not isinstance(gates, list):
        result.error("fatal_gates must be an array")
        gates = []
    codes = [gate.get("code") for gate in gates if isinstance(gate, dict)]
    if set(codes) != FATAL_CODES or len(codes) != 4:
        result.error("fatal_gates must contain each v4 gate exactly once")
    for gate in gates:
        if not isinstance(gate, dict):
            result.error("fatal gate must be an object")
            continue
        if gate.get("status") not in FATAL_STATUSES:
            result.error(f"fatal gate {gate.get('code')} has invalid status")
        if not gate.get("evidence_ids"):
            result.error(f"fatal gate {gate.get('code')} requires evidence_ids")
        for evidence_id in gate.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                result.error(f"fatal gate {gate.get('code')} references unknown evidence {evidence_id}")

    assumptions = assessment["riskiest_assumptions"]
    if not isinstance(assumptions, list):
        result.error("riskiest_assumptions must be an array")
        assumptions = []
    for assumption in assumptions:
        claim_id = assumption.get("claim_id")
        if claim_id not in claim_groups:
            result.error(f"RAT references unknown claim_id {claim_id}")
        if assumption.get("category") not in RISK_CATEGORIES:
            result.error(f"RAT {claim_id} has invalid category")
        if assumption.get("claim_grade") not in CLAIM_GRADES:
            result.error(f"RAT {claim_id} has invalid claim_grade")
        expected_grade = computed_grades.get(claim_id, "D")
        if assumption.get("claim_grade") != expected_grade:
            result.error(
                f"RAT {claim_id} grade {assumption.get('claim_grade')} does not match evidence grade {expected_grade}"
            )
    overall = expected_overall_grade(assumptions, computed_grades)
    if assessment["overall_evidence_grade"] != overall:
        result.error(
            f"overall_evidence_grade must be minimum of top three RAT claims: expected {overall}"
        )

    blocked = any(gate.get("status") == "blocked" for gate in gates if isinstance(gate, dict))
    unknown = any(gate.get("status") == "unknown" for gate in gates if isinstance(gate, dict))
    decision = assessment["decision"]
    stage = assessment["stage"]
    opportunity = expected_opportunity
    grade = assessment["overall_evidence_grade"]
    if stage == "desk_research":
        if blocked:
            expected_decision = "ELENDIR"
        elif unknown or opportunity is None or grade == "D":
            expected_decision = "BELIRSIZ"
        elif opportunity["high"] < 40:
            expected_decision = "ELENDIR"
        elif opportunity["low"] >= 60:
            expected_decision = "TEST_ONCELIKLI"
        else:
            expected_decision = "TESTE_DEGER"
        if decision != expected_decision:
            result.error(f"desk decision must be {expected_decision}, got {decision}")
    elif stage == "prebuild_validation":
        if decision not in {"KILL", "PIVOT", "BUILD_SMALL", "TESTE_DEVAM"}:
            result.error("prebuild decision must be KILL, PIVOT, BUILD_SMALL or TESTE_DEVAM")
        if blocked and decision != "KILL":
            result.error("blocked fatal gate requires KILL at prebuild stage")
        value_countered = any(
            item.get("category") == "value"
            and has_strong_counter(claim_groups.get(item.get("claim_id"), []))
            for item in assumptions
        )
        value_supported = any(
            item.get("category") == "value"
            and item.get("claim_grade") in {"A", "B"}
            and item.get("disposition") == "supported"
            for item in assumptions
        )
        solution_countered = any(
            item.get("category") == "usability"
            and has_strong_counter(claim_groups.get(item.get("claim_id"), []))
            for item in assumptions
        )
        if value_countered and decision != "KILL":
            result.error("strongly contradicted value/problem claim requires KILL")
        elif value_supported and solution_countered and decision != "PIVOT":
            result.error("supported problem plus contradicted solution/wedge requires PIVOT")
        if decision == "BUILD_SMALL":
            top = sorted(
                assumptions,
                key=lambda item: item.get("impact", 0) * item.get("uncertainty", 0),
                reverse=True,
            )[:1]
            top_grade_ok = bool(top) and top[0].get("claim_grade") in {"A", "B"}
            behavior_ok = any(item.get("product_specific_behavior") for item in assumptions)
            if blocked or unknown:
                result.error("BUILD_SMALL cannot have blocked/unknown fatal gates")
            if opportunity is None or opportunity["low"] < 60:
                result.error("BUILD_SMALL requires opportunity.low >= 60")
            if grade not in {"A", "B"} or not top_grade_ok:
                result.error("BUILD_SMALL requires overall and top RAT grade B+")
            if not behavior_ok:
                result.error("BUILD_SMALL requires product-specific behavior")
            if archetype == "consumer_subscription":
                retention_ready = any(
                    item.get("category") == "retention"
                    and item.get("claim_grade") in {"A", "B"}
                    and item.get("product_specific_behavior")
                    for item in assumptions
                )
                if not retention_ready:
                    result.error("subscription BUILD_SMALL requires product-specific retention evidence B+")
            if archetype == "marketplace_network":
                liquidity_ready = any(
                    item.get("category") == "liquidity"
                    and item.get("claim_grade") in {"A", "B"}
                    and item.get("product_specific_behavior")
                    for item in assumptions
                )
                if not liquidity_ready:
                    result.error("marketplace BUILD_SMALL requires product-specific liquidity evidence B+")
    elif stage == "post_mvp":
        if decision not in {"SCALE", "ITERATE", "STOP"}:
            result.error("post_mvp decision must be SCALE, ITERATE or STOP")
        if blocked and decision != "STOP":
            result.error("blocked fatal gate requires STOP at post_mvp stage")
        post = assessment.get("post_mvp_result")
        if not isinstance(post, dict):
            result.error("post_mvp stage requires post_mvp_result")
        elif decision == "SCALE":
            if (
                post.get("consecutive_passing_cohorts", 0) < 2
                or not post.get("value_activation_passed")
                or not post.get("retention_passed")
                or not post.get("economics_passed")
                or post.get("remaining_failed_metrics") != 0
            ):
                result.error("SCALE requires two passing cohorts and all core thresholds")
        elif decision == "ITERATE":
            if (
                not post.get("value_activation_passed")
                or post.get("remaining_failed_metrics") != 1
                or post.get("consecutive_value_or_retention_failures", 0) >= 2
            ):
                result.error("ITERATE requires value pass, one failed metric, and no two-cohort stop condition")
        elif decision == "STOP" and not blocked:
            if (
                post.get("consecutive_value_or_retention_failures", 0) < 2
                and post.get("value_activation_passed")
            ):
                result.error("STOP requires a fatal gate, value failure, or two value/retention failures")
    if stage != "post_mvp" and assessment.get("post_mvp_result") is not None:
        result.error("post_mvp_result must be null before post_mvp stage")

    allowed_status = {
        "ELENDIR": {"KILLED"},
        "BELIRSIZ": {"DESK_RESEARCH_COMPLETE"},
        "TESTE_DEGER": {"PREBUILD_PENDING"},
        "TEST_ONCELIKLI": {"PREBUILD_PENDING"},
        "KILL": {"KILLED"},
        "PIVOT": {"PREBUILD_PENDING"},
        "BUILD_SMALL": {"PREBUILD_PASSED", "BUILDING"},
        "TESTE_DEVAM": {"PREBUILD_PENDING"},
        "SCALE": {"POSTLAUNCH"},
        "ITERATE": {"POSTLAUNCH"},
        "STOP": {"KILLED"},
    }
    if assessment["status"] not in allowed_status.get(decision, set()):
        result.error(f"status {assessment['status']} is inconsistent with decision {decision}")
    return result


def markdown_escape(value: Any) -> str:
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_ledger(records: Sequence[Dict[str, Any]]) -> str:
    ordered = sorted(records, key=lambda item: (item.get("claim_id", ""), item.get("evidence_id", "")))
    lines = [
        "# Kanit Defteri",
        "",
        "> Bu dosya `data/evidence.jsonl` kaynagindan deterministik olarak uretilmistir.",
        "",
        "| Evidence | Claim | Seviye | Yon | Gozlem | Kaynak | Baglam | Sinirlar |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for record in ordered:
        source_label = markdown_escape(record.get("source_title"))
        if record.get("source_url"):
            source = f"[{source_label}]({record['source_url']})"
        else:
            ref = record.get("source_ref") or record.get("artifact_path") or "—"
            source = f"{source_label} ({markdown_escape(ref)})"
        context = "/".join(
            markdown_escape(value)
            for value in (record.get("geo"), record.get("storefront"), record.get("platform"))
            if value
        ) or "—"
        limitations = "; ".join(record.get("limitations") or []) or "—"
        lines.append(
            "| {evidence} | {claim} | {level} | {direction} | {observation} | {source} | {context} | {limitations} |".format(
                evidence=markdown_escape(record.get("evidence_id")),
                claim=markdown_escape(record.get("claim_id")),
                level=markdown_escape(record.get("evidence_level")),
                direction=markdown_escape(record.get("direction")),
                observation=markdown_escape(record.get("observation")),
                source=source,
                context=context,
                limitations=markdown_escape(limitations),
            )
        )
    lines.append("")
    return "\n".join(lines)


def required_phase_files(mode: str, decision: str) -> List[str]:
    if mode not in {"standard", "deep"}:
        return []
    files = [
        "01-market-scan.md",
        "02-competitor-analysis.md",
        "03-review-mining.md",
        "04-scoring.md",
        "05-validation.md",
    ]
    if decision in {"TESTE_DEGER", "TEST_ONCELIKLI", "TESTE_DEVAM", "PIVOT", "BUILD_SMALL"}:
        files.append("06-prebuild-plan.md")
    if mode == "deep":
        files.extend(
            [
                "07-feature-matrix.md",
                "08-aso-research.md",
                "09-financial-model.md",
                "10-project-brief.md",
                "11-devils-advocate.md",
            ]
        )
    return files


def validate_output(output_dir: Path) -> ValidationResult:
    result = ValidationResult()
    report_path = output_dir / "REPORT.md"
    evidence_path = output_dir / "data" / "evidence.jsonl"
    assessment_path = output_dir / "data" / "assessment.json"
    ledger_path = output_dir / "data" / "evidence-ledger.md"
    records = load_jsonl(evidence_path, result)
    result.merge(validate_evidence_records(records))
    assessment = load_json(assessment_path, result)
    if assessment is not None:
        result.merge(validate_assessment(assessment, records))
    if not ledger_path.exists():
        result.error(f"missing file: {ledger_path}")
    else:
        expected_ledger = render_ledger(records)
        actual_ledger = ledger_path.read_text(encoding="utf-8")
        if actual_ledger != expected_ledger:
            result.error("evidence-ledger.md is not in sync; run evidence_tool.py render")
    if not report_path.exists():
        result.error(f"missing file: {report_path}")
    elif assessment is not None:
        report = report_path.read_text(encoding="utf-8")
        if "v4.0" not in report:
            result.error("REPORT.md must identify methodology v4.0")
        if assessment["decision"] not in report:
            result.error("REPORT.md decision does not match assessment.json")
        if "data/evidence-ledger.md" not in report:
            result.error("REPORT.md must link data/evidence-ledger.md")
    if assessment is not None:
        phases = output_dir / "phases"
        for name in required_phase_files(assessment["mode"], assessment["decision"]):
            if not (phases / name).exists():
                result.error(f"missing phase file for {assessment['mode']}: phases/{name}")
        if assessment["mode"] == "deep" and not (output_dir / "data" / "raw-search-results.md").exists():
            result.error("deep mode requires data/raw-search-results.md")
    return result


def print_result(label: str, result: ValidationResult) -> None:
    status = "PASS" if result.ok else "FAIL"
    print(f"{status} {label}")
    for warning in result.warnings:
        print(f"  WARN: {warning}")
    for error in result.errors:
        print(f"  ERROR: {error}")


def command_render(output_dir: Path) -> int:
    result = ValidationResult()
    records = load_jsonl(output_dir / "data" / "evidence.jsonl", result)
    result.merge(validate_evidence_records(records))
    if not result.ok:
        print_result(str(output_dir), result)
        return 1
    ledger_path = output_dir / "data" / "evidence-ledger.md"
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    ledger_path.write_text(render_ledger(records), encoding="utf-8")
    print(f"WROTE {ledger_path}")
    return 0


def classify_output(output_dir: Path) -> str:
    """Return the contract that governs a directory.

    ``assessment`` directories are v4 idea runs and carry ``data/assessment.json``.
    ``support`` directories are v4 portable analysis surfaces (keyword research,
    compare artifacts) that carry ``artifact.json`` but score no single idea, so the
    Quick/Standard/Deep output contract does not apply to them.
    Everything else is a pre-v4 report.
    """
    if (output_dir / "data" / "assessment.json").exists():
        return "assessment"
    if (output_dir / "artifact.json").exists():
        return "support"
    return "legacy"


def command_validate_all(output_root: Path, skip_legacy: bool) -> int:
    failed = False
    found = False
    for output_dir in sorted(path for path in output_root.iterdir() if path.is_dir()):
        kind = classify_output(output_dir)
        if kind == "support":
            print(f"SKIP SUPPORT {output_dir}")
            continue
        if kind == "legacy":
            if skip_legacy:
                print(f"SKIP LEGACY {output_dir}")
                continue
            if not (output_dir / "REPORT.md").exists():
                continue
        found = True
        result = validate_output(output_dir)
        print_result(str(output_dir), result)
        failed = failed or not result.ok
    if not found and not skip_legacy:
        print(f"WARN no output directories found under {output_root}")
    return 1 if failed else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    render_parser = subparsers.add_parser("render", help="render Markdown ledger from JSONL")
    render_parser.add_argument("output_dir", type=Path)
    validate_parser = subparsers.add_parser("validate", help="validate one v4 output directory")
    validate_parser.add_argument("output_dir", type=Path)
    all_parser = subparsers.add_parser("validate-all", help="validate all output directories")
    all_parser.add_argument("output_root", type=Path, nargs="?", default=Path("output"))
    all_parser.add_argument("--skip-legacy", action="store_true")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "render":
        return command_render(args.output_dir)
    if args.command == "validate":
        result = validate_output(args.output_dir)
        print_result(str(args.output_dir), result)
        return 0 if result.ok else 1
    if args.command == "validate-all":
        return command_validate_all(args.output_root, args.skip_legacy)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
