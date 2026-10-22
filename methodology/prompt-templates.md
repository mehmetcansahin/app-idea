# App Fikri Arastirma Prompt Sablonlari — v4.0

> Bu sablonlar workflow yardimcisidir. Skor, kanit ve deney kurallari kanonik
> metodoloji dosyalarindan gelir. Mod ve urun turu kapsami
> `data-collection-protocol.md` Rakip kapsami ve Urun Turu tablolarindadir.

## Preflight

```text
Bu fikir icin Research Contract olustur:
- problem/JTBD ve spesifik hedef segment
- mod: quick / standard / deep (compare'de her aday quick)
- urun turu (product_type): app / web_saas / service
- platform veya hizmet kanali ve 3-5 hedef geo/storefront
- birincil arketip: consumer_utility / consumer_subscription / b2b_prosumer /
  marketplace_network
- risk modifier'lari
- karar asamasi: desk_research / prebuild_validation / post_mvp

Iki arketip makulse ve agirliklar sonucu degistirecekse kullaniciya sor. Urun turu
yalniz toplama kapsamini belirler; arketip agirliklari, fatal gate'ler ve karar
esikleri ayni kalir. Urun turu belirsizse (ornek: app mi hizmet mi) kullaniciya sor.
```

## Faz 1-2: Problem, Ikame ve Kanal

```text
[ALAN] icinde kullanicinin son spesifik davranisiyla tanimlanabilen problemleri
bul. Her problem icin kim, ne zaman, status quo, harcanan zaman/para, urun turune
uygunluk (app'te mobil), app-disi ikame, keyword cluster ve watering-hole yaz.
Gelecek niyeti gecmis davranis gibi sunma.
```

## Faz 3: Hizli Tarama

```text
[FIKIR] icin ayni JTBD'yi cozen app, web urunu, hizmet ve manuel workflow'lari
tara. Metadata'yi product_type'a gore URL ve tarihle kaydet:
- app: store URL, storefront, platform, rating count, fiyat/IAP, app yasi
- web_saas: fiyat/plan/limit, deneme veya demo, aciklanan musteri, guvenlik/uyum
  sayfasi, self-serve veya satis ekibi
- service: saglayici (lisans, konum, hizmet alani), teklif ve fiyat, teslim suresi,
  rezervasyon/teklif akisi, yerel review sayisi
Non-app'te store metadata, store review ve ASO arama; bunun yerine tek bir
`<prefix>-collection-scope` `not_applicable` kaydi yaz. Rating ve review puanini
E2/supporting proxy olarak kullan; fatal gate yapma. Trend, geo ve dagitim
claim'leri icin bagimsiz ve karsit kaynak ara. Standard/Deep'te pazar buyuklugunu
en az 3 yayincinin tahmin dagilimi, resmi dosyalar ve davranis sayilariyla kaydet;
tek bir rakam uydurma. Karar-kritik alan bulunamazsa en az 3 sorgu varyanti ve 2
kaynak ailesi dene, sonra `not_found_after_protocol` ile dur; kozmetik profil
alaninda tek tarama yap. Her bulguyu evidence JSONL sozlesmesine gore kaydet.
```

## Faz 4: Rakip ve Review

Mod belirtilmeden kullanilmaz; asagidaki iki sablondan moda uyani secilir.

### Quick ve Compare adayi

```text
Mod: Quick (Compare'deki her aday icin ayni kapsam). Top 5 rakip/ikame icin sirket
profili topla: kurulus ve urun baslangic yili, sahiplik/fonlama, calisan araligi,
aciklanan kullanici/gelir, platform veya hizmet kanali, reklam edilen ve otomatik
calisan kapsam, sinirlar. Profil alanlari kozmetiktir: tek tarama yap, bulunamayani
tabloda "bulunamadı" yaz ve kaydin limitations dizisine ekle; alan bir skor, gate
veya RAT claim'ine dayanak oluyorsa karar-kritik yokluk protokolunu uygula. Top 3
rakip icin Meta Ad Library ve Google Ads Transparency Center'da yalniz var/yok,
aktif sayi ve hedef URL turunu kaydet (`ad_library` + screenshot). TikTok, mesaj
acisi kodlamasi, organik kanal sahipligi, visual intelligence ve stratified review
yapma; tekil bir yorum alintisini genelleme. Community verisini JTBD
Push/Pull/Anxiety/Habit ile kisaca analiz et. Fiyat ve odeme davranisini
claim/evidence ID'lerine bagla.
```

### Standard ve Deep

```text
Mod: Standard/Deep. Top 10 rakip/ikame matrisi olustur ve her biri icin sirket
profilini topla (Quick ile ayni alanlar ve ayni yokluk kurali). Top 5 rakip icin son
12 aydan stratified review sample topla; kaynak product_type'a gore:
- app: App Store/Play yorumlari, storefront ve version ile
- web_saas: G2, Capterra veya TrustRadius yorumlari, platform ve listing URL'si ile
- service: Google Business Profile, Yelp, Trustpilot veya marketplace yorumlari,
  listing URL'si ve konum/hizmet alani ile
1-2, 3 ve 4-5 yildizdan min 5'er, hedef 30/min 15. Eksik tabakayi baska kaynaktan
doldurma; protokoldeki status ile kaydet. Tema frekansini yalniz sample
denominator'u icinde raporla. Community verisini JTBD Push/Pull/Anxiety/Habit ile
analiz et. Bagimsiz basari olcumlerini sirket iddialarindan ayir. Top 5 rakip icin
Meta, Google ATC ve TikTok ad/channel kayitlarini (`ad_library`), organik kanal
sahipligini (min 8 web arama sorgusu, video, sponsorluk, topluluk, urun turune gore
liste gorunurlugu) ve visual intelligence'i (app: store/onboarding/paywall;
web_saas: ana sayfa/fiyat/deneme-demo; service: teklif/rezervasyon akisi)
claim/evidence ID'lerine bagla.
```

## Faz 5: Iki Eksenli Degerlendirme

```text
`methodology/scoring-model.md` kullan:
1. Fatal gate'leri evidence ID'leriyle clear/blocked/unknown yap.
2. Arketipin agirligi sifir olmayan her boyutuna 1-5 low/base/high ver; veri yoksa
   null kullan. product_type agirliklari degistirmez.
3. Opportunity low/base/high hesapla.
4. RAT ile en riskli varsayimlari sirala. Her varsayima
   `product_specific_evidence_ids` yaz: masa basinda `[]`; yalniz ayni claim/idea
   icin gozlenmis, direct/direct, supports, E3/E4, experiment veya first_party ve
   source_ref/artifact_path tasiyan kayitlar baglanir. Rakip URL'si baglanmaz.
5. `evidence-model.md` ile claim ve overall A-D hesapla.
6. Asamaya uygun karar matrisini uygula. Desk research build/scale karari vermez.
7. Sonucu `data/assessment.json` sozlesmesine yaz (`product_type` dahil).
```

## Faz 5.5: Deney Sozlesmesi

```text
En riskli claim icin landing'i otomatik varsayma. Risk turune gore interview,
deposit/preorder/LOI, competitor prototype, technical spike, concierge retention,
channel veya liquidity testi sec. Segment, orneklem, baseline/MDE, metric,
threshold derivation, guardrail, stopping rule, pass/fail aksiyonu ve
privacy/refund kosullarini onceden yaz. `owner:` alanina deneyi yurutecek insan
rolunu yaz (ornek: kurucu); kullanici kisi vermediyse isim uydurma, rol de belli
degilse alani bos birakip bunu acikca belirt. Deneye baslamak icin gereken
onkosullari ayri listele. Waitlist max E1'dir; yuzde guven uretme.
```

## Faz 5.5: Sonuc Isleme ve Devir

```text
Yalniz insan deneyinden gercek sonuc geldiyse: her sonucu evidence kaydi yaz
(source_type experiment veya first_party, status observed, observation_quality
direct, claim_relevance direct, RAT ile ayni claim_id ve idea_id, bos olmayan
source_ref veya artifact_path). Yalniz E3/E4 ve direction supports kayitlarini
ilgili RAT'in `product_specific_evidence_ids` dizisine ekle; curuten veya zayif
sonuclari da kaydet ama baglama. Karar matrisini yeniden uygula. Sonra
`data/portfolio.json` `handoff`'unu guncelle: owner (plandaki rol), state,
prerequisites, next_action, plan_path, result_evidence_ids. Sonuc yoksa state'i
completed yapma ve sonuc kaydi uydurma. REPORT metni veya evidence degisirse okur
incelemesi yeniden yapilir.
```

## Faz 7: Evidence Audit

```text
Kritik claim'leri audit et: observation vs inference, source root independence,
freshness, geo/storefront, behavior vs stated intent, missingness, sample
denominator, contradicting evidence. Iki URL ayni primary raporu aktariyorsa tek
root say. Yokluk kayitlarinin protokole uydugunu ve `not_applicable` kaydinin
yokluk diye sunulmadigini kontrol et. Audit sonucunu `05-validation.md` icine yaz.
```

## Faz 8: Compare

```text
Yalniz ayni methodology version raporlarini karsilastir. Her aday ayni Quick
kapsamiyla arastirilmis olmali: top 5 rakip/ikame profili, top 3 rakip icin Meta +
Google ATC var/yok, stratified review yok; farkli kapsamli adayi ayni siraya koyma.
Sirayi fatal gate, overall evidence grade, opportunity interval, top-risk test cost
ve operasyon kisitlarina gore kur. Farkli arketiplerin agirliklarini acikla; ciplak
skoru tek gerekce yapma. Her aday kendi data/portfolio.json'unu tasir; Compare turu
INDEX'te uretilen bolgelerin disinda elle yazilir.
```

## Faz 9: Brief ve Ekonomi

```text
Faz 5.5 tamamlanmadiysa brief'i PREBUILD_PENDING kosullu taslak yap. BUILD_SMALL
yalniz bagli urun-spesifik E3/E4 kaydiyla gecerlidir; varsa max 4 core ekran, 3
ozellik ve gerekirse 1 paywall sinirla. Deep arama gorunurlugu: app icin ASO;
web_saas icin SEO/karsilastirma siteleri; service icin yerel arama ve rehber
listeleri (non-app'te ASO `not_applicable`). Pre-launch ekonomiyi benchmark
senaryosu olarak etiketle; D30/D90 realized ARPPU, payback, brut katki ve retention
kohortlarini first-party veri plani olarak yaz. AI variable cost ve geo sensitivity
gerekiyorsa ekle.
```

## Faz 10: Seytanin Avukati

```text
Value, usability, feasibility, viability, retention, distribution, regulation ve
marketplace ise liquidity varsayimlarina guclu karsit kanit ara. Yeni fatal gate,
unresolved contradiction veya evidence downgrade varsa assessment ve karari
yeniden hesapla.
```

## Final Rapor

```text
`templates/report-template.md` iskeletini ve `methodology/report-writing.md`
kurallarini kullan. Moda ve product_type'a ait olmayan ⚐ alt bolumleri yazma;
zorunlu basliklari koru. Konuya ilk kez bakan okur icin tam cumlelerle yaz;
terimleri ilk geciste acikla ve Ek A'ya ekle. Her numarali bolumu sorusuyla ac ve
"Bu bölümün sonucu" kutusuyla kapat; bulgulari uc parcali yaz. Kritik iddialari
govdede evidence kaydindaki URL ile bagla; claim/evidence ID'lerini yalniz Ek C'de
listele. REPORT, assessment.json ve evidence ledger ayni arketip, skor, grade,
karar ve durumu gostersin. Portfoy lifecycle'ini ve devir durumunu rapora yazma.
`## Özet` yazma; evidence_tool render (ozeti bolum sonuc kutularindan uretir),
Standard/Deep'te okur incelemesi, validate, data/portfolio.json ve portfolio_tool
render + validate sirasini izle.
```

## Okur Incelemesi (Standard/Deep)

Raporu yazmayan ayri bir alt ajana verilir; alt ajan yalniz
`data/reader-review.md` yazar.

```text
[CIKTI_KLASORU]/REPORT.md'yi konuya ilk kez bakan bir okur olarak bastan sona oku;
anlamak icin data/ veya phases/ acma. methodology/report-writing.md sozlesmesine
gore templates/reader-review-template.md'deki 11 olcutu GEÇTİ veya KALDI olarak
degerlendir; Not sutununa satir numarasi yaz. Somut her sorunu (aciklanmamis terim,
telgraf cumle, tahmin gerektiren tablo hucresi, bolumler arasi tutarsiz sayi,
yanlis capraz referans, yazim hatasi, kaynak turu belirsiz karar iddiasi, kapsam
disi ornek, moda veya urun turune ait olmayan alt bolum) yer, kisa alinti, `Açık`
durumu ve onerilen duzeltmeyle listele. Zevk tercihi ekleme. Bolum 2-10'a yayilan
en az 10, hedef 12 benzersiz iddiayi data/evidence.jsonl ile karsilastir: ayni
iddia metni + yer satirini tekrar yazma (sayilmaz ve hatadir); ayni evidence kaydi
farkli iddialarda kullanilabilir. "Kanıt kaydı" hucresine yalniz kayitta var olan
evidence_id'leri yaz (virgul/noktali virgulle); aciklamayi "Uyuyor mu?" sutununa
yaz. Tutmayani `Hayır` yaz ve
sorunlara da ekle. Iddia kontrolunu bitirdikten sonra
`python3 scripts/evidence_tool.py revision [CIKTI_KLASORU]` ciktisini
`- İncelenen revizyon: <hash>` satirina yaz. Sonucu
[CIKTI_KLASORU]/data/reader-review.md'ye yaz; baska dosyaya dokunma.
```

## Okur Dogrulama Turu (Standard/Deep)

Yazar sorunlari duzeltip Durum/Cozum sutunlarini doldurduktan sonra ayni bagimsiz
okura verilir. Yazar revizyon satirini degistirmez; hicbir komut incelemeyi
onaylamaz veya yeniden baglamaz.

```text
[CIKTI_KLASORU]/REPORT.md'nin guncel halini bastan sona yeniden oku. data/
reader-review.md'deki her sorunun duzeltmesini raporda dogrula; dogrulanamayani
`Açık` yap, yeni sorunlari ekle ve olcut sonuclarini guncel metne gore yeniden
ver. Iddia kontrolunu guncel metin ve data/evidence.jsonl ile yeniden yap (en az
10, hedef 12 benzersiz). Ancak bu kontroller bittikten sonra
`python3 scripts/evidence_tool.py revision [CIKTI_KLASORU]` ciktisini
`- İncelenen revizyon:` satirina yaz. Yalniz data/reader-review.md'yi degistir.
```

## Portfoy Kaydi

```text
[CIKTI_KLASORU]/data/portfolio.json yaz: title (INDEX'te gorunecek kisa konu),
lifecycle "active", superseded_by null, reason null. handoff: 06-prebuild-plan.md'de
`owner:` rolu olan bir deney varsa {owner: plandaki rol, state, prerequisites,
next_action, plan_path: "phases/06-prebuild-plan.md", result_evidence_ids: []};
plan veya rol yoksa null. state: onkosul varsa "blocked" ve onkosullari listele,
yoksa "ready"; "in_progress" yalniz insan deneyi baslattigini bildirdiyse;
"completed" yalniz result_evidence_ids gercek gozlenmis deney/first-party
kayitlarini gosterdiginde; "not_planned" kullanici deney yapilmayacagina karar
verdiyse. Yeni kosu eski bir kosunun yerine geciyorsa yalniz eski kosunun
portfolio.json'unu lifecycle "superseded", superseded_by yeni klasor adi ve reason
ile guncelle; eski raporu, skoru ve assessment durumunu degistirme. Sonra
`python3 scripts/portfolio_tool.py render` ve
`python3 scripts/portfolio_tool.py validate` calistir.
```
