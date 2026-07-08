# Indie iOS Uygulama Finansal Model Sablonu

Bu sablon, bagimsiz iOS uygulama gelistiricileri icin bottom-up gelir modelleme rehberidir.
Tum hesaplamalar gercek benchmark verilerine dayanir, ancak her uygulama farklıdir —
rakamlari kendi verinizle degistirin.

---

## 1. BOTTOM-UP GELIR MODELI

Adim adim hesaplama mantigi:

```
Aylik Organik Indirme = App Store Impression x ASO Donusum Orani
Aylik Ucretli Indirme = Reklam Butcesi / CPA
Toplam Indirme = Organik + Ucretli

Trial Baslatan = Toplam Indirme x Trial Baslama Orani
Odeme Yapan = Trial Baslatan x Trial→Paid Donusum Orani
Yeni MRR = Odeme Yapan x Aylik Fiyat (veya Yillik / 12)

Churn = Mevcut Odemeli Kullanici x Aylik Churn Orani
Net MRR = Onceki MRR + Yeni MRR - Churn MRR
```

**Ornek ile aciklama:**

```
Diyelim ki App Store'da ayda 50,000 impression aliyorsun.
ASO donusum oranin %3 → 50,000 x 0.03 = 1,500 organik indirme
Reklam butcen $300/ay, CPA $2 → 300 / 2 = 150 ucretli indirme
Toplam indirme = 1,500 + 150 = 1,650

Trial baslama orani %20 → 1,650 x 0.20 = 330 trial kullanici
Trial→Paid donusum %10 → 330 x 0.10 = 33 yeni abone
Aylik fiyat $5.99 → 33 x $5.99 = $197.67 yeni MRR

Mevcut 200 abone, aylik churn %7 → 200 x 0.07 = 14 kaybedilen abone
Churn MRR = 14 x $5.99 = $83.86
Net MRR = Onceki MRR + $197.67 - $83.86
```

---

## 2. BENCHMARK DEGERLERI (Kategori Bazli)

Asagidaki tablo endustri ortalamalarini gosterir. Kaynaklar: RevenueCat State of
Subscription Apps 2024/2025, Sensor Tower, Apple Search Ads benchmark raporlari.

**Gercek sonuclar bu aralikların disinda olabilir. Kendi verinizi topladikca bu
degerleri guncellemeniz gerekir.**

| Metrik | Genel Ortalama | Saglik | Finans | Produktivite | Lifestyle |
|--------|---------------|--------|--------|-------------|-----------|
| ASO Donusum (impression→install) | %2-5 | %2-4 | %3-5 | %3-6 | %2-4 |
| Trial Baslama Orani | %15-25 | %20-30 | %15-20 | %20-25 | %15-20 |
| Trial→Paid (haftalik trial) | %15-25 | %20-30 | %15-25 | %15-20 | %10-15 |
| Trial→Paid (aylik trial) | %5-15 | %8-15 | %5-12 | %8-12 | %5-10 |
| Aylik Churn | %5-10 | %6-10 | %4-8 | %5-9 | %8-12 |
| Yillik Churn | %40-60 | %45-60 | %35-50 | %40-55 | %50-65 |
| ARPU (aylik) | $5-15 | $8-15 | $10-20 | $5-12 | $4-10 |
| CPA (App Store Ads) | $1-5 | $4-9 | $6-13 | $1.50-3.50 | $2-5 |
| Day 1 Retention | %25-35 | %25-35 | %20-30 | %25-35 | %20-30 |
| Day 7 Retention | %10-20 | %12-20 | %10-18 | %12-18 | %8-15 |
| Day 30 Retention | %5-12 | %6-12 | %5-10 | %6-10 | %4-8 |

**Notlar:**
- Haftalik trial genelde aylik trial'dan daha yuksek donusum orani verir, cunku
  kullanicinin karar verme suresi kisadir ve "kaybetme korkusu" daha gucludur.
- Saglik kategorisi genelde en yuksek trial baslama ve donusum oranlarina sahiptir
  cunku motivasyon yuksektir (kilo verme, meditasyon, vs).
- Finans kategorisi CPA'nin en yuksek oldugu kategoridir — rekabet yogundur.
- Lifestyle kategorisi churn'un en yuksek oldugu kategoridir — kullanicilar
  kolayca alternatife gecer.

---

## 3. SENARYO ANALIZI SABLONU

Her projeksiyon uc senaryo icermeli. Tek bir rakama guvenmek en yaygin hatadir.

### 3.0 Geo-LTV / Ulke Bazli Sensitivity (v3.4)

Senaryo kurmadan once 3-5 oncelikli ulke sec. "Global yayinlarim, organik gelir" varsayimi tek basina finansal model degildir.

| Ulke/Bolge | Dil/Localization | Benchmark LTV | Tahmini CPA/CAC | LTV:CAC | App Store fiyat tier | Not / Risk |
|------------|------------------|---------------|-----------------|---------|----------------------|------------|
| US | EN | $___ (TAHMINI) | $___ | ___x | $___/ay | [ASA rekabeti, localization yok] |
| UK | EN | $___ (TAHMINI) | $___ | ___x | $___/ay | [not] |
| CA | EN/FR | $___ (TAHMINI) | $___ | ___x | $___/ay | [not] |
| TR | TR | $___ (TAHMINI) | $___ | ___x | TRY tier | [dusuk LTV / maliyet avantaji / tesvik kontrolu] |

**Veri etiketleri:**
- RevenueCat/Adapty benchmark veya Apple Search Ads bid verisi: TAHMINI
- App Store Connect / RevenueCat kendi uygulama verisi: KESIN
- Rakip localized sayfa varligi: KESIN ama LTV kaniti DEGIL

**Kural:** 80+ ulkeye yayilma varsayimi, ilk 3-5 ulkede LTV:CAC kaniti olmadan kullanilmaz. Yuksek LTV ulkeleri erisilemiyorsa veya localization/ASA rekabeti cok yuksekse, gelir modeline UYARI ekle.

### Senaryo Tanimlari

**KOTUMSER (Pessimistic)**
- Organik indirme: benchmark alt sinirinin %50'si
- Trial baslama: benchmark alt siniri
- Donusum: benchmark alt siniri
- Churn: benchmark ust siniri
- Buyume: ayda %3-5

**GERCEKCI (Realistic)**
- Organik indirme: benchmark ortalamasi
- Trial baslama: benchmark ortalamasi
- Donusum: benchmark ortalamasi
- Churn: benchmark ortalamasi
- Buyume: ayda %8-12

**IYIMSER (Optimistic)**
- Organik indirme: benchmark ust siniri
- Trial baslama: benchmark ust siniri
- Donusum: benchmark ust siniri
- Churn: benchmark alt siniri
- Buyume: ayda %15-25

### Senaryo Tablosu Sablonu

Asagidaki tabloyu kendi uygulamaniz icin doldurun:

| Metrik | Ay 1 Kot. | Ay 1 Ger. | Ay 1 Iyi. | Ay 3 Kot. | Ay 3 Ger. | Ay 3 Iyi. | Ay 6 Kot. | Ay 6 Ger. | Ay 6 Iyi. | Ay 12 Kot. | Ay 12 Ger. | Ay 12 Iyi. |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------------|------------|------------|
| Indirme | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Trial | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Yeni Paid | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Toplam Odemeli | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Churn (kisi) | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Yeni MRR | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Churn MRR | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| Net MRR | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |

---

## 4. UNIT ECONOMICS

### LTV (Lifetime Value) Hesaplama

```
LTV = ARPU x (1 / Aylik Churn Orani)
```

**Ornek:**
```
ARPU: $8/ay
Aylik Churn: %8 (0.08)
LTV = $8 x (1 / 0.08) = $8 x 12.5 = $100
```

Bu, ortalama bir abonenin uygulaman ile gecirdigi sure boyunca
toplam $100 gelir uretecegi anlamina gelir.

**Farkli churn oranlarina gore LTV ornekleri:**

| ARPU | %5 Churn | %8 Churn | %10 Churn | %15 Churn |
|------|----------|----------|-----------|-----------|
| $3.99 | $79.80 | $49.88 | $39.90 | $26.60 |
| $5.99 | $119.80 | $74.88 | $59.90 | $39.93 |
| $8.99 | $179.80 | $112.38 | $89.90 | $59.93 |
| $12.99 | $259.80 | $162.38 | $129.90 | $86.60 |

### LTV:CAC Orani — Ne Anlama Gelir?

```
CAC (Customer Acquisition Cost) = Toplam Pazarlama Harcamasi / Kazanilan Abone Sayisi

LTV:CAC Orani:
- < 1x : ZARAR — her kullanicide para kaybediyorsun. Acil dur.
- 1-2x : TEHLIKE — marjin yok, tek bir olumsuzluk seni batirabilir.
- 2-3x : DIKKAT — marjin dar ama hayatta kalabilirsin.
- 3-5x : SAGLIKLI — buyume icin yatirim yapabilirsin.
- 5x+  : MUKEMMEL — agresif buyume zamani.

Ornek:
- LTV: $100
- CAC: $25 (CPA $2, trial rate %20, conversion %10 → 1 abone icin 50 indirme x $2/indirme...
  Aslinda: CAC = CPA / (Trial Rate x Conversion Rate) = $2 / (0.20 x 0.10) = $2 / 0.02 = $100)

DIKKAT: CPA ≠ CAC! CPA indirme basina maliyettir.
CAC = CPA / (Trial Rate x Conversion Rate)

Duzeltilmis ornek:
- CPA: $2
- Trial Rate: %20
- Conversion: %15
- CAC = $2 / (0.20 x 0.15) = $2 / 0.03 = $66.67
- LTV: $100
- LTV:CAC = $100 / $66.67 = 1.5x → DIKKAT bolgesinde, iyilestirme gerek.

Eger organik kullanicilar dahil edilirse (CAC = $0):
- Toplam harcama: $300, toplam yeni abone: 33 (10 ucretli, 23 organik)
- Blended CAC = $300 / 33 = $9.09
- LTV:CAC = $100 / $9.09 = 11x → MUKEMMEL (ama organik buyume surekli mi?)
```

### Break-Even (Basabas Noktasi) Hesaplama

```
Tipik Indie Uygulama Aylik Sabit Maliyetleri:
------------------------------------------
Apple Developer Account: $99/yil = ~$8.25/ay
Hosting/Backend:
  - Firebase Spark (ucretsiz): $0/ay
  - Firebase Blaze (kucuk olcek): $5-20/ay
  - Kendi sunucun (VPS): $5-50/ay
Araclar:
  - RevenueCat: ucretsiz (ayda $2,500 MRR'a kadar)
  - Analytics (Mixpanel/Amplitude free tier): $0/ay
  - Crash Reporting (Firebase Crashlytics): $0/ay
  - Email servisi (kucuk olcek): $0-10/ay
Tasarim araclari:
  - Figma (free tier): $0/ay
Toplam minimum: ~$10/ay
Toplam gercekci: ~$30-90/ay

Apple Komisyonu:
  - Standart: %30
  - Small Business Program (yillik $1M altinda gelir): %15
  - Indie gelistirici olarak buyuk ihtimalle %15

Break-Even Hesabi:
  Net Gelir = MRR x 0.85 (Apple %15 komisyon sonrasi)
  Break-Even MRR = Sabit Maliyet / 0.85

  Sabit maliyet $50/ay ise:
  Break-Even MRR = $50 / 0.85 = $58.82

  $5.99/ay fiyat ile: $58.82 / $5.99 = ~10 abone
  $3.99/ay fiyat ile: $58.82 / $3.99 = ~15 abone

Sonuc: Indie bir uygulama icin break-even noktasi sasirtici derecede dusuktur.
Zor olan kisim bu aboneleri BULMAK ve TUTMAK'tir.
```

---

## 5. GELIR BUYUME MODELI

### Organik Buyume Formulu

```
Ay N Indirme = Ay 1 Indirme x (1 + Aylik Buyume Orani)^(N-1)
```

### Tipik Organik Buyume Oranlari

```
Sadece ASO (keyword optimizasyonu):        %5-10/ay
ASO + blog/icerik pazarlama:               %10-20/ay
ASO + ucretli reklam (Apple Search Ads):   %20-40/ay
ASO + sosyal medya/influencer:             %15-30/ay
Viral/PR spike sonrasi:                    Degisken — genelde spike sonrasi
                                           %60-80 dusus olur, sonra yeni
                                           baseline oncekinden %20-50 yuksek
```

### 12 Aylik Buyume Projeksiyonu Ornegi

Ay 1 indirme: 500, buyume orani: %10/ay

| Ay | Indirme | Kumulatif | Yeni Abone (%2) | Toplam Abone | MRR ($5.99) |
|----|---------|-----------|-----------------|-------------|-------------|
| 1 | 500 | 500 | 10 | 10 | $59.90 |
| 2 | 550 | 1,050 | 11 | 20 | $119.80 |
| 3 | 605 | 1,655 | 12 | 31 | $185.69 |
| 4 | 666 | 2,321 | 13 | 42 | $251.58 |
| 5 | 732 | 3,053 | 15 | 54 | $323.46 |
| 6 | 805 | 3,858 | 16 | 67 | $401.33 |
| 7 | 886 | 4,744 | 18 | 81 | $485.19 |
| 8 | 974 | 5,718 | 19 | 96 | $575.04 |
| 9 | 1,072 | 6,790 | 21 | 112 | $670.88 |
| 10 | 1,179 | 7,969 | 24 | 130 | $778.70 |
| 11 | 1,297 | 9,266 | 26 | 149 | $892.51 |
| 12 | 1,427 | 10,693 | 29 | 170 | $1,018.30 |

*Not: Bu tablo basitlestirilmistir — churn dahil edilmemistir. Gercek rakamlarda
churn'u cikarmaniz gerekir. Asagidaki Penlo orneginde churn dahil tam hesaplama vardir.*

---

## 6. ORNEK: JURNAL UYGULAMASI (PENLO)

Gercek bir uygulama uzerinden tam 12 aylik projeksiyon.

### Uygulama Bilgileri
- **Kategori:** Health & Fitness / Productivity (capraz)
- **Fiyatlandirma:** $3.99/ay, $29.99/yil ($2.50/ay), $49.99 lifetime
- **Hedef pazar:** Gunluk tutmak isteyen iOS kullanicilari
- **Dil:** Turkce + Ingilizce
- **CPA tahmini:** ~$1.50-2.50 (productivity benchmark)

### Kullanilan Benchmark Degerleri

| Parametre | Kotumser | Gercekci | Iyimser |
|-----------|----------|----------|---------|
| Ay 1 organik indirme | 200 | 500 | 1,000 |
| Aylik indirme buyumesi | %5 | %12 | %20 |
| Trial baslama orani | %15 | %22 | %30 |
| Trial→Paid donusum | %8 | %12 | %18 |
| Net donusum (indirme→paid) | %1.2 | %2.64 | %5.4 |
| Aylik churn | %10 | %7 | %5 |
| ARPU (agirlikli ortalama) | $3.50 | $4.50 | $5.50 |
| CPA (ucretli reklam, Ay 4+) | $2.50 | $2.00 | $1.50 |

*ARPU notu: ARPU $3.99'dan dusuk olabilir cunku yillik aboneler aylik
bazda $2.50 oder. Karisik ARPU genelde fiyatin %80-110'u arasindadir.*

### KOTUMSER SENARYO — 12 Aylik Projeksiyon

| Ay | Indirme | Trial | Yeni Paid | Churn | Toplam Abone | Brut MRR | Apple Sonrasi |
|----|---------|-------|-----------|-------|-------------|----------|---------------|
| 1 | 200 | 30 | 2 | 0 | 2 | $7.00 | $5.95 |
| 2 | 210 | 32 | 3 | 0 | 5 | $17.50 | $14.88 |
| 3 | 221 | 33 | 3 | 1 | 7 | $24.50 | $20.83 |
| 4 | 232 | 35 | 3 | 1 | 9 | $31.50 | $26.78 |
| 5 | 243 | 36 | 3 | 1 | 11 | $38.50 | $32.73 |
| 6 | 255 | 38 | 3 | 1 | 13 | $45.50 | $38.68 |
| 7 | 268 | 40 | 3 | 1 | 15 | $52.50 | $44.63 |
| 8 | 281 | 42 | 3 | 2 | 16 | $56.00 | $47.60 |
| 9 | 296 | 44 | 4 | 2 | 18 | $63.00 | $53.55 |
| 10 | 310 | 47 | 4 | 2 | 20 | $70.00 | $59.50 |
| 11 | 326 | 49 | 4 | 2 | 22 | $77.00 | $65.45 |
| 12 | 342 | 51 | 4 | 2 | 24 | $84.00 | $71.40 |

**Yil sonu kotumser:** 24 abone, $84 MRR, ~$71 net (Apple sonrasi)
**Toplam yillik net gelir:** ~$460

### GERCEKCI SENARYO — 12 Aylik Projeksiyon

| Ay | Indirme | Trial | Yeni Paid | Churn | Toplam Abone | Brut MRR | Apple Sonrasi |
|----|---------|-------|-----------|-------|-------------|----------|---------------|
| 1 | 500 | 110 | 13 | 0 | 13 | $58.50 | $49.73 |
| 2 | 560 | 123 | 15 | 1 | 27 | $121.50 | $103.28 |
| 3 | 627 | 138 | 17 | 2 | 42 | $189.00 | $160.65 |
| 4 | 702 | 154 | 18 | 3 | 57 | $256.50 | $218.03 |
| 5 | 786 | 173 | 21 | 4 | 74 | $333.00 | $283.05 |
| 6 | 880 | 194 | 23 | 5 | 92 | $414.00 | $351.90 |
| 7 | 986 | 217 | 26 | 6 | 112 | $504.00 | $428.40 |
| 8 | 1,104 | 243 | 29 | 8 | 133 | $598.50 | $508.73 |
| 9 | 1,236 | 272 | 33 | 9 | 157 | $706.50 | $600.53 |
| 10 | 1,385 | 305 | 37 | 11 | 183 | $823.50 | $699.98 |
| 11 | 1,551 | 341 | 41 | 13 | 211 | $949.50 | $807.08 |
| 12 | 1,737 | 382 | 46 | 15 | 242 | $1,089.00 | $925.65 |

**Yil sonu gercekci:** 242 abone, $1,089 MRR, ~$926 net (Apple sonrasi)
**Toplam yillik net gelir:** ~$5,140

### IYIMSER SENARYO — 12 Aylik Projeksiyon

| Ay | Indirme | Trial | Yeni Paid | Churn | Toplam Abone | Brut MRR | Apple Sonrasi |
|----|---------|-------|-----------|-------|-------------|----------|---------------|
| 1 | 1,000 | 300 | 54 | 0 | 54 | $297.00 | $252.45 |
| 2 | 1,200 | 360 | 65 | 3 | 116 | $638.00 | $542.30 |
| 3 | 1,440 | 432 | 78 | 6 | 188 | $1,034.00 | $878.90 |
| 4 | 1,728 | 518 | 93 | 9 | 272 | $1,496.00 | $1,271.60 |
| 5 | 2,074 | 622 | 112 | 14 | 370 | $2,035.00 | $1,729.75 |
| 6 | 2,488 | 746 | 134 | 19 | 485 | $2,667.50 | $2,267.38 |
| 7 | 2,986 | 896 | 161 | 24 | 622 | $3,421.00 | $2,907.85 |
| 8 | 3,583 | 1,075 | 194 | 31 | 785 | $4,317.50 | $3,669.88 |
| 9 | 4,300 | 1,290 | 232 | 39 | 978 | $5,379.00 | $4,572.15 |
| 10 | 5,160 | 1,548 | 279 | 49 | 1,208 | $6,644.00 | $5,647.40 |
| 11 | 6,191 | 1,857 | 334 | 60 | 1,482 | $8,151.00 | $6,928.35 |
| 12 | 7,430 | 2,229 | 401 | 74 | 1,809 | $9,949.50 | $8,457.08 |

**Yil sonu iyimser:** 1,809 abone, $9,950 MRR, ~$8,457 net (Apple sonrasi)
**Toplam yillik net gelir:** ~$39,130

### Senaryo Karsilastirma Ozeti

| Metrik | Kotumser | Gercekci | Iyimser |
|--------|----------|----------|---------|
| Yil sonu abone | 24 | 242 | 1,809 |
| Yil sonu MRR | $84 | $1,089 | $9,950 |
| Yil sonu net MRR | $71 | $926 | $8,457 |
| Toplam yillik net gelir | ~$460 | ~$5,140 | ~$39,130 |
| Break-even ayi (maliyet $50/ay) | Hic | Ay 7-8 | Ay 1-2 |

**Gerceklik kontrolu:** Cogu indie uygulama ilk yilinda kotumser ile gercekci
arasinda bir yere duser. Iyimser senaryo genelde iyi ASO + viral etki +
surekli icerik uretimi gerektirir.

---

## 7. REKLAM BUTCESI PLANLAMA

### Ilk 3 Ay Stratejisi: REKLAM YAPMA

```
Tavsiye: Ilk 3 ayda ucretli reklam YAPMA.

Neden?
1. Organik verileri topla — baseline'ini bil.
2. ASO'yu optimize et — keyword, screenshot, aciklama testleri yap.
3. Donusum hunisini iyilestir — onboarding, paywall, trial sureleri.
4. Retention'i olc — kullanicilar geri donuyor mu?
5. Ucretli trafik ile kotulugu olceklendirmek pahadir.

Ilk 3 ayda yapman gerekenler:
- App Store Connect'ten organik impression ve indirme verisi topla.
- Trial baslama ve donusum oranlarini RevenueCat'ten izle.
- Day 1, Day 7, Day 30 retention oranlarini olc.
- Paywall tasarimini en az 2-3 kez A/B test et.
- Bu veriler olmadan reklam butcesi harcamak kor ucustur.
```

### Ay 4+ Reklam Baslatma

```
Adim 1: Kucuk baslat
- Gunluk butce: $5-10
- Platform: Apple Search Ads (en dusuk CPA, en yuksek intent)
- Sure: Minimum 2 hafta (yeterli veri icin)
- Hedef: CPA'yi olc, donusum hunisini dogrula

Adim 2: ROI hesapla
- Aylik reklam butcesi: $150-300
- Beklenen indirme: Butce / CPA
- Beklenen yeni abone: Indirme x Trial Rate x Conversion Rate
- Beklenen gelir (ilk ay): Yeni abone x ARPU
- Beklenen LTV geliri: Yeni abone x LTV

Ornek:
  Butce: $300/ay
  CPA: $2.00
  Indirme: 150
  Trial Rate: %22 → 33 trial
  Conversion: %12 → 4 yeni abone
  ARPU: $4.50/ay
  Ilk ay gelir: 4 x $4.50 = $18
  LTV gelir: 4 x $80 = $320

  Ilk ay ROI: ($18 - $300) / $300 = -%94 (NEGATIF - bu normal!)
  LTV ROI: ($320 - $300) / $300 = %6.7 (POZITIF ama marjin cok dar)

Adim 3: Karar
  LTV:CAC = LTV / (CPA / Trial Rate / Conversion Rate)
  LTV:CAC = $80 / ($2 / 0.22 / 0.12) = $80 / $75.76 = 1.06x

  Bu ornekte LTV:CAC 1x civarinda → DIKKAT bolgesi.
  Donusum hunisini iyilestirmeden butceyi artirma.

Adim 4: Olceklendirme (sadece LTV:CAC > 3x ise)
  - Gunluk butceyi kademe kademe artir: $10 → $20 → $50
  - Her kademede 1 hafta bekle, CPA'yi izle
  - CPA yukseldikce dur — diminishing returns
  - Farkli keyword gruplari test et
  - Seasonal farklari goz onunde bulundur
```

### Reklam Butcesi Hesaplama Tablosu

```
Hedef yeni abone/ay = X
Gereken indirme = X / (Trial Rate x Conversion Rate)
Butce = Gereken indirme x CPA

Ornek: Ayda 20 yeni abone hedefi
  Gereken indirme = 20 / (0.22 x 0.12) = 20 / 0.0264 = 758 indirme
  Butce = 758 x $2.00 = $1,516/ay

  Bu kadar harcamaya deger mi?
  20 abone x $80 LTV = $1,600 LTV gelir
  LTV:CAC = 1.06x → Hayir, yetmez. Once donusumu iyilestir.
```

---

## 8. ONEMLI UYARILAR

Bu bolumu atlama. Burasi belki de en onemli bolum.

### Modelin Sinirlari

1. **"Bu model TAHMINDIR. Gercek rakamlar %50+ farkli olabilir."**
   Finansal model bir pusula gibidir — yonu gosterir ama tam konumu degil.
   Model ne kadar detayli olursa olsun, gerceklik her zaman surprizler icerir.

2. **"Ilk 3 ay hemen hemen her zaman projeksiyonun altinda kalir."**
   ASO etkisi zaman alir. App Store algoritmasi yeni uygulamalara hemen
   gorunurluk vermez. Ilk 90 gun "karanlik donem"dir — sabir gerektirir.

3. **"Organik buyume zaman alir — sabir gerekli."**
   %10/ay organik buyume bile ilk birkac ayda cok kucuk rakamlardir.
   500 indirme x %10 = 550. Buyuk sayilara ulasmak 6-12 ay surer.

4. **"Lifetime purchase LTV hesabini bozar — ayri modellemek gerekir."**
   Lifetime (tek seferlik) satin alma abonelik modelinin disindadir.
   LTV hesaplami = lifetime fiyat x lifetime satin alma orani + abonelik LTV.
   Lifetime genelde toplu gelir getirir ama uzun vadede abonelikten dusuktur.

5. **"Apple'in %30 komisyonunu UNUTMA."**
   (Small Business Program ile %15). Her gelir hesabinda bu kesinti
   uygulanmalidir. $1,000 MRR = $850 net gelir (SBP ile) veya $700 (standart).

6. **"Seasonal peaks (Kasim-Ocak) yillik ortalamadan cok farkli olabilir."**
   - Kasim: Black Friday indirimleri, yuksek indirme
   - Aralik: Yilbasi hediye kartlari, yeni cihaz aktivasyonu
   - Ocak: "Yeni yil kararlari" — saglik/produktivite uygulamalari icin zirve
   - Yaz aylari: Genelde dusus
   - Bu donemler yillik ortalamadan %50-200 farkli olabilir.

7. **"Churn hep var — buyuk gorununce moral bozmasin."**
   %7 aylik churn = yilda abonelerinin ~%58'ini kaybedersin.
   100 abonenle baslarsan ve yeni abone almazsan, yil sonunda 42 kalir.
   Bu normal. Herkes bunu yasiyor. Onemli olan net buyumenin pozitif olmasi.

8. **"Bir rakip ayni isi daha iyi yaparsa tum model coker."**
   Rekabet analizi surekli yapilmalidir. Model statik degil, dinamik olmalidir.

9. **"Kur farki var — Turkiye'den gelistiriyorsan maliyet avantajin var,
   ama gelirin dolar bazinda dusuk olabilir."**

---

## 9. HIZLI HESAPLAMA TABLOLARI

### "Ayda $X kazanmak icin kac abone lazim?"

Apple Small Business Program (%15 komisyon) varsayimiyla NET gelir icin
gereken abone sayilari:

| Hedef Net MRR | $3.99/ay fiyat | $6.99/ay fiyat | $9.99/ay fiyat |
|---------------|---------------|---------------|---------------|
| $100 | 30 abone | 17 abone | 12 abone |
| $250 | 74 abone | 42 abone | 30 abone |
| $500 | 148 abone | 84 abone | 59 abone |
| $1,000 | 295 abone | 169 abone | 118 abone |
| $2,000 | 590 abone | 337 abone | 236 abone |
| $5,000 | 1,474 abone | 842 abone | 589 abone |
| $10,000 | 2,948 abone | 1,683 abone | 1,178 abone |

*Hesaplama: Abone = Hedef / (Fiyat x 0.85)*

### "Ayda $X BRUT gelir icin kac abone lazim?" (Apple komisyonu oncesi)

| Hedef Brut MRR | $3.99/ay fiyat | $6.99/ay fiyat | $9.99/ay fiyat |
|----------------|---------------|---------------|---------------|
| $500 | 126 abone | 72 abone | 50 abone |
| $1,000 | 251 abone | 143 abone | 100 abone |
| $2,000 | 501 abone | 286 abone | 200 abone |
| $5,000 | 1,253 abone | 715 abone | 500 abone |
| $10,000 | 2,506 abone | 1,431 abone | 1,001 abone |

### "Bu kadar abone icin kac indirme lazim?"

Trial Rate %20 ve Trial→Paid Conversion %10 varsayimiyla
(net donusum orani: %2):

| Hedef Abone | Gereken Indirme | Aylik (12 aya yayilirsa) |
|-------------|----------------|-------------------------|
| 50 | 2,500 | ~209/ay |
| 100 | 5,000 | ~417/ay |
| 250 | 12,500 | ~1,042/ay |
| 500 | 25,000 | ~2,083/ay |
| 1,000 | 50,000 | ~4,167/ay |
| 2,500 | 125,000 | ~10,417/ay |

**Perspektif:** Ayda 4,167 indirme = gunluk ~139 indirme. Bir produktivite
uygulamasi icin bu rakam iyi ASO ve biraz da sans gerektirir. Cogu indie
uygulama bu seviyeye ulasana kadar 6-12 ay harcar.

### "Organik olarak bu kadar indirmeye ne kadar surede ulasirim?"

Ay 1'de 300 organik indirme ile baslayip farkli buyume oranlariyla:

| Buyume Orani | 500/ay | 1,000/ay | 2,500/ay | 5,000/ay |
|-------------|--------|---------|---------|---------|
| %5/ay | Ay 11 | Ay 25 | Ay 44 | Ay 58 |
| %10/ay | Ay 6 | Ay 13 | Ay 23 | Ay 30 |
| %15/ay | Ay 4 | Ay 9 | Ay 16 | Ay 21 |
| %20/ay | Ay 3 | Ay 7 | Ay 13 | Ay 17 |

---

## SONRAKI ADIMLAR

1. Bu sablondaki bos tablolari kendi uygulamaniz icin doldurun.
2. Geo-LTV tablosunda 3-5 oncelikli ulkeyi secin; global olcek varsayimini erteleyin.
3. Ilk 30 gunde gercek verilerinizi toplayin.
4. Her ay modeli gercek verilerle karsilastirin ve guncelleyin.
5. Kotumser senaryo ile planlayin, gercekci senaryo ile motive olun.
6. LTV:CAC 3x'i gecene kadar ucretli reklama baslamayin.

**Unutmayin:** En iyi finansal model bile bir tahmindir. Onemli olan modelin
kendisi degil, onu surekli guncelleyerek ogrenme surecidir.
