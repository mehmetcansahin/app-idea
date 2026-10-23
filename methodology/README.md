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
| `scoring-model.md` | Preflight ve urun turu, arketipler, agirliklar, fatal gate ve karar matrisi |
| `evidence-model.md` | E0-E4, A-D, kaynak bagimsizligi, veri sozlesmesi, urun-spesifik kanit baglantisi, portfoy metadatasi ve INDEX |
| `pre-build-validation.md` | RAT, insan deneyleri, sonuc isleme ve insan deneyi devri |
| `phases.md` | Pipeline ve faz sahipligi |
| `data-collection-protocol.md` | Faz bazli toplama adimlari |
| `prompt-templates.md` | Agent prompt'lari |
| `report-writing.md` | REPORT.md dili, yapisi, okunabilirlik kontrolleri ve okur incelemesi revizyonu |
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

Masa basi arastirmasi build veya scale izni vermez. Deney plani veya devri sonuc
degildir: insan deneyi yurutulup sonucu `evidence.jsonl` ve `assessment.json`'a
islenmeden gate, karar veya durum yukselmez (`pre-build-validation.md` §1, §10).

## Cikti Sozlesmesi

Tum modlar:

```text
output/
├── INDEX.md                # portfoy gorunumu; isaretli bloklar uretilir
└── {YYYY-MM-DD}-{konu}/
    ├── REPORT.md
    ├── REPORT.pdf          # istege bagli; evidence_tool.py pdf
    └── data/
        ├── assessment.json
        ├── portfolio.json  # yasam dongusu + insan deneyi devri
        ├── evidence.jsonl
        └── evidence-ledger.md
```

Standard/Deep `phases/` dosyalarini ve `data/reader-review.md` okur incelemesini;
Deep ayrica `data/raw-search-results.md` dosyasini uretir. REPORT.md iskeleti
`templates/report-template.md`, kurallari `report-writing.md`'dir.
`data/portfolio.json` arastirma kararindan ayridir (`evidence-model.md` §11).

Komutlar:

```bash
python3 scripts/evidence_tool.py render output/{tarih}-{konu}    # ledger + Özet
python3 scripts/evidence_tool.py validate output/{tarih}-{konu}
python3 scripts/evidence_tool.py revision output/{tarih}-{konu}  # okur icin revizyon
python3 scripts/evidence_tool.py validate-all output
python3 scripts/evidence_tool.py pdf output/{tarih}-{konu}
python3 scripts/portfolio_tool.py render output                 # INDEX bloklari
python3 scripts/portfolio_tool.py validate output
```

`revision` yalniz degeri yazdirir; incelemeyi onaylamaz (`report-writing.md` §13).

## Surum Gecmisi

| Surum | Tarih | Ozet |
|---|---|---|
| v4.0 | 2026-10-23 | Rapor dili: UTF-8 ve Türkçe karakter kullanımı, tam cümle, açık özne, tutarlı terim ve anlamı koruyan son okuma kuralları belirginleştirildi. Rapor şablonu, otomatik kanıt defteri ve portföy panosu metinleri Türkçe yazımına uyarlandı. Dil düzeltmeleri gözlem, varsayım, plan, koşul ve belirsizlik ayrımını korur; skor modeli değişmedi. |
| v4.0 | 2026-10-22 | Sozlesme sertlestirmesi: `BUILD_SMALL`'in urun-spesifik kosulu RAT `product_specific_evidence_ids` ile ayni claim/fikre ait, gozlenmis, destekleyici E3/E4 first-party/deney kayitlarina baglandi; eski `product_specific_behavior` bool'u kaldirildi. Preflight `product_type` (`app`, `web_saas`, `service`) kilitler; urun turu yalniz toplama dalini degistirir, ayni arketip modeli ve agirliklar kullanilir. Assessment/evidence yapisal dogrulamasi bozuk veride traceback yerine hata verir. Okur incelemesi `İncelenen revizyon` ile Ozet haric yazar metni + sirali kanit hash'ine baglanir; ilk `## Ek` oncesi bosluk `render`'daki gibi tek bos satira normallestirilir, boylece ilk ve sonraki `render` incelemeyi bayatlatmaz; `revision` komutu yalniz degeri yazdirir, `render` onaylamaz, diger yazar metni/kanit degisikligi incelemeyi bayatlatir; tekrar eden iddia kontrolu sayilmaz (10 asgari, 12 hedef). Portfoy yasam dongusu ve insan deneyi devri `data/portfolio.json`'a ayrildi; `output/INDEX.md` isaretli bloklari `portfolio_tool.py render` ile uretilir; assessment durumundan `ARCHIVED`/`LEGACY` cikarildi. Quick ve ust modlarda deney plani sonuc sayilmaz. Gecmis assessment JSON'larinda yalniz alan gocu yapildi; metodoloji v4, agirliklar, skor, karar, kanit dereceleri ve v3 raporlari degismedi |
| v4.0 | 2026-10-20 | Rapor yazim sozlesmesi: anlati iskeleti, uc parcali bulgular, bolum sonu ozetleri, govdede kaynak baglantisi; validator kontrolleri ve PDF komutu. 2026-10-21: arastirma kaniti (rakip profili, pazar buyuklugu, arama sonucu), Standard/Deep okur incelemesi kontrolleri ve `render`'in urettigi `## Özet` bolumu. Skorlar degismedi |
| v4.0 | 2026-07-10 | Iki eksenli arketip modeli, evidence contract, staged decision ve validator |
| v3.4 | 2026-07-08 | Geo-LTV, visual intelligence, micro-MVP, security ve TR operasyon notlari |
| v3.3 | 2026-06-26 | RAT, JTBD, Lean Canvas ve ek pazar araclari |
| v3.2 | 2026-06-01 | Dagitim fizibilitesi ve Faz 5.5 |
| v3.1 | 2026-03-12 | Triangle rule ve veri etiketleri |

v3.x raporlari tarihsel kayittir ve `output/INDEX.md` icinde uretilen bloklarin
disindaki `LEGACY` satirlarinda kalir; bu bir assessment durumu degildir ve v3
raporlari degistirilmez. v3 ve v4 skorlarini dogrudan karsilastirma.
