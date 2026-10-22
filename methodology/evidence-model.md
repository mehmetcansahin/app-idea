# Kanit Modeli ve Arastirma Sozlesmesi — v4.0

> Bu dosya kanit kayitlari, kaynak bagimsizligi, kanit dereceleri ve makine-okunur
> ciktilar icin tek yetkili kaynaktir. JSON sozlesmeleri `schemas/` altindadir.

## 1. Temel Ayrim: Gozlem != Cikarim

Her kayit iki ayri eksende degerlendirilir:

- `observation_quality`: `direct`, `estimated`, `inferred`
- `claim_relevance`: `direct`, `supporting`, `weak`

Ornek: US App Store'da gorulen rating sayisi `direct` bir gozlemdir; pazar talebi
iddiasi icin yalnizca `supporting` kanittir. Tek basina talep claim'ini B veya A
seviyesine tasiyamaz.

## 2. Kanit Seviyeleri

| Seviye | Tanim | Ornek |
|---|---|---|
| `E0` | AI cikarimi, sentetik kullanici veya temelsiz varsayim | LLM persona cevabi |
| `E1` | Gorus, niyet, vendor iddiasi veya dusuk-maliyetli davranis | waitlist, tiklama, "oderim" |
| `E2` | Resmi/public metrik, dogrulanabilir gecmis davranis veya dogrudan gozlem | App Store rating, gecmis ucretli workaround |
| `E3` | Gercek islem, depozito, randevu, imzali taahhut veya gozlenen pazar davranisi | iade edilebilir depozito, LOI |
| `E4` | Urun-spesifik first-party odeme, tekrarlanan kullanim veya retention | ucretli kohort, D30 retention |

AI ciktisi hipotez uretebilir fakat karari destekleyen evidence root sayilmaz.

`ad_library` (reklam kutuphanesi) gozlemi en fazla `E2`dir; reklamverenin mesajini
gosterir, kullanici davranisini degil.

## 3. Claim Bazli Kanit Derecesi

Claim derecesi, ayni iddiaya bagli kayitlardan hesaplanir:

- `A`: Bir `E4` veya farkli `independence_root` degerlerinden iki `E3`; kaynaklar
  dogrudan ilgili ve cozulmemis guclu karsit kanit yok.
- `B`: Farkli koklerden `E3 + E2` veya en az uc bagimsiz `E2`.
- `C`: En az bir `E2` ya da iki `E1`; yalnizca yon gosterir.
- `D`: Yalniz `E0/E1`, olculemeyen durum, eksik kanit veya cozulmemis celiski.

`claim_relevance=weak` kayitlari A/B sayimina girmez. `direction=contradicts` olan
guclu kayitlar cozulmeden claim A olamaz.

Bir claim'in tum destekleyen kayitlari `ad_library` ise derece en fazla C olur;
`scripts/evidence_tool.py` bu tavani hesaplar. Rating kuralinin reklam karsiligidir:
reklam yogunlugu tek basina talep, dagitim veya odeme davranisi kanitlamaz.

Genel Kanit Gucu, RAT tablosundaki en yuksek `impact * uncertainty` degerine sahip
uc varsayimin en dusuk claim derecesidir. Uc varsayim tamamlanmamissa eksik olan D
sayilir.

## 4. Kaynak Bagimsizligi

Her kayit `independence_root` tasir. Ayni birincil raporu aktaran farkli URL'ler tek
kaynak sayilir. Ornek: RevenueCat raporu ve o raporu ozetleyen iki haberin ucu de
`revenuecat-sosa-2026` kokunu kullanir.

- Birincil kaynaktaki ciplak gozlem tek kaynakla kaydedilebilir.
- Gozlemden pazar/urun sonucu cikariliyorsa B+ icin bagimsiz kok gerekir.
- `synthetic` kaynaklar bagimsiz kok sayimina girmez.
- `ad_library` kokleri `adlib-<platform>-<reklamveren>-<tarih>` bicimindedir;
  `publisher` granulerliginde ayni reklamverenin Meta ve Google kayitlari tek kok
  olur.

### Kok Granulerligi

Bir analiz kok granulerligini secer ve rapor icinde sabit tutar:

- `document`: kok tek bir artefakti tanimlar (bir store listing, bir dokumantasyon
  sayfasi, bir review feed). Ayni saticinin iki listing'i ayri kok alir.
- `publisher`: kok yayinciyi tanimlar. Ayni yayincinin tum artefaktlari tek kok
  olur; yayincinin kendi urunu veya platformu hakkindaki iddialari birbirini
  dogrulamaz.

`publisher` daha muhafazakardir ve bagimsizligi asla sismez; vendor kendi
kabiliyetini iddia ediyorsa bu granulerlik kullanilir. Farkli granulerlik kullanan
analizlerin kokleri birbiriyle karsilastirilmaz.

Bagimsizlik uyarisi derece-duyarlidir: `scripts/evidence_tool.py` ayni kok altindaki
birden fazla URL'yi yalniz o kok bolunse claim derecesi yukselecekse isaretler.
Publisher granulerligi veya tek toplama protokolu gibi muhafazakar kokler bu esikte
sessizdir; ekonun karari degistirdigi durum gorunur kalir.

Portable destek yuzeyleri (`artifact.json` tasiyan, tek fikri puanlamayan analizler)
`data/evidence.jsonl` uretmez; kaynak koklerini kendi veri dosyasindaki
`source_roots` kaydinda tutar ve `granularity` alanini belirtir.

## 5. Bulunamayan Veri

`status` degerleri:

- `observed`
- `not_found_after_protocol`
- `structurally_unobservable`
- `not_applicable`

`not_found_after_protocol` zayif karsit kanittir; aranan sorgular ve kaynaklar
kaydedilir. `structurally_unobservable` yokluk degildir ve negatif puanlanmaz;
ilgili claim'in kanit derecesini dusurur. "Indie gelir kaniti bulunamadi" ifadesi
"kimse kazanmiyor" olarak yazilamaz.

## 6. Evidence JSONL Sozlesmesi

Kanonik kayit `data/evidence.jsonl` dosyasidir. Her satir tek JSON nesnesidir ve su
alanlari kullanir:

- Kimlik: `evidence_id`, `claim_id`, `idea_id`, `phase`
- Kaynak: `source_type`, `source_title`, `source_url`, `source_ref`,
  `artifact_path`, `independence_root`
- Baglam: `collected_at`, `data_period`, `geo`, `storefront`, `platform`
- Gozlem: `status`, `observation`, `value`, `unit`
- Degerlendirme: `evidence_level`, `observation_quality`, `claim_relevance`,
  `direction`
- Orneklem: `sample_n`, `denominator`
- Sinirlar: `limitations`
- Arama yoklugu: `search_queries`, `attempted_sources`

Web kaydinda `source_url`; insan deneyi, user input veya yerel gozlemde
`source_ref` ya da `artifact_path` zorunludur. `evidence_id` ve `claim_id` analiz
icinde benzersiz, ASCII slug formatinda olmalidir.

## 7. Assessment JSON Sozlesmesi

`data/assessment.json` karar mekanizmasinin makine-okunur ozetidir:

- metodoloji, tarih, mod ve asama
- urun turu: `product_type` = `app`, `web_saas` veya `service`
  (`scoring-model.md` §1)
- hedef segment/geo, arketip ve risk modifier'lari
- boyutlarin `low/base/high` puanlari ve claim baglantilari
- firsat skor araligi ve sinifi
- fatal gate durumlari
- RAT varsayimlari, claim dereceleri ve `product_specific_evidence_ids`
- genel Kanit Gucu
- karar, arastirma/build durumu, bir sonraki deney ve durdurma kurali
- post-MVP asamasinda ardışık kohort ve threshold sonucu

Tam alan ve enum listesi `schemas/assessment.schema.json` dosyasindadir.

`status` yalniz arastirma/build durumudur: `DESK_RESEARCH_COMPLETE`,
`PREBUILD_PENDING`, `PREBUILD_PASSED`, `BUILDING`, `POSTLAUNCH`, `KILLED`.
Arsivlenme ve baska kosuyla yer degistirme assessment durumu degil, portfoy
metadatasidir (§11); assessment'ta `ARCHIVED` veya `LEGACY` yoktur. v3.x raporlari
assessment tasimaz ve oldugu gibi kalir.

### Urun-spesifik kanit baglantisi

Her RAT varsayimi `product_specific_evidence_ids` tasir: benzersiz evidence ID
dizisi; bos dizi gecerlidir. Listeye giren her kayit su kosullarin hepsini saglar;
saglamayan kimlik karardan bagimsiz olarak `validate` hatasidir:

- `data/evidence.jsonl` icinde vardir; `claim_id`'si RAT'in `claim_id`'si,
  `idea_id`'si assessment'in `idea_id`'sidir.
- `status=observed`, `observation_quality=direct`, `claim_relevance=direct`,
  `direction=supports`.
- `evidence_level` `E3` veya `E4`'tur.
- `source_type` `first_party` veya `experiment`'tir.
- Bos olmayan `source_ref` veya `artifact_path` tasir. Rakip sayfasi gibi yalniz
  bir web URL'si urun-spesifik kanit degildir.

Bu acik baglanti urun-spesifik davranis beyaninin kendisidir; ayri bir bayrak
yoktur ve eski `product_specific_behavior` alani kaldirildi. Masa basi kaniti,
deney plani veya portfoy devri bu listeye girmez. `BUILD_SMALL` kullanimi
`scoring-model.md` §6'dadir.

### Yapisal dogrulama

`scripts/evidence_tool.py validate` once yapiyi denetler: her evidence kaydi
`schemas/evidence-record.schema.json`, assessment `schemas/assessment.schema.json`
ile karsilastirilir. Bozuk JSON/JSONL, yanlis tip (sayi yerine bool dahil), enum
disi deger, eksik zorunlu alan veya bilinmeyen alan dosya/satir/alan bilgisiyle
hata olur; arac traceback ile kesilmez. Derece, gate ve karar kontrolleri yalniz
yapisal olarak gecerli veride calisir; evidence yapisal olarak gecersizken
assessment capraz kontrolleri uyariyla atlanir. `validate-all` bir klasordeki
hatadan sonra digerlerine devam eder.

### Gecmis assessment gocu

2026-10-22 sozlesme sertlestirmesi yerel v4 assessment dosyalarinda yalniz alan
gocu yapar: `product_type` eklenir, `product_specific_behavior` yerine
`product_specific_evidence_ids` yazilir ve her kosuya `data/portfolio.json`
eklenir. Skor, karar, durum ve kanit dereceleri degismez; uygun E3/E4
urun-spesifik kayit yoksa liste bos kalir. `REPORT.md`, `evidence.jsonl`, okur
incelemesi ve v3 raporlari bu gocle degistirilmez.

## 8. Markdown Kanit Defteri

`data/evidence-ledger.md`, JSONL'nin insan-okunur ve deterministik gorunumudur.
Elle kanonik veri sayilmaz; `scripts/evidence_tool.py render <output-dir>` ile
uretilir. `REPORT.md` kritik iddialari govdede kaynagin tiklanabilir URL'siyle,
denetim icin claim/evidence kimlikleriyle de Ek C'de bu deftere baglar
(`report-writing.md` §5). 2026-10-20 ve sonrasi analiz tarihli raporlarda
kimlikler govdede kullanilmaz.

Okur incelemesi raporun yazar metnine ve `evidence.jsonl` kayitlarina birlikte
baglanir (`report-writing.md` §13). Bir kaydin eklenmesi, silinmesi veya
degismesi incelemeyi bayatlatir; ledger'in yeniden uretilmesi tek basina
bayatlatmaz.

## 9. Zaman ve Tazelik

- Her kayit `collected_at` ve mumkunse `data_period` tasir.
- Rating, fiyat, reklam, mevzuat, urun ozelligi ve benchmark gibi degisebilir veri
  her arastirmada yeniden kontrol edilir.
- 6 aydan eski zaman-duyarli veri uyari; 12 aydan eski veri guncel karar icin
  varsayilan olarak `weak` relevance alir.
- Tarihsel arastirmalarda veri guncel veriyle sessizce doldurulmaz; zaman farki
  sinirlama olarak kaydedilir.

## 10. Raporlama Kurallari

- Her kritik internet iddiasinda tiklanabilir URL bulunur; URL `evidence.jsonl`
  kaydindan gelir.
- Geo/storefront/platform baglami kaybolmaz.
- Review tema frekansi yalniz incelenen orneklem icin raporlanir; random sample
  yoksa pazar prevalansi denmez.
- Direkt alinti yalniz gerekli kisa parcayla sinirli tutulur; `observation` alani
  varsayilan olarak paraphrase kullanir.
- Raporun dili, yapisi ve kaynak turu etiketleri `report-writing.md` dosyasina
  uyar.

## 11. Portfoy Metadatasi ve INDEX

Her v4 kosusu (`output/` altinda dogrudan `data/assessment.json` tasiyan klasor)
`data/portfolio.json` tasir. Bu dosya portfoy yasam dongusunu ve insan deneyi
devrini tutar; `assessment.json` icine gomulmez, arastirma durumunu, skoru veya
karari degistirmez ve `BUILD_SMALL` icin girdi degildir. Sema:
`schemas/portfolio-entry.schema.json`. Destek analizleri (`artifact.json`) ve v3
raporlari bu dosyayi tasimaz; bu klasorlerde bulunan `portfolio.json` hatadir.

Alanlarin hepsi zorunludur; baska alan kullanilmaz:

| Alan | Deger | Kural |
|---|---|---|
| `title` | bos olmayan metin | INDEX'te gorunen konu |
| `lifecycle` | `active`, `archived`, `superseded` | Portfoydeki yer |
| `superseded_by` | `null` veya klasor adi | Yalniz `superseded` icin dolu |
| `reason` | metin veya `null` | `archived` ve `superseded` icin bos olmayan gerekce |
| `handoff` | nesne veya `null` | Insan deneyi devri (`pre-build-validation.md` §10) |

Yasam dongusu kurallari:

- `active`: `superseded_by=null`.
- `archived`: bos olmayan `reason`, `superseded_by=null`.
- `superseded`: bos olmayan `reason`; `superseded_by`, ayni `output/` kokundeki
  baska bir v4 kosusunun klasor adidir (yol degil). Kendine, olmayan klasore veya
  `..`/yol ayirici iceren degere isaret edemez; yer degistirme zinciri dongu
  olusturamaz.
- Her durumda kosunun `assessment.json` durumu, skoru, karari ve kanit derecesi
  oldugu gibi kalir. Yerine baska kosu gelen bir Quick'in `PREBUILD_PENDING`
  durumu tarihsel arastirma sonucudur, yurutulecek is degildir.

`handoff` nesnesinin alanlari:

| Alan | Kural |
|---|---|
| `owner` | Mevcut deney planinda adi gecen insan rolu; uydurulmus kisi veya kimlik degil; bos olamaz. `plan_path` doluysa rol o dosyada gecmelidir (gecmiyorsa uyari) |
| `state` | `blocked`, `ready`, `in_progress`, `completed`, `not_planned` |
| `prerequisites` | Metin dizisi; `blocked` icin bos olamaz |
| `next_action` | Bos olmayan metin: siradaki insan adimi |
| `plan_path` | Kosu klasorune gore goreli, var olan dosya (ornek `phases/06-prebuild-plan.md`) veya `null`; mutlak yol, `..` ve ters bolu kullanilmaz |
| `result_evidence_ids` | Benzersiz evidence ID dizisi |

`result_evidence_ids` icindeki her kayit kosunun `evidence.jsonl` dosyasinda
bulunur, `idea_id`'si assessment ile aynidir ve `status=observed`'dur. `completed`
icin liste bos olamaz ve her kayit `first_party` veya `experiment` kaynaklidir,
bos olmayan `source_ref` ya da `artifact_path` tasir. Yurutulmemis deney
`completed` yazilmaz. Deney plani yoksa `handoff=null` kalir; plan veya sorumlu
uydurulmaz. `archived` veya `superseded` kosuda acik (`blocked`, `ready`,
`in_progress`) devir kuyrukta gizlendigi icin uyari verir.

### Uretilen INDEX bloklari

`output/INDEX.md` icindeki iki blok veriden uretilir ve elle duzenlenmez:

- `<!-- portfolio:scoreboard:start -->` ... `<!-- portfolio:scoreboard:end -->`:
  v4 scoreboard'u. Tarihe gore yeniden eskiye, sonra klasor adina gore siralanir;
  yasam dongusunu assessment durumundan ayri sutunda ve yerine gecen kosunun
  baglantisini gosterir. Ciplak skora gore siralama yapmaz.
- `<!-- portfolio:handoff:start -->` ... `<!-- portfolio:handoff:end -->`
  (`## Insan Deney Kuyrugu`): devri olan aktif kosularin arketipi, karari, devir
  durumu, sorumlusu, on kosullari, sonraki adimi, plan baglantisi ve sonuc
  kayitlari. Devri olmayan aktif kosular kuyrugun altinda deney sahibi atanmamis
  olarak ayrica listelenir; `archived` ve `superseded` kosularin deneyleri aktif
  kuyrukta yer almaz.

Bloklarin disindaki legacy (v3) satirlari, Compare ve destek bolumleri ile
tarihsel notlar degismez.

```bash
python3 scripts/portfolio_tool.py render [output_root]     # varsayilan: output
python3 scripts/portfolio_tool.py validate [output_root]
```

`render` once butun kosulari dogrular; herhangi bir hata varsa hicbir dosya
yazmaz. Isaretsiz mevcut v4 scoreboard'u ilk `render`'da benimsenir: rapor
baglantili v4 satirlari uretilen blokla degisir, legacy satirlari ve basliklar
korunur; kuyruk bolumu yoksa scoreboard'dan sonra eklenir. `validate`
metadata alanlarini, `superseded_by` baglantilarini, sonuc kayitlarini ve INDEX
bloklarinin guncelligini kontrol eder; `portfolio.json` eksik v4 kosusu ve
uretilen blok disinda kalan v4 scoreboard satiri hatadir.
`evidence_tool.py validate <output-dir>` tek kosuda portfoy metadatasi istemez;
`validate-all` kok dizinde `INDEX.md` varsa portfoy dogrulamasini da calistirir.
