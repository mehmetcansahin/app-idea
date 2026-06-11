# Arac, Veri Kaynagi ve Yontem Envanteri — App Pazar Arastirmasi

> Bu belge, app pazar arastirmasinda kullanilabilecek TUM araclari, veri kaynaklarini ve yontemleri durust guvenilirlik degerlendirmeleriyle dokumante eder.
> Amac: Hangi veriye guvenilebilir, hangisine guvenilemez — net olmak.

---

## 1. APP STORE VERILERI

### 1.1 Ucretsiz Yontemler

| Arac / Yontem | Ne Verir | Guvenilirlik | Notlar |
|---|---|---|---|
| App Store (manuel arama) | Rating sayisi, yildiz puani, fiyat, screenshot, description, in-app purchase listesi, guncelleme sikligi, developer bilgisi | ✅ Yuksek | En guvenilir kaynak — Apple'in kendi gercek verisi. Hicbir tahmin yok. |
| App Store Search Suggest | Populer arama terimleri (autocomplete) | ✅ Yuksek | Gercek kullanici aramalarini yansitir. Kullanicilarin ne arayip ne bulamadigini anlamak icin degerli. |
| Google "site:apps.apple.com" | Uygulama sayfalari, indexed aciklamalar | ✅ Yuksek | App Store disinda alternatif erisim yolu. SEO perspektifi de verir. |
| Google Play Store (manuel) | Android tarafindaki rating, indirme araligi, fiyat | ✅ Yuksek | iOS ile karsilastirma icin. Google Play "10K-50K indirme" gibi aralik gosterir. |
| App Store "What's New" gecmisi | Guncelleme sikligi ve ne degistirildi | ✅ Yuksek | Aktif gelistirme sinyali. Sik guncelleme = aktif urun. |
| App Store kategori siralamasi | Top Free, Top Paid, Top Grossing listeleri | ✅ Yuksek | Anlik siralama, gecmis trend yok. |

### 1.2 Ucretsiz Araclar (Sinirli Erisim)

| Arac | Ne Verir | Guvenilirlik | Sinirlamalar |
|---|---|---|---|
| AppFollow (free tier) | Review monitoring, basit analytics, rating takibi | ⚠️ Orta | Sinirli uygulama sayisi. Ucretsiz planda 1-2 uygulama takip edilebilir. |
| AppMagic (free tier) | Indirme tahminleri, kategori siralamasi, basit rakip karsilastirma | ⚠️ Orta | 3. parti tahmin modeli. Rakamlar kesin degil, yonlendirici. |
| SimilarWeb (free tier) | Web trafik verileri, genel kullanim istatistikleri | ⚠️ Orta | Mobil uygulama verileri cok sinirli. Web-first arac. |
| Sensor Tower (free) | Sinirli keyword data, basit siralama bilgisi | ⚠️ Orta | Cogu degerli veri paywall arkasinda. Free tier neredeyse islevsiz. |
| AppFigures (free tier) | Basit ASO verileri, keyword oneriler | ⚠️ Orta | Cok sinirli. Ucretli plana yonlendirmek icin tasarlanmis. |
| AppBot (free trial) | Review analizi, sentiment analysis | ⚠️ Orta | Trial suresi sinirli. Sonra ucretli. |

### 1.3 Ucretli Araclar

| Arac | Fiyat Araligi | Ne Verir | Guvenilirlik |
|---|---|---|---|
| Sensor Tower (paid) | $$$ (enterprise, yillik sozlesme) | Indirme tahmini, gelir tahmini, keyword data, kategori analizi, reklam istihbarati | ⚠️ Orta-Yuksek (hepsi tahmin modeli) |
| data.ai (eski adi App Annie) | $$$ (enterprise, yillik sozlesme) | En kapsamli pazar verisi, indirme/gelir tahmini, kullanim metrikleri, demografi | ⚠️ Orta-Yuksek (tahmin modeli) |
| AppTweak | ~$69/ay baslangic | ASO, keyword difficulty, rakip takip, A/B test onerisi | ⚠️ Orta |
| Mobile Action | ~$59/ay baslangic | ASO, keyword explorer, rakip analizi, siralama takibi | ⚠️ Orta |
| Appfigures (paid) | ~$29/ay baslangic | ASO analytics, keyword takip, review monitoring | ⚠️ Orta |
| RevenueCat | Ucretsiz (kendi uygulamani icin) | Gercek gelir verisi, churn, subscription analytics | ✅ Yuksek (SADECE kendi uygulamanin verisi) |
| Adapty | Ucretsiz baslangic | Subscription analytics, paywall A/B test | ✅ Yuksek (SADECE kendi uygulamanin verisi) |
| Superwall | Ucretsiz baslangic | Paywall optimizasyonu, A/B test | ✅ Yuksek (SADECE kendi uygulamanin verisi) |

**ONEMLI NOT:** Sensor Tower ve data.ai gibi araclarin verdigi indirme/gelir rakamlari TAHMIN'dir. Gercek veri degil. Bu araclarin kendi modelleri vardir ve hata payi %30-50 arasinda olabilir. Ozellikle niche uygulamalarda hata payi daha da yuksektir.

---

## 2. KEYWORD / ASO VERILERI

| Kaynak | Ne Verir | Guvenilirlik | Not |
|---|---|---|---|
| Apple Search Ads (ucretsiz hesap) | Keyword popularity (1-5 skala), onerilen teklif fiyatlari | ⚠️ Orta | Eylul 2025'te sistem degisti. Eski veriler ve rehberler artik guvenilmez. Yeni sistemi ogrenip ona gore degerlendirilmeli. |
| App Store Search Suggest | Autocomplete onerileri, iliskili arama terimleri | ✅ Yuksek | Gercek kullanici davranisina dayali. Kullanicilarin gercekten ne aradigini gosterir. |
| Google Trends | Arama trendi karsilastirma, mevsimsellik, bolgesel ilgi | ✅ Yuksek | WEB aramasi verisi — mobil uygulama aramasi degil. Ama genel ilgi seviyesini gosterir. |
| Google Keyword Planner | Aylik arama hacmi (web), rekabet seviyesi | ✅ Yuksek | Mobil degil ama bir konuya ilgi olup olmadiginin guclu gostergesi. |
| Keyword Tool (keywordtool.io, free) | App Store keyword onerileri | ⚠️ Dusuk-Orta | Tahmini veriler. Free tier'da hacim gostermez. |
| ASO araclari (AppTweak, MobileAction) | Keyword difficulty, search volume tahmini, siralama sansi | ⚠️ Orta | Hepsi tahmin modeli. Farkli araclar farkli rakamlar verebilir. |
| Rakip uygulamalarin description'lari | Hedefledikleri keywordler | ✅ Yuksek | Rakip ne yaziyorsa o keyword'e onem veriyor demektir. Ucretsiz, herkese acik. |
| App Store review metinleri | Kullanicilarin kendi kullandigi terimler | ✅ Yuksek | Gercek kullanici dili. Keyword arastirmasi icin altin madeni. |

**PRATIK ONERI:** En iyi keyword arastirmasi kombinasyonu:
1. App Store Search Suggest ile baslayip gercek aramalari gorun
2. Google Trends ile ilgi seviyesini dogrulayin
3. Rakip description'larindan keyword cikartin
4. Apple Search Ads ile popularity kontrol edin

---

## 3. KULLANICI & PAZAR ARASTIRMASI

| Kaynak | Ne Verir | Guvenilirlik | Nasil Kullanilir |
|---|---|---|---|
| Reddit (subreddit arama) | Gercek kullanici sikayetleri, goc sinyalleri, ozellik talepleri, memnuniyetsizlik | ✅ Yuksek | `[uygulama adi] alternative` veya `leaving [uygulama]` veya `hate [uygulama]` seklinde ara. r/apps, r/iphone, niche subreddit'ler. |
| Twitter/X | Build in public verileri, kullanici tepkileri, anlik duyarlilik | ⚠️ Orta | `#buildinpublic` hashtag'i, uygulama adi ile arama. Ses getiren sikayetler ozellikle degerli. |
| Product Hunt | Yeni uygulama lansmanlari, upvote sayilari, erken kullanici yorumlari | ✅ Yuksek | Kategori bazli arama. Upvote sayisi ilgi gostergesi. Yorumlar kalite gostergesi. |
| IndieHackers | Indie gelistirici gelir raporlari, basari/basarisizlik hikayeleri | ✅ Yuksek | Gelir kaniti icin en iyi kaynak. Gelistiriciler gercek rakamlarini paylasir. |
| AlternativeTo | Rakip listeleri, kullanici tercihleri, alternatif arayanlar | ⚠️ Orta | Bir uygulamaya alternatif arayan kullanici sinyali. Hangi ozelliklerin onemli oldugu gorulur. |
| G2 / Capterra | B2B uygulama review'lari, detayli karsilastirmalar | ✅ Yuksek | Daha cok B2B/SaaS icin. Profesyonel kullanici gorusleri. |
| Trustpilot | Kullanici sikayetleri, genel memnuniyet | ⚠️ Orta | Negatif bias var — memnun kullanicilar genelde yorum yazmaz. Sikayet kaliplari icin degerli. |
| Quora | Soru-cevap formati, kullanici ihtiyaclari | ⚠️ Orta | Insanlarin hangi problemlere cozum aradigini gosterir. |
| Discord serverlari | Topluluk tartismalari, gercek zamanli feedback | ⚠️ Orta | Niche topluluklarin nerede aktif oldugunu bulmak gerekir. |
| App Store 1-2 yildiz review'lar | Spesifik sikayet kaliplari, eksik ozellikler | ✅ Yuksek | En degerli pazar arastirmasi verilerinden biri. Ne eksik, ne kirik, ne sinir bozucu. |
| App Store 4-5 yildiz review'lar | Kullanicilarin en cok sevdigi ozellikler | ✅ Yuksek | Must-have ozellikleri anlamak icin. |

---

## 4. GELIR TAHMINLERI

> **KRITIK BOLUM:** Gelir verisi, app pazar arastirmasinin en yaniltici alanidir. Asagidaki tabloyu dikkatle okuyun.

| Kaynak | Ne Verir | Guvenilirlik | UYARI |
|---|---|---|---|
| Sensor Tower (gelir tahmini) | Aylik gelir tahmini (USD) | ⚠️ DUSUK | 3. parti MODEL, gercek veri degil. %50+ hata payi olabilir. Kucuk uygulamalarda tamamen yanlis olabilir. |
| data.ai (gelir tahmini) | Aylik/yillik gelir tahmini | ⚠️ DUSUK | Ayni sorun — model bazli tahmin. Enterprise fiyat odeyip de yanlis veri alabilirsiniz. |
| App Store "Top Grossing" listesi | Siralama (1, 2, 3...) | ⚠️ Orta | Siralama gorursun, rakam gormezsin. Siralamanin gelire donusumu bilinmez. |
| IndieHackers gelir raporlari | Gercek gelir rakami (dev kendisi bildiriyor) | ✅ YUKSEK | Gelistirici kendi raporluyorsa en guvenilir kaynak. Ama herkes paylasmaz. |
| Twitter #buildinpublic | Gelir screenshot'lari, MRR paylasimi | ⚠️ Orta | Dogrulanmasi zor ama genelde dogru. Basarili olanlarin paylasma egilimi daha yuksek (survivorship bias). |
| RevenueCat blog / benchmark | Benchmark verileri, ortalama churn, conversion rate'ler | ✅ Yuksek | Kendi platformlarindaki aggregate veriler. Industri ortalamalari icin en guvenilir. |
| Superwall blog / benchmark | Paywall conversion rate verileri | ✅ Yuksek | Kendi musterilerinden aggregate veri. |
| Pazar arastirma raporlari (Grand View, Mordor, vb.) | "$XB pazar buyuklugu", "CAGR %Y" | ❌ DUSUK | Metodolojisi opaque. KANIT: Menopoz uygulamasi pazar arastirmasi $4.2B buyukluk tahmini yapiyordu, ancak lider uygulamanin sadece 890 rating'i vardi. Bu dengesizlik, raporlarin gerceklikten ne kadar kopuk olabilecegini gosterir. |
| Crunchbase / funding verileri | Ne kadar yatirim almis | ⚠️ Orta | Yatirim almis olmak gelir anlamina gelmez. Ama "bu alana para akiyor" sinyali verir. |

**ALTIN KURAL:** Gelir tahminlerinde her zaman %50 hata payi kabul edin. Eger bir aracin verdigi rakamla karar verecekseniz, o rakami yarilayip hala mantikli mi diye sorun.

**GUVENILIRLIK SIRASI (gelir icin):**
1. Gelistiricinin kendisinin paylastigi gercek rakam (IndieHackers, blog, Twitter)
2. RevenueCat/Superwall benchmark verileri (industri ortalamalari)
3. App Store rating sayisindan ters muhendislik (kaba tahmin: rating x 100 = indirme, conversion %2-5)
4. Sensor Tower / data.ai tahminleri (son care)
5. Pazar arastirma raporlari (neredeyse hicbir zaman guvenilir degil)

---

## 4.5 REKLAM ISTIHBARATI (AD LIBRARY) KAYNAKLARI

> Regulasyon geregi acilan ucretsiz reklam kutuphaneleri, rakiplerin paid UA davranisini dogrudan gozlemlemeyi saglar.
> En degerli sinyal: reklam LONGEVITY'si — aylardir kesintisiz donen reklam, calisan unit economics'in DAVRANIS kanitidir (Mom Test uyumlu).
> **ERISIM:** Ucu de WebFetch ile OKUNAMAZ (2026-06'da test edildi: FB baglantiyi keser, Google/TikTok bos JS kabugu doner).
> Birincil yol browser otomasyonu (Claude in Chrome); yoksa WebSearch dolayli (TAHMINI). Detayli sorgu sablonlari: `data-collection-protocol.md` Faz 4 Adim 8.

| Kaynak | Arama | Login | Ne Verir | Guvenilirlik | Okuma Yontemi |
|---|---|---|---|---|---|
| FB (Meta) Ad Library | Keyword + advertiser | Gerekmez (politik reklamlar haric) | Aktif reklam sayisi, baslama tarihi, kreatif metin/medya, versiyon sayisi, landing domain | ✅ Yuksek (KESIN — dogrudan gozlem) | Browser + get_page_text |
| Google Ads Transparency Center | SADECE advertiser/domain (keyword YOK) | Gerekmez | Rakibin tum Google/YouTube reklamlari, ~toplam sayi, dogrulanmis tuzel kisi, format/zaman filtreleri | ✅ Yuksek (KESIN) | Browser + SCREENSHOT (get_page_text bos doner) |
| TikTok Creative Center (Top Ads) | Keyword + sektor (login ile) | Login'siz SINIRLI onizleme; tam erisim ucretsiz Business hesabi ister | Top reklam kreatifleri, Likes, CTR yuzdelik dilimi, Budget kademesi | ⚠️ Orta (reklamveren onayli "top" alt kume — tam liste degil) | Browser (login'li oturum onerilir) |

**Sinirlar (durust degerlendirme):**
- Harcama TUTARI hicbir kaynakta gorunmez (FB'de EU reach araliklari haric). Tutar tahmini = DUSUK etiket → puan MAX 3.
- Apple Search Ads'in kamuya acik kutuphanesi YOK → iOS install reklamlarinin onemli kanali kor noktadir. Raporda acikca not et.
- FB keyword aramasi genis esleme yapar; alakasiz sektor reklamlari karisir (elle ayiklama gerekir).
- TikTok "Top Ads" reklamveren onayli alt kumedir; "TikTok'ta reklam yok" sonucu TikTok CC'den TEK BASINA cikarilamaz.
- Anlik goruntudur; gecmis kampanya arsivi sinirlidir.

**Sinyal degeri:**
1. **Longevity:** 6+ ay kesintisiz reklam = calisan ekonomi (sirket olceginde; indie gelir kaniti YERINE GECMEZ — `scoring-model.md` Gelir Kaniti notu)
2. **Kreatif yogunluk:** Pazar parasallasmasi + paid kanal doygunlugu (Dagitim Fizibilitesi girdisi)
3. **Mesaj acilari:** Kullanilan ve KULLANILMAYAN acilar → adlandirilmis icgoru + ASO/positioning girdisi
4. **Sessizlik:** Hicbir rakip reklam vermiyorsa paid UA dogrulanmamis demektir — bu da veridir ("bulunamadi da veridir" kurali)

---

## 5. CLAUDE / AI YETENEKLERI

> Bu bolum, Claude'un pazar arastirmasinda neler yapabilecegini ve yapamayacagini durust sekilde dokumante eder.

| Yetenek | Durum | Sinirlamalar |
|---|---|---|
| Web Search | ✅ Var | Claude web search tool ile gercek zamanli arama yapabilir. Google sonuclarina erisir. |
| App Store sayfasi okuma | ✅ Var (web fetch) | Rating sayisi, fiyat, description, in-app purchase listesi okunabilir. Ancak sayfanin tamamini her zaman tam cekmeyebilir. |
| Reddit thread okuma | ✅ Var (web fetch) | Spesifik URL verilirse thread icerik okunabilir. Arama sonuclari uzerinden de gidilebilir. |
| Product Hunt sayfasi okuma | ✅ Var (web fetch) | Urun sayfalari, upvote sayisi, yorumlar okunabilir. |
| IndieHackers profili okuma | ✅ Var (web fetch) | Gelir raporlari, gelistirici profilleri okunabilir. |
| Google Trends karsilastirma | ⚠️ Sinirli | Web uzerinden erisim mumkun ama interaktif grafikleri tam okuyamayabilir. |
| Gercek zamanli indirme verisi | ❌ Yok | Hicbir 3. parti API entegrasyonu yok. Bu veri Apple tarafindan gizli tutulur. |
| Gercek zamanli gelir verisi | ❌ Yok | Mumkun degil. Bu veri tamamen gizlidir. Sadece gelistiricinin kendisi bilir. |
| App Store icerisinde arama | ⚠️ Sinirli | Web uzerinden dolaylidir. Native App Store arama kadar kapsamli ve dogru degil. |
| Gecmis veri / trend analizi | ❌ Yok | Anlik snapshot alinabilir ama gecmis verilere erisim yok. "3 ay once rating kacti?" sorusuna cevap verilemez. |
| Keyword difficulty skoru | ❌ Yok | Apple API'ye dogrudan erisim yok. ASO araclarina erisim yok. |
| Kategori siralama gecmisi | ❌ Yok | Anlik siralama gorulur, gecmis trend gorulmez. |
| Reklam istihbarati (ad library) | ⚠️ Kismi | Browser otomasyonu ile FB Ad Library (keyword+advertiser) ve Google ATC (sadece advertiser) okunur: kreatifler, baslama tarihleri, aktif reklam sayilari. WebFetch ile OKUNAMAZ. Harcama TUTARI hicbir kaynakta gorunmez. Bkz. Bolum 4.5. |
| Bulk veri toplama | ⚠️ Sinirli | Tek tek sayfa okuyabilir ama 100 uygulamayi otomatik taramak pratik degil. |

**CLAUDE ILE EN IYI YAPILABILECEKLER:**
- App Store sayfalarindan rating/fiyat/description toplama
- Reddit'te kullanici sikayeti ve goc sinyali arama
- Rakip uygulamalarin review'larini analiz etme
- Google Trends ile ilgi karsilastirmasi
- IndieHackers/Product Hunt'ta gelir kaniti arama
- Ad library taramasi (browser otomasyonu bagliysa): rakip kreatifleri, baslama tarihleri, aktif reklam sayilari (Bolum 4.5)
- Toplanan tum verileri yapilandirilmis sekilde analiz etme ve puanlama

**CLAUDE ILE YAPILAMAYACAKLAR:**
- Kesin indirme/gelir rakami verme
- Gecmis trend analizi
- Keyword difficulty skoru hesaplama
- Bulk uygulama taramasi
- Reklam harcama TUTARI gorme (kreatif/longevity GORULUR — Bolum 4.5; tutar hicbir kaynakta yok)

---

## 6. VERI GUVENILIRLIK MATRISI (OZET)

| Veri Turu | En Guvenilir Kaynak | Guvenilirlik | Alternatif Kaynak |
|---|---|---|---|
| iOS Rating sayisi | App Store (direkt) | ✅ Kesin | Google "site:apps.apple.com" |
| Yildiz puani | App Store (direkt) | ✅ Kesin | - |
| Fiyat modeli | App Store (direkt) | ✅ Kesin | - |
| In-app purchase listesi | App Store (direkt) | ✅ Kesin | - |
| Son guncelleme tarihi | App Store (direkt) | ✅ Kesin | - |
| Uygulamanin yasam durumu | Guncelleme sikligi + rating trend | ✅ Yuksek | Reddit'te kullanici yorumlari |
| Aylik indirme sayisi | data.ai / Sensor Tower | ⚠️ Tahmin (%30-50 hata) | AppMagic, Google Play indirme araligi (Android icin) |
| Aylik gelir | IndieHackers (dev raporu) | ✅ (varsa) | Sensor Tower (tahmin, dusuk guvenilirlik) |
| Keyword hacmi / popularity | Apple Search Ads | ⚠️ Orta (2025 degisimi) | Google Trends (dolayli), App Store Search Suggest |
| Keyword difficulty | ASO araclari (AppTweak, vb.) | ⚠️ Dusuk-Orta | Rakip rating sayisindan ters muhendislik |
| Pazar buyuklugu | Birden fazla kaynak karsilastirmasi | ⚠️ Dusuk | App Store rating ile cross-check |
| Kullanici memnuniyetsizligi | Reddit + App Store 1-2 star reviews | ✅ Yuksek | Twitter, AlternativeTo, forums |
| Kullanici goc sinyali | Reddit ("alternative" aramalari) | ✅ Yuksek | AlternativeTo, Google Trends karsilastirma |
| Rakip ozellik listesi | App Store description + screenshot | ✅ Yuksek | Rakibin web sitesi |
| Conversion rate benchmark | RevenueCat / Superwall blog | ✅ Yuksek | IndieHackers raporlari |
| Churn rate benchmark | RevenueCat blog | ✅ Yuksek | - |
| Rakip reklam aktivitesi (kreatif, longevity) | FB Ad Library (browser otomasyonu) | ✅ Yuksek (KESIN — dogrudan gozlem) | Google ATC (advertiser bazli), WebSearch dolayli (TAHMINI) |

---

## 7. ARASTIRMA IPUCLARI

### Genel Prensipler

- **App Store'da bir uygulamanin rating sayisi, pazar buyuklugu raporlarindan daha guvenilir bir talep gostergesidir.** 10K+ rating = kanitlanmis talep. 100 rating = niche veya erken asama.

- **Pazar arastirma firmalarinin "milyar dolarlik" projeksiyonlarina korkorune guvenmeyin.** Menopoz uygulamasi orneginde $4.2B pazar tahmini vardi, ama lider uygulamanin sadece 890 rating'i vardi. Pazar "buyuk" olabilir ama dijital uygulama olarak yakalanmamis olabilir.

- **Indie gelir kaniti her zaman pazar raporu tahminlerinden daha degerlidir.** Bir indie gelistirici "ayda $5K kazaniyorum" diyorsa, bu $5B pazar buyuklugu raporundan daha bilgilendiricidir.

- **Revenue tahminlerinde %50 hata payi kabul edin.** Sensor Tower $100K diyorsa, gercek $50K-$200K arasinda herhangi bir yer olabilir.

### Spesifik Arama Taktikleri

- **Reddit goc sinyali arama:** `[uygulama adi] alternative` veya `leaving [uygulama]` veya `switched from [uygulama]` arama terimleri kullanin. Sonuclarin tarihi onemli — son 1 yil icindekiler daha anlamli.

- **Rating-indirme ters muhendislik:** Rating sayisi x 100 = kaba indirme tahmini. Bu cok kaba bir tahmindir ama ucretsiz ve aninda yapilabilir. Ornek: 5K rating ≈ 500K toplam indirme.

- **Mevsimsellik kontrolu:** Google Trends'te arama terimini son 5 yillik gosterin. Mevsimsel dalgalanma var mi? Yukselen mi dusen mi trend?

- **"Dead app" kontrolu:** Son guncelleme 1 yildan eski + dusuk recent rating = terk edilmis uygulama. Bu bir firsat olabilir.

- **Review mining:** 1-2 yildiz review'larda tekrar eden sikayetlari cikartin. Bu sikayetler sizin icin feature listesi olur.

- **Fiyat arastirmasi:** Benzer uygulamalarin fiyat modellerini karsilastirin. Cogunluk subscription mi, one-time mi, freemium mi? Bu size fiyatlama stratejisi verir.

### Yanilgidan Kacinma

- **Survivorship bias:** IndieHackers ve Twitter'da sadece basarili insanlar paylasim yapar. Basarisiz olanlari gormezsiniz. Bunu hesaba katin.

- **Buyuk pazar yanilgisi:** "Pazar buyuk" demek "ben de kazanirim" demek degildir. Kucuk ama net bir niche, buyuk ama belirsiz bir pazardan iyidir.

- **Rating enflasyonu:** Uygulamalar kullanicilara rating istegi gonderir (genelde uygulama ici pop-up). Bu, rating'leri yukari cikarabilir. 1-2 star review'larin icerigine rating ortalamasindan daha fazla dikkat edin.

- **"Rakip yok" yanilgisi:** App Store'da rakip bulamiyorsaniz, muhtemelen pazar yok demektir — kendiniz dahiyseniz degil. Her zaman en az dolayli rakipler olmalidir.

---

## 8. HIZLI KONTROL LISTESI

Her arastirma fazi icin hangi araclarin kullanilacagi:

| Faz | Birincil Arac | Ikincil Arac | Claude Yapabilir mi? |
|---|---|---|---|
| Faz 1: Problem Havuzu | Reddit, App Store 1-2 star reviews | Twitter/X, niche forumlar, Quora | ✅ Web search ve web fetch ile |
| Faz 2: Keywords | App Store Search Suggest, Google Trends | Apple Search Ads, Google Keyword Planner | ⚠️ Kismi (Search Suggest ve Trends icin web erisim var, ASA icin yok) |
| Faz 3: Hizli Tarama | App Store (direkt sayfa okuma) | AppMagic (ucretsiz tier) | ✅ Web fetch ile App Store sayfalari okunabilir |
| Faz 4: Rakip Analizi | App Store + Reddit reviews | Sensor Tower (sinirli free), AlternativeTo | ✅ Web fetch ile App Store ve Reddit okunabilir |
| Faz 5: Puanlama | Faz 3-4'te toplanan veriler | - | ✅ Tam — Claude veri analizi ve puanlama yapabilir |
| Faz 6: Deep Dive | App Store reviews (tum yildizlar), Reddit threads | IndieHackers, Product Hunt | ✅ Web fetch ile detayli okuma yapilabilir |
| Faz 7: Dogrulama | IndieHackers (gelir kaniti), Reddit, App Store | Product Hunt, Twitter #buildinpublic | ✅ Web search ve web fetch ile |
| Faz 8: Karsilastirma | Tum onceki fazlardaki veriler | - | ✅ Tam — Claude karsilastirma analizi yapabilir |
| Faz 9: Go/No-Go | Tum fazlarin ozeti | - | ✅ Tam — Claude karar matrisi olusturabilir |
| Faz 10: Devil's Advocate | Tum kaynaklar, ters perspektif | - | ✅ Tam — Claude her fikre karsi arguman uretebilir |

---

## 9. KAYNAK KONTROL FREKANSI

| Kaynak | Ne Siklikla Kontrol Edilmeli | Neden |
|---|---|---|
| App Store rating/review | Her arastirma basinda | Rating sayisi ve yorumlar zamanla degisir |
| Google Trends | Arastirma basinda + mevsim kontrolu | Trendler degisir, mevsimsellik onemli |
| Reddit | Her arastirma basinda | Yeni thread'ler surekli acilir |
| Ad library (FB/Google ATC) | Her arastirma basinda | Aktif reklamlar ve kreatifler surekli degisir; anlik goruntu |
| Sensor Tower / data.ai | Ayda 1 (ucretli planla) | Tahminler guncellenir |
| IndieHackers | Ceyreklik | Gelir raporlari genelde aylik/ceyreklik paylasilir |
| Pazar arastirma raporlari | Yilda 1 (varsa) | Nadiren guncellenir, nadiren guvenilir |

---

## 10. SON SOZ: DURUST DEGERLENDIRME

**Gercekten guvenebileceginiz veriler:**
- App Store'daki rating sayisi, yildiz puani, fiyat, description, guncelleme tarihi
- Reddit ve App Store review'larindaki kullanici sikayetleri
- IndieHackers'da gelistiricinin kendisinin paylastigi gelir rakamlari
- Google Trends'teki genel ilgi trendi
- RevenueCat/Superwall benchmark verileri

**Tuz ile alinmasi gereken veriler:**
- Sensor Tower / data.ai indirme ve gelir tahminleri
- ASO araclarinin keyword difficulty skorlari
- Apple Search Ads popularity skorlari (2025 sonrasi degisim)
- Twitter'daki gelir paylasimi (dogrulanmasi zor)

**Neredeyse hic guvenilmemesi gereken veriler:**
- Pazar arastirma firmalarinin milyar dolarlik pazar buyuklugu tahminleri
- "CAGR %XX" projeksiyonlari
- Rakipsiz gibi gorunen pazarlar (muhtemelen pazar yoktur)

**Altin kural:** Birden fazla bagimsiz kaynak ayni seyi soyluyorsa, guvenilirlik artar. Tek bir kaynaga dayanarak karar vermeyin. Cross-check her zaman yapin.
