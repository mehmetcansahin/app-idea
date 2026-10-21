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
- hedef segment/geo, arketip ve risk modifier'lari
- boyutlarin `low/base/high` puanlari ve claim baglantilari
- firsat skor araligi ve sinifi
- fatal gate durumlari
- RAT varsayimlari ve claim dereceleri
- genel Kanit Gucu
- karar, bir sonraki deney ve durdurma kurali
- post-MVP asamasinda ardışık kohort ve threshold sonucu

Tam alan ve enum listesi `schemas/assessment.schema.json` dosyasindadir.

## 8. Markdown Kanit Defteri

`data/evidence-ledger.md`, JSONL'nin insan-okunur ve deterministik gorunumudur.
Elle kanonik veri sayilmaz; `scripts/evidence_tool.py render <output-dir>` ile
uretilir. `REPORT.md` kritik iddialari govdede kaynagin tiklanabilir URL'siyle,
denetim icin claim/evidence kimlikleriyle de Ek C'de bu deftere baglar
(`report-writing.md` §5). 2026-10-20 ve sonrasi analiz tarihli raporlarda
kimlikler govdede kullanilmaz.

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
