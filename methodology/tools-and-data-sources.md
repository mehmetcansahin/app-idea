# Arac ve Veri Kaynagi Envanteri — v4.0

> Kaynagin dogru olmasi, o kaynaktan yapilan cikarimin dogru oldugu anlamina
> gelmez. Evidence kaydi hem observation quality hem claim relevance tasir.

## App Store / Google Play

| Kaynak | Gozlem | Varsayilan evidence notu |
|---|---|---|
| App Store product page | rating, star, fiyat, version, screenshot | E2/direct; talep icin supporting |
| Google Play product page | rating, install bandi, fiyat | E2/direct; platforma ozgu |
| App Store Connect | download, conversion, proceeds, retention | First-party E4 olabilir |
| Apple peer benchmark | category/model/volume karsilastirmasi | E2/supporting; directional |

Store verisi her zaman storefront/country, platform, app yasi ve erisim tarihiyle
kaydedilir. Rating count pazar gate'i degildir.

## Keyword / ASO

| Kaynak | Kullanim | Sinir |
|---|---|---|
| App Store autocomplete | arama dili ve intent | hacim degil |
| Apple Ads keyword UI | popularity 1-5 | relative, campaign/geo baglamli |
| Apple Ads Insights report | popularity 1-100 veya 1-5 | report/scale/geo kaydet |
| AppTweak/AppFigures/SearchAds.com | volume/difficulty estimate | third-party; methodology degisebilir |
| Google Trends/Glimpse | lifecycle ve yon | mutlak app demand degil |

Apple popularity olcegini kaynaga gore acikca yaz; farkli olcekleri sessizce
karsilastirma. Top-result rating profilinden difficulty uretmek inferred/weak'tir.

## Community ve Kullanici Arastirmasi

| Kaynak | Guclu oldugu konu | Varsayilan sinir |
|---|---|---|
| Reddit/forum/community | dil, workaround, migration nedeni | temsil gucu belirsiz |
| App review | aktif kullanicinin urun deneyimi | self-selection, rating prompt bias |
| Mom-Test interview | gecmis olay ve davranis | nicel oran degil |
| Synthetic persona | hipotez/edge case uretimi | E0; kullanici kaniti degil |

Watering-hole once bulunur; sonra community okunur. Organik ve paid trafik farkli
sorulari yanitlar ve ayni denominator'da karistirilmaz.

## Gelir ve Ekonomi

| Kaynak | Evidence potansiyeli | Not |
|---|---|---|
| App Store Connect/RevenueCat first-party | E4 | proceeds, cohorts, retention |
| Kapanmis app satisi | E3 | gelir mi kar mi, multiple acikla |
| Imzali LOI/depozito/on-siparis | E3 | urun-spesifik commitment |
| Kurucu revenue beyanı | E1/E2 | dogrulanabilirlik ve survivorship |
| Sensor Tower/AppMagic estimate | E1/E2 | estimate, aralik kullan |
| RevenueCat/Adapty benchmark | E2/supporting | kategori, geo ve selection bias |
| Canli marketplace ilani | E1 | asking price/seller claim |

Pre-launch LTV:CAC proof degildir. First-party geldikce D30/D90 realized ARPPU,
payback, brut katki ve retention kohortlari kullanilir.

## Ad/Channel Intelligence

Reklam kutuphaneleri rakibin ne soyledigini, hangi kanali kullandigini ve nereye
yonlendirdigini gosterir; harcama, CPI, CAC, ROAS, ABD gosterim sayisi veya keyword
hacmi gostermez. Bunlar yalniz Faz 5.5 kanal testiyle olculur.

| Kaynak | ABD'de gorulen | Gorulmeyen | Resmi API / veri seti | Sinir |
|---|---|---|---|---|
| Meta Ad Library (`facebook.com/ads/library`) | Yalniz su an aktif reklamlar: sayfa, baslangic tarihi, format, metin, hedef URL, platformlar | Harcama, gosterim, bitmis reklamlar | `ads_archive` Graph API AB'ye ulasmayan ticari reklamlari dondurmez; AB reklamlarinda `eu_total_reach` ve hedefleme var | Otomatik toplama Meta Automated Data Collection Terms'e tabidir; scraper kullanma |
| Google Ads Transparency Center (`adstransparency.google.com`) | Reklamveren/domain bazinda kreatif, format, ilk/son gosterim, dogrulanmis reklamveren adi, bolge filtresi | Harcama, gosterim, keyword | BigQuery `google_ads_transparency_center.creative_stats`; `region_stats` yalniz AEA + Turkiye | Keyword niyeti yalniz baslik metninden cikarilir ve `inferred` kalir |
| TikTok Creative Center Top Ads (`ads.tiktok.com/business/creativecenter`) | TikTok for Business girisiyle bolge/sektor bazli ornek reklamlar | Girissiz yalniz birkac genel kart; reklamveren onayli secilmis ornek, tum reklamlar degil | Commercial Content Library/API (`library.tiktok.com`) yalniz AB/AEA + UK + CH; basvuru gerekir | Giris yoksa `structurally_unobservable` |

Kayit kurallari:

- `source_type=ad_library`; `evidence_level` en fazla `E2`. Tarayici gozlemi
  `E2/direct`, WebSearch veya ucuncu taraf ozeti `E1/estimated`.
- `independence_root=adlib-<platform>-<reklamveren-slug>-<YYYY-MM-DD>`; keyword
  aramasinda `adlib-<platform>-kw-<keyword-slug>-<YYYY-MM-DD>`. `platform` alani
  `meta`, `google_ads` veya `tiktok`.
- `artifact_path=data/artifacts/ads/<platform>-<reklamveren-slug>-<YYYY-MM-DD>.png`.
  Kutuphaneler yalniz canli reklami gosterdigi icin ekran goruntusu tek kalici
  kanittir; gozlenen kayitta eksikse validator uyarir.
- Yalniz `ad_library` kayitlarina dayanan destek claim'i C'de tutar
  (`evidence-model.md`).
- AB/TR veri setindeki erisim veya gosterim araligi ABD iddiasi icin en fazla
  `supporting`tir; geo farki `limitations` icine yazilir.
- Harcama tutari resmi olarak gorulmuyorsa uretme. Ad longevity monetizasyon
  davranisini destekleyebilir; profit veya indie gelir kaniti degildir.

Boyut eslemesi:

| Boyut | Kullanim | Relevance |
|---|---|---|
| `competitive_wedge` | Rakibin kullandigi mesaj acilari; bizim wedge'imizin zaten reklamda olmasi | direct, cogunlukla contradicts |
| `distribution_access` | Kullanilan kanal, hedef (App Store/Play/web), rakip adina bidding, creator/affiliate payi, reklamveren yogunlugu | direct |
| `monetization_economics` | Reklamdaki fiyat/indirim capasi; uzun sure yayinda kalan reklam | supporting |
| `timing` | Yeni girislerin baslangic tarihlerinde kumelenmesi | supporting |
| `problem_demand` | Reklam sayisi talep gostermez | weak |

## Visual Intelligence

- App Store screenshots: direct urun mesaji gozlemi
- Mobbin: third-party flow library
- Adapty Paywall Library: pattern referansi
- Codia/Figma/screenshot-to-code: uretim yardimi, E0

Kopyalama yapma; tekrar eden pattern, ilk deger ani, paywall trigger ve bos kalan
aciyi cikar.

## Regulator ve Resmi Kaynak

Yasa, tesvik, payout ve platform policy zaman-duyarlidir. Resmi/guncel sayfa
birincil kaynaktir. Turkiye tesvik sorgusunda `site:gov.tr` kullan; resmi kaynak
yoksa BELIRSIZ yaz. Hukuki yorum gerektiren fatal gate'te uzman gorusu planla.

## Kaynak Secim Sirasi

1. Urun-spesifik first-party davranis
2. Resmi/birincil gozlem veya gercek islem
3. Bagimsiz davranis kaydi
4. Third-party estimate
5. Gorus/vendor iddiasi
6. AI/sentetik hipotez

Her seviye alt seviyenin yerine gecmez: birincil rating gozlemi, urun-spesifik
odeme veya retention kaniti degildir.

## Tazelik

| Veri | Kontrol |
|---|---|
| Store metadata/rating/fiyat | her analiz |
| Ads/keyword/trend | her analiz |
| Revenue benchmark | yayin yilini kaydet |
| Regulator/platform policy | her analiz ve build oncesi |
| Review/community | son 12 ay agirlikli |

6+ aylik zaman-duyarli veri uyari; 12+ aylik veri guncel claim icin varsayilan
olarak weak relevance alir.
