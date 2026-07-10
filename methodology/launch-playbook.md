# Lansman Playbook

Indie iOS uygulamasi icin kapsamli lansman rehberi.
Pre-launch'tan post-launch analizine kadar her adim.

---

## FAZ 5.5 SONRASI: 1 HAFTALIK MICRO-MVP SPRINT

Bu sprint sadece Faz 5.5 davranisla DOGRULANDI olan, teknik/regulasyon olarak basit ve max 4 core ekran + gerekiyorsa 1 paywall/upgrade ekranla cikabilecek app'ler icindir. Karmasik ML, agir regule veri, donanim entegrasyonu veya coklu backend bagimliligi varsa 8 haftalik pre-launch planini kullan.

**Uygunluk checklist'i:**
- [ ] Faz 5.5 sonucu DOGRULANDI veya guven >=%70 + gercek davranis sinyali var
- [ ] MVP max 4 core ekran, 3 ana ozellik; sprintte gerekiyorsa ek 1 paywall/upgrade ekran
- [ ] Paywall ilk versiyona eklenebilir
- [ ] App Store privacy/policy riski basit
- [ ] Security preflight'ta olumcul eksik yok

| Gun | Odak | Cikti |
|-----|------|-------|
| Pazartesi | Keyword + final scope | App name/subtitle taslagi, max 4 core ekran + gerekiyorsa 1 paywall/upgrade ekran, V1 disi liste |
| Sali | Proje kurulumu + onboarding | Repo/app skeleton, ilk acilis akisi, analytics event taslagi |
| Carsamba | MVP ekranlari | Core flow calisir, empty/error/loading durumlari var |
| Persembe | Paywall + market-fit copy | RevenueCat/StoreKit/Adapty/Superwall entegrasyonu, paywall mesajlari |
| Cuma | Test + screenshots | Smoke test, crash kontrolu, App Store screenshot taslaklari |
| Cumartesi | Submit | App Store Connect metadata, privacy nutrition, review notes |
| Pazar | Marketing | Reddit/PH/X/email taslaklari, launch waitlist follow-up |

**Paywall pattern girdileri:** App Store screenshot'lari, Mobbin onboarding/paywall akislari ve Adapty Paywall Library pattern'leri ilham icin kullanilir; metin/gorsel/marka kopyalanmaz.

---

## PRE-LAUNCH (8 Hafta Once)

### Hafta -8 to -6: Temel Hazirlik

#### Landing Page & Online Varlik
- [ ] Landing page olustur (Carrd.co $19/yil veya GitHub Pages ucretsiz)
- [ ] Waitlist formu ekle (Buttondown ucretsiz veya MailChimp free tier)
- [ ] Ozel domain al (uygulamaadi.com veya uygulamaadi.app)
- [ ] Twitter/X hesabi ac ve #buildinpublic ile paylasim baslat
- [ ] Product Hunt'ta "Upcoming" sayfasi olustur
- [ ] IndieHackers'da profil olustur

#### Teknik Hazirlik
- [ ] App Store Connect hesabini hazirla ($99/yil Apple Developer Program)
- [ ] App ID, Bundle ID, ve provisioning profile olustur
- [ ] RevenueCat veya StoreKit 2 entegrasyonu baslat (abonelik yonetimi)
- [ ] Analytics SDK entegre et (TelemetryDeck privacy-friendly, veya Mixpanel free tier)
- [ ] Crash reporting ekle (Firebase Crashlytics ucretsiz)
- [ ] TestFlight dahili test grubunu kur

#### Icerik Hazirlik
- [ ] Screenshot mockup'larin ilk versiyonlarini olustur (Figma veya Rotato)
- [ ] App Store aciklama taslagi yaz
- [ ] Privacy Policy olustur (generator: privacypolicies.com veya iubenda)
- [ ] Terms of Service olustur
- [ ] Support email adresi kur (support@uygulamaadi.com)
- [ ] Basit bir FAQ sayfasi hazirla

#### Build in Public Stratejisi
- [ ] Haftada 2-3 paylasim plani yap
- [ ] Paylasim turleri belirle:
  - Gelistirme sureci screenshot'lari
  - Karsilasilan teknik zorluklar ve cozumler
  - Kullanici arastirmasi bulgulari
  - Tasarim kararlari ve nedenleri
  - Gelir/metrik paylasimi (lansman sonrasi)

### Hafta -5 to -3: Beta Donemi

#### TestFlight Beta
- [ ] TestFlight beta dagitimi baslat (hedef: 50-100 kisi)
- [ ] Beta tester kaynaklari:
  - Twitter'da #buildinpublic takipcileri
  - IndieHackers toplulugu
  - Reddit r/TestFlight, r/betaapps
  - Yakin cevre (ama SADECE hedef kitle olanlari)
  - Landing page waitlist'i
- [ ] Beta feedback toplama araci kur:
  - In-app feedback formu (basit bir Google Form bile olur)
  - TestFlight'in yerlesik feedback sistemi
  - Kisa anket (Typeform free tier: 10 soru, 100 cevap/ay)

#### Beta Odak Noktalari
- [ ] Kritik bug'lari duzelt (crash, veri kaybi, UI kirilmasi)
- [ ] Onboarding akisini test et ve optimize et
  - Ilk acilistan deger gormeye kadar kac adim?
  - 60 saniyede temel islem yapilabiliyor mu?
  - Kullanici nerede takilıyor?
- [ ] Paywall zamanlamasini test et
  - Soft paywall: Bazi ozellikler kilitli, temel kullanim ucretsiz
  - Hard paywall: Trial sonrasi tam kilit
  - Metered paywall: X kullanim ucretsiz, sonra odeme
  - Test: Paywall'u hangi ekranda/aksiyonda gostermek en iyi conversion verir?
- [ ] Performance testi
  - App launch suresi < 2 saniye
  - Ekran gecisleri akici (60fps)
  - Bellek kullanimi makul (< 100MB)
- [ ] Accessibility kontrolu
  - VoiceOver ile kullanilabiliyor mu?
  - Dynamic Type destegi var mi?
  - Renk kontrast oranlari yeterli mi?

#### Beta Feedback Analizi
- [ ] En cok istenen 3 ozellik nedir? (V1.1 icin planla)
- [ ] En buyuk 3 sikayet nedir? (Lansmandan once duzelt)
- [ ] NPS skoru kac? (0-6: Kotü, 7-8: Orta, 9-10: Iyi)
- [ ] "Bu uygulamayi baskasina onerir misiniz?" → %40+ "evet" = iyi sinyal

### Hafta -2 to -1: Final Hazirlik

#### App Store Sayfa Optimizasyonu
- [ ] App Store aciklama metni finalize
  - Ilk 3 satir EN ONEMLI (fold ustunde gorunen kisim)
  - Anahtar kelime yogunlugu dogal olmali
  - Ozellik listesi degil, FAYDA listesi yaz
  - Social proof (beta kullanici sayisi, varsa oduller)
- [ ] Subtitle (30 karakter) finalize — en onemli keyword burada
- [ ] Keyword field (100 karakter) optimize et
  - Virgul kullanma, boslukla ayir (Apple otomatik kombinasyon yapar)
  - Tekrar etme (subtitle'daki kelimeyi keyword field'da tekrarlama)
  - Rakip isimlerini KOYMA (reddedilir)
- [ ] Kategori secimi (Primary + Secondary)
- [ ] Yas siniflandirmasi (dogru isaretleme yapmazsan reddedilir)

#### Screenshot'lar
- [ ] 6.7" iPhone 15 Pro Max screenshot'lari (zorunlu)
- [ ] 6.5" iPhone 14 Plus screenshot'lari (zorunlu)
- [ ] iPad screenshot'lari (iPad destekliyorsan)
- [ ] Screenshot kurallari:
  - ILK screenshot en onemli — App Store browse'da gorulen tek screenshot
  - Her screenshot TEK BIR mesaj versin
  - Metin buyuk ve okunakli olsun
  - Gercek uygulama ekrani goster (mockup verisi gercekci olsun)
  - 10 screenshot hakkin var, en az 6 kullan
  - Siralama: En guclu ozellik → fark yaratici ozellik → detay ozellikler
- [ ] App Preview Video (opsiyonel ama guclu)
  - 15-30 saniye
  - Ilk 3 saniye dikkat cekmeli
  - Muzik + metin overlay
  - Gercek kullanim senaryosu goster

#### Teknik Final
- [ ] App Review'a gonder (2-3 gun once)
  - Review sureleri: Genellikle 24-48 saat, bazen 1 hafta
  - Ilk submission'da reddedilme orani: ~%40
  - Reddedilme durumunda: Sakin ol, rehberligı oku, duzelt, tekrar gonder
- [ ] Release tipi sec:
  - "Manual Release" sec (lansman gununu kontrol et)
  - Otomatik release secme — zamanlaman bozulur
- [ ] Son smoke test: Gercek cihazda (TestFlight degil) production build'i test et
- [ ] Server tarafindaki her sey hazir mi? (API, veritabani, CDN)
- [ ] Push notification sertifikalari uretim icin dogru mu?
- [ ] Security & secret hygiene preflight tamam mi? (asagidaki bolum)

#### Lansman Gunu Plani
- [ ] Sosyal medya postlarini onceden hazirla
  - Twitter/X thread (8-10 tweet)
  - Reddit postlari (3-4 farkli subreddit icin ayrı ayrı)
  - LinkedIn postu (profesyonel ag)
  - Product Hunt aciklamasi
  - Hacker News "Show HN" postu
- [ ] Email listesine lansman maili taslagi hazirla
- [ ] Yakin cevre listesi hazirla (ilk gun destek icin)
- [ ] Monitoring dashboard hazirla (RevenueCat + Analytics + Crashlytics)

---

## LAUNCH WEEK (Gun Gun)

### Pazartesi: Soft Launch

#### Sabah (09:00)
- App Store'da "Release This Version" butonuna bas
- Canli oldugunu dogrula (App Store'da ara, link'i test et)
- Son dakika kontrolleri:
  - In-app purchase'lar calisiyor mu?
  - Onboarding akisi dogru mu?
  - Analytics event'leri geliyor mu?
  - Crash monitoring aktif mi?

#### Ogle (12:00)
- Yakin cevreye duyur (WhatsApp, iMessage, email)
- ONEMLI: "Indir ve 5 yildiz ver" DEME. "Indir, kullan, durust geri bildirim ver" de.
- Ilk kullanici geri bildirimlerini topla
- Acil bug varsa hotfix hazirla

#### Aksam (18:00)
- Ilk gun verileri:
  - Kac install?
  - Kac crash?
  - Onboarding completion rate?
  - Trial baslama orani?
- Ciddi bug varsa gece hotfix gonder

### Sali: Community Launch

#### Reddit Stratejisi (10:00)
- r/SideProject — "I built [app] — [tek cumle aciklama]"
- r/productivity veya ilgili nis subreddit — deger odakli post
- r/iOSProgramming — teknik hikaye (Swift, SwiftUI, architecture)
- r/AppIdeas — "I turned this idea into reality"

**Reddit Post Kurallari:**
- REKLAM DEGIL, hikaye anlat
- "I built..." formati kullan
- Acik ve durust ol (kac ayda yaptin, ne ogrending)
- Ucretsiz versiyonun ne yaptigini acikla
- Negatif yorumlara savunmaci OLMA
- Her subreddit'in kurallarini lansmandan once OKU
- Self-promotion kurali olan subreddit'lerde dikkatli ol
- Yorum karman dusukse post kaldirilebilir — onceden karma kazan

#### Hacker News Stratejisi (14:00 — 9 AM EST)
- "Show HN: [App Name] — [tek cumle tanim, teknik detay icersin]"
- Ilk yorum olarak "maker comment" yaz:
  - Neden yaptin?
  - Teknik stack ne? (HN kitlesi bunu sever)
  - Fiyatlandirma modelin ne?
  - Gelecek planlarin ne?
- Sorulara HIZLI cevap ver (ilk 2 saat kritik)
- Negatif geri bildirime acik ol, savunma yapma
- Fiyatlandirma sorusuna hazir ol (HN "ucretsiz olmali" taraftarlari vardir)

**HN Beklenti Yonetimi:**
- Front page'e cikma olasiligi: ~%5-10
- Front page'e cikarsa: 2000-10000 site ziyareti, 100-500 install
- Cikamazsa: 50-100 site ziyareti, 10-30 install
- Her iki durumda da degerli geri bildirim alirsin

#### IndieHackers (16:00)
- Urun sayfasi olustur
- "Launch" postu yaz
- Gelir verilerini paylasmayi planla (seffaflik onemli)

### Carsamba: Product Hunt Launch

#### Hazirlik (Onceki Gece)
- Product Hunt'ta her sey hazir mi?
  - Tagline (kisa ve net)
  - Aciklama (ilk paragraf = hook)
  - Gorseller (logo, screenshot'lar, GIF/video)
  - Maker comment taslagi
  - Ilk yorum icin 3-4 hazir cevap

#### Lansman (00:01 PST / 10:01 TR saati)
- Launch butonuna bas
- Maker comment'i hemen yaz (samimi, hikayeni anlat)
- Ilk 4 saatte kritik donem:
  - Topluluguna duyur (email listesi, Twitter, yakin cevre)
  - Upvote icin SPAM YAPMA — gercek kullanicilardan organik destek iste
  - "Hey, Product Hunt'ta ciktik, gorus ve onerilerinizi bekliyoruz" mesaji
  - Yorumlara 5 dakika icinde cevap ver

#### Gun Boyunca
- Her yoruma samimi ve hizli cevap ver
- Sorulari firsata cevir (ozellik sorulari = gelecek planlar)
- Gercek zamanli metrikleri izle
- Sosyal medyada PH linkini paylas

**Product Hunt Beklenti Yonetimi:**
- Top 5: 200-1000 site ziyareti, 50-200 install
- Top 10: 100-500 site ziyareti, 30-100 install
- Top 20: 50-200 site ziyareti, 15-50 install
- En iyi gunler: Sali veya Carsamba (Pazartesi cok rekabetci, Cuma az trafik)
- Golden Kitty odulu = buyuk bonus ama bekleme

### Persembe: Content Push

#### Blog / SEO Icerigi
- Blog yazisi yayinla (Medium veya kendi sitenin blogu):
  - Secenek A: "Why I Built [App Name]" — kisisel hikaye
  - Secenek B: "The Best [Kategori] Apps in 2026" — listede kendi uygulamani da dahil et
  - Secenek C: "[Rakip] vs [App Name]: Which is Better for [nis]?" — karsilastirma
  - SEO icin "[rakip] alternative" keyword'unu hedefle

#### Twitter/X Push
- Build story thread'i (8-10 tweet):
  1. Hook: "6 aydir uzerinde calistigim uygulamayi yayinladim."
  2. Problem: "Su problemi cozuyor..."
  3. Cozum: "Nasil cozuyor..."
  4. Screenshot/video
  5. Zorluklar: "En zor kisim suydu..."
  6. Rakamlar: "Beta'da su sonuclari gurduk..."
  7. Gelecek: "Sonraki planlarim..."
  8. CTA: "Denemek isterseniz link bio'da"
- Thread'i iyi saatte paylas (TR: 10:00-12:00, US: 09:00-11:00 EST)
- #buildinpublic #indiedev #iosdev hashtag'leri

#### Email Listesi
- Waitlist'e lansman maili gonder
- Icerik:
  - "Sonunda cikti!" basligi
  - 3 temel ozellik
  - Ozel lansman indirimi (varsa)
  - Dogrudan App Store linki
  - "Reply to this email" ile geri bildirim iste
- Acilma orani hedefi: %40+ (liste kucuk ve nitelikli olmali)

### Cuma: Ilk Hafta Analizi

#### Veri Toplama
- [ ] Toplam install sayisi
- [ ] Trafik kaynaklari breakdown (Reddit, PH, HN, Twitter, Organik)
- [ ] Trial baslama orani
- [ ] Day 1 retention orani
- [ ] Crash-free rate
- [ ] App Store conversion rate (impression → install)
- [ ] Kullanici geri bildirim ozeti (App Store + in-app + email)

#### Analiz Sorulari
- Hangi kanal en cok install getirdi?
- Hangi kanal en kaliteli kullanici getirdi? (retention bazinda)
- Kullanicilar onboarding'in neresinde takildi?
- En cok kullanilan 3 ozellik hangisi?
- En buyuk sikayet/istek ne?

#### Aksiyon Plani
- Sonraki hafta icin 3 oncelik belirle:
  1. Kritik bug fix (varsa)
  2. En cok istenen ozellik (hizli kazanim)
  3. Retention iyilestirmesi (onboarding veya notification)

---

## SECURITY & SECRET HYGIENE PREFLIGHT

Lansman oncesi bu kontrol tamamlanmadan public launch yapma. Basit app'lerde bile admin paneli, paywall entitlement'i ve kullanici verisi hatalari kalici hasar verebilir.

### Auth / Authorization
- [ ] Admin endpoint'leri sadece rol bazli yetkiyle calisiyor
- [ ] User content erisimi ID-only URL ile acilmiyor; ownership/session check var
- [ ] Entitlement/subscription status server veya guvenilir receipt kontroluyle dogrulaniyor
- [ ] Kullanici `isAdmin`, `role`, `credits`, `subscriptionStatus` gibi korumali alanlari update edemiyor

### Secrets / Backend
- [ ] API key, admin token, service role key frontend bundle'a koyulmadi
- [ ] Supabase RLS / Firestore rules / backend policy'leri test edildi
- [ ] Predictable ID riski kontrol edildi
- [ ] Webhook endpoint'lerinde signature verification var
- [ ] Crash/logging araclari PII veya token basmiyor

### AI Share Hygiene
- [ ] ChatGPT/Codex/Claude public share linkleri secret, private repo icerigi, musteri verisi icermiyor
- [ ] Paylasilacak prompt/log/screenshot'lar secret scrub'dan gecti
- [ ] `.env`, App Store Connect ekranlari ve payment/account bilgileri public gorselde yok

**Sonuc:** GECTI / EKSIK / UYGULANAMAZ. EKSIK ise launch checklist skorundan bagimsiz olarak once duzelt.

---

## TURKIYE OPERASYON: TESVIK VE PAYOUT CHECKLIST'I

Bu bolum yalnizca kurucu Turkiye'de sirket/operasyon yurutuyorsa, giderleri Turkiye'de belgelemek istiyorsa veya tesvik kullanacaksa uygulanir. Tweet/blog bilgisi kanit degildir; resmi ve guncel kaynak gerekir.

### Resmi Tesvik Dogrulama
- [ ] Ilgili resmi kurum/program sayfasinda guncel kapsam, limit, basvuru kosulu ve tarih kontrol edildi
- [ ] Reklam, tool, komisyon veya diger gider kalemlerinin kapsama girip girmedigi resmi kaynaktan yazildi
- [ ] Basvuru icin gerekli sirket/evrak/fatura/dekont kosullari not edildi
- [ ] Tutar/limit hard-code edilmedi; raporda "guncel resmi kaynakla dogrulanmali" notu var
- [ ] Mali musavir/uzman teyidi gerekiyorsa Sonraki Adimlar'a eklendi

### App Store Connect Payout
- [ ] Agreements, Tax, and Banking durumu aktif
- [ ] Banka hesap sahibi, ulke, IBAN/SWIFT/branch bilgisi dogru
- [ ] Vergi formlari ve sozlesmeler tamamlandi
- [ ] Payout para birimi ve muhasebe kaydi not edildi
- [ ] Apple komisyonu (%15 Small Business Program veya standart %30) finansal modele dogru yansitildi

**Kural:** Tesvik/payout uygunlugu pazar GO kararinin yerine gecmez; yalnizca maliyet ve launch fizibilitesi girdisidir.

---

## POST-LAUNCH METRIKLERI

### Hafta 1 Hedefleri

| Metrik | Minimum | Iyi | Mukemmel |
|---|---|---|---|
| Install | 100+ | 500+ | 1000+ |
| Trial baslama | %15+ | %20+ | %30+ |
| Day 1 retention | %25+ | %35+ | %45+ |
| Crash-free rate | %99+ | %99.5+ | %99.9+ |
| App Store rating | 4.0+ | 4.5+ | 4.8+ |
| App Store conversion | %20+ | %30+ | %40+ |
| Onboarding completion | %50+ | %65+ | %80+ |

### Ay 1 Hedefleri

| Metrik | Minimum | Iyi | Mukemmel |
|---|---|---|---|
| Total install | 300+ | 1000+ | 3000+ |
| Trial→Paid conversion | %5+ | %10+ | %15+ |
| MRR | $50+ | $200+ | $500+ |
| Day 7 retention | %10+ | %15+ | %25+ |
| Day 30 retention | %5+ | %8+ | %15+ |
| Organik install orani | %30+ | %50+ | %70+ |
| App Store rating sayisi | 10+ | 30+ | 100+ |
| Ortalama rating | 4.0+ | 4.5+ | 4.8+ |

### PMF Sinyali — Sean Ellis %40 Testi (Ay 1+)

Metriklerin yaninda tek standart PMF olcusu ekle. Yeterli aktif kullanici olunca (Ay 1-2) anket gonder:

> **Soru:** "[Uygulama]'yi artik kullanamasan ne hissederdin?"
> Secenekler: Cok uzulurdum / Biraz uzulurdum / Uzulmezdim / Zaten kullanmiyorum

- **Esik:** "Cok uzulurdum" >= **%40** = PMF sinyali (Sean Ellis benchmark'i, ~100 startupta dogrulanmis).
- **Kimlere:** Sadece NITELIKLI kullanicilar — cekirdek ozelligi yasamis, son donemde >=2 kez kullanmis olanlar. Ham signup'lari ve churn olanlari HARIC tut.
- **Ornek buyuklugu:** >=40 yanit hedefle (az yanit = gurultu).
- **Aksiyon:** <%40 ise "Cok uzulurdum" diyen kohortu segmentle (onlari ne ceken?), urunu o cekirdege daralt. Bu, Davranis sinyali (RF-16 uyumlu) — beyani degil, gercek kullanimi olcer.

### Ay 3 Kontrol Noktasi (KRITIK KARAR)

| Durum | MRR | Retention (D30) | Aksiyon |
|---|---|---|---|
| Basarili | $500+ | %10+ | Devam et, buyume yatirim yap |
| Umut verici | $100-500 | %6-10 | Optimize et (ASO, paywall, retention) |
| Zayif | $50-100 | %3-6 | Pivot dusun (fiyat, hedef kitle, ozellik) |
| Basarisiz | < $50 | < %3 | Kill veya radikal pivot |

**3. Ay Karar Cercevesi:**

Asagidaki 4 soruyu cevapla:

1. **Kullanicilar geri geliyor mu?** (D30 retention > %5)
   - Evet → urun-pazar uyumu var, buyumeye odaklan
   - Hayir → urun problemi var, retention duzelt veya pivot

2. **Kullanicilar oduyor mu?** (Trial→Paid > %5)
   - Evet → fiyatlandirma dogru, hacim artir
  - Hayir → fiyat cok yuksek, veya deger yeterince gosterilemiyor

3. **Organik buyume var mi?** (Organik install orani > %30)
   - Evet → ASO ve word-of-mouth calisiyor
   - Hayir → ASO optimize et veya paid acquisition dene

4. **Kullanicilar oneriyor mu?** (App Store rating 4.5+ ve yorum sayisi artiyor)
   - Evet → organik buyume devam edecek
   - Hayir → urun deneyimini iyilestir

5. **PMF sinyali var mi?** (Sean Ellis: "Cok uzulurdum" >= %40)
   - Evet → gercek PMF, buyumeye guvenle yatirim yap
   - Hayir → cekirdek kohorta daralt, %40'a cikana kadar buyume harcamasini ertele

---

## KANAL BAZLI TAKTIKLER

### Reddit

**Genel Kurallar:**
- KURAL #1: Deger kat, reklam yapma. Reddit bunu hemen anlar ve cezalandirir.
- "I built" formatinda paylasim yap — hikaye anlat, link birak
- Ilgili subreddit'lerin kurallarini LANSMANDAN ONCE oku
- Negatif yorumlara savunmaci olma, dinle ve ogren
- Her subreddit'e FARKLI post yaz (copy-paste yapma)
- Karma'n dusukse once yorum yap, karma kazan, sonra post at

**En Iyi Subreddit'ler:**
- r/SideProject — en rahat yer, self-promo kabul ediliyor
- r/AppIdeas — fikir tartismasi formati
- r/iOSProgramming — teknik hikaye (SwiftUI, architecture)
- r/productivity — eger productivity uygulamasiysa
- r/journaling — eger journaling uygulamasiysa
- r/personalfinance — eger finans uygulamasiysa (DIKKATLI ol, cok strict kurallar)
- r/apple — genel iOS uygulamalari (self-promo kurallari strict)
- Nis subreddit — hedef kitlenin takildigi yer

**Post Yapisi:**
```
Baslik: I built [App Name] — [bir cumle aciklama]

Icerik:
- Problem: Ne problemi cozuyor?
- Hikaye: Neden yaptin?
- Nasil: Kac ayda, hangi teknolojiler?
- Fark: Rakiplerden farki ne?
- Screenshot veya video link
- App Store link (yorum olarak, post'un icine degil)
- Soru: "Ne dusunuyorsunuz? Geri bildirim cok degerli."
```

### Product Hunt

**Zamanlama:**
- En iyi gun: Sali veya Carsamba
- En iyi saat: 00:01 PST (Turkiye 10:01)
- KACINILACAK gunler: Buyuk teknoloji sirketlerinin lansman gunleri

**Hazirlik Checklist'i:**
- [ ] Hunter bul veya kendi hesabinla lansman yap (hunter bonus traffic getirmez artik)
- [ ] Tagline: Maksimum 60 karakter, net ve merak uyandirici
- [ ] Aciklama: Problem → Cozum → Fark formatinda
- [ ] Gorseller: Logo (240x240), Gallery (1270x760), GIF veya video
- [ ] Maker comment taslagi: Kisisel, samimi, hikayeni anlat
- [ ] Ilk 100 upvote icin organik topluluk destegi planla

**Lansman Gunu:**
- Ilk 4 saat en kritik donem (PH algoritmasi bu saatlere agirlik verir)
- Her yoruma 5 dakika icinde cevap ver
- Durust ol: "Henuz bu ozellik yok ama planliyorum" de
- Diger maker'lara da destek ver (topluluk kulturu)

### Hacker News

**Format:**
```
Show HN: [App Name] — [teknik/deger odakli tanim]
```

**Basari Faktobleri:**
- Teknik derinlik (HN kitlesi teknik insanlar)
- Acik kaynaklik varsa buyuk avantaj
- Fiyatlandirma seffafligi
- "Show HN" postu tartisma postundan farkli — urun goster, soru sorma
- Ilk 30 dakikada 5+ upvote = front page sansi artar

**Hazirlik:**
- Teknik detaylari bilmeyen HN'ciler soru soracak — hazir ol
- "Neden bunu degil de X kullanayim?" sorusuna hazir ol
- Fiyatlandirma hakkinda soru GELECEK — net cevap ver
- Negatif yorum gelecek — savunma yapma, kabul et ve ogren

### Twitter/X

**Surekli Strateji (#buildinpublic):**
- Haftada 3-5 paylasim
- Icerik turleri:
  - Gelistirme sureci (screenshot, video clip)
  - Metrikler (install, gelir — seffaflik onemli)
  - Ogrenilen dersler
  - Kullanici geri bildirimleri (izinli)
  - Teknik zorluklar ve cozumler
- Diger indie dev'lerle etkilesim (yorum yap, RT yap)
- Thread formati haftada 1 kez (daha yuksek erisim)

**Thread Yapisi (Lansman):**
1. Hook tweet (dikkat cekmeli, merak uyandirmali)
2. Problem tanimi
3. Cozumun nasil calistigi (screenshot/video)
4. En etkileyici ozellik
5. Build sureci / zorluklar
6. Beta sonuclari / metrikler
7. Gelecek planlari
8. CTA (App Store link)

### Content Marketing / SEO

**Hedef Keyword'ler:**
- "[rakip] alternative" — en yuksek donusum orani
- "best [kategori] app 2026" — liste yazisi
- "[kategori] app for [nis]" — nis hedefleme
- "free [kategori] app" — ucretsiz tier varsa

**Blog Yazisi Turleri:**
1. **Karsilastirma:** "[Rakip] vs [App Name]" — tarafsiz ol, rakibin guclu yonlerini de yaz
2. **Liste:** "5 Best [Kategori] Apps in 2026" — kendi uygulamanı da ekle
3. **Hikaye:** "Why I Built [App Name]" — kisisel, samimi
4. **Rehber:** "How to [problem]" — cozum olarak uygulamani goster
5. **Case study:** "[Kullanici] nasil [sonuc] elde etti" — sosyal kanit

**Yayinlama Platformlari:**
- Medium (yuksek domain authority, ama algoritma degisken)
- Dev.to (teknik kitle icin)
- Kendi blog (uzun vadede en iyi SEO)
- LinkedIn makaleleri (profesyonel kitle)

---

## ASO ITERASYON SURECI

Lansmandan sonra ASO surekli optimize edilmeli. Tek seferlik degil, surekli bir surec.

### Hafta 2: Ilk Veri Analizi

**Kontrol Edilecek Metrikler:**
- [ ] Hangi keyword'ler impression getiriyor? (App Store Connect → App Analytics)
- [ ] Product page conversion rate nedir? (Impression → Install)
- [ ] Hangi screenshot en cok goruntuleniyor? (varsa Custom Product Pages ile A/B test)
- [ ] Keyword rank pozisyonlari (AppTweak veya ASOTools ile)
- [ ] Rakiplerin keyword degisiklikleri

**Ilk Aksiyon:**
- Impression getiren ama dusuk rank olan keyword'leri belirle — bunlari yukari cekmeye odaklan
- Hic impression getirmeyen keyword'leri listele — degistirmeye aday

### Hafta 4: Ilk Optimizasyon

**Subtitle Optimizasyonu:**
- En yuksek hacim keyword'u subtitle'in BASINA al
- 30 karakter limitini maksimum kullan
- Ornek: "Simple Budget Tracker & Planner" → cok fazla keyword, okunakli olmali

**Screenshot Optimizasyonu:**
- Ilk screenshot'i en yuksek conversion ekrani ile degistir
- A/B test: Metin agirlikli vs gorsel agirlikli screenshot
- Ilk 3 screenshot en cok gorulur — en guclu mesajlari buraya koy

**Keyword Field Optimizasyonu:**
- Dusuk performans keyword'leri cikar
- Yeni keyword ekle (rakip analizi + Google Trends verileri)
- Keyword field'da bosluk kullan, virgul kullanma
- Subtitle'da olan keyword'leri tekrarlama (bos yer israf)

### Ay 2+: Surekli Test ve Optimizasyon

**Her 2-4 Haftada Bir:**
- [ ] Screenshot sirasi veya icerigi degisikligi
- [ ] Subtitle tweaki (keyword onceligi degisimi)
- [ ] Keyword field guncelleme
- [ ] Aciklama metninin ilk 3 satirini guncelle (fold ustunde en onemli mesaj)

**Mevsimsel Adaptasyon:**
- Ocak: "New Year", "resolution", "start fresh" keyword'leri
- Nisan: "tax", "budget season" (ABD pazari)
- Eylul: "back to school", "organize", "plan" keyword'leri
- Kasim-Aralik: "gift", "holiday", "end of year" keyword'leri

**Rakip Keyword Takibi:**
- Rakiplerin subtitle ve keyword degisikliklerini aylik izle
- Rakibin biraktigi keyword'leri almaya calis
- Rakibin yeni hedefledigi keyword'leri takip et

**Custom Product Pages (CPP):**
- Farkli trafik kaynaklari icin ozel App Store sayfalari olustur
- Reddit'ten gelenler icin: community odakli mesaj
- Google Ads'ten gelenler icin: keyword odakli mesaj
- Sosyal medyadan gelenler icin: gorsel odakli mesaj
- Her CPP icin ayri conversion rate takip et

---

## PIVOT/PERSEVERE KARAR CERCEVESI

### Devam Et (Persevere) Sinyalleri

- Trial→Paid conversion > %8 (surekli, tek seferlik spike degil)
- Day 7 retention > %12 (kullanicilar geri geliyor)
- Organik indirmeler haftalik artis trendinde (%5-10 haftalik buyume)
- Kullanicilardan pozitif geri bildirim (App Store 4.5+ rating)
- En az 1 kanal surekli ve olceklenebilir trafik getiriyor
- Word-of-mouth var (kullanicilar baskasina oneriyor)
- Kullanicilar ozellik istegi yapiyor (ilgileniyorlar = onemsiyor)
- MRR ay bazinda artiyor (dusuk bile olsa, trend onemli)

### Optimize Et Sinyalleri

- Trial→Paid %5-8 arasi (iyi ama iyilestirilebilir)
- Day 7 retention %8-12 arasi
- Organik indirmeler sabit (artmiyor ama dusmuyor)
- Rating 4.0-4.5 arasi
- 1-2 potansiyel buyume kanali var ama optimize edilmemis

**Optimizasyon Oncelikleri:**
1. Paywall zamanlama ve tasarim testi
2. Onboarding akisi iyilestirmesi
3. ASO optimizasyonu (keyword, screenshot)
4. Push notification stratejisi (retention icin)
5. Fiyat testi (daha yuksek veya daha dusuk)

### Pivot Sinyalleri

- Trial→Paid < %5 (3 hafta boyunca, iyilestirme denemelerine ragmen)
- Day 7 retention < %8
- Indirmeler haftalik dusus trendinde
- Kullanici geri bildirimi "I don't need this" veya "meh" tonunda
- Hicbir kanal surekli trafik getirmiyor
- Kullanicilarin cogu ucretsiz tier'de kaliyor ve premium'a gecmiyor

**Pivot Secenekleri:**
1. **Hedef kitle pivotu:** Ayni urun, farkli kitleye (ornk: bireysel → freelancer)
2. **Fiyat pivotu:** Subscription → one-time purchase veya tersi
3. **Ozellik pivotu:** Core ozelligi degistir (ornk: journaling → gratitude only)
4. **Platform pivotu:** iOS → macOS veya web
5. **Is modeli pivotu:** B2C → B2B (ornk: takim planlama araci)

### Kill Sinyalleri

- 3 ayda MRR < $50
- Day 1 retention < %15 (kullanicilar ilk gunde bile geri gelmiyor)
- Kullanicilar "bunu zaten [diger app] yapiyor" diyor surekli
- Teknik borc cok buyuk, iterasyon yavas (1 ozellik = 2 hafta)
- Kendin bile uygulamani kullanmiyorsun
- Motivasyonun tamamen dusmus
- 3 farkli pivot denemesi basarisiz olmus

**Kill Ettikten Sonra:**
1. Mevcut kullanicilara 30 gun onceden bildirim yap
2. Data export imkani sun
3. Ogrenilen dersleri dokumante et (sonraki proje icin)
4. Code base'i acik kaynaga ac (opsiyonel ama iyi niyetli)
5. Post-mortem blog yazisi yaz (topluluk icin degerli)

---

## FIYATLANDIRMA STRATEJISI

### Model Secenekleri

| Model | Avantaj | Dezavantaj | Ne Zaman Sec |
|---|---|---|---|
| Freemium + Subscription | Onceden tahmin edilebilir gelir, dusuk bariyer | Churn riski, surekli deger sunmali | Gunluk/haftalik kullanim uygulamalari |
| Free Trial + Subscription | Yuksek conversion (kullanici degeri gorur) | Trial suresi bitmeden terk edenler | Premium ozellikli uygulamalar |
| One-time Purchase | Subscription fatigue avantaji, basit | Gelir tahmini zor, surekli yeni kullanici gerek | Utility uygulamalari |
| Freemium + IAP | Esnek, kullanici istedigini satin alir | Karmasik implementasyon | Cok ozellikli uygulamalar |
| Paymium (odenen indirme) | Gelen kullanici ciddiler | Dusuk install hacmi | Nis, premium uygulamalar |

### Fiyat Noktasi Rehberi

**Subscription:**
- Haftalik: $1.99-4.99 (yuksek conversion, dusuk LTV)
- Aylik: $2.99-9.99 (en yaygin)
- Yillik: $19.99-59.99 (en iyi LTV, ayliga gore %40-50 indirimli sun)
- Onerilen: Yillik plani one cikar, ama aylik secenegi de sun

**One-time Purchase:**
- Utility/basit: $4.99-9.99
- Orta karmasiklik: $14.99-29.99
- Premium/profesyonel: $39.99-79.99
- Tip: Psychological pricing kullan ($9.99, $29.99)

### Lansman Indirimi Stratejisi

- Lansman haftasi: %50 indirim (FOMO + erken adaptorler)
- Ilk ay: %30 indirim
- Ikinci ay: %20 indirim
- Ucuncu ay+: Normal fiyat

**Onemli:** Indirim surekli yapma. Surekli indirim = "gercek fiyat" algisi olusturur ve normal fiyata donmek zorlaşır.

---

## LANSMAN SONRASI HAFTALIK RUTIN

### Her Pazartesi (30 dk)
- [ ] Gecen haftanin metriklerini incele (install, revenue, retention)
- [ ] App Store yorumlarini oku ve cevaplamayi planla
- [ ] Bu haftanin 3 onceligi ne?

### Her Carsamba (20 dk)
- [ ] ASO metriklerini kontrol et (keyword rank degisimi)
- [ ] Rakip degisikliklerini kontrol et (yeni guncelleme, fiyat degisimi)
- [ ] #buildinpublic paylasimlari yap

### Her Cuma (30 dk)
- [ ] Haftalik ozet raporu olustur
- [ ] Kullanici geri bildirimlerini derle
- [ ] Gelecek hafta icin oncelikleri belirle
- [ ] App Store yorumlarini cevapla

---

## CHECKLIST: LANSMAN HAZIRLIK SKORU

Lansman oncesinde bu checklist'i doldur. Her "evet" = 1 puan.

**Urun Hazirliyi (10 puan):**
- [ ] MVP tamamlandi ve calisiyor (crash-free)
- [ ] Onboarding 60 saniyenin altinda
- [ ] In-app purchase/subscription calisiyor
- [ ] Analytics entegre ve calisiyor
- [ ] Crash reporting entegre
- [ ] TestFlight beta en az 30 kisi tarafindan test edildi
- [ ] Beta NPS > 7
- [ ] En az 1 kisi "bunu para verip kullanirim" dedi
- [ ] Performance kabul edilebilir (launch < 2sn)
- [ ] Accessibility temelleri mevcut (VoiceOver, Dynamic Type)

**Pazarlama Hazirliyi (10 puan):**
- [ ] App Store sayfa metinleri hazir
- [ ] Screenshot'lar hazir (en az 6 adet)
- [ ] Landing page canli ve calisiyor
- [ ] Email listesinde en az 50 kisi var
- [ ] Twitter/X hesabi aktif ve takipci var
- [ ] Reddit'te karma yeterli (en az 100)
- [ ] Product Hunt sayfasi hazir
- [ ] Blog yazisi / lansman icerigi hazir
- [ ] Lansman gunu sosyal medya postlari hazir
- [ ] Press kit / medya paketi hazir

**Skor Degerlendirmesi:**
- 16-20 puan: Lansaman icin hazirsin. Git!
- 12-15 puan: Birkac eksik var ama lansman yapilabilir
- 8-11 puan: Daha fazla hazirlik gerekli, 2 hafta ertele
- 0-7 puan: Henuz hazir degilsin, checklist'i tamamla

---

## KAYNAKLAR VE ARACLAR

### Ucretsiz Araclar
- **Landing Page:** Carrd.co ($19/yil), GitHub Pages (ucretsiz)
- **Email:** Buttondown (ucretsiz, 100 abone), MailChimp (ucretsiz, 500 abone)
- **Analytics:** TelemetryDeck (ucretsiz tier), Firebase Analytics (ucretsiz)
- **Crash Reporting:** Firebase Crashlytics (ucretsiz)
- **Subscription:** RevenueCat (ucretsiz, $2.5K/ay gelire kadar)
- **Paywall Pattern:** Adapty Paywall Library (pattern referansi; kopyalama degil)
- **Screenshot Mockup:** Previewed.app, Rotato (trial), Figma (ucretsiz), Codia AI Design / screenshot-to-Figma (uretim yardimi)
- **Privacy Policy:** PrivacyPolicies.com, iubenda (ucretsiz tier)

### Ucretli Araclar (Buyudukce)
- **ASO:** AppTweak ($69/ay), ASOTools ($49/ay)
- **Market Data:** Sensor Tower (eski data.ai dahil), AppFigures, AppMagic
- **Product Flow Research:** Mobbin (onboarding/paywall/screenshot pattern kutuphanesi)
- **A/B Test:** SplitMetrics ($100+/ay)
- **Email (buyudukce):** ConvertKit, Beehiiv
- **Design:** Figma Pro ($12/ay), Rotato ($49)

### Ogrenme Kaynaklari
- **Podcast:** Indie Hackers, Under the Radar, The Changelog
- **Twitter:** @IndieHackers, @levelsio, @marc_louvion
- **Kitap:** "The Mom Test" (Rob Fitzpatrick) — kullanici arastirmasi icin SART
- **Blog:** IndieHackers.com, indiehackers.com/podcasts
- **Video:** Sean Allen (YouTube, iOS gelistirme), Paul Hudson (Hacking with Swift)
