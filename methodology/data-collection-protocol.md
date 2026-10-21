# Veri Toplama Protokolu — v4.0

> Her gozlem `data/evidence.jsonl` icine yazilir. Alan ve derece kurallari icin
> `evidence-model.md` yetkilidir.

## Genel Kurallar

1. Once claim yaz, sonra o claim'i destekleyen ve curuten kaniti ara.
2. Gozlem kalitesi ile claim relevance'i ayri kaydet.
3. URL sayisi degil `independence_root` sayisi kullan.
4. Her zaman tarih, geo, storefront ve platform baglamini koru.
5. Zaman-duyarli veriyi arastirma gunu yeniden kontrol et.
6. Bulunamayan veride min 3 sorgu varyanti + denenen kaynaklari kaydet.
7. AI/sentetik ciktisini evidence olarak degil hipotez olarak kullan.
8. Karsit kanit sorgusu yapmadan claim derecesini kapatma.

## Preflight

Su sorular cevaplanmadan aramaya baslama:

- Hedef segment kim ve sonucun hangi geo/storefront'ta gecerli olmasi gerekiyor?
- App search-led mi, community/sales/partnership-led mi?
- Birincil arketip hangisi?
- Regulated, sensitive data, AI variable cost, hardware, children veya platform
  dependency modifier'i var mi?
- Bu analiz desk, prebuild veya post-MVP asamasinda mi?

## Faz 3: Hizli Pazar Taramasi

### 1. App ve ikame bul

Arama ornekleri:

- `site:apps.apple.com [keyword] app`
- `best [job to be done] app`
- `[problem] spreadsheet template`
- `[problem] service OR consultant OR manual workflow`
- `site:reddit.com [problem] what do you use`

En yuksek rating'i otomatik "pazar lideri" yapma. Segmentin ayni isini cozen app,
web urunu, hizmet veya manuel workflow'u ayri kaydet.

### 2. Store metadata

Her app icin:

- tam URL
- storefront/country ve platform
- rating count + star rating
- fiyat/IAP
- ilk yayin veya bilinen app yasi
- son guncelleme
- incelenen tarih

Rating `E2/direct observation/supporting relevance`dir. Talep claim'i icin ikinci
bagimsiz davranis sinyali gerekir.

### 3. Trend ve lifecycle

Dogru Google Trends erisimi yoksa dolayli makale sonucunu `estimated/inferred`
olarak kaydet. Lifecycle'i Exploding/Regular/Peaked ve buyume seklini ayri yaz.
Trend claim'inde yayin tarihi ile kapsanan veri donemini karistirma.

### 4. Geo ve dagitim

Hedef geo basina:

- store search sonucu ve autocomplete
- Apple Ads popularity/Insights kullanildiysa olcek baglami (1-5 veya 1-100)
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
cikarimi raporda "yazarın kaba çıkarımı" diye etiketlenir.

## Faz 4: Rakip ve Davranis Analizi

### Rakip kapsami

- Quick: min 5 rakip/ikame
- Standard/Deep: min 10 rakip/ikame
- App rakibi yoksa manual workflow ve service competitor'lari listeye dahil et

### Rakip profili

Quick'te top 5, Standard/Deep'te top 10 rakip/ikame icin:

- sirket kurulus yili ve bu urunun/ozelligin baslangic tarihi
- merkez, sahiplik/ana sirket, fonlama veya satin alma
- calisan sayisi veya araligi ve kaynagi (resmi dosya, sirket sayfasi, LinkedIn
  araligi)
- aciklanan kullanici, musteri veya gelir
- platformlar (iOS, Android, web, tarayici eklentisi) ve ulke kisitlari
- reklam edilen kapsam (site/ozellik sayisi) ile otomatik calisan kapsam farki
- sirketin kendi yazdigi sinirlar (yapmadigi isler)

Kayit: `claim_id=<prefix>-competitor-profile`, `direction=neutral`, `phase=4`.
Sirketin kendini anlatmasi `E1`; resmi dosya veya dogrudan gozlem `E2`. Bulunamayan
alan `not_found_after_protocol` olarak sorgu ve kaynaklarla kaydedilir. Raporda
`report-writing.md` §10 tablolarina girer.

### Bagimsiz basari olcumleri (Standard/Deep)

Rakiplerin isi ne kadar iyi yaptigini olcen kaynaklari ayri ara ve ayri yaz:

1. Test kurulusu ve akademik calisma: yontem, orneklem, donem.
2. Basin testi: kendi olcumu mu, rakibin panosundaki sayiyi mi aktariyor; satis
   ortakligi baglantisi var mi.
3. Sirketin kendi veya yaptirdigi olcum: `E1`, raporda "şirket beyanı".

Olcum, kullanicinin sikayet ettigi sonuca gore secilir (ornek: "kaldirildi"
sayisi mi, gercek kaldirma mi). 12 aydan eski olcum `weak` relevance alir.

### Stratified review mining

Standard/Deep'te top 5 rakip icin:

- hedef 30, erisim sinirliysa min 15 review
- 1-2, 3 ve 4-5 yildizdan min 5'er
- son 12 ay, app version ve storefront
- tema, star, tarih, kaynak URL ve evidence ID

Tema frekansi `tema kaydi / incelenen review` olarak raporlanir. Orneklem random
degilse genelleme yapilmaz. Pozitif review'lar kullanicinin gercekten deger verdigi
ozellikleri; 3-star review'lar tradeoff'u gosterir.

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
1-2 keyword aramasi (yeni girisleri yakalamak icin). Quick'te top 3 rakip icin
yalniz var/yok, aktif sayi ve hedef URL turu; mesaj acisi kodlamasi yok. Kayit
kurallari (`source_type=ad_library`, kok, artifact, seviye)
`tools-and-data-sources.md` icindedir; `phase` degeri `4`tur.

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
baslangic tarihi araligi ve kumelenme, format dagilimi, hedef URL turu (App Store /
Play / web), mesaj acilari (`kodlanan/incelenen` oraniyla), teklif/fiyat/indirim
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
6. Magaza listeleri (top charts) ve son 12 aydaki yeni girislerin gorunurlugu.

Kayit: `claim_id=<prefix>-distribution`; buyuk oyuncu hakimiyeti `contradicts`,
yeni bir oyuncunun organik cekisi `supports`, digerleri `neutral`. Raporda kanal
ozet tablosu kullanilir (`report-writing.md` §10).

### Visual intelligence

Her kayit:

- kaynak URL/tool ve tarih
- storefront/country
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
5. Arketip agirliklariyla assessment'i hesapla.
6. En riskli uc varsayimin evidence grade'ini yaz.

Agent skor matematigini elle yazdiktan sonra validator ile dogrular.

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

## Faz 9: ASO, Ekonomi ve Brief

ASO:

- keyword source/scale/geo kaydet
- head term disinda segment-intent terimleri ara
- screenshot/paywall mesajini evidence'dan hipoteze izlenebilir bagla

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

- `[idea] failed app`
- `[competitor] complaints refund cancel`
- `[problem] free alternative enough`
- `[category] churn retention benchmark`
- `[feature] API limitation policy`
- `[market] regulation enforcement official`
- `[channel] CAC benchmark country`
- `why users return to [competitor]`

Karsit kanit yoklugu pozitif kanit degildir; denenen sorgulari kaydet.

## Cikti Kontrolu

Arastirma sonunda:

```bash
python3 scripts/evidence_tool.py render output/{tarih}-{konu}
python3 scripts/evidence_tool.py validate output/{tarih}-{konu}
python3 scripts/evidence_tool.py pdf output/{tarih}-{konu}   # istege bagli paylasim kopyasi
```

Validator gecmeden rapor tamamlanmis sayilmaz. Rapor dili ve yapisi
`report-writing.md` sozlesmesine uyar.
