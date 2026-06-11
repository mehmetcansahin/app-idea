# Build-Oncesi Talep Dogrulama (Faz 5.5)

> Puanlama (Faz 5) ile Proje Brief/MVP (Faz 9) ARASINA giren opsiyonel-ama-onerilen ara faz.
> Amac: Kod yazmadan once "bu seyi gercekten isteyen var mi" sorusunu DAVRANISLA test etmek.
> Bu faz INSAN tarafindan yurutulur; Claude landing-page metnini, reklam kopyasini ve
> gorusme kilavuzunu yazar, sonuclari analiz eder. Mod sure butcelerinden (Claude arastirma
> suresi) ayridir -- bu, kurucunun harcadigi saattir.

## Neden var?

Mevcut pipeline puanlamadan dogrudan MVP'ye atliyordu. Skor "pazar var + rakipte bosluk var"
diyebilir ama bu, BU kullanicilarin BU cozumu isteyecegi anlamina gelmez. Build-oncesi
dogrulama, en pahali hatayi (yanlis seyi insa etmek) ucuza eler.

---

## 2 / 20 / 200 Merdiveni (Rob Walling)

Her fikir bir sonraki basamaga gecmeden once esigi gecmeli. Her basamak bir GUVEN YUZDESI verir.

| Basamak | Sure | Ne yapilir | Cikti |
|---------|------|------------|-------|
| **2 saat** | ~2 sa | Rakip fikirler arasi hizli eleme (zaten Faz 1-5 bunu yapiyor) | En umutlu 1-2 fikir + baslangic guven %'si |
| **20 saat** | ~20 sa | **Build-oncesi TALEP testi**: landing page / fake-door + 5-10 Mom-Test gorusmesi | Davranis-bazli go/no-go + guncellenmis guven % |
| **200 saat** | ~200 sa | MVP insasi (= Faz 9 + gelistirme) | Calisan MVP, ilk kullanicilar |

**Bizde eksik olan 20-saat basamagiydi.** Bu dosya onu tanimlar.

### Guven Yuzdesi (mod basina alan)

Her fazda kararina bir guven % ata ve raporda goster:
- Faz 5 sonrasi (sadece masa-basi arastirma): tipik %30-50
- Faz 5.5 sonrasi (davranis sinyali eklendi): GO icin >=%70 hedefle
- 200h MVP sonrasi (gercek kullanim): gercek retention/donusum verisi

---

## 20-Saat Basamak: Iki Paralel Test

### A) Landing Page / Fake-Door Testi

Kod yok; sadece bir sayfa + net deger onerisi + tek CTA (ornk "Erken erisim al" / "Beni
haberdar et" / sahte "Satin al" butonu -> "yakinda" + email).

- **Kur:** Carrd/GitHub Pages (ucretsiz). Claude basligi, alt basligi, 3 fayda maddesini ve
  CTA metnini yazar (Faz 9 ASO/konumlandirma taslagindan turetir).
- **Trafik:** Faz 4'te bulunan watering-hole'lara (Sales Safari, bkz. data-collection Kural 7)
  organik paylasim VEYA kucuk ($20-50) Apple Search Ads/Reddit reklami.
- **Sinyal:** Ziyaretci -> CTA tiklama / email birakma orani.
- **KRITIK kural:** Esigi ONCEDEN yaz (pre-registration). "Su trafik kaynagindan gelen
  X ziyaretcinin %Y'si email birakirsa GO." Sonradan esik kaydirma = kendini kandirma.
  Orani trafik kaynaginin kalitesine gore yorumla (yuksek-intent ASA != soguk reklam).
- **UYARI (Mom Test):** Email birakmak bile "beyan edilen niyet"e yakindir; gercek davranis
  > tiklama > email > sadece "begendim" yorumu. Mumkunse kucuk bir on-odeme/rezervasyon iste.

### B) Mom-Test Gorusmeleri (5-10 kisi)

Hedef kullaniciyla konus. Amac fikrini SATMAK degil, gecmis davranisi OGRENMEK.

**Mom Test kurallari (Rob Fitzpatrick):**
1. Fikrinden degil, onlarin HAYATINDAN ve GECMISINDEN konus.
2. Gelecek/hipotez ("kullanir miydin") degil, somut gecmis ("son kez ne zaman bu problemi
   yasadin, ne yaptin, ne kadar surdu/ne odedin") sor.
3. Iltifati ve "harika fikir"i VERI sayma -- bunlar bedava.
4. Genel ("genelde") degil, spesifik ("o gun tam olarak") cevap kovala.

**Iyi vs kotu veri:**
| Iyi (davranis) | Kotu (beyan/hipotez) |
|----------------|----------------------|
| "Gecen ay bunun icin X'e $20 odedim" | "Boyle bir sey olsa oderim" |
| "Su an 3 farkli app + Excel kullaniyorum" | "Bu cok ise yarar gibi" |
| "Bu yuzden tatilde 2 saat kaybettim" | "Iyi fikir, basarili olur" |

**Soru sablonu (Claude uretir, kurucu uyarlar):**
- "Bana son kez [problem] yasadigin ani anlat. Ne yaptin?"
- "Su an bunu nasil cozuyorsun? Hangi araclar/yontemler?"
- "Bu cozumde en sinir bozucu sey ne? En son ne zaman oldu?"
- "Bunu cozmek icin daha once para/zaman harcadin mi? Ne kadar?"
- (ASLA: "Boyle bir app'i kullanir miydin / oder miydin?")

---

## Puanlamaya Geri Besleme

Faz 5.5 sonuclari Faz 5 puanini DUZELTEBILIR (ve override tetikler):
- Landing/gorusme sadece "begendim/kullanirim" uretti, davranis sinyali yok
  -> Talep ve Gelir icin **beyan-niyet override**'i (o kriter MAX 3, RF-16).
- Gercek davranis sinyali (on-odeme, mevcut araca para harcama, aktif cozum arayisi)
  -> Talep/Gelir delili GUCLENIR (KESIN/TAHMINI etiketiyle).
- Hicbir watering-hole'da problem dogrulanamadi -> SISP suphesi (RF-17), Faz 8'e geri don.

---

## Cikti Formati

```
=== Faz 5.5 Build-Oncesi Dogrulama: [FIKIR] ===
Baslangic guven (Faz 5 sonrasi): %__

A) Landing page:
   Trafik kaynagi: ___ | Ziyaretci: ___ | CTA/email orani: __% | Onceden yazilan esik: __%
   Sonuc: ESIK GECTI / KALDI

B) Gorusmeler (n=__):
   Davranis sinyali bulunan: __/__ (gecmis para/zaman harcamasi)
   Sadece beyan/iltifat: __/__
   En guclu somut alinti: "___"

Guncellenmis guven: %__
KARAR: GO (>=%70) / DEVAM ET-DOGRULA / PIVOT / KILL
Puanlama duzeltmesi: [varsa override + yeni K2]
```

**Mod entegrasyonu:** Quick Scan'de opsiyonel (sadece SARTLI GO cikarsa onerilir);
Standard ve Deep'te GO adaylari icin ZORUNLU adim.
