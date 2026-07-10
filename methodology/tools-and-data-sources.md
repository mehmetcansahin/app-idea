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

Meta Ad Library, Google Ads Transparency Center ve TikTok Creative Center icin
browser gozlemi tercih edilir. Kaydet:

- advertiser/domain
- aktif kreatif sayisi ve gorulen tarih araligi
- geo ve placement
- mesaj acisi
- ekran goruntusu/artifact

WebSearch ozetini direct sayma. Harcama tutari resmi olarak gorulmuyorsa uretme.
Ad longevity monetizasyon davranisini destekleyebilir; profit veya indie gelir
kaniti degildir.

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
