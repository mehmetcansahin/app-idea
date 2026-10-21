# App Arastirma Metodolojisi v4.0

> Mobil app fikirlerini otomatik olarak "dogrulamak" yerine, denetlenebilir kanit
> toplayan, riskleri siralayan ve gercek insan deneyini tasarlayan karar destek
> metodolojisi.

## v4.0 Degisikligi

- K2/K3 ve kalibrasyonsuz yuzde guven kaldirildi.
- Firsat Cekiciligi 20-100 araligi ile Kanit Gucu A-D ayrildi.
- Puanlama `consumer_utility`, `consumer_subscription`, `b2b_prosumer` ve
  `marketplace_network` arketiplerine gore agirliklandirildi.
- Rating/rakip sayisi fatal gate olmaktan cikarildi.
- Bulunamayan veri yokluk, AI persona ise kullanici kaniti sayilmiyor.
- Masa basi karar dili `ELENDIR/BELIRSIZ/TESTE_DEGER/TEST_ONCELIKLI` oldu.
- Faz 5.5 risk-turune uygun deney merdivenine donustu.
- Tum modlarda JSONL evidence ledger, assessment JSON ve kaynakli Markdown zorunlu.
- Kaynak bagimsizligi `independence_root` ile izleniyor.
- v4 ciktilari bagimliliksiz validator ile kontrol ediliyor.

## Kanonik Dosyalar

| Dosya | Yetki |
|---|---|
| `scoring-model.md` | Arketipler, agirliklar, fatal gate ve karar matrisi |
| `evidence-model.md` | E0-E4, A-D, kaynak bagimsizligi ve veri sozlesmesi |
| `pre-build-validation.md` | RAT ve insan deneyleri |
| `phases.md` | Pipeline ve faz sahipligi |
| `data-collection-protocol.md` | Faz bazli toplama adimlari |
| `prompt-templates.md` | Agent prompt'lari |
| `report-writing.md` | REPORT.md dili, yapisi ve okunabilirlik kontrolleri |
| `financial-model-template.md` | Kohort ekonomi ve senaryolar |
| `launch-playbook.md` | BUILD_SMALL sonrasi SCALE/ITERATE/STOP |

Celiskide ilk uc kanonik dosya sirasiyla puanlama, kanit ve deney konusunda esas
alinir. `AGENTS.md`, `CLAUDE.md` ve `.claude/commands/` yalniz workflow ozetidir.

## Pipeline

Research Contract Preflight'tan sonra mevcut 10 faz korunur:

1. Problem havuzu
2. Keyword ve kanal cluster
3. Hizli pazar tarama
4. Rakip/davranis analizi
5. Iki eksenli degerlendirme
5.5. Build-oncesi insan dogrulamasi
6. Finalist secimi
7. Kanit denetimi ve karsi kontrol
8. Capraz karsilastirma
9. Brief ve BUILD_SMALL scope
10. Seytanin avukati

Masa basi arastirmasi build veya scale izni vermez.

## Cikti Sozlesmesi

Tum modlar:

```text
output/{YYYY-MM-DD}-{konu}/
├── REPORT.md
├── REPORT.pdf          # istege bagli; evidence_tool.py pdf
└── data/
    ├── assessment.json
    ├── evidence.jsonl
    └── evidence-ledger.md
```

Standard/Deep `phases/` dosyalarini; Deep ayrica
`data/raw-search-results.md` dosyasini uretir. REPORT.md iskeleti
`templates/report-template.md`, kurallari `report-writing.md`'dir.

## Surum Gecmisi

| Surum | Tarih | Ozet |
|---|---|---|
| v4.0 | 2026-10-20 | Rapor yazim sozlesmesi: anlati iskeleti, uc parcali bulgular, bolum sonu ozetleri, govdede kaynak baglantisi; validator kontrolleri ve PDF komutu. Skorlar degismedi |
| v4.0 | 2026-07-10 | Iki eksenli arketip modeli, evidence contract, staged decision ve validator |
| v3.4 | 2026-07-08 | Geo-LTV, visual intelligence, micro-MVP, security ve TR operasyon notlari |
| v3.3 | 2026-06-26 | RAT, JTBD, Lean Canvas ve ek pazar araclari |
| v3.2 | 2026-06-01 | Dagitim fizibilitesi ve Faz 5.5 |
| v3.1 | 2026-03-12 | Triangle rule ve veri etiketleri |

v3.x raporlari tarihsel kayittir ve `output/INDEX.md` icinde `LEGACY` olarak
etiketlenir. v3 ve v4 skorlarini dogrudan karsilastirma.
