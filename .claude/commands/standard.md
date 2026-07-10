---
description: Standard analiz (~3-4 saat) — tam pazar arastirmasi + Faz 5.5 plani
argument-hint: <app fikri/konu>
---

Konu: $ARGUMENTS

CLAUDE.md'deki **Standard** modunu bu konu icin calistir:

1. Girdi analizi + disambiguation + use case segmentasyonu
2. Paralel Grup A: App Store tarama (top 10) | Google Trends | Reddit sentiment (min 3 sorgu)
3. Paralel Grup B: Review mining (20+ kotu yorum) | Gelir kaniti (min 4 sorgu) | Fiyat matrisi | Reklam istihbarati (kalite kurali #11) | Geo-LTV/hedef ulke kontrolu | Visual intelligence (App Store screenshot + Mobbin/Adapty Paywall Library varsa)
4. Puanlama — `methodology/scoring-model.md` yetkili kaynak; Dagitim Fizibilitesi dahil
5. Pazar dogrulama (4 kontrol)
6. GO/SARTLI GO ise: Faz 5.5 plani (`methodology/pre-build-validation.md`) → `06-prebuild-plan.md`; Sonraki Adimlar'a security preflight, AI share/secret hygiene ve basit app ise max 4 core ekran + gerekiyorsa 1 paywall/upgrade ekranlik 1 haftalik micro-MVP sprint opsiyonu ekle
7. Rapor + cross-report karsilastirma + `output/INDEX.md` guncelle

**ZORUNLU cikti yapisi** (CLAUDE.md Standard bolumundeki dosya adlari AYNEN): `REPORT.md` + `phases/01-market-scan.md … 06-prebuild-plan.md`. `02-competitor-analysis.md` Faz 4 adim 1-2 ve 4-9'u, `03-review-mining.md` yalnizca Faz 4 adim 3'u sahiplenir.
