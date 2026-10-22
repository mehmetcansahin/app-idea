---
description: Standard v4.0 — tam pazar arastirmasi + evidence audit + Faz 5.5 plani
argument-hint: <fikir/konu>
---

Konu: $ARGUMENTS

`AGENTS.md` Standard workflow'unu uygula. Kapsam:
`methodology/data-collection-protocol.md` Rakip kapsami ve Urun Turu tablolari.

1. Preflight + use case/arketip segmentasyonu; `product_type` (`app` | `web_saas`
   | `service`). Urun turu yalniz toplama kapsamini degistirir; arketip agirliklari
   ayni kalir.
2. Top 10 rakip/ikame ve sirket profili; urun turune gore metadata (`app` store;
   `web_saas` fiyat/plan/musteri/guvenlik-uyum/satis hareketi; `service`
   saglayici/teklif/teslim/musteri davranisi); bagimsiz basari olcumleri; pazar
   buyuklugu dagilimi; trend, community, fiyat, gelir/odeme, ad/channel (top 5
   rakip Meta/Google ATC/TikTok, `ad_library` + screenshot), organik kanal
   sahipligi (min 8 web arama sorgusu), Geo-LTV.
3. Top 5 rakip icin stratified review minimumunu uygula (`scoring-model.md` §8);
   kaynak urun turune gore: `app` App Store/Play, `web_saas` ucuncu taraf review
   platformu, `service` yerel review/marketplace. Non-app'te store metadata, store
   review ve ASO aranmaz; tek `<prefix>-collection-scope` `not_applicable` kaydi.
4. Visual intelligence (urun turune uygun yuzey) ve JTBD migration analizi yap.
5. Yokluk: karar-kritik alan/claim icin en az 3 sorgu varyanti ve 2 kaynak ailesi,
   sonra `not_found_after_protocol` ile dur; kozmetik profil alaninda tek tarama.
6. JSONL evidence kaydet; `04-scoring.md` icinde iki eksenli v4 sonucu uret. Her
   RAT varsayiminda `product_specific_evidence_ids` (masa basinda `[]`).
7. `05-validation.md` icinde Faz 7 evidence audit yap.
8. Test adayiysa `06-prebuild-plan.md` icinde RAT-bazli deney sozlesmesi yaz;
   `owner:` insan rolu, onkosullar ayri.
9. REPORT'u `templates/report-template.md` Standard ve urun turu ⚐ isaretleri ve
   `methodology/report-writing.md` kurallariyla yaz; zorunlu phase/data dosyalarini
   uret. `python3 scripts/evidence_tool.py render <output-dir>`.
10. Raporu yazmayan ayri bir alt ajana `prompt-templates.md` "Okur Incelemesi"
    prompt'uyla `data/reader-review.md` yazdir (11 olcut, en az 10 / hedef 12
    benzersiz iddia). Her sorunu duzelt ve durumunu doldur; revizyon satirina
    dokunma. Sonra ayni okura "Okur Dogrulama Turu"nu yaptir; okur guncel raporu
    okuyup kontrol ettikten sonra `python3 scripts/evidence_tool.py revision
    <output-dir>` ciktisini `- İncelenen revizyon:` satirina yazar.
11. `python3 scripts/evidence_tool.py validate <output-dir>` basarili olmadan
    tamamlanmis sayma.
12. `data/portfolio.json` yaz (`prompt-templates.md` "Portfoy Kaydi"; deney planinda
    `owner:` rolu varsa `handoff`, yoksa `null`), sonra
    `python3 scripts/portfolio_tool.py render` ve `validate`.

Insan deneyi yurutulmediyse durum PREBUILD_PENDING'dir ve devir `completed`
yazilmaz. Masa basi build karari vermez; `BUILD_SMALL` yalniz RAT'a bagli gercek
urun-spesifik E3/E4 kaydiyla mumkundur.
