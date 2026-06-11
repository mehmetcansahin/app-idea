---
description: Standard analiz (~3-4 saat) — tam pazar arastirmasi + Faz 5.5 plani
argument-hint: <app fikri/konu>
---

Konu: $ARGUMENTS

CLAUDE.md'deki **Standard** modunu bu konu icin calistir:

1. Girdi analizi + disambiguation + use case segmentasyonu
2. Paralel Grup A: App Store tarama (top 10) | Google Trends | Reddit sentiment (min 3 sorgu)
3. Paralel Grup B: Review mining (20+ kotu yorum) | Gelir kaniti (min 4 sorgu) | Fiyat matrisi | Reklam istihbarati (kalite kurali #11)
4. Puanlama — `methodology/scoring-model.md` yetkili kaynak; Dagitim Fizibilitesi dahil
5. Pazar dogrulama (4 kontrol)
6. GO/SARTLI GO ise: Faz 5.5 plani (`methodology/pre-build-validation.md`) → `06-prebuild-plan.md`
7. Rapor + cross-report karsilastirma + `output/INDEX.md` guncelle

**ZORUNLU cikti yapisi** (CLAUDE.md Standard bolumundeki dosya adlari AYNEN): `REPORT.md` + `phases/01-market-scan.md … 06-prebuild-plan.md`. Review mining AYRI dosya (03).
