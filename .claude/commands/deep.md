---
description: Deep v4.0 — Standard + feature, arama gorunurlugu/ASO, kohort ekonomi, brief, adversarial audit
argument-hint: <fikir/konu>
---

Konu: $ARGUMENTS

`AGENTS.md` Deep workflow'unu uygula. Kapsam:
`methodology/data-collection-protocol.md` Rakip kapsami ve Urun Turu tablolari.

1. Standard pipeline'in tamamini calistir (`product_type` dahil; top 10 rakip/profil,
   top 5 stratified review, top 5 Meta/Google ATC/TikTok, organik kanal). Okur
   incelemesi ve portfoy adimlari asagida, rapor bittikten sonra yapilir.
2. Feature matrix, visual/paywall ve arketip-bazli distribution analizi ekle.
   `08-aso-research.md`: `app` icin ASO; `web_saas` icin SEO/karsilastirma siteleri;
   `service` icin yerel arama/harita/rehber. Non-app'te dosya ASO'nun
   uygulanmadigini `<prefix>-collection-scope` `not_applicable` kaydiyla acar.
3. `financial-model-template.md` ile 3 senaryo + geo/cohort unit economics yaz;
   pre-launch benchmark'i en fazla C kanit kabul et.
4. Brief/MVP/Lean Canvas/Moat/Security yalniz karar asamasinin izin verdigi dilde
   yaz; Faz 5.5 yoksa kosullu taslak olarak isaretle.
5. Devil's advocate ile fatal gate, en riskli varsayim ve karsit evidence audit yap.
6. Tum phase dosyalari, assessment/evidence/ledger ve raw-search-results uret. Her
   RAT varsayiminda `product_specific_evidence_ids` (masa basinda `[]`).
7. REPORT'u `templates/report-template.md` Deep ve urun turu ⚐ isaretleri ve
   `methodology/report-writing.md` kurallariyla yaz;
   `python3 scripts/evidence_tool.py render <output-dir>`.
8. Raporu yazmayan ayri bir alt ajana `prompt-templates.md` "Okur Incelemesi"
   prompt'uyla `data/reader-review.md` yazdir (en az 10 / hedef 12 benzersiz
   iddia); her sorunu duzelt ve durumunu doldur, revizyon satirina dokunma. Sonra
   ayni okura "Okur Dogrulama Turu"nu yaptir; okur kontrolden sonra
   `python3 scripts/evidence_tool.py revision <output-dir>` ciktisini
   `- İncelenen revizyon:` satirina yazar.
9. `python3 scripts/evidence_tool.py validate <output-dir>`.
10. `data/portfolio.json` yaz (`prompt-templates.md` "Portfoy Kaydi"), sonra
    `python3 scripts/portfolio_tool.py render` ve `validate`.
11. Paylasim icin `python3 scripts/evidence_tool.py pdf <output-dir>` calistir.

BUILD_SMALL scope max 4 core ekran, 3 ana ozellik ve gerekiyorsa 1 paywall'dir;
karar yalniz RAT'a bagli gercek urun-spesifik E3/E4 kaydiyla verilir. Insan deneyi
yapilmadan devir `completed` yazilmaz.
