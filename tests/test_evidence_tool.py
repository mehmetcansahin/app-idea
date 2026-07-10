import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import evidence_tool  # noqa: E402


def evidence(evidence_id, claim_id, level, root, source_type="official_primary"):
    return {
        "evidence_id": evidence_id,
        "claim_id": claim_id,
        "idea_id": "fixture-app",
        "phase": "5",
        "source_type": source_type,
        "source_title": evidence_id,
        "source_url": f"https://example.com/{evidence_id}",
        "source_ref": None,
        "artifact_path": None,
        "independence_root": root,
        "collected_at": "2026-07-10",
        "data_period": "2026",
        "geo": "US",
        "storefront": "US",
        "platform": "iOS",
        "status": "observed",
        "observation": f"Observed evidence for {claim_id}",
        "value": 1,
        "unit": "signal",
        "evidence_level": level,
        "observation_quality": "direct",
        "claim_relevance": "direct",
        "direction": "supports",
        "sample_n": None,
        "denominator": None,
        "limitations": [],
        "search_queries": [],
        "attempted_sources": [],
    }


def valid_records():
    records = []
    for claim in ("claim-demand", "claim-economics", "claim-wedge"):
        records.append(evidence(f"{claim}-behavior", claim, "E3", f"{claim}-behavior-root"))
        records.append(evidence(f"{claim}-metric", claim, "E2", f"{claim}-metric-root"))
    for code in ("legal", "feasibility", "platform", "safety"):
        records.append(evidence(f"gate-{code}", f"claim-gate-{code}", "E2", f"gate-{code}-root"))
    return records


def valid_assessment(mode="quick"):
    dimension = {"low": 3, "base": 3, "high": 3, "claim_ids": ["claim-demand"]}
    return {
        "methodology_version": "4.0",
        "idea_id": "fixture-app",
        "analysis_date": "2026-07-10",
        "mode": mode,
        "stage": "desk_research",
        "target_segment": "US consumers",
        "target_geos": ["US"],
        "primary_archetype": "consumer_utility",
        "risk_modifiers": [],
        "dimensions": {
            "problem_demand": copy.deepcopy(dimension),
            "monetization_economics": {**copy.deepcopy(dimension), "claim_ids": ["claim-economics"]},
            "competitive_wedge": {**copy.deepcopy(dimension), "claim_ids": ["claim-wedge"]},
            "distribution_access": copy.deepcopy(dimension),
            "repeat_value_retention": {**copy.deepcopy(dimension), "claim_ids": ["claim-economics"]},
            "timing": {**copy.deepcopy(dimension), "claim_ids": ["claim-wedge"]},
            "liquidity_cold_start": None,
        },
        "opportunity": {"low": 60, "base": 60, "high": 60, "classification": "attractive"},
        "fatal_gates": [
            {"code": "LEGAL_BLOCKED", "status": "clear", "evidence_ids": ["gate-legal"]},
            {"code": "CORE_FEASIBILITY_BLOCKED", "status": "clear", "evidence_ids": ["gate-feasibility"]},
            {"code": "PLATFORM_BLOCKED", "status": "clear", "evidence_ids": ["gate-platform"]},
            {"code": "SAFETY_ETHICS_BLOCKED", "status": "clear", "evidence_ids": ["gate-safety"]},
        ],
        "riskiest_assumptions": [
            {
                "claim_id": "claim-demand",
                "category": "value",
                "impact": 3,
                "uncertainty": 3,
                "claim_grade": "B",
                "product_specific_behavior": False,
                "disposition": "supported",
            },
            {
                "claim_id": "claim-economics",
                "category": "business_viability",
                "impact": 3,
                "uncertainty": 2,
                "claim_grade": "B",
                "product_specific_behavior": False,
                "disposition": "supported",
            },
            {
                "claim_id": "claim-wedge",
                "category": "usability",
                "impact": 2,
                "uncertainty": 3,
                "claim_grade": "B",
                "product_specific_behavior": False,
                "disposition": "partial",
            },
        ],
        "overall_evidence_grade": "B",
        "decision": "TEST_ONCELIKLI",
        "status": "PREBUILD_PENDING",
        "next_test": "Run a refundable-deposit test",
        "stopping_rule": "Close after the preregistered sample target",
        "post_mvp_result": None,
    }


def write_output(root, mode="quick"):
    output_dir = root / f"fixture-{mode}"
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True)
    records = valid_records()
    (data_dir / "evidence.jsonl").write_text(
        "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n",
        encoding="utf-8",
    )
    assessment = valid_assessment(mode)
    (data_dir / "assessment.json").write_text(
        json.dumps(assessment, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (data_dir / "evidence-ledger.md").write_text(
        evidence_tool.render_ledger(records), encoding="utf-8"
    )
    (output_dir / "REPORT.md").write_text(
        "# Fixture\n\nMetodoloji: v4.0\n\nKarar: TEST_ONCELIKLI\n\n"
        "[Kanit](data/evidence-ledger.md)\n",
        encoding="utf-8",
    )
    if mode in {"standard", "deep"}:
        phases = output_dir / "phases"
        phases.mkdir()
        for name in evidence_tool.required_phase_files(mode, assessment["decision"]):
            (phases / name).write_text(f"# {name}\n", encoding="utf-8")
    if mode == "deep":
        (data_dir / "raw-search-results.md").write_text("# Raw\n", encoding="utf-8")
    return output_dir


class EvidenceToolTests(unittest.TestCase):
    def test_agent_instruction_files_are_synced(self):
        self.assertEqual(
            (ROOT / "AGENTS.md").read_text(encoding="utf-8"),
            (ROOT / "CLAUDE.md").read_text(encoding="utf-8"),
        )

    def test_json_contracts_parse(self):
        for name in ("evidence-record.schema.json", "assessment.schema.json"):
            json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))

    def test_removed_v3_rules_are_absent_from_active_docs(self):
        roots = [ROOT / "AGENTS.md", ROOT / "CLAUDE.md"]
        for directory in ("methodology", "templates", ".claude/commands"):
            roots.extend((ROOT / directory).glob("**/*.md"))
        removed = [
            "rating " + "> 500",
            "rating " + "< 500",
            "%" + "70",
            "GO/" + "SARTLI",
            "3 " + "Katmanli",
        ]
        for path in roots:
            content = path.read_text(encoding="utf-8")
            for phrase in removed:
                self.assertNotIn(phrase, content, f"{phrase!r} found in {path}")

    def test_repository_fixture_passes(self):
        result = evidence_tool.validate_output(ROOT / "tests" / "fixtures" / "valid-quick")
        self.assertTrue(result.ok, result.errors)

    def test_valid_quick_standard_and_deep_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for mode in ("quick", "standard", "deep"):
                result = evidence_tool.validate_output(write_output(root, mode))
                self.assertTrue(result.ok, result.errors)

    def test_duplicate_id_fails(self):
        records = valid_records()
        records.append(copy.deepcopy(records[0]))
        result = evidence_tool.validate_evidence_records(records)
        self.assertFalse(result.ok)
        self.assertTrue(any("duplicate evidence_id" in error for error in result.errors))

    def test_web_evidence_requires_url(self):
        records = valid_records()
        records[0]["source_url"] = None
        result = evidence_tool.validate_evidence_records(records)
        self.assertFalse(result.ok)
        self.assertTrue(any("source_url" in error for error in result.errors))

    def test_same_independence_root_does_not_reach_b(self):
        records = [
            evidence("one", "claim", "E3", "same-root"),
            evidence("two", "claim", "E2", "same-root"),
        ]
        self.assertEqual("C", evidence_tool.compute_claim_grade(records))

    def test_unresolved_strong_counter_forces_d(self):
        records = [
            evidence("support", "claim", "E4", "first-party"),
            evidence("counter", "claim", "E3", "counter-root"),
        ]
        records[1]["direction"] = "contradicts"
        self.assertEqual("D", evidence_tool.compute_claim_grade(records))

    def test_low_rating_is_supporting_evidence_not_a_gate(self):
        record = evidence("low-rating", "claim-demand", "E2", "app-store-root")
        record["value"] = 300
        record["unit"] = "ratings"
        record["claim_relevance"] = "supporting"
        result = evidence_tool.validate_evidence_records([record])
        self.assertTrue(result.ok, result.errors)
        self.assertEqual("C", evidence_tool.compute_claim_grade([record]))

    def test_b2b_loi_and_workaround_reach_b_without_app_competitor(self):
        loi = evidence("signed-loi", "claim-demand", "E3", "customer-loi", "experiment")
        workaround = evidence("paid-workaround", "claim-demand", "E2", "customer-history", "interview")
        self.assertEqual("B", evidence_tool.compute_claim_grade([loi, workaround]))

    def test_marketplace_missing_liquidity_has_no_score(self):
        dimensions = valid_assessment()["dimensions"]
        self.assertIsNone(evidence_tool.compute_opportunity("marketplace_network", dimensions))

    def test_synthetic_evidence_cannot_exceed_e0(self):
        record = evidence("persona", "claim-demand", "E1", "llm", "synthetic")
        result = evidence_tool.validate_evidence_records([record])
        self.assertFalse(result.ok)
        self.assertTrue(any("synthetic evidence must be E0" in error for error in result.errors))

    def test_unknown_evidence_field_is_rejected(self):
        record = evidence("extra", "claim-demand", "E2", "root")
        record["unexpected"] = True
        result = evidence_tool.validate_evidence_records([record])
        self.assertFalse(result.ok)
        self.assertTrue(any("unknown fields" in error for error in result.errors))

    def test_desk_decision_is_rejected_at_prebuild_stage(self):
        records = valid_records()
        assessment = valid_assessment()
        assessment["stage"] = "prebuild_validation"
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("prebuild decision must be" in error for error in result.errors))

    def test_strongly_countered_value_requires_kill(self):
        records = valid_records()
        counter = evidence("demand-counter", "claim-demand", "E3", "counter-root")
        counter["direction"] = "contradicts"
        records.append(counter)
        assessment = valid_assessment()
        assessment["stage"] = "prebuild_validation"
        assessment["decision"] = "TESTE_DEVAM"
        assessment["status"] = "PREBUILD_PENDING"
        assessment["riskiest_assumptions"][0]["claim_grade"] = "D"
        assessment["riskiest_assumptions"][0]["disposition"] = "contradicted"
        assessment["overall_evidence_grade"] = "D"
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("requires KILL" in error for error in result.errors))

    def test_missing_required_dimension_requires_null_opportunity(self):
        records = valid_records()
        assessment = valid_assessment()
        assessment["dimensions"]["distribution_access"] = None
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("opportunity" in error for error in result.errors))

    def test_blocked_gate_rejects_positive_desk_decision(self):
        records = valid_records()
        assessment = valid_assessment()
        assessment["fatal_gates"][0]["status"] = "blocked"
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("desk decision must be ELENDIR" in error for error in result.errors))

    def test_build_small_rejects_c_grade(self):
        records = valid_records()
        assessment = valid_assessment()
        assessment["stage"] = "prebuild_validation"
        assessment["decision"] = "BUILD_SMALL"
        assessment["status"] = "PREBUILD_PASSED"
        assessment["overall_evidence_grade"] = "C"
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("BUILD_SMALL" in error or "overall_evidence_grade" in error for error in result.errors))

    def test_subscription_build_small_requires_retention_evidence(self):
        records = valid_records()
        assessment = valid_assessment()
        assessment["primary_archetype"] = "consumer_subscription"
        assessment["opportunity"] = evidence_tool.compute_opportunity(
            "consumer_subscription", assessment["dimensions"]
        )
        assessment["stage"] = "prebuild_validation"
        assessment["decision"] = "BUILD_SMALL"
        assessment["status"] = "PREBUILD_PASSED"
        assessment["riskiest_assumptions"][0]["product_specific_behavior"] = True
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("retention evidence" in error for error in result.errors))

    def test_scale_requires_two_passing_cohorts(self):
        records = valid_records()
        assessment = valid_assessment()
        assessment["stage"] = "post_mvp"
        assessment["decision"] = "SCALE"
        assessment["status"] = "POSTLAUNCH"
        assessment["post_mvp_result"] = {
            "consecutive_passing_cohorts": 1,
            "consecutive_value_or_retention_failures": 0,
            "value_activation_passed": True,
            "retention_passed": True,
            "economics_passed": True,
            "remaining_failed_metrics": 0,
        }
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("SCALE requires two passing cohorts" in error for error in result.errors))

    def test_post_mvp_result_is_rejected_before_post_mvp(self):
        records = valid_records()
        assessment = valid_assessment()
        assessment["post_mvp_result"] = {
            "consecutive_passing_cohorts": 0,
            "consecutive_value_or_retention_failures": 0,
            "value_activation_passed": False,
            "retention_passed": False,
            "economics_passed": False,
            "remaining_failed_metrics": 3,
        }
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertFalse(result.ok)
        self.assertTrue(any("post_mvp_result must be null" in error for error in result.errors))

    def test_render_is_deterministic(self):
        records = valid_records()
        self.assertEqual(
            evidence_tool.render_ledger(records),
            evidence_tool.render_ledger(list(reversed(records))),
        )

    def test_validate_all_can_skip_legacy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            legacy = root / "legacy"
            legacy.mkdir()
            (legacy / "REPORT.md").write_text("legacy\n", encoding="utf-8")
            self.assertEqual(0, evidence_tool.command_validate_all(root, skip_legacy=True))


if __name__ == "__main__":
    unittest.main()
