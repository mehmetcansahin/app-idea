# App Arastirma Raporu: [KONU]

> Tarih: [TARIH]
> Mod: Quick Scan / Standard / Deep
> Metodoloji: v3.4 - sablon rev. v3.4 (10 Faz + Faz 5.5, 3 Katmanli Puanlama + Dagitim Fizibilitesi + Geo-LTV + Visual Intelligence + JTBD/Lean Canvas/PMF)

---

## Yonetici Ozeti

| Alan | Deger |
|------|-------|
| **Karar** | GO / SARTLI GO / NO-GO / ELENDIR |
| **Durum** | ARASTIRMA TAMAM / FAZ 5.5 BEKLIYOR / DOGRULANDI / TERK / ARSIV |
| **Guven** | %XX (Faz 5 sonrasi tipik %30-50; Faz 5.5 sonrasi GO icin >=%70) |
| **Final Skor** | X/100 (K2) × X.XX (K3) = **XX.X** |
| **Risk Seviyesi** | DUSUK / ORTA / YUKSEK / COK YUKSEK |
| **MVP Tahmini** | X hafta |
| **Hedef Geo / Geo-LTV** | [US/UK/TR/global] — YUKSEK / ORTA / DUSUK / BELIRSIZ |
| **Dagitim Fizibilitesi** | KD ~XX (DUSUK/ORTA/YUKSEK) — [kesfedilebilir mi, 1 cumle] |
| **Anahtar Bulgu** | [1-2 cumle] |
| **Oneri** | [1-2 cumle] |

---

## 1. Pazar Analizi

### 1.1 Pazar Durumu
| Gosterge | Deger | Etiket |
|----------|-------|--------|
| Ana Keyword | [keyword] | — |
| Lider Uygulama | [app adi] | — |
| Lider Rating | [sayi] | KESIN |
| Lider Yildiz | [X/5] | KESIN |
| Pazar Sinifi | Guclu / Orta / Mikro | — |
| Google Trends | YUKARI / DUZ / ASAGI | TAHMINI |
| Yasam-Dongusu | Exploding / Regular / Peaked + Ustel / Sabit / Duragan | TAHMINI |
| Mevsimsellik | [varsa aciklama] | TAHMINI |
| Hedef Geo | [ulke/bolge] | — |
| Geo-LTV Sinifi | YUKSEK / ORTA / DUSUK / BELIRSIZ | TAHMINI / KESIN (first-party ise) |

### 1.2 Pazar Gecerliligi (Katman 1)
| Kriter | Sonuc |
|--------|-------|
| Pazar var mi? (rating > 500) | GECTI / KALDI |
| Erisilebilir mi? (Apple/Google engeli yok) | GECTI / KALDI |
| Buyuyor mu? (trend + yeni girisler) | GECTI / KALDI |
| Regulasyon asilabilir mi? (indie icin) | GECTI / KALDI |

### 1.3 Dagitim Fizibilitesi (Kesfedilebilirlik) ⚐ STANDARD+
*Quick Scan'de bu bolum atlanir; keyword difficulty override'i puanlama icinde kisa uygulanir.*

| Hedef Keyword | Top-10 Rating Profili | Difficulty (0-100) | Rank Sansi |
|---------------|----------------------|--------------------|-----------|
| [keyword 1] | [ornk: hepsi 5K+ / karisik / dusuk] | ~XX | VAR / YOK |
| [keyword 2] | ... | ~XX | ... |

| Kontrol | Sonuc | Etiket |
|---------|-------|--------|
| Paid kanal doygunlugu (ad library: lider kreatif sayisi/longevity) | DOYGUN / ORTA / BOS | KESIN (browser) / TAHMINI (WebSearch) |
| Organik/ASO wedge var mi? | [wedge tanimi veya YOK] | — |
| En az 3 orta-hacim/dusuk-difficulty keyword? | EVET / HAYIR (HAYIR ise fizibilite UYARISI) | TAHMINI |
| Hedef geo'da LTV:CAC varsayimi | SAGLIKLI / DAR / BELIRSIZ | TAHMINI / KESIN |

### 1.4 Geo-LTV / Hedef Ulke ⚐ STANDARD+
*Quick Scan'de tam tablo atlanir; Yonetici Ozeti'nde `Hedef Geo / Geo-LTV` satiri ve Pazar Analizi'nde tek cumlelik uyari yeterlidir.*

| Ulke/Bolge | LTV Sinifi | Dil/ASO | CAC Riski | Kaynak | Not |
|------------|------------|---------|-----------|--------|-----|
| [US] | YUKSEK | EN | ORTA | [RevenueCat/Adapty/App Store Connect] | [not] |
| [TR] | DUSUK/ORTA | TR | DUSUK/ORTA | [kaynak] | [tesvik/payout gerekiyorsa not] |

**Geo-LTV yorumu:** [K2 formulune dahil degil; gelir/dagitim guvenini nasil etkiliyor?]

---

## 2. Rakip Analizi

### Top 5 Rakip
| # | Uygulama | Rating | Yildiz | Fiyat | Model | Son Guncelleme |
|---|----------|--------|--------|-------|-------|----------------|
| 1 | [app] | [sayi] | [X/5] | [fiyat] | [model] | [tarih] |
| 2 | ... | ... | ... | ... | ... | ... |

### Sikayet Temalari (1-2 Yildiz Review Mining)
| # | Tema | Siklik | Ornek |
|---|------|--------|-------|
| 1 | [tema] | ~X yorum | "[ornek]" |
| 2 | ... | ... | ... |

**Adlandirilmis Icgoru (Rekabet 4-5 icin ZORUNLU):** [Rakiplerin kacirdigi SPESIFIK icgoru tek cumleyle — neden onlar yapmamis/yapamamis. Adlandirilamiyorsa Rekabet MAX 3.]

**Goc Dinamigi (JTBD Forces) ⚐ STANDARD+:** [Kullanicilar mevcut cozumden NEDEN ayriliyor/ayrilmiyor? Push (iten aci) + Pull (ceken vaat) vs Anxiety (gecis korkusu) + Habit (aliskanlik). Push+Pull > Anxiety+Habit ise goc gercek; degilse fantezi (RF-7).]

### Visual Intelligence ⚐ STANDARD+
| Rakip | Kaynak URL/Tool | Erisim Tarihi | Storefront/Country | Incelenen Ekran/Akis | Gorulen Metin | Kanit Etiketi | Screenshot/File Path | Paywall Pattern | Bos Kalan Aci |
|-------|-----------------|---------------|--------------------|-----------------------|--------------|---------------|----------------------|-----------------|---------------|
| [app] | App Store URL / Mobbin / Adapty | [YYYY-MM-DD] | [US/TR/global] | Screenshot / Onboarding / Paywall | [mesaj/CTA] | KESIN/TAHMINI/DUSUK | [path veya YOK] | [pattern] | [wedge] |

**Not:** Codia/screenshot-to-Figma kullanildiysa kaynak olarak "uretim yardimi" diye yaz; pazar kaniti sayma.

### 2x2 Stratejik Konumlandirma ⚐ DEEP
[Kullanici-degeri 2 ekseni (or. Basitlik <-> Guc) + rakiplerin yerlesimi + bos pozisyon/wedge. Bos ceyrek ancak adlandirilmis icgoruyle firsattir.]

### Fiyat Karsilastirmasi
| Metrik | Deger |
|--------|-------|
| [Rakip 1] | $X [model] |
| [Rakip 2] | $X [model] |
| ... | ... |
| **Ortalama aylik** | $X |
| **Medyan aylik** | $X |
| **Fiyat araligi** | $X — $X |
| **Lifetime sunan** | X/Y rakip |
| **Hakim model** | Tek seferlik / Abonelik / Freemium |

---

## 3. Firsat Puanlama

### Katman 2: Firsat Kalitesi (/100)
| Kriter | Agirlik | Skor (1-5) | Puan | Veri Kaynagi |
|--------|---------|-----------|------|-------------|
| Talep Sinyali | ×5 | [X] | [XX] | [kaynak + etiket] |
| Gelir Kaniti | ×5 | [X] | [XX] | [kaynak + etiket] |
| Rekabet Boslugu | ×4 | [X] | [XX] | [kaynak + etiket] |
| Retention | ×3 | [X] | [XX] | [kaynak + etiket] |
| Zamanlama | ×3 | [X] | [XX] | [kaynak + etiket] |
| **Toplam** | | | **[XX]** | |

**Uygulanan Override:** [varsa listele — tam liste: `methodology/scoring-model.md`]

**Geo-LTV / Dagitim Guveni:** [Hedef ulke LTV/CAC varsayimi gelir veya paid UA guvenini artiriyor mu, yoksa UYARI mi? K2 formulu degismedi.]

### Katman 3: Fizibilite Carpani
| Kriter | Skor | Gerekce |
|--------|------|---------|
| Teknik Zorluk | [0.6/0.8/1.0] | [aciklama] |
| Kurucu Uyumu | [0.6/0.8/1.0] | [aciklama] |
| Regulasyon/Uyum | [0.6/0.8/1.0] | [aciklama — 1.0 ise regulasyon yok] |
| MVP Suresi | [0.6/0.8/1.0] | [aciklama] |
| **Carpan** | **[X.XX]** | |

### Final Skor
**[K2 Toplam] × [K3 Carpan] = [Final Skor]** → [Guclu (60+) / Orta (45-59) / Zayif (30-44) / Elendir (<30)]

---

## 4. Gelir Potansiyeli

### Indie Gelir Kaniti
| # | Kim | Uygulama | Gelir | Kaynak | Guvenilirlik |
|---|-----|----------|-------|--------|-------------|
| 1 | [developer] | [app] | [miktar] | [kaynak] | KESIN/TAHMINI/DUSUK |

*Bulunamadiysa: "X farkli sorgu yapildi, indie gelir kaniti BULUNAMADI"*

**Satin-alma/exit komparasyonu (B5):** [Acquire.com/Flippa ilani veya Starter Story medyani varsa: ima edilen MRR = satis fiyati / carpan. Ankora (>=$1K/ay) eslesiyorsa "Gelir MAX 2" override'ini kaldirir. Tek/zayif komparasyon = TAHMINI, MAX 3.]

**Reklam longevity sinyali:** [2+ rakip 6+ aydir kesintisiz reklam donduruyorsa belirt — parasallasma DAVRANIS kaniti; indie gelir kaniti DEGILDIR, "Gelir MAX 2" kuralini degistirmez]

**Geo-LTV monetizasyon notu:** [Ulke bazli LTV/CAC benchmark'i, fiyat tier ve localization riski. Benchmark TAHMINI ise acikca yaz.]

### Quantified Value Prop ⚐ STANDARD+
[Status quo'ya gore degeri SAYISALLASTIR: "X saat / $Y / Z adim tasarruf". Fiyatlandirma ve Talep argumanini besler.]

### Fiyat Modeli Onerisi
| Plan | Fiyat | Icerik |
|------|-------|--------|
| Ucretsiz | $0 | [icerik] |
| Premium | $X/ay | [icerik] |
| Yillik | $X/yil | [icerik] |

---

## 5. Dogrulama ⚐ STANDARD+

### 5.1 — 4 Dogrulama Kontrolu
| # | Kontrol | Sonuc | Guvenilirlik |
|---|---------|-------|-------------|
| 1 | Lider rating gercek mi? | [sonuc] | KESIN |
| 2 | Indie gelir kaniti | [sonuc] | [etiket] |
| 3 | Kullanici goc sinyali | [sonuc] | [etiket] |
| 4 | Menopoz Testi | GECTI / KALDI / UYGULANAMADI | [etiket] |

**Dogrulama Sonucu:** DOGRULANDI / KISMI / DOGRULANAMADI

### 5.2 — Faz 5.5 Build-Oncesi Dogrulama Plani ⚐ (Karar GO/SARTLI GO ise ZORUNLU)
*Detay ve kurallar: `methodology/pre-build-validation.md`. Bu faz INSAN-aksiyonudur; burada plan teslim edilir, Durum "FAZ 5.5 BEKLIYOR" olur.*

| Alan | Deger |
|------|-------|
| Baslangic guven (Faz 5 sonrasi) | %XX |
| A) Landing/fake-door | Kur: [Carrd/GitHub Pages] — Trafik: [watering-hole / $20-50 reklam] |
| **ONCEDEN yazilan esik** | "[kaynak]tan gelen X ziyaretcinin %Y'si email birakirsa GO" |
| B) Mom-Test gorusmeleri | n=5-10, hedef: [kitle] — kilavuz: [link/ek] |
| GO esigi | Guven >=%70 + en az 1 GERCEK davranis sinyali (beyan yetmez, RF-16) |
| Basarisizlik yolu | Sadece beyan → Talep/Gelir MAX 3; problem dogrulanamadi → SISP (RF-17), KILL/PIVOT |

---

## 6. Risk Degerlendirmesi

### Regulasyon Riski ⚐ (varsa)
*Bu bolum sadece regulasyon engeli olan pazarlar icin doldurulur.*

| Alan | Detay |
|------|-------|
| Gecerli yasalar | [FCRA, HIPAA, CCPA, vb.] |
| Ceza ornekleri | [varsa gercek ceza/dava ornekleri] |
| Indie etkisi | [indie developer icin ne anlama geliyor] |
| Uyum maliyeti | [tahmini maliyet] |

### Ana Riskler
| # | Risk | Olasilik | Etki | Onlem |
|---|------|----------|------|-------|
| 1 | [risk] | Dusuk/Orta/Yuksek | [etki] | [onlem] |
| 2 | ... | ... | ... | ... |

### Security Preflight + AI Share Hygiene ⚐ STANDARD+
| Kontrol | Sonuc | Not |
|---------|-------|-----|
| Admin endpoint auth/role check | GECTI / EKSIK / UYGULANAMAZ | [not] |
| User content ownership/token check | GECTI / EKSIK / UYGULANAMAZ | [not] |
| Frontend secret/API admin token yok | GECTI / EKSIK / UYGULANAMAZ | [not] |
| Supabase RLS/Firestore rules/backend auth | GECTI / EKSIK / UYGULANAMAZ | [not] |
| Protected fields client update riski | GECTI / EKSIK / UYGULANAMAZ | [not] |
| Public AI share secret scrub | GECTI / EKSIK / UYGULANAMAZ | [not] |

### Turkiye Tesvik / Payout ⚐ Gerekiyorsa
| Alan | Deger |
|------|-------|
| Uygulanir mi? | EVET / HAYIR |
| Resmi kaynak | [URL + erisim tarihi; yoksa BELIRSIZ] |
| Kapsam | Reklam / tool / komisyon / diger |
| Hard-coded tutar kullanildi mi? | HAYIR |
| App Store Connect payout hazirligi | [banking/tax/contracts notu] |

**Kural:** Tesvik kaniti icin `site:gov.tr` resmi kaynak ara. Resmi kaynak yoksa sonuc BELIRSIZ; tweet/blog ile tutar, limit veya kapsam yazma.

---

## 7. MVP Onerisi ⚐ STANDARD+

### Lean Canvas (1 sayfa) ⚐ DEEP
| Problem | Musteri Segmenti | UVP | Cozum | Kanallar |
|---------|------------------|-----|-------|----------|
| [top 3 problem] | [hedef kitle] | [essiz deger onerisi] | [top 3 ozellik] | [ASO/Reddit/PH...] |

| Gelir Akisi | Maliyet Yapisi | Anahtar Metrikler | Haksiz Avantaj (= Moat) |
|-------------|----------------|-------------------|-------------------------|
| [fiyat modeli] | [Apple %, altyapi, UA] | [aktivasyon/retention/MRR] | [veri/network/gecis...] |

*Bos kalan blok = kapatilmasi gereken arastirma boslugu.*

### Ekranlar (Normal MVP: Max 4 Core Product Screen)
| # | Ekran | Ne Yapar |
|---|-------|----------|
| 1 | [ekran] | [aciklama] |

### 3 Ana Ozellik
1. **[ozellik]:** [aciklama]
2. **[ozellik]:** [aciklama]
3. **[ozellik]:** [aciklama]

### V1'de OLMAYACAKLAR
- [kapsam disi 1]
- [kapsam disi 2]

### 1 Haftalik Micro-MVP Sprint Opsiyonu ⚐ (Faz 5.5 DOGRULANDI + basit app ise)
| Gun | Cikti |
|-----|-------|
| Pazartesi | Keyword/final scope |
| Sali | Proje kurulumu + onboarding |
| Carsamba | Max 4 core ekran MVP + gerekiyorsa 1 paywall/upgrade ekran |
| Persembe | Paywall + market-fit copy |
| Cuma | Test + screenshots |
| Cumartesi | App Store submit |
| Pazar | Marketing/community posts |

### Teknik Stack Onerisi
| Alan | Oneri |
|------|-------|
| Platform | [platform] |
| Framework | [framework] |
| DB | [db] |
| Odeme | [odeme] |

---

## 8. ASO Stratejisi ⚐ DEEP

| Alan | Oneri |
|------|-------|
| App Name (30 kar) | [oneri] |
| Subtitle (30 kar) | [oneri] |
| Keywords (100 kar) | [oneri] |
| Screenshot 1 | [mesaj] |
| Screenshot 2 | [mesaj] |
| Screenshot 3 | [mesaj] |
| Paywall / onboarding pattern | [Mobbin/App Store/Adapty referansindan cikan hipotez] |
| Screenshot uretim yardimi | [Codia/Figma/Rotato vb. kullanilacaksa] |

---

## 9. Sonraki Adimlar

1. [ ] [adim 1]
2. [ ] [adim 2]
3. [ ] [adim 3]

*Karar GO/SARTLI GO ise: ilk adim Faz 5.5 planinin (bolum 5.2) yurutulmesidir. Faz 5.5 DOGRULANDI ile biterse lansman hazirligi icin `methodology/launch-playbook.md` ile devam et.*
*Basit app + Faz 5.5 DOGRULANDI ise: Sonraki Adimlar'a max 4 core ekran + gerekiyorsa 1 paywall/upgrade ekranlik 1 haftalik micro-MVP sprint opsiyonunu ekle. Turkiye operasyonu varsa resmi tesvik/payout dogrulamasini ayri adim yap.*

---

## 10. Cross-Report Karsilastirma ⚐ (onceki analizler varsa)

*Guncel skorlar icin `output/INDEX.md` scoreboard'una bak; bu tabloyu ve INDEX'i senkron tut.*

| Fikir | K2 | K3 | Final | Karar | Ana Avantaj | Ana Risk |
|-------|----|----|-------|-------|-------------|----------|
| [fikir 1] | XX | X.XX | XX.X | [karar] | [1 cumle] | [1 cumle] |
| [fikir 2] | XX | X.XX | XX.X | [karar] | [1 cumle] | [1 cumle] |

---

## Veri Kaynaklari

| # | Kaynak | Erisim Tarihi | Guvenilirlik |
|---|--------|---------------|-------------|
| 1 | [kaynak] | [tarih] | KESIN/TAHMINI/DUSUK |

---

*Bu rapor App Idea Research Agent v3.4 metodolojisi ile olusturulmustur.*

---

## Mod Bazli Bolum Haritasi

| Bolum | Quick Scan | Standard | Deep |
|-------|-----------|----------|------|
| Yonetici Ozeti (+Durum +Guven) | ✓ | ✓ | ✓ |
| 1.1-1.2 Pazar Analizi (+yasam-dongusu, +regulasyon K1) | ✓ | ✓ | ✓ |
| 1.3 Dagitim Fizibilitesi | — (puanlamada kisa) | ✓ | ✓ |
| 1.4 Geo-LTV / Hedef Ulke | kisa ozet, tam tablo yok | ✓ | ✓ + finansal model |
| 2. Rakip Analizi (+adlandirilmis icgoru) | ✓ (top 5) | ✓ (top 10) | ✓ (top 10+) |
| Visual Intelligence | — | ✓ | ✓ |
| 3. Firsat Puanlama (+regulasyon K3) | ✓ | ✓ | ✓ |
| 4. Gelir Potansiyeli (+reklam longevity) | ✓ (basit) | ✓ (detayli) | ✓ (finansal model) |
| 5.1 Dogrulama (4 kontrol) | — | ✓ | ✓ |
| 5.2 Faz 5.5 Plani | — (Sonraki Adimlar'da oneri) | ✓ (GO/SARTLI GO ise) | ✓ (GO/SARTLI GO ise) |
| 6. Risk Degerlendirmesi (+regulasyon riski + security) | ✓ (top 3) | ✓ | ✓ |
| 7. MVP Onerisi (+micro-MVP opsiyonu) | — | ✓ | ✓ |
| 8. ASO Stratejisi (+paywall/screenshot pattern) | — | — | ✓ |
| 9. Sonraki Adimlar | ✓ | ✓ | ✓ |
| 10. Cross-Report Karsilastirma | — | ✓ (varsa) | ✓ |
| Veri Kaynaklari | ✓ | ✓ | ✓ |
