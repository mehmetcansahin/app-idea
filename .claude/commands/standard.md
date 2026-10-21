---
description: Standard v4.0 — tam pazar arastirmasi + evidence audit + Faz 5.5 plani
argument-hint: <app fikri/konu>
---

Konu: $ARGUMENTS

`AGENTS.md` Standard workflow'unu uygula.

1. Preflight + use case/arketip segmentasyonu.
2. Top 10 rakip/ikame ve sirket profili; bagimsiz basari olcumleri; pazar
   buyuklugu dagilimi; trend, community, fiyat, gelir/odeme, ad/channel (top 5
   rakip, `ad_library` + screenshot), organik kanal sahipligi, Geo-LTV.
3. Top 5 rakip icin `scoring-model.md` stratified review minimumunu uygula.
4. Visual intelligence ve JTBD migration analizi yap.
5. JSONL evidence kaydet; `04-scoring.md` icinde iki eksenli v4 sonucu uret.
6. `05-validation.md` icinde Faz 7 evidence audit yap.
7. Test adayiysa `06-prebuild-plan.md` icinde RAT-bazli deney sozlesmesi yaz.
8. REPORT'u `methodology/report-writing.md` kurallariyla yaz; zorunlu phase/data
   dosyalari ve INDEX'i uret.
9. `evidence_tool.py render` ve `validate` basarili olmadan tamamlanmis sayma.

Insan deneyi yurutulmediyse durum PREBUILD_PENDING'dir. Masa basi build karari
vermez.
