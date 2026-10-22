---
description: Quick Scan v4.0 — app, web SaaS veya hizmet fikri icin kanitli desk-research elemesi
argument-hint: <fikir/konu>
---

Konu: $ARGUMENTS

`AGENTS.md` Quick Scan workflow'unu uygula. Kapsam:
`methodology/data-collection-protocol.md` Rakip kapsami ve Urun Turu tablolari.

1. Research Contract Preflight: segment, geo, platform/hizmet kanali, `product_type`
   (`app` | `web_saas` | `service`), birincil arketip ve modifier. Urun turu yalniz
   toplama kapsamini degistirir; arketip agirliklari ayni kalir.
2. Top 5 rakip/app-disi ikame ve sirket profili; urun turune gore metadata (`app`
   store; `web_saas` fiyat/plan/musteri/guvenlik-uyum/satis hareketi; `service`
   saglayici/teklif/teslim/musteri davranisi); trend/community; fatal gate ve
   dagitim taramasi; top 3 rakip icin Meta Ad Library + Google ATC reklam var/yok,
   aktif sayi ve hedef URL (`ad_library` + screenshot).
3. Quick'te yapma: stratified review, TikTok, mesaj acisi kodlamasi, organik kanal
   sahipligi, visual intelligence, pazar buyuklugu. Non-app'te store metadata,
   store review ve ASO aranmaz; tek `<prefix>-collection-scope` `not_applicable`
   kaydi yazilir.
4. Yokluk: karar-kritik alan/claim icin en az 3 sorgu varyanti ve 2 kaynak ailesi,
   sonra `not_found_after_protocol` ile dur; kozmetik profil alaninda tek tarama ve
   tabloda "bulunamadı".
5. Her kritik iddiayi `methodology/evidence-model.md` ile JSONL'ye kaydet.
6. `methodology/scoring-model.md` ile Firsat low/base/high + Kanit A-D hesapla; her
   RAT varsayiminda `product_specific_evidence_ids: []` (masa basinda urun-spesifik
   E3/E4 kaydi yoktur).
7. Yalniz desk karari ver: ELENDIR/BELIRSIZ/TESTE_DEGER/TEST_ONCELIKLI.
8. `templates/report-template.md` iskeletini Quick ve urun turu ⚐ isaretlerine gore
   ve `methodology/report-writing.md` kurallariyla REPORT + data/assessment.json +
   evidence.jsonl yaz.
9. `python3 scripts/evidence_tool.py render <output-dir>` ve `validate <output-dir>`.
10. `data/portfolio.json` yaz (`prompt-templates.md` "Portfoy Kaydi"; yeni kosu
    `active`, deney plani yoksa `handoff: null`), sonra
    `python3 scripts/portfolio_tool.py render` ve `validate`; `output/INDEX.md`
    uretilen bolgeleri elle duzenlenmez.

Rating fatal gate degildir. Bulunamayan veri yokluk, AI persona kullanici kaniti
sayilmaz. Insan deneyi yapilmadan devir `completed` yazilmaz. Quick artik tek dosya
degildir.
