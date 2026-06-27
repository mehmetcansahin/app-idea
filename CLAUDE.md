# App Idea Research Agent

> Herhangi bir app fikri icin otomatik pazar arastirmasi yapan bir research agent.
> Kullanici "X konusunda bir app yapmak istiyorum" dediginde, bu talimatlar cercevesinde
> sistematik analiz yapilir ve yapilandirilmis rapor uretilir.

## Nasil Calisir

1. Kullanici bir app fikri/konusu belirtir
2. Agent modu belirler (kullaniciya sorar veya fikirden cikarir)
3. Pipeline calistirilir — her faz bir oncekinin ciktisini kullanir
4. Sonuclar `output/{tarih}-{konu}/` klasorune kaydedilir
5. Final rapor (`REPORT.md`) kullaniciya sunulur
6. `output/INDEX.md` scoreboard guncellenir (yeni satir; ayni konu yeniden analiz edildiyse eski satirin Durum'u "ARSIV" yapilir)

Kisayol komutlari: `/quick-scan`, `/standard`, `/deep`, `/compare` (bkz. `.claude/commands/`).

## Calisma Modlari

### 1. Quick Scan (~30 dakika)
**Ne zaman:** "Hizli bir fikir var, bakmak istiyorum" veya ilk kaba deger bicme

**Pipeline:**
1. **Girdi analizi + disambiguation** → konu, keyword, hedef kitle cikar. Konu birden fazla anlama gelebiliyorsa (ornk: "people finder" = background check MI, eski arkadaslari bulma MI, dating safety MI?) → alt segmentleri listele, kullaniciya sor. Kullanici belirtmezse en belirgin yorumu kullan + raporda diger yorumlari not et.
2. **[PARALEL]**
   - App Store lider tespiti + top 5 rakip metadata (WebSearch + WebFetch)
   - Google Trends kontrol (WebSearch — direkt trends.google.com interaktif grafigi okunamaz, arama sonuclarindan cikarim yap)
   - Reddit hizli tarama (1 sorgu: "[keyword] app reddit")
3. Hizli 3 katmanli puanlama (K1 pass/fail + K2 agirlikli + K3 fizibilite)
   - **Early termination:** K1 KALDI ise → puanlama tamamla ama raporda "ELENDIR (K1 fail)" yaz, MVP/detay bolumlerini atla
   - **Early termination:** K3 < 0.5 ise → raporda "Fizibilite cok dusuk — detay analiz gereksiz" notu ekle
4. → `REPORT.md` (1-2 sayfa fizibilite raporu)
   - Karar GO/SARTLI GO ise: Sonraki Adimlar'a Faz 5.5 build-oncesi dogrulama onerisi ekle (Quick'te opsiyonel — bkz. `methodology/pre-build-validation.md`)

**Minimum rakip sayisi:** 5
**Rapor bolumleri:** Yonetici Ozeti, Pazar Analizi, Rakip Analizi, Puanlama, Risk, Sonraki Adimlar, Kaynaklar
**Raporda ATLANACAK bolumler:** Dogrulama (#5, 5.2 Faz 5.5 plani dahil), MVP Onerisi (#7), ASO (#8), Dagitim Fizibilitesi tam bolumu (1.3 — Quick'te sadece puanlama icinde kisa uygulanir) — bunlar Standard+ icin

**Cikti:** Tek dosya — `output/{tarih}-{konu}/REPORT.md`

### 2. Standard (~3-4 saat)
**Ne zaman:** "Bu fikri ciddi olarak dusunuyorum"

**Pipeline:**
1. **Girdi analizi + disambiguation** → konu, keyword cluster, hedef kitle. Konu belirsizse → alt segmentleri listele, kullaniciya sor veya her birini ayri analiz et.
   - **Use case segmentasyonu:** Pazarin farkli kullanim senaryolarini (ornk: reconnection, dating safety, tenant screening) tanimla ve her birinin indie uygunlugunu degerlendir.
2. **[PARALEL GRUP A]**
   - App Store tarama (lider + top 10 rakip metadata via WebFetch)
   - Google Trends analizi (WebSearch ile trend yonu + mevsimsellik)
   - Reddit sentiment tarama (min 3 sorgu: sikayet, goc sinyali, alternatif arama)
3. **[PARALEL GRUP B]**
   - Review mining (1-2 yildiz, top 5 rakip icin WebFetch + sikayet tema cikarimi)
   - Gelir kaniti arama (min 4 sorgu: IndieHackers, Twitter #buildinpublic, bloglar, "[app] revenue")
   - Fiyat karsilastirma matrisi (tum rakiplerin fiyat bilgilerini tek tabloda — ortalama, medyan, aralik, lifetime sunan)
   - Reklam istihbarati (FB Ad Library keyword + top rakip advertiser, Google ATC — browser otomasyonu, bkz. kalite kurali #11; longevity, kreatif yogunluk, mesaj acilari)
4. 3 katmanli puanlama (tam versiyon, her puan veri referansli)
   - **Early termination:** K1 KALDI ise → puanlama tamamla ama "ELENDIR (K1 fail)" yaz
   - **Early termination:** K3 < 0.5 ise → raporda notu ekle, MVP detayini kisalt
5. Pazar dogrulama (4 kontrol: rating, indie gelir, goc sinyali, menopoz testi)
6. **Faz 5.5 build-oncesi dogrulama PLANI** — karar GO/SARTLI GO ise ZORUNLU (bkz. `methodology/pre-build-validation.md`): landing/fake-door kopyasi + Mom-Test gorusme kilavuzu + ONCEDEN yazilmis esikler → `06-prebuild-plan.md`. Faz 5.5 insan-aksiyonudur; rapor "Durum: FAZ 5.5 BEKLIYOR" ile biter.
7. → `REPORT.md` + faz ciktilari

**Minimum rakip sayisi:** 10
**Rapor bolumleri:** TUM bolumler (#1-#9, ASO #8 haric) + cross-report karsilastirma (onceki analizler varsa). Karar GO/SARTLI GO ise 5.2 Faz 5.5 plani zorunlu.
**Review mining minimum:** Her rakip icin 10+ kotu yorum, toplam 20+ yorum

**Cikti (ZORUNLU yapi — dosya adlari AYNEN boyle):**
```
output/{tarih}-{konu}/
├── REPORT.md
└── phases/
    ├── 01-market-scan.md          # kanonik Faz 3
    ├── 02-competitor-analysis.md  # kanonik Faz 4 (adim 1-2, 4-8)
    ├── 03-review-mining.md        # kanonik Faz 4 (adim 3)
    ├── 04-scoring.md              # kanonik Faz 5
    ├── 05-validation.md           # kanonik Faz 7
    └── 06-prebuild-plan.md        # kanonik Faz 5.5 — sadece GO/SARTLI GO ise
```
**Not:** `phases/` klasoru Standard modda ZORUNLUDUR. Sadece REPORT.md uretmek yeterli degil. Review mining verisi 02'ye gomulmez; ayri dosya olarak yazilir. "Kanonik Faz" = `methodology/phases.md` numaralandirmasi.

### 3. Deep (~8-12 saat)
**Ne zaman:** "Gelistirmeye baslamadan once her seyi bilmek istiyorum"

**Pipeline:** Standard pipeline (adim 1-6) + asagidakiler:
7. Ozellik karsilastirma matrisi (temel/gelismis/benzersiz/eksik)
8. ASO keyword arastirmasi (6+ sorgu, rakip ASO analizi + reklam kreatif aci analizi [Faz 4 Adim 8 verisinden])
9. Finansal model (3 senaryo: konservatif/realistik/iyimser) — **sablon:** `methodology/financial-model-template.md`
10. Proje brief + MVP scope + Moat analizi (kanonik Faz 9). Faz 5.5 henuz insan tarafindan yurutulmediyse brief DOGRULAMAYA KOSULLU TASLAKTIR — nihai GO karari Faz 5.5 sonucuna baglidir (Durum: FAZ 5.5 BEKLIYOR).
11. Seytan'in avukati (varsayim tablosu, menopoz testi, en kotu senaryolar) (kanonik Faz 10)
12. → `REPORT.md` + tam faz ciktilari. Karar GO ise Sonraki Adimlar'a lansman yonlendirmesi: `methodology/launch-playbook.md`

**Cikti (ZORUNLU yapi — dosya adlari AYNEN boyle):**
```
output/{tarih}-{konu}/
├── REPORT.md
├── phases/
│   ├── 01-market-scan.md … 06-prebuild-plan.md   # Standard ile AYNI (06 sadece GO/SARTLI GO ise)
│   ├── 07-feature-matrix.md
│   ├── 08-aso-research.md
│   ├── 09-financial-model.md      # sablon: financial-model-template.md
│   ├── 10-project-brief.md        # kanonik Faz 9
│   └── 11-devils-advocate.md      # kanonik Faz 10
└── data/
    └── raw-search-results.md
```

---

## Coklu Fikir Karsilastirma

Kullanici birden fazla fikir verirse veya "hangi alanda app yapmaliyim?" derse:

1. Her fikir icin Quick Scan calistir (paralel)
2. Skorlari karsilastir
3. Top 2-3 icin Standard analiz calistir
4. Capraz karsilastirma tablosu olustur
5. Siralama + oneri sun

Bu mod, orijinal 10 fazli pipeline'in tam versiyonunu kullanir.
Detay: `methodology/phases.md`

---

## Kalite Kurallari (ZORUNLU)

### 1. Ucgen Kurali
Hicbir kritik iddia tek kaynaga dayanamaz. Minimum 2 bagimsiz kaynak gerekli.
**Istisna:** App Store'dan direkt okunan veriler (rating, fiyat) tek kaynak yeterli.

### 2. Veri Kalite Etiketleri
Her veri noktasini isaretlemek ZORUNLU:

| Etiket | Anlami | Ornek |
|--------|--------|-------|
| KESIN | Birincil kaynak, direkt gozlem | App Store rating sayisi |
| TAHMINI | 3. parti tahmin/model | Sensor Tower gelir tahmini |
| DUSUK | Cikarim, varsayim | Pazar buyuklugu projeksiyonu |

**Kural:** DUSUK etiketli veriye dayanan puanlar MAX 3 olabilir.

### 3. Override Kurallari
Puanlama sonrasi ZORUNLU kontrol:

| Kosul | Kural |
|-------|-------|
| Lider rating < 500 | Katman 1 FAIL → ELEN |
| Regulasyon engeli indie icin asilmaz | Katman 1 FAIL → ELEN |
| Indie gelir kaniti yok | Gelir puani MAX 2 (B5 istisnasi: Acquire/Flippa/Starter Story komparasyonu ima edilen MRR'a cevrilip ankora eslesirse override kalkar — bkz. scoring-model.md) |
| Top 5 hepsi 4.7+ yildiz | Rekabet puani MAX 2 |
| Apple/Google yerlesik cozum var | Rekabet puani MAX 1 |
| Veri/network/regulasyon moat | Rekabet puanini 1 dusur (moat duzeltmesi) |
| Beyan edilen niyet/iltifat tek delil | O kriter (Talep/Gelir) MAX 3 |
| Rekabet 4-5 ama adlandirilmis icgoru yok | Rekabet puani MAX 3 |
| Keyword difficulty yuksek + wedge yok | Rekabet puani MAX 2 |

**Yetkili kaynak:** Bu tablo OZETTIR. Tam ve yetkili liste (ankorlar, formuller, Dagitim Fizibilitesi dahil): `methodology/scoring-model.md`. Celiski durumunda scoring-model.md esas alinir.

### 4. Menopoz Testi
Pazar raporu buldugunda MUTLAKA uygula:
- Rapor "$X milyar pazar" diyor + lider uygulama < 2K rating → UYARI: Pazar dijitalde yakalanmamis
- Ornek: Menopoz pazari $4.2B tahmini ama lider app sadece 890 rating

### 5. Google Trends Notu
trends.google.com interaktif grafigi WebFetch ile okunamaz. Bunun yerine:
- `WebSearch: "[keyword] app" trend popularity growth 2024 2025 2026` ile dolayli veri topla
- Makale ve raporlardan trend yonu cikar
- Etiket: TAHMINI (dogrudan Trends verisi degil, dolayli cikarim)
- TELAFI (B1): tarayici/insan erisimi varsa Glimpse (Trends'i mutlak hacme cevirir) + Exploding Topics (breakout/buyume %) kullan → Yasam-Dongusu (#10) icin daha guvenilir, KESIN'e yakin etiket. Detay: `methodology/tools-and-data-sources.md` (Bolum 2/5).

### 6. "Bulunamadi" da Veridir
| Bulunamayan | Sonuc |
|-------------|-------|
| Indie gelir kaniti | Gelir puani MAX 2 |
| Reddit tartismasi | Talep puani MAX 3 |
| Google Trends verisi | Trend "belirsiz" |

### 7. Mom Test (Beyan vs Davranis)
Beyan edilen niyet ve iltifat veri DEGILDIR; sadece spesifik gecmis davranis sayilir. "Kullanirim/oderim/iyi fikir" tek basina Talep veya Gelir puanini yukseltemez (o kriter MAX 3). Reddit/review okurken "gercekten yapmis/odemis" sinyalini "isterdim"den ayir. Detay: `methodology/pre-build-validation.md`, red-flags RF-16.

### 8. Adlandirilmis Icgoru + SISP
Yuksek Rekabet (4-5) icin rakiplerin kacirdigi SPESIFIK icgoruyu adlandir; ciplak "bosluk var" yetmez (yoksa MAX 3). Cozum-once secilmis fikir (SISP) bir UYARI'dir. "Rakip yok = pazar yok"un keskin hali: kazanan sinyal = rakipler VAR + adlandirilmis kacirilmis icgoru. Detay: red-flags RF-17.

### 9. Dagitim Fizibilitesi (Kesfedilebilirlik)
Pazar buyuk olsa da app KESFEDILEMEZSE olmaz. Keyword difficulty'yi (0-100) hedef keyword'lerde rank alan top-10 uygulamanin rating sayilarindan tahmin et (paid arac gerekmez). EK VERI (B3): tarayici/insan erisimi varsa SearchAds.com (Mobile Action, ucretsiz plan) Apple popularity'sini yuzeye cikarir → tahmini GUCLENDIRIR (ama Ekim 2025 bozulmasi gecerli, <35 bastiriliyor, tek-kaynak DEGIL). Yuksek difficulty + farklilasma wedge'i yok → Rekabet MAX 2. Detay: `methodology/scoring-model.md` (Dagitim Fizibilitesi).

### 10. Yasam-Dongusu (Zamanlama)
Zamanlama puanindan once trendi siniflandir: Asama (Exploding/Regular/Peaked) + Buyume sekli (Ustel/Sabit/Duragan), mutlak hacimden bagimsiz. PEAKED (zirve yapmis fad) yuksek zamanlama puani ALAMAZ. Etiket TAHMINI.

### 11. Ad Library Notu (Reklam Istihbarati)
FB Ad Library, Google Ads Transparency Center ve TikTok Creative Center WebFetch ile OKUNAMAZ (Trends gibi). Bunun yerine:
- Browser otomasyonu (Claude in Chrome) ile oku → KESIN etiket. Google ATC'de get_page_text bos doner, SCREENSHOT ile oku.
- Browser yoksa WebSearch dolayli → TAHMINI etiket.
- Google ATC SADECE advertiser/domain aramasi yapar (keyword yok). TikTok CC login'siz sinirli onizleme verir.
- Sinyaller: reklam longevity (6+ ay kesintisiz = parasallasma davranis kaniti), aktif kreatif sayisi (paid kanal doygunlugu → dagitim fizibilitesi), mesaj acilari (wedge/ASO girdisi). "Kimse reklam vermiyor" da veridir.
- Harcama TUTARI hicbir kaynakta yok (tahmin = DUSUK). Apple Search Ads kutuphanesi yok = kor nokta, raporda not et.
- Reklam harcamasi indie gelir kaniti DEGILDIR; "indie gelir yok → Gelir MAX 2" kurali degismez.
Detay: `methodology/data-collection-protocol.md` (Faz 4 Adim 8), `methodology/tools-and-data-sources.md` (Bolum 4.5).

### 12. JTBD Forces (Goc Analizi)
Goc sinyalini (Faz 4/7) ham sayma; NEDEN goculdugunu coz: goc ancak Push (mevcuttan iten aci) + Pull (yeniye ceken vaat) > Anxiety (gecis korkusu) + Habit (aliskanlik) ise GERCEK'tir. Aksi halde "fantezi goc" (RF-7). Detay: `methodology/data-collection-protocol.md` (Faz 4 Adim 4 kayit formati).

### 13. Riskiest Assumption Test (RAT) — Faz 5.5
Faz 5.5'te otomatik talebi degil, EN RISKLI varsayimi test et. Varsayimlari (Talep/Odeme/Teknik/Retention/Regulasyon/Dagitim) etki x belirsizlik ile sirala; en riskliyi uygun yontemle (landing/on-satis/spike/concierge/uzman-gorusme/ASO-testi) once dogrula. Cogu tuketici app'inde en riskli = Talep. Detay: `methodology/pre-build-validation.md` (Adim 0).

---

## Dosya Haritasi

### Metodoloji (Bilgi Tabani)
```
methodology/
├── README.md                    # Metodoloji ozeti ve surum bilgisi
├── phases.md                    # 10 faz tanimlari + gate'ler + cikti formatlari
├── scoring-model.md             # 3 katmanli puanlama detayi (ankorlar, formuller)
├── data-collection-protocol.md  # Faz bazli sorgu sablonlari (WebSearch/WebFetch)
├── prompt-templates.md          # Her faz icin hazir prompt'lar
├── tools-and-data-sources.md    # Arac guvenilirlik matrisi + Claude yetenekleri
├── financial-model-template.md  # Bottom-up gelir modeli + benchmark'lar (Deep adim 9 sablonu)
├── launch-playbook.md           # Lansman stratejisi (GO karari SONRASI — rapor Sonraki Adimlar'dan yonlendirilir)
└── patterns/
    ├── red-flags.md             # 17 tehlike isareti (RF-1 … RF-17)
    └── green-flags.md           # 15 basari isareti (GF-1 … GF-15)
```

### Sablonlar
```
templates/
└── report-template.md           # Final rapor formati
```

### Komutlar
```
.claude/commands/                # /quick-scan, /standard, /deep, /compare
```

### Ciktilar
```
output/
├── INDEX.md                     # Scoreboard: tum analizlerin skor/karar/durum ozeti (her rapor sonrasi guncellenir)
└── {YYYY-MM-DD}-{konu}/         # Her arastirma icin ayri klasor
    ├── REPORT.md
    ├── phases/
    └── data/
```

---

## Paralellestirme Stratejisi

Agent tool ile paralel calistirilabilecek arastirma gruplari. Gruplar HARF ile etiketlidir
(yukaridaki mod pipeline adim numaralariyla [1-12] karistirilmamasi icin):

### Quick Scan
```
[SERI]    A. Girdi analizi + disambiguation (konu belirsizse)
[PARALEL] B. App Store lider tespiti | Google Trends kontrol
[SERI]    C. Puanlama (K1 fail → early termination, K3 < 0.5 → kisalt) + Rapor
```

### Standard
```
[SERI]    A. Girdi analizi + disambiguation + use case segmentasyonu
[PARALEL] B. App Store tarama | Google Trends | Reddit sentiment
[PARALEL] C. Review mining | Gelir kaniti | Fiyat matrisi | Reklam istihbarati
[SERI]    D. Puanlama (K1 fail → early termination, K3 < 0.5 → kisalt)
[SERI]    E. Dogrulama + Faz 5.5 plani (GO/SARTLI GO ise) + Rapor + Cross-report + INDEX guncelle
```

### Deep
```
Standard gruplari (A-E) +
[PARALEL] F. Ozellik matrisi | ASO arastirmasi | Finansal model (sablon: financial-model-template.md)
[SERI]    G. Proje brief + MVP + Moat (F'ye bagimli)
[SERI]    H. Seytan'in avukati (tum verilere bagimli)
[SERI]    I. Final rapor + INDEX guncelle (GO ise launch-playbook yonlendirmesi)
```

---

## Teknik Stack Onerileri

Analiz sonucunda MVP onerisi yaparken su default stack'i kullan (kullanici farkli isterse degistir):

| Alan | Oneri | Alternatif |
|------|-------|------------|
| iOS Native | Swift + SwiftUI | — |
| Cross-platform | React Native (Expo) | Flutter |
| State | Zustand | Redux Toolkit |
| Lokal DB | MMKV (basit) / WatermelonDB (karmasik) | Realm |
| Sync | iCloud (CloudKit) | Supabase |
| Auth | Apple Sign In + Email | Firebase Auth |
| Odeme | RevenueCat | StoreKit 2 direkt |
| Analytics | PostHog | Mixpanel |

---

## Onemli Notlar

- **Confirmation bias'tan kacin:** Bir fikri begenmek veri degil. Puanlar objektif ankorlara dayali olmali.
- **Scope creep:** MVP onerisinde max 3-4 ekran, 3 ana ozellik. "V1'de olmayacaklar" listesi zorunlu.
- **Gelir tahminlerinde %50 hata payi:** Sensor Tower (eski data.ai dahil) rakamlari tahmin. Yarilayip hala mantikli mi kontrol et.
- **Survivorship bias:** IndieHackers'ta sadece basarili insanlar paylasim yapar.
- **"Rakip yok" = "Pazar yok":** App Store'da rakip bulamiyorsan, pazar yoktur.
- **Arastirma bitince is bitmez:** GO/SARTLI GO cikan fikir once Faz 5.5 davranis dogrulamasindan gecer (`pre-build-validation.md`); dogrulanan fikir icin lansman plani `launch-playbook.md`'den baslar. Rapor Durum alani (`FAZ 5.5 BEKLIYOR` → `DOGRULANDI`/`TERK`) INDEX.md'de takip edilir.
