# Veri Toplama Protokolu — v4.0

> Her gozlem `data/evidence.jsonl` icine yazilir. Alan ve derece kurallari icin
> `evidence-model.md` yetkilidir.

## Genel Kurallar

1. Once claim yaz, sonra o claim'i destekleyen ve curuten kaniti ara.
2. Gozlem kalitesi ile claim relevance'i ayri kaydet.
3. URL sayisi degil `independence_root` sayisi kullan.
4. Her zaman tarih, geo, storefront ve platform baglamini koru.
5. Zaman-duyarli veriyi arastirma gunu yeniden kontrol et.
6. Bulunamayan veride asagidaki Yokluk Protokolu'nu uygula: karar-kritik alanda
   sinirli arama ve acik kayit, kozmetik alanda tek tarama.
7. AI/sentetik ciktisini evidence olarak degil hipotez olarak kullan.
8. Karsit kanit sorgusu yapmadan claim derecesini kapatma.

## Preflight

Su sorular cevaplanmadan aramaya baslama:

- Hedef segment kim ve sonucun hangi geo/storefront'ta gecerli olmasi gerekiyor?
- Urun turu (`product_type`) `app`, `web_saas` veya `service` mi? Toplama kapsamini
  bu belirler (asagida); arketip ve agirliklari degistirmez.
- Urun store/web/yerel arama-led mi, community/sales/partnership-led mi?
- Birincil arketip hangisi?
- Regulated, sensitive data, AI variable cost, hardware, children veya platform
  dependency modifier'i var mi?
- Bu analiz desk, prebuild veya post-MVP asamasinda mi?

## Urun Turu ve Toplama Kapsami

`data/assessment.json` icindeki zorunlu `product_type` (`app` | `web_saas` |
`service`) yalniz hangi kaynaklarin toplanacagini belirler. Arketip secimi, boyut
agirliklari, fatal gate'ler ve karar esikleri `scoring-model.md`'deki ayni
arketiplerden gelir; ornegin bir `b2b_prosumer` fikri app, web SaaS veya hizmet
olarak ayni agirliklarla puanlanir.

| Toplama alani | `app` | `web_saas` | `service` |
|---|---|---|---|
| Liste ve metadata | App Store/Play metadata | Fiyat sayfasi, plan/limit, deneme/demo, entegrasyonlar | Saglayici (lisans, konum, hizmet alani), teklif paketi ve fiyati |
| Musteri kaniti | Rating count, indirme bandi | Aciklanan musteri/logo/vaka calismasi | Rezervasyon/teklif davranisi, yerel listeler |
| Guven ve uyum | Privacy label, store kurallari | Guvenlik/uyum sayfasi (SOC 2, ISO 27001, SSO, DPA), veri barindirma | Lisans/izin, sigorta, sozlesme/garanti, teslim sorumlulugu |
| Satis hareketi | Store aramasi, paywall | Self-serve veya demo/satis ekibi, sozlesme suresi | Teklif/rezervasyon akisi, teslim suresi, kapasite |
| Review mining (Standard/Deep) | App Store/Play yorumlari | Ucuncu taraf review platformu (G2, Capterra, TrustRadius) | Google Business Profile, Yelp, Trustpilot, marketplace yorumlari |
| Arama gorunurlugu (Deep'te ayrica) | ASO | SEO, karsilastirma/inceleme siteleri | Yerel arama, harita ve rehber listeleri |

`web_saas` ve `service` icin App Store/Play metadata, store review ve ASO gorevleri
zorunlu degildir ve aranmaz. Bir rakip ayrica app olarak yayindaysa o rakibin store
bilgisi profil satirina eklenebilir; bu, store gorevlerini zorunlu kilmaz. Atlanan
gorevler sessiz kalmaz: analiz basina bir acik kayit yazilir:

- `claim_id=<prefix>-collection-scope`, `status=not_applicable`, `phase=3`
- `source_type=local_artifact`, `source_ref=data/assessment.json#product_type`
- `evidence_level=E0`, `observation_quality=direct`, `claim_relevance=weak`,
  `direction=neutral`
- `observation`: hangi gorevlerin (store metadata, store review, ASO) neden kapsam
  disi oldugu; `search_queries` ve `attempted_sources` bos

Bu kayit yokluk veya karsit kanit degildir; hicbir boyuta puan vermez. Raporda
Kanitin sinirlari bolumunde bir cumleyle anilir.

## Yokluk Protokolu

**Karar-kritik** alan veya claim: bir fatal gate'i, puanlanan bir boyutun claim'ini,
en riskli uc varsayimdan birini veya karari degistirebilecek olandir. Bunlarda:

1. En az 3 sorgu varyanti ve en az 2 farkli kaynak ailesi dene (ornek: web aramasi +
   resmi kayit/store/review platformu).
2. Ilk uc sorgu yeni bir iz (yeni terim, kaynak veya belge) gosterirse en fazla bir
   takip sorgusu yap; iz yoksa dur.
3. Hala bulunamadiysa `not_found_after_protocol` kaydini `search_queries` ve
   `attempted_sources` ile yaz, claim derecesini buna gore birak ve kalan belirsizligi
   masa basi aramayi uzatmak yerine RAT/deney planina tasi.
4. Erisim duvari, hesap veya giris gerekiyorsa `structurally_unobservable` yaz.

**Kozmetik** alan: hicbir skor, gate veya RAT varsayimini degistirmeyen profil
ayrintisidir (ornek: merkez sehri, calisan araligi, kurulus ayi). Sirketin kendi
sitesi ve bir standart kaynakla (resmi kayit, LinkedIn, Crunchbase) tek tarama
yapilir; bulunamazsa raporda hucre "bulunamadı" olur ve eksik alan ilgili profil
kaydinin `limitations` dizisine yazilir. Kozmetik alan icin ayri arama zinciri
veya ayri `not_found_after_protocol` kaydi gerekmez. Bir profil alani bir claim'e
dayanak olursa (ornek: aciklanan gelir monetizasyon claim'inde) karar-kritik
sayilir.

## Faz 3: Hizli Pazar Taramasi

### 1. Rakip ve ikame bul

Arama ornekleri (urun turune gore secilir; ikame aramalari her turde yapilir):

- app: `site:apps.apple.com [keyword] app`, `best [job to be done] app`
- web_saas: `[job to be done] software pricing`, `site:g2.com [category]`,
  `[competitor] alternatives`
- service: `[service] near [city]`, `[service] cost [geo]`, `[service] provider
  reviews`
- tum turler: `[problem] spreadsheet template`,
  `[problem] service OR consultant OR manual workflow`,
  `site:reddit.com [problem] what do you use`

En yuksek rating'i otomatik "pazar lideri" yapma. Segmentin ayni isini cozen app,
web urunu, hizmet veya manuel workflow'u ayri kaydet.

### 2. Liste ve metadata

`app` icin her store kaydinda:

- tam URL
- storefront/country ve platform
- rating count + star rating
- fiyat/IAP
- ilk yayin veya bilinen app yasi
- son guncelleme
- incelenen tarih

Rating `E2/direct observation/supporting relevance`dir. Talep claim'i icin ikinci
bagimsiz davranis sinyali gerekir.

`web_saas` icin her rakipte: fiyat sayfasi URL'si, plan/limitler, deneme veya demo
zorunlulugu (self-serve mi satis ekibi mi), aciklanan musteri/logo/vaka calismasi,
guvenlik/uyum sayfasi (SOC 2, ISO 27001, SSO, DPA, veri barindirma), entegrasyonlar
ve incelenen tarih. Ucuncu taraf review platformu puani ve sayisi `E2/supporting`
proxy'dir; rating gibi fatal gate degildir.

`service` icin her saglayicida: saglayici kimligi (lisans/sertifika, konum, hizmet
alani), teklif paketi ve fiyat/teklif yontemi, teslim suresi ve kapasite sinyali,
rezervasyon/teklif akisi, yerel review sayisi ve puani (Google Business Profile,
Yelp, Trustpilot veya marketplace) ve incelenen tarih.

Non-app turlerde store metadata yerine bu alanlar toplanir; atlanan store gorevleri
icin Urun Turu bolumundeki `not_applicable` kaydi yazilir.

### 3. Trend ve lifecycle

Dogru Google Trends erisimi yoksa dolayli makale sonucunu `estimated/inferred`
olarak kaydet. Lifecycle'i Exploding/Regular/Peaked ve buyume seklini ayri yaz.
Trend claim'inde yayin tarihi ile kapsanan veri donemini karistirma.

### 4. Geo ve dagitim

Hedef geo basina:

- arama sonucu ve autocomplete: `app` icin store search; `web_saas` icin web
  aramasi ve karsilastirma/inceleme siteleri; `service` icin yerel arama, harita ve
  rehber listeleri
- `app`: Apple Ads popularity/Insights kullanildiysa olcek baglami (1-5 veya 1-100)
- top result profili
- watering-hole ve sales/community kanallari
- paid channel rekabeti
- localization, odeme ve regulator risk

Keyword difficulty tek basina rating'den uretiliyorsa `inferred/weak` kalir.

### 5. Pazar buyuklugu (Standard/Deep)

Tek bir "pazar buyuklugu" rakami uretme; olculebilen parcalari ve dagilimi kaydet:

- En az 3 farkli yayincinin tahmini: rakam, baz yil, buyume orani, cografya ve
  kapsam tanimi. Ayni yazar/editor kadrosunu paylasan yayincilar tek
  `independence_root`'tur. Arastirma sirketi tahmini `third_party_estimate`,
  `E1`, `weak`. Ucretli raporun yalniz ozeti okunduysa `limitations` icine yaz.
- Daha saglam dayanaklar: resmi dosyalar (SEC 10-K/S-1 vb.), sirketin acikladigi
  gelir/abone/kullanici, regulator kayit sayilari.
- Talep tarafi davranis sayilari (kayit, talep, kullanim) ve ulusal temsili
  anketler; kisi sayisi ile talep sayisini karistirma.
- Hesaplanamayanlar listesi.

Kayit: tahmin, gelir ve kayit sayilari `claim_id=<prefix>-market-size`,
`direction=neutral`; davranis ve anket sayilari talep claim'ine. Yazarin kaba
cikarimi raporda "yazarın yorumu, kaba çıkarım" diye etiketlenir.

## Faz 4: Rakip ve Davranis Analizi

### Rakip kapsami

| Mod | Rakip/ikame ve profil | Reklam kutuphanesi | Stratified review | Organik kanal |
|---|---|---|---|---|
| Quick | top 5 | top 3, Meta + Google ATC var/yok | yok | yok |
| Standard/Deep | top 10 | top 5, Meta + Google ATC + TikTok | top 5 | var |
| Compare | her aday icin Quick ile ayni | Quick ile ayni | yok | yok |

Compare adaylari arasinda kapsam farki yaratilmaz; bir adaya Standard toplamasi
eklenirse o aday Compare satiri degil, ayri Standard analizidir.

App rakibi yoksa manual workflow, web urunu ve service competitor'lari listeye
dahil et. `web_saas` ve `service` fikirlerinde bu ikameler listenin dogal
parcasidir.

### Rakip profili

Quick'te top 5, Standard/Deep'te top 10 rakip/ikame icin (Compare: her aday top 5):

- sirket kurulus yili ve bu urunun/ozelligin baslangic tarihi
- merkez, sahiplik/ana sirket, fonlama veya satin alma
- calisan sayisi veya araligi ve kaynagi (resmi dosya, sirket sayfasi, LinkedIn
  araligi)
- aciklanan kullanici, musteri veya gelir
- platformlar (iOS, Android, web, tarayici eklentisi) veya `service` icin hizmet
  kanali (yerinde, uzaktan, web) ve ulke/hizmet alani kisitlari
- reklam edilen kapsam (site/ozellik sayisi) ile otomatik calisan kapsam farki
- sirketin kendi yazdigi sinirlar (yapmadigi isler)

Kayit: `claim_id=<prefix>-competitor-profile`, `direction=neutral`, `phase=4`.
Sirketin kendini anlatmasi `E1`; resmi dosya veya dogrudan gozlem `E2`. Profil
alanlari varsayilan olarak kozmetiktir: Yokluk Protokolu'ndaki tek tarama
uygulanir, bulunamayan alan tabloda "bulunamadı" ve kaydin `limitations` dizisinde
yer alir. Bir alan skor, gate veya RAT claim'ine dayanak olursa karar-kritik
protokol ve `not_found_after_protocol` kaydi uygulanir. Raporda `report-writing.md`
§10 tablolarina girer.

### Bagimsiz basari olcumleri (Standard/Deep)

Rakiplerin isi ne kadar iyi yaptigini olcen kaynaklari ayri ara ve ayri yaz:

1. Test kurulusu ve akademik calisma: yontem, orneklem, donem.
2. Basin testi: kendi olcumu mu, rakibin panosundaki sayiyi mi aktariyor; satis
   ortakligi baglantisi var mi.
3. Sirketin kendi veya yaptirdigi olcum: `E1`, raporda "şirket beyanı".

Olcum, kullanicinin sikayet ettigi sonuca gore secilir (ornek: "kaldirildi"
sayisi mi, gercek kaldirma mi). 12 aydan eski olcum `weak` relevance alir.

### Stratified review mining (Standard/Deep)

Quick ve Compare'de stratified review orneklemi toplanmaz ve tema frekansi
raporlanmaz; problem kaniti community ve davranis sinyalinden gelir. Quick'te tek
bir yorum alintilanirsa tekil gozlem olarak etiketlenir ve genellenmez.

Standard/Deep'te top 5 rakip icin, kaynak urun turune gore secilir:

- `app`: App Store/Play yorumlari; storefront ve app version kaydedilir
- `web_saas`: ucuncu taraf review platformu (G2, Capterra, TrustRadius); platform,
  ulke/listing URL'si ve tarih kaydedilir
- `service`: Google Business Profile, Yelp, Trustpilot veya marketplace yorumlari;
  platform, listing URL'si, konum/hizmet alani ve tarih kaydedilir

Her turde ayni orneklem kurali:

- hedef 30, erisim sinirliysa min 15 review
- 1-2, 3 ve 4-5 yildizdan min 5'er
- son 12 ay
- tema, star, tarih, kaynak URL ve evidence ID

Platform yildiz filtresi sunmuyorsa okunan yorumlar kendi yildizina gore
tabakalanir. Yildiz tabakasi hic yoksa veya bir tabaka 5'e ulasmiyorsa eksik tabaka
erisim duvarinda `structurally_unobservable`, protokolden sonra yetersiz yorumda
`not_found_after_protocol` olarak kaydedilir; eksik tabaka baska kaynaktan
uydurulmaz.

Tema frekansi `tema kaydi / incelenen review` olarak raporlanir. Orneklem random
degilse genelleme yapilmaz. Pozitif review'lar kullanicinin gercekten deger verdigi
ozellikleri; 3-star review'lar tradeoff'u gosterir. Satici tarafindan secilmis
vaka calismasi veya logo duvari review orneklemine girmez; sirket beyanidir.

### Community/JTBD

Min 3 sorgu ailesi:

- sikayet/push: `[problem] frustrating reddit`
- alternatif/pull: `[competitor] alternative reddit`
- gecis/anxiety/habit: `switched from [competitor]`, `why I came back`

Post veya yorumun varligi dogrudan gozlemdir; toplulugun tumunu temsil ettigi
cikarimi weak olabilir. Gecmis para/zaman harcamasi ile gelecekteki niyeti ayir.

### Gelir ve odeme

Kaynak sirasi:

1. First-party proceeds/transaction
2. Kapanmis satis/exit veya dogrulanabilir odeme
3. Kurucu beyanli revenue
4. Third-party estimate
5. Vendor/marketing iddiasi

Canli ilan ile kapanmis satisi ayir. Gelir bulunamazsa arama protokolunu kaydet;
"gelir yok" sonucu cikarma. Ads longevity monetizasyon sinyali olabilir fakat indie
geliri veya profit kaniti degildir.

### Ad/channel intelligence

Kapsam: Standard/Deep'te review mining ile ayni top 5 rakip ve kategori ifadesiyle
1-2 keyword aramasi (yeni girisleri yakalamak icin); asagidaki uc adimin hepsi.
Quick'te ve Compare adaylarinda top 3 rakip icin yalniz adim 1-2 (Meta Ad Library
ve Google Ads Transparency Center): var/yok, aktif sayi ve hedef URL turu; TikTok,
keyword aramasi ve mesaj acisi kodlamasi yok. Kayit kurallari
(`source_type=ad_library`, kok, artifact, seviye) `tools-and-data-sources.md`
icindedir; `phase` degeri `4`tur.

Her rakip icin sirayla:

1. Meta Ad Library: reklamveren sayfasi (`search_type=page`, `view_all_page_id`),
   `country=` hedef geo, `active_status=active`, `ad_type=all`. Gosterilen toplam
   `denominator`, incelenen kart sayisi `sample_n`.
2. Google Ads Transparency Center: `domain=` sorgusu, `region=` hedef geo, `hl=en`
   (TR IP'sinden arayuz Turkce acilir; sayi "~300 reklam" yerine "~300 ads" okunur).
   "Any time" ve "Last 30 days" (`preset-date=Last+30+days`) sayilarini ayri yaz.
3. TikTok: TikTok for Business girisi varsa Creative Center Top Ads, bolge = hedef
   geo, son 30 gun; yoksa denenen URL ile `structurally_unobservable`.

Her kayitta gozlenen alanlar: aktif reklam sayisi (gosterildigi gibi, `~` kabul),
baslangic tarihi araligi ve kumelenme, format dagilimi, hedef URL turu (`app`: App
Store / Play / web; `web_saas`: ana sayfa, fiyat, deneme veya demo formu;
`service`: rezervasyon, teklif formu veya telefon), mesaj acilari
(`kodlanan/incelenen` oraniyla; Standard/Deep), teklif/fiyat/indirim
kodu, creator/affiliate payi, rakip adina bidding. Her gozlem bir screenshot ile
`data/artifacts/ads/` altina kaydedilir.

Sonuc yoksa: "No ads match" veya 0 reklam `not_found_after_protocol`;
`search_queries` icine reklamveren dropdown, exact keyword ve domain sorgularini
yaz. Giris duvari `structurally_unobservable`.

Tablo: Standard/Deep'te `phases/02-competitor-analysis.md` icinde
`## Ad/Channel Intelligence` basligi; Quick'te `REPORT.md` Dagitim Erisimi
tablosunda satirlar. Kolonlar: Reklamveren | Meta (aktif, tarih) | Google ATC
(any time / 30g) | TikTok | Mesaj acilari (n/N) | Teklif/CTA | Hedef | Evidence.

Harcama, gosterim, CPI veya CAC tahmin etme. Reklam gozlemi `problem_demand` icin
`weak` kalir.

### Organik kanal sahipligi (Standard/Deep)

Hedef geo icin kanallara kimin hakim oldugunu olc:

1. Web aramasi: satin alma, karsilastirma, "nasil yapilir" ve marka niyetini
   kapsayan min 8 sorgu. Her sorguda ilk 10 organik sonucun turu (rakip sitesi
   veya rehberi, satis ortakligi kullanan inceleme sitesi, platform/resmi kaynak,
   forum/topluluk, sorgulanan sitenin kendisi) ve ucretli alanlardaki
   reklamverenler. Motor, `gl`/`hl` parametreleri ve gozlem yeri (IP ulkesi)
   `limitations` icine yazilir; ham sonuc `data/` altina kaydedilip
   `artifact_path` ile baglanir.
2. Anahtar kelime hacmi: hesap gerektiren arac yoksa `structurally_unobservable`;
   ucretsiz arac tahmini `E1` ve goreli olarak.
3. Video aramasi: ilk 10 sonucta sponsorlu, satis ortakligi baglantili veya rakip
   sahipli icerik orani.
4. Podcast ve icerik ureticisi sponsorlugu: takip sitesindeki sayilar ve donem;
   harcama tahmin edilmez.
5. Topluluk buyuklugu (haftalik ziyaretci, uye, aktif kullanici) ve rakip
   calisanlarinin tartismalardaki varligi.
6. Liste gorunurlugu ve son 12 aydaki yeni girisler: `app` icin magaza listeleri
   (top charts); `web_saas` icin review platformu kategori siralamalari, Product
   Hunt ve entegrasyon marketplace'leri; `service` icin harita/yerel paket ve rehber
   listeleri.

Kayit: `claim_id=<prefix>-distribution`; buyuk oyuncu hakimiyeti `contradicts`,
yeni bir oyuncunun organik cekisi `supports`, digerleri `neutral`. Web ve video
aramasi kayitlarinda `source_url` sorgunun sonuc sayfasi URL'sidir (orn.
`https://www.google.com/search?q=...&gl=us`); validator bu kayitlari sayar. Raporda
kanal ozet tablosu kullanilir (`report-writing.md` §10).

### Visual intelligence (Standard/Deep)

Incelenen yuzey urun turune gore secilir: `app` icin store screenshot'lari,
onboarding ve paywall; `web_saas` icin ana sayfa, fiyat sayfasi, deneme/demo kaydi
ve guvenlik sayfasi; `service` icin teklif sayfasi ve rezervasyon/teklif akisi.

Her kayit:

- kaynak URL/tool ve tarih
- storefront/country veya web icin geo
- ekran/akis
- gorulen mesaj/CTA
- screenshot/artifact path
- pattern ve bos kalan aci

Mobbin/Adapty pattern referansidir; pazar davranisi degildir. Codia/Figma uretim
yardimidir ve E0'dan yuksek evidence olamaz.

## Faz 5: Puanlama Girdisi

Her boyut icin:

1. claim ID'lerini sec.
2. supporting ve contradicting evidence'i yan yana koy.
3. 1-5 ankoruna gore low/base/high araligi ver.
4. Gerekli veri olculemiyorsa null kullan.
5. Arketip agirliklariyla assessment'i hesapla. `product_type` agirliklari
   degistirmez; ayni arketip her urun turunde ayni tabloyu kullanir.
6. En riskli uc varsayimin evidence grade'ini yaz. Her RAT varsayiminda
   `product_specific_evidence_ids` alani zorunludur; masa basinda bos dizi `[]`dir
   (Faz 5.5 sonuc kaydi bolumu).

Agent skor matematigini elle yazdiktan sonra validator ile dogrular.

## Faz 5.5: Insan Deneyi Sonuc Kaydi ve Devir

Deneyi insan yurutur; agent sonucu uydurmaz, tahmin etmez veya "tamamlandi" diye
yazmaz. Gercek sonuc geldiginde:

1. Her sonuc ayri evidence kaydidir: `source_type=experiment` veya `first_party`,
   `status=observed`, `observation_quality=direct`, `claim_relevance=direct`,
   deneyin test ettigi RAT ile ayni `claim_id` ve `idea_id`, ve bos olmayan
   `source_ref` (deney kimligi, odeme/islem kaydi) veya `artifact_path` (export,
   ekran goruntusu). Rakip URL'si urun-spesifik kanit degildir.
2. Kaydin seviyesi `pre-build-validation.md` merdiveninden gelir; urun-spesifik
   attestation yalniz `E3`/`E4` ve `direction=supports` kayitlariyla olur.
3. Bu kosullari saglayan kayitlarin ID'leri ilgili RAT varsayiminin
   `product_specific_evidence_ids` dizisine yazilir. `BUILD_SMALL` en az bir boyle
   bagli kayit ister; consumer_subscription retention ve marketplace liquidity
   kosullari kendi RAT kategorisindeki bagli kayitlarla karsilanir. Bagli kayit
   yoksa `BUILD_SMALL` yazilmaz.
4. Curuten veya E3 altindaki sonuclar da kaydedilir; bagli dizinin disinda kalir ve
   karar matrisine (`TESTE_DEVAM`, `PIVOT`, `KILL`) girer. Kosullari saglamayan bir
   kaydi diziye baglamak karardan bagimsiz olarak validate hatasidir; ekibin
   yurutmedigi bir deney icin dizi `[]` kalir.

Devir durumu raporda degil `data/portfolio.json` icindeki `handoff` nesnesinde
tutulur (`evidence-model.md` ve `pre-build-validation.md`): `owner` deney planindaki
`owner:` rolu (yeni kisi uydurulmaz), `state`, `prerequisites`, `next_action`,
`plan_path` ve `result_evidence_ids`. `completed` yalniz yukaridaki gibi gercek ve
gozlenmis deney/first-party sonuc kayitlari `result_evidence_ids` icindeyse
yazilir; `blocked` en az bir onkosul ister. Deney plani yoksa `handoff` `null`
kalir; plan uydurulmaz.

## Faz 7: Evidence Audit

Her finalistte su audit zorunludur:

- exact observation gercek mi ve baglami tam mi?
- claim'e relevance dogru mu?
- iki kaynak ayni root'u mu aktariyor?
- gelir/odeme davranis mi iddia mi?
- karsit kanit bulundu mu?
- missingness yokluk diye sunulmus mu?
- review/Reddit orneklemi genellenmis mi?
- zaman-duyarli veri bayat mi?

## Faz 9: Arama Gorunurlugu, Ekonomi ve Brief

Arama gorunurlugu (Deep; `phases/08-aso-research.md`):

- `app`: ASO; keyword source/scale/geo kaydet, head term disinda segment-intent
  terimleri ara, screenshot/paywall mesajini evidence'dan hipoteze izlenebilir bagla
- `web_saas`: ASO uygulanmaz; SEO sorgu niyeti, karsilastirma/alternatif sayfalari
  ve fiyat/landing mesaj hipotezleri
- `service`: ASO uygulanmaz; yerel arama/harita gorunurlugu, rehber listeleri ve
  teklif sayfasi mesaj hipotezleri

Non-app Deep'te dosya adi korunur; dosya ASO'nun neden uygulanmadigini
`<prefix>-collection-scope` `not_applicable` kaydina baglayarak acar ve urun
turunun arama gorunurlugu analizini icerir.

Ekonomi:

- pre-launch benchmark senaryosu en fazla C
- D30/D90 realized ARPPU, payback, brut katki ve retention first-party geldikce E4
- AI variable cost varsa kullanici/istek basina cost sensitivity
- geo kohortlarini ortalamayla gizleme

Brief:

- `BUILD_SMALL` yoksa kosullu taslak
- max 4 core ekran, 3 ozellik, gerekirse 1 paywall
- activation/retention/economy esikleri build oncesi yazili

## Faz 10: Karsit Kanit Sorgulari

- `[idea] failed app` (`web_saas`: `[idea] startup shut down`; `service`:
  `[service] business closed why`)
- `[competitor] complaints refund cancel`
- `[problem] free alternative enough`
- `[category] churn retention benchmark`
- `[feature] API limitation policy`
- `[market] regulation enforcement official`
- `[channel] CAC benchmark country`
- `why users return to [competitor]`

Karsit kanit yoklugu pozitif kanit degildir; denenen sorgulari kaydet.

## Cikti Kontrolu

Arastirma sonunda, sirayla:

1. `python3 scripts/evidence_tool.py render output/{tarih}-{konu}` — ledger ve
   raporun `## Özet` bolumu.
2. Standard/Deep: bagimsiz okur incelemesi ve dogrulama turu
   (`report-writing.md` §13). Okur guncel raporu okuyup iddialari kontrol ettikten
   sonra `python3 scripts/evidence_tool.py revision output/{tarih}-{konu}` ciktisini
   `data/reader-review.md` icinde `- İncelenen revizyon: <hash>` satirina yazar. Bu
   komut salt okunurdur; yazar veya baska bir komut revizyonu yeniden baglamaz.
   Sonradan REPORT metni veya evidence degisirse inceleme bayatlar ve okur turu
   tekrarlanir.
3. `python3 scripts/evidence_tool.py validate output/{tarih}-{konu}`
4. `data/portfolio.json` yaz veya guncelle: `title`, `lifecycle` (`active` |
   `archived` | `superseded`), `superseded_by`, `reason`, `handoff`. Yeni kosu
   `active`, `superseded_by: null`; deney plani yoksa `handoff: null`. Portfoy
   bilgisi `assessment.json` veya REPORT icine yazilmaz ve `BUILD_SMALL`
   yetkilendirmez.
5. `python3 scripts/portfolio_tool.py render` ve
   `python3 scripts/portfolio_tool.py validate` (varsayilan kok `output`) —
   `output/INDEX.md` icindeki uretilen scoreboard ve insan deneyi kuyrugu
   bolgeleri. Uretilen bolgeler elle duzenlenmez; Compare, destekleyici analiz ve
   tarihsel notlar bu bolgelerin disinda elle tutulur.
6. Istege bagli paylasim kopyasi:
   `python3 scripts/evidence_tool.py pdf output/{tarih}-{konu}`

Validator ve portfoy validate'i gecmeden rapor tamamlanmis sayilmaz. Rapor dili ve
yapisi `report-writing.md` sozlesmesine uyar.
