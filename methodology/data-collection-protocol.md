# Veri Toplama Protokolu — Adim Adim Rehber

> **Problem:** Test arastirmalarinda (ornek: "alarm clock app") mevcut verinin sadece %30'u toplanabiliyor.
> Bu protokol, her arastirma fazinda HANGI sorgularin HANGI sirada yapilacagini tanimlar.
> Hedef: Veri toplama oranini %30'dan %80+'ya cikarmak.

> **Nasil Kullanilir:** Her fazda ilgili bolume git, `[DEGISKEN]` yerlerine gercek degerlerini yaz,
> sorgulari sirayla calistir, cikti formatina uygun sekilde kaydet.

---

## GENEL KURALLAR

### Kural 1: Ucgen Kurali

Hicbir kritik iddia tek kaynaga dayanmamali. Her kritik veri noktasi icin **minimum 2 bagimsiz kaynak** gerekli.

Ornek:
- "Alarmy 500K rating" → App Store sayfasindan dogrudan oku (1. kaynak) + Sensor Tower/AppFigures ile cross-check (2. kaynak)
- "Jurnal pazari buyuyor" → Grand View Research raporu (1. kaynak) + App Store'da yeni uygulama sayisinin artisi (2. kaynak)

Ucgen kurali uygulanamayan durumlar:
- App Store'dan direkt okunan veriler (rating sayisi, yildiz, fiyat) → tek kaynak yeterli, cunku birincil kaynak

### Kural 2: Veri Kalite Etiketi

Her veri noktasini asagidaki etiketlerden biriyle isaretle:

| Etiket | Anlami | Ornek | Guvenilirlik |
|--------|--------|-------|--------------|
| KESIN | Direkt gozlem, birincil kaynak | App Store rating sayisi, fiyat, yildiz | Tam guvenilir |
| TAHMINI | 3. parti tahmin veya model | Sensor Tower gelir tahmini, indirme tahmini | Orta guvenilir |
| DUSUK | Cikarim, varsayim, projeksiyon | Pazar buyuklugu projeksiyonu, gelecek trend tahmini | Dusuk guvenilir |

**Puanlama kurali:** DUSUK etiketli veriye dayanan puanlar max 3 olabilir.

### Kural 3: Zaman Damgasi

- Her veri noktasina toplama tarihini ekle
- 6 aydan eski veri "BAYAT" olarak isaretlenir
- 12 aydan eski veri puanlamada kullanilmaz, sadece referans olur
- App Store rating sayisi gibi kumulatif veriler icin "bayat" etiketi uygulanmaz

### Kural 4: "Bulamadim" da Veridir

Bir bilgiyi bulamamak, o bilginin olmadigi anlamina gelir ve bu da karar verir.

| Bulunamayan Bilgi | Sonuc |
|-------------------|-------|
| Indie gelir kaniti bulunamadi | Gelir Kaniti skoru MAX 2 |
| Reddit tartismasi bulunamadi | Talep Sinyali skoru MAX 3 |
| Google Trends verisi bulunamadi | Trend yonu "belirsiz" olarak isaretlenir |
| Pazar raporu bulunamadi | Pazar buyuklugu "bilinmiyor" olarak isaretlenir |

### Kural 5: Sorgu Dili Stratejisi

- **Ingilizce sorgular:** App Store verileri, pazar raporlari, gelir kanitleri, Reddit
- **Turkce sorgular:** Sadece Turkiye'ye ozel pazar verileri gerektiginde
- **Neden?** Uluslararasi pazari hedefliyoruz, Ingilizce kaynaklar 10x daha zengin

### Kural 6: Sorgu Basarisizlik Protokolu

Bir sorgu sonuc vermezse:
1. Keyword'leri degistirerek 2 alternatif sorgu dene
2. Hala sonuc yoksa → "Bulamadim" etiketiyle kaydet
3. 3 farkli sorgu formati denenmeden "bulunamadi" deme

### Kural 7: Watering-Hole Kesfi (Sales Safari)

Ad-hoc Reddit sorgusu yapmadan ONCE, pazarin nerede toplandigini SISTEMATIK bul. Once mecra, sonra talep okuma. Pasif gozlem > anket/gorusme (self-report guvenilmez).

Her pazar icin su sablonlari ara (Amy Hoy Sales Safari):
- "[pazar] forum" / "[pazar] subreddit" / "[pazar] community" / "[pazar] mailing list" / "[pazar] discord OR slack" / "[pazar] wiki" / "best [pazar] tools" (yorumlar)
- Bulunan her mecrada not al: insanlarin kullandigi DIL, tekrarlayan sikayet, "su araci denedim ama..." ifadeleri, sorulan sorular.

Not: Kati 7-etiketli kodlama SART degil (dogrulanmadi); sablonlari ve "once mecra bul, pasif gozle" durusunu benimse. The Mom Test (RF-16) ile birlikte calisir.

### Kural 8: Geo-LTV ve Ulke Varsayimi

Pazar "global" diye varsayilmaz. Her analizde hedef ulke/bolge acikca yazilir.

- Quick Scan: hedef geo belirsizse US/global varsayimini not et ve "Geo-LTV belirsiz" uyarisi ekle.
- Standard+: 3-5 oncelikli ulke sec; LTV/CAC, dil/ASO, odeme ve regulasyon riskini tabloya koy.
- RevenueCat/Adapty benchmark'lari TAHMINI; App Store Connect veya RevenueCat kendi app verisi KESIN'dir.
- 80+ ulkeye yayilma varsayimi, ilk 3-5 ulkede LTV:CAC kaniti olmadan finansal modele girmez.

---

## FAZ 3: HIZLI PAZAR TARAMA — Veri Toplama Protokolu

**Amac:** Her keyword cluster icin pazarin buyuklugunu ve rekabet durumunu hizlica anlamak.
**Girdi:** Keyword cluster listesi (Faz 2'den)
**Cikti:** Her cluster icin pazar durumu ozet tablosu

### Her Keyword Cluster Icin 7 Adim

#### Adim 1: App Store Lider Tespiti

```
WebSearch: "[KEYWORD] app" site:apps.apple.com
```

**Degiskenler:**
- `[KEYWORD]` = Cluster'in ana keyword'u (ornek: "alarm clock", "habit tracker", "journal")

**Ne cikarilacak:**
- Ilk 5 sonuctaki uygulama adlari
- En yuksek rating'li uygulamayi "lider" olarak isaretle
- Lider uygulamanin App Store URL'sini kaydet

**Sonuc gelmezse alternatif sorgu:**
```
WebSearch: "best [KEYWORD] app iOS"
WebSearch: "[KEYWORD] app" site:apple.com
```

---

#### Adim 2: Lider Uygulama Detaylari

```
WebFetch: https://apps.apple.com/us/app/[APP-SLUG]/id[APP-ID]
Prompt: "Extract the following data points:
1) Total iOS ratings count (exact number)
2) Average star rating (e.g., 4.7)
3) Price model: free, freemium, paid, subscription
4) All subscription/IAP tiers with prices
5) App Store category
6) Last updated date
7) Developer name
8) App size in MB
9) In-app purchase list with each price
10) First sentence of the description"
```

**Degiskenler:**
- `[APP-SLUG]` = URL'deki uygulama adi (ornek: "alarmy-alarm-clock")
- `[APP-ID]` = URL'deki numerik ID (ornek: "1163786454")

**Kayit formati:**
```
Lider: [App Adi]
Rating: [sayi] (KESIN, tarih: [bugunun tarihi])
Yildiz: [sayi]/5 (KESIN)
Fiyat: [model + detay] (KESIN)
Kategori: [kategori] (KESIN)
Son Guncelleme: [tarih] (KESIN)
Developer: [isim]
```

---

#### Adim 3: Top 3 Rakip Detaylari

Adim 1'den gelen ilk 5 sonucun **lider haricindeki ilk 3'u** icin Adim 2'yi tekrarla.

```
WebFetch: https://apps.apple.com/us/app/[RAKIP-1-SLUG]/id[RAKIP-1-ID]
Prompt: [Adim 2 ile ayni prompt]

WebFetch: https://apps.apple.com/us/app/[RAKIP-2-SLUG]/id[RAKIP-2-ID]
Prompt: [Adim 2 ile ayni prompt]

WebFetch: https://apps.apple.com/us/app/[RAKIP-3-SLUG]/id[RAKIP-3-ID]
Prompt: [Adim 2 ile ayni prompt]
```

---

#### Adim 4: Hizli Google Trends Kontrolu

```
WebSearch: "[KEYWORD] app" Google Trends interest 2024 2025 2026
```

**Ne cikarilacak:**
- Trend yonu: YUKARI / DUZ / ASAGI
- Mevsimsellik var mi? (ornek: "fitness app" Ocak'ta zirve yapar)
- Ani bir artis veya dusus var mi?

**Sonuc gelmezse alternatif sorgular:**
```
WebSearch: "[KEYWORD] app" trend popularity growth
WebSearch: "[KEYWORD]" search interest over time
```

**Mutlak hacim + breakout (B1 — Trends kor noktasi telafisi):** WebSearch ile gelen Trends verisi yalnizca GORELI ve TAHMINI'dir. Tarayici/insan erisimi varsa:
- **Glimpse** (Google Trends eklentisi): goreli grafigi MUTLAK arama hacmine + YoY buyume %'sine cevirir. "Ilgi var ama hacim yok" tuzagini (Menopoz Testi mantigi) ayirir.
- **Exploding Topics:** konunun breakout/yukselis durumunu + buyume %'sini verir → Yasam-Dongusu siniflamasini (Exploding/Regular/Peaked, CLAUDE.md Kalite Kurali #10) dogrudan besler.
- Etiket: insan eliyle Glimpse/Exploding Topics'ten okunduysa KESIN'e yakin; yalnizca WebSearch cikarimi ise TAHMINI.

---

#### Adim 5: Apple First-Party Talep Sinyali (Ucgen Kurali)

Lider rating'i TEK Talep sinyali olarak kullanma. Ikinci, first-party bir Apple sinyali ekle:

- **App Store Search Suggest (autocomplete):** Ana keyword'u arama kutusuna yazip onerilen tamamlamalari kaydet. Kullanicilarin GERCEKTEN arattigi terimleri gosterir. Claude WebSearch ile dolayli erisilir.
- **Apple Search Ads keyword popularity (5-100):** Varsa (ucretsiz ASA hesabi, SearchAds.com veya AppFigures ucretsiz arac) skoru al. Apple'in kendi verisi -- Sensor Tower gibi modellenmis degil.

**UYARI:** Apple bu sinyali ~Ekim 2025'te bozdu (yaklasik 35 altini bastiriyor, ~%77 dusus). Dusuk-hacim/niche'te zayif. Etiket TAHMINI; tek-kaynak kullanma.

---

#### Adim 6: Keyword Difficulty + Opportunity (paid arac YOK)

Talep kadar KESFEDILEBILIRLIGI de olc (bkz. scoring-model.md "Dagitim Fizibilitesi"):

- **Difficulty (0-100):** Hedef keyword'de rank alan top-10 uygulamanin rating sayilarina bak (Adim 1-3'te zaten topladin). Top-10 rating'leri yuksek = difficulty yuksek; dusuk-rating/eski/terk-edilmis uygulamalar = difficulty dusuk.
- **EK VERI yolu (B3, tercih edilen):** Tarayici/insan erisimi varsa SearchAds.com (Mobile Action, ucretsiz plan) Apple Search popularity'sini yuzeye cikarir; AppTweak (paid) difficulty/KEI dogrudan dondurur. Bu durumda rating-tahminini bu veriyle GUCLENDIR → ama Ekim 2025 bozulmasi gecerli (<35 bastiriliyor, tek-kaynak degil); etiket KESIN degil, "guclendirilmis TAHMINI".
- **Opportunity = Hacim x0.4 + (100 - Difficulty) x0.3 + Relevance x0.3** (40/30/30, ayarlanabilir).
- **Kural:** Sadece top-10'un minimum rating/popularity esigini yakalayip asabilecegin keyword'leri hedefle.

Kayit: her ana keyword icin difficulty (dusuk/orta/yuksek), kaynak (rating-tahmini / SearchAds.com-popularity) + en az 3 dusuk-difficulty alternatif keyword.

---

#### Adim 7: Hedef Geo / Geo-LTV Hizli Kontrolu

```
WebSearch: "[KATEGORI] app subscription LTV country benchmark RevenueCat Adapty"
WebSearch: "[KATEGORI] app pricing country iOS subscription"
```

**Ne cikarilacak:**
- Varsayilan hedef ulke/bolge: US / UK / CA / AU / EU / TR / global / diger
- Bu geo icin monetizasyon beklentisi: YUKSEK / ORTA / DUSUK / BELIRSIZ
- Dil/localization gereksinimi
- Odeme/regulasyon riski

**Kayit formati:**
```
Hedef Geo: [ulke/bolge]
Geo-LTV sinifi: YUKSEK / ORTA / DUSUK / BELIRSIZ (TAHMINI)
Kaynak: [RevenueCat/Adapty benchmark, App Store localized rakip, vb.]
Uyari: [varsa — hedef geo belirsiz, localization gerekir, CAC yuksek...]
```

**Kural:** Geo-LTV K2 formülünü degistirmez. Gelir ve Dagitim Fizibilitesi guvenini artiran/azaltan ek sinyaldir.

---

### Faz 3 Cikti Formati

Her cluster icin bir satir:

| Cluster | Lider | iOS Rating | Yildiz | Fiyat Modeli | Kategori | Son Guncelleme | Trend | Hedef Geo / Geo-LTV | Pazar Durumu |
|---------|-------|------------|--------|--------------|----------|----------------|-------|---------------------|--------------|
| [KEYWORD] | [App Adi] | [sayi] | [x/5] | [free/paid/sub] | [kat] | [tarih] | [Y/D/A] | [US/YUKSEK] | [DOYMUS/BUYUYOR/NIS] |

**Pazar Durumu degerlendirmesi:**
- DOYMUS: Lider 100K+ rating VE 4.5+ yildiz VE 5+ guclu rakip
- BUYUYOR: Trend yukari VE lider 50K+ rating
- NIS: Lider <50K rating VEYA belirgin bosluk var
- ERKEN: Lider <10K rating, pazar yeni olusyor

**Tahmini sure:** Cluster basina ~5 dakika, 15 cluster = ~75 dakika

### Faz 3 Kontrol Listesi

Her cluster icin:
- [ ] Lider uygulama App Store sayfasi WebFetch ile okundu
- [ ] Rating sayisi, yildiz, fiyat KESIN etiketiyle kaydedildi
- [ ] Son guncelleme tarihi kontrol edildi (6 aydan eski = bayat)
- [ ] En az 3 rakip daha tespit edildi
- [ ] Google Trends yonu kontrol edildi
- [ ] Hedef geo ve Geo-LTV hizli kontrolu kaydedildi
- [ ] Pazar durumu degerlendirmesi yapildi

---

## FAZ 4: RAKIP ANALIZI — Veri Toplama Protokolu

**Amac:** Hayatta kalan her cluster icin derinlemesine rakip analizi yapmak.
**Girdi:** Faz 3'ten gecen cluster'lar (genelde 15'ten 8'e duser)
**Cikti:** Her cluster icin rakip matrisi, sikayet analizi, fiyat/ozellik karsilastirmasi

### Her Hayatta Kalan Cluster Icin 9 Adim

#### Adim 1: Tam Rakip Listesi Olusturma

**Sorgu 1 — Blog/listicle kaynaklari:**
```
WebSearch: "best [KEYWORD] app iOS 2025 2026"
```

**Sorgu 2 — Direkt App Store:**
```
WebSearch: "[KEYWORD] app" site:apps.apple.com
```

**Sorgu 3 — Alternatif formatlari:**
```
WebSearch: "top [KEYWORD] apps iPhone"
WebSearch: "[KEYWORD] app alternatives"
```

**Hedef:** En az 5, ideal olarak 10 rakip tespit et.
Her rakip icin App Store URL'sini kaydet.

---

#### Adim 2: Her Rakip Icin Tam Metadata

Her rakip icin:

```
WebFetch: https://apps.apple.com/us/app/[RAKIP-SLUG]/id[RAKIP-ID]
Prompt: "Extract ALL of the following data points:
1) App name and developer name
2) Total iOS ratings count (exact number)
3) Average star rating
4) Full price/subscription model — list every tier:
   - Is the app free to download?
   - Monthly subscription price
   - Annual subscription price
   - Lifetime purchase price
   - Any other IAP with prices
5) App Store category (primary and secondary if visible)
6) Last updated date
7) App size in MB
8) In-app purchase list with each individual price
9) First 3 sentences of the app description
10) What's New section — last 3 update entries with dates
11) Minimum iOS version required
12) Languages supported"
```

**Kayit formati (her rakip icin):**
```
=== [APP ADI] ===
Developer: [isim]
Rating: [sayi] (KESIN, [tarih])
Yildiz: [x/5] (KESIN)
Fiyat: Free:[evet/hayir] | Aylik:[$X] | Yillik:[$X] | Lifetime:[$X]
Kategori: [birincil] / [ikincil]
Son Guncelleme: [tarih]
Boyut: [X MB]
IAP: [liste]
Aciklama: "[ilk 3 cumle]"
Son 3 Guncelleme: [tarihler + icerikler]
Min iOS: [versiyon]
Diller: [liste]
```

---

#### Adim 3: Kotu Yorum Analizi (1-2 Yildiz)

**BU ADIM KRITIK — Firsat boslugunu burada buluyoruz.**

**Sorgu 1 — App Store review'lari:**
```
WebFetch: https://apps.apple.com/us/app/[RAKIP-SLUG]/id[RAKIP-ID]
Prompt: "Find and extract ALL negative reviews (1-star and 2-star ratings). For each review provide:
1) Star rating (1 or 2)
2) Review title
3) The main complaint summarized in one sentence
4) Review date
After listing all reviews, group the complaints into categories and count how many reviews fall into each category. Sort categories by frequency (most common first)."
```

**EGER App Store'dan yeterli review gelmezse (10'dan az), alternatif kaynaklar:**

**Sorgu 2 — Reddit sikayetleri:**
```
WebSearch: "[APP ADI] complaints OR problems OR bugs reddit"
```

**Sorgu 3 — Genel review siteleri:**
```
WebSearch: "[APP ADI] review complaints problems"
```

**Sorgu 4 — Spesifik sikayet arama:**
```
WebSearch: "[APP ADI] 1 star review"
WebSearch: "[APP ADI] worst app"
```

**Minimum hedef:** Her rakip icin en az 10 kotu yorum, ideal 20+.

**Kayit formati:**
```
=== [APP ADI] — Kotu Yorum Analizi ===
Toplam okunan kotu yorum: [sayi]

Sikayet Temalari (siralamali):
1. [TEMA] — [sayi] yorum — Ornek: "[ornek yorum]"
2. [TEMA] — [sayi] yorum — Ornek: "[ornek yorum]"
3. [TEMA] — [sayi] yorum — Ornek: "[ornek yorum]"
...

En kritik bosluk: [1-2 cumle ozet]
```

---

#### Adim 4: Reddit Sentiment Analizi

Her rakip icin (en azindan top 3 rakip icin):

**Sorgu 1 — Genel sentiment:**
```
WebSearch: "[APP ADI] reddit review 2025 2026"
```

**Sorgu 2 — Alternatif arayanlar:**
```
WebSearch: "[APP ADI] alternative reddit"
```

**Sorgu 3 — Sikayet odakli:**
```
WebSearch: "[APP ADI] complaints OR problems OR issues reddit"
```

**Sorgu 4 — Goc sinyali:**
```
WebSearch: "switched from [APP ADI] reddit"
WebSearch: "leaving [APP ADI] reddit"
```

**Olcekleme — surekli izleme (B4, opsiyonel ama veri yakalamayi yukseltir):** Manuel 4-sorgu anlik bir snapshot'tir; ~%30 yakalama riski var. Daha genis kapsama icin keyword-uyari araclari kur:
- **F5Bot (UCRETSIZ):** rakip adi + "alternative to [APP]" + sikayet keyword'lerini gir → Reddit/HN'de gecince e-posta gelir.
- **Syften (~$30/ay):** 18+ toplulukta AI-filtreli, daha genis kapsam.
- (GummySearch KULLANMA — Reddit API lisansini kaybetti, Kas 2025 kapandi.)

**Her sonuc icin not al:**
- [ ] Kac kisi alternatif ariyor? (tahmini sayi)
- [ ] En sik tekrarlanan sikayet ne?
- [ ] "Switched to [BASKA APP]" ifadeleri var mi? Hangi uygulamaya geciyorlar?
- [ ] Fiyat sikayeti var mi? Ne kadar pahali bulduklar?
- [ ] Hangi ozellik en cok isteniyor ama yok?
- [ ] JTBD Forces (A3): goc NEDEN oluyor? Push (mevcuttan iten aci) + Pull (yeniye ceken vaat) vs Anxiety (yeniden korku) + Habit (eskiye aliskanlik). Goc ancak Push+Pull > Anxiety+Habit ise gercektir.

**Kayit formati:**
```
=== [APP ADI] — Reddit Sentiment ===
Incelenen thread sayisi: [sayi]
Genel sentiment: POZITIF / NOTR / NEGATIF / KARISIK
Alternatif arayanlarin sayisi: ~[sayi]
En sik sikayet: [tema]
Goc yonu: [hangi uygulamaya geciyorlar]
En cok istenen eksik ozellik: [ozellik]
Fiyat algisi: UCUZ / MAKUL / PAHALI / COK PAHALI
JTBD Forces (goc dinamigi):
  Push (mevcuttan iten):   [aci / sikayet]
  Pull (yeniye ceken):     [vaat / ozellik]
  Anxiety (gecis korkusu): [veri kaybi, ogrenme, fiyat...]
  Habit (eskiye baglilik): [aliskanlik, switching cost...]
  Net: Push+Pull > Anxiety+Habit MI? → goc GERCEK / FANTEZI (RF-7)
```

---

#### Adim 5: Fiyat Karsilastirma Matrisi

Adim 2'den toplanan fiyat verilerini tek tabloya birlesir:

| Uygulama | Ucretsiz | Ucretsiz Limit | Aylik ($) | Yillik ($) | Yillik/Aylik Orani | Lifetime ($) | En Pahali Ozellik |
|----------|----------|----------------|-----------|------------|---------------------|-------------|-------------------|
| [App A] | Evet/Hayir | [limit aciklamasi] | [fiyat] | [fiyat] | [oran] | [fiyat/yok] | [ozellik] |
| [App B] | ... | ... | ... | ... | ... | ... | ... |

**Ek analiz:**
- Ortalama aylik fiyat: $[X]
- Medyan aylik fiyat: $[X]
- En ucuz: [App] — $[X]/ay
- En pahali: [App] — $[X]/ay
- Lifetime sunan rakip sayisi: [X]/[toplam]
- Fiyat boslugu var mi? (ornek: $3-5 arasinda hicbir uygulama yok)

---

#### Adim 6: Ozellik Karsilastirma Matrisi

**Sorgu 1 — Karsilastirma makaleleri:**
```
WebSearch: "[KEYWORD] app comparison features 2025 2026"
```

**Sorgu 2 — Alternatif format:**
```
WebSearch: "best [KEYWORD] app features comparison"
```

**Sorgu 3 — Versus siteleri:**
```
WebSearch: "[APP A] vs [APP B] vs [APP C] features"
```

Tum rakipleri tek tabloda karsilastir:

| Ozellik | [App A] | [App B] | [App C] | [App D] | [App E] |
|---------|---------|---------|---------|---------|---------|
| [Temel Ozellik 1] | VAR/YOK | ... | ... | ... | ... |
| [Temel Ozellik 2] | VAR/YOK | ... | ... | ... | ... |
| [Gelismis Ozellik 1] | VAR/YOK | ... | ... | ... | ... |
| [Gelismis Ozellik 2] | VAR/YOK | ... | ... | ... | ... |
| [Benzersiz Ozellik 1] | VAR/YOK | ... | ... | ... | ... |

**Ozellik kategorileri:**
- **Temel:** Kategorideki her uygulamada olmasi gereken ozellikler
- **Gelismis:** Premium/pro katmaninda sunulan ozellikler
- **Benzersiz:** Sadece 1-2 uygulamada olan farklilik ozellikleri
- **Eksik:** Hicbir uygulamada olmayan ama kullanicilarin istedigi ozellikler (Adim 3-4'ten)

**Adim 6.5: 2x2 Stratejik Konumlandirma (A6)**
Ozellik/fiyat matrisi "kim ne yapiyor"u gosterir ama "bos pozisyon nerede"yi gostermez. Hedef kitlenin
EN cok onemsedigi 2 ekseni sec (ornk: Basitlik <-> Guc, Fiyat <-> Kapsam, Hiz <-> Dogruluk) ve rakipleri
bu 2x2'ye yerlestir.
```
            Yuksek [Eksen Y]
                |
   [App C]      |   [App A]
                |
  --------------+--------------  [Eksen X] dusuk -> yuksek
                |
   ( BOS? )     |   [App B, D]
                |
            Dusuk [Eksen Y]
```
- Eksenler kullanici-degeri olmali (rakip yogunlugu degil). Bos ceyrek = potansiyel wedge.
- UYARI: bos ceyrek "rakip yok = pazar yok" (RF-2) olabilir; ancak Named-Insight (Kalite Kurali #8) ile
  desteklenirse firsattir. Bos pozisyonu adlandirilmis kacirilmis icgoruyle birlikte raporla.
- Cikti: `07-feature-matrix.md` icine 2x2 (Deep modunda zorunlu; Standard'da opsiyonel).

---

#### Adim 7: Google Play Cross-Check

Her rakip icin (App Store'da buldugun ilk 5 icin):

**Once package name bul:**
```
WebSearch: "[APP ADI] android app play store"
```

**Sonra detay cek:**
```
WebFetch: https://play.google.com/store/apps/details?id=[PACKAGE-NAME]
Prompt: "Extract:
1) Total rating count
2) Average star rating
3) Download range (e.g., 1M+, 10M+)
4) Price/subscription model
5) Last updated date
6) Content rating"
```

**Degiskenler:**
- `[PACKAGE-NAME]` = Android package name (ornek: "com.alarmy.alarm")

**Karsilastirma tablosu:**

| Uygulama | iOS Rating | Android Rating | iOS Yildiz | Android Yildiz | Android Indirme | Fark Notu |
|----------|-----------|---------------|------------|----------------|----------------|-----------|
| [App A] | [sayi] | [sayi] | [x/5] | [x/5] | [aralik] | [not] |

**ONEMLI:** Buyuk farklar not alinmali. Ornekler:
- iOS'ta 100K rating, Android'da 0 → iOS-exclusive uygulama
- Android'da 10M+ indirme, iOS'ta 5K rating → iOS pazarinda bosluk olabilir
- Her iki platformda guclu → Pazar buyuk ama rekabet sert

---

#### Adim 8: Reklam Istihbarati (Ad Library)

**Amac:** Rakiplerin paid UA davranisini dogrudan gozlemle: kim reklam veriyor, ne kadar suredir, hangi mesaj acilariyla.

**ERISIM NOTU (2026-06'da test edildi):** Uc kaynak da WebFetch ile OKUNAMAZ (FB baglantiyi keser, Google/TikTok bos JS kabugu doner).
Birincil yol browser otomasyonu (Claude in Chrome). Browser yoksa WebSearch fallback kullan (etiket TAHMINI).

**Sorgu 1 — FB Ad Library keyword taramasi (pazar geneli):**
```
Browser: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[KEYWORD]&search_type=keyword_unordered
Okuma: get_page_text calisir (sayfa metni dogrudan okunur)
```
- Toplam sonuc sayisini kaydet ("~N sonuc") (KESIN)
- Ilk 20-30 reklamdan: reklamveren adi, baslama tarihi ("... tarihinde yayinlanmaya basladi"), kreatif metin, landing domain
- **GURULTU UYARISI:** Keyword aramasi genis esleme yapar (ornk "debt payoff" aramasina VA loan/mortgage reklamlari da karisir). Dogrudan rakip/app reklamlarini elle ayikla.

**Sorgu 2 — FB Ad Library advertiser taramasi (top 3-5 rakip):**
```
Browser: ayni URL, q=[RAKIP ADI] (reklamverene gore ara)
```
- Rakip basina: aktif reklam sayisi, EN ESKI aktif reklamin baslama tarihi (longevity), kac farkli kreatif/versiyon

**Sorgu 3 — Google Ads Transparency Center (top 3-5 rakip):**
```
Browser: https://adstransparency.google.com/?region=US&domain=[RAKIP-DOMAIN]
Okuma: get_page_text BOS doner — SCREENSHOT ile oku
```
- **SINIR:** SADECE advertiser/domain aramasi var, keyword aramasi YOK. Once rakip listesi (Adim 1), sonra bu adim.
- Toplam reklam sayisi (~N), dogrulanmis tuzel kisi ("Onayli"), format dagilimi (arama/gorsel/video), zaman filtresi

**Sorgu 4 — TikTok Creative Center (opsiyonel):**
```
Browser: https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en
```
- **SINIR:** Login'siz sadece 4 reklamlik genel onizleme gosterir; keyword filtre ucretsiz TikTok Business hesabi login'i ister.
  Tarayicida login'li oturum varsa kullan; yoksa bu kaynagi "erisilemedi" olarak isaretle (Kural 4).

**Fallback — Browser otomasyonu yoksa (WebSearch, etiket TAHMINI):**
```
WebSearch: "[RAKIP APP] facebook ads OR tiktok ads"
WebSearch: "[KEYWORD] app advertising facebook tiktok"
WebSearch: "[RAKIP APP] ad creative OR ad campaign"
```

**Kayit formati:**
```
=== Reklam Istihbarati — [CLUSTER] ===
Tarama tarihi: [tarih]
Erisim yolu: BROWSER / WEBSEARCH-FALLBACK
FB keyword sonuc sayisi: ~[N] (KESIN)
App/dogrudan rakip reklamvereni: VAR/YOK — [liste]

| Rakip | Platform | Aktif reklam | En eski aktif reklam | Longevity | Ana mesaj acisi |
|-------|----------|--------------|----------------------|-----------|-----------------|
| [App] | FB/Google | [N] | [tarih] | [X ay] | [aci] |

Mesaj acilari (pazar geneli): [kullanilan acilar + KULLANILMAYAN acilar]
Review sikayetleriyle kesisim: [reklamlarin vurgulamadigi ama kullanicilarin sikayet ettigi aci = wedge adayi]
Paid kanal yorumu: DOYGUN / AKTIF / BOS — [1-2 cumle]
```

**Sinyal okuma:**
- 6+ ay kesintisiz donen reklam = calisan unit economics (davranis kaniti, Mom Test uyumlu). Sirket olcegindedir; indie gelir kaniti YERINE GECMEZ.
- Lider(ler) yuzlerce aktif kreatif donduruyor = paid kanal doygun, indie CAC yarisina giremez → organik/ASO wedge SART.
- Hicbir rakip reklam vermiyor = paid UA dogrulanmamis, buyume organik bagimli (Kural 4: bulamamak da veridir).
- **KOR NOKTA:** Apple Search Ads'in kamuya acik kutuphanesi yok; iOS install reklamlarinin onemli kanali gorunmez. Raporda acikca not et.
- Harcama TUTARI hicbir kaynakta gorunmez; tutar tahmini yapma (yapilirsa DUSUK etiketi → puan MAX 3).

---

#### Adim 9: Visual / Product Flow Intelligence

**Amac:** Rakiplerin onboarding, paywall ve App Store screenshot mesajlarini inceleyerek satis/pattern bosluklarini bulmak.

**Birincil kaynak — App Store screenshot'lari:**
```
WebFetch: https://apps.apple.com/us/app/[RAKIP-SLUG]/id[RAKIP-ID]
Prompt: "Extract screenshot captions/messages and summarize the first 3 screenshot value propositions."
```

**Tamamlayici kaynaklar (browser/insan erisimi gerekebilir):**
- Mobbin: top 3-5 rakibin onboarding, paywall, permission prompt ve upgrade akislari
- Adapty Paywall Library: benzer kategoride paywall pattern referanslari
- Codia AI Design / screenshot-to-Figma: secilen referans screenshot'i uretim taslagina cevirmek icin, pazar kaniti olarak degil

**Kayit formati:**
```
=== Visual Intelligence — [CLUSTER] ===
Tarama tarihi: [tarih]
Kaynaklar: App Store / Mobbin / Adapty Paywall Library / Codia

| Rakip | Kaynak | Incelenen akis | Ilk vaat / CTA | Paywall pattern | Bos kalan aci |
|-------|--------|----------------|-----------------|-----------------|---------------|
| [App] | [kaynak] | Onboarding/Paywall/Screenshot | [mesaj] | [pattern] | [wedge] |

Sonuc:
- Tekrarlanan mesaj/pattern:
- Rakiplerin kullanmadigi ama review/reddit'te acik olan aci:
- MVP/paywall hipotezi:
```

**Kural:** Visual intelligence, review/Reddit/fiyat kanitiyla desteklenmedikce Rekabet 4-5 icin tek basina yeterli degildir. Kopyalama yasak; sadece pattern ve bosluk cikar.

---

### Faz 4 Cikti Formati

Her cluster icin asagidaki 8 ciktiyi hazirla:

1. **Rakip Matrisi** (5-10 satir x 12+ kolon)
2. **Kotu Yorum / Sikayet Ozeti** (top 5 tema + frekans sayilari)
3. **Fiyat Karsilastirma Tablosu** (tum rakipler + ortalama/medyan analizi)
4. **Ozellik Karsilastirma Tablosu** (temel/gelismis/benzersiz/eksik kategorileri)
5. **Reddit Sentiment Ozeti** (her rakip icin sentiment + goc sinyalleri)
6. **iOS vs Android Karsilastirma** (cross-platform fark analizi)
7. **Reklam Istihbarati Ozeti** (rakip basina longevity + mesaj acilari + paid kanal yorumu)
8. **Visual Intelligence Ozeti** (screenshot/onboarding/paywall pattern + bos acilar)

**Tahmini sure:** Cluster basina ~30 dakika, 8 cluster = ~4 saat

### Faz 4 Kontrol Listesi

Her cluster icin:
- [ ] En az 5 rakip tam metadata toplandi (Adim 2)
- [ ] Her rakip icin App Store sayfasi WebFetch ile okundu
- [ ] Her rakip icin en az 10 kotu yorum okundu (1-2 yildiz) (Adim 3)
- [ ] Toplam en az 20 kotu yorum analiz edildi
- [ ] Top 3 sikayet temasi belirlendi ve frekans sayildi
- [ ] Reddit sentiment aramalari yapildi — minimum 3 farkli sorgu formatı (Adim 4)
- [ ] "Switched to..." veya alternatif arayan kullanicilar tespit edildi
- [ ] Fiyat karsilastirma tablosu tamamlandi — ortalama ve medyan hesaplandi (Adim 5)
- [ ] Ozellik karsilastirma tablosu tamamlandi — eksik ozellikler isaretlendi (Adim 6)
- [ ] Google Play cross-check yapildi — en az top 5 rakip icin (Adim 7)
- [ ] iOS vs Android farkliliklari not alindi
- [ ] Reklam istihbarati taramasi yapildi — FB keyword + top rakip advertiser, erisim yolu not edildi (Adim 8)
- [ ] Visual intelligence tamamlandi — App Store screenshot + varsa Mobbin/Adapty Paywall Library/Codia not edildi (Adim 9)

---

## FAZ 5: FIRSAT PUANLAMA — Veri Dogrulama Protokolu

**Amac:** Cluster'lari puanlarken her puanin arkasinda somut veri oldugunu garantilemek.
**Kural:** Duygusal puanlama YASAK. Her puan bir veriye dayanmali.
**Girdi:** Faz 3 ve Faz 4'ten toplanan tum veriler
**Cikti:** Dogrulanmis puanlama tablosu + veri kaynaklari

### Her Puanlama Kriteri Icin Dogrulama

#### Kriter 1: Talep Sinyali

**Kullanilacak veriler (onceden toplanmis olmali):**
```
Kaynak 1: Lider rating sayisi → FAZ 3 Adim 2'den (KESIN)
Kaynak 2: Google Trends yonu → FAZ 3 Adim 4'ten (KESIN)
Kaynak 3: Reddit tartisma yogunlugu → FAZ 4 Adim 4'ten (TAHMINI)
```

**Puanlama skalasi:**
- 5: Lider 200K+ rating VE trend yukari VE Reddit'te aktif tartisma
- 4: Lider 100K+ rating VE (trend yukari VEYA Reddit aktif)
- 3: Lider 50K+ rating VEYA (trend yukari VE Reddit tartismasi var)
- 2: Lider 10K-50K rating, trend duz
- 1: Lider <10K rating, trend asagi veya belirsiz

**Eksik veri durumu:**
- Google Trends verisi bulunamadiysa → max puan 4
- Reddit tartismasi bulunamadiysa → max puan 3
- Lider uygulama tespit edilemediyse → max puan 2

---

#### Kriter 2: Gelir Kaniti

**Ek veri toplama GEREKLI (Faz 3-4'te toplanmamis olabilir):**

**Sorgu 1 — IndieHackers:**
```
WebSearch: "[KATEGORI] app indie developer revenue indiehackers"
```

**Sorgu 2 — Twitter/X #buildinpublic:**
```
WebSearch: "[KATEGORI] app revenue #buildinpublic twitter"
```

**Sorgu 3 — Genel gelir arama:**
```
WebSearch: "[KATEGORI] app how much money earn indie"
```

**Sorgu 4 — Spesifik platform:**
```
WebSearch: "[KATEGORI] app MRR solo developer"
WebSearch: "[KATEGORI] iOS app revenue report"
```

**Sorgu 5 — Satin-alma/exit komparasyonlari (B5, survivorship'i dengeler):**
```
WebSearch: "[KATEGORI] app acquire.com OR flippa asking price revenue"
WebSearch: "[KATEGORI] app for sale revenue multiple flippa"
WebSearch: "[KATEGORI] business starter story revenue"
```
- IndieHackers/Twitter "survivorship bias"lidir (sadece kazananlar paylasir). Acquire.com/Flippa ilanlari +
  Starter Story kategori MEDYANI bunu dengeler.
- **Ima edilen aylik gelir = satis fiyati / carpan.** Carpan AYLIK ise dogrudan (or. $48K / 36x aylik kar
  ≈ $1.3K/ay); YILLIK ise once 12'ye bol (or. $48K / 3x yillik = $16K/yil ÷ 12 ≈ $1.3K/ay). Carpan gelir mi
  kar mi belirt; KAR carpanindan cikan rakami GELIR ankoruna sayma.
- **Kanit turu:** KAPANMIS satis = davranis (ankora sayilabilir). CANLI/satilmamis ILAN (asking price +
  satici-beyani) = IDDIA → TAHMINI, MAX 3 (kac ilan olursa olsun; Mom Test/RF-16).

**Sorgu 6 — Geo-LTV / ulke bazli monetizasyon:**
```
WebSearch: "[KATEGORI] app subscription LTV country benchmark RevenueCat"
WebSearch: "[KATEGORI] app paywall conversion country Adapty"
WebSearch: "[KATEGORI] app Apple Search Ads CPA country"
```
- 3-5 hedef ulkeyi sec ve her biri icin LTV/CAC sinifini not et.
- Benchmark verisi TAHMINI'dir; first-party App Store Connect/RevenueCat verisi yoksa KESIN yazma.
- Geo-LTV sinyali Gelir puanini otomatik artirmaz; gelir kaniti ve dagitim guvenini yorumlar.

**Puanlama skalasi:**
- 5: 3+ bagimsiz indie gelir kaniti, ortalama $5K+/ay
- 4: 2+ indie gelir kaniti, ortalama $2K+/ay
- 3: 1 indie gelir kaniti VEYA lider uygulamanin premium modeli acikca calisiyor
- 2: Gelir kaniti yok AMA lider uygulama premium fiyatli (dolaylı kanit)
- 1: Gelir kaniti yok VE lider uygulama ucretsiz/reklam destekli

**OVERRIDE KURALI:** Hicbir indie gelir kaniti bulunamadiysa → skor MAX 2. (B5 istisnasi: KAPANMIS satis
komparasyonu ima edilen aylik gelire cevrilip ilgili ankora eslesirse override KALKAR; ankor + bagimsiz-kaynak
SAYISI kapisi gecerli kalir [skor 4 = 2+, skor 5 = 3+]. Canli/satilmamis ilan = iddia → TAHMINI, hala MAX 3.
Yetkili tanim: `scoring-model.md` override tablosu.)

---

#### Kriter 3: Rekabet Boslugu

**Kullanilacak veriler (onceden toplanmis olmali):**
```
Kaynak 1: 1-2 yildiz review temalari → FAZ 4 Adim 3'ten (KESIN)
Kaynak 2: Fiyat boslugu → FAZ 4 Adim 5 fiyat tablosundan (KESIN)
Kaynak 3: Ozellik boslugu → FAZ 4 Adim 6 ozellik tablosundan (KESIN/TAHMINI)
Kaynak 4: Reddit "alternatif ariyorum" sinyalleri → FAZ 4 Adim 4'ten (TAHMINI)
```

**Puanlama skalasi:**
- 5: 3+ tekrarlanan sikayet temasi VE acik fiyat boslugu VE eksik ozellik boslugu
- 4: 2+ sikayet temasi VE (fiyat VEYA ozellik boslugu)
- 3: 1-2 sikayet temasi VEYA belirgin bir bosluk
- 2: Sikayetler var ama cozumu zor (ornek: "cok yavas" = altyapi sorunu)
- 1: Sikayetler minimal, rakipler iyi is yapiyor

---

#### Kriter 4: Retention Potansiyeli

**Ek veri toplama GEREKLI:**

**Sorgu 1 — DAU/retention verileri:**
```
WebSearch: "[APP ADI] daily active users retention rate"
```

**Sorgu 2 — Kategori benchmark:**
```
WebSearch: "[KATEGORI] app retention rate benchmark"
```

**Sorgu 3 — Alternatif sinyal — guncelleme sikligi:**
```
FAZ 4 Adim 2'deki "Son 3 Guncelleme" verilerini kullan.
```

**Puanlama skalasi:**
- 5: Gunluk kullanim kategorisi (alarm, todo, habit) VE lider sik guncelleniyor
- 4: Haftalik+ kullanim beklentisi VE lider aktif gelistirme yapiyor
- 3: Duzensiz kullanim ama tekrar eden ihtiyac (ornek: yemek tarifi)
- 2: Tek seferlik veya cok seyrek kullanim
- 1: Bir kere kullan, unut tipi uygulama

---

#### Kriter 5: Zamanlama

**Ek veri toplama GEREKLI:**

**Sorgu 1 — Pazar degisimi:**
```
WebSearch: "[KATEGORI] app market changes 2025 2026"
```

**Sorgu 2 — Lider uygulama degisiklikleri:**
```
WebSearch: "[LIDER APP] price increase OR shutdown OR acquired 2025 2026"
```

**Sorgu 3 — Yeni iOS API'leri:**
```
WebSearch: "iOS [GUNCEL_SURUM] new API features [KATEGORI]"
WebSearch: "WWDC [GUNCEL_YIL] [KATEGORI] related announcements"
(GUNCEL_SURUM/GUNCEL_YIL: arastirma tarihindeki en yeni iOS major surumu ve son WWDC yili ile doldur)
```

**Sorgu 4 — Regulasyon/trend degisimi:**
```
WebSearch: "[KATEGORI] new regulation OR law OR policy 2025 2026"
```

**Puanlama skalasi:**
- 5: Aktif pazar degisimi (lider fiyat artirdi, yeni iOS API, regulasyon degisimi)
- 4: Yakinda beklenen degisim (WWDC duyurusu, trend yukari)
- 3: Stabil pazar, belirgin zamanlama avantaji yok
- 2: Pazar olgunlasmis, yeni giris zor
- 1: Pazar kuculuyor veya yakindan buyuk bir rakip girecek

---

### Faz 5 Cikti Formati

| Cluster | Talep (1-5) | Talep Kaynagi | Gelir (1-5) | Gelir Kaynagi | Bosluk (1-5) | Bosluk Kaynagi | Retention (1-5) | Ret. Kaynagi | Zamanlama (1-5) | Zam. Kaynagi | TOPLAM |
|---------|-------------|---------------|-------------|---------------|--------------|----------------|-----------------|-------------|-----------------|-------------|--------|
| [KEYWORD] | [X] | [kaynak+etiket] | [X] | [kaynak+etiket] | [X] | [kaynak+etiket] | [X] | [kaynak+etiket] | [X] | [kaynak+etiket] | [X/25] |

**Ek not (K2 formulune dahil degil):**
| Cluster | Hedef Geo | Geo-LTV sinifi | Gelir/Dagitim Etkisi |
|---------|-----------|----------------|----------------------|
| [KEYWORD] | [US/UK/TR...] | YUKSEK/ORTA/DUSUK/BELIRSIZ | [guven artar/uyari] |

**Tahmini sure:** Cluster basina ~15 dakika, 8 cluster = ~2 saat

### Faz 5 Kontrol Listesi

- [ ] Her kriter icin veri kaynagi acikca belirtildi (KESIN/TAHMINI/DUSUK)
- [ ] Gelir kaniti icin en az 3 farkli sorgu yapildi
- [ ] Geo-LTV / hedef ulke monetizasyon kontrolu yapildi
- [ ] Override kurallari kontrol edildi (ornek: gelir kaniti yok → max 2)
- [ ] Tek kaynaga dayanan hicbir puan yok (Ucgen kurali)
- [ ] Retention icin guncelleme sikligi alternatif sinyal olarak kontrol edildi
- [ ] Zamanlama icin iOS yenilik ve pazar degisimi arandi
- [ ] DUSUK etiketli veriye dayanan puanlar max 3 ile sinirlandirildi

---

## FAZ 7: PAZAR DOGRULAMA — Veri Toplama Protokolu

**Amac:** Finalist fikirlerin gercekten iyi oldugundan emin olmak.
**Girdi:** Faz 6'dan gecen finalistler (genelde 3-5 fikir)
**Cikti:** Her finalist icin 4 dogrulama raporu

### Her Finalist Fikir Icin 4 Dogrulama

#### Dogrulama 1: Gercek Rating Sayilari (Teyit)

Faz 4'te toplanan verilerin GUNCEL oldugunu dogrula:

```
WebFetch: https://apps.apple.com/us/app/[TOP-1-SLUG]/id[TOP-1-ID]
Prompt: "Extract: total rating count, average star rating, last updated date"

WebFetch: https://apps.apple.com/us/app/[TOP-2-SLUG]/id[TOP-2-ID]
Prompt: [ayni]

WebFetch: https://apps.apple.com/us/app/[TOP-3-SLUG]/id[TOP-3-ID]
Prompt: [ayni]

WebFetch: https://apps.apple.com/us/app/[TOP-4-SLUG]/id[TOP-4-ID]
Prompt: [ayni]

WebFetch: https://apps.apple.com/us/app/[TOP-5-SLUG]/id[TOP-5-ID]
Prompt: [ayni]
```

**UCGEN KURALI ISTISNASI:** App Store birincil kaynak oldugu icin tek kaynak yeterli.

**Kayit formati:**
```
=== Rating Dogrulama — [FIKIR ADI] ===
Dogrulama Tarihi: [tarih]
| Uygulama | Faz 4 Rating | Guncel Rating | Fark | Guncel Yildiz |
| [App 1] | [eski] | [yeni] | [+/-X] | [x/5] |
| [App 2] | ... | ... | ... | ... |

Buyuk fark var mi? [EVET/HAYIR]
Not: [aciklama]
```

---

#### Dogrulama 2: Indie Gelir Kaniti (Derinlemesine)

**Bu dogrulama FAZ 5'ten daha kapsamli olmali. En az 4 farkli sorgu formatı kullan.**

**Sorgu 1 — IndieHackers platformu:**
```
WebSearch: "[KATEGORI] indie app revenue 2025 2026 indiehackers"
```

**Sorgu 2 — IndieHackers direkt:**
```
WebSearch: "[KATEGORI] app indiehackers revenue report"
```

**Sorgu 3 — Twitter/X #buildinpublic:**
```
WebSearch: "[KATEGORI] app #buildinpublic revenue monthly"
```

**Sorgu 4 — Solo developer arama:**
```
WebSearch: "[KATEGORI] solo developer app income earnings"
```

**Sorgu 5 — Blog/medium arama:**
```
WebSearch: "[KATEGORI] app revenue case study indie developer blog"
```

**Sorgu 6 — Spesifik rakip gelir arama:**
```
WebSearch: "[LIDER APP ADI] revenue earnings how much"
```

**Sorgu 7 — Satin-alma/exit komparasyonu (B5):**
```
WebSearch: "[KATEGORI] app acquire.com OR flippa asking price revenue"
WebSearch: "[KATEGORI] business starter story revenue median"
```

**En az 4 farkli sorgu yap. Bulamazsan → "Kanit bulunamadi" yaz.**

**Her bulunan kanit icin kayit formati:**
```
=== Gelir Kaniti #[N] ===
Kim: [developer adi/username VEYA "Flippa/Acquire ilani"]
Uygulama: [uygulama adi]
Gelir: [aylik/yillik miktar]   (komparasyon ise: ima edilen MRR = satis fiyati / beyan carpan)
Kaynak: [URL veya platform adi]
Tarih: [ne zaman paylandi]
Guvenilirlik: KESIN (kendi bildirimi, detayli) / TAHMINI (kendi bildirimi/ilan, yuvarlak sayi) / DUSUK (anonim veya 3. parti)
Kategori uyumu: [bizim kategorimizle ne kadar alakali? 1-5]
```

**Bulunamazsa:**
```
=== Gelir Kaniti Arama Sonucu ===
Yapilan sorgu sayisi: [sayi]
Sonuc: KANIT BULUNAMADI
Etki: Gelir Kaniti puani MAX 2 ile sinirlandirildi (B5: Acquire/Flippa/Starter Story komparasyonu da denendi mi? Ima edilen MRR ankora eslesiyorsa override kalkar — scoring-model.md)
Yorum: [neden bulunamadigi hakkinda tahmin — pazar yeni mi, nihai mi, gizlilik kulturu mu]
```

---

#### Dogrulama 3: Kullanici Goc Sinyali

**Sorgu 1 — Alternatif arama:**
```
WebSearch: "[LIDER APP] alternative 2025 2026"
```

**Sorgu 2 — Reddit goc sinyali:**
```
WebSearch: "leaving [LIDER APP] reddit"
```

**Sorgu 3 — Fiyat sikayeti:**
```
WebSearch: "[LIDER APP] too expensive reddit"
```

**Sorgu 4 — Abonelik iptali:**
```
WebSearch: "[LIDER APP] cancelled subscription reddit"
```

**Sorgu 5 (eger ilk 4 yeterli sonuc vermezse):**
```
WebSearch: "[LIDER APP] vs [RAKIP] reddit"
```

**Sorgu 6 (eger ilk 4 yeterli sonuc vermezse):**
```
WebSearch: "best alternative to [LIDER APP]"
```

**Sorgu 7 — Genel goc sinyali:**
```
WebSearch: "[KATEGORI] app switching users frustrated"
```

**Kayit formati:**
```
=== Kullanici Goc Analizi — [FIKIR ADI] ===
Lider uygulama: [App Adi]
Incelenen kaynak sayisi: [sayi]

Goc sinyali GUCLU / ORTA / ZAYIF / YOK

Kanitlar:
1. [Kaynak URL/platform] — "[alinti veya ozet]" — Tarih: [tarih]
2. [Kaynak URL/platform] — "[alinti veya ozet]" — Tarih: [tarih]
3. ...

Goc nedenleri (siralamali):
1. [neden] — [kac farkli kaynakta goruldu]
2. [neden] — [kac farkli kaynakta goruldu]
3. ...

Nereye goc ediyorlar:
- [App A] — [kac kisi bahsetti]
- [App B] — [kac kisi bahsetti]

Bosluk: Goc edecek iyi bir alternatif var mi, yok mu?
```

---

#### Dogrulama 4: Pazar Raporu Cross-Check + Menopoz Testi

**Sorgu 1 — Pazar buyuklugu:**
```
WebSearch: "[KATEGORI] app market size 2025 2026"
```

**Sorgu 2 — Buyume orani:**
```
WebSearch: "[KATEGORI] app market growth CAGR forecast"
```

**Sorgu 3 — Bolgeler:**
```
WebSearch: "[KATEGORI] app market by region north america europe"
```

**MENOPOZ TESTI — Pazar raporu bulduysan uygula:**

Mantik: Pazar raporu rakamlari gercek App Store verileriyle uyusmali.

```
Test Degiskenleri:
- Rapor pazar buyuklugu: $[X] milyar
- Lider uygulama iOS rating: [sayi]
- Top 5 toplam iOS rating: [sayi]

Kontrol 1: Rating/Milyar orani
- $[X]B pazar / [Y] lider rating = [oran]
- Kiyaslama: Jurnal pazari $5.7B / 115K rating = 49,565 — MAKUL
- Kiyaslama: Menopoz pazari $4.2B / 890 rating = 4,719,101 — UYUMSUZ

Kontrol 2: Mantik testi
- Bu pazar buyuklugu B2C mobil uygulama gelirini mi, yoksa tum sektoru mu kapsıyor?
- Ornek: "Sleep market $100B" = tum yatak/ilac/cihaz sektoru, mobil app degil

Sonuc: UYUMLU / UYUMSUZ / BELIRSIZ
```

**Kayit formati:**
```
=== Pazar Dogrulama — [FIKIR ADI] ===
Pazar buyuklugu (rapor): $[X]B (TAHMINI, kaynak: [rapor adi])
Lider rating: [sayi] (KESIN, App Store)
Rating/Milyar orani: [sayi]
Menopoz Testi: GECTI / KALDI / UYGULANAMADI
Buyume orani (CAGR): %[X] (TAHMINI, kaynak: [rapor adi])
Hedef segment buyuklugu: $[X]M (DUSUK, cikarim)
Not: [onemli notlar]
```

---

### Faz 7 Cikti Formati

Her finalist icin:
1. Rating dogrulama tablosu
2. Gelir kaniti listesi veya "bulunamadi" raporu
3. Kullanici goc analizi
4. Pazar dogrulama + Menopoz Testi sonucu
5. **GENEL KARAR:** DOGRULANDI / KISMI DOGRULAMA / DOGRULANAMADI

**Tahmini sure:** Finalist basina ~45 dakika, 5 finalist = ~3.5 saat

### Faz 7 Kontrol Listesi

Her finalist icin:
- [ ] Top 5 uygulamanin gercek rating sayilari App Store'dan teyit edildi
- [ ] Faz 4'teki verilerle karsilastirildi, buyuk fark varsa not alindi
- [ ] Indie gelir kaniti en az 4 farkli sorgu formatiyla arandi
- [ ] Bulunan her kanit icin guvenilirlik etiketi verildi
- [ ] Bulunamadiysa "KANIT BULUNAMADI" acikca yazildi ve skor sinirlandirildi
- [ ] Kullanici goc sinyali en az 4 farkli sorgu ile arandi
- [ ] Goc nedenleri siralanip frekans sayildi
- [ ] Pazar raporu arandi
- [ ] Pazar raporu bulunduysa Menopoz Testi uygulanidi
- [ ] Ucgen kurali her kritik iddia icin saglandi
- [ ] GENEL KARAR verildi (DOGRULANDI / KISMI / DOGRULANAMADI)

---

## FAZ 9: PROJE BRIEF — ASO Veri Toplama Protokolu

**Amac:** Secilen fikir icin App Store Optimization verilerini toplamak.
**Girdi:** Faz 8'den secilen tek finalist
**Cikti:** Keyword listesi, rakip ASO analizi, screenshot/visual intelligence analizi, micro-MVP/security/tesvik guardrail notlari

### Adim 1: Keyword Arastirmasi

**Sorgu 1 — Ana keyword autocomplete:**
```
WebSearch: "[ANA KEYWORD] app" — autocomplete onerileri
```

**Sorgu 2 — Alternatif keyword'ler:**
```
WebSearch: "[ANA KEYWORD] app alternatives"
```

**Sorgu 3 — Blog keyword kaliplari:**
```
WebSearch: "best [KATEGORI] app 2026"
```

**Sorgu 4 — Long-tail keyword'ler:**
```
WebSearch: "[ANA KEYWORD] app for [SPESIFIK KULLANIM]"
```

**Sorgu 5 — Rakip keyword'leri:**
```
WebSearch: "[RAKIP APP ADI] app similar"
```

**Sorgu 6 — Iliskili kategoriler:**
```
WebSearch: "[ANA KEYWORD] OR [SYNONYM 1] OR [SYNONYM 2] app iOS"
```

**Kayit formati:**
```
=== Keyword Arastirmasi ===

Ana Keyword'ler (yuksek hacim, yuksek rekabet):
1. [keyword] — Kaynak: [nereden bulundu]
2. [keyword] — Kaynak: [nereden bulundu]

Orta Keyword'ler (orta hacim, orta rekabet):
1. [keyword] — Kaynak: [nereden bulundu]
2. ...

Long-tail Keyword'ler (dusuk hacim, dusuk rekabet):
1. [keyword phrase] — Kaynak: [nereden bulundu]
2. ...

Rakip Keyword'leri (rakiplerin kullandigi):
1. [keyword] — Kullanan: [rakip adi]
2. ...
```

---

### Adim 2: Rakip ASO Analizi

Her rakip (top 5) icin App Store sayfasindan cikar:

```
WebFetch: https://apps.apple.com/us/app/[RAKIP-SLUG]/id[RAKIP-ID]
Prompt: "Extract the following ASO-related information:
1) Full app title (exact text)
2) Subtitle (exact text, if visible)
3) First 3 sentences of the description
4) All keywords that appear in title + subtitle
5) Category placement
6) Any promotional text visible"
```

**Kayit formati:**
```
=== Rakip ASO — [APP ADI] ===
Title: "[tam metin]"
   → Keyword'ler: [title'dan cikan keyword'ler]
Subtitle: "[tam metin]"
   → Keyword'ler: [subtitle'dan cikan keyword'ler]
Aciklama (ilk 3 cumle): "[metin]"
   → Keyword'ler: [aciklamadan cikan keyword'ler]
Kategori: [kategori]
Tahmin edilen keyword stratejisi: [analiz]
```

---

### Adim 3: Screenshot Analizi

Her rakip (top 3) icin:

```
WebFetch: https://apps.apple.com/us/app/[RAKIP-SLUG]/id[RAKIP-ID]
Prompt: "Describe the first 3 app preview screenshots in detail:
For each screenshot:
1) What text/headline is shown on the screenshot?
2) What feature or benefit does it highlight?
3) What is the primary color scheme?
4) Is it a mockup or actual app UI?
5) What emotion or value proposition does it convey?"
```

**Kayit formati:**
```
=== Screenshot Analizi — [APP ADI] ===

Screenshot 1:
  Baslik: "[metin]"
  Ozellik: [vurgulanan ozellik]
  Renk: [renk semasi]
  Tip: MOCKUP / GERCEK UI
  Mesaj: [deger onerisi]

Screenshot 2: [ayni format]
Screenshot 3: [ayni format]

Genel ASO stratejisi: [analiz]
```

---

### Adim 4: ASO Strateji Cikarimi

Tum verileri birlestirerek:

```
=== ASO Strateji Onerisi ===

Onerilen Title: "[max 30 karakter]"
Onerilen Subtitle: "[max 30 karakter]"
Hedef Keyword'ler (oncelik sirasina gore):
1. [keyword] — Neden: [aciklama]
2. [keyword] — Neden: [aciklama]
3. ...

Screenshot 1 onerisi: [ne gostermeli]
Screenshot 2 onerisi: [ne gostermeli]
Screenshot 3 onerisi: [ne gostermeli]

Rakiplerden farklilasma noktasi: [ne]
```

---

### Adim 5: Paywall / Onboarding Pattern Referansi

Faz 4 Adim 9 visual intelligence verisini kullan. Eksikse top 3 rakip icin tamamla.

**Kaynaklar:**
- App Store screenshot'lari (KESIN)
- Mobbin onboarding/paywall akislari (TAHMINI/tamamlayici)
- Adapty Paywall Library (pattern referansi)
- Codia AI Design / screenshot-to-Figma (uretim yardimi; pazar kaniti degil)

**Cikti:**
```
=== Paywall / Onboarding Pattern Onerisi ===
Ilk deger ani: [kullanici ilk 60 sn'de ne gorecek]
Paywall tetigi: [hangi aksiyon/ekran]
Default plan: [aylik/yillik/lifetime]
Kopyalanmayacak referanslar: [hangi pattern'ler, neden]
Farkli mesaj acisi: [review/reddit'ten gelen bos aci]
```

---

### Adim 6: Micro-MVP Sprint Uygunlugu

```
Micro-MVP sprint uygunlugu: EVET / HAYIR
Kosul kontrolu:
- Faz 5.5 durumu:
- Teknik/regulasyon karmasikligi:
- Max 5 ekran mumkun mu:
- Paywall erken eklenebilir mi:

1 haftalik sprint:
Pazartesi: keyword/final scope
Sali: proje kurulumu + onboarding
Carsamba: max 5 ekran MVP
Persembe: paywall + market-fit copy
Cuma: test + screenshots
Cumartesi: App Store submit
Pazar: marketing/community posts
```

Bu sprint sadece Faz 5.5 davranisla dogrulanmis, dusuk karmasiklikli app'ler icin uygulama planidir; K3 MVP suresi ankori degismez.

---

### Adim 7: Security Preflight + AI Share Hygiene

**Checklist:**
- [ ] Admin endpoint'leri auth/role check ile korunuyor
- [ ] User content ID-only URL ile acilmiyor; token/session/ownership check var
- [ ] API key/admin token frontend bundle'a koyulmuyor; backend/proxy kullaniliyor
- [ ] Supabase RLS / Firestore rules / backend authorization kurallari yazildi ve test edildi
- [ ] Predictable ID riski kontrol edildi
- [ ] Kullanici `isAdmin`, `role`, `credits`, `subscriptionStatus` gibi korumali alanlari update edemiyor
- [ ] Public AI share linklerinde API key, admin token, private repo icerigi veya musteri verisi yok

**Cikti:** Risk bolumune "Security preflight: GECTI / EKSIK / UYGULANAMAZ" olarak yaz.

---

### Adim 8: Turkiye Tesvik / Payout Kontrolu

**Ne zaman:** Kurucu Turkiye'de sirket/operasyon yurutuyorsa, maliyetleri Turkiye'de gider yazacaksa veya tesvik kullanmayi planliyorsa.

```
WebSearch: "mobil uygulama ihracat destekleri resmi site guncel"
WebSearch: "dijital hizmet ihracati reklam komisyon destekleri resmi site"
App Store Connect UI: Agreements, Tax, and Banking > Bank Accounts / Tax Forms
```

**Kayit formati:**
```
Turkiye tesvik uygunlugu: UYGUN / BELIRSIZ / UYGUN DEGIL
Resmi kaynak: [URL, tarih]
Kapsam: [reklam/tool/komisyon/diger]
Hard-coded tutar kullanildi mi: HAYIR
Payout hazirligi: [IBAN/SWIFT/vergi formu/banka sahibi notu]
```

**Kural:** Tweet/blog/soylenti TAHMINI'dir. Resmi ve guncel kaynak yoksa "BELIRSIZ" yaz; GO kararini tesvige dayandirma.

**Tahmini sure:** ~60 dakika (1 finalist icin)

### Faz 9 Kontrol Listesi

- [ ] En az 6 farkli keyword arama sorgusu yapildi
- [ ] Keyword'ler ana/orta/long-tail olarak kategorize edildi
- [ ] Top 5 rakibin ASO verileri (title, subtitle, description) toplandi
- [ ] Her rakibin keyword stratejisi analiz edildi
- [ ] Top 3 rakibin screenshot'lari analiz edildi
- [ ] Her screenshot icin metin, ozellik, renk, mesaj cikarldi
- [ ] Kendi uygulamamiz icin ASO stratejisi olusturuldu
- [ ] Paywall/onboarding pattern referansi cikartildi (Mobbin/App Store/Adapty Paywall Library varsa)
- [ ] Micro-MVP sprint uygunlugu belirlendi
- [ ] Security preflight + AI share/secret hygiene checklist'i dolduruldu
- [ ] Turkiye tesvik/payout kontrolu gerekti mi ve resmi kaynakla dogrulandi mi not edildi

---

## FAZ 10: SEYTAN'IN AVUKATI — Counter-Evidence Protokolu

**Amac:** Her varsayimi zorlayarak yanlis pozitif riskini azaltmak.
**Girdi:** Faz 9'a kadar olusan tum kararlar ve varsayimlar
**Cikti:** Her varsayim icin karsit kanit arama sonucu

### Varsayim 1: "Pazar buyuk ve buyuyor"

**Sorgu 1:**
```
WebSearch: "[KATEGORI] app market saturated 2025 2026"
```

**Sorgu 2:**
```
WebSearch: "[KATEGORI] app too many competitors overcrowded"
```

**Sorgu 3:**
```
WebSearch: "[KATEGORI] app failed startup postmortem"
```

**Sorgu 4:**
```
WebSearch: "[KATEGORI] app market declining shrinking"
```

**Kayit formati:**
```
Varsayim: "Pazar buyuk ve buyuyor"
Karsit kanit arama sonucu: BULUNDU / BULUNAMADI

Bulunan karsit kanitlar:
1. [Kaynak] — "[ozet]" — Tarih: [tarih]
2. ...

Degerlendirme: Varsayim GUCLENIYOR / ZAYIFLIYOR / COKUYOR
Aksiyon: [ne yapilmali]
```

---

### Varsayim 2: "Kullanicilar oder (premium modeli calisir)"

**Sorgu 1:**
```
WebSearch: "[KATEGORI] free app good enough"
```

**Sorgu 2:**
```
WebSearch: "[LIDER APP] free alternative"
```

**Sorgu 3:**
```
WebSearch: "why I cancelled [LIDER APP] subscription"
```

**Sorgu 4:**
```
WebSearch: "[KATEGORI] app subscription fatigue"
```

**Sorgu 5:**
```
WebSearch: "[KATEGORI] app users won't pay"
```

**Kayit formati:** [ayni format]

---

### Varsayim 3: "Farklilasma yeterli (bizi secerler)"

**Sorgu 1 — Baskasi bunu zaten yapmis mi:**
```
WebSearch: "[FARKLILIK OZELLIGI] [KATEGORI] app"
```

**Sorgu 2 — Ozellik kopyalanabilirlik riski:**
```
WebSearch: "[LIDER APP] new features update 2025 2026"
```

**Sorgu 3 — Kullanici perspektifi:**
```
WebSearch: "[FARKLILIK OZELLIGI] [KATEGORI] do users want"
```

**Sorgu 4 — Gercekten istenen bir sey mi:**
```
WebSearch: "[FARKLILIK OZELLIGI] [KATEGORI] reddit request"
```

**Kayit formati:** [ayni format]

---

### Varsayim 4: "Teknik olarak yapabiliriz"

**Sorgu 1:**
```
WebSearch: "[TEMEL OZELLIK] iOS implementation difficulty"
```

**Sorgu 2:**
```
WebSearch: "[TEMEL OZELLIK] iOS API limitations"
```

**Sorgu 3:**
```
WebSearch: "[TEMEL OZELLIK] solo developer feasibility"
```

**Kayit formati:** [ayni format]

---

### Varsayim 5: "Zamanlama dogru"

**Sorgu 1:**
```
WebSearch: "[KATEGORI] app [BUYUK RAKIP] entering market 2025 2026"
```

**Sorgu 2:**
```
WebSearch: "Apple [KATEGORI] built-in feature iOS"
```

**Sorgu 3:**
```
WebSearch: "[KATEGORI] app market window closing"
```

**Kayit formati:** [ayni format]

**Tahmini sure:** ~30 dakika

### Faz 10 Kontrol Listesi

- [ ] "Pazar buyuk" varsayimi icin en az 3 karsit kanit sorgusu yapildi
- [ ] "Kullanicilar oder" varsayimi icin en az 4 karsit kanit sorgusu yapildi
- [ ] "Farkimiz yeterli" varsayimi icin en az 3 karsit kanit sorgusu yapildi
- [ ] "Teknik olarak yapabiliriz" varsayimi icin en az 2 karsit kanit sorgusu yapildi
- [ ] "Zamanlama dogru" varsayimi icin en az 2 karsit kanit sorgusu yapildi
- [ ] Her varsayim icin GUCLENIYOR/ZAYIFLIYOR/COKUYOR degerlendirmesi yapildi
- [ ] COKUYOR degerlendirmesi alan varsayim varsa → Faz 8'e geri don, farkli finalist sec

---

## VERI TOPLAMA ZAMAN TAHMINI

| Faz | Arastirma Konusu | Birim Basina Sure | Birim Sayisi | Toplam Sure |
|-----|------------------|-------------------|--------------|-------------|
| Faz 3 | Hizli Pazar Tarama | ~5 dk/cluster | 15 cluster | ~75 dk |
| Faz 4 | Rakip Analizi | ~30 dk/cluster | 8 cluster | ~4 saat |
| Faz 5 | Firsat Puanlama | ~15 dk/cluster | 8 cluster | ~2 saat |
| Faz 7 | Pazar Dogrulama | ~45 dk/finalist | 5 finalist | ~3.5 saat |
| Faz 9 | ASO Veri Toplama | ~60 dk/finalist | 1 finalist | ~1 saat |
| Faz 10 | Seytan'in Avukati | ~30 dk/finalist | 1 finalist | ~30 dk |
| **TOPLAM** | | | | **~12 saat** |

**Not:** Bu sureler "veri toplama" suresidir. Analiz, puanlama ve karar verme sureleri haric.

---

## HIZLI REFERANS: SORGU SABLONLARI

Asagida en sik kullanilan sorgu sablonlarinin hizli listesi:

### App Store Verileri
```
WebSearch: "[KEYWORD] app" site:apps.apple.com
WebFetch: https://apps.apple.com/us/app/[SLUG]/id[ID]
WebFetch: https://play.google.com/store/apps/details?id=[PACKAGE]
```

### Rakip Bulma
```
WebSearch: "best [KEYWORD] app iOS 2025 2026"
WebSearch: "[KEYWORD] app alternatives"
WebSearch: "top [KEYWORD] apps iPhone"
```

### Kotu Yorum / Sikayet
```
WebSearch: "[APP ADI] complaints OR problems OR bugs reddit"
WebSearch: "[APP ADI] 1 star review"
WebSearch: "[APP ADI] worst app"
```

### Reddit Sentiment
```
WebSearch: "[APP ADI] reddit review 2025 2026"
WebSearch: "[APP ADI] alternative reddit"
WebSearch: "switched from [APP ADI] reddit"
WebSearch: "leaving [APP ADI] reddit"
```

### Gelir Kaniti
```
WebSearch: "[KATEGORI] app indie developer revenue indiehackers"
WebSearch: "[KATEGORI] app revenue #buildinpublic twitter"
WebSearch: "[KATEGORI] app how much money earn indie"
WebSearch: "[KATEGORI] solo developer app income earnings"
```

### Pazar Buyuklugu
```
WebSearch: "[KATEGORI] app market size 2025 2026"
WebSearch: "[KATEGORI] app market growth CAGR forecast"
```

### Trend
```
WebSearch: "[KEYWORD] app" Google Trends interest 2024 2025 2026
```

### Geo-LTV / Hedef Ulke
```
WebSearch: "[KATEGORI] app subscription LTV country benchmark RevenueCat"
WebSearch: "[KATEGORI] app paywall conversion country Adapty"
WebSearch: "[KATEGORI] app Apple Search Ads CPA country"
```

### Reklam Istihbarati (Ad Library — WebFetch CALISMAZ, browser otomasyonu gerekir)
```
Browser: facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[KEYWORD]&search_type=keyword_unordered
Browser: adstransparency.google.com/?region=US&domain=[RAKIP-DOMAIN]   (sadece advertiser; screenshot ile oku)
WebSearch (fallback): "[RAKIP APP] facebook ads OR tiktok ads"
```

### Visual Intelligence
```
WebFetch: https://apps.apple.com/us/app/[RAKIP-SLUG]/id[RAKIP-ID]
Browser/insan: Mobbin onboarding/paywall akislari
Browser/insan: Adapty Paywall Library benzer kategori pattern'leri
Uretim yardimi: Codia AI Design / screenshot-to-Figma
```

### Turkiye Tesvik / Payout
```
WebSearch: "mobil uygulama ihracat destekleri resmi site guncel"
WebSearch: "dijital hizmet ihracati reklam komisyon destekleri resmi site"
App Store Connect UI: Agreements, Tax, and Banking
```

### Karsit Kanit
```
WebSearch: "[KATEGORI] app market saturated 2025 2026"
WebSearch: "[KATEGORI] free app good enough"
WebSearch: "[FARKLILIK OZELLIGI] [KATEGORI] app"
WebSearch: "Apple [KATEGORI] built-in feature iOS"
```

---

## MASTER KONTROL LISTESI

Tum arastirma boyunca takip edilecek kontrol listesi:

### Faz 3 Kontrolleri (Her Cluster Icin)
- [ ] Lider uygulama App Store sayfasi WebFetch ile okundu
- [ ] Rating sayisi, yildiz, fiyat KESIN etiketiyle kaydedildi
- [ ] Son guncelleme tarihi kontrol edildi
- [ ] En az 3 rakip daha tespit edildi
- [ ] Google Trends yonu kontrol edildi
- [ ] Hedef geo / Geo-LTV hizli kontrolu kaydedildi
- [ ] Pazar durumu degerlendirmesi yapildi (DOYMUS/BUYUYOR/NIS/ERKEN)

### Faz 4 Kontrolleri (Her Cluster Icin)
- [ ] En az 5 rakip tam metadata toplandi
- [ ] Her rakip icin App Store sayfasi WebFetch ile okundu
- [ ] En az 20 kotu yorum okundu (1-2 yildiz)
- [ ] Top 3 sikayet temasi belirlendi ve frekans sayildi
- [ ] Reddit sentiment aramalari yapildi — minimum 3 farkli sorgu
- [ ] "Switched to..." veya alternatif arayan kullanicilar tespit edildi
- [ ] Fiyat karsilastirma tablosu tamamlandi
- [ ] Ozellik karsilastirma tablosu tamamlandi
- [ ] Google Play cross-check yapildi — en az top 5 rakip icin
- [ ] Reklam istihbarati taramasi yapildi (browser varsa KESIN; yoksa WebSearch fallback TAHMINI)
- [ ] Visual intelligence taramasi yapildi (App Store screenshot + varsa Mobbin/Adapty Paywall Library/Codia)

### Faz 5 Kontrolleri
- [ ] Her kriter icin veri kaynagi belirtildi (KESIN/TAHMINI/DUSUK)
- [ ] Gelir kaniti icin en az 3 farkli sorgu yapildi
- [ ] Geo-LTV / hedef ulke monetizasyon kontrolu yapildi
- [ ] Override kurallari kontrol edildi
- [ ] Tek kaynaga dayanan puan yok (Ucgen kurali)
- [ ] Retention icin guncelleme sikligi kontrol edildi
- [ ] DUSUK etiketli veriye dayanan puanlar max 3

### Faz 7 Kontrolleri (Her Finalist Icin)
- [ ] Gercek rating sayilari App Store'dan dogrulandi
- [ ] Indie gelir aranmasi en az 4 farkli sorgu ile yapildi
- [ ] Bulunamayan gelir kaniti acikca raporlandi
- [ ] Kullanici goc sinyali en az 4 farkli sorgu ile arandi
- [ ] Pazar raporu arandi ve bulunduysa Menopoz Testi uygulanidi
- [ ] Ucgen kurali her kritik iddia icin saglandi
- [ ] GENEL KARAR verildi

### Faz 9 Kontrolleri
- [ ] En az 6 keyword arama sorgusu yapildi
- [ ] Top 5 rakibin ASO verileri toplandi
- [ ] Top 3 rakibin screenshot'lari analiz edildi
- [ ] ASO stratejisi olusturuldu
- [ ] Paywall/onboarding pattern'i ve micro-MVP sprint uygunlugu yazildi
- [ ] Security preflight + AI share/secret hygiene kontrol edildi
- [ ] Turkiye tesvik/payout kontrolu gerekiyorsa resmi kaynakla ele alindi

### Faz 10 Kontrolleri
- [ ] 5 varsayimin her biri icin karsit kanit arandi
- [ ] Her varsayim icin GUCLENIYOR/ZAYIFLIYOR/COKUYOR degerlendirmesi yapildi
- [ ] COKUYOR varsayim varsa geri donus plani belirlendi
