import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import portfolio_tool  # noqa: E402


ALPHA = "2026-07-10-us-alpha"
BETA = "2026-07-10-us-beta"
GAMMA_QUICK = "2026-07-12-us-gamma-quick"
GAMMA_DEEP = "2026-07-12-us-gamma-deep"
DELTA = "2026-07-08-us-delta"
EPSILON = "2026-07-09-us-epsilon"
LEGACY = "2026-03-12-legacy-app"
SUPPORT = "2026-07-16-support-report"
PLAN = "phases/06-prebuild-plan.md"
SCOREBOARD = portfolio_tool.SCOREBOARD
HANDOFF = portfolio_tool.HANDOFF


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def assessment(
    idea_id,
    analysis_date,
    mode="quick",
    archetype="consumer_utility",
    scores=(40, 55, 70),
    grade="C",
    decision="TESTE_DEGER",
    status="PREBUILD_PENDING",
):
    opportunity = None
    if scores is not None:
        low, base, high = scores
        opportunity = {"low": low, "base": base, "high": high, "classification": "borderline"}
    return {
        "methodology_version": "4.0",
        "idea_id": idea_id,
        "analysis_date": analysis_date,
        "mode": mode,
        "stage": "desk_research",
        "primary_archetype": archetype,
        "opportunity": opportunity,
        "overall_evidence_grade": grade,
        "decision": decision,
        "status": status,
    }


def handoff(
    state="ready",
    owner="Kurucu (atanmadi)",
    prerequisites=(),
    next_action="Deneyi baslat",
    plan_path=PLAN,
    results=(),
):
    return {
        "owner": owner,
        "state": state,
        "prerequisites": list(prerequisites),
        "next_action": next_action,
        "plan_path": plan_path,
        "result_evidence_ids": list(results),
    }


def entry(title, lifecycle="active", superseded_by=None, reason=None, handoff_value=None):
    return {
        "title": title,
        "lifecycle": lifecycle,
        "superseded_by": superseded_by,
        "reason": reason,
        "handoff": handoff_value,
    }


def result_record(
    evidence_id,
    idea_id="alpha",
    source_type="experiment",
    status="observed",
    source_ref="experiments/e1-results.csv",
):
    return {
        "evidence_id": evidence_id,
        "claim_id": f"{idea_id}-value",
        "idea_id": idea_id,
        "source_type": source_type,
        "status": status,
        "source_ref": source_ref,
        "artifact_path": None,
        "observation": "Observed experiment result",
    }


def write_records(root, name, records):
    (root / name / "data" / "evidence.jsonl").write_text(
        "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8"
    )


def write_run(root, name, assessment_value, entry_value):
    run = root / name
    write_json(run / "data" / "assessment.json", assessment_value)
    write_json(run / "data" / "portfolio.json", entry_value)
    write_records(root, name, [])
    (run / "phases").mkdir()
    (run / PLAN).write_text("# Plan\n\nowner: Kurucu (tek gelistirici)\n", encoding="utf-8")
    (run / "REPORT.md").write_text("# Report\n", encoding="utf-8")


def build_root(base):
    """Five v4 runs (active, active without handoff, superseded, archived), legacy, support."""
    root = base / "output"
    write_run(
        root,
        ALPHA,
        assessment("alpha", "2026-07-10"),
        entry(
            "US Alpha",
            handoff_value=handoff(
                "blocked",
                prerequisites=["Apple Search Popularity export"],
                next_action="Export gelince Kapi 1'i ac",
            ),
        ),
    )
    write_run(
        root,
        BETA,
        assessment("beta", "2026-07-10", archetype="b2b_prosumer", scores=(70, 80, 90)),
        entry("US Beta | Pro"),
    )
    write_run(
        root,
        GAMMA_QUICK,
        assessment("gamma", "2026-07-12"),
        entry(
            "US Gamma",
            "superseded",
            GAMMA_DEEP,
            "Ayni gun Deep analizle supersede edildi",
            handoff("not_planned", next_action="Quick concierge testi calistirilmaz", plan_path=None),
        ),
    )
    write_run(
        root,
        GAMMA_DEEP,
        assessment(
            "gamma-deep",
            "2026-07-12",
            mode="deep",
            grade="D",
            decision="BELIRSIZ",
            status="DESK_RESEARCH_COMPLETE",
        ),
        entry("US Gamma", handoff_value=handoff("ready", next_action="Concierge kohortunu ac")),
    )
    write_run(
        root,
        DELTA,
        assessment("delta", "2026-07-08", scores=None, decision="ELENDIR", status="KILLED"),
        entry("US Delta", "archived", reason="Fiziksel workflow kurucu kisitina uymuyor"),
    )
    (root / LEGACY).mkdir()
    (root / LEGACY / "REPORT.md").write_text("# Legacy\n", encoding="utf-8")
    write_json(root / SUPPORT / "artifact.json", {"kind": "compare"})
    return root


def edit_entry(root, name, edit):
    path = root / name / "data" / "portfolio.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    edit(value)
    write_json(path, value)


def edit_assessment(root, name, edit):
    path = root / name / "data" / "assessment.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    edit(value)
    write_json(path, value)


def run_cli(*args):
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        code = portfolio_tool.main([str(arg) for arg in args])
    return code, stdout.getvalue()


def region(text, name):
    start = text.index(portfolio_tool.marker(name, "start"))
    end = text.index(portfolio_tool.marker(name, "end"))
    return text[start:end]


INDEX_HEAD = (
    "# Arastirma Scoreboard\n\n"
    "> v4.0 satirlari yalniz ayni metodoloji surumu icinde karsilastirilir.\n\n"
)
V4_HEADER = "| Tarih | Konu | Mod | Arketip | Firsat Skoru | Kanit | Karar | Asama | Durum | Metodoloji | Rapor |"
SEPARATOR = "|---|---|---|---|---|---|---|---|---|---|---|"
LEGACY_ROW = (
    "| 2026-03-12 | Legacy App | Quick Scan | — | — | — | NO-GO (tarihsel) | legacy | "
    f"**LEGACY** | v3.1 | [REPORT]({LEGACY}/REPORT.md) |"
)
INDEX_TAIL = (
    "## Compare Turlari\n\n"
    "| Tarih | Compare | Portable artifact |\n|---|---|---|\n"
    f"| 2026-07-16 | [Support]({SUPPORT}/REPORT.md) | [artifact]({SUPPORT}/artifact.json) |\n\n"
    "## Faz 5.5 Sozlesmeleri\n\n| Fikir | Sozlesme |\n|---|---|\n"
    f"| US Alpha | [06-prebuild-plan]({ALPHA}/{PLAN}) |\n\n"
    "## Tarihsel Notlar\n\n- Elle yazilmis not aynen korunur.\n"
)


def unmarked_index(alpha_title="US Alpha"):
    """Hand-maintained scoreboard: unsorted v4 rows, a stale status, then a legacy row."""
    rows = [
        f"| 2026-07-10 | US Beta \\| Pro | Quick Scan | B2B/Prosumer | 70 / 80 / 90 | C | TESTE_DEGER | desk_research | **PREBUILD_PENDING** | v4.0 | [REPORT]({BETA}/REPORT.md) |",
        f"| 2026-07-12 | US Gamma | Deep | Consumer Utility | 40 / 55 / 70 | D | BELIRSIZ | desk_research | **DESK_RESEARCH_COMPLETE** | v4.0 | [REPORT]({GAMMA_DEEP}/REPORT.md) |",
        f"| 2026-07-12 | US Gamma | Quick Scan | Consumer Utility | 40 / 55 / 70 | C | TESTE_DEGER | desk_research | **ARCHIVED** | v4.0 | [REPORT]({GAMMA_QUICK}/REPORT.md) |",
        f"| 2026-07-10 | {alpha_title} | Quick Scan | Consumer Utility | 40 / 55 / 70 | C | TESTE_DEGER | desk_research | **PREBUILD_PENDING** | v4.0 | [REPORT]({ALPHA}/REPORT.md) |",
        f"| 2026-07-08 | US Delta | Quick Scan | Consumer Utility | — | C | ELENDIR | desk_research | **KILLED** | v4.0 | [REPORT]({DELTA}/REPORT.md) |",
        LEGACY_ROW,
    ]
    return INDEX_HEAD + "\n".join([V4_HEADER, SEPARATOR, *rows]) + "\n\n" + INDEX_TAIL


class PortfolioTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = build_root(Path(self.tmp.name))
        self.index = self.root / "INDEX.md"

    def fresh_root(self):
        return build_root(Path(tempfile.mkdtemp(dir=self.tmp.name)))

    def load_errors(self, root=None):
        return portfolio_tool.load_portfolio(root or self.root).errors

    def assert_error(self, name, fragment, errors):
        self.assertTrue(
            any(error.startswith(f"{name}/") and fragment in error for error in errors),
            f"no {name} error containing {fragment!r}: {errors}",
        )

    def render(self, root=None):
        code, output = run_cli("render", root or self.root)
        self.assertEqual(code, 0, output)
        return ((root or self.root) / "INDEX.md").read_text(encoding="utf-8")


class RenderTests(PortfolioTestCase):
    def test_fixture_is_valid_without_warnings(self):
        portfolio = portfolio_tool.load_portfolio(self.root)
        self.assertEqual(portfolio.errors, [])
        self.assertEqual(portfolio.warnings, [])
        self.assertEqual(
            [run.name for run in portfolio.runs], sorted([ALPHA, BETA, GAMMA_QUICK, GAMMA_DEEP, DELTA])
        )

    def test_render_creates_index_and_rerender_is_identical(self):
        text = self.render()
        regions = portfolio_tool.expected_regions(portfolio_tool.load_portfolio(self.root))
        self.assertEqual(
            text,
            f"{portfolio_tool.INDEX_TITLE}\n\n{regions[SCOREBOARD]}\n\n"
            f"{portfolio_tool.QUEUE_HEADING}\n\n{regions[HANDOFF]}\n",
        )
        code, output = run_cli("render", self.root)
        self.assertEqual(code, 0, output)
        self.assertIn("UNCHANGED", output)
        self.assertEqual(self.index.read_text(encoding="utf-8"), text)
        self.assertEqual(portfolio_tool.validate_portfolio(self.root), ([], []))
        code, output = run_cli("validate", self.root)
        self.assertEqual(code, 0, output)
        self.assertIn(f"PASS {self.index} (portfolio)", output)

    def test_render_never_touches_run_files(self):
        paths = sorted(path for path in self.root.rglob("*") if path.is_file())
        before = {path: path.read_bytes() for path in paths}
        self.render()
        self.assertEqual({path: path.read_bytes() for path in paths}, before)

    def test_scoreboard_sorts_by_date_then_directory_not_score(self):
        scoreboard = region(self.render(), SCOREBOARD)
        positions = [
            scoreboard.index(f"[REPORT]({name}/REPORT.md)")
            for name in (GAMMA_DEEP, GAMMA_QUICK, ALPHA, BETA, DELTA)
        ]
        self.assertEqual(positions, sorted(positions))

    def test_scoreboard_separates_lifecycle_from_research_status(self):
        lines = region(self.render(), SCOREBOARD).split("\n")
        quick = next(line for line in lines if f"[REPORT]({GAMMA_QUICK}/REPORT.md)" in line)
        archived = next(line for line in lines if f"[REPORT]({DELTA}/REPORT.md)" in line)
        self.assertIn("| **PREBUILD_PENDING** | superseded |", quick)
        self.assertIn(f"[US Gamma]({GAMMA_DEEP}/REPORT.md)", quick)
        self.assertIn("| **KILLED** | archived |", archived)
        self.assertTrue(any(line.startswith("| 2026-07-10 | US Beta \\| Pro |") for line in lines))

    def test_queue_shows_only_active_runs_with_handoff(self):
        queue = region(self.render(), HANDOFF)
        lines = queue.split("\n")
        self.assertIn(
            f"| 2026-07-10 | [US Alpha]({ALPHA}/REPORT.md) | Consumer Utility | TESTE_DEGER | blocked "
            "| Kurucu (atanmadi) | Apple Search Popularity export | Export gelince Kapi 1'i ac "
            f"| [plan]({ALPHA}/{PLAN}) | — |",
            lines,
        )
        self.assertLess(queue.index(f"({GAMMA_DEEP}/REPORT.md)"), queue.index(f"({ALPHA}/REPORT.md)"))
        self.assertNotIn(GAMMA_QUICK, queue)
        self.assertNotIn(DELTA, queue)
        self.assertIn(f"[US Beta \\| Pro]({BETA}/REPORT.md)", queue)

    def test_superseded_replacement_follows_metadata(self):
        self.render()
        edit_entry(self.root, GAMMA_QUICK, lambda value: value.update(superseded_by=ALPHA))
        errors, _ = portfolio_tool.validate_portfolio(self.root)
        self.assertIn(
            f"INDEX.md: generated scoreboard region is stale; run {portfolio_tool.RENDER_COMMAND}",
            errors,
        )
        scoreboard = region(self.render(), SCOREBOARD)
        self.assertIn(f"| superseded | [US Alpha]({ALPHA}/REPORT.md) |", scoreboard)
        self.assertEqual(portfolio_tool.validate_portfolio(self.root), ([], []))

    def test_open_handoff_on_superseded_run_is_hidden_with_warning(self):
        edit_entry(self.root, GAMMA_QUICK, lambda value: value["handoff"].update(state="ready"))
        portfolio = portfolio_tool.load_portfolio(self.root)
        self.assertEqual(portfolio.errors, [])
        self.assertTrue(any("hidden from the experiment queue" in item for item in portfolio.warnings))
        self.assertNotIn(GAMMA_QUICK, region(self.render(), HANDOFF))

    def test_cli_defaults_to_output_root(self):
        parser = portfolio_tool.build_parser()
        self.assertEqual(parser.parse_args(["render"]).output_root, Path("output"))
        self.assertEqual(parser.parse_args(["validate"]).output_root, Path("output"))


class IndexTests(PortfolioTestCase):
    def test_first_render_adopts_unmarked_scoreboard_losslessly(self):
        original = unmarked_index()
        self.index.write_text(original, encoding="utf-8")
        text = self.render()
        regions = portfolio_tool.expected_regions(portfolio_tool.load_portfolio(self.root))
        self.assertEqual(
            text,
            INDEX_HEAD
            + regions[SCOREBOARD]
            + f"\n\n{V4_HEADER}\n{SEPARATOR}\n{LEGACY_ROW}\n\n"
            + f"{portfolio_tool.QUEUE_HEADING}\n\n{regions[HANDOFF]}\n\n"
            + INDEX_TAIL,
        )
        self.assertNotIn("**ARCHIVED**", text)
        self.assertEqual(portfolio_tool.validate_portfolio(self.root), ([], []))
        self.assertEqual(self.render(), text)

    def test_adoption_refuses_to_drop_an_authored_title(self):
        original = unmarked_index(alpha_title="US Alpha (eski ad)")
        self.index.write_text(original, encoding="utf-8")
        code, output = run_cli("render", self.root)
        self.assertEqual(code, 1)
        self.assertIn("would replace title 'US Alpha (eski ad)'", output)
        self.assertEqual(self.index.read_text(encoding="utf-8"), original)

    def test_stale_regions_detected_and_manual_text_preserved(self):
        self.render()
        manual = "\n## Notlar\n\nElle yazilmis not.\n"
        with self.index.open("a", encoding="utf-8") as handle:
            handle.write(manual)
        self.assertEqual(portfolio_tool.validate_portfolio(self.root), ([], []))

        edit_assessment(
            self.root,
            ALPHA,
            lambda value: value["opportunity"].update(low=41, base=56, high=71),
        )
        errors, _ = portfolio_tool.validate_portfolio(self.root)
        self.assertIn(
            f"INDEX.md: generated scoreboard region is stale; run {portfolio_tool.RENDER_COMMAND}",
            errors,
        )
        self.assertFalse(any("handoff region is stale" in error for error in errors), errors)
        code, output = run_cli("validate", self.root)
        self.assertEqual(code, 1, output)

        text = self.render()
        self.assertTrue(text.endswith(manual))
        self.assertIn("| 41 / 56 / 71 |", text)
        self.assertEqual(portfolio_tool.validate_portfolio(self.root), ([], []))

        self.index.write_text(
            text.replace("Concierge kohortunu ac", "Elle degistirildi"), encoding="utf-8"
        )
        errors, _ = portfolio_tool.validate_portfolio(self.root)
        self.assertIn(
            f"INDEX.md: generated handoff region is stale; run {portfolio_tool.RENDER_COMMAND}",
            errors,
        )
        self.assertEqual(self.render(), text)

    def test_v4_row_outside_generated_region_is_error(self):
        text = self.render()
        self.index.write_text(
            text
            + "\n| Tarih | Rapor |\n|---|---|\n"
            + f"| 2026-07-10 | [REPORT]({ALPHA}/REPORT.md) |\n",
            encoding="utf-8",
        )
        errors, _ = portfolio_tool.validate_portfolio(self.root)
        self.assertTrue(
            any(f"scoreboard row for v4 run {ALPHA} is outside" in error for error in errors), errors
        )

    def test_malformed_markers_block_render(self):
        text = self.render()
        broken = text + portfolio_tool.marker(SCOREBOARD, "start") + "\n"
        self.index.write_text(broken, encoding="utf-8")
        errors, _ = portfolio_tool.validate_portfolio(self.root)
        self.assertTrue(any("scoreboard region needs exactly one" in error for error in errors), errors)
        self.assertFalse(any("missing generated scoreboard" in error for error in errors), errors)
        code, _ = run_cli("render", self.root)
        self.assertEqual(code, 1)
        self.assertEqual(self.index.read_text(encoding="utf-8"), broken)

    def test_missing_index_is_validation_error(self):
        errors, _ = portfolio_tool.validate_portfolio(self.root)
        self.assertIn(f"INDEX.md: missing file; run {portfolio_tool.RENDER_COMMAND}", errors)


class MetadataTests(PortfolioTestCase):
    def test_missing_metadata_on_v4_run_is_error_and_legacy_support_untouched(self):
        (self.root / BETA / "data" / "portfolio.json").unlink()
        errors = self.load_errors()
        self.assert_error(BETA, "missing file; every v4 run needs portfolio metadata", errors)
        self.assertFalse(any(LEGACY in error or SUPPORT in error for error in errors), errors)
        code, output = run_cli("render", self.root)
        self.assertEqual(code, 1, output)
        self.assertFalse(self.index.exists())

        write_json(self.root / LEGACY / "data" / "portfolio.json", entry("Legacy App"))
        self.assert_error(LEGACY, "belongs only to v4 runs", self.load_errors())

    def test_exact_fields(self):
        cases = {
            "unknown top-level": (lambda value: value.update(status="ARCHIVED"), "unknown field(s): status"),
            "missing top-level": (lambda value: value.pop("reason"), "missing required field(s): reason"),
            "unknown handoff": (
                lambda value: value["handoff"].update(date="2026-11-01"),
                "handoff unknown field(s): date",
            ),
            "missing handoff": (
                lambda value: value["handoff"].pop("plan_path"),
                "handoff missing required field(s): plan_path",
            ),
            "blank title": (lambda value: value.update(title="  "), "title must be a nonblank string"),
            "blank owner": (lambda value: value["handoff"].update(owner=""), "handoff.owner must be"),
            "blank next action": (
                lambda value: value["handoff"].update(next_action=" "),
                "handoff.next_action must be",
            ),
            "bad state": (lambda value: value["handoff"].update(state="done"), "handoff.state must be"),
        }
        for label, (edit, fragment) in cases.items():
            with self.subTest(label):
                root = self.fresh_root()
                edit_entry(root, ALPHA, edit)
                self.assert_error(ALPHA, fragment, self.load_errors(root))

    def test_lifecycle_rules(self):
        cases = {
            "archived without reason": (DELTA, {"reason": None}, "lifecycle archived needs a nonblank reason"),
            "archived with replacement": (
                DELTA,
                {"superseded_by": GAMMA_DEEP},
                "superseded_by must be null when lifecycle is archived",
            ),
            "active with replacement": (
                ALPHA,
                {"superseded_by": GAMMA_DEEP},
                "superseded_by must be null when lifecycle is active",
            ),
            "superseded blank reason": (
                GAMMA_QUICK,
                {"reason": "  "},
                "lifecycle superseded needs a nonblank reason",
            ),
            "research status as lifecycle": (ALPHA, {"lifecycle": "ARCHIVED"}, "lifecycle must be one of"),
        }
        for label, (name, changes, fragment) in cases.items():
            with self.subTest(label):
                root = self.fresh_root()
                edit_entry(root, name, lambda value: value.update(changes))
                self.assert_error(name, fragment, self.load_errors(root))

    def test_superseded_target_must_be_another_v4_run(self):
        cases = {
            "missing target": ("2026-07-12-us-missing", "is not a v4 run"),
            "self": (GAMMA_QUICK, "cannot name the run itself"),
            "parent traversal": (f"../{GAMMA_DEEP}", "must be a bare run directory name"),
            "nested traversal": (f"{GAMMA_DEEP}/../{ALPHA}", "must be a bare run directory name"),
            "absolute path": (f"/tmp/{GAMMA_DEEP}", "must be a bare run directory name"),
            "legacy target": (LEGACY, "is not a v4 run"),
            "support target": (SUPPORT, "is not a v4 run"),
            "null target": (None, "needs superseded_by naming the replacement run"),
        }
        for label, (target, fragment) in cases.items():
            with self.subTest(label):
                root = self.fresh_root()
                edit_entry(root, GAMMA_QUICK, lambda value: value.update(superseded_by=target))
                self.assert_error(GAMMA_QUICK, fragment, self.load_errors(root))

    def test_superseded_cycle_is_error(self):
        edit_entry(
            self.root,
            GAMMA_DEEP,
            lambda value: value.update(
                lifecycle="superseded", superseded_by=GAMMA_QUICK, reason="Quick yeniden acildi"
            ),
        )
        errors = self.load_errors()
        self.assert_error(
            GAMMA_DEEP,
            f"superseded_by cycle {GAMMA_DEEP} -> {GAMMA_QUICK} -> {GAMMA_DEEP}",
            errors,
        )
        code, output = run_cli("render", self.root)
        self.assertEqual(code, 1, output)
        self.assertFalse(self.index.exists())

    def test_blocked_handoff_needs_prerequisites(self):
        edit_entry(self.root, ALPHA, lambda value: value["handoff"].update(prerequisites=[]))
        self.assert_error(ALPHA, "a blocked handoff needs at least one prerequisite", self.load_errors())

    def test_completed_handoff_needs_observed_first_party_or_experiment_results(self):
        cases = {
            "no results": ([], [], "a completed handoff needs result_evidence_ids"),
            "unknown record": (["exp-1"], [], "'exp-1' is not in data/evidence.jsonl"),
            "desk research record": (
                ["exp-1"],
                [result_record("exp-1", source_type="official_primary")],
                "needs first_party or experiment results",
            ),
            "not observed": (
                ["exp-1"],
                [result_record("exp-1", status="not_found_after_protocol")],
                "is not an observed result",
            ),
            "other idea": (["exp-1"], [result_record("exp-1", idea_id="beta")], "belongs to idea 'beta'"),
            "no reference": (
                ["exp-1"],
                [result_record("exp-1", source_ref=None)],
                "result needs a nonblank source_ref or artifact_path",
            ),
            "duplicate ids": (["exp-1", "exp-1"], [result_record("exp-1")], "repeats exp-1"),
        }
        for label, (results, records, fragment) in cases.items():
            with self.subTest(label):
                root = self.fresh_root()
                write_records(root, ALPHA, records)
                edit_entry(
                    root,
                    ALPHA,
                    lambda value: value["handoff"].update(state="completed", result_evidence_ids=results),
                )
                self.assert_error(ALPHA, fragment, self.load_errors(root))

    def test_completed_handoff_with_real_result_renders(self):
        write_records(self.root, ALPHA, [result_record("exp-1")])
        edit_entry(
            self.root,
            ALPHA,
            lambda value: value["handoff"].update(state="completed", result_evidence_ids=["exp-1"]),
        )
        self.assertEqual(self.load_errors(), [])
        queue = region(self.render(), HANDOFF)
        self.assertIn("| completed |", queue)
        self.assertIn("| `exp-1` |", queue)

    def test_in_progress_handoff_may_cite_observed_partial_result(self):
        write_records(self.root, ALPHA, [result_record("smoke-1", source_type="local_artifact")])
        edit_entry(
            self.root,
            ALPHA,
            lambda value: value["handoff"].update(state="in_progress", result_evidence_ids=["smoke-1"]),
        )
        self.assertEqual(self.load_errors(), [])

    def test_plan_path_must_be_safe_existing_file_in_run(self):
        os.symlink(self.root / BETA / PLAN, self.root / ALPHA / "phases" / "link.md")
        cases = {
            "absolute": ("/etc/hosts", "must be null or a relative path"),
            "parent traversal": (f"../{BETA}/{PLAN}", "must be null or a relative path"),
            "inner traversal": ("phases/../../x.md", "must be null or a relative path"),
            "backslash": ("phases\\06-prebuild-plan.md", "must be null or a relative path"),
            "missing file": ("phases/missing.md", "is not an existing file in the run directory"),
            "directory": ("phases", "is not an existing file in the run directory"),
            "symlink escape": ("phases/link.md", "escapes the run directory"),
        }
        for label, (plan_path, fragment) in cases.items():
            with self.subTest(label):
                edit_entry(self.root, ALPHA, lambda value: value["handoff"].update(plan_path=plan_path))
                self.assert_error(ALPHA, fragment, self.load_errors())

    def test_owner_role_must_come_from_plan(self):
        edit_entry(self.root, ALPHA, lambda value: value["handoff"].update(owner="Pazarlama ekibi"))
        portfolio = portfolio_tool.load_portfolio(self.root)
        self.assertEqual(portfolio.errors, [])
        self.assertTrue(
            any("owner role 'Pazarlama ekibi' does not appear" in item for item in portfolio.warnings),
            portfolio.warnings,
        )

    def test_malformed_files_are_reported_per_run_without_traceback(self):
        (self.root / BETA / "data" / "portfolio.json").write_text("{not json", encoding="utf-8")
        (self.root / GAMMA_DEEP / "data" / "assessment.json").write_text("[]", encoding="utf-8")
        write_json(
            self.root / ALPHA / "data" / "portfolio.json",
            {"title": 5, "lifecycle": ["active"], "superseded_by": {"x": 1}, "reason": 3, "handoff": "x"},
        )
        edit_assessment(self.root, DELTA, lambda value: value.update(opportunity="high", analysis_date=20260708))
        (self.root / GAMMA_QUICK / "data" / "evidence.jsonl").write_text(
            "{broken\n" + json.dumps(result_record("exp-2", idea_id="gamma")) + "\n", encoding="utf-8"
        )
        edit_entry(
            self.root,
            GAMMA_QUICK,
            lambda value: value["handoff"].update(state="completed", result_evidence_ids=["exp-1"]),
        )
        write_run(self.root, EPSILON, assessment("epsilon", "2026-07-09"), entry("US Epsilon"))
        (self.root / EPSILON / "data" / "portfolio.json").write_text("[" * 100000, encoding="utf-8")

        errors, _ = portfolio_tool.validate_portfolio(self.root)
        self.assert_error(BETA, "invalid JSON", errors)
        self.assert_error(GAMMA_DEEP, "JSON root must be an object", errors)
        self.assert_error(ALPHA, "title must be a nonblank string", errors)
        self.assert_error(ALPHA, "lifecycle must be one of", errors)
        self.assert_error(ALPHA, "reason must be a string or null", errors)
        self.assert_error(ALPHA, "handoff must be an object or null", errors)
        self.assert_error(DELTA, "analysis_date must be an ISO date", errors)
        self.assert_error(DELTA, "opportunity must be null or have integer low/base/high", errors)
        self.assert_error(GAMMA_QUICK, "evidence.jsonl:1: invalid JSON", errors)
        self.assert_error(GAMMA_QUICK, "'exp-1' is not in data/evidence.jsonl", errors)
        self.assert_error(EPSILON, "invalid JSON", errors)

        code, output = run_cli("validate", self.root)
        self.assertEqual(code, 1)
        self.assertNotIn("Traceback", output)
        self.assertIn(f"FAIL {self.index} (portfolio)", output)
        code, output = run_cli("render", self.root)
        self.assertEqual(code, 1)
        self.assertIn("not written", output)
        self.assertFalse(self.index.exists())




if __name__ == "__main__":
    unittest.main()
