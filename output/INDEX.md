# Arastirma Scoreboard

> Tum analizlerin merkezi ozeti. Her yeni rapor sonrasi guncellenir (CLAUDE.md "Nasil Calisir" adim 6).
> Ayni konu yeniden analiz edildiginde eski satirin Durum'u ARSIV yapilir, yeni satir eklenir.

| Tarih | Konu | Mod | K2 | K3 | Final | Karar | Durum | Rapor |
|-------|------|-----|----|----|-------|-------|-------|-------|
| 2026-06-01 | Debt Payoff | Standard (v3.2) | 56 | 0.80 | **44.8** | SARTLI GO | **FAZ 5.5 BEKLIYOR** | [REPORT](2026-06-01-debt-payoff/REPORT.md) |
| 2026-03-12 | Debt Payoff | Quick Scan | 64→59 | 0.80 | 51.2→47.2 | SARTLI GO | ARSIV (yerine 2026-06-01) | [REPORT](2026-03-12-debt-payoff/REPORT.md) |
| 2026-03-12 | People Finder | Standard | 55 | 0.307 | 16.9 | ELENDIR (K1 FAIL: regulasyon) | TERK | [REPORT](2026-03-12-people-finder/REPORT.md) |
| 2026-03-12 | Subscription Tracker | Quick Scan | 48 | 0.80 | 38.4 | NO-GO (Apple yerlesik tehdidi) | TERK | [REPORT](2026-03-12-subscription-tracker/REPORT.md) |

## Durum Lejanti

| Durum | Anlami |
|-------|--------|
| ARASTIRMA TAMAM | Rapor bitti, karar NO-GO/ELENDIR oldugu icin aksiyon yok |
| FAZ 5.5 BEKLIYOR | GO/SARTLI GO cikti; build-oncesi davranis dogrulamasi (insan-aksiyonu) bekleniyor |
| DOGRULANDI | Faz 5.5 gecti (guven >=%70 + davranis sinyali) — gelistirmeye baslanabilir |
| TERK | NO-GO/ELENDIR veya Faz 5.5 basarisiz |
| ARSIV | Ayni konunun daha yeni analizi var; bu satir tarihsel kayit |

## Acik Aksiyonlar

- [ ] **Debt Payoff Faz 5.5** (2026-06-01'den beri bekliyor): "messy-middle" icgorusunu r/debtfree + Ramsey ekosisteminde landing/fake-door + Mom-Test ile davranisla dogrula. Plan: [REPORT bolum 9](2026-06-01-debt-payoff/REPORT.md). Sonuca gore bu tabloda Durum'u DOGRULANDI veya TERK yap.

## Tarihsel Notlar

- 2026-03-12 People Finder: Standard mod ama `phases/` klasoru uretilmemis (v3.2.1 oncesi calisma; yapi kurali sonradan netlestirildi).
- 2026-06-01 Debt Payoff: `phases/` dosya adlari eski sema (03-scoring, 04-faz5.5-validation; review-mining ayri dosya degil). v3.2.1 itibariyle zorunlu adlandirma: 01-market-scan … 06-prebuild-plan.
