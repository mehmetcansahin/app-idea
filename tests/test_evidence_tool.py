import contextlib
import copy
import hashlib
import io
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


def product_evidence(evidence_id, claim_id, root, source_type="first_party", level="E3"):
    """This product's own observed result, traceable to an export instead of a public URL."""
    record = evidence(evidence_id, claim_id, level, root, source_type)
    record.update(
        source_title=f"Fixture app pilot {evidence_id}",
        source_url=None,
        source_ref=f"Pilot export {evidence_id}, 2026-07-10",
        observation=f"Pilot visitors of the fixture app acted on {claim_id}",
        value=12,
        unit="paid pre-orders",
        sample_n=120,
        denominator=120,
    )
    return record


def valid_records():
    records = []
    for claim in ("claim-demand", "claim-economics", "claim-wedge"):
        records.append(evidence(f"{claim}-behavior", claim, "E3", f"{claim}-behavior-root"))
        records.append(evidence(f"{claim}-metric", claim, "E2", f"{claim}-metric-root"))
    for code in ("legal", "feasibility", "platform", "safety"):
        records.append(evidence(f"gate-{code}", f"claim-gate-{code}", "E2", f"gate-{code}-root"))
    return records


def build_small_records(*extra):
    """valid_records() plus a first-party pilot result for the demand claim."""
    pilot = product_evidence("claim-demand-pilot", "claim-demand", "fixture-app-pilot")
    return valid_records() + [pilot] + list(extra)


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
        "product_type": "app",
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
                "product_specific_evidence_ids": [],
                "disposition": "supported",
            },
            {
                "claim_id": "claim-economics",
                "category": "business_viability",
                "impact": 3,
                "uncertainty": 2,
                "claim_grade": "B",
                "product_specific_evidence_ids": [],
                "disposition": "supported",
            },
            {
                "claim_id": "claim-wedge",
                "category": "usability",
                "impact": 2,
                "uncertainty": 3,
                "claim_grade": "B",
                "product_specific_evidence_ids": [],
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


def rat(claim_id, category, links=()):
    """An extra riskiest assumption; grade_assessment() fills in its grade."""
    return {
        "claim_id": claim_id,
        "category": category,
        "impact": 3,
        "uncertainty": 2,
        "claim_grade": "D",
        "product_specific_evidence_ids": list(links),
        "disposition": "supported",
    }


def grade_assessment(assessment, records):
    """Record the claim grades the evidence earns, as the analyst does after research."""
    grades = {
        claim_id: evidence_tool.compute_claim_grade(claim_records)
        for claim_id, claim_records in evidence_tool.group_by_claim(records).items()
    }
    for item in assessment["riskiest_assumptions"]:
        item["claim_grade"] = grades.get(item["claim_id"], "D")
    assessment["overall_evidence_grade"] = evidence_tool.expected_overall_grade(
        assessment["riskiest_assumptions"], grades
    )
    return assessment


def build_small_assessment(records, links=None, archetype="consumer_utility", extra=(), dimensions=None):
    """Pre-build BUILD_SMALL assessment whose RATs link ``links[claim_id]`` as product proof."""
    assessment = valid_assessment()
    assessment.update(
        primary_archetype=archetype,
        stage="prebuild_validation",
        decision="BUILD_SMALL",
        status="PREBUILD_PASSED",
    )
    assessment["dimensions"].update(copy.deepcopy(dimensions or {}))
    assessment["riskiest_assumptions"].extend(copy.deepcopy(list(extra)))
    for item in assessment["riskiest_assumptions"]:
        if links and item["claim_id"] in links:
            item["product_specific_evidence_ids"] = list(links[item["claim_id"]])
    assessment["opportunity"] = evidence_tool.compute_opportunity(archetype, assessment["dimensions"])
    return grade_assessment(assessment, records)


def scale_assessment(cohorts=2):
    assessment = valid_assessment()
    assessment.update(stage="post_mvp", decision="SCALE", status="POSTLAUNCH")
    assessment["post_mvp_result"] = {
        "consecutive_passing_cohorts": cohorts,
        "consecutive_value_or_retention_failures": 0,
        "value_activation_passed": True,
        "retention_passed": True,
        "economics_passed": True,
        "remaining_failed_metrics": 0,
    }
    return assessment


DELETE = object()


def set_path(document, path, value):
    target = document
    for key in path[:-1]:
        target = target[key]
    if value is DELETE:
        del target[path[-1]]
    else:
        target[path[-1]] = value


# (path, value, parts one error must contain). Each defect would otherwise be
# silently accepted, misread or crash the score/grade computation.
ASSESSMENT_DEFECTS = (
    (("dimensions",), [], ("assessment dimensions",)),
    (("dimensions", "problem_demand"), "strong", ("dimensions.problem_demand",)),
    (("dimensions", "distribution_access", "low"), True, ("dimensions.distribution_access.low", "boolean")),
    (("dimensions", "timing", "base"), "3", ("dimensions.timing.base",)),
    (("dimensions", "timing", "claim_ids"), "claim-wedge", ("dimensions.timing.claim_ids",)),
    (("dimensions", "problem_demand", "claim_ids"), [["claim-demand"]], ("dimensions.problem_demand.claim_ids[0]",)),
    (("dimensions", "competitive_wedge", "notes"), "strong", ("dimensions.competitive_wedge", "unknown fields: notes")),
    (("dimensions", "liquidity_cold_start"), DELETE, ("dimensions", "missing fields: liquidity_cold_start")),
    (("fatal_gates",), {"code": "LEGAL_BLOCKED"}, ("assessment fatal_gates",)),
    (("fatal_gates", 0), "LEGAL_BLOCKED", ("fatal_gates[0]",)),
    (("fatal_gates", 0, "status"), ["clear"], ("fatal_gates[0].status",)),
    (("fatal_gates", 0, "evidence_ids"), "gate-legal", ("fatal_gates[0].evidence_ids",)),
    (("fatal_gates", 1, "note"), "checked", ("fatal_gates[1]", "unknown fields: note")),
    (("riskiest_assumptions",), {}, ("assessment riskiest_assumptions",)),
    (("riskiest_assumptions", 0), "claim-demand", ("riskiest_assumptions[0]",)),
    (("riskiest_assumptions", 0, "impact"), True, ("riskiest_assumptions[0].impact", "boolean")),
    (("riskiest_assumptions", 1, "uncertainty"), "2", ("riskiest_assumptions[1].uncertainty",)),
    (("riskiest_assumptions", 2, "impact"), 4, ("riskiest_assumptions[2].impact",)),
    (("riskiest_assumptions", 0, "claim_id"), ["claim-demand"], ("riskiest_assumptions[0].claim_id",)),
    (("riskiest_assumptions", 0, "disposition"), DELETE, ("riskiest_assumptions[0]", "missing fields: disposition")),
    (("riskiest_assumptions", 0, "disposition"), "maybe", ("riskiest_assumptions[0].disposition",)),
    (
        ("riskiest_assumptions", 0, "product_specific_evidence_ids"),
        "claim-demand-behavior",
        ("riskiest_assumptions[0].product_specific_evidence_ids",),
    ),
    (
        ("riskiest_assumptions", 0, "product_specific_evidence_ids"),
        ["claim-demand-behavior", 7],
        ("riskiest_assumptions[0].product_specific_evidence_ids[1]",),
    ),
    (("opportunity",), "60", ("assessment opportunity",)),
    (("opportunity", "low"), True, ("opportunity.low", "boolean")),
    (("target_geos",), ["US", 5], ("target_geos[1]",)),
    (("risk_modifiers",), [["regulated"]], ("risk_modifiers[0]",)),
    (("mode",), ["quick"], ("assessment mode",)),
    (("primary_archetype",), ["consumer_utility"], ("assessment primary_archetype",)),
    (("decision",), {"value": "TEST_ONCELIKLI"}, ("assessment decision",)),
    (("product_type",), ["app"], ("assessment product_type",)),
    (("idea_id",), 5, ("assessment idea_id",)),
    (("next_test",), 5, ("assessment next_test",)),
    (("methodology_version",), 4.0, ("assessment methodology_version",)),
)

# (field, value, extra parts) applied to one otherwise valid evidence record.
EVIDENCE_DEFECTS = (
    ("evidence_id", ["one"], ()),
    ("claim_id", {"id": "claim-demand"}, ()),
    ("idea_id", True, ("boolean",)),
    ("phase", 5, ()),
    ("source_type", ["official_primary"], ()),
    ("status", ["observed"], ()),
    ("evidence_level", ["E2"], ()),
    ("observation_quality", None, ()),
    ("direction", ["supports"], ()),
    ("source_ref", 5, ()),
    ("artifact_path", ["shot.png"], ()),
    ("unit", 3, ()),
    ("geo", 1, ()),
    ("sample_n", True, ("boolean",)),
    ("sample_n", 2.5, ()),
    ("denominator", [1], ()),
    ("limitations", "none", ()),
    ("limitations", [1], ("limitations[0]",)),
    ("search_queries", "query", ()),
    ("attempted_sources", [None], ("attempted_sources[0]",)),
    ("collected_at", 20260710, ()),
    ("observation", ["seen"], ()),
)


def write_jsonl(path, records):
    """Write records verbatim, including malformed ones render would refuse."""
    path.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in records), encoding="utf-8"
    )


def write_records(output_dir, records):
    data_dir = output_dir / "data"
    write_jsonl(data_dir / "evidence.jsonl", records)
    (data_dir / "evidence-ledger.md").write_text(
        evidence_tool.render_ledger(records), encoding="utf-8"
    )


def write_assessment(output_dir, assessment):
    (output_dir / "data" / "assessment.json").write_text(
        json.dumps(assessment, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def read_assessment(output_dir):
    return json.loads((output_dir / "data" / "assessment.json").read_text(encoding="utf-8"))


def write_output(root, mode="quick"):
    output_dir = root / f"fixture-{mode}"
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True)
    write_records(output_dir, valid_records())
    assessment = valid_assessment(mode)
    write_assessment(output_dir, assessment)
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


NARRATIVE_SUMMARY = "> **Bu bölümün sonucu.** Ne öğrendik: x. Neden önemli: y. Karara etkisi: z.\n\n"


def narrative_section(number, title, question):
    return f"## {number}. {title}\n\nBu bölüm şu soruyu yanıtlıyor: {question}\n\n"


def narrative_report(opportunity="60 / 60 / 60", body_extra="", glossary_extra=""):
    """Smallest report that satisfies methodology/report-writing.md."""
    return (
        "# Fixture uygulaması\n\nMetodoloji v4.0\n\n**Karar: `TEST_ONCELIKLI`.**\n\n"
        "Kaynaklar: [kanıt defteri](data/evidence-ledger.md)\n\n"
        f"## Kısa cevap: Bu projeyi hayata geçirmek mantıklı mı?\n\nFırsat {opportunity}.\n\n"
        "## Bu rapor nasıl okunmalı?\n\nRehber.\n\n"
        + narrative_section(1, "Neyi değerlendirdik?", "Ne?")
        + "### Kapsam dışında kalanlar\n\nEski hesaplar.\n\n"
        + NARRATIVE_SUMMARY
        + narrative_section(2, "Kullanıcının sorunu", "Gerçek mi?")
        + "### Bulgu 1 — Talep var\n\n"
        + "**Ne gözlemledik?** Kayıtlar arttı ([kaynak](https://example.com/claim-demand-behavior)).\n\n"
        + "**Ürün açısından anlamı.** Talep var.\n\n"
        + "**Henüz varamadığımız sonuç.** Ödeme isteği bilinmiyor.\n\n"
        + body_extra
        + NARRATIVE_SUMMARY
        + narrative_section(3, "Mevcut çözümler", "Kim çözüyor?")
        + "| Rakip | Bu işte ne zamandan beri? | Platformlar |\n|---|---|---|\n| A | 2015 | iOS |\n\n"
        + NARRATIVE_SUMMARY
        + narrative_section(4, "Kullanıcıya ulaşma", "Nasıl ulaşırız?")
        + "| Kanal | Kim hâkim? | Yeni bir uygulama için gerçekçi mi? |\n|---|---|---|\n"
        + "| Web araması | Rakip siteleri | Hayır |\n\n"
        + NARRATIVE_SUMMARY
        + narrative_section(5, "Karar ve öneri", "Ne yapalım?")
        + "Yasal engel görülmedi; önce ön sipariş testi yapılmalı.\n\n"
        + NARRATIVE_SUMMARY
        + narrative_section(6, "Kanıtın sınırları", "Neye güvenebiliriz?")
        + "Pazar büyüklüğü tek bir kaynağa dayanıyor.\n\n"
        + NARRATIVE_SUMMARY
        + "## Ek A — Terimler sözlüğü\n\n| Terim | Anlamı |\n|---|---|\n"
        + glossary_extra
        + "\n## Ek C — Araştırma arşivi (denetim için)\n\n- Bölüm 2 → `claim-demand`\n"
    )


def research_records(mode, search_pages=8):
    """Competitor, market and search-results evidence the research steps produce."""
    records = [evidence("fixture-competitor-profile-a", "fixture-competitor-profile", "E2", "competitor-a")]
    if mode in {"standard", "deep"}:
        records.append(evidence("fixture-market-size-a", "fixture-market-size", "E2", "market-a"))
        for index in range(search_pages):
            record = evidence(f"fixture-serp-{index}", "fixture-distribution", "E2", f"serp-{index}")
            record["source_url"] = f"https://www.google.com/search?q=query+{index}"
            records.append(record)
    return records


def review_records():
    """Every record a Standard/Deep narrative output carries."""
    return valid_records() + research_records("deep")


# Ten distinct statements of narrative_report(): (claim, where it stands, evidence IDs).
CLAIM_CHECKS = (
    ("Fırsat 60 / 60 / 60", "Kısa cevap", "claim-demand-metric"),
    ("Kayıtlar arttı", "Bölüm 2, Bulgu 1 — Ne gözlemledik?", "claim-demand-behavior"),
    ("Talep var", "Bölüm 2, Bulgu 1 — Ürün açısından anlamı", "claim-demand-metric"),
    ("Ödeme isteği bilinmiyor", "Bölüm 2, Bulgu 1 — Henüz varamadığımız sonuç", "claim-economics-metric"),
    ("Rakip A 2015'ten beri bu işte", "Bölüm 3, rakip tablosu", "fixture-competitor-profile-a"),
    ("Rakip A iOS'ta", "Bölüm 3, rakip tablosu", "fixture-competitor-profile-a"),
    ("Web aramasında rakip siteleri hâkim", "Bölüm 4, kanal tablosu", "fixture-serp-0"),
    ("Web araması yeni bir uygulama için gerçekçi değil", "Bölüm 4, kanal tablosu", "fixture-serp-0 fixture-serp-1"),
    ("Yasal engel görülmedi", "Bölüm 5, Karar ve öneri", "gate-legal"),
    ("Pazar büyüklüğü tek bir kaynağa dayanıyor", "Bölüm 6, Kanıtın sınırları", "fixture-market-size-a"),
)

# The same check as CLAIM_CHECKS[0], written the ways a reviewer repeats a row.
DUPLICATE_CHECKS = (
    ("Fırsat 60 / 60 / 60", "Kısa cevap", "claim-demand-metric"),
    ("FIRSAT 60 / 60 / 60", "KISA CEVAP", "claim-demand-metric"),
    ("Fırsat  60 /\t60 / 60", "Kısa   cevap", "claim-demand-metric"),
    ("**Fırsat** 60 / 60 / 60", "`Kısa cevap`", "claim-demand-metric"),
    ("Fırsat 60 / 60 / 60", "Kısa cevap", "claim-wedge-metric"),
)

# Ten different claims that one competitor profile record supports.
SAME_RECORD_CHECKS = tuple(
    (claim, location, "fixture-competitor-profile-a")
    for claim, location in (
        ("Rakip A 2015'ten beri bu işte", "Bölüm 3, rakip tablosu"),
        ("Rakip A iOS'ta", "Bölüm 3, rakip tablosu"),
        ("Rakip A'nın Android sürümü yok", "Bölüm 3, rakip tablosu"),
        ("Rakip A aylık 4,99 dolar istiyor", "Bölüm 3, fiyat paragrafı"),
        ("Rakip A aile planı sunuyor", "Bölüm 3, fiyat paragrafı"),
        ("Rakip A'nın puanı 4,6", "Bölüm 3, puan paragrafı"),
        ("Rakip A'yı 12 bin kişi puanlamış", "Bölüm 3, puan paragrafı"),
        ("Rakip A son güncellemeyi Haziran 2026'da yaptı", "Bölüm 3, güncelleme notu"),
        ("Rakip A'nın web sürümü yok", "Bölüm 4, kanal tablosu"),
        ("Rakip A 2015'ten beri bu işte", "Kısa cevap"),
    )
)


def evidence_cell(ids):
    return ", ".join(f"`{evidence_id}`" for evidence_id in ids.split())


def reader_review(
    revision,
    reviewer="Bağımsız okur",
    criterion_verdict="GEÇTİ",
    issue_status="Düzeltildi",
    issue_fix="Cümle tamamlandı.",
    claim_verdict="Evet",
    claims=CLAIM_CHECKS,
):
    """data/reader-review.md for the report revision ``revision`` (None omits the line)."""
    criteria = "".join(
        f"| **{key}** — ölçüt | {criterion_verdict} | satır 1 |\n"
        for key in evidence_tool.READER_REVIEW_CRITERIA
    )
    checks = "".join(
        f"| {claim} | {location} | {evidence_cell(ids)} | {claim_verdict} |\n"
        for claim, location, ids in claims
    )
    revision_line = "" if revision is None else f"- İncelenen revizyon: {revision}\n"
    return (
        f"# Okur İncelemesi\n\n- İnceleyen: {reviewer}\n- Tarih: 2026-10-21\n"
        + revision_line
        + "\n## Ölçütler\n\n| Ölçüt | Sonuç | Not |\n|---|---|---|\n"
        + criteria
        + "\n## Bulunan sorunlar\n\n| # | Yer | Sorun | Durum | Çözüm |\n|---|---|---|---|---|\n"
        + f"| 1 | Bölüm 2 | Yarım cümle | {issue_status} | {issue_fix} |\n"
        + "\n## İddia kontrolü\n\nRaporun farklı yerlerinden iddialar kanıt kayıtlarıyla karşılaştırıldı.\n\n"
        + "| İddia | Yer | Kanıt kaydı | Uyuyor mu? |\n|---|---|---|---|\n"
        + checks
    )


def check_review(review, report=None, records=None):
    if records is None:
        records = review_records()
    if report is None:
        report = narrative_report()
    return evidence_tool.validate_reader_review(review, records, report)


def current_review(**kwargs):
    revision = evidence_tool.report_revision(narrative_report(), review_records())
    return reader_review(revision, **kwargs)


def set_analysis_date(output_dir, value):
    assessment = read_assessment(output_dir)
    assessment["analysis_date"] = value
    write_assessment(output_dir, assessment)


def write_narrative_output(root, report, mode="quick", research=None, review=None, summary=True):
    """Output dated on the narrative cutoff; research, Özet and a current review default to complete."""
    output_dir = write_output(root, mode)
    set_analysis_date(output_dir, evidence_tool.NARRATIVE_REPORT_FROM.isoformat())
    if research is None:
        research = research_records(mode)
    records = valid_records() + research
    write_records(output_dir, records)
    if summary:
        report = evidence_tool.with_report_summary(report, read_assessment(output_dir)) or report
    (output_dir / "REPORT.md").write_text(report, encoding="utf-8")
    if review is None and mode in {"standard", "deep"}:
        review = reader_review(evidence_tool.report_revision(report, records))
    if review:
        (output_dir / evidence_tool.READER_REVIEW_PATH).write_text(review, encoding="utf-8")
    return output_dir


def run_render(output_dir):
    with contextlib.redirect_stdout(io.StringIO()):
        return evidence_tool.command_render(output_dir)


def run_main(*argv):
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        code = evidence_tool.main([str(arg) for arg in argv])
    return code, stdout.getvalue()


class EvidenceToolTests(unittest.TestCase):
    def assertErrorWith(self, result, *parts):
        self.assertTrue(
            any(all(part in error for part in parts) for error in result.errors),
            f"no error containing {parts!r} in {result.errors!r}",
        )

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

    def test_echoed_root_warns_when_splitting_it_would_raise_the_grade(self):
        records = [
            evidence("primary", "claim", "E2", "one-report"),
            evidence("coverage-a", "claim", "E2", "one-report"),
            evidence("coverage-b", "claim", "E2", "one-report"),
        ]
        result = evidence_tool.validate_evidence_records(records)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual("C", evidence_tool.compute_claim_grade(records))
        self.assertTrue(
            any("would grade B instead of C" in warning for warning in result.warnings),
            result.warnings,
        )

    def test_conservative_root_over_several_urls_stays_silent(self):
        records = [
            evidence("vendor-api-doc", "claim", "E2", "Apple Inc."),
            evidence("vendor-writer-doc", "claim", "E2", "Apple Inc."),
        ]
        result = evidence_tool.validate_evidence_records(records)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual("C", evidence_tool.compute_claim_grade(records))
        self.assertEqual([], result.warnings)

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

    def test_ad_library_evidence_cannot_exceed_e2(self):
        record = evidence("meta-longevity", "claim-economics", "E3", "adlib-meta-x-2026-07-10", "ad_library")
        record["artifact_path"] = "data/artifacts/ads/meta-x-2026-07-10.png"
        result = evidence_tool.validate_evidence_records([record])
        self.assertFalse(result.ok)
        self.assertTrue(any("ad_library evidence must be E1 or E2" in error for error in result.errors))

    def test_observed_ad_library_record_without_screenshot_warns(self):
        record = evidence("meta-x", "claim-distribution", "E2", "adlib-meta-x-2026-07-10", "ad_library")
        result = evidence_tool.validate_evidence_records([record])
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("artifact_path" in warning for warning in result.warnings), result.warnings)
        record["artifact_path"] = "data/artifacts/ads/meta-x-2026-07-10.png"
        result = evidence_tool.validate_evidence_records([record])
        self.assertEqual([], result.warnings)

    def test_ad_library_alone_cannot_reach_b(self):
        records = [
            evidence("meta-incogni", "claim-distribution", "E2", "adlib-meta-incogni-2026-07-10", "ad_library"),
            evidence("meta-deleteme", "claim-distribution", "E2", "adlib-meta-deleteme-2026-07-10", "ad_library"),
            evidence("google-optery", "claim-distribution", "E2", "adlib-google-optery-2026-07-10", "ad_library"),
        ]
        for record in records:
            record["artifact_path"] = f"data/artifacts/ads/{record['evidence_id']}-2026-07-10.png"
        self.assertEqual("C", evidence_tool.compute_claim_grade(records))
        self.assertEqual([], evidence_tool.validate_evidence_records(records).warnings)
        records.append(evidence("store-serp", "claim-distribution", "E2", "itunes-search-api"))
        self.assertEqual("B", evidence_tool.compute_claim_grade(records))

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

    def test_product_type_is_required_and_enumerated(self):
        records = valid_records()
        missing = valid_assessment()
        del missing["product_type"]
        self.assertErrorWith(
            evidence_tool.validate_assessment(missing, records), "assessment missing fields: product_type"
        )
        for value in ("mobile", "", None):
            with self.subTest(value=value):
                assessment = valid_assessment()
                assessment["product_type"] = value
                result = evidence_tool.validate_assessment(assessment, records)
                self.assertErrorWith(result, "assessment product_type")

    def test_product_type_leaves_archetype_scoring_unchanged(self):
        # The same dimensions score 60 / 60 / 60 whichever surface the product ships on.
        for product_type in ("app", "web_saas", "service"):
            with self.subTest(product_type):
                assessment = valid_assessment()
                assessment["product_type"] = product_type
                result = evidence_tool.validate_assessment(assessment, valid_records())
                self.assertTrue(result.ok, result.errors)

    def test_archival_is_not_an_assessment_status(self):
        for status in ("ARCHIVED", "LEGACY"):
            with self.subTest(status):
                assessment = valid_assessment()
                assessment["status"] = status
                result = evidence_tool.validate_assessment(assessment, valid_records())
                self.assertErrorWith(result, "assessment status is invalid")

    def test_rat_attests_product_behavior_by_evidence_ids_not_a_boolean(self):
        records = valid_records()
        legacy = valid_assessment()
        legacy["riskiest_assumptions"][0]["product_specific_behavior"] = True
        self.assertErrorWith(
            evidence_tool.validate_assessment(legacy, records),
            "riskiest_assumptions[0]",
            "unknown fields: product_specific_behavior",
        )
        missing = valid_assessment()
        del missing["riskiest_assumptions"][0]["product_specific_evidence_ids"]
        self.assertErrorWith(
            evidence_tool.validate_assessment(missing, records),
            "riskiest_assumptions[0]",
            "missing fields: product_specific_evidence_ids",
        )

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

    def test_build_small_passes_with_a_linked_product_result(self):
        for source_type, reference in (("first_party", "source_ref"), ("experiment", "artifact_path")):
            with self.subTest(source_type):
                pilot = product_evidence("claim-demand-pilot", "claim-demand", "fixture-app-pilot", source_type)
                if reference == "artifact_path":
                    pilot["source_ref"] = None
                    pilot["artifact_path"] = "data/artifacts/pilot-preorders.csv"
                records = valid_records() + [pilot]
                assessment = build_small_assessment(records, {"claim-demand": ["claim-demand-pilot"]})
                self.assertEqual("A", assessment["riskiest_assumptions"][0]["claim_grade"])
                self.assertEqual("B", assessment["overall_evidence_grade"])
                result = evidence_tool.validate_assessment(assessment, records)
                self.assertTrue(result.ok, result.errors)

    def test_build_small_needs_more_than_b_grade_desk_evidence(self):
        # Before the cutover this B-grade desk research reached BUILD_SMALL with a
        # bare product_specific_behavior=true; a public source URL is not product proof.
        records = valid_records()
        unlinked = build_small_assessment(records)
        self.assertEqual("B", unlinked["overall_evidence_grade"])
        self.assertErrorWith(
            evidence_tool.validate_assessment(unlinked, records),
            "BUILD_SMALL requires product-specific evidence",
        )
        competitor = build_small_assessment(records, {"claim-demand": ["claim-demand-behavior"]})
        result = evidence_tool.validate_assessment(competitor, records)
        self.assertErrorWith(result, "RAT claim-demand", "claim-demand-behavior", "not eligible", "source_type")
        self.assertErrorWith(result, "claim-demand-behavior", "not eligible", "source_ref or artifact_path")
        self.assertErrorWith(result, "BUILD_SMALL requires product-specific evidence")

    def test_build_small_rejects_e2_only_product_evidence(self):
        records = [record for record in valid_records() if record["evidence_id"] != "claim-demand-behavior"]
        records += [
            evidence("claim-demand-survey", "claim-demand", "E2", "demand-survey-root"),
            product_evidence("claim-demand-pilot", "claim-demand", "fixture-app-pilot", level="E2"),
        ]
        assessment = build_small_assessment(records, {"claim-demand": ["claim-demand-pilot"]})
        self.assertEqual("B", assessment["riskiest_assumptions"][0]["claim_grade"])
        result = evidence_tool.validate_assessment(assessment, records)
        self.assertErrorWith(result, "claim-demand-pilot", "not eligible", "evidence_level")
        self.assertErrorWith(result, "BUILD_SMALL requires product-specific evidence")

    def test_build_small_rejects_ineligible_product_links(self):
        def pilot(**changes):
            record = product_evidence("claim-demand-pilot", "claim-demand", "fixture-app-pilot")
            record.update(changes)
            return record

        cases = {
            "wrong claim": (pilot(claim_id="claim-economics"), "claim_id"),
            "wrong idea": (pilot(idea_id="other-app"), "idea_id"),
            "contradicting": (pilot(direction="contradicts"), "direction"),
            "neutral": (pilot(direction="neutral"), "direction"),
            "supporting relevance": (pilot(claim_relevance="supporting"), "claim_relevance"),
            "weak relevance": (pilot(claim_relevance="weak"), "claim_relevance"),
            "estimated": (pilot(observation_quality="estimated"), "observation_quality"),
            "not observed": (
                pilot(
                    status="not_found_after_protocol",
                    search_queries=["fixture app pilot export"],
                    attempted_sources=["payment processor export"],
                ),
                "status",
            ),
            "E2": (pilot(evidence_level="E2"), "evidence_level"),
            "public source": (
                pilot(source_type="official_primary", source_url="https://example.com/pilot"),
                "source_type",
            ),
            "url only": (
                pilot(source_ref=None, source_url="https://example.com/pilot"),
                "source_ref or artifact_path",
            ),
            "blank reference": (
                pilot(source_ref="   ", source_url="https://example.com/pilot"),
                "source_ref or artifact_path",
            ),
        }
        for name, (record, field) in cases.items():
            with self.subTest(name):
                records = valid_records() + [record]
                assessment = build_small_assessment(records, {"claim-demand": ["claim-demand-pilot"]})
                result = evidence_tool.validate_assessment(assessment, records)
                self.assertErrorWith(result, "RAT claim-demand", "claim-demand-pilot", "not eligible", field)
                self.assertErrorWith(result, "BUILD_SMALL requires product-specific evidence")

    def test_product_links_must_name_unique_known_records(self):
        records = build_small_records()
        missing = build_small_assessment(
            records, {"claim-demand": ["claim-demand-pilot", "claim-demand-retired-pilot"]}
        )
        self.assertErrorWith(
            evidence_tool.validate_assessment(missing, records),
            "RAT claim-demand",
            "unknown evidence claim-demand-retired-pilot",
        )
        repeated = build_small_assessment(records, {"claim-demand": ["claim-demand-pilot", "claim-demand-pilot"]})
        self.assertErrorWith(
            evidence_tool.validate_assessment(repeated, records),
            "riskiest_assumptions[0].product_specific_evidence_ids",
            "duplicate",
        )

    def test_product_links_are_checked_before_any_build_decision(self):
        records = valid_records()
        desk = valid_assessment()
        desk["riskiest_assumptions"][0]["product_specific_evidence_ids"] = ["claim-demand-behavior"]
        self.assertErrorWith(
            evidence_tool.validate_assessment(desk, records),
            "RAT claim-demand",
            "claim-demand-behavior",
            "not eligible",
        )
        records = build_small_records()
        linked = grade_assessment(valid_assessment(), records)
        linked["riskiest_assumptions"][0]["product_specific_evidence_ids"] = ["claim-demand-pilot"]
        result = evidence_tool.validate_assessment(linked, records)
        self.assertTrue(result.ok, result.errors)

    def test_subscription_build_small_requires_its_own_retention_result(self):
        records = build_small_records(
            evidence("claim-retention-metric", "claim-retention", "E2", "retention-metric-root"),
            product_evidence("claim-retention-cohort", "claim-retention", "fixture-app-cohort", "experiment"),
        )
        dimensions = {
            "repeat_value_retention": {"low": 3, "base": 3, "high": 3, "claim_ids": ["claim-retention"]}
        }

        def subscription(*extra):
            return build_small_assessment(
                records, {"claim-demand": ["claim-demand-pilot"]}, "consumer_subscription", extra, dimensions
            )

        cases = {
            "no retention RAT": subscription(),
            "unlinked retention RAT": subscription(rat("claim-retention", "retention")),
            "value proof reused": subscription(rat("claim-retention", "retention", ["claim-demand-pilot"])),
        }
        for name, assessment in cases.items():
            with self.subTest(name):
                result = evidence_tool.validate_assessment(assessment, records)
                self.assertErrorWith(
                    result, "subscription BUILD_SMALL requires product-specific retention evidence"
                )
        ready = subscription(rat("claim-retention", "retention", ["claim-retention-cohort"]))
        self.assertEqual("B", ready["riskiest_assumptions"][-1]["claim_grade"])
        result = evidence_tool.validate_assessment(ready, records)
        self.assertTrue(result.ok, result.errors)

    def test_marketplace_build_small_requires_linked_liquidity_at_b_or_better(self):
        liquidity_pilot = product_evidence(
            "claim-liquidity-pilot", "claim-liquidity", "fixture-app-liquidity-pilot", "experiment"
        )
        liquidity_metric = evidence("claim-liquidity-metric", "claim-liquidity", "E2", "liquidity-metric-root")
        dimensions = {
            "liquidity_cold_start": {"low": 3, "base": 3, "high": 3, "claim_ids": ["claim-liquidity"]}
        }

        def marketplace(records, liquidity_links):
            return build_small_assessment(
                records,
                {"claim-demand": ["claim-demand-pilot"]},
                "marketplace_network",
                [rat("claim-liquidity", "liquidity", liquidity_links)],
                dimensions,
            )

        lone = build_small_records(liquidity_pilot)
        below = marketplace(lone, ["claim-liquidity-pilot"])
        self.assertEqual("C", below["riskiest_assumptions"][-1]["claim_grade"])
        self.assertErrorWith(
            evidence_tool.validate_assessment(below, lone),
            "marketplace BUILD_SMALL requires product-specific liquidity evidence",
        )
        corroborated = build_small_records(liquidity_pilot, liquidity_metric)
        unlinked = marketplace(corroborated, [])
        self.assertEqual("B", unlinked["riskiest_assumptions"][-1]["claim_grade"])
        self.assertErrorWith(
            evidence_tool.validate_assessment(unlinked, corroborated),
            "marketplace BUILD_SMALL requires product-specific liquidity evidence",
        )
        ready = marketplace(corroborated, ["claim-liquidity-pilot"])
        result = evidence_tool.validate_assessment(ready, corroborated)
        self.assertTrue(result.ok, result.errors)

    def test_scale_requires_two_passing_cohorts(self):
        records = valid_records()
        self.assertTrue(evidence_tool.validate_assessment(scale_assessment(), records).ok)
        result = evidence_tool.validate_assessment(scale_assessment(cohorts=1), records)
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

    def test_malformed_assessment_is_reported_not_computed(self):
        records = valid_records()
        for path, value, parts in ASSESSMENT_DEFECTS:
            with self.subTest(path=path, value=value):
                assessment = valid_assessment()
                set_path(assessment, path, value)
                result = evidence_tool.validate_assessment(assessment, records)
                self.assertErrorWith(result, *parts)

    def test_malformed_post_mvp_result_is_reported_not_computed(self):
        records = valid_records()
        cases = (
            ("consecutive_passing_cohorts", True, ("post_mvp_result.consecutive_passing_cohorts", "boolean")),
            ("consecutive_passing_cohorts", "2", ("post_mvp_result.consecutive_passing_cohorts",)),
            ("retention_passed", 1, ("post_mvp_result.retention_passed", "integer")),
            ("remaining_failed_metrics", DELETE, ("post_mvp_result", "missing fields: remaining_failed_metrics")),
            ("cohort_notes", "two cohorts", ("post_mvp_result", "unknown fields: cohort_notes")),
        )
        for key, value, parts in cases:
            with self.subTest(key=key, value=value):
                assessment = scale_assessment()
                set_path(assessment, ("post_mvp_result", key), value)
                result = evidence_tool.validate_assessment(assessment, records)
                self.assertErrorWith(result, *parts)

    def test_malformed_evidence_record_is_reported_not_computed(self):
        for field_name, value, parts in EVIDENCE_DEFECTS:
            with self.subTest(field=field_name, value=value):
                record = evidence("one", "claim-demand", "E2", "root")
                record[field_name] = value
                result = evidence_tool.validate_evidence_records([record])
                self.assertErrorWith(result, f"evidence line 1: {field_name}", *parts)

    def test_assessment_cross_checks_wait_for_valid_evidence(self):
        records = valid_records()
        records[0]["claim_id"] = ["claim-demand"]
        result = evidence_tool.validate_assessment(valid_assessment(), records)
        self.assertErrorWith(result, "assessment cross-checks skipped")

    def test_malformed_web_url_reports_error_without_crashing(self):
        for source_url in ("https://[", "https://]"):
            with self.subTest(source_url=source_url), tempfile.TemporaryDirectory() as tmp:
                output_dir = write_output(Path(tmp))
                records = valid_records()
                records[0]["source_url"] = source_url
                write_jsonl(output_dir / "data" / "evidence.jsonl", records)
                for action in ("validate", "render"):
                    code, output = run_main(action, output_dir)
                    self.assertEqual(1, code)
                    self.assertIn("source_url", output)

    def test_malformed_evidence_file_is_reported_by_validate_and_render(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), narrative_report(), "deep")
            records = review_records()
            records[0]["claim_id"] = ["claim-demand"]
            records[1]["evidence_id"] = {"id": "claim-demand-metric"}
            write_jsonl(output_dir / "data" / "evidence.jsonl", records)
            result = evidence_tool.validate_output(output_dir)
            render_code = run_render(output_dir)
        self.assertErrorWith(result, "evidence line 1: claim_id")
        self.assertErrorWith(result, "evidence line 2: evidence_id")
        self.assertEqual(1, render_code)

    def test_malformed_assessment_file_is_reported_by_validate(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), narrative_report(), "deep")
            assessment = read_assessment(output_dir)
            assessment["riskiest_assumptions"][0] = "claim-demand"
            assessment["dimensions"]["problem_demand"]["low"] = True
            write_assessment(output_dir, assessment)
            result = evidence_tool.validate_output(output_dir)
        self.assertErrorWith(result, "riskiest_assumptions[0]")
        self.assertErrorWith(result, "dimensions.problem_demand.low", "boolean")

    def test_non_standard_json_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_output(Path(tmp))
            assessment_path = output_dir / "data" / "assessment.json"
            assessment_path.write_text(
                assessment_path.read_text(encoding="utf-8").replace('"base": 3', '"base": NaN', 1),
                encoding="utf-8",
            )
            evidence_path = output_dir / "data" / "evidence.jsonl"
            lines = evidence_path.read_text(encoding="utf-8").splitlines()
            lines[0] = lines[0][:-1] + ', "evidence_level": "E4"}'
            lines[1] = lines[1][:-1] + ', "__line__": 7}'
            evidence_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            result = evidence_tool.validate_output(output_dir)
        self.assertErrorWith(result, "invalid JSON", "assessment.json")
        self.assertErrorWith(result, "invalid JSONL", "evidence.jsonl:1")
        self.assertErrorWith(result, "__line__ is reserved")

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

    def test_support_surface_is_not_judged_by_the_idea_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            support = root / "keyword-report"
            support.mkdir()
            (support / "REPORT.md").write_text("# keyword research\n", encoding="utf-8")
            (support / "artifact.json").write_text('{"surface": "report"}\n', encoding="utf-8")
            self.assertEqual("support", evidence_tool.classify_output(support))
            # A support surface has no assessment.json, but it is a v4 shape rather
            # than a pre-v4 report, so validate-all must not fail on it.
            self.assertEqual(0, evidence_tool.command_validate_all(root, skip_legacy=False))

    def test_legacy_report_still_fails_without_skip_legacy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            legacy = root / "legacy"
            legacy.mkdir()
            (legacy / "REPORT.md").write_text("legacy\n", encoding="utf-8")
            self.assertEqual("legacy", evidence_tool.classify_output(legacy))
            self.assertEqual(1, evidence_tool.command_validate_all(root, skip_legacy=False))

    def test_assessment_dir_with_artifact_is_still_validated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_dir = write_output(root, "deep")
            (output_dir / "artifact.json").write_text('{"surface": "report"}\n', encoding="utf-8")
            self.assertEqual("assessment", evidence_tool.classify_output(output_dir))
            self.assertEqual(0, evidence_tool.command_validate_all(root, skip_legacy=False))

    def test_validate_all_reports_malformed_runs_and_checks_the_rest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            broken_evidence = write_output(root, "deep")
            records = valid_records()
            records[0]["claim_id"] = ["claim-demand"]
            write_jsonl(broken_evidence / "data" / "evidence.jsonl", records)
            broken_assessment = write_output(root, "quick")
            assessment = read_assessment(broken_assessment)
            assessment["riskiest_assumptions"][0] = "claim-demand"
            write_assessment(broken_assessment, assessment)
            valid = write_output(root, "standard")
            code, output = run_main("validate-all", root)
        self.assertEqual(1, code)
        self.assertIn(f"FAIL {broken_evidence}", output)
        self.assertIn(f"FAIL {broken_assessment}", output)
        self.assertIn(f"PASS {valid}", output)
        self.assertIn("riskiest_assumptions[0]", output)

    def test_validate_all_rejects_a_missing_output_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, output = run_main("validate-all", Path(tmp) / "missing")
        self.assertEqual(1, code)
        self.assertIn("output root not found", output)

    def test_incomplete_assessment_is_reported_not_raised(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_output(Path(tmp))
            (output_dir / "data" / "assessment.json").write_text("{}\n", encoding="utf-8")
            result = evidence_tool.validate_output(output_dir)
            self.assertFalse(result.ok)
            self.assertTrue(any("assessment missing fields" in error for error in result.errors))

    def test_narrative_contract_applies_from_cutoff_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            before = write_output(root / "before")
            set_analysis_date(before, "2026-10-19")
            self.assertTrue(evidence_tool.validate_output(before).ok)
            after = write_output(root / "after")
            set_analysis_date(after, evidence_tool.NARRATIVE_REPORT_FROM.isoformat())
            result = evidence_tool.validate_output(after)
            self.assertFalse(result.ok)
            self.assertTrue(any("Kısa cevap" in error for error in result.errors))

    def test_narrative_report_passes_without_warnings(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(write_narrative_output(Path(tmp), narrative_report()))
            self.assertTrue(result.ok, result.errors)
            self.assertEqual([], result.warnings)

    def test_ids_and_phase_paths_belong_in_the_appendix_not_the_body(self):
        leaked = narrative_report(
            body_extra="Ayrıntı: [claim-demand-behavior] ve phases/04-scoring.md.\n\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(write_narrative_output(Path(tmp), leaked))
        self.assertFalse(result.ok)
        self.assertTrue(any("claim-demand-behavior" in error for error in result.errors))
        self.assertTrue(any("phases/" in error for error in result.errors))

    def test_section_summary_must_answer_all_three_questions(self):
        report = narrative_report().replace("Neden önemli: y. ", "", 1)
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(write_narrative_output(Path(tmp), report))
        self.assertFalse(result.ok)
        self.assertTrue(any("summary lacks: Neden önemli" in error for error in result.errors))

    def test_section_must_open_with_its_question(self):
        report = narrative_report().replace("Bu bölüm şu soruyu yanıtlıyor: Ne yapalım?", "Karar.")
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(write_narrative_output(Path(tmp), report))
        self.assertFalse(result.ok)
        self.assertTrue(any("'5. Karar ve öneri' does not open" in error for error in result.errors))

    def test_finding_must_state_what_it_does_not_prove(self):
        report = narrative_report().replace(
            "**Henüz varamadığımız sonuç.** Ödeme isteği bilinmiyor.\n\n", ""
        )
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(write_narrative_output(Path(tmp), report))
        self.assertFalse(result.ok)
        self.assertTrue(any("lacks: Henüz varamadığımız sonuç" in error for error in result.errors))

    def test_jargon_in_body_requires_a_glossary_entry(self):
        body = "Bu fikrin wedge'i zayıf.\n\n"
        with tempfile.TemporaryDirectory() as tmp:
            undefined = evidence_tool.validate_output(
                write_narrative_output(Path(tmp) / "a", narrative_report(body_extra=body))
            )
            defined = evidence_tool.validate_output(
                write_narrative_output(
                    Path(tmp) / "b",
                    narrative_report(
                        body_extra=body,
                        glossary_extra="| Ayırt edici avantaj (wedge) | Bizi seçtiren üstünlük. |\n",
                    ),
                )
            )
        self.assertTrue(any("wedge" in error for error in undefined.errors))
        self.assertTrue(defined.ok, defined.errors)

    def test_report_must_state_the_assessment_opportunity_range(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(
                write_narrative_output(Path(tmp), narrative_report(opportunity="55 / 60 / 65"))
            )
        self.assertFalse(result.ok)
        self.assertTrue(any("60 / 60 / 60" in error for error in result.errors))

    def test_body_link_absent_from_evidence_warns_without_failing(self):
        report = narrative_report(body_extra="Ek kaynak ([site](https://unknown.example/page)).\n\n")
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(write_narrative_output(Path(tmp), report))
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("unknown.example" in warning for warning in result.warnings))

    def test_report_must_show_competitor_profiles_and_channel_summary(self):
        without_channels = narrative_report().replace("Kim hâkim?", "Sahip")
        with tempfile.TemporaryDirectory() as tmp:
            no_profiles = evidence_tool.validate_output(
                write_narrative_output(Path(tmp) / "a", narrative_report(), research=[])
            )
            no_table = evidence_tool.validate_output(
                write_narrative_output(Path(tmp) / "b", without_channels)
            )
        self.assertTrue(any("competitor-profile" in error for error in no_profiles.errors))
        self.assertTrue(any("channel summary table" in error for error in no_table.errors))

    def test_standard_report_needs_market_size_and_search_results_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = evidence_tool.validate_output(
                write_narrative_output(
                    Path(tmp) / "a", narrative_report(), "standard", research=research_records("quick")
                )
            )
            few_pages = evidence_tool.validate_output(
                write_narrative_output(
                    Path(tmp) / "b",
                    narrative_report(),
                    "standard",
                    research=research_records("standard", search_pages=3),
                )
            )
        self.assertTrue(any("market-size" in error for error in missing.errors))
        self.assertTrue(any("search results page" in error for error in missing.errors))
        self.assertTrue(few_pages.ok, few_pages.errors)
        self.assertTrue(any("only 3 distinct" in warning for warning in few_pages.warnings))

    def test_deep_report_with_complete_reader_review_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(
                write_narrative_output(Path(tmp), narrative_report(), "deep")
            )
        self.assertTrue(result.ok, result.errors)
        self.assertEqual([], result.warnings)

    def test_research_modes_require_reader_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = evidence_tool.validate_output(
                write_narrative_output(Path(tmp), narrative_report(), "standard", review=False)
            )
        self.assertTrue(any("reader-review.md" in error for error in result.errors))

    def test_existing_reader_review_is_checked_before_the_narrative_cutoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            # A July Deep run without a review keeps passing: the file is required only
            # from the narrative cutoff on.
            july = write_output(root / "july", "deep")
            self.assertFalse((july / evidence_tool.READER_REVIEW_PATH).exists())
            july_result = evidence_tool.validate_output(july)
            # A review that does exist is judged whatever the analysis date.
            results = {}
            for name, issue_status in (("open", "Açık"), ("fixed", "Düzeltildi")):
                output_dir = write_output(root / name, "deep")
                set_analysis_date(output_dir, "2026-10-19")
                write_records(output_dir, review_records())
                report = (output_dir / "REPORT.md").read_text(encoding="utf-8")
                revision = evidence_tool.report_revision(report, review_records())
                (output_dir / evidence_tool.READER_REVIEW_PATH).write_text(
                    reader_review(revision, issue_status=issue_status), encoding="utf-8"
                )
                results[name] = evidence_tool.validate_output(output_dir)
        self.assertTrue(july_result.ok, july_result.errors)
        self.assertErrorWith(results["open"], "issue 1 is still open")
        self.assertTrue(results["fixed"].ok, results["fixed"].errors)

    def test_reader_review_blocks_unresolved_findings(self):
        cases = {
            "still open": current_review(issue_status="Açık"),
            "is KALDI": current_review(criterion_verdict="KALDI"),
            "does not match": current_review(claim_verdict="Hayır"),
            "without a reason": current_review(issue_status="Kabul edilmedi", issue_fix=""),
            "at least 10": current_review(claims=CLAIM_CHECKS[:9]),
            "reviewer": current_review(reviewer="[bağımsız okur]"),
        }
        for expected, text in cases.items():
            with self.subTest(expected):
                result = check_review(text)
                self.assertTrue(any(expected in error for error in result.errors), result.errors)
        rejected = check_review(current_review(issue_status="Kabul edilmedi", issue_fix="Kapsam dışı."))
        self.assertTrue(rejected.ok, rejected.errors)

    def test_report_revision_hashes_authored_report_and_evidence(self):
        records = review_records()
        report = narrative_report()
        revision = evidence_tool.report_revision(report, records)
        payload = json.dumps(
            {"report": report.strip(), "evidence": sorted(records, key=lambda record: record["evidence_id"])},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        self.assertEqual(hashlib.sha256(payload.encode("utf-8")).hexdigest(), revision)
        self.assertRegex(revision, r"\A[0-9a-f]{64}\Z")
        loaded = [dict(record, __line__=line) for line, record in enumerate(reversed(records), 1)]
        self.assertEqual(revision, evidence_tool.report_revision(report, loaded))
        for same in (
            evidence_tool.with_report_summary(report, valid_assessment()),
            report.replace("\n", "\r\n"),
            f"\n\n{report}\n\n",
        ):
            self.assertEqual(revision, evidence_tool.report_revision(same, records))
        edited = copy.deepcopy(records)
        edited[0]["observation"] = "Sign-ups fell after the price change"
        self.assertNotEqual(revision, evidence_tool.report_revision(report, edited))
        self.assertNotEqual(
            revision, evidence_tool.report_revision(report.replace("Talep var.", "Talep güçlü."), records)
        )

    def test_reader_review_requires_the_current_revision(self):
        records = review_records()
        report = narrative_report()
        current = check_review(current_review())
        self.assertTrue(current.ok, current.errors)
        older_report = evidence_tool.report_revision(
            narrative_report(body_extra="Eski taslak cümlesi.\n\n"), records
        )
        older_records = copy.deepcopy(records)
        older_records[0]["value"] = 2
        older_evidence = evidence_tool.report_revision(report, older_records)
        cases = {
            "missing": (reader_review(None), "has no '- İncelenen revizyon"),
            "malformed": (reader_review("abc123"), "İncelenen revizyon"),
            "authored text changed": (reader_review(older_report), "İncelenen revizyon is stale"),
            "evidence changed": (reader_review(older_evidence), "İncelenen revizyon is stale"),
        }
        for name, (review, expected) in cases.items():
            with self.subTest(name):
                self.assertErrorWith(check_review(review, report, records), expected)

    def test_reader_review_counts_each_claim_and_location_once(self):
        cases = {
            "one claim ten times": ((CLAIM_CHECKS[0],) * 10, "checks 1 unique claim(s); at least 10 required"),
            "nine and a repeat": (
                CLAIM_CHECKS[:9] + DUPLICATE_CHECKS[1:2],
                "checks 9 unique claim(s); at least 10 required",
            ),
            "nine and every repeat": (
                CLAIM_CHECKS[:9] + DUPLICATE_CHECKS,
                "checks 9 unique claim(s); at least 10 required",
            ),
        }
        for name, (claims, expected) in cases.items():
            with self.subTest(name):
                result = check_review(current_review(claims=claims))
                self.assertErrorWith(result, expected)
                self.assertErrorWith(result, "repeats claim check 1 (same claim and location)")
        # Exact, Turkish upper-case, whitespace, Markdown and other-record copies of
        # row 1 are each a repeat, while the ten distinct rows still satisfy the count.
        complete = check_review(current_review(claims=CLAIM_CHECKS + DUPLICATE_CHECKS))
        for row in range(11, 11 + len(DUPLICATE_CHECKS)):
            self.assertErrorWith(complete, f"claim check {row} repeats claim check 1")
        self.assertFalse(any("unique claim(s)" in error for error in complete.errors), complete.errors)

    def test_reader_review_accepts_distinct_claims_backed_by_one_record(self):
        result = check_review(current_review(claims=SAME_RECORD_CHECKS))
        self.assertTrue(result.ok, result.errors)

    def test_reader_review_claim_checks_must_cite_known_evidence(self):
        def with_second_row(ids):
            claims = list(CLAIM_CHECKS)
            claims[1] = (claims[1][0], claims[1][1], ids)
            return current_review(claims=claims)

        unknown = check_review(with_second_row("claim-demand-behavior claim-demand-signups"))
        self.assertErrorWith(unknown, "claim check 2 cites unknown evidence_id(s)", "claim-demand-signups")
        self.assertFalse(
            any("unknown evidence_id(s)" in error and "claim-demand-behavior" in error for error in unknown.errors),
            unknown.errors,
        )
        self.assertErrorWith(check_review(with_second_row("")), "claim check 2 cites no evidence_id")

    def test_authored_edit_makes_review_stale_and_render_does_not_rebind_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), narrative_report(), "deep")
            review_path = output_dir / evidence_tool.READER_REVIEW_PATH
            review = review_path.read_text(encoding="utf-8")
            report_path = output_dir / "REPORT.md"
            report_path.write_text(
                report_path.read_text(encoding="utf-8").replace("Talep var.", "Talep güçlü."),
                encoding="utf-8",
            )
            render_code = run_render(output_dir)
            result = evidence_tool.validate_output(output_dir)
            rendered_review = review_path.read_text(encoding="utf-8")
        self.assertEqual(0, render_code)
        self.assertEqual(review, rendered_review)
        self.assertErrorWith(result, "İncelenen revizyon is stale")
        self.assertFalse(any("Özet" in error for error in result.errors), result.errors)

    def test_evidence_edit_makes_review_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), narrative_report(), "deep")
            records = review_records()
            records[0]["observation"] = "Sign-ups fell after the price change"
            write_records(output_dir, records)
            result = evidence_tool.validate_output(output_dir)
        self.assertErrorWith(result, "İncelenen revizyon is stale")

    def test_regenerated_summary_keeps_the_reviewed_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), narrative_report(), "deep", summary=False)
            review_path = output_dir / evidence_tool.READER_REVIEW_PATH
            review = review_path.read_text(encoding="utf-8")
            before = evidence_tool.validate_output(output_dir)
            render_code = run_render(output_dir)
            after = evidence_tool.validate_output(output_dir)
            rendered_review = review_path.read_text(encoding="utf-8")
        self.assertErrorWith(before, "no generated '## Özet'")
        self.assertFalse(any("İncelenen revizyon" in error for error in before.errors), before.errors)
        self.assertEqual(0, render_code)
        self.assertEqual(review, rendered_review)
        self.assertTrue(after.ok, after.errors)

    def test_first_summary_render_keeps_the_review_across_the_appendix_gap(self):
        # Trailing spaces, extra blank lines and CRLF before the first appendix are layout
        # the first render collapses to one blank line, not an authored edit.
        report = narrative_report().replace(
            NARRATIVE_SUMMARY + "## Ek A",
            NARRATIVE_SUMMARY.rstrip("\n") + "  \r\n \r\n\r\n\r\n## Ek A",
        )
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), report, "deep", summary=False)
            review_path = output_dir / evidence_tool.READER_REVIEW_PATH
            report_path = output_dir / "REPORT.md"
            review = review_path.read_bytes()
            revision = evidence_tool.report_revision(report, review_records())
            first_code = run_render(output_dir)
            first = report_path.read_text(encoding="utf-8")
            second_code = run_render(output_dir)
            rendered = report_path.read_text(encoding="utf-8")
            current = evidence_tool.validate_output(output_dir)
            rendered_review = review_path.read_bytes()
            report_path.write_text(rendered.replace("Talep var.", "Talep güçlü."), encoding="utf-8")
            authored_edit = evidence_tool.validate_output(output_dir)
            report_path.write_text(rendered, encoding="utf-8")
            records = review_records()
            records[0]["observation"] = "Sign-ups fell after the price change"
            write_records(output_dir, records)
            evidence_edit = evidence_tool.validate_output(output_dir)
        self.assertEqual((0, 0), (first_code, second_code))
        self.assertIn(f"Karara etkisi: z.\n\n{evidence_tool.REPORT_SUMMARY_START}", first)
        self.assertEqual(first, rendered)
        self.assertEqual(review, rendered_review)
        self.assertEqual(revision, evidence_tool.report_revision(rendered, review_records()))
        self.assertTrue(current.ok, current.errors)
        self.assertErrorWith(authored_edit, "İncelenen revizyon is stale")
        self.assertErrorWith(evidence_edit, "İncelenen revizyon is stale")

    def test_revision_command_prints_the_current_hash_and_leaves_the_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), narrative_report(), "deep")
            review_path = output_dir / evidence_tool.READER_REVIEW_PATH
            review = review_path.read_text(encoding="utf-8")
            report = (output_dir / "REPORT.md").read_text(encoding="utf-8")
            code, output = run_main("revision", output_dir)
            rendered_review = review_path.read_text(encoding="utf-8")
            records = review_records()
            records[0]["claim_id"] = ["claim-demand"]
            write_jsonl(output_dir / "data" / "evidence.jsonl", records)
            broken_code, _ = run_main("revision", output_dir)
        self.assertEqual(0, code)
        self.assertEqual(evidence_tool.report_revision(report, review_records()) + "\n", output)
        self.assertEqual(review, rendered_review)
        self.assertEqual(1, broken_code)

    def test_render_writes_summary_from_section_boxes_before_appendices(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_narrative_output(Path(tmp), narrative_report(), summary=False)
            self.assertEqual(0, run_render(output_dir))
            report = (output_dir / "REPORT.md").read_text(encoding="utf-8")
            self.assertEqual(0, run_render(output_dir))
            rerendered = (output_dir / "REPORT.md").read_text(encoding="utf-8")
            result = evidence_tool.validate_output(output_dir)
        summary = report[report.index("## Özet") : report.index("## Ek A")]
        self.assertIn("**Karar: `TEST_ONCELIKLI`**", summary)
        self.assertIn("60 / 60 / 60", summary)
        self.assertIn("- **2. Kullanıcının sorunu** — Ne öğrendik: x. Karara etkisi: z.", summary)
        self.assertNotIn("Neden önemli", summary)
        self.assertIn("Bölüm 5 (Karar ve öneri)", summary)
        self.assertEqual(report, rerendered)
        self.assertTrue(result.ok, result.errors)

    def test_summary_is_required_and_must_follow_the_section_boxes(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = evidence_tool.validate_output(
                write_narrative_output(Path(tmp) / "a", narrative_report(), summary=False)
            )
            stale_dir = write_narrative_output(Path(tmp) / "b", narrative_report())
            report_path = stale_dir / "REPORT.md"
            report = report_path.read_text(encoding="utf-8")
            report_path.write_text(report.replace("Ne öğrendik: x.", "Ne öğrendik: yeni.", 1), encoding="utf-8")
            stale = evidence_tool.validate_output(stale_dir)
        self.assertTrue(any("no generated '## Özet'" in error for error in missing.errors))
        self.assertTrue(any("'## Özet' is out of date" in error for error in stale.errors))

    def test_render_leaves_reports_without_section_boxes_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = write_output(Path(tmp))
            before = (output_dir / "REPORT.md").read_text(encoding="utf-8")
            self.assertEqual(0, run_render(output_dir))
            after = (output_dir / "REPORT.md").read_text(encoding="utf-8")
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
