# Pipeline Tanimlari — v4.0

> Faz sahipligi ve gate'ler icin kanonik ozet. Puanlama:
> `scoring-model.md`; kanit: `evidence-model.md`; Faz 5.5:
> `pre-build-validation.md`.

## Research Contract Preflight (Numarasiz)

**Amac:** Problem, segment, geo, platform, asama, arketip ve risk modifier'larini
kilitle.

**Cikti:** `data/assessment.json` baslangic alanlari.

**Gate:** Tek birincil arketip secilmis; belirsiz ve skoru degistiren secim
kullaniciya sorulmus; hedef segment/geo acik.

## Faz 1: Problem Havuzu

**Amac:** Somut, tekrarlanan ve mobilde anlamli problemleri bul.

**Cikti:** Kim, son ne zaman, status quo, harcanan zaman/para ve mobil uygunluk
iceren problem listesi.

**Gate:** Coklu fikir kesfinde min 15 problem ve 3 kategori. Tek fikir analizinde
problemin en az bir spesifik segmenti ve ikameleri tanimli.

## Faz 2: Keyword ve Kanal Cluster

**Amac:** Arama terimlerini ve kullanicilarin gercekte bulundugu kanallari esle.

**Cikti:** Keyword cluster + watering-hole + app disi ikame listesi.

**Gate:** Her problem icin aranabilir terimler ve en az bir erisim kanali; yoksa
dagitim claim'i `not_found_after_protocol` olarak kaydedilir.

## Faz 3: Hizli Pazar Taramasi

**Amac:** Pazar proxy'lerini, ikameleri ve fatal gate adaylarini erken tara.

**Cikti:** Lider/rakipler, storefront-bazli metadata, arama/trend, ikameler,
hedef geo ve ilk evidence kayitlari.

**Kural:** Rating fatal gate degildir; `E2/supporting` proxy'dir. Rakip app yoksa
manuel workflow, web urunu ve hizmet aranir.

## Faz 4: Rakip ve Davranis Analizi

**Amac:** Rakip, ikame, review, fiyat, JTBD, dagitim, reklam ve visual pattern'leri
incele.

**9 adim:**

1. Rakip + ikame listesi
2. Metadata ve storefront kaydi
3. Stratified review mining
4. Reddit/community + JTBD Forces
5. Fiyat ve gercek odeme davranisi
6. Ozellik/wedge ve Deep'te 2x2
7. Platform cross-check
8. Ad/channel intelligence
9. Onboarding, paywall ve screenshot visual intelligence

**Review minimumu (Standard/Deep):** Top 5 rakip, hedef 30/min 15 yorum; 1-2,
3 ve 4-5 yildizdan en az 5'er; son 12 ay/surum/storefront kaydi.

**Cikti sahipligi:**

- `02-competitor-analysis.md`: adim 1-2, 4-9
- `03-review-mining.md`: adim 3

## Faz 5: Iki Eksenli Degerlendirme

**Amac:** Arketip-bazli Firsat Cekiciligi ile Kanit Gucu'nu ayri hesapla.

**Cikti:** `04-scoring.md` + tamamlanmis `data/assessment.json`.

**Gate:** Fatal gate'ler kanitli; agirligi sifir olmayan boyutlar low/base/high
puanli veya acikca `null`; en riskli uc varsayim dereceli.

**Masa basi kararlari:** `ELENDIR`, `BELIRSIZ`, `TESTE_DEGER`,
`TEST_ONCELIKLI`. Masa basi arastirmasi GO veya BUILD karari vermez.

## Faz 5.5: Build-Oncesi Dogrulama

**Amac:** En riskli varsayimi uygun davranis deneyiyle test et.

**Cikti:** Standard/Deep'te `06-prebuild-plan.md`; insan deneyi tamamlanirsa yeni
evidence kayitlari ve assessment guncellemesi.

**Gate:** `BUILD_SMALL` icin firsat low >=60, genel kanit B+, top risk B+ ve en az
bir urun-spesifik E3+ davranis. Aksi `TESTE_DEVAM`, `PIVOT` veya `KILL`.

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

**Cikti:** Arketip/agirlk farklarini gosteren tablo, tercih ve bir sonraki test.

## Faz 9: Brief, BUILD_SMALL Scope ve Ekonomi

**Amac:** Yalniz Faz 5.5 sonucu izin veriyorsa sinirli urun plani hazirla.

**Cikti:** Lean Canvas, Quantified Value Prop, max 4 core ekran/3 ozellik,
monetizasyon, first-party metrik plani, moat, security ve geo/cohort ekonomi.

**Kural:** Faz 5.5 yurutulmediyse brief `PREBUILD_PENDING` kosullu taslaktir;
gelistirme talimati degildir.

## Faz 10: Seytanin Avukati

**Amac:** Deger, usability, fizibilite, viability, dagitim, retention ve
regulasyon varsayimlarini karsi kanitla kir.

**Cikti:** Varsayim tablosu, fatal gate audit'i, worst case ve karar matrisi
uygunluk kontrolu.

## MVP Sonrasi

Onceden yazilan aktivasyon, retention ve ekonomi esikleri kohort bazli izlenir:

- iki ardisik kohort tum esikleri gecer -> `SCALE`
- deger/aktivasyon gecer, tek alt metrik kalir -> `ITERATE`
- deger veya retention iki kohort kalir -> `STOP`

Detay: `launch-playbook.md`.
