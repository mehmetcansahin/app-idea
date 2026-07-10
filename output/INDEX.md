# Arastirma Scoreboard

> v4.0 satirlari yalniz ayni metodoloji surumu icinde karsilastirilir. v3.x
> raporlari tarihsel kayittir; yeni skor/kanit modeline map edilmez.

| Tarih | Konu | Mod | Arketip | Firsat Skoru | Kanit | Karar | Asama | Durum | Metodoloji | Rapor |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-01 | Debt Payoff | Standard | — | — | — | SARTLI GO (tarihsel) | legacy | **LEGACY** | v3.2 | [REPORT](2026-06-01-debt-payoff/REPORT.md) |
| 2026-03-12 | Debt Payoff | Quick Scan | — | — | — | SARTLI GO (tarihsel) | legacy | **LEGACY** | v3.1 | [REPORT](2026-03-12-debt-payoff/REPORT.md) |
| 2026-03-12 | People Finder | Standard | — | — | — | ELENDIR (tarihsel) | legacy | **LEGACY** | v3.1 | [REPORT](2026-03-12-people-finder/REPORT.md) |
| 2026-03-12 | Subscription Tracker | Quick Scan | — | — | — | NO-GO (tarihsel) | legacy | **LEGACY** | v3.1 | [REPORT](2026-03-12-subscription-tracker/REPORT.md) |

## v4.0 Durumlari

| Durum | Anlam |
|---|---|
| DESK_RESEARCH_COMPLETE | Masa basi raporu bitti; build izni yok |
| PREBUILD_PENDING | Insan davranis deneyi bekliyor |
| PREBUILD_PASSED | BUILD_SMALL kosullari karsilandi |
| BUILDING | Sinirli MVP insa ediliyor |
| POSTLAUNCH | First-party kohort karari izleniyor |
| KILLED | Fatal gate veya guclu olumsuz davranis sonucu durduruldu |
| ARCHIVED | Ayni metodolojiyle daha yeni analiz var |
| LEGACY | v3.x tarihsel raporu; v4 ile karsilastirilmaz |

## Tarihsel Notlar

- Debt Payoff icin eski Faz 5.5 aksiyonu aktif backlog degildir; iki rapor da legacy'dir.
- v3.x K2/K3/final skorlari orijinal raporlarda korunur, bu tabloda v4 Firsat
  Skoru gibi gosterilmez.
- People Finder'in eski Standard raporu tarihsel output semasini kullanir.
- Yeni analizler `REPORT.md` yaninda `data/assessment.json`, `data/evidence.jsonl`
  ve `data/evidence-ledger.md` uretmelidir.
