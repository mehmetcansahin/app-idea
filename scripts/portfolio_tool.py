#!/usr/bin/env python3
"""Render and validate the App Idea Research portfolio (data/portfolio.json + INDEX.md).

Every v4 run (a directory under the output root with ``data/assessment.json``) carries
``data/portfolio.json`` (schemas/portfolio-entry.schema.json): the run's portfolio
lifecycle (active | archived | superseded), its replacement run and its human
experiment handoff. Portfolio metadata never changes the research status, scores,
evidence grade or decision in assessment.json and never authorizes BUILD_SMALL.

``render`` regenerates the two marked INDEX.md regions -- the v4 scoreboard and the
human experiment queue -- from assessment.json and portfolio.json; every line outside
the regions is kept. The first render adopts an unmarked scoreboard table: its v4 rows
move into the generated region, legacy rows stay below it under the original header.
``validate`` checks every run's metadata and that the INDEX.md regions are current.
Standard library only; independent of evidence_tool.py.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple


ASSESSMENT_PATH = Path("data") / "assessment.json"
PORTFOLIO_PATH = Path("data") / "portfolio.json"
EVIDENCE_PATH = Path("data") / "evidence.jsonl"
INDEX_NAME = "INDEX.md"
RENDER_COMMAND = "python3 scripts/portfolio_tool.py render"

ENTRY_FIELDS = ("title", "lifecycle", "superseded_by", "reason", "handoff")
HANDOFF_FIELDS = (
    "owner",
    "state",
    "prerequisites",
    "next_action",
    "plan_path",
    "result_evidence_ids",
)
LIFECYCLES = ("active", "archived", "superseded")
HANDOFF_STATES = ("blocked", "ready", "in_progress", "completed", "not_planned")
# Handoff states that are still work to do; on an archived/superseded run they are
# hidden from the queue, which is worth a warning.
OPEN_HANDOFF_STATES = ("blocked", "ready", "in_progress")
# A completed handoff must point at results the founder actually observed.
RESULT_SOURCE_TYPES = ("first_party", "experiment")
GRADES = ("A", "B", "C", "D")
MODE_NAMES = {
    "quick": "Quick Scan",
    "standard": "Standard",
    "deep": "Deep",
    "compare": "Compare",
}
ARCHETYPE_NAMES = {
    "consumer_utility": "Consumer Utility",
    "consumer_subscription": "Consumer Subscription",
    "b2b_prosumer": "B2B/Prosumer",
    "marketplace_network": "Marketplace/Network",
}

RUN_NAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
# Relative path of nonempty segments; no '.'/'..' segment, no leading '/', no '\'.
PLAN_PATH_RE = re.compile(r"(?!\.{1,2}(?:/|\Z))[^/\\]+(?:/(?!\.{1,2}(?:/|\Z))[^/\\]+)*")
ISO_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
REPORT_LINK_RE = re.compile(r"\]\(<?([^()<>\s/]+)/REPORT\.md>?\)")
UNESCAPED_PIPE_RE = re.compile(r"(?<!\\)\|")
TABLE_SEPARATOR_RE = re.compile(r"\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?")
FENCE_RE = re.compile(r"\s{0,3}(```|~~~)")

SCOREBOARD = "scoreboard"
HANDOFF = "handoff"
REGIONS = (SCOREBOARD, HANDOFF)
INDEX_TITLE = "# Araştırma Panosu"
SCOREBOARD_HEADING = "## v4.0 Araştırma Panosu"
QUEUE_HEADING = "## İnsan Deneyleri Kuyruğu"
GENERATED_NOTE = (
    "<!-- scripts/portfolio_tool.py render bu bloğu data/assessment.json ve "
    "data/portfolio.json dosyalarından üretir; elle düzenlemeyin. -->"
)
SCOREBOARD_NOTE = (
    "> Kayıtlar analiz tarihine göre yeniden eskiye, aynı tarihte dizin adına göre "
    "sıralanır; skora göre sıralanmaz. Fırsat skorları yalnız aynı arketip içinde "
    "karşılaştırılır. Skor, kanıt, karar, aşama ve `Araştırma Durumu` "
    "`data/assessment.json` dosyasından; `Konu`, `Portföy`, `Yerine Geçen`, "
    "`Portföy Notu` ve `Deney Devri` `data/portfolio.json` dosyasından gelir. "
    "Portföy durumu araştırma durumunu değiştirmez ve geliştirme izni vermez."
)
QUEUE_NOTE = (
    "> Yalnız `active` (aktif) kayıtların tanımlı deney devirleri listelenir; "
    "`archived` (arşivlenmiş) ve `superseded` (yerini başka rapor almış) kayıtların "
    "deneyleri burada görünmez. Kuyruk, deneyin yapıldığını göstermez: `completed` "
    "(tamamlandı) durumu yalnız doğrudan gözlenmiş `first_party` (birinci taraf) veya "
    "`experiment` (deney) sonuç kayıtlarıyla geçerlidir. Kayıtlar analiz tarihine göre "
    "yeniden eskiye, aynı tarihte dizin adına göre sıralanır."
)
SCOREBOARD_COLUMNS = (
    "Tarih",
    "Konu",
    "Mod",
    "Arketip",
    "Fırsat Skoru",
    "Kanıt",
    "Karar",
    "Aşama",
    "Araştırma Durumu",
    "Portföy",
    "Yerine Geçen",
    "Portföy Notu",
    "Deney Devri",
    "Metodoloji",
    "Rapor",
)
QUEUE_COLUMNS = (
    "Tarih",
    "Konu",
    "Arketip",
    "Karar",
    "Deney Durumu",
    "Sahip",
    "Ön koşullar",
    "Sonraki Adım",
    "Plan",
    "Sonuç Kanıtları",
)
NO_HANDOFF = "yok (sorumlu atanmadı)"


@dataclass
class Run:
    name: str
    assessment: Dict[str, Any]
    entry: Dict[str, Any]


@dataclass
class Portfolio:
    """v4 runs under one output root; ``runs`` holds only runs without errors."""

    runs: List[Run] = field(default_factory=list)
    v4_names: Set[str] = field(default_factory=set)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


def marker(region: str, edge: str) -> str:
    return f"<!-- portfolio:{region}:{edge} -->"


def is_nonblank(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_choice(value: Any, options: Sequence[str]) -> bool:
    return isinstance(value, str) and value in options


def is_score(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def is_iso_date(value: Any) -> bool:
    if not isinstance(value, str) or not ISO_DATE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def missing_and_unknown(value: Dict[str, Any], fields: Sequence[str]) -> List[str]:
    problems = []
    missing = [key for key in fields if key not in value]
    unknown = sorted(str(key) for key in value if key not in fields)
    if missing:
        problems.append(f"missing required field(s): {', '.join(missing)}")
    if unknown:
        problems.append(f"unknown field(s): {', '.join(unknown)}")
    return problems


def read_json_object(
    run_dir: Path, relative: Path, errors: List[str], missing_hint: str = ""
) -> Optional[Dict[str, Any]]:
    label = f"{run_dir.name}/{relative.as_posix()}"
    try:
        value = json.loads((run_dir / relative).read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{label}: missing file{missing_hint}")
        return None
    except OSError as exc:
        errors.append(f"{label}: cannot read: {exc}")
        return None
    except UnicodeDecodeError as exc:
        errors.append(f"{label}: not UTF-8: {exc}")
        return None
    except (ValueError, RecursionError) as exc:
        errors.append(f"{label}: invalid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label}: JSON root must be an object")
        return None
    return value


def check_assessment(name: str, assessment: Dict[str, Any]) -> List[str]:
    """Fields the INDEX shows; the full assessment contract belongs to evidence_tool."""
    label = f"{name}/{ASSESSMENT_PATH.as_posix()}"
    errors = []
    if not is_iso_date(assessment.get("analysis_date")):
        errors.append(f"{label}: analysis_date must be an ISO date (YYYY-MM-DD)")
    if not is_choice(assessment.get("mode"), tuple(MODE_NAMES)):
        errors.append(f"{label}: mode must be one of {', '.join(MODE_NAMES)}")
    if not is_choice(assessment.get("primary_archetype"), tuple(ARCHETYPE_NAMES)):
        errors.append(f"{label}: primary_archetype must be one of {', '.join(ARCHETYPE_NAMES)}")
    if not is_choice(assessment.get("overall_evidence_grade"), GRADES):
        errors.append(f"{label}: overall_evidence_grade must be one of {', '.join(GRADES)}")
    for key in ("idea_id", "methodology_version", "decision", "stage", "status"):
        if not is_nonblank(assessment.get(key)):
            errors.append(f"{label}: {key} must be a nonblank string")
    if "opportunity" not in assessment:
        errors.append(f"{label}: missing opportunity")
    else:
        opportunity = assessment["opportunity"]
        if opportunity is not None and not (
            isinstance(opportunity, dict)
            and all(is_score(opportunity.get(key)) for key in ("low", "base", "high"))
        ):
            errors.append(f"{label}: opportunity must be null or have integer low/base/high")
    return errors


def load_evidence_index(run_dir: Path) -> Tuple[Dict[str, Dict[str, Any]], List[str]]:
    label = f"{run_dir.name}/{EVIDENCE_PATH.as_posix()}"
    try:
        text = (run_dir / EVIDENCE_PATH).read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}, [f"{label}: missing file; handoff result evidence cannot be verified"]
    except OSError as exc:
        return {}, [f"{label}: cannot read: {exc}"]
    except UnicodeDecodeError as exc:
        return {}, [f"{label}: not UTF-8: {exc}"]
    index: Dict[str, Dict[str, Any]] = {}
    errors = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except (ValueError, RecursionError) as exc:
            errors.append(f"{label}:{number}: invalid JSON: {exc}")
            continue
        if isinstance(record, dict) and isinstance(record.get("evidence_id"), str):
            index.setdefault(record["evidence_id"], record)
    return index, errors


def check_results(
    run_dir: Path, label: str, evidence_ids: Sequence[str], idea_id: Any, completed: bool
) -> List[str]:
    index, errors = load_evidence_index(run_dir)
    for evidence_id in evidence_ids:
        record = index.get(evidence_id)
        prefix = f"{label}.result_evidence_ids: {evidence_id!r}"
        if record is None:
            errors.append(f"{prefix} is not in {EVIDENCE_PATH.as_posix()}")
            continue
        if isinstance(idea_id, str) and record.get("idea_id") != idea_id:
            errors.append(f"{prefix} belongs to idea {record.get('idea_id')!r}, not {idea_id!r}")
        if record.get("status") != "observed":
            errors.append(f"{prefix} is not an observed result (status {record.get('status')!r})")
        if not completed:
            continue
        if not is_choice(record.get("source_type"), RESULT_SOURCE_TYPES):
            errors.append(
                f"{prefix}: a completed handoff needs first_party or experiment results, "
                f"not source_type {record.get('source_type')!r}"
            )
        if not (is_nonblank(record.get("source_ref")) or is_nonblank(record.get("artifact_path"))):
            errors.append(f"{prefix}: result needs a nonblank source_ref or artifact_path")
    return errors


def check_plan_path(run_dir: Path, label: str, plan_path: Any) -> Tuple[List[str], Optional[Path]]:
    if plan_path is None:
        return [], None
    if not isinstance(plan_path, str) or not PLAN_PATH_RE.fullmatch(plan_path):
        return [
            f"{label}.plan_path must be null or a relative path inside the run directory "
            "(no leading '/', no '\\', no '.' or '..' segments)"
        ], None
    try:
        run_root = run_dir.resolve()
        target = (run_dir / plan_path).resolve()
    except (OSError, RuntimeError) as exc:
        return [f"{label}.plan_path {plan_path!r} cannot be resolved: {exc}"], None
    if run_root not in target.parents:
        return [f"{label}.plan_path {plan_path!r} escapes the run directory"], None
    if not target.is_file():
        return [f"{label}.plan_path {plan_path!r} is not an existing file in the run directory"], None
    return [], target


def check_handoff(
    run_dir: Path, label: str, handoff: Any, idea_id: Any
) -> Tuple[List[str], List[str]]:
    label = f"{label}: handoff"
    if not isinstance(handoff, dict):
        return [f"{label} must be an object or null"], []
    errors = [f"{label} {problem}" for problem in missing_and_unknown(handoff, HANDOFF_FIELDS)]
    warnings: List[str] = []
    owner = handoff.get("owner")
    if not is_nonblank(owner):
        errors.append(f"{label}.owner must be a nonblank human role from the plan")
    state = handoff.get("state")
    if not is_choice(state, HANDOFF_STATES):
        errors.append(f"{label}.state must be one of {', '.join(HANDOFF_STATES)}")
    prerequisites = handoff.get("prerequisites")
    if not isinstance(prerequisites, list) or not all(is_nonblank(item) for item in prerequisites):
        errors.append(f"{label}.prerequisites must be an array of nonblank strings")
    elif state == "blocked" and not prerequisites:
        errors.append(f"{label}: a blocked handoff needs at least one prerequisite")
    if not is_nonblank(handoff.get("next_action")):
        errors.append(f"{label}.next_action must be a nonblank string")
    plan_errors, plan_file = check_plan_path(run_dir, label, handoff.get("plan_path"))
    errors.extend(plan_errors)
    if plan_file is not None and is_nonblank(owner):
        try:
            plan_text = plan_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{label}.plan_path cannot be read: {exc}")
        else:
            # "Kurucu (atanmadı)" names the plan's role "Kurucu" plus an annotation.
            role = owner.split(" (", 1)[0].strip() or owner.strip()
            if role.casefold() not in plan_text.casefold():
                warnings.append(
                    f"{label}.owner role {role!r} does not appear in {handoff['plan_path']}; "
                    "use the human role the plan names"
                )
    results = handoff.get("result_evidence_ids")
    if not isinstance(results, list) or not all(is_nonblank(item) for item in results):
        errors.append(f"{label}.result_evidence_ids must be an array of nonblank evidence IDs")
        return errors, warnings
    duplicates = sorted({item for item in results if results.count(item) > 1})
    if duplicates:
        errors.append(f"{label}.result_evidence_ids repeats {', '.join(duplicates)}")
    if state == "completed" and not results:
        errors.append(
            f"{label}: a completed handoff needs result_evidence_ids naming observed "
            "first_party/experiment result records; nothing may be marked completed "
            "without its results"
        )
    if results:
        errors.extend(check_results(run_dir, label, results, idea_id, state == "completed"))
    return errors, warnings


def check_entry(
    run_dir: Path, entry: Dict[str, Any], idea_id: Any, v4_names: Set[str]
) -> Tuple[List[str], List[str]]:
    name = run_dir.name
    label = f"{name}/{PORTFOLIO_PATH.as_posix()}"
    errors = [f"{label}: {problem}" for problem in missing_and_unknown(entry, ENTRY_FIELDS)]
    warnings: List[str] = []
    if not is_nonblank(entry.get("title")):
        errors.append(f"{label}: title must be a nonblank string")
    lifecycle = entry.get("lifecycle")
    if not is_choice(lifecycle, LIFECYCLES):
        errors.append(f"{label}: lifecycle must be one of {', '.join(LIFECYCLES)}")
    reason = entry.get("reason")
    if reason is not None and not isinstance(reason, str):
        errors.append(f"{label}: reason must be a string or null")
    target = entry.get("superseded_by")
    if lifecycle in ("active", "archived") and target is not None:
        errors.append(f"{label}: superseded_by must be null when lifecycle is {lifecycle}")
    if lifecycle in ("archived", "superseded") and not is_nonblank(reason):
        errors.append(f"{label}: lifecycle {lifecycle} needs a nonblank reason")
    if lifecycle == "superseded":
        if not isinstance(target, str):
            errors.append(f"{label}: lifecycle superseded needs superseded_by naming the replacement run")
        elif not RUN_NAME_RE.fullmatch(target):
            errors.append(
                f"{label}: superseded_by {target!r} must be a bare run directory name "
                "under the output root, not a path"
            )
        elif target == name:
            errors.append(f"{label}: superseded_by cannot name the run itself")
        elif target not in v4_names:
            errors.append(
                f"{label}: superseded_by {target!r} is not a v4 run "
                f"(directory with {ASSESSMENT_PATH.as_posix()}) under the output root"
            )
    handoff = entry.get("handoff")
    if handoff is not None:
        handoff_errors, handoff_warnings = check_handoff(run_dir, label, handoff, idea_id)
        errors.extend(handoff_errors)
        warnings.extend(handoff_warnings)
        state = handoff.get("state") if isinstance(handoff, dict) else None
        if lifecycle in ("archived", "superseded") and is_choice(state, OPEN_HANDOFF_STATES):
            warnings.append(
                f"{label}: handoff state {state} on a {lifecycle} run is hidden from the "
                "experiment queue"
            )
    return errors, warnings


def supersede_cycles(edges: Dict[str, str]) -> List[List[str]]:
    cycles = []
    seen: Set[str] = set()
    for start in sorted(edges):
        path: List[str] = []
        position: Dict[str, int] = {}
        node = start
        while node in edges and node not in seen and node not in position:
            position[node] = len(path)
            path.append(node)
            node = edges[node]
        if node in position:
            cycles.append(path[position[node]:])
        seen.update(path)
    return cycles


def load_portfolio(output_root: Path) -> Portfolio:
    portfolio = Portfolio()
    try:
        children = sorted(path for path in output_root.iterdir() if path.is_dir())
    except OSError as exc:
        portfolio.errors.append(f"{output_root}: cannot list output root: {exc}")
        return portfolio
    run_dirs = [path for path in children if (path / ASSESSMENT_PATH).exists()]
    portfolio.v4_names = {path.name for path in run_dirs}
    for path in children:
        if path.name not in portfolio.v4_names and (path / PORTFOLIO_PATH).exists():
            portfolio.errors.append(
                f"{path.name}/{PORTFOLIO_PATH.as_posix()}: portfolio metadata belongs only to "
                f"v4 runs with {ASSESSMENT_PATH.as_posix()}; legacy and support outputs stay unchanged"
            )
    entries: Dict[str, Dict[str, Any]] = {}
    candidates: Dict[str, Run] = {}
    failed: Set[str] = set()
    for run_dir in run_dirs:
        errors: List[str] = []
        assessment = read_json_object(run_dir, ASSESSMENT_PATH, errors)
        if assessment is not None:
            errors.extend(check_assessment(run_dir.name, assessment))
        entry = read_json_object(
            run_dir,
            PORTFOLIO_PATH,
            errors,
            "; every v4 run needs portfolio metadata (schemas/portfolio-entry.schema.json)",
        )
        if entry is not None:
            entries[run_dir.name] = entry
            idea_id = assessment.get("idea_id") if assessment is not None else None
            entry_errors, entry_warnings = check_entry(
                run_dir, entry, idea_id, portfolio.v4_names
            )
            errors.extend(entry_errors)
            portfolio.warnings.extend(entry_warnings)
        if errors or assessment is None or entry is None:
            failed.add(run_dir.name)
        else:
            candidates[run_dir.name] = Run(run_dir.name, assessment, entry)
        portfolio.errors.extend(errors)
    edges = {
        name: entry["superseded_by"]
        for name, entry in entries.items()
        if entry.get("lifecycle") == "superseded"
        and isinstance(entry.get("superseded_by"), str)
        and entry["superseded_by"] in portfolio.v4_names
        and entry["superseded_by"] != name
    }
    for cycle in supersede_cycles(edges):
        chain = " -> ".join(cycle + [cycle[0]])
        portfolio.errors.append(
            f"{cycle[0]}/{PORTFOLIO_PATH.as_posix()}: superseded_by cycle {chain}"
        )
        failed.update(cycle)
    for name, target in sorted(edges.items()):
        if entries.get(target, {}).get("lifecycle") == "archived":
            portfolio.warnings.append(
                f"{name}/{PORTFOLIO_PATH.as_posix()}: replacement {target} is archived"
            )
    portfolio.runs = [run for name, run in sorted(candidates.items()) if name not in failed]
    return portfolio


def md(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def link(text: Any, target: str) -> str:
    label = md(text).replace("[", "\\[").replace("]", "\\]")
    if any(character.isspace() for character in target):
        target = f"<{target}>"
    return f"[{label}]({target})"


def table_row(cells: Sequence[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def table_head(columns: Sequence[str]) -> List[str]:
    return [table_row(columns), "|" + "---|" * len(columns)]


def ordered(runs: Sequence[Run]) -> List[Run]:
    by_name = sorted(runs, key=lambda run: run.name)
    return sorted(by_name, key=lambda run: run.assessment["analysis_date"], reverse=True)


def score_cell(opportunity: Optional[Dict[str, Any]]) -> str:
    if opportunity is None:
        return "—"
    return f"{opportunity['low']} / {opportunity['base']} / {opportunity['high']}"


def render_scoreboard(runs: Sequence[Run]) -> str:
    lines = [GENERATED_NOTE, "", SCOREBOARD_NOTE, ""]
    if not runs:
        lines.append("_Henüz v4.0 araştırma kaydı yok._")
        return "\n".join(lines)
    titles = {run.name: run.entry["title"] for run in runs}
    lines.extend(table_head(SCOREBOARD_COLUMNS))
    for run in ordered(runs):
        assessment, entry = run.assessment, run.entry
        target = entry["superseded_by"]
        handoff = entry["handoff"]
        lines.append(
            table_row(
                [
                    assessment["analysis_date"],
                    md(entry["title"]),
                    MODE_NAMES[assessment["mode"]],
                    ARCHETYPE_NAMES[assessment["primary_archetype"]],
                    score_cell(assessment["opportunity"]),
                    assessment["overall_evidence_grade"],
                    md(assessment["decision"]),
                    md(assessment["stage"]),
                    f"**{md(assessment['status'])}**",
                    entry["lifecycle"],
                    link(titles[target], f"{target}/REPORT.md") if target else "—",
                    md(entry["reason"]) if is_nonblank(entry["reason"]) else "—",
                    handoff["state"] if handoff is not None else NO_HANDOFF,
                    f"v{md(assessment['methodology_version'])}",
                    link("REPORT", f"{run.name}/REPORT.md"),
                ]
            )
        )
    return "\n".join(lines)


def render_queue(runs: Sequence[Run]) -> str:
    active = [run for run in ordered(runs) if run.entry["lifecycle"] == "active"]
    queued = [run for run in active if run.entry["handoff"] is not None]
    unassigned = [run for run in active if run.entry["handoff"] is None]
    lines = [GENERATED_NOTE, "", QUEUE_NOTE, ""]
    if not queued:
        lines.append("_Aktif deney devri yok._")
    else:
        lines.extend(table_head(QUEUE_COLUMNS))
    for run in queued:
        assessment, handoff = run.assessment, run.entry["handoff"]
        plan_path = handoff["plan_path"]
        results = handoff["result_evidence_ids"]
        lines.append(
            table_row(
                [
                    assessment["analysis_date"],
                    link(run.entry["title"], f"{run.name}/REPORT.md"),
                    ARCHETYPE_NAMES[assessment["primary_archetype"]],
                    md(assessment["decision"]),
                    handoff["state"],
                    md(handoff["owner"]),
                    "; ".join(md(item) for item in handoff["prerequisites"]) or "—",
                    md(handoff["next_action"]),
                    link("plan", f"{run.name}/{plan_path}") if plan_path else "—",
                    ", ".join(f"`{md(item)}`" for item in results) or "—",
                ]
            )
        )
    if unassigned:
        names = ", ".join(link(run.entry["title"], f"{run.name}/REPORT.md") for run in unassigned)
        lines.extend(["", f"Deney devri tanımlanmamış aktif kayıtlar (deney sorumlusu atanmadı): {names}"])
    return "\n".join(lines)


def expected_regions(portfolio: Portfolio) -> Dict[str, str]:
    bodies = {SCOREBOARD: render_scoreboard(portfolio.runs), HANDOFF: render_queue(portfolio.runs)}
    return {
        region: f"{marker(region, 'start')}\n\n{body}\n\n{marker(region, 'end')}"
        for region, body in bodies.items()
    }


def fenced_flags(lines: Sequence[str]) -> List[bool]:
    flags = []
    fence: Optional[str] = None
    for line in lines:
        match = FENCE_RE.match(line)
        if fence is None:
            flags.append(bool(match))
            if match:
                fence = match.group(1)
        else:
            flags.append(True)
            if match and match.group(1) == fence:
                fence = None
    return flags


def region_spans(
    lines: Sequence[str], fenced: Sequence[bool]
) -> Tuple[Dict[str, Tuple[int, int]], List[str]]:
    spans: Dict[str, Tuple[int, int]] = {}
    errors = []
    for region in REGIONS:
        start, end = marker(region, "start"), marker(region, "end")
        starts = [i for i, line in enumerate(lines) if not fenced[i] and line.strip() == start]
        ends = [i for i, line in enumerate(lines) if not fenced[i] and line.strip() == end]
        if not starts and not ends:
            continue
        if len(starts) != 1 or len(ends) != 1 or ends[0] < starts[0]:
            errors.append(
                f"{INDEX_NAME}: the {region} region needs exactly one '{start}' line "
                f"followed by one '{end}' line"
            )
            continue
        spans[region] = (starts[0], ends[0])
    if len(spans) == 2:
        (a_start, a_end), (b_start, b_end) = spans[SCOREBOARD], spans[HANDOFF]
        if a_start <= b_end and b_start <= a_end:
            errors.append(f"{INDEX_NAME}: the scoreboard and handoff regions overlap")
    return spans, errors


def is_table_line(line: str) -> bool:
    return line.lstrip().startswith("|")


def table_blocks(
    lines: Sequence[str], fenced: Sequence[bool], excluded: Set[int]
) -> List[Tuple[int, int]]:
    """(first, end) line ranges of pipe tables with a header separator."""
    blocks = []
    index = 0
    usable = [not fenced[i] and i not in excluded for i in range(len(lines))]
    while index < len(lines):
        if not (usable[index] and is_table_line(lines[index])):
            index += 1
            continue
        end = index
        while end < len(lines) and usable[end] and is_table_line(lines[end]):
            end += 1
        if end - index >= 2 and TABLE_SEPARATOR_RE.fullmatch(lines[index + 1].strip()):
            blocks.append((index, end))
        index = end
    return blocks


def table_cells(line: str) -> List[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|") and not body.endswith("\\|"):
        body = body[:-1]
    return [cell.strip() for cell in UNESCAPED_PIPE_RE.split(body)]


def linked_runs(line: str, names: Set[str]) -> List[str]:
    return [name for name in REPORT_LINK_RE.findall(line) if name in names]


def region_lines(spans: Dict[str, Tuple[int, int]]) -> Set[int]:
    return {i for start, end in spans.values() for i in range(start, end + 1)}


def adopt_scoreboard(
    lines: List[str],
    fenced: Sequence[bool],
    excluded: Set[int],
    scoreboard: List[str],
    portfolio: Portfolio,
) -> Tuple[Optional[List[str]], List[str]]:
    """Move the v4 rows of the first unmarked scoreboard table into the region.

    Rows that link no v4 run's REPORT.md (legacy rows) stay verbatim below the region
    under the table's original header. Adoption refuses to drop an authored title.
    """
    titles = {run.name: run.entry["title"] for run in portfolio.runs}
    for start, end in table_blocks(lines, fenced, excluded):
        adopted = [i for i in range(start + 2, end) if linked_runs(lines[i], portfolio.v4_names)]
        if not adopted:
            continue
        errors = []
        header = table_cells(lines[start])
        if "Konu" in header:
            column = header.index("Konu")
            for i in adopted:
                cells = table_cells(lines[i])
                actual = cells[column] if column < len(cells) else ""
                for name in linked_runs(lines[i], portfolio.v4_names):
                    if actual != md(titles[name]):
                        errors.append(
                            f"{INDEX_NAME}:{i + 1}: adopting the unmarked scoreboard would "
                            f"replace title {actual!r} of {name} with portfolio title "
                            f"{titles[name]!r}; align {name}/{PORTFOLIO_PATH.as_posix()} first"
                        )
        if errors:
            return None, errors
        moved = set(adopted)
        kept = [lines[i] for i in range(start + 2, end) if i not in moved]
        replacement = list(scoreboard)
        if kept:
            replacement += ["", lines[start], lines[start + 1], *kept]
        return lines[:start] + replacement + lines[end:], []
    return None, []


def queue_insertion_point(lines: Sequence[str], fenced: Sequence[bool], scoreboard_end: int) -> int:
    """Just after the scoreboard region, or after a table directly following it."""
    index = scoreboard_end + 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines) and not fenced[index] and is_table_line(lines[index]):
        while index < len(lines) and not fenced[index] and is_table_line(lines[index]):
            index += 1
        return index
    return scoreboard_end + 1


def render_index(text: Optional[str], portfolio: Portfolio) -> Tuple[Optional[str], List[str]]:
    """INDEX.md with fresh generated regions, or (None, errors)."""
    regions = {region: body.split("\n") for region, body in expected_regions(portfolio).items()}
    if text is None or not text.strip():
        lines = [INDEX_TITLE, "", *regions[SCOREBOARD], ""]
    else:
        lines = text.split("\n")
        fenced = fenced_flags(lines)
        spans, errors = region_spans(lines, fenced)
        if errors:
            return None, errors
        if SCOREBOARD in spans:
            start, end = spans[SCOREBOARD]
            lines[start : end + 1] = regions[SCOREBOARD]
        else:
            adopted, errors = adopt_scoreboard(
                lines, fenced, region_lines(spans), regions[SCOREBOARD], portfolio
            )
            if errors:
                return None, errors
            if adopted is None:
                while lines and not lines[-1].strip():
                    lines.pop()
                lines += ["", SCOREBOARD_HEADING, "", *regions[SCOREBOARD], ""]
            else:
                lines = adopted
    fenced = fenced_flags(lines)
    spans, errors = region_spans(lines, fenced)
    if errors:
        return None, errors
    if HANDOFF in spans:
        start, end = spans[HANDOFF]
        lines[start : end + 1] = regions[HANDOFF]
    else:
        point = queue_insertion_point(lines, fenced, spans[SCOREBOARD][1])
        lines[point:point] = ["", QUEUE_HEADING, "", *regions[HANDOFF]]
    rendered = "\n".join(lines)
    return (rendered if rendered.endswith("\n") else rendered + "\n"), []


def check_index(text: str, portfolio: Portfolio) -> List[str]:
    lines = text.split("\n")
    fenced = fenced_flags(lines)
    spans, errors = region_spans(lines, fenced)
    marked = {
        region
        for region in REGIONS
        for i, line in enumerate(lines)
        if not fenced[i] and line.strip() in (marker(region, "start"), marker(region, "end"))
    }
    for region in REGIONS:
        if region not in marked:
            errors.append(
                f"{INDEX_NAME}: missing generated {region} region "
                f"({marker(region, 'start')} ... {marker(region, 'end')}); run {RENDER_COMMAND}"
            )
    if not portfolio.errors:
        # With broken runs the expected regions are unknown; those errors are reported.
        expected = expected_regions(portfolio)
        for region, (start, end) in sorted(spans.items()):
            if "\n".join(lines[start : end + 1]) != expected[region]:
                errors.append(f"{INDEX_NAME}: generated {region} region is stale; run {RENDER_COMMAND}")
    for start, end in table_blocks(lines, fenced, region_lines(spans)):
        for i in range(start + 2, end):
            for name in linked_runs(lines[i], portfolio.v4_names):
                errors.append(
                    f"{INDEX_NAME}:{i + 1}: scoreboard row for v4 run {name} is outside the "
                    f"generated region; remove it and run {RENDER_COMMAND}"
                )
    return errors


def read_index(path: Path) -> Tuple[Optional[str], Optional[str]]:
    try:
        return path.read_text(encoding="utf-8"), None
    except FileNotFoundError:
        return None, None
    except OSError as exc:
        return None, f"{INDEX_NAME}: cannot read: {exc}"
    except UnicodeDecodeError as exc:
        return None, f"{INDEX_NAME}: not UTF-8: {exc}"


def validate_portfolio(output_root: Path) -> Tuple[List[str], List[str]]:
    """(errors, warnings) for every run's portfolio metadata and INDEX.md freshness."""
    portfolio = load_portfolio(output_root)
    errors = list(portfolio.errors)
    text, read_error = read_index(output_root / INDEX_NAME)
    if read_error is not None:
        errors.append(read_error)
    elif text is None:
        errors.append(f"{INDEX_NAME}: missing file; run {RENDER_COMMAND}")
    else:
        errors.extend(check_index(text, portfolio))
    return errors, list(portfolio.warnings)


def print_result(label: str, errors: Sequence[str], warnings: Sequence[str]) -> None:
    print(f"{'FAIL' if errors else 'PASS'} {label}")
    for warning in warnings:
        print(f"  WARN: {warning}")
    for error in errors:
        print(f"  ERROR: {error}")


def command_render(output_root: Path) -> int:
    index_path = output_root / INDEX_NAME
    label = f"{index_path} (portfolio)"
    portfolio = load_portfolio(output_root)
    if portfolio.errors:
        print_result(label, portfolio.errors, portfolio.warnings)
        print(f"{index_path} not written: fix the portfolio errors first")
        return 1
    text, read_error = read_index(index_path)
    if read_error is not None:
        print_result(label, [read_error], portfolio.warnings)
        return 1
    rendered, errors = render_index(text, portfolio)
    if rendered is None:
        print_result(label, errors, portfolio.warnings)
        print(f"{index_path} not written: fix INDEX.md first")
        return 1
    if rendered == text:
        print(f"UNCHANGED {index_path}")
    else:
        try:
            index_path.write_text(rendered, encoding="utf-8")
        except OSError as exc:
            print_result(label, [f"{INDEX_NAME}: cannot write: {exc}"], portfolio.warnings)
            return 1
        print(f"WROTE {index_path}")
    errors = check_index(rendered, portfolio)
    print_result(label, errors, portfolio.warnings)
    return 1 if errors else 0


def command_validate(output_root: Path) -> int:
    errors, warnings = validate_portfolio(output_root)
    print_result(f"{output_root / INDEX_NAME} (portfolio)", errors, warnings)
    return 1 if errors else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    render_parser = subparsers.add_parser(
        "render", help="regenerate the INDEX.md scoreboard and experiment-queue regions"
    )
    render_parser.add_argument("output_root", type=Path, nargs="?", default=Path("output"))
    validate_parser = subparsers.add_parser(
        "validate", help="validate every v4 run's portfolio.json and INDEX.md freshness"
    )
    validate_parser.add_argument("output_root", type=Path, nargs="?", default=Path("output"))
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "render":
        return command_render(args.output_root)
    if args.command == "validate":
        return command_validate(args.output_root)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
