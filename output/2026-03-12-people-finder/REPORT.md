# App Arastirma Raporu: People Finder

> Tarih: 2026-03-12
> Mod: Standard
> Metodoloji: v3.1 (10 Faz, 3 Katmanli Puanlama)

---

## Yonetici Ozeti

| Alan | Deger |
|------|-------|
| **Karar** | ELENDIR |
| **Final Skor** | 55/100 (K2) × 0.307 (K3) = **16.9** |
| **Risk Seviyesi** | COK YUKSEK |
| **MVP Tahmini** | 6-8 hafta |
| **Anahtar Bulgu** | K1 regulasyon kriteri KALDI. Pazar VC-funded sirketlerin (Whitepages 162K, BeenVerified 31K, Spokeo $57M gelir) domine ettigi, agir regulasyonlu (FCRA, CCPA, FTC cezalari $5.8M+) ve veri erisimi icin yuksek maliyet gerektiren ($0.28+/profil) bir alan. Indie developer gelir kaniti SIFIR. |
| **Oneri** | Bu kategoriye KESINLIKLE girme. Regulasyon riski, veri maliyeti, etik sorunlar ve yerlesik dev rakipler indie gelistirici icin asimaz engeller olusturuyor. |

---

## 1. Pazar Analizi

### Pazar Durumu
| Gosterge | Deger | Etiket |
|----------|-------|--------|
| Ana Keyword | "people finder" / "people search" | — |
| Lider Uygulama (genis) | Whitepages: People Search | — |
| Lider Rating (genis) | 161,827 | KESIN |
| Lider Yildiz (genis) | 4.6/5 | KESIN |
| Lider (orta) | BeenVerified: People Search | — |
| Lider Rating (orta) | 31,336 | KESIN |
| Lider Yildiz (orta) | 4.6/5 | KESIN |
| Lider (AI niche) | DeepSearch AI: People Finder | — |
| Lider Rating (AI niche) | 24 | KESIN |
| Pazar Sinifi | Guclu (genis) / Mikro (AI niche) | — |
| Google Trends | TAHMINI YUKARI — makale ve AI tool kullanimindaki artis | TAHMINI |
| Mevsimsellik | Belirgin mevsimsellik yok | TAHMINI |
| Pazar Baglami | Data broker pazari $257B (2023) → $441B (2032), %7.4 CAGR | KESIN |

### Pazar Gecerliligi (Katman 1)
| Kriter | Sonuc |
|--------|-------|
| Pazar var mi? (rating > 500) | **GECTI** — Whitepages 162K, BeenVerified 31K |
| Erisilebilir mi? (Apple/Google engeli yok) | **GECTI** — Apple Find My consent-based konum paylasimi (farkli kullanim alani). |
| Buyuyor mu? (trend + yeni girisler) | **GECTI** — 2025-2026'da AI-powered yeni girisler (DeepSearch, PrimeSearch, DeepTrace). Data broker pazari %7.4 CAGR. |
| Regulasyon asilabilir mi? (indie icin) | **KALDI** ⚠️ FCRA, CCPA, eyalet gizlilik yasalari dev regulasyon engeli olusturuyor. FTC aktif ceza kesiyor ($5.8M TruthFinder, $4.89M PeopleFinders). Veri broker tescili gerekli. Indie developer hukuk ekibi olmadan giremez. |

### Pazar Segmentasyonu
Bu pazar 4 belirgin segmentten olusuyor:

| Segment | Ornekler | Giris Bariyeri | Indie Uygunlugu |
|---------|----------|----------------|-----------------|
| **A: Tam veri broker (iOS)** | Whitepages, BeenVerified, Intelius | COK YUKSEK — veri ortakliklari, FCRA uyumu, hukuk ekibi | ❌ Imkansiz |
| **B: Niche/kucuk people finder** | PeopleFinders, Sheepy | YUKSEK — veri API maliyeti, regulasyon | ❌ Zor |
| **C: AI-powered yeni girisler** | DeepSearch, PrimeSearch, DeepTrace | ORTA — LLM API + web tarama | ⚠️ Mumkun ama kanitlanmamis |
| **D: Web-only servisler** | Spokeo, TruthFinder, Instant Checkmate | COK YUKSEK — altyapi, veri, hukuk | ❌ Imkansiz |

---

## 2. Rakip Analizi

### Top 10 Rakip
| # | Uygulama | Rating | Yildiz | Fiyat | Model | Son Guncelleme | Not |
|---|----------|--------|--------|-------|-------|----------------|-----|
| 1 | Whitepages: People Search | 161,827 | 4.6 | $1.99-29.99/yr | Freemium | Mar 2026 | **PAZAR LIDERI** — reverse phone, email, adres arama. Devasa veri tabani. |
| 2 | BeenVerified: People Search | 31,336 | 4.6 | $9.99-67.99/ay | Abonelik | Mar 2026 | **PREMIUM LIDER** — dark web tarama, arac/VIN arama, PDF export |
| 3 | Intelius Search | 9,952 | 4.5 | $9.99-49.99 | Freemium+Abo | Dec 2025 | Genis veri kaynaklari, suc istatistikleri, mahalle bilgisi |
| 4 | Sheepy: People Search & Finder | 279 | 4.2 | $4.99-19.99/yr | Freemium+Abo | Oct 2025 | **B2B ODAKLI** — email finder, lead export, CRM entegrasyonu |
| 5 | PeopleFinders | 172 | 3.4 | $24.99-219.99 | Abonelik | Feb 2025 | **DUSUK KALITE** — update loop, iptal zorlugu, sahte sonuclar |
| 6 | Radarly: Find People Near Me | 66 | 4.1 | $7.99-49.99 | Abonelik | Dec 2025 | **FARKLI SEGMENT** — konum bazli sosyal kesfetme, people search degil |
| 7 | DeepSearch AI: People Finder | 24 | 3.8 | $8.99-39.99/ay | Abonelik | Feb 2026 | **AI GIRISIMCI** — sosyal profil tarama, public records. Karisik yorumlar. |
| 8 | AI People Finder - Find Anyone | 9 | 4.4 | $6.99-39.99/yr | Abonelik | — | Yeni, Wikipedia + haber + public records. Cok az kullanici. |
| 9 | PrimeSearch - AI People Finder | 2 | 5.0 | $9.99-44.99 | Abonelik+Lifetime | Jan 2026 | Cok yeni, 2 rating — guvenilir degil |
| 10 | DeepTrace: AI People Finder | 2 | 4.5 | $9.99/hafta | Abonelik | Dec 2025 | AI rapor olusturma, kategori arama. 2 rating — guvenilir degil |

### Web-Only Buyuk Oyuncular (iOS App Yok)
| Servis | Tahmini Gelir | Model | Not |
|--------|--------------|-------|-----|
| Spokeo | ~$57M/yr | Abo ($19.95/ay) | Pipl tarafindan satin alindi. 15M aylik ziyaretci. |
| TruthFinder | Bilinmiyor | Abo ($28/ay) | H.I.G. Capital sahip. FTC cezasi aldi. |
| Instant Checkmate | Bilinmiyor | Abo ($34.78/ay) | FTC $5.8M ceza. A+ BBB rating. |
| TruePeopleSearch | $1-5M | Ucretsiz (reklam) | 2017'den beri. San Francisco merkezli. |
| FastPeopleSearch | Bilinmiyor | %100 Ucretsiz | Reklam geliri. |

### Sikayet Temalari (Review Mining — Reddit + App Store + Consumer Sites)
| # | Tema | Siklik | Ornek |
|---|------|--------|-------|
| 1 | **Aldatici free trial / otomatik abonelik** | Cok yaygin (~50+ yorum) | "Spokeo free trial immediately turns into $29.95/month" — Reddit |
| 2 | **Veri yanlisligi / eski bilgi** | Yaygin (~30+ yorum) | "Traffic tickets listed as criminal offenses" — TruthFinder kullanicisi |
| 3 | **Iptal zorlugu** | Yaygin (~25+ yorum) | "Charged for six months, company said nothing they can do" — ConsumerAffairs |
| 4 | **Gizlilik / stalking endisesi** | Orta (~20+ yorum) | "Criminals can easily access people's info with just a first and last name" — Fox News |
| 5 | **Sahte yukleme ekranlari / scammy UX** | Orta (~15+ yorum) | "Forced through 8-10 loading screens before accessing report" — Reddit |
| 6 | **Kotu musteri hizmeti** | Orta (~15+ yorum) | "Unresponsive support, frustration after being dissatisfied" — ConsumerAffairs |
| 7 | **Ucretsiz site bait-and-switch** | Yaygin (~20+ yorum) | "Charges $1 to show non-existent results" — PeopleFinders yorumu |

### Fiyat Karsilastirmasi
| Metrik | Deger |
|--------|-------|
| Whitepages | $1.99 tek seferlik — $29.99/yr |
| BeenVerified | $9.99-67.99/ay |
| Intelius | $9.99-49.99 paket |
| PeopleFinders | $24.99-219.99/ay |
| Spokeo (web) | $19.95/ay |
| TruthFinder (web) | $28.05/ay |
| AI yeni girisler | $6.99-39.99/hafta-ay |
| **Ortalama aylik** | ~$30/ay (niche iOS) |
| **Medyan aylik** | ~$20/ay |
| **Fiyat araligi** | $2 — $220/ay (cok genis) |
| **Lifetime sunan** | 1/10 rakip (PrimeSearch $44.99) |
| **Hakim model** | **Abonelik** — tek seferlik SADECE Whitepages'te var |

---

## 3. Firsat Puanlama

### Katman 2: Firsat Kalitesi (/100)
| Kriter | Agirlik | Skor (1-5) | Puan | Veri Kaynagi |
|--------|---------|-----------|------|-------------|
| Talep Sinyali | ×5 | **5** | 25 | Whitepages 162K (KESIN) — ayni segment, dogrudan rakip. Lider Secim Kurali: Whitepages people finder, kullanici da people finder → ayni kategori. |
| Gelir Kaniti | ×5 | **2** | 10 | Spokeo $57M, Intelius $35M (KESIN) — TAMAMI kurumsal. Indie gelir kaniti SIFIR. |
| Rekabet Boslugu | ×4 | 3→**2** | 8 | 7 sikayet temasi var → anchor 3 (KESIN). **Moat duzeltmesi:** Bosluk UX'te ama avantaj VERI moat'unda → 1 dusur → 2. Veri ortakliklari indie kopyalayamaz. |
| Retention | ×3 | **1** | 3 | People search tek kullanimlik/aylik — gunluk engagement yok (TAHMINI) |
| Zamanlama | ×3 | 3 | 9 | AI trend yeni giris yaratıyor (KESIN), ama regulasyon sikisiyor (KESIN) |
| **Toplam** | | | **55** | |

**Uygulanan Override:**
- ⚠️ Indie gelir kaniti SIFIR → Gelir MAX 2 ✓ (uygulandı)
- ⚠️ Rekabet: Anchor skoru 3 (7 sikayet temasi) ama **veri moat duzeltmesi** ile 1 dusuruldu → 2
  - Not: Onceki raporda "Top 5 hepsi 4.5+" override'i yanlis uygulanmisti. Override kurali "Top 5 hepsi **4.7+**" diyor. Gercek yildizlar: 4.6, 4.6, 4.5, 4.2, 3.4 → override UYGULANMAZ. Moat duzeltmesi daha dogru bir mekanizma.

### Katman 3: Fizibilite Carpani
| Kriter | Skor | Gerekce |
|--------|------|---------|
| Teknik Zorluk | **0.8** | Orta — LLM API + web arama + sonuc derleme. Veri API maliyeti yuksek ($0.28+/profil) |
| Kurucu Uyumu | **0.8** | Ilgi var, bilgi sinirli — problemi anliyor ama domain deneyimi yok |
| Regulasyon/Uyum | **0.6** | Agir regulasyon — FCRA, CCPA, veri broker tescili. Hukuk danismani SART ($10K-50K+). Indie icin en buyuk engel. |
| MVP Suresi | **0.8** | 6-8 hafta — API entegrasyonu + compliance + UI. Basit CRUD degil. |
| **Carpan** | **0.307** | |

### Final Skor
**55 × 0.307 = 16.9** → **ELENDIR — K1 regulasyon kriteri zaten KALDI, bu fikre devam etme**

---

## 4. Gelir Potansiyeli

### Indie Gelir Kaniti
*8 farkli sorgu yapildi (IndieHackers, Twitter #buildinpublic, "people finder revenue", "people search indie developer", Product Hunt). Indie gelistirici gelir kaniti KESINLIKLE BULUNAMADI.*

Yerlesik oyuncularin gelirleri:

| # | Sirket | Gelir | Kaynak | Guvenilirlik |
|---|--------|-------|--------|-------------|
| 1 | Spokeo | ~$57M/yr | Zippia + Wikipedia | TAHMINI |
| 2 | Intelius | ~$35M/yr | Zippia (Aug 2025) | TAHMINI |
| 3 | BeenVerified (parent: Lifetime Value Co.) | $44.7M/yr | RocketReach | TAHMINI |
| 4 | TruePeopleSearch | $1-5M/yr | Crunchbase | DUSUK |

**Neden indie basarisiz:** Bu alan yuksek sermaye gerektirir. Veri API maliyeti profil basina $0.28+, FCRA uyumu hukuk danismanı gerektirir, veri ortakliklari kurumsal anlasmalar gerektirir. Indie gelistirici icin ekonomik olarak SURDURULEMEZ.

### Veri API Maliyetleri
| Saglayici | Fiyat | Model |
|-----------|-------|-------|
| People Data Labs | $98/ay + $0.28/profil | Kredi bazli |
| Hunter.io | $49-299/ay | Email bulma, %35-45 basari |
| Clearbit (Breeze) | $45-50/ay + profil | Kredi bazli |
| Apollo.io | Ucretsiz (temel) | Kredi bazli |
| Checkr (background) | $29.99-79.99/kontrol | Per-check |

**Maliyet Analizi:** 1000 kullanicinin ayda 5 arama yaptigi varsayilirsa:
- 5000 arama × $0.28 = **$1,400/ay sadece veri maliyeti**
- + LLM API maliyeti + sunucu + App Store komisyon
- Karlilik icin kullanici basina $5+/ay almak gerekir
- AMA kullanicilar "ucretsiz" alternatifler varken (TruePeopleSearch, FastPeopleSearch) neden odesin?

### Fiyat Modeli Gozlemi
Pazar **abonelik hakim** ($10-68/ay). Tek seferlik model yok (Whitepages $1.99 haric). Indie giris icin fiyat belirleme cok zor:
- Dusuk fiyat → veri maliyetini karsilamaz
- Yuksek fiyat → ucretsiz alternatiflerle yarisimaz
- **Ekonomik olarak cikmaz**

---

## 5. Dogrulama

### 4 Dogrulama Kontrolu
| # | Kontrol | Sonuc | Guvenilirlik |
|---|---------|-------|-------------|
| 1 | Lider rating gercek mi? | **DOGRULANDI** — Whitepages 161,827 App Store'da dogrudan kontrol edildi | KESIN |
| 2 | Indie gelir kaniti | **BULUNAMADI** — 8 sorgu, 0 sonuc. Bu alanda indie gelistirici yok. | KESIN (yokluk dogrulandi) |
| 3 | Kullanici goc sinyali | **KISMI** — Reddit'te mevcut servislerden memnuniyetsizlik var (billing, accuracy) AMA alternatif uygulamaya degil, ucretsiz web sitelerine yoneliyorlar | TAHMINI |
| 4 | Menopoz Testi | **GECTI** — Pazar canli, yeni AI girisler var. Ama girisler COK KUCUK (2-24 rating). | KESIN |

**Dogrulama Sonucu:** KISMI — Pazar var ve canli, ama indie gelistirici icin ERISILEBILIR degil.

---

## 6. Risk Degerlendirmesi

### Regulasyon Riski
| Alan | Detay |
|------|-------|
| Gecerli yasalar | FCRA (background check), CCPA (California gizlilik), GDPR (Avrupa), 37 eyalet Ban-the-Box, 12 eyalet Clean Slate |
| Ceza ornekleri | TruthFinder + Instant Checkmate → $5.8M FTC cezasi (2023). PeopleFinders → $4.89M class action (Illinois). Eightfold AI → sinif davasi (2026). |
| Indie etkisi | Hukuk departmani olmadan calismak mumkun degil. Tek bir FTC sorusturmasi indie gelistiriciyi bitirir. |
| Uyum maliyeti | $10K-50K+ avukat + devam eden uyum maliyeti. Veri broker tescili gereken eyaletler var. |

### Ana Riskler
| # | Risk | Olasilik | Etki | Onlem |
|---|------|----------|------|-------|
| 1 | **FCRA/Regulasyon ihlali** — FCRA uyumsuz rapor uretme, FTC sorusturma/ceza | YUKSEK | OLUMCUL — milyonlarca dolar ceza + uygulama kaldirilmasi | Hukuk danismani SART. Maliyet: $10K-50K+ |
| 2 | **Veri maliyeti surdurulemez** — API basina $0.28+, 5000 arama/ay = $1,400 sadece veri | YUKSEK | Finansal CIKMAZ — gelir gideri karsilamaz | Maliyet/gelir modeli onceden cok detayli planlanmali |
| 3 | **App Store reddi** — Apple gizlilik politikalarina aykiri bulabilir | ORTA | OLUMCUL — urun yayinlanamaz | Apple Privacy Guidelines detayli incelenmeli |
| 4 | **Etik/hukuki sorumluluk** — Uygulama stalking/harassment icin kullanilirsa | YUKSEK | OLUMCUL — dava + itibar kaybi | Kullanim amaci dogrulama, rate limiting |
| 5 | **Veri dogrulugu davasi** — Yanlis bilgi nedeniyle zarar goren kullanici dava acarsa | ORTA | YUKSEK — tazminat + uygulama kaldirilmasi | Disclaimer yeterli olmayabilir |
| 6 | **Ucretsiz alternatifler** — TruePeopleSearch, FastPeopleSearch tamamen ucretsiz | KESIN | YUKSEK — kullanici neden odesin? | Farklilasmma cok zor |

### KRITIK RISK: Regulasyon Mayini
Bu pazar aktif FTC gozaltinda:
- **2023:** TruthFinder + Instant Checkmate → $5.8M ceza (aldatici pazarlama)
- **2023:** PeopleFinders → $4.89M ceza (Illinois Right of Publicity Act)
- **2026:** Eightfold AI → sinif davasi (FCRA ihlali, kisisel veri derleme)
- **12 eyalet** "Clean Slate" yasasi gecirdi — sealed kayitlara erisim kisitlaniyor
- **37 eyalet** "Ban-the-Box" yasasi — ceza gecmisi sorgulamasi kisitli

Bir indie gelistirici bu regulasyon ortaminda hayatta kalamaz. Buyuk sirketlerin bile milyonlarca dolar ceza odedigi bir alanda, hukuk departmani olmadan calismak INTIHARDIR.

---

## 7. MVP Onerisi

> **NOT:** Final Skor 16.9 (ELENDIR). Bu MVP onerisi SADECE bilgi amaclidir. Bu uygulamayi gelistirmeyi ONERMIYORUZ.

### En Az Riskli Yaklasim: AI-Powered Web Aggregator
| # | Ekran | Ne Yapar |
|---|-------|----------|
| 1 | Arama | Isim + sehir/eyalet girisi |
| 2 | Sonuclar | AI ile derlenmis web sonuclari (LinkedIn, haber, public profil) |
| 3 | Profil Detay | Bulunan bilgilerin ozeti |

### Neden Bu Yaklasim
- FCRA kapsamina girmez (background check/screening DEGIL, sadece public web bilgisi)
- Veri API'si yerine web arama + LLM kullanir (dusuk maliyet)
- AMA: Sonuc kalitesi cok dusuk olur (mevcut AI girisler 2-24 rating)

### Teknik Stack
| Alan | Oneri |
|------|-------|
| Platform | iOS (Swift + SwiftUI) |
| AI | Claude API / OpenAI API |
| Web Search | SearchApi veya SerpApi ($50-100/ay) |
| DB | SwiftData (yerel) |
| Odeme | RevenueCat |

### V1'de OLMAYACAKLAR (ve neden)
- ❌ Background check — FCRA uyumu gerektirir
- ❌ Ceza gecmisi arama — hukuki sorumluluk
- ❌ Adres/telefon arama — veri API maliyeti surdurulemez
- ❌ Banka/finansal bilgi — regulasyon

---

## 8. Alternatif Degerlenirme

### Neden Bu Fikir Calismiyor
| Engel | Aciklama | Asabilir mi? |
|-------|----------|-------------|
| Regulasyon | FCRA, CCPA, 37 eyalet yasasi, aktif FTC cezalari | ❌ Indie gelistirici icin asimaz |
| Veri Moat | Whitepages/Spokeo yillarin veri ortakliklarina sahip | ❌ Para ile bile kolay degil |
| Maliyet | $0.28+/profil API, $1,400+/ay minimum | ❌ Indie gelir modeliyle uyumsuz |
| Etik | Stalking, harassment, doxing riski | ⚠️ Yonetilebilir ama riskli |
| Retention | Tek kullanimlik — gunluk/haftalik engagement yok | ❌ LTV cok dusuk |
| Ucretsiz rakipler | TruePeopleSearch, FastPeopleSearch tamamen ucretsiz | ❌ Fiyat avantaji yok |

### Onerilen Alternatifler
1. **Debt Payoff Planner** → Final Skor 51.2, SARTLI GO, dusuk risk, regulasyon engeli yok
2. **Baska niche ara** → Quick Scan ile farkli fikirler test et
3. **AI-powered FARKLI alanda** → AI teknolojisini regulasyon riski OLMAYAN bir alanda kullan (ornk: AI ozet, AI ceviri, AI yardimci)

---

## 9. Sonraki Adimlar

**ONERI: Bu fikri KESINLIKLE BIRAK.**

Gerekceler:
1. **K1 KALDI** — Regulasyon kriteri fail (FCRA, FTC cezalari, veri broker tescili)
2. Final Skor **16.9** — ELENDIR kategorisi (< 30)
3. Regulasyon riski **OLUMCUL** — FTC aktif ceza kesiyor (milyonlarca dolar)
4. Indie gelir kaniti **SIFIR** — bu alanda tek bir basarili indie yok
5. Veri maliyeti **SURDURULEMEZ** — $0.28+/profil
6. Yerlesik rakipler **ASIMAZ** — $57M gelirli Spokeo, 162K rating'li Whitepages
7. Retention **COK DUSUK** — tek kullanimlik
8. Etik sorunlar **CIDDI** — stalking/harassment riski
9. Ucretsiz alternatifler **MEVCUT** — TruePeopleSearch, FastPeopleSearch

**Sonraki adim:** Debt Payoff Planner (51.2) uzerinde Standard mod analiz calistir, veya yeni fikir bul.

---

## 10. Cross-Report Karsilastirma

| Fikir | K2 | K3 | Final | Karar | Ana Avantaj | Ana Risk |
|-------|----|----|-------|-------|-------------|----------|
| Debt Payoff Planner | 64 | 0.80 | **51.2** | SARTLI GO | Tek ciddi rakip (OxbowSoft), Apple Watch/Widget boslugu | OxbowSoft gelir kaniti dogrulanamadi |
| Subscription Tracker | 48 | 0.80 | **38.4** | NO-GO | Abonelik yorgunlugu trendi yukari | Apple yerlesik abonelik yonetimi, dusuk retention |
| **People Finder** | 55 | 0.307 | **16.9** | ELENDIR | Guclu talep (162K lider) | Regulasyon mayini, veri moat, $0 indie kanit |

**Analiz:** People Finder'in K2 skoru (55) aslinda Sub Tracker'dan (48) yuksek — talep gercekten var. Ama K3'teki regulasyon carpani (0.6) tum firsati oldurdu. Bu, regulasyon engelinin neden K1'de gate olmasi gerektigini gosteriyor: K1'de KALDI → analiz daha erken sonlandirilabilirdi.

---

## Veri Kaynaklari

| # | Kaynak | Erisim Tarihi | Guvenilirlik |
|---|--------|---------------|-------------|
| 1 | App Store — Whitepages | 2026-03-12 | KESIN |
| 2 | App Store — BeenVerified | 2026-03-12 | KESIN |
| 3 | App Store — Intelius | 2026-03-12 | KESIN |
| 4 | App Store — Sheepy | 2026-03-12 | KESIN |
| 5 | App Store — PeopleFinders | 2026-03-12 | KESIN |
| 6 | App Store — Radarly | 2026-03-12 | KESIN |
| 7 | App Store — DeepSearch AI | 2026-03-12 | KESIN |
| 8 | App Store — AI People Finder | 2026-03-12 | KESIN |
| 9 | App Store — PrimeSearch | 2026-03-12 | KESIN |
| 10 | App Store — DeepTrace | 2026-03-12 | KESIN |
| 11 | TechRadar — Best People Search 2026 | 2026-03-12 | KESIN |
| 12 | TheGWW — Ultimate Comparison 2026 | 2026-03-12 | KESIN |
| 13 | SNS Insider — Data Brokers Market $441B | 2026-03-12 | KESIN |
| 14 | FTC — TruthFinder/Instant Checkmate $5.8M ceza | 2026-03-12 | KESIN |
| 15 | TopClassActions — PeopleFinders $4.89M ceza | 2026-03-12 | KESIN |
| 16 | Privacy Rights Clearinghouse — Data broker FAQ | 2026-03-12 | KESIN |
| 17 | ConsumerAffairs — BeenVerified, PeopleFinders yorumlari | 2026-03-12 | KESIN |
| 18 | Sitejabber — BeenVerified yorumlari | 2026-03-12 | KESIN |
| 19 | Reddit — people finder complaints, scam tartismalari | 2026-03-12 | TAHMINI |
| 20 | Spokeo/Intelius gelir tahminleri — Zippia, Wikipedia | 2026-03-12 | TAHMINI |
| 21 | People Data Labs — API fiyatlama | 2026-03-12 | KESIN |
| 22 | iProspectCheck — Ban-the-Box, Clean Slate yasalari | 2026-03-12 | KESIN |
| 23 | Guru99, GeeksforGeeks — Best people search sites | 2026-03-12 | TAHMINI |
| 24 | Ogletree — Eightfold AI FCRA davasi (Jan 2026) | 2026-03-12 | KESIN |

---

*Bu rapor App Idea Research Agent v3.1 metodolojisi ile olusturulmustur.*
*Mod: Standard | Sure: ~35 dakika | Sorgu sayisi: 20+ (4 paralel agent)*
