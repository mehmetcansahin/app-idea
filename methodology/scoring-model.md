# Firsat ve Karar Modeli — v4.0

> Bu dosya arketip, firsat skoru, fatal gate ve karar matrisi icin tek yetkili
> kaynaktir. Kanit dereceleri icin `evidence-model.md` esas alinir.

## 1. Research Contract Preflight

Puanlamadan once su alanlar kilitlenir:

- problem, hedef segment ve cozulmek istenen is (JTBD)
- platform ve 3-5 oncelikli geo/storefront
- analiz modu ve karar asamasi
- tek birincil arketip
- risk modifier'lari
- arastirma tarihi ve zaman-duyarli veri penceresi

Iki arketip makulse ve secim sonucu anlamli degistirecekse kullaniciya sor.

### Birincil arketipler

| Arketip | Tanim |
|---|---|
| `consumer_utility` | Tek seferlik veya donemsel is tamamlayan tuketici app'i |
| `consumer_subscription` | Surekli deger ve tekrarlanan kullanim gerektiren abonelik app'i |
| `b2b_prosumer` | Profesyonel is akisi, ekip veya bireysel uzman urunu |
| `marketplace_network` | Degeri arz, talep, topluluk veya ag likiditesine bagli urun |

Risk modifier'lari: `regulated`, `sensitive_data`, `ai_variable_cost`,
`hardware_dependency`, `children`, `platform_dependency`.

## 2. Fatal Gate'ler

Rating veya rakip sayisi fatal gate degildir. Yalniz su gate'ler kullanilir:

| Kod | Blocked kosulu |
|---|---|
| `LEGAL_BLOCKED` | Gerekli lisans, hak veya mevzuat indie olcekte asilamiyor |
| `CORE_FEASIBILITY_BLOCKED` | Cekirdek veri/API/teknoloji yasal ve pratik olarak erisilebilir degil |
| `PLATFORM_BLOCKED` | Urun App Store/Google Play kurallariyla yayinlanamiyor |
| `SAFETY_ETHICS_BLOCKED` | Kabul edilemez guvenlik, gizlilik veya zarar riski var |

Her gate `clear`, `blocked` veya `unknown` olur ve evidence ID'lerine baglanir.
`blocked` masa basinda `ELENDIR`, sonraki asamalarda `KILL`; `unknown` masa
basinda `BELIRSIZ`, Faz 5.5'te `TESTE_DEVAM` uretir.

## 3. Firsat Boyutlari ve Agirliklar

Her gerekli boyut `low`, `base`, `high` olmak uzere 1-5 araliginda puanlanir.
Olculemeyen boyut `null` olur; sifir sayilmaz ve toplam skor uretilmez.

| Boyut | Utility | Subscription | B2B/Prosumer | Marketplace |
|---|---:|---:|---:|---:|
| `problem_demand` | 25 | 20 | 25 | 20 |
| `monetization_economics` | 15 | 20 | 25 | 10 |
| `competitive_wedge` | 20 | 15 | 15 | 10 |
| `distribution_access` | 25 | 20 | 15 | 20 |
| `repeat_value_retention` | 5 | 20 | 15 | 10 |
| `timing` | 10 | 5 | 5 | 5 |
| `liquidity_cold_start` | 0 | 0 | 0 | 25 |

`Firsat skoru = SUM(agirlik * boyut_puani / 5)`

Low/base/high ayri hesaplanir ve tam sayiya yuvarlanir. Agirligi sifir olmayan
herhangi bir boyut `null` ise `opportunity=null`, sinif `insufficient_data` ve masa
basi karari `BELIRSIZ` olur.

### Boyut ankorlari

#### Problem / Talep

1. Nadir, dusuk-maliyetli veya cozulmeyen davranis yok.
2. Problem var fakat ucretsiz/status-quo yeterli, aciliyet dusuk.
3. Tekrarlanan problem + somut zaman/para workaround'u veya aktif arama var.
4. Birden fazla bagimsiz davranis sinyali, aktif goc veya yuksek problem maliyeti.
5. Segmentte olcekli odeme/goc/kullanim davranisi ve urun-spesifik guclu sinyal.

#### Monetizasyon / Ekonomi

1. Odeme davranisi yok veya marj yapisal olarak negatif.
2. Yalniz rakip fiyatlari/vendor iddialari; unit economics belirsiz.
3. En az bir dogrulanabilir odeme/workaround + makul pre-launch ekonomi.
4. Birden fazla bagimsiz islem ve olumlu payback/brut katki kaniti.
5. Urun-spesifik ucretli kohort ve surdurulebilir gerceklesen ekonomi.

#### Rekabet / Wedge

1. Yerlesik/incumbent cozum baskin; adlandirilmis icgoru yok.
2. Yalniz daha guzel/ucuz/ozellikli olma iddiasi veya yuksek switch cost.
3. Spesifik, cozulebilir missed insight ve erisilebilir alt segment var.
4. Tekrarlanan tema + dusuk/asilabilir switch cost + prototip tercih kaniti.
5. Urun-spesifik tercih ve savunulabilir avantaj davranisla kanitli.

#### Dagitim Erisimi

1. Erisilebilir kanal yok veya CAC yapisal olarak tasinamiyor.
2. Yalniz doygun head-term/genis paid kanal; wedge yok.
3. Bir ulasilabilir kanal ve adlandirilmis organik/paid hipotez var.
4. Kanalda gozlenen traction ve makul maliyet/payback sinyali var.
5. Tekrarlanabilir, birden fazla kanal ve pozitif first-party payback var.

#### Tekrarlanan Deger / Retention

1. Tek kullanim; tekrar veya tekrar eden ekonomi yok.
2. Episodik deger; geri donus nedeni zayif.
3. Dogal tekrar dongusu ve test edilebilir retention hipotezi var.
4. Concierge/prototipte en az iki dogal dongude tekrarli kullanim var.
5. First-party kohort retention'i ilgili peer benchmark'i karsiliyor/asiyor.

#### Zamanlama

1. Dusen/peaked pazar veya kapanan pencere.
2. Durgun, yapisal degisim yok.
3. Notr; yeni giris veya istikrar var.
4. Aktif goc, fiyat/platform/regulasyon degisimi davranisla goruluyor.
5. Zaman-sinirli yapisal pencere + guclu gercek davranis.

#### Likidite / Cold Start

1. Iki taraf ayni anda yoksa urun deger uretemiyor; bootstrap plani yok.
2. Genis iki tarafli pazar, yogun operasyon ve belirsiz lokal yogunluk.
3. Single-player wedge, dar geo veya tek tarafi onceden toplama plani var.
4. Arz tohumlanmis ve talebe erisim davranisla destekli.
5. Lokal/segment bazli likidite first-party islemlerle kanitli.

## 4. Skor Sinifi

- `high < 40`: `weak`
- Aralik 40 veya 60 sinirini kesiyorsa: `borderline`
- `low >= 60`: `attractive`
- Gerekli veri eksikse: `insufficient_data`

Skor basari olasiligi degildir. v4.0 agirliklari `provisional`dir. Farkli metodoloji
surumlerinin skorlari dogrudan karsilastirilmaz.

## 5. Kanit Gucu

Claim ve genel derece kurallari `evidence-model.md` dosyasindadir. Ozet:

- A/B: guclu ve bagimsiz davranis/first-party kanit
- C: yon gosterici public/qualitative kanit
- D: zayif, olculemeyen veya celiskili kanit

Genel derece, en riskli uc varsayimin minimum derecesidir. Yuzde guven uretilmez.

## 6. Karar Matrisi

### Masa basi (`desk_research`)

Sirayla uygula:

1. Herhangi bir fatal gate `blocked` -> `ELENDIR`.
2. Gate `unknown`, gerekli boyut `null` veya genel kanit D -> `BELIRSIZ`.
3. `opportunity.high < 40` ve kanit C+ -> `ELENDIR`.
4. `opportunity.low >= 60` ve kanit C+ -> `TEST_ONCELIKLI`.
5. Diger tum durumlar -> `TESTE_DEGER`.

Masa basi arastirmasi `BUILD_SMALL`, `SCALE` veya eski `GO` kararini uretemez.

### Build-oncesi (`prebuild_validation`)

1. Fatal gate `blocked` veya problem/talep E3+ ile curutulmus -> `KILL`.
2. Problem B+ fakat mevcut wedge/cozum E3+ ile curutulmus -> `PIVOT`.
3. `opportunity.low >= 60`, genel kanit B+, en riskli varsayim B+ ve en az bir
   urun-spesifik E3+ davranis varsa -> `BUILD_SMALL`.
4. Diger tum durumlar -> `TESTE_DEVAM`.

### MVP sonrasi (`post_mvp`)

- Onceden kayitli aktivasyon, retention ve ekonomi esikleri iki ardisik kohortta
  gecerse -> `SCALE`.
- Deger/aktivasyon gecer, yalniz bir alt metrik kalirsa -> `ITERATE`.
- Deger veya retention iki ardisik kohortta kalirsa -> `STOP`.
- Yeni fatal gate -> `STOP`.

## 7. Rating, Rakip ve Menopoz Kontrolu

- Rating fatal gate degildir; storefront, platform, app yasi ve erisim tarihiyle
  kaydedilen `E2/supporting` proxy'dir.
- Rating talep icin tek basina B/A olamaz.
- App rakibi yoksa Excel, WhatsApp, manuel workflow, hizmet ve web urunleri gibi
  ikameler aranir. "Rakip yok = pazar yok" otomatik kural degildir.
- Menopoz kontrolu pazar raporu ile dijital davranis arasindaki uyumsuzlugu uyarir;
  tek basina eleme yapmaz.

## 8. Review Mining

Standard/Deep'te top 5 rakip icin hedef 30, erisim sinirliysa minimum 15 yorum:

- en az 5 adet 1-2 yildiz
- en az 5 adet 3 yildiz
- en az 5 adet 4-5 yildiz

Son 12 ay, app surumu ve storefront kaydedilir. Tema orani yalniz incelenen
orneklem icin yazilir. Random sample yoksa pazar prevalansi iddia edilmez.

## 9. Cross-Report Karsilastirma

Yalniz ayni metodoloji surumu icinde karsilastir:

1. Fatal gate durumu
2. Kanit Gucu
3. Firsat skor araligi
4. En riskli varsayim ve bir sonraki test maliyeti
5. Kurucu/operasyon kisitlari

Farkli arketip skorlarini tek basina siralama gerekcesi yapma; agirlik farklarini
acikca goster.
