+# App Idea Research Agent v4.0

> Mobil app fikirleri icin denetlenebilir pazar arastirmasi ve deney tasarimi.
> Sistem bir fikri otomatik olarak "dogrulamaz"; kanit toplar, riskleri siralar ve
> bir sonraki gercek davranis testini belirler.

## Yetkili Kaynaklar

Celiskide su dosyalar esas alinir:

1. `methodology/scoring-model.md` — arketip, skor, fatal gate, karar
2. `methodology/evidence-model.md` — E0-E4, A-D, kaynak ve JSONL
3. `methodology/pre-build-validation.md` — RAT ve insan deneyleri
4. `methodology/phases.md` — pipeline ve faz sahipligi
5. `methodology/report-writing.md` — REPORT.md dili, yapisi ve okunabilirligi

Bu dosya workflow ozetidir; puanlama tablosunu kopyalamaz.

## Nasil Calisir

1. Konu, segment, platform, geo ve karar asamasini netlestir.
2. Research Contract Preflight ile birincil arketip ve risk modifier'larini sec.
3. Moda uygun arastirmayi calistir; her kritik iddiayi evidence kaydina bagla.
4. Arketip-bazli Firsat Cekiciligi low/base/high ve Kanit Gucu A-D hesapla.
5. Yalniz asamaya izin verilen karari ver.
6. Raporu `templates/report-template.md` iskeleti ve `methodology/report-writing.md`
   kurallariyla, makine-okunur dosyalarla birlikte yaz.
7. Standard/Deep: raporu yazmayan bir okura (ayri alt ajan veya kisi)
   `templates/reader-review-template.md` ile inceleme yaptir; sonuc
   `data/reader-review.md`'ye yazilir, yazar her sorunu kapatir.
8. `python3 scripts/evidence_tool.py render <output-dir>` ve sonra `validate` calistir;
   `render` ledger'i ve raporun sonundaki `## Özet` bolumunu otomatik uretir.
   Paylasim kopyasi gerekiyorsa `pdf` ile `REPORT.pdf` uret.
9. `output/INDEX.md` scoreboard'unu guncelle.

Masa basi karar enum'lari: `ELENDIR`, `BELIRSIZ`, `TESTE_DEGER`,
`TEST_ONCELIKLI`. Masa basi build/scale izni vermez.

## Modlar

### Quick Scan

Amac: Fikri ucuza elemek veya test yatirimina aday gostermek.

- Preflight + use case/ikame ayrimi
- Top 5 rakip/ikame ve sirket profili (kurulus, sahiplik, buyukluk, platform,
  fiyat), hizli trend/community, hedef geo
- Top 3 rakip icin Meta Ad Library + Google Ads Transparency var/yok, aktif sayi ve
  hedef URL (`ad_library` + screenshot)
- Fatal gate taramasi
- Iki eksenli desk assessment
- Kisa risk ve bir sonraki test

Zorunlu cikti:

```text
output/{tarih}-{konu}/
├── REPORT.md
└── data/
    ├── assessment.json
    ├── evidence.jsonl
    └── evidence-ledger.md
```

### Standard

Quick'e ek olarak:

- top 10 rakip/ikame metadata ve sirket profili; bagimsiz basari olcumleri
- top 5 icin stratified review mining
- pazar buyuklugu dagilimi (en az 3 yayinci + resmi dosya + davranis sayilari)
- gelir/odeme, fiyat, ad/channel (top 5 rakip Meta/Google/TikTok, `ad_library`
  kayitlari + screenshot), organik kanal sahipligi (web/video aramasi,
  sponsorluk, topluluk), Geo-LTV ve visual intelligence
- Faz 7 evidence audit
- test adayiysa Faz 5.5 deney sozlesmesi
- cross-report karsilastirma
- bagimsiz okur incelemesi (`data/reader-review.md`)

Zorunlu `phases/`:

```text
01-market-scan.md
02-competitor-analysis.md
03-review-mining.md
04-scoring.md
05-validation.md
06-prebuild-plan.md       # yalniz test/pivot/build adayiysa
```

Standard insan deneyi yurutulmediyse `PREBUILD_PENDING` ile biter.

### Deep

Standard'a ek olarak:

- `07-feature-matrix.md`
- `08-aso-research.md`
- `09-financial-model.md`
- `10-project-brief.md`
- `11-devils-advocate.md`
- `data/raw-search-results.md`

Brief, Faz 5.5 gecilmediyse kosullu taslaktir.

### Compare

- Her fikir icin ayni metodoloji surumunde Quick calistir.
- Fatal gate -> Kanit Gucu -> skor araligi -> top risk/test maliyeti sirasi kullan.
- Farkli arketipleri ciplak skorla siralama; agirlik farkini goster.
- Top adaylar icin Standard oner.

## Zorunlu Kalite Kurallari

- Direkt gozlem ile o gozlemden yapilan cikarimi ayir.
- Web iddiasi URL, erisim tarihi, geo/storefront/platform ve `independence_root` tasir.
- Ayni birincil raporu aktaran URL'leri bagimsiz kaynak sayma.
- Rating yalniz `E2/supporting` proxy'dir; eleme gate'i degildir.
- App rakibi yoksa manuel workflow, spreadsheet, web urunu ve hizmet ikamelerini ara.
- Bulunamayan veriyi `not_found_after_protocol` veya
  `structurally_unobservable` olarak kaydet; yokluk diye sunma.
- AI persona/sentetik kullanici `E0`dir ve karar kaniti degildir.
- Review mining'de yildiz katmanlarini, son 12 ayi, storefront ve denominator'u kaydet.
- Tema frekansini yalniz incelenen orneklem icin yaz.
- Regule/sensitive-data fikirlerde fatal gate ve security kontrolunu erken yap.
- Masa basi benchmark'i first-party veri gibi sunma.
- Reklam kutuphanesi gozlemi `ad_library` kaydidir: en fazla E2, screenshot
  artifact'i tasir, tek basina claim'i B'ye tasimaz; harcama/CPI tahmin etme.
- Farkli metodoloji surumlerinin skorlarini karsilastirma.

## Rapor Yazimi

Ayrinti ve validator kontrolleri `methodology/report-writing.md` icindedir.

- Okur konuya ilk kez bakar; her bolumun sonunda "ne ogrendim, neden onemli, karari
  nasil etkiliyor, proje mantikli mi?" sorularini yazara sormadan cevaplayabilmeli.
- Baslik ve kapsam incelenen urunu tarif eder; `Kapsam dışında kalanlar` zorunlu.
- Akis: kisa cevap → kapsam → sorun → pazar → rakipler → urun → kanallar → para →
  riskler → puanlama → karar → sinirlar → ozet. Her numarali bolum sorusuyla acilir
  ve `Bu bölümün sonucu` kutusuyla kapanir.
- `## Özet` elle yazilmaz: `render` bolum sonuc kutularindan ve `assessment.json`'dan
  eklerden once uretir; degisiklik kutularda yapilir.
- Bulgular rapor boyunca numaralanir ve uc parcalidir: ne gozlemledik, urun acisindan
  anlami, henuz varamadigimiz sonuc.
- Tam cumle; terimler ilk geciste aciklanir ve Ek A'ya yazilir; skor olcegi
  (20-100), formul ve A-D notlari anlatilir.
- Kurgusal senaryo ile gercek kullanici deneyimi ayri etiketlenir.
- Kritik iddialar govdede evidence kaydindaki URL ile baglanir; claim/evidence
  kimlikleri ve `phases/` yollari yalniz Ek C'dedir.
- Karar bolumu ne onerildigini, hangi bulgulara dayandigini, neyin belirsiz
  oldugunu ve hangi bilginin karari degistirecegini soyler.
- `validate` rakip profili, pazar buyuklugu ve arama sonucu kanitini; Standard/Deep'te
  okur incelemesini de denetler. `KALDI` olcut, `Açık` sorun veya tutmayan iddia
  varken rapor tamamlanmis sayilmaz.

## Faz 5.5

Test turu en riskli varsayima gore secilir. Landing page her fikir icin varsayilan
degildir. Waitlist en fazla E1; gercek depozito/LOI E3; ucretli tekrarli urun
davranisi E4'tur. Gorusmeler yuzde guven uretmez.

`BUILD_SMALL` icin tum kosullar `scoring-model.md` karar matrisine uymali.
Scope max 4 core ekran, 3 ana ozellik ve gerekiyorsa 1 paywall/upgrade ekranidir.

## Finans ve Post-Launch

Pre-launch LTV/CAC projeksiyonu yalniz senaryodur. First-party veri geldikce D30/D90
gerceklesen ARPPU, payback, brut katki, activation ve retention kohortlari kullanilir.
Post-MVP karar enum'lari `SCALE`, `ITERATE`, `STOP`tur.

## Default Teknik Stack

| Alan | Varsayilan |
|---|---|
| iOS | Swift + SwiftUI |
| Cross-platform | React Native (Expo) |
| State | Zustand |
| Lokal DB | MMKV / WatermelonDB |
| Sync | iCloud veya Supabase |
| Auth | Apple Sign In + Email |
| Odeme | RevenueCat |
| Analytics | PostHog |

## Legacy

Mevcut v3.x raporlari degistirme veya yeniden puanlama. `output/INDEX.md` icinde
`LEGACY` olarak tut. Yeni v4 satirlari eski skorlarla dogrudan karsilastirilmaz.
