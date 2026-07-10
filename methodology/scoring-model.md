# 3 Katmanli Firsat Puanlama Modeli

> App fikirlerini objektif, tekrarlanabilir sekilde degerlendirme sistemi.
> Subjektif yargidan kacinmak icin her puan icin sabit ankor tanimlari kullanilir.

---

## Katman 1: Pazar Gecerliligi (Pass/Fail)

**4 kriter — TUMU GECMELI. Biri fail → ELEN.**

| # | Kriter | Pass Kosulu | Kontrol |
|---|--------|-------------|---------|
| 1 | Pazar var mi? | Lider rating > 500 | App Store'da ana keyword ara |
| 2 | Pazar erisilebilir mi? | Apple/Google yerlesik cozumu tamamen cozmuyor | Health, Reminders, Notes, Calendar, Wallet ile karsilastir |
| 3 | Pazar buyuyor mu? | Yeni uygulamalar cikiyor VE/VEYA trend yukari | Son 1 yil yeni giris + Google Trends |
| 4 | Regulasyon engeli asilabilir mi? | Indie developer hukuk ekibi/ozel lisans olmadan girebilir | FCRA, HIPAA, finans lisansi, veri broker tescili gibi engelleri kontrol et |

**Kriter 4 aciklama:** Bazi pazarlar teknik olarak mumkun ama regulasyon (FTC cezalari, FCRA uyumu, saglik verisi HIPAA, finansal lisans gereksinimleri) indie developer icin asilmaz engel olusturabilir. Bu durumda pazar "erisilemez" kabul edilir.

---

## Katman 2: Firsat Kalitesi (Agirlikli Skor, Max 100)

**Formul:** `Toplam = (Talep × 5) + (Gelir × 5) + (Rekabet × 4) + (Retention × 3) + (Zamanlama × 3)`

### Lider Secim Kurali
Puanlamada kullanilacak "lider", kullanicinin giris yapacagi segmentte ayni kullanim alanini **dogrudan** cozen en buyuk rakiptir.
- Rakip **farkli segmentteyse** (ornk: fintech vs basit tracker, kredi vs borc odeme), niche lideri kullan.
- Rakip **ayni segmentteyse** (ornk: Whitepages de people finder, kullanici da people finder), o rakibi lider kabul et.
- Belirsizse: Kullanici "X app" arattiginda App Store'da ilk cikan ve dogrudan yariscagi uygulamayi sec.

### Talep Sinyali (%25, max 25 puan)

| Skor | Tanim | Objektif Ankor |
|------|-------|----------------|
| 1 | Cok dusuk | Lider < 2K rating, Reddit'te tartisma yok |
| 2 | Sinirli | Lider 2K-10K, sinirli tartisma |
| 3 | Orta | Lider 10K-50K, aktif topluluk |
| 4 | Guclu | Lider 50K-100K, guclu arama hacmi |
| 5 | Cok guclu | Lider 100K+, yaygin goc sinyalleri |

**Ucgen Kurali (Talep):** Lider rating tek basina yeterli degil. Ikinci bir first-party Apple sinyaliyle capraz dogrula: App Store Search Suggest (autocomplete -- kullanicilarin gercekten arattigi terimler) + varsa Apple Search Ads keyword popularity (5-100). Etiket TAHMINI; Ekim 2025'te dusuk-hacim bolgesinde bozuldugu icin tek-kaynak kullanma.

### Gelir Kaniti (%25, max 25 puan)

| Skor | Tanim | Objektif Ankor |
|------|-------|----------------|
| 1 | Yok | Hic indie gelir kaniti yok |
| 2 | Belirsiz | Paid app var ama indie gelir bilinmiyor |
| 3 | Baslangic | 1-2 indie dev $1K-5K/ay |
| 4 | Kanitlanmis | Birden fazla indie dev $5K-20K/ay |
| 5 | Guclu | Birden fazla indie dev $20K+/ay |

**Reklam Longevity Destekleyici Sinyali:** Ad library'de (bkz. `tools-and-data-sources.md` 4.5) 2+ rakibin 6+ aydir kesintisiz donen reklami varsa, bu "pazar parasallasiyor" yonunde DAVRANIS kanitidir (Mom Test uyumlu) — raporda belirt ve Faz 7 gelir dogrulamasini derinlestirme gerekcesi say. Ancak sirket olcegindeki reklam harcamasi INDIE gelir kaniti DEGILDIR: "indie gelir kaniti yok → MAX 2" kurali aynen gecerli kalir; bu sinyal yalnizca 2 puanin guvenini artirir.

**Satin-alma/Exit Komparasyonu Kanit Olarak (B5):** IndieHackers/Twitter survivorship-biaslidir. Acquire.com/Flippa ve Starter Story gelir kanitina KATKI yapabilir — ama once ima edilen aylik gelire cevir VE kanit turunu ayir:
- **Ima edilen aylik gelir = satis fiyati / carpan.** Carpan AYLIK ise dogrudan (or. $48K / 36x aylik kar ≈ $1.3K/ay). Carpan YILLIK ise once 12'ye bol (or. $48K / 3x yillik = $16K/yil ÷ 12 ≈ $1.3K/ay). Carpan gelir mi kar mi oldugunu belirt; KAR carpanindan cikan rakami GELIR ankoruna dogrudan sayma.
- **Kanit turu (Mom Test ile uyumlu):** KAPANMIS satis (gerceklesen islem) = DAVRANIS → ankora gore puanlanabilir. CANLI/satilmamis ILAN (asking price + satici-beyani gelir) = IDDIA → TAHMINI, o kriter MAX 3 (kac ilan olursa olsun; RF-16).
- **Ankor + sayim kapisi:** rakami yukaridaki Gelir Kaniti olcegine gore puanla; olcek bagimsiz-kaynak SAYISINI da sart kosar (skor 4 = 2+ bagimsiz, skor 5 = 3+ bagimsiz). Tek komparasyon bu sayilari yakalamaz.

**Geo-LTV / Ulke Bazli Monetizasyon Sinyali (v3.4):** Hedef ulkelerin LTV/CAC profili Gelir Kaniti puaninin yerine gecmez, ancak gelir ve dagitim guvenini yorumlar.
- RevenueCat/Adapty benchmark'lari veya Apple Search Ads country/bid verisi = TAHMINI; kendi App Store Connect/RevenueCat verin = KESIN.
- Yuksek LTV ulkelerine (dil, ASO, lokalizasyon, odeme, regule olmayan pazar) erisim varsa gelir modelinin guveni artar.
- Hedef geo belirsizse, sadece dusuk-LTV pazarlara yaslaniyorsa veya CAC/LTV dengesi bilinmiyorsa rapora UYARI ekle.
- K2 formulu degismez; Geo-LTV tek basina Gelir puanini artirmaz ve "indie gelir kaniti yok → Gelir MAX 2" override'ini kaldirmaz.

### Rekabet Boslugu (%20, max 20 puan)

| Skor | Tanim | Objektif Ankor |
|------|-------|----------------|
| 1 | Yok | Liderler mukemmel, sikayet minimal |
| 2 | Kucuk | Kucuk kalite farklari, yeterli degil |
| 3 | Belirgin | 1-2 yildiz yorumlarda tekrarlayan UX/fiyat/ozellik temasi |
| 4 | Buyuk | Buyuk sikayet temasi: pahali, karmasik, buggy |
| 5 | Kritik | Lider terk edilmis/cokmus VEYA buyuk bosluk |

**Adlandirilmis Icgoru Kurali (Rekabet 4-5 icin ZORUNLU):** Rekabet 4 veya 5 vermek icin, rakiplerin kacirdigi SPESIFIK icgoruyu (neden onlar yapmamis/yapamamis) tek cumleyle adlandir. Adlandirilamiyorsa -> MAX 3. Ciplak "bosluk var" yetmez. (YC: kazanan sinyal "rakipler var + spesifik kacirilmis icgoru"; "rakip yok" degil. Bkz. red-flags RF-17 SISP.)

**Moat Tipi Duzeltmesi:** Bosluk puanini verdikten sonra, boslugun kaynagini kontrol et:
| Moat Tipi | Aciklama | Etki |
|-----------|----------|------|
| UX/fiyat moat | Sikayet konusu UX, fiyat veya ozellik eksikligi → indie cozebilir | Puan kalir |
| Veri moat | Rakibin avantaji buyuk veri seti veya veri ortakliklari → indie kopyalayamaz | Puani 1 dusur |
| Network moat | Rakibin avantaji kullanici agi → indie kuramaz | Puani 1 dusur |
| Regulasyon moat | Rakibin avantaji lisans/uyum altyapisi → indie karsilayamaz | Puani 1 dusur |

### Retention Potansiyeli (%15, max 15 puan)

| Skor | Tanim | Objektif Ankor |
|------|-------|----------------|
| 1 | Tek kullanimlik | Ayda 1 veya daha az |
| 2 | Aylik | Aylik duzenli kullanim |
| 3 | Haftalik | Haftalik kullanim |
| 4 | Gunluk | Gunluk kullanim |
| 5 | Coklu gunluk | Gunde birden fazla VEYA yillarca devam |

### Zamanlama (%15, max 15 puan)

| Skor | Tanim | Objektif Ankor |
|------|-------|----------------|
| 1 | Durgun | Pazar stabil, degisim yok |
| 2 | Hafif | Yeni girisler var, buyuk degisim yok |
| 3 | Firsat | Bir rakip zayifliyor VEYA yeni trend |
| 4 | Aktif | Buyuk rakip kapandi/zam yapti + aktif goc |
| 5 | Kirilma | Platform/regulasyon degisimi VEYA buyuk cokus |

**Yasam-Dongusu Etiketi (ZORUNLU):** Zamanlama puanindan once trendi siniflandir -- Asama: Exploding / Regular / Peaked; Buyume sekli: Ustel / Sabit / Duragan. Mutlak hacimden bagimsiz olarak degerlendir. PEAKED (zirve yapmis fad) yuksek zamanlama puani ALAMAZ (dusen trende girmek = RF-14). Etiket TAHMINI.

---

## Override Kurallari (ZORUNLU)

Puanlama sonrasi bu kontrolleri MUTLAKA uygula:

| Kosul | Kural | Aciklama |
|-------|-------|----------|
| Lider rating < 2K | UYARI ekle | Mikro pazar — dikkatli ilerle |
| Indie gelir kaniti yok | Gelir MAX 2 | Kimse kazanmiyorsa risk yuksek. ISTISNA (B5): KAPANMIS satis komparasyonu (davranis) ima edilen aylik gelire cevrilip ankora ($1K+/ay) eslesirse override KALKAR. Canli/satilmamis ilan (iddia) = TAHMINI, hala MAX 3. |
| Top 5 hepsi 4.7+ | Rekabet MAX 2 | Memnun kullaniciyi cekmek cok zor |
| Apple/Google yerlesik alternatif | Rekabet MAX 1 | Yerlesik cozumle yarisma zor |
| DUSUK etiketli veri | O kriter MAX 3 | Dusuk guvenilirlik → dusuk puan |
| Tek kaynak (Ucgen Kurali ihlali) | O kriter MAX 3 | Kanitlanmamis → sinirla |
| Beyan edilen niyet/iltifat tek delil | O kriter MAX 3 | "Kullanirim/oderim" davranis degil (Mom Test, RF-16) |
| Yuksek Rekabet ama adlandirilmis icgoru yok | Rekabet MAX 3 | Ciplak bosluk yeterli degil (YC) |
| Hedef keyword'lerde difficulty yuksek + wedge yok | Rekabet MAX 2 | Kesfedilemezsin, top-10'u yenemezsin |

---

## Dagitim Fizibilitesi (Kesfedilebilirlik)

Pazar buyuk olabilir ama yeni app KESFEDILEMEZSE olmaz. Puanlamadan once olc:

- **Keyword Difficulty (0-100):** Hedef keyword'lerde rank alan top-10 uygulamanin rating sayilarindan tahmin et. Top-10 rating'leri yuksek (hepsi 5K+) = difficulty yuksek (zor); dusuk-rating/eski/terk-edilmis uygulamalar = difficulty dusuk (firsat). Public veri, paid arac gerekmez (rating sayilarini zaten topluyoruz).
- **Opportunity (kopyalanabilir formul):** Opportunity = Hacim x0.4 + (100 - Difficulty) x0.3 + Relevance x0.3  (40/30/30 bir konvansiyon, ayarlanabilir).
- **AppFigures kurali:** Sadece top-10'un minimum esigini yakalayip asabilecegin keyword'leri hedefle.
- **Paid Kanal Kontrolu (ad library):** Lider(ler) FB/Google'da yuzlerce aktif kreatif donduruyorsa paid kanal doygundur; indie CAC yarisina giremez → organik/ASO wedge SART (yoksa fizibilite UYARISI). Hicbir rakip reklam vermiyorsa paid UA dogrulanmamis, buyume tamamen organik/ASO'ya bagimli — bunu da fizibilite degerlendirmesine yaz. Etiket: browser ile dogrudan gozlem KESIN, WebSearch dolayli TAHMINI. (Veri: Faz 4 Adim 8)
- **Geo-LTV Fit:** Hedef keyword/kanal secimi ulke bazli LTV ile uyumlu mu? Yuksek LTV ulkelerinde rank sansi veya paid CAC makul degilse, pazar buyuk olsa bile Dagitim Fizibilitesi UYARISI ekle. Baslangicta 3-5 ulke sec; 80+ ulkeye yayilma varsayimi first-party LTV:CAC verisi olmadan kullanilmaz.

**Puanlamaya etkisi:** Yuksek difficulty + farklilasma wedge'i yok -> Rekabet MAX 2 (yukaridaki override). En az 3 orta-hacim/dusuk-difficulty keyword'de rank sansi yoksa -> fizibilite UYARISI ekle. Etiket: TAHMINI.

---

## Katman 3: Fizibilite Carpani (0.1296 — 1.0)

| Kriter | 1.0 (En iyi) | 0.8 (Orta) | 0.6 (Zor) |
|--------|-------------|------------|-----------|
| Teknik Zorluk | Basit (CRUD, bildirim, liste) | Orta (API, grafik, sync) | Zor (ML, real-time, hardware) |
| Kurucu-Pazar Uyumu | Problemi kendin yasiyorsun | Ilgi var, bilgi sinirli | Ne ilgi ne bilgi |
| Regulasyon/Uyum Bilgisi | Regulasyon yok veya basit (App Store kurallari) | Orta regulasyon var, ogrenebilir (KVKK, temel gizlilik) | Agir regulasyon, uzman/avukat SART (FCRA, HIPAA, finans lisansi) |
| MVP Suresi | < 4 hafta | 4-8 hafta | 8+ hafta |

**Carpan = Teknik × Kurucu × Regulasyon × MVP**

> **Not:** Regulasyon 1.0 ise (engel yok), carpan onceki gibi 3 faktorlu kalir. Sadece regulasyon engeli olan pazarlarda 4. faktor devreye girer.
> **v3.4 Notu:** 1 haftalik micro-MVP sprint, Faz 5.5 sonrasi uygulama planidir; K3 MVP suresi ankori degismez. Sprint yalnizca basit, dogrulanmis, max 4 core ekran + gerekiyorsa 1 paywall/upgrade ekranlik app'ler icin onerilir.

---

## Final Skor

**Final Skor = Katman 2 Toplam × Katman 3 Carpan**

| Final Skor | Anlami | Aksiyon |
|-----------|--------|---------|
| 60+ | Guclu firsat | Hemen ilerle |
| 45-59 | Orta firsat | Ek dogrulama gerek |
| 30-44 | Zayif firsat | Sadece diger secenekler daha zayifsa |
| < 30 | Elendir | Devam etme |

---

## Ornek Hesaplamalar

```
Debt Payoff Planlayici:
  K1: Pazar var (6.9K ✓), erisilebilir (Apple borc app yok ✓), buyuyor (Trends UP ✓),
      regulasyon asilabilir (ozel lisans gerekmiyor ✓) → GECTI
  K2: Talep 3(15) + Gelir 3(15) + Rekabet 4(16) + Retention 3(9) + Zamanlama 3(9) = 64
      Override: Gelir kaniti DOGRULANAMADI → Gelir max 3 ✓ (zaten 3)
  K3: Teknik 1.0 × Kurucu 0.8 × Regulasyon 1.0 × MVP 1.0 = 0.80
  Final: 64 × 0.80 = 51.2 → Orta firsat, ek dogrulama gerek

People Finder:
  K1: Pazar var (162K ✓), erisilebilir (Apple Find My farkli ✓), buyuyor (AI girisler ✓),
      regulasyon asilabilir? → KALDI ⚠️ (FCRA, FTC cezalari, veri broker tescili gerekli)
  K2: Talep 5(25) + Gelir 2(10) + Rekabet 3→2*(12→8) + Retention 1(3) + Zamanlama 3(9) = 55
      Override: Indie gelir yok → Gelir max 2 ✓
      *Rekabet: 3 puan (7 sikayet temasi) ama veri moat → 1 dusur → 2
  K3: Teknik 0.8 × Kurucu 0.8 × Regulasyon 0.6 × MVP 0.8 = 0.3072
  Final: 55 × 0.307 = 16.9 → Elendir (K1 zaten KALDI)
```
