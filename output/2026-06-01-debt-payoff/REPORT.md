# App Arastirma Raporu: Debt Payoff Planner

> Tarih: 2026-06-01
> Mod: Standard
> Metodoloji: v3.2 (10 Faz + Faz 5.5, 3 Katmanli Puanlama + Dagitim Fizibilitesi)

---

## Yonetici Ozeti

| Alan | Deger |
|------|-------|
| **Karar** | SARTLI GO -- Faz 5.5 davranis dogrulamasina KOSULLU |
| **Final Skor** | 56/100 (K2) x 0.80 (K3) = **44.8** (Zayif-Orta sinirinda) |
| **Risk Seviyesi** | ORTA |
| **MVP Tahmini** | ~4 hafta (manuel, regulasyonsuz) |
| **Dagitim Fizibilitesi** | KD ~30-40 (DUSUK-ORTA) -- long-tail acik, KESFEDILEBILIR |
| **Anahtar Bulgu** | Pazar mature/duz (Regular/Constant) ve indie gelir kaniti SIFIR -- ama tek gercek duvar OxbowSoft (7.1K), sonrasi dik ucurum; somut bir adlandirilmis icgoru var: rakipler urunu statik HESAPLAYICI saniyor, gercek is "cok yillik odemenin messy-middle'ini hayatta tutmak" ve tam orada kiriliyorlar. Apple Watch/Widget 1/10 (liderde YOK). |
| **Oneri** | Hemen insa ETME. Once Faz 5.5: "messy-middle" icgorusunu r/debtfree + Ramsey ekosisteminde landing/fake-door + Mom-Test ile DAVRANISLA dogrula. Davranis sinyali gelirse GO (urun-farki + dagitim acikligi guclu); gelmezse KILL (pazar duz, indie kanit yok). |

---

## 1. Pazar Analizi

### Pazar Durumu
| Gosterge | Deger | Etiket |
|----------|-------|--------|
| Ana Keyword | "debt payoff" / "debt snowball" | -- |
| Lider (niche) | Debt Payoff Planner & Tracker (OxbowSoft) | -- |
| Lider Rating | 7,100 | KESIN |
| Lider Yildiz | 4.7/5 | KESIN |
| #2 Oyuncu | Changed (Mark Cuban destekli) -- 5,200 rating, 4.6 | KESIN |
| Lider (genis segment) | Bright Money 231K (FARKLI segment: fintech/kredi) | KESIN |
| Yasam-Dongusu | **Asama: Regular (mature) / Buyume: Constant (duz)** | TAHMINI |
| Mevsimsellik | Guclu Ocak "yeni yil karari" spike (~%61 finans odakli) | TAHMINI |
| Makro baglam | ABD hanehalki borcu $18.8T (Q1 2026, +%0.1 QoQ duz); CC borcu $1.252T (QoQ DUSTU) | KESIN (NY Fed) |
| Apple autocomplete (1. parti talep) | "debt" -> debt payoff / tracker / snowball / free (head'ler gercek) | DUSUK (cikarim) |

### Pazar Gecerliligi (Katman 1)
| Kriter | Sonuc |
|--------|-------|
| Pazar var mi? (rating > 500) | **GECTI** -- OxbowSoft 7.1K, Changed 5.2K |
| Erisilebilir mi? (Apple/Google engeli yok) | **GECTI** -- Apple'in snowball/borc-odeme araci yok (Wallet/Health bunu yapmiyor) |
| Buyuyor mu? (yeni girisler VE/VEYA trend) | **GECTI (zar zor)** -- yeni kucuk girisler var (2025-2026) AMA trend duz; bkz. Zamanlama |
| Regulasyon asilabilir mi? (indie) | **GECTI** -- manuel hesaplayici, finansal lisans gerekmez (bank-sync MVP'de YOK) |

**Not:** K1#3 yeni-giris sayesinde geciyor ama yasam-dongusu duz/mature; bu nuans Zamanlama puanina yansidi (v3.2).

---

## 2. Dagitim Fizibilitesi (Kesfedilebilirlik) -- v3.2 YENI

Pazar var ama YENI APP RANK ALABILIR MI? Bu pazarda cevap: buyuk olcude EVET.

### Keyword Difficulty (top-10 rating dagilimindan, paid arac YOK)
| # | App | iOS Rating | Yildiz | Not |
|---|-----|-----------:|:------:|-----|
| 1 | OxbowSoft (Debt Payoff Planner) | 7,100 | 4.7 | Tek gercek duvar |
| 2 | Changed | 5,200 | 4.6 | Mark Cuban destekli, roundup modeli |
| 3 | Debt Payoff Box (Snowball) | 2,400 | 4.5 | $9.99 tek-seferlik |
| 4 | Debt Snowball / Polybit | 1,300 | 4.7 | **2023'ten beri stale** |
| 5 | Debt Free / Mobile Innovations | 942 | **4.1** | Zayif rating -- 4.7 duvarini kiriyor |
| 6-10 | OweMe, Debt Payoff Assistant, AppFlux, DebtApp, Kuznecovs | 315 -> 21 | 3.6-4.7 | Yarisi <140 rating; bazilari terk edilmis |

**Difficulty okumasi: ~KD 30-40 (DUSUK-ORTA, TAHMINI).** Gerekce: top-3 sonrasi dik ucurum (hepsi <1.3K), top-10'un yarisi <315 rating, iki incumbent 2023'ten stale, biri 3.6 yildiz. Savunulmamis bir alan.

**Override kontrolu:** "Top-5 hepsi 4.7+ -> Rekabet MAX 2" TETIKLENMIYOR (4.1 var). "Yuksek difficulty + wedge yok -> MAX 2" TETIKLENMIYOR (difficulty dusuk + wedge var).

### Opportunity / Long-tail (dusuk-difficulty acik keyword'ler)
- **"debt snowball"** -- birincil app stale (Polybit 2023) -> DUSUK difficulty
- **"debt free tracker" / "debt free"** -- tek incumbent 4.1 yildiz/942 -> DUSUK
- **"debt avalanche"** -- hicbir app ismiyle sahiplenmemis -> bos long-tail (hacim ayri dogrulanmali)
- **"debt payoff" / "pay off debt"** -- head, OxbowSoft/Changed sahibi -> ORTA-YUKSEK, lider OLMA

**Karar etkisi:** Kesfedilebilirlik LEHTE. Head term'de degil, long-tail'de gir. Bu, v3.2'nin yeni ekledigi ve onceki analizde HIC olcmedigimiz boyut -- ve burada en guclu pozitif sinyal.

---

## 3. Rakip Analizi

### Adlandirilmis Missed-Insight (Rekabet 4-5 icin ZORUNLU -- KARSILANDI)

**Tek cumle:** Rakipler (ozellikle OxbowSoft) debt-payoff app'ini statik bir HESAPLAYICI saniyor (borclari bir kez gir, odeme tarihi gosterilsin) -- ama gercek is-to-be-done cok-yillik odemenin **messy-middle**'ini hayatta tutmak: gerceklesEN duzensiz/biweekly/ekstra odemeleri ve bakiye degisimlerini loglamak ve plan saptiginda yeniden MOTIVE olmak -- ve app'ler tam o anda kiriliyor.

**Davranissal kanit (Ucgen Kurali, sadece "isterdim" degil):**
- "Toplam tutari degistirmek payoff hesabini berbat ediyor" -- bakiye degisince cekirdek vaat (dogru tarih) cokuyor. (Review mining: ekstra-odeme karisik ~7, duzenlenemez ~6)
- Ekstra-odeme tahsisi (snowball'un TUM olayi) belirsiz -- "ek paranin nereye gidecegi" net degil. (biweekly Pro-kilitli ~8)
- Asil basarisizlik modu matematiksel degil MOTIVASYONEL: insanlar "matematikte basarisiz" hissedip biraktigi icin -- Ramsey "debt-free scream" fenomeni kullanicilarin kutlanmis kilometretaslari ile suruklendiginin kaniti. Incumbentlar %20'yi (hesaplayici) optimize edip %80'i (davranis) ihmal ediyor.

**Indie-exploit acisi:** Dusuk-friksiyon "messy-middle" tracker -- bakiye/ekstra/biweekly duzenleme payoff tarihini ASLA bozmaz + kilometretasi kutlamasi gomulu. YNAB/Monarch/Rocket Money (bank-sync) bunu COZMUYOR (onlar aggregation cozer, snowball-execution-through-disruption degil).

### Fiyat Karsilastirmasi
| Metrik | Deger |
|--------|-------|
| Median yillik | $19.99 (KESIN) -- OxbowSoft tam burada |
| Ortalama (OweMe outlier haric) | ~$14.8 |
| Aralik | $4.99 -> $69.99 |
| **Bos band** | **$25-65/yr TAMAMEN BOS** (up-market acik) |
| Hakim model | Freemium + abonelik; lifetime ucuz ($6.99-9.99) |

**Fiyat stratejisi:** Alt-fiyat tukenmis (Mobile Innovations $9.99/yr, AppFlux $4.99/yr zaten var). Acik olan UP-market (~$29.99/yr daha iyi urun) veya orta lifetime (~$24.99).

### Ozellik Bosluk Matrisi (10 app)
| Ozellik | Var olan | Not |
|---------|:--------:|-----|
| Apple Watch | **1/10** | Sadece Debt Free (en zayif oyuncu 4.1); OxbowSoft'ta YOK |
| Widget | **1/10** | Ayni; lider liderde YOK |
| iCloud sync | 2/10 | Apple-native kitle icin table-stakes ama nadir |
| Bank-sync | ~0/10 | Tum planlayici manuel (regulasyon/Plaid maliyeti) |

**Watering-Hole'lar (Sales Safari -- Faz 5.5 + lansman icin):** r/personalfinance (17-21M, hacim), **r/debtfree (~1M, cekirdek)**, **r/DaveRamsey (~900K-1M, en hedefli alici)**, r/ynab (200K), Ramsey ekosistemi (haftada 18M dinleyici, "debt-free scream"). En yuksek-intent: r/debtfree + r/DaveRamsey + Ramsey/EveryDollar.

---

## 4. Firsat Puanlama

### Katman 2: Firsat Kalitesi (/100)
| Kriter | Agirlik | Skor | Puan | Veri Kaynagi / Gerekce |
|--------|---------|:----:|:----:|------------------------|
| Talep Sinyali | x5 | 3 | 15 | Lider 7.1K (rating-ankoru 2) AMA 2. kaynak triangulasyonu yukseltir: Apple autocomplete head'leri gercek + Android 500-650K indirme + r/debtfree~1M / Ramsey 18M (KESIN/TAHMINI) |
| Gelir Kaniti | x5 | **2** | 10 | Indie gelir kaniti SIFIR (3. kez dogrulandi). OxbowSoft indie degil (cok-kuruculu LLC). Override: indie gelir yok -> MAX 2 |
| Rekabet Boslugu | x4 | 4 | 16 | Adlandirilmis icgoru VAR (messy-middle, davranis kanitli) + Watch/widget whitespace + 8 sikayet temasi. Difficulty dusuk, wedge UX-moat (indie cozer) -> override yok |
| Retention | x3 | 3 | 9 | Cok-yillik haftalik check-in; AMA borc bitince silme + motivasyon churn riski (TAHMINI) |
| Zamanlama | x3 | **2** | 6 | **Yasam-dongusu: Regular/Constant (duz/mature).** Makro borc duz (CC borcu QoQ dustu). Onceki "trends up -> 4" v3.2 yasam-dongusu disipliniyle DUZELTILDI. Ocak spike taktiksel pencere, stratejik tailwind degil |
| **Toplam** | | | **56** | |

**Uygulanan Override:** Indie gelir yok -> Gelir MAX 2 (uygulandi). Difficulty/4.7-duvar/named-insight override'lari kontrol edildi -> tetiklenmedi (lehte).

### Katman 3: Fizibilite Carpani
| Kriter | Skor | Gerekce |
|--------|:----:|---------|
| Teknik Zorluk | 1.0 | Basit: snowball/avalanche matematik + CRUD + bildirim + widget/Watch (standart SwiftUI), dis API yok |
| Kurucu Uyumu | 0.8 | Ilgi var, borc domain deneyimi sinirli |
| Regulasyon/Uyum | 1.0 | Manuel hesaplayici -- finansal lisans/regulasyon yok (bank-sync olsa 0.6'ya duserdi) |
| MVP Suresi | 1.0 | ~4 hafta (cekirdek + robust-edit; widget/Watch v1.1) |
| **Carpan** | **0.80** | |

### Final Skor
**56 x 0.80 = 44.8** -> **Zayif-Orta sinirinda (45 esiginin 0.2 altinda)**

Ham skor "Zayif" diyor; ama v3.2 dagitim fizibilitesi (KESFEDILEBILIR) + somut named-insight raw skorun yakalamadigi iki guclu pozitif. Bu yuzden karar otomatik "birak" degil, "Faz 5.5 ile ucuza dogrula."

---

## 5. Gelir Potansiyeli

### Indie Gelir Kaniti
*IndieHackers/#buildinpublic/blog -- 3. kez tarandi (Haziran 2026). Debt-payoff niche'inde indie gelir kaniti BULUNAMADI.* Diger niche'lerde bol indie gelir var (habit tracker, AI/SaaS) ama debt-payoff'ta SIFIR -- bu, survivorship bias gozonune alindiginda hafif NEGATIF sinyal (deneyenler yeterince kazanamadigi icin paylasmiyor olabilir).

OxbowSoft = funded-benzeri cok-kuruculu sirket (GMA/Motley Fool basini); "indie kazaniyor" premisi gecerli degil.

### Fiyat Modeli Onerisi (up-market acikligi)
| Plan | Fiyat | Icerik |
|------|-------|--------|
| Ucretsiz | $0 | 3 borca kadar, snowball/avalanche, temel ilerleme |
| Premium yillik | $29.99/yr | Sinirsiz borc, messy-middle (robust edit + biweekly/ekstra), Watch+Widget, kilometretasi kutlama, export |
| Lifetime | $24.99 | Ayni (abonelik-yorgunlugu segmenti) |

Not: $25-65/yr bandi bos -> $29.99 up-market savunulabilir AMA sadece urun gercekten ustun olursa.

---

## 6. Dogrulama (4 Kontrol)

| # | Kontrol | Sonuc | Guvenilirlik |
|---|---------|-------|-------------|
| 1 | Lider rating gercek mi? | **DOGRULANDI** -- OxbowSoft 7.1K App Store'dan dogrudan | KESIN |
| 2 | Indie gelir kaniti | **BULUNAMADI** -- 3 ayri tarama, 0 sonuc | KESIN (yokluk) |
| 3 | Kullanici goc/talep sinyali | **KISMI** -- guclu topluluk (r/debtfree, Ramsey) + complaint var; ama bunlar "isterdim" agirlikli, davranis (odeme) dogrulanmadi -> Faz 5.5 sart | TAHMINI |
| 4 | Menopoz Testi | **GECTI** -- pazar gercek (7.1K + 500-650K Android + $18.8T makro), hayali degil | KESIN |

**Dogrulama Sonucu:** KISMI -- pazar ve urun-boslugu gercek; eksik olan DAVRANISSAL talep kaniti (messy-middle icgorusu henuz hipotez). Faz 5.5 bunu kapatacak.

---

## 7. Risk Degerlendirmesi

| # | Risk | Olasilik | Etki | Onlem |
|---|------|----------|------|-------|
| 1 | Funded rakipler (OxbowSoft + Mark Cuban'in Changed'i) niche'i sikilastirir | Orta | Kaynak esitsizligi | Long-tail + messy-middle wedge'e odaklan, head-term savasina girme |
| 2 | Messy-middle icgorusu yanlis (kullanici aslinda umursamiyor) | Orta | Tum tez coker | **Faz 5.5 davranis testi** -- insa etmeden once |
| 3 | Pazar duz/mature -- ucretli buyume yavas | Yuksek | Dusuk gelir | Ocak mevsimsel pencere + organik (r/debtfree, Ramsey) |
| 4 | Post-payoff churn (borc bitince silme) | Yuksek | Dusuk LTV | "Debt-free sonrasi" tasarruf/birikim modu, referral, kutlama paylasimi |
| 5 | Indie gelir kaniti sifir -- belki kimse para kazanamiyor | Orta | Ekonomik cikmaz | Faz 5.5'te fiyat sinyali (on-odeme/rezervasyon) test et |

---

## 8. MVP Onerisi -- "Messy-Middle" Wedge

### Ekranlar (3)
| # | Ekran | Ne yapar |
|---|-------|----------|
| 1 | Borc Listesi | Borc ekle/duzenle (bakiye degissin -- payoff tarihi BOZULMAZ) |
| 2 | Odeme Plani | Snowball vs avalanche; ekstra/biweekly odeme tahsisi NET gosterilir |
| 3 | Ilerleme + Kutlama | Kalan/odenen, tahmini debt-free tarihi, kilometretasi kutlamasi |

### 3 Ana Ozellik (rakiplerin kirildigi yer)
1. **Bozulmayan plan:** Her duzenleme (bakiye, ekstra, biweekli) sonrasi payoff tarihi dogru kalir -- OxbowSoft'un #1 sikayeti.
2. **Net ekstra-odeme tahsisi:** "Ek $X nereye gidiyor" tek bakista -- snowball'un ozu.
3. **Kilometretasi kutlamasi:** Motivasyon (%80 davranis) -- Ramsey "scream" mantigi, glanceable Widget + Watch.

### V1'de OLMAYACAKLAR
- Bank-sync (regulasyon + Plaid maliyeti + K3'u dusurur)
- Coklu kullanici / aile
- AI tavsiye

### Teknik Stack
iOS (Swift + SwiftUI + WidgetKit + WatchKit), SwiftData (yerel), iCloud (CloudKit), RevenueCat, PostHog.

---

## 9. Faz 5.5: Build-Oncesi Dogrulama Paketi -- v3.2 YENI (insa ETMEDEN once calistir)

Skor borderline + messy-middle henuz HIPOTEZ + indie gelir kaniti yok. Bu yuzden v3.2: kod yazmadan davranisla dogrula.

### A) Landing / Fake-Door Metni (Claude uretti)
- **Baslik:** "Borcunu ode -- plan hayatla birlikte degissin."
- **Alt baslik:** "Ekstra odeme yaptin, bakiye degisti? Tarihi bozmadan guncelle. Abonelik yok secenegi."
- **3 fayda:** (1) Bakiye/ekstra/biweekli duzenle -- payoff tarihi dogru kalir. (2) Ek paran tam nereye gidiyor, gor. (3) Her kilometretasini kutla (Widget + Watch).
- **CTA:** "Erken erisim -- ilk 100 kisi $24.99 lifetime'i kilitler" (sahte buton -> email + "yakinda").

### B) Onceden-Yazilan Esik (pre-registration, DEGISTIRILEMEZ)
"r/debtfree + r/DaveRamsey'den gelen 200 ziyaretcinin >=%8'i email birakir VE >=5 kisi $24.99 on-rezervasyon yaparsa -> GO." (Sadece tiklama/email zayif; on-odeme = gercek davranis.)

### C) Mom-Test Gorusme Kilavuzu (5-7 kisi, r/debtfree/Ramsey)
- "Bana borc odeme planini en son ne zaman BOZDUGUNU anlat -- ne oldu, ne yaptin?"
- "Su an hangi app/Excel ile takip ediyorsun? Onda en sinir bozucu an neydi, en son ne zaman oldu?"
- "Ekstra para geldiginde nereye koyacagina nasil karar veriyorsun?"
- "Bunun icin daha once para odedin mi? Ne kadar, neye?"
- (YASAK: "Boyle bir app kullanir/oder miydin?")

### D) Karar Mantigi
- Davranis sinyali (on-odeme, mevcut araca harcama) -> GO, urun-farki + dagitim acikligi guclu.
- Sadece "kullanirim/begendim" -> Talep/Gelir MAX 3 zaten uygulandi; YENIDEN dusun (RF-16).
- Messy-middle umursanmiyor -> icgoru yanlis, KILL (pazar duz, indie kanit yok).

---

## 10. Sonraki Adimlar

1. [ ] **Faz 5.5'i calistir** (landing + 5-7 Mom-Test gorusmesi, r/debtfree + r/DaveRamsey). Guven >=%70 + 1 davranis sinyali ara.
2. [ ] Long-tail keyword hacmini dogrula ("debt snowball", "debt avalanche", "debt free tracker").
3. [ ] OxbowSoft + Changed'i indir, messy-middle kirilmasini birinci elden gor.
4. [ ] Faz 5.5 GO verirse -> MVP wireframe (3 ekran) + Ocak penceresine lansman planla.

---

## 11. Cross-Report Karsilastirma (guncel veri, v3.2)

| Fikir | K2 | K3 | Final | Karar | Ana not |
|-------|----|----|-------|-------|---------|
| **Debt Payoff (v3.2)** | 56 | 0.80 | **44.8** | SARTLI GO (Faz 5.5) | Kesfedilebilir + named-insight; pazar duz, indie kanit yok |
| Journal | 57 | 0.512 | 29.2 | ELENDIR/Zayif | Apple Journal cross-platform |
| Subscription Tracker | 48 | 0.80 | 38.4 | NO-GO | Apple yerlesik abonelik |
| Medication | 55 | 0.41 | 22.5 | ELENDIR | Apple Health yerlesik + regulasyon |
| People Finder | 55 | 0.307 | 16.9 | ELENDIR | Regulasyon mayini |

Debt Payoff hala en yuksek -- ve v3.2'nin dagitim fizibilitesi onu digerlerinden ayiran yeni bir avantaj veriyor (Apple ile yarismiyor + kesfedilebilir). Ama 44.8 borderline; karar Faz 5.5'e baglandi.

---

## Veri Kaynaklari

| # | Kaynak | Tarih | Guvenilirlik |
|---|--------|-------|-------------|
| 1 | App Store -- OxbowSoft, Changed + top-10 cluster (dogrudan) | 2026-06-01 | KESIN |
| 2 | Bagimsiz OxbowSoft gelir dogrulamasi (cok-kuruculu LLC, $30K dogrulanamadi) | 2026-06-01 | KESIN/TAHMINI |
| 3 | NY Fed Q1 2026 HHDC ($18.8T, CC $1.252T) | 2026-06-01 | KESIN |
| 4 | Review mining + named-insight (app reviews + Ramsey/Bankrate davranis cercevesi) | 2026-06-01 | TAHMINI (uclendi) |
| 5 | Watering-hole'lar (r/personalfinance, r/debtfree, r/DaveRamsey, Ramsey Show) | 2026-06-01 | KESIN/DUSUK (uye sayilari kismi) |
| 6 | Keyword difficulty (top-10 rating dagilimi) + autocomplete | 2026-06-01 | TAHMINI/DUSUK |
| 7 | Yasam-dongusu / Google Trends cikarimi | 2026-06-01 | TAHMINI |
| 8 | IndieHackers/#buildinpublic indie gelir taramasi | 2026-06-01 | KESIN (yokluk) |

---

*Bu rapor App Idea Research Agent v3.2 metodolojisi ile olusturulmustur.*
*Mod: Standard | v3.2 yeni: Dagitim Fizibilitesi, yasam-dongusu Zamanlama, adlandirilmis-icgoru Rekabet, Apple autocomplete Talep, Sales Safari, Faz 5.5 | 2 paralel arastirma agenti*
