# Pipeline Tanimlari — v4.0

> Faz sahipligi ve gate'ler icin kanonik ozet. Puanlama:
> `scoring-model.md`; kanit: `evidence-model.md`; Faz 5.5:
> `pre-build-validation.md`; rapor dili ve yapisi: `report-writing.md`.

## Research Contract Preflight (Numarasiz)

**Amac:** Problem, segment, geo, platform, urun turu, asama, arketip ve risk
modifier'larini kilitle.

**Cikti:** `data/assessment.json` baslangic alanlari; `product_type` (`app` |
`web_saas` | `service`) dahil.

**Gate:** Tek birincil arketip secilmis; belirsiz ve skoru degistiren secim
kullaniciya sorulmus; hedef segment/geo ve urun turu acik. Urun turu toplama
kapsamini belirler, arketip agirliklarini degistirmez
(`data-collection-protocol.md` Urun Turu ve Toplama Kapsami).

## Faz 1: Problem Havuzu

**Amac:** Somut, tekrarlanan ve secilen urun turunde (app'te mobilde) anlamli
problemleri bul.

**Cikti:** Kim, son ne zaman, status quo, harcanan zaman/para ve urun turune
uygunluk iceren problem listesi.

**Gate:** Coklu fikir kesfinde min 15 problem ve 3 kategori. Tek fikir analizinde
problemin en az bir spesifik segmenti ve ikameleri tanimli.

## Faz 2: Keyword ve Kanal Cluster

**Amac:** Arama terimlerini ve kullanicilarin gercekte bulundugu kanallari esle.

**Cikti:** Keyword cluster + watering-hole + app disi ikame listesi.

**Gate:** Her problem icin aranabilir terimler ve en az bir erisim kanali; yoksa
dagitim claim'i `not_found_after_protocol` olarak kaydedilir.

## Faz 3: Hizli Pazar Taramasi

**Amac:** Pazar proxy'lerini, ikameleri ve fatal gate adaylarini erken tara.

**Cikti:** Lider/rakipler, urun turune gore metadata (`app`: storefront-bazli store
metadata; `web_saas`: fiyat, plan, musteri, guvenlik/uyum ve satis hareketi;
`service`: saglayici, teklif, teslim ve musteri davranisi), arama/trend, ikameler,
hedef geo, Standard/Deep'te pazar buyuklugu dagilimi ve ilk evidence kayitlari.

**Kural:** Rating fatal gate degildir; `E2/supporting` proxy'dir. Rakip app yoksa
manuel workflow, web urunu ve hizmet aranir. Non-app turlerde store metadata,
store review ve ASO gorevleri zorunlu degildir; atlandiklari tek bir
`not_applicable` kaydiyla acikca yazilir.

## Faz 4: Rakip ve Davranis Analizi

**Amac:** Rakip, ikame, review, fiyat, JTBD, dagitim, reklam ve visual pattern'leri
moda ve urun turune uygun kapsamda incele.

**Mod kapsami:**

| Mod | Rakip/ikame ve profil | Reklam kutuphanesi | Stratified review | Organik kanal, visual, bagimsiz olcum |
|---|---|---|---|---|
| Quick | top 5 | top 3, Meta + Google ATC var/yok | yok | yok |
| Standard/Deep | top 10 | top 5, Meta + Google ATC + TikTok | top 5 | var |
| Compare | her aday Quick ile ayni | Quick ile ayni | yok | yok |

**9 adim** (Quick ve Compare 3 ile 9'u yapmaz; 6 ve 8'de yalniz Quick kismini
yapar):

1. Rakip + ikame listesi ve sirket profili (kurulus, sahiplik, buyukluk,
   platform/hizmet kanali, kapsam ve sinirlar)
2. Urun turune gore metadata: `app` store/storefront; `web_saas` fiyat, plan,
   musteri, guvenlik/uyum, satis hareketi; `service` saglayici, teklif, teslim
3. Stratified review mining (Standard/Deep): `app` store yorumlari; `web_saas`
   ucuncu taraf review platformu; `service` yerel review/marketplace yorumlari
4. Reddit/community + JTBD Forces
5. Fiyat ve gercek odeme davranisi
6. Ozellik/wedge, Standard/Deep'te bagimsiz basari olcumleri ve Deep'te 2x2
7. Platform cross-check (app: iOS/Android/web; non-app: web, entegrasyon veya
   hizmet kanali)
8. Ad/channel intelligence (Quick top 3 Meta/Google var/yok; Standard/Deep top 5
   ve TikTok; `ad_library` kayitlari) ve Standard/Deep'te organik kanal sahipligi
   (web/video aramasi, sponsorluk, topluluk, urun turune gore liste gorunurlugu);
   protokol `data-collection-protocol.md`
9. Visual intelligence (Standard/Deep): `app` store screenshot, onboarding ve
   paywall; `web_saas` ana sayfa, fiyat ve deneme/demo akisi; `service` teklif ve
   rezervasyon akisi

**Review minimumu (Standard/Deep):** Top 5 rakip, hedef 30/min 15 yorum; 1-2,
3 ve 4-5 yildizdan en az 5'er; son 12 ay; `app` icin surum/storefront, non-app
icin platform/listing kaydi. Quick ve Compare'de stratified review yoktur.

**Yokluk:** Karar-kritik alan/claim icin en az 3 sorgu varyanti ve sinirli durma;
kozmetik profil alaninda tek tarama (`data-collection-protocol.md` Yokluk
Protokolu).

**Cikti sahipligi:**

- Quick/Compare: bulgular dogrudan `REPORT.md` ve evidence kayitlarinda
- Standard/Deep `02-competitor-analysis.md`: adim 1-2, 4-9
- Standard/Deep `03-review-mining.md`: adim 3

## Faz 5: Iki Eksenli Degerlendirme

**Amac:** Arketip-bazli Firsat Cekiciligi ile Kanit Gucu'nu ayri hesapla.

**Cikti:** Standard/Deep'te `04-scoring.md`; tum modlarda tamamlanmis
`data/assessment.json`.

**Gate:** Fatal gate'ler kanitli; agirligi sifir olmayan boyutlar low/base/high
puanli veya acikca `null`; en riskli uc varsayim dereceli ve her RAT varsayiminda
`product_specific_evidence_ids` dizisi var (masa basinda `[]`). `product_type`
arketip agirliklarini degistirmez.

**Masa basi kararlari:** `ELENDIR`, `BELIRSIZ`, `TESTE_DEGER`,
`TEST_ONCELIKLI`. Masa basi arastirmasi GO veya BUILD karari vermez.

## Faz 5.5: Build-Oncesi Dogrulama

**Amac:** En riskli varsayimi uygun davranis deneyiyle test et.

**Cikti:** Standard/Deep'te `06-prebuild-plan.md`; insan deneyi gercekten
yurutulurse yeni evidence kayitlari, RAT `product_specific_evidence_ids`
baglantilari ve assessment guncellemesi. Devir durumu `data/portfolio.json`
`handoff` nesnesindedir (Portfoy ve INDEX).

**Gate:** `BUILD_SMALL` icin firsat low >=60, genel kanit B+, top risk B+ ve RAT
`product_specific_evidence_ids` ile bagli en az bir uygun urun-spesifik kayit:
ayni `claim_id` ve `idea_id`, `status=observed`, `observation_quality=direct`,
`claim_relevance=direct`, `direction=supports`, `E3`/`E4`, `source_type`
`experiment` veya `first_party`, bos olmayan `source_ref` veya `artifact_path`.
Rakip URL'si bu kanit yerine gecmez. consumer_subscription retention ve
marketplace liquidity kosullari kendi RAT kategorisindeki bagli kayitlarla
karsilanir. Aksi `TESTE_DEVAM`, `PIVOT` veya `KILL`. Sonuc gelmeden deney
tamamlanmis yazilmaz.

## Faz 6: Finalist Secimi

**Amac:** Coklu fikirlerde test yatirimi yapilacak finalistleri sec.

**Oncelik:** Fatal gate -> Kanit Gucu -> skor araligi -> top risk/test maliyeti ->
kurucu/operasyon kisitlari.

**Kural:** Farkli metodoloji surumleri ve arketipler ciplak skorla siralanmaz.

## Faz 7: Kanit Denetimi ve Karsi Kontrol

**Amac:** Kritik claim'leri bagimsizlik, tazelik, karsit kanit ve construct
validity acisindan denetle.

**Kontroller:**

1. Primary/public gozlem gercek ve baglami tam mi?
2. Gelir/odeme kaniti iddia mi davranis mi?
3. Goc Push+Pull > Anxiety+Habit mi?
4. Pazar raporu dijital davranisla uyumlu mu?
5. Iki URL ayni `independence_root` mu?
6. Gozlemin claim relevance'i dogru mu?

**Cikti:** `05-validation.md`. Adi tarihsel uyumluluk icin korunur; icerik pazar
"dogrulamasi" degil evidence audit'tir.

## Faz 8: Capraz Karsilastirma

**Amac:** Ayni metodoloji surumundeki finalistleri iki eksende karsilastir.

**Kapsam:** Compare'deki her aday ayni Quick kapsamiyla arastirilir: top 5
rakip/ikame profili, top 3 rakip icin Meta + Google ATC var/yok, stratified
review yok. Farkli kapsamla toplanmis adaylar ayni siralamaya girmez.

**Cikti:** Arketip/agirlk farklarini gosteren tablo, tercih ve bir sonraki test.
Farkli arketipler ciplak skorla siralanmaz.

## Faz 9: Brief, BUILD_SMALL Scope ve Ekonomi

**Amac:** Yalniz Faz 5.5 sonucu izin veriyorsa sinirli urun plani hazirla.

**Cikti:** Lean Canvas, Quantified Value Prop, max 4 core ekran/3 ozellik,
monetizasyon, first-party metrik plani, moat, security ve geo/cohort ekonomi.
Deep `08-aso-research.md`: `app` icin ASO; `web_saas` icin SEO/karsilastirma
siteleri, `service` icin yerel arama gorunurlugu ve ASO icin `not_applicable`
kaydi.

**Kural:** Faz 5.5 yurutulmediyse brief `PREBUILD_PENDING` kosullu taslaktir;
gelistirme talimati degildir.

## Faz 10: Seytanin Avukati

**Amac:** Deger, usability, fizibilite, viability, dagitim, retention ve
regulasyon varsayimlarini karsi kanitla kir.

**Cikti:** Varsayim tablosu, fatal gate audit'i, worst case ve karar matrisi
uygunluk kontrolu.

## Okur Incelemesi (Numarasiz, Standard/Deep)

**Amac:** Raporu yazmayan bir okurun, raporun guncel revizyonunu
`report-writing.md` basari olcutune gore incelemesi ve bulunan sorunlarin
kapatilmasi.

**Cikti:** `data/reader-review.md` (`templates/reader-review-template.md`): 11 olcut,
bulunan sorunlar, en az 10 (hedef 12) benzersiz iddia kontrolu ve
`- İncelenen revizyon: <hash>` satiri. Iddia kimligi normalize iddia metni +
normalize yerdir; ayni evidence kaydi farkli iddialari destekleyebilir. Ayni
iddia + yer tekrari sayilmaz ve hatadir; "Kanıt kaydı" hucresi yalniz var olan
evidence ID'leri tasir, bilinmeyen veya eksik ID hatadir.

**Akis:** Okur inceler → yazar duzeltir ve durumlari doldurur (revizyon satirina
dokunmaz) → ayni bagimsiz okur guncel raporu yeniden okur, duzeltmeleri ve
iddialari kontrol eder, sonra `python3 scripts/evidence_tool.py revision
<output-dir>` ciktisini revizyon satirina yazar. Komut salt okunurdur; hicbir komut
incelemeyi onaylamaz veya yeniden baglamaz. Sonradan REPORT metni veya evidence
degisirse inceleme bayatlar.

**Gate:** Tum olcutler `GEÇTİ`; `Açık` sorun ve `Hayır` iddia yok; revizyon guncel;
`validate` gecer. Ayrinti: `report-writing.md` §13.

## Portfoy ve INDEX (Numarasiz, tum v4 modlari)

**Amac:** Kosunun portfoydeki yerini ve insan deneyine devrini, arastirma
sonucundan ayri tutmak.

**Cikti:** Her v4 kosusu icin `data/portfolio.json`
(`schemas/portfolio-entry.schema.json`): `title`, `lifecycle` (`active` |
`archived` | `superseded`), `superseded_by`, `reason`, `handoff`. `handoff`
`null` veya `owner`, `state` (`blocked` | `ready` | `in_progress` | `completed` |
`not_planned`), `prerequisites`, `next_action`, `plan_path`,
`result_evidence_ids` alanlaridir.

**Kurallar:**

- `assessment.json` `status` yalniz arastirma/build durumudur; arsiv ve yerine
  gecme portfoy bilgisidir. Lifecycle degisince arastirma durumu ve skorlar
  degismez; portfoy `BUILD_SMALL` yetkilendirmez.
- `superseded` gerekce ve gecerli baska bir v4 kosu klasoru ister; `archived`
  gerekce ister; `active` ve `archived`'da `superseded_by` `null`dir.
- `owner` mevcut deney planindaki `owner:` rolu olur; kisi uydurulmaz. Onkosul,
  sonraki adim ve sonuc kayitlari ayri alanlardadir. `completed` yalniz gercek,
  gozlenmis deney/first-party sonuc kayitlariyla; `blocked` onkosulla yazilir.
  Deney plani veya plandaki `owner:` rolu yoksa `handoff` `null` kalir ve INDEX bunu
  atanmamis olarak gosterir; plan veya rol uydurulmaz.

**Adim:** `python3 scripts/portfolio_tool.py render` ve
`python3 scripts/portfolio_tool.py validate` (varsayilan `output`). Render
`output/INDEX.md` icindeki `portfolio:scoreboard` ve `portfolio:handoff` bolgelerini
uretir; bu bolgeler elle duzenlenmez. Legacy satirlar, Compare turlari,
destekleyici analizler ve tarihsel notlar bolgelerin disinda kalir. Arsivlenen
ve yerine gecilen kosular aktif deney kuyrugunda gosterilmez.

## MVP Sonrasi

Onceden yazilan aktivasyon, retention ve ekonomi esikleri kohort bazli izlenir:

- iki ardisik kohort tum esikleri gecer -> `SCALE`
- deger/aktivasyon gecer, tek alt metrik kalir -> `ITERATE`
- deger veya retention iki kohort kalir -> `STOP`

Detay: `launch-playbook.md`.
