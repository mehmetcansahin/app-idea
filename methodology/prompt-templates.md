# App Fikri Arastirma Prompt Sablonlari

Bu dosya, bir app fikrini sistematik olarak arastirmak icin 10 fazlik prompt sablonlarini icerir.

## Nasil Kullanilir

- Her fazin prompt'u copy-paste hazir sekilde asagida yer aliyor
- `[DEGISKEN]` ile isaretlenen yerleri kendi bilgilerinle degistir
- Her prompt'un sonunda beklenen cikti formati ve GATE (gecis kosulu) var
- Fazlar sirasiyla calistirilmali — bir fazin GATE'ini gecemezsen bir onceki faza donup iyilestirme yap
- Her fazin ciktisini bir yere kaydet, sonraki fazlarda girdi olarak kullanacaksin

---

## FAZ 1: Problem Havuzu

**Amac:** Secilen alanda mobilde cozulmeye deger 20-30 somut problem belirlemek.

**Prompt:**

```
[ALAN] kategorisinde iOS App Store icin 20-30 somut, aci veren problem alani belirle.

Kurallar:
- Sadece mobilde cozulmesi mantikli problemler
- Tek kullanimlik degil, tekrarlayan kullanim gerektiren
- Odeme niyeti olan kullanici segmentlerine yonel
- Her problem icin su formati kullan:

### Problem #X: [Baslik]
- Kullanici kim:
- Ne sorunu var:
- Telefonda cozmek mantikli mi: Evet/Hayir - neden
- Sik tekrar ediyor mu: Evet/Hayir - sikligi
- Para verir mi: Evet/Hayir - neden

Odaklanilacak yuksek odeme niyetli alanlar: saglik, para yonetimi, zaman yonetimi, is verimliligi, ebeveynlik, profesyonel kullanim.

Eleme: Mobilde mantikli degil, tek kullanimlik, kullanici odemez, cok genis/genel alan → listeye alma.

GATE: Minimum 15 problem, en az 3 farkli kategori olmali.
```

---

## FAZ 2: Keyword Cluster'lar

**Amac:** Her problem icin App Store'da aranabilir keyword kumeleri olusturmak.

**Prompt:**

```
Asagidaki problem listesi icin her bir probleme 10-20 keyword'luk kume olustur.

5 keyword tipi kullan:
1. Ana keyword — kullanicinin direkt arayacagi
2. Hedef kitle odakli — "[arac] for [kitle]"
3. Sonuc odakli — "[eylem] [sonuc]"
4. Alternatif ifade — ayni seyi farkli kelimelerle
5. Uzun kuyruklu — spesifik, dusuk rekabet

Her keyword icin tahmini rekabet seviyesi ekle (Dusuk/Orta/Yuksek).

Cikti formati:
### Problem: [Baslik]
| Tip | Keyword | Tahmini Rekabet |
|-----|---------|-----------------|
| Ana | ... | Dusuk/Orta/Yuksek |
| Hedef kitle | ... | Dusuk/Orta/Yuksek |
| Sonuc | ... | Dusuk/Orta/Yuksek |
| Alternatif | ... | Dusuk/Orta/Yuksek |
| Uzun kuyruk | ... | Dusuk/Orta/Yuksek |

Problemler:
[PROBLEM LISTESINI BURAYA YAPISTIR]

GATE: Her problem icin minimum 10 keyword olmali.
```

---

## FAZ 3: Hizli Pazar Tarama

**Amac:** Keyword cluster'larin gercek App Store verileriyle pazar buyuklugunu dogrulamak.

**Prompt:**

```
Asagidaki keyword cluster'lari icin App Store'da hizli bir pazar taramasi yap.

Her cluster icin:
1. Ana keyword'u App Store'da ara
2. Ilk siradaki (lider) uygulamayi bul
3. iOS rating sayisini, yildiz puanini, fiyat modelini kaydet

Pazar durumu kriterleri:
- Rating > 10K = Guclu pazar
- Rating 2K-10K = Orta pazar
- Rating 500-2K = Mikro pazar (dikkat)
- Rating < 500 = Pazar yok (ELEN)

Cikti formati:
| # | Cluster | Lider Uygulama | iOS Rating | Yildiz | Fiyat | Pazar Durumu |
|---|---------|----------------|------------|--------|-------|--------------|
| 1 | ... | ... | ... | ... | ... | Guclu/Orta/Mikro/Yok |

Sonunda ozet: Kac cluster gecti, kac elendi.

Keyword cluster'lari:
[CLUSTER LISTESINI YAPISTIR]

GATE: En az 8 cluster "pazar var" (Guclu veya Orta) olmali.
```

---

## FAZ 4: Rakip Analizi

**Amac:** Gecen cluster'lardaki rakipleri derinlemesine inceleyip firsat bosluklarini bulmak.

**Prompt:**

```
Hizli pazar taramasini gecen asagidaki keyword cluster'lari icin detayli rakip analizi yap.

Her cluster icin:
1. App Store'da ilk 5-10 sonucu incele
2. Her rakip icin: isim, iOS rating, yildiz, fiyat modeli, son guncelleme tarihi
3. 1-2 yildiz review'larda en sik tekrarlanan 3 sikayeti bul
4. Rekabet durumunu degerlendir
5. Reklam istihbarati: FB Ad Library'de keyword + top 3 rakibi ara (browser otomasyonu, WebFetch calismaz)
   — aktif reklam sayisi, en eski reklamin baslama tarihi (longevity), mesaj acilari

Cikti formati (her cluster icin):

### Cluster: [Baslik]

| Rakip | iOS Rating | Yildiz | Fiyat | Model | Son Guncelleme |
|-------|------------|--------|-------|-------|----------------|
| ... | ... | ... | ... | Freemium/Abonelik/Tek seferlik | ... |

**1-2 Yildiz Review Analizi:**
- En sik sikayet 1: [sikayet] (tekrar sayisi/orani)
- En sik sikayet 2: [sikayet]
- En sik sikayet 3: [sikayet]

**Firsat Degerlendirmesi:**
- Guclu markalar var mi: Evet/Hayir
- UX kalitesi: Dusuk/Orta/Yuksek
- Fiyat boslugu var mi: Evet/Hayir - aciklama
- Giris firsati: Var/Yok - neden
- A6 (2x2 konumlandirma, DEEP): kullanici-degeri 2 ekseni + rakip yerlesimi + bos pozisyon/wedge
- A3 (JTBD Forces): goc Push+Pull vs Anxiety+Habit — goc gercek mi fantezi mi (RF-7)

**Reklam Istihbarati:**
- Reklam veren rakip sayisi: [N] / [toplam rakip]
- En uzun donen reklam: [rakip] - [baslama tarihi] ([X ay])
- Kullanilmayan mesaj acisi (wedge adayi): [aci]
- Paid kanal durumu: DOYGUN / AKTIF / BOS
- Erisim yolu: BROWSER (KESIN) / WEBSEARCH-FALLBACK (TAHMINI)

Gecen cluster'lar:
[CLUSTER LISTESINI YAPISTIR]

GATE: Her cluster icin en az 5 rakip analiz edilmis olmali.
```

---

## FAZ 5: Firsat Puanlama (3 Katmanli Model)

**Amac:** Kalan fikirleri 3 katmanli modelle degerlendirmek: Pass/Fail → Agirlikli Skor → Fizibilite Carpani.

> **Yetkili kaynak:** Puanlama detaylari (ankorlar, override kurallari, K1/K3 formulleri) icin tek gecerli kaynak `scoring-model.md`'dir. Celiski durumunda `scoring-model.md` esas alinir.

**Prompt:**

```
Asagidaki cluster'lar icin 3 KATMANLI firsat puanlamasi yap.

=== KATMAN 1: PAZAR GECERLILIGI (Pass/Fail) ===

4 kriter — TUMU GECMELI. Biri bile basarisiz → ELENDIR, Katman 2'ye tasima.

| Kriter | Pass Kosulu |
|--------|-------------|
| 1. Pazar var mi? | Lider rating > 500 |
| 2. Pazar erisilebilir mi? | Apple/Google yerlesik cozumu bu isi tamamen cozmuyor (Health, Reminders, Notes, Calendar, Clock, Wallet ile karsilastir) |
| 3. Pazar buyuyor mu? | Son 1 yilda yeni girisler var VE/VEYA Google Trends yukseliste |
| 4. Regulasyon asilabilir mi? | Indie developer hukuk ekibi/ozel lisans olmadan girebilir (FCRA, HIPAA, finans lisansi, veri broker tescili gibi asilmaz engel yoksa GECTI) |

Cikti:
| # | Cluster | Lider > 500? | Apple/Google engeli yok mu? | Buyuyor mu? | Regulasyon asilabilir mi? | Sonuc |
|---|---------|--------------|----------------------------|-------------|---------------------------|-------|
| 1 | ... | ... | ... | ... | ... | GECTI / ELENDI |

=== KATMAN 2: FIRSAT KALITESI (Agirlikli Skor, Max 100) ===

Sadece Katman 1'i gecenler icin. 5 kriter, her biri 1-5:

Formul: Toplam = (Talep x 5) + (Gelir x 5) + (Rekabet x 4) + (Retention x 3) + (Zamanlama x 3)

OBJEKTIF ANKORLAR:

Talep Sinyali (%25):
1=Lider < 2K rating, Reddit'te tartisma yok | 2=Lider 2K-10K, sinirli tartisma | 3=Lider 10K-50K, aktif topluluk | 4=Lider 50K-100K, guclu arama hacmi | 5=Lider 100K+, yaygin goc sinyalleri

Gelir Kaniti (%25):
1=Hic indie gelir kaniti yok | 2=Paid uygulamalar var ama indie gelir bilinmiyor | 3=1-2 indie dev $1K-5K/ay | 4=Birden fazla indie dev $5K-20K/ay | 5=Birden fazla indie dev $20K+/ay

Rekabet Boslugu (%20):
1=Liderler mukemmel, sikayet yok | 2=Kucuk kalite farklari, yeterli degil | 3=Belirgin UX/fiyat/ozellik boslugu (1-2 yildiz yorumlarinda tekrarlayan tema) | 4=Buyuk sikayet temasi (too expensive, too complex, buggy) | 5=Lider terk edilmis VEYA buyuk fiyat/ozellik boslugu

Retention Potansiyeli (%15):
1=Tek kullanimlik | 2=Aylik | 3=Haftalik | 4=Gunluk | 5=Gunde birden fazla VEYA yillarca surecek

Zamanlama (%15):
1=Durgun pazar, degisim yok | 2=Yeni girisler var ama buyuk degisim yok | 3=Bir rakip zayifliyor VEYA yeni trend | 4=Buyuk rakip kapandi/zam yapti + aktif goc | 5=Platform degisimi VEYA regulasyon degisimi VEYA buyuk cokus

ZORUNLU OVERRIDE KURALLARI:
- Lider rating < 2K → UYARI: "Mikro pazar — dikkatli ilerle"
- Indie gelir kaniti yoksa → Gelir Kaniti skoru MAX 2 (B5 istisnasi: Acquire/Flippa/Starter Story komparasyonu ima edilen MRR'a [satis fiyati / carpan] cevrilip ankora eslesirse override kalkar; tek/zayif komparasyon hala MAX 3)
- Top 5 hepsi 4.7+ yildiz → Rekabet Boslugu skoru MAX 2
- Apple/Google yerlesik alternatifi varsa → Rekabet Boslugu skoru MAX 1
- DUSUK etiketli veriye dayanan kriter → O kriter skoru MAX 3
- Tek kaynak (Ucgen Kurali ihlali) → O kriter skoru MAX 3
- Moat duzeltmesi: Rekabet boslugu puanini verdikten sonra, bosluk veri/network/regulasyon moat'undan kaynaklaniyorsa → Rekabet puanini 1 dusur (UX/fiyat moat ise puan kalir)
- Beyan edilen niyet/iltifat tek delil → O kriter (Talep/Gelir) MAX 3 (Mom Test, RF-16)
- Rekabet 4-5 ama adlandirilmis kacirilmis icgoru yok → Rekabet MAX 3
- Hedef keyword'lerde difficulty yuksek + farklilasma wedge'i yok → Rekabet MAX 2 (Dagitim fizibilitesi)

Cikti:
| # | Cluster | Talep (x5) | Gelir (x5) | Rekabet (x4) | Retention (x3) | Zamanlama (x3) | Toplam (/100) |
|---|---------|-----------|-----------|-------------|---------------|---------------|--------------|
| 1 | ... | X (XX) | X (XX) | X (XX) | X (XX) | X (XX) | XX |

=== KATMAN 3: UYGULAMA FIZIBILITESI (Carpan) ===

Her cluster icin 4 carpan, her biri 0.6 / 0.8 / 1.0:

Teknik Zorluk:
1.0=Basit (CRUD, bildirim, liste) | 0.8=Orta (API entegrasyon, grafik, sync) | 0.6=Zor (ML, real-time, hardware)

Kurucu-Pazar Uyumu:
1.0=Alan bilgisi + ilgi var (problemi kendin yasiyorsun) | 0.8=Ilgi var, alan bilgisi sinirli | 0.6=Ne ilgi ne bilgi

Regulasyon/Uyum:
1.0=Regulasyon yok veya basit (App Store kurallari) | 0.8=Orta regulasyon, ogrenilebilir (KVKK, temel gizlilik) | 0.6=Agir regulasyon, uzman/avukat sart (FCRA, HIPAA, finans lisansi)

MVP Suresi:
1.0=< 4 hafta | 0.8=4-8 hafta | 0.6=8+ hafta

Carpan = Teknik x Kurucu x Regulasyon x MVP
(Not: Regulasyon 1.0 ise carpan pratikte 3 faktorlu kalir; sadece regulasyon engeli olan pazarlarda 4. faktor devreye girer.)

=== FINAL SKOR ===

Final Skor = Katman 2 Toplam x Katman 3 Carpan

| Final Skor | Anlami | Aksiyon |
|-----------|--------|---------|
| 60+ | Guclu firsat | Hemen Faz 6'ya tasi |
| 45-59 | Orta firsat | Ek dogrulama gerek |
| 30-44 | Zayif firsat | Sadece diger firsatlar daha zayifsa devam et |
| < 30 | Elendir | Bu fikirle devam etme |

Cikti:
| # | Cluster | Katman 2 | Teknik | Kurucu | Regulasyon | MVP | Carpan | Final Skor | Durum |
|---|---------|---------|--------|--------|------------|-----|--------|-----------|-------|
| 1 | ... | XX | X | X | X | X | X.XX | XX.X | Guclu/Orta/Zayif/Elen |

Her Final Skor 45+ olan cluster icin kisa aciklama (2-3 cumle).

Cluster verileri:
[FAZ 3-4 VERILERINI YAPISTIR]

GATE: En az 3 cluster'in Final Skoru 45+ olmali.
```

---

## FAZ 5.5: Build-Oncesi Talep Dogrulama

**Amac:** GO adayini kod yazmadan, davranisla dogrulamak. Detay: `pre-build-validation.md`.

**Prompt (Claude assetleri uretir, kurucu yurutur):**

```
[FIKIR] icin build-oncesi dogrulama paketi uret:

0. EN RISKLI VARSAYIM (RAT): Varsayimlari (Talep/Odeme/Teknik/Retention/Regulasyon/Dagitim) etki x belirsizlik ile sirala. EN riskliyi sec ve testi ona gore belirle (Talep→landing+gorusme; Odeme→on-satis; Teknik→spike; Retention→concierge; Regulasyon→uzman gorusme; Dagitim→ASO testi). Cogu tuketici app'inde Talep'tir; asagidaki paket o durum icindir.
1. LANDING PAGE METNI (fake-door): baslik (<=10 kelime), alt baslik, 3 FAYDA maddesi, tek CTA. Konumlandirma Faz 9 taslagindan tureyecek. Ozellik degil fayda yaz.
2. ONCEDEN-YAZILAN ESIK: "Su trafik kaynagindan X ziyaretcinin %Y'si email/CTA birakirsa GO." (Esik sonradan DEGISTIRILEMEZ — pre-registration.)
3. MOM-TEST GORUSME KILAVUZU: 5-7 soru, HEPSI gecmis davranis odakli ("son kez ne zaman... ne yaptin... ne odedin"). Fikri sunan/hipotetik soru ("kullanir miydin") YASAK.
4. WATERING-HOLE LISTESI: Faz 4 Sales Safari'den — landing trafigi + gorusme katilimcisi nereden bulunacak.

Sonra sonuclari degerlendir:
- Gercek davranis sinyali (on-odeme, mevcut araca harcama, aktif cozum arayisi) → delil GUCLENIR (KESIN/TAHMINI)
- Sadece "kullanirim/begendim" → Talep/Gelir MAX 3 (RF-16)
- Problem hicbir watering-hole'da dogrulanamadi → SISP (RF-17)
- Guven %'sini guncelle.
```

GATE: GO icin guven >=%70 VE en az 1 gercek davranis sinyali.

---

## FAZ 6: En Iyi 5 Secim

**Amac:** Kalan fikirleri 4 pratik filtreden gecirerek en iyi 5'i secmek.

**Prompt:**

```
Asagidaki puanlanmis fikirler arasinden en iyi 5'i sec.

4 FILTRE (hepsini gecmeli):
1. Tek cumlede anlatilabilir mi?
2. MVP ilk versiyonu 2-4 haftada yapilabilir mi?
3. Rakipten farki tek cumlede soylenebilir mi?
4. Ucretli modele (abonelik/premium) baglanabilir mi?

Her fikir icin 4 filtreyi uygula ve sonucu goster:

| # | Fikir | F1 Anlatim | F2 MVP | F3 Fark | F4 Odeme | Gecti? |
|---|-------|------------|--------|---------|----------|--------|
| 1 | ... | Evet/Hayir | Evet/Hayir | Evet/Hayir | Evet/Hayir | EVET/HAYIR |

Gecen fikirleri Final Skor (3 katmanli puanlama sonucu) sirasina gore sirala.

Her gecen fikir icin:
- Tek cumle tanim:
- MVP'de olacak 3 ana ozellik:
- Rakipten fark cumlesi:
- Onerilen fiyat modeli:

Puanlanmis fikirler:
[FAZ 5 SONUCLARINI YAPISTIR]

GATE: En az 3 fikir 4 filtrenin hepsini gecmeli.
```

---

## FAZ 7: Pazar Dogrulama

**Amac:** En iyi 5 fikri gercek verilerle dogrulamak, hayali pazarlardan kacmak.

**Prompt:**

```
Asagidaki en iyi 5 fikir icin GERCEK VERI ile pazar dogrulamasi yap.

Her fikir icin 4 dogrulama kontrolu:

1. GERCEK RATING KONTROLU
   - Lider uygulamanin APP STORE'daki gercek iOS rating sayisini bul
   - Rating > 10K = Guclu, 2-10K = Orta, <2K = Zayif

2. INDIE GELIR KANITI
   - IndieHackers, Reddit, Twitter #buildinpublic'te bu kategoride indie dev'in gelir paylasimi var mi?
   - Var → ne kadar? Yok → "Kanitlanamamis"
   - B5: Acquire.com/Flippa ilani veya Starter Story medyani da ara. Varsa ima edilen MRR = satis fiyati / carpan; ankora (>=$1K/ay) eslesirse "Gelir MAX 2" override kalkar (survivorship'i dengeler).

3. KULLANICI GOC SINYALI
   - Reddit'te "[lider uygulama] alternative", "leaving [uygulama]" gibi tartismalar var mi?
   - Lider uygulamada fiyat artisi/kalite dususu var mi?
   - A3 (JTBD Forces): goc NEDEN oluyor? Push (iten aci) + Pull (ceken vaat) > Anxiety (gecis korkusu) + Habit (aliskanlik) ise GERCEK; degilse fantezi goc (RF-7).

4. PAZAR RAPORU vs GERCEK
   - Pazar buyuklugu raporlari ne diyor?
   - Bu rakamlar App Store rating sayilariyla uyusuyor mu?
   - MENOPOZ TESTI: Rapor milyarlarca diyorsa ama lider uygulama 890 rating ise → UYARI

Cikti formati (her fikir icin):

### [Fikir Adi] — Dogrulama

| Kontrol | Kaynak | Sonuc | Guvenilirlik |
|---------|--------|-------|--------------|
| Lider rating | App Store | [sayi] | Guclu/Orta/Zayif |
| Indie gelir | [kaynak] | [miktar veya "yok"] | Guclu/Orta/Zayif |
| Kullanici gocu | Reddit | [var/yok, detay] | Guclu/Orta/Zayif |
| Pazar raporu vs gercek | [kaynak] | [uyumlu/uyumsuz] | Guclu/Orta/Zayif |

**Dogrulama Sonucu:** GECTI / KALDI / BELIRSIZ

Sonunda ozet: Kac fikir gecti, kac kaldi.

En iyi 5 fikir:
[FAZ 6 SONUCLARINI YAPISTIR]

GATE: En az 2 fikir GECTI almali.
```

---

## FAZ 8: Capraz Kategori Karsilastirma

**Amac:** Dogrulanan fikirler arasinda net bir kazanan belirlemek.

**Prompt:**

```
Dogrulamayi gecen fikirler arasinda capraz karsilastirma yap.

Oncelik sirasi (en onemliden en az onemliye):
1. Kanitlanmis Talep (lider rating sayisi)
2. Indie Gelir Kaniti (gercek rakamlar)
3. Final Skor (3 katmanli puanlama)
4. MVP Kolayligi (teknik zorluk)
5. Kullanici Edinme Maliyeti (CPA)

Cikti formati:

| Kriter | [Fikir A] | [Fikir B] | [Fikir C] |
|--------|-----------|-----------|-----------|
| Lider Rating | ... | ... | ... |
| Indie Gelir Kaniti | ... | ... | ... |
| Final Skor (Faz 5) | ... | ... | ... |
| MVP Kolayligi | Kolay/Orta/Zor | ... | ... |
| Tahmini CPA | ... | ... | ... |
| Risk Seviyesi | Dusuk/Orta/Yuksek | ... | ... |
| Ozel Avantaj | ... | ... | ... |
| **SIRALAMA** | **#?** | **#?** | **#?** |

Siralamanin gerekce aciklamasi (3-5 cumle).

Dogrulanan fikirler:
[FAZ 7 SONUCLARINI YAPISTIR]

GATE: Net #1 kazanan veya max 2 finalist olmali.
```

---

## FAZ 9: Proje Brief + MVP Scope + Moat Analizi

**Amac:** Kazanan fikir icin detayli proje dokumani, MVP kapsamini ve moat (savunulabilirlik) analizini olusturmak.

**Prompt:**

```
[FIKIR ADI] icin detayli proje brief'i, MVP scope'u ve moat analizi olustur.

## Proje Brief

**Uygulama adi fikri:**
**Tek cumle tanim:**
**Ana keyword:**
**Destek keyword'ler:**
**Hedef kullanici:**
**Ana problem:**
**Mevcut alternatifler:**
**Rakiplerdeki eksikler:**
**Benim farkim (tek cumle):**
**Neden simdi?**
**Final Skor (3 katmanli):**

## Lean Canvas (1 sayfa, 9 blok)
| Blok | Icerik |
|------|--------|
| Problem (top 3) | ... |
| Musteri Segmenti | ... |
| UVP (essiz deger onerisi) | ... |
| Cozum (top 3 ozellik) | ... |
| Kanallar | ... (ASO/Reddit/PH/SEO) |
| Gelir Akisi | ... (fiyat modeli) |
| Maliyet Yapisi | ... (Apple kesintisi, altyapi, UA) |
| Anahtar Metrikler | ... (aktivasyon/retention/MRR) |
| Haksiz Avantaj (= Moat) | ... |
Bos kalan blok = kapatilmasi gereken arastirma boslugu olarak isaretle.

## Quantified Value Prop
Status quo'ya gore degeri SAYISALLASTIR: "[X saat] / [$Y] / [Z adim] tasarruf veya kazanc". Kaynak/varsayim belirt.

## MVP Scope

### Ekranlar (max 3-4)
Her ekran icin:
1. [Ekran adi] — Ne yapar (2 cumle)
2. [Ekran adi] — Ne yapar
3. [Ekran adi] — Ne yapar

### 3 Ana Ozellik
1. ...
2. ...
3. ...

### V1'de OLMAYACAK seyler
- ...
- ...
- ...

## Moat Degerlendirmesi (Savunulabilirlik Analizi)

Soru: "Birisi bunu gordugunde 3 ayda kopyalayabilir mi?"

5 moat turunu degerlendir, her biri 0-3:

| Moat Turu | Skor (0-3) | Soru | Aciklama |
|-----------|-----------|------|----------|
| Veri Avantaji | ? | Daha cok kullanim = daha iyi urun mu? | Kullanicinin verdigi veri ile urun kisisellesir |
| Gecis Maliyeti | ? | Kullanici ne kadar veri/emek yatirir? | Ne kadar cok veri girerse, gecis o kadar zor |
| Network Etkisi | ? | Kullanici arttikca deger artar mi? | Birden fazla kisi ile daha degerli mi? |
| Hiz Avantaji | ? | Yeni niste ilk olma firsati var mi? | Ilk hareket eden ASO avantaji kazanir |
| Ekosistem Kilit | ? | Platform entegrasyonu rakibin kolayca kopyalayamayacagi mi? | HealthKit, Shortcuts, Watch, Widget gibi derin entegrasyon |

Skor ankorlari: 0=Yok | 1=Minimal (rakip 1-3 ayda kopyalar) | 2=Orta (3-6 ay) | 3=Guclu (6+ ay)

Toplam Moat Degerlendirmesi:
- < 5: Zayif moat — ilk 3 ayda sadik kullanici tabani olustur
- 5-10: Orta moat — 6-12 ay avantaj
- 10+: Guclu moat — uzun vadeli buyume plani yapabilirsin

Moat skoru < 5 ise: MVP'ye veya v2'ye moat artirici ozellikler oner (veri biriktirme, kisisellesme, platform entegrasyonu).

## Monetizasyon

| Plan | Fiyat | Icerik |
|------|-------|--------|
| Ucretsiz | $0 | ... |
| Premium | $X/ay | ... |
| Yillik | $X/yil | ... |

## Teknik Kararlar
- Platform: iOS (Swift/SwiftUI)
- Framework:
- Veritabani:
- Backend:
- Odeme: RevenueCat / StoreKit 2

## App Store Optimizasyonu
- **App Name (30 karakter):**
- **Subtitle (30 karakter):**
- **Keywords (100 karakter):**
- **Ilk 3 screenshot metni:**
  1. ...
  2. ...
  3. ...

## Ilk 30 Gun Plani
- Takip edilecek metrikler:
- Hedef sayilar (install, trial, paid):
- Pazarlama kanallari:

Onceki faz verileri:
[FAZ 1-8 OZETINI YAPISTIR]

GATE: Proje brief, MVP scope, moat degerlendirmesi, monetizasyon modeli ve ASO taslagi tamamlanmali.
```

---

## FAZ 10: Seytan'in Avukati

**Amac:** Projenin tum varsayimlarini sorgulamak, 3 katmanli puanlama sonuclarini dogrulamak ve go/no-go karari vermek.

**Prompt:**

```
[FIKIR ADI] projesi icin seytanin avukati rolunu ustlen. Her kritik varsayimi sorgula.

Bu projenin 3 katmanli puanlama sonuclari:
- Katman 1 (Pass/Fail): [SONUC]
- Katman 2 (Agirlikli Skor /100): [SKOR]
- Katman 3 (Fizibilite Carpani): [CARPAN]
- Final Skor: [SKOR]
- Moat Toplam Skoru: [SKOR]

## Varsayim Tablosu

Projenin dayandigi her varsayimi listele ve sorgula:

| # | Varsayim | Kanit Gucu (Guclu/Orta/Zayif) | Yanlis olsaydi ne olurdu? | Risk (Dusuk/Orta/Yuksek) | Onlem |
|---|----------|-------------------------------|---------------------------|--------------------------|-------|
| 1 | Pazar yeterince buyuk | ... | ... | ... | ... |
| 2 | Kullanicilar oder | ... | ... | ... | ... |
| 3 | Fark yeterli | ... | ... | ... | ... |
| 4 | MVP yeterli | ... | ... | ... | ... |
| 5 | Retention var | ... | ... | ... | ... |
| 6 | Moat yeterli (skor < 5 ise ozellikle sorgula) | ... | ... | ... | ... |

## Menopoz Testi (5 Soru)

Bu 5 soruyu cevapla:
1. Lider uygulamanin rating sayisi pazardaki GERCEK talebi destekliyor mu?
2. Bu kategoride indie developer para kazanmis mi? Kanit nerede?
3. Pazar raporu rakamlari ile gercek App Store verileri uyusuyor mu?
4. "Bos alan" gercekten firsat mi yoksa kimsenin istemediginden mi bos?
5. Sectigimiz farklilasma (fark) gercekten kullanicinin umrunda mi?

## En Kotu Senaryo

3 en kotu senaryoyu yaz ve her biri icin:
- Ne olurdu?
- Nasil toparlanirdin?
- Bunu onlemek icin simdi ne yapabilirsin?

### Senaryo 1: [Baslik]
- ...

### Senaryo 2: [Baslik]
- ...

### Senaryo 3: Moat yetersiz, rakip kopyalar
- Ne olurdu? Rakip 1-3 ayda benzer urunu cikarir
- Nasil toparlanirdin? Veri avantaji ve gecis maliyeti olusturacak ozellikler ekle
- Bunu onlemek icin simdi ne yapabilirsin? Ilk 3 ayda sadik kullanici tabani olustur, ASO avantajini kullan

## Go / No-Go Kontrol Listesi

- [ ] Olumcul kusur yok
- [ ] En az 3 varsayim GUCLU kanita sahip
- [ ] Indie gelir kaniti en az 1 tane var
- [ ] Lider uygulama rating'i 10K+ (pazar var)
- [ ] Fark cumlesi net ve kullanici odakli
- [ ] MVP 4 haftada cikarilabilir
- [ ] Moat skoru < 5 ise moat artirma plani var

→ KARAR: DEVAM / PIVOT / GERI DON

Olumcul kusurlar (bunlardan biri varsa PIVOT veya KILL):
- Lider rating < 500 (pazar yok)
- Hicbir indie gelir kaniti yok VE monetization modeli belirsiz
- Apple/Google'in yerlesik cozumu tam bu problemi cozuyor
- MVP 2-4 haftada cikarilmaz
- Farklilasma cumlesi yazilamiyor
- Moat skoru 0 VE rakipler aktif/guclu

Basarisizlik durumunda:
- Pivot icin: Ayni pazar farkli aci VEYA ayni aci farkli pazar
- Kill icin: Tamamen birak, Faz 1'e don, onceki kategorilerden farkli alanlara yonel

Proje brief:
[FAZ 9 SONUCLARINI YAPISTIR]
```

---

## BONUS: Hizli Fizibilite Analizi (3 Katmanli Mini Versiyon)

**Amac:** Herhangi bir app fikri icin 10 dakikada hizli bir fizibilite kontrolu yapmak. Tum sureci baslatmadan once fikrin temel degerini olcmek icin kullan. 3 katmanli modelin hizli versiyonu.

**Prompt:**

```
[APP FIKRI] icin 3 katmanli hizli fizibilite analizi yap.

=== KATMAN 1: PAZAR GECERLILIGI (Pass/Fail) ===

Su 4 kontrol TUMU GECMELI:

1. PAZAR VAR MI?
   - Bu kategorideki lider uygulamanin iOS rating sayisi kac?
   - Rating > 500 ise GECTI, < 500 ise ELENDI.

2. PAZAR ERISILEBILIR MI?
   - Apple/Google yerlesik cozumu (Health, Reminders, Notes, Calendar) bu isi tamamen cozuyor mu?
   - Cozuyorsa ELENDI, cozemiyorsa GECTI.

3. PAZAR BUYUYOR MU?
   - Son 1 yilda yeni uygulamalar cikti mi? Google Trends yukseliste mi?
   - Evet ise GECTI, hayir ise ELENDI.

4. REGULASYON ASILABILIR MI?
   - Indie developer hukuk ekibi/ozel lisans olmadan bu pazara girebilir mi? (FCRA, HIPAA, finans lisansi, veri broker tescili gibi asilmaz engel var mi?)
   - Asilabilir ise GECTI, asilmaz ise ELENDI.

Herhangi biri ELENDI ise → VAZGEC. Devam etme.

=== KATMAN 2: FIRSAT KALITESI (Hizli Degerlendirme) ===

5 kriteri 1-5 puanla, agirlikli toplam hesapla (max 100):

| Kriter | Agirlik | Skor (1-5) | Puan |
|--------|---------|-----------|------|
| Talep Sinyali (lider rating buyuklugu, goc sinyalleri) | x5 | ? | ? |
| Gelir Kaniti (indie dev para kazaniyor mu?) | x5 | ? | ? |
| Rekabet Boslugu (1-2 yildiz sikayetler, fiyat/UX boslugu) | x4 | ? | ? |
| Retention (kullanim sikligi) | x3 | ? | ? |
| Zamanlama (pazar degisimi, firsat penceresi) | x3 | ? | ? |
| **Toplam** | | | **/100** |

=== KATMAN 3: FIZIBILITE CARPANI ===

4 carpan, her biri 0.6 / 0.8 / 1.0:
- Teknik Zorluk: 1.0=Basit | 0.8=Orta | 0.6=Zor
- Kurucu Uyumu: 1.0=Problemi kendin yasiyorsun | 0.8=Ilgi var | 0.6=Ilgi yok
- Regulasyon/Uyum: 1.0=Regulasyon yok/basit | 0.8=Orta (KVKK, temel gizlilik) | 0.6=Agir (FCRA, HIPAA, finans lisansi)
- MVP Suresi: 1.0=< 4 hafta | 0.8=4-8 hafta | 0.6=8+ hafta

Carpan = Teknik x Kurucu x Regulasyon x MVP
(Regulasyon 1.0 ise pratikte 3 faktorlu kalir.)

=== FINAL ===

Final Skor = Katman 2 Toplam x Katman 3 Carpan

| Final Skor | Sonuc |
|-----------|-------|
| 60+ | DEVAM ET — guclu firsat |
| 45-59 | DIKKATLI ILERLE — ek dogrulama gerek |
| 30-44 | RISKLI — diger firsatlar daha zayifsa dusun |
| < 30 | VAZGEC |

MENOPOZ TESTI (ek kontrol):
- Pazar buyuklugu iddialari ile gercek App Store verileri uyusuyor mu?
- Rapor "milyarlar" diyorsa ama lider uygulama 1K rating ise → UYARI

Sonuc: DEVAM ET / DIKKATLI ILERLE / VAZGEC
```
