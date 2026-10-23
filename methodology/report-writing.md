# Rapor Yazim Sozlesmesi — v4.0

> `REPORT.md`'nin dili, yapisi ve okunabilirligi icin yetkili kaynak. Skor, kanit ve
> deney kurallari `scoring-model.md`, `evidence-model.md` ve
> `pre-build-validation.md` dosyalarinda kalir; bu dosya o sonuclarin okura nasil
> anlatilacagini belirler. Sablon: `templates/report-template.md`.

## 1. Okur ve Basari Olcutu

Okur konuya ilk kez bakan, Turkce okuyan bir karar vericidir. Terimleri cozmek,
eksik baglantilari kurmak veya arastirma dosyalarini acarak anlami tamamlamak
okura birakilmaz.

Basari olcutu: Okur her bolumun sonunda yazara sormadan su sorulari
cevaplayabilir:

1. Ne ogrendim?
2. Bu neden onemli?
3. Karari nasil etkiliyor?
4. Bu projeyi hayata gecirmek mantikli mi?

## 2. Baslik ve Kapsam

- Baslik konu etiketi degil, degerlendirilen urundur: kullanici + is + urun turu +
  geo/platform. Ornek: "ABD'de kisi-arama sitelerinden adres ve telefon kaldirma:
  iPhone uygulamasi fikri". "Dijital ayak izi silme" gibi incelenen urunden genis
  basliklar kullanilmaz. Basliktaki urun turu `assessment.json` `product_type`
  degeriyle uyusur: `app` uygulama, `web_saas` web urunu/SaaS, `service` hizmet.
- Bolum 1 kullaniciyi, sorunu ve urun onerisini tam cumlelerle tarif eder.
- `### Kapsam dışında kalanlar` zorunludur. Arastirilmayan ihtiyaclar burada
  listelenir; sonuc bunlara genellenmez.
- Kapsam disi bir ihtiyac, urunun cozdugu sorun gibi orneklenmez.

## 3. Zorunlu Yapi

Basliklar sablondaki metinle birebir yazilir; validator bir kismini kontrol eder
(§11).

| Sira | Baslik | Cevapladigi soru |
|---|---|---|
| 0 | `# [urun basligi]` + ust bilgi | Ne degerlendirildi, karar ne? |
| 1 | `## Kısa cevap: Bu projeyi hayata geçirmek mantıklı mı?` | Tek paragrafta karar ve gerekce |
| 2 | `## Bu rapor nasıl okunmalı?` | Akis, bulgu bicimi, kaynak turleri, puan/not |
| 3 | `## 1. Neyi değerlendirdik?` | Kullanici, sorun, urun, kapsam disi |
| 4 | `## 2. Kullanıcının sorunu ...` | Sorun gercek mi, bugun nasil cozuluyor? |
| 5 | `## 3. Pazar ...` | Ne kadar buyuk, kimler var, nereye gidiyor? |
| 6 | `## 4. Mevcut çözümler ...` | Rakipler neyi, nasil, ne kadar iyi yapiyor? |
| 7 | `## 5. Önerdiğimiz ürün ...` | Kullanici neden bizi secsin? |
| 8 | `## 6. Kullanıcıya nasıl ulaşılır? ...` | Kanallar, anahtar kelimeler, reklamlar |
| 9 | `## 7. Para kazanma ...` | Gelir edinme maliyetini karsilar mi? |
| 10 | `## 8. Hukuk, platform, teknik ...` | Projeyi durduracak engel var mi? |
| 11 | `## 9. Puanlama: sayılar nasıl okunur?` | Skor ve not ne demek? |
| 12 | `## 10. Karar ve öneri` | Ne yapiyoruz, neden, ne degistirir? |
| 13 | `## 11. Kanıtın sınırları` | Neye ne kadar guvenebiliriz? |
| 14 | `## Özet` (otomatik, §14) | Karar, puan, not ve her bolumun sonucu tek yerde |
| 15 | `## Ek A — Terimler sözlüğü` | Terimler |
| 16 | `## Ek B — Ana kaynaklar (türüne göre)` | Kaynaklar |
| 17 | `## Ek C — Araştırma arşivi (denetim için)` | Claim/evidence kimlikleri, faz dosyalari |

Quick Scan ayni iskeleti kisa tutar; sablonda `⚐` ile isaretli alt bolumler moda
gore eklenir.

Her numarali bolum (`## N. ...`):

- `Bu bölüm şu soruyu yanıtlıyor: ...` cumlesiyle baslar.
- `> **Bu bölümün sonucu.** Ne öğrendik: ... Neden önemli: ... Karara etkisi: ...`
  kutusuyla biter. Uc etiket ayni paragrafta yer alir.

## 4. Bulgu Bicimi

Onemli bulgular rapor boyunca `Bulgu 1`, `Bulgu 2` ... diye tek sirayla
numaralanir ve uc parcalidir:

```markdown
### Bulgu 3 — [Bulguyu tam cumleyle soyleyen baslik]

**Ne gözlemledik?** [Kaynakli gozlem; kaynak turu etiketli]

**Ürün açısından anlamı.** [Yazarin yorumu; neden onemli]

**Henüz varamadığımız sonuç.** [Bu gozlemin kanitlamadigi sey]
```

Bulgu numaralari alt bolum numaralariyla karismasin diye `Bulgu 4.1` gibi
iki duzeyli numara kullanilmaz.

## 5. Kaynak ve Iddia Turleri

- Karari etkileyen her iddianin yaninda dogrudan tiklanabilir kaynak bulunur.
  Baglanti metni kaynagi tarif eder (`[Kaliforniya Gizlilik Koruma Ajansı
  duyurusu, 12 Ekim 2026](...)`), ham URL degil.
- Govdedeki URL'ler `data/evidence.jsonl` kayitlarindan gelir; kaydi olmayan URL
  validator uyarisi uretir.
- Claim/evidence kimlikleri (`[abc-wedge]`) ve `phases/` yollari govdede
  kullanilmaz; yalniz Ek C'de denetim icin listelenir.
- Gozlem cumlelerinde kaynagin turu asagidaki bes etiketten biriyle belirtilir;
  gerekirse virgulden sonra ayrinti eklenir (`şirket beyanı, denetlenmemiş`,
  `yazarın yorumu, kaba çıkarım`). Bu bes etiketin disinda tur adi kullanilmaz ve
  okuma rehberi bes etiketin hepsini tanitir:

| Etiket | Anlami |
|---|---|
| gözlem | Arastirmacinin dogrudan gordugu: store sayfasi, fiyat sayfasi, reklam kutuphanesi, form |
| şirket beyanı | Sirketin kendisi hakkinda soyledigi, bagimsiz dogrulanmamis bilgi |
| bağımsız kaynak | Resmi kurum, mahkeme, SEC dosyasi, basin, test kurulusu, sektor raporu, akademik calisma |
| varsayım | Yalniz hesapta kullanilan, kanit olmayan deger |
| yazarın yorumu | Gozlemden yapilan cikarim; "Ürün açısından anlamı" paragraflari varsayilan olarak yorumdur |

## 6. Ornekler

- Soyut ifadeler kisa orneklerle somutlasir: kullanicinin sorunu, urunun isleyisi,
  ozelligin faydasi.
- Aciklama icin kurgulanan senaryo `> **Örnek senaryo (kurgusal).**` ile baslar.
- Gozlenen kullanici deneyimi `> **Gerçek kullanıcı (uygulama, kaynak, tarih,
  puan):**` ile verilir; ceviri ise belirtilir.
- Belgelenmis bir is akisi `> **Gerçek işleyiş örneği (kaynak).**` ile verilir.
- Ornekler arastirilan kapsamla uyumlu olur.

## 7. Dil Kuralları

- Rapor ve rapordan üretilen çıktılar UTF-8 kodlamasıyla yazılır. Türkçe
  sözcüklerde `ç, ğ, ı, İ, ö, ş, ü` kullanılır; `kanit`, `sonuc`, `kullanici`
  gibi ASCII yazımlar raporun başlık, tablo, açıklama ve özetlerinde bırakılmaz.
  Bozulmuş karakterler (`�`, `Ã`, `Ä±`, `ÅŸ` vb.) kaynak metinden kontrol
  edilerek düzeltilir. Dosya yolu, URL, kimlik ve makine kodu değiştirilmez.
- Tam cümle kullanılır; kimin ne yaptığı, neyin ölçüldüğü ve neden önemli olduğu
  yazılır. Belirsiz özne, eksik yüklem ve sözcüğü sözcüğüne çeviriyle oluşan
  anlatım bozuklukları giderilir. Telgraf dili kullanılmaz:

| Kullanma | Kullan |
|---|---|
| Paid/affiliate doymuş | Büyük rakipler reklam ve satış ortaklığı kanallarında yoğun biçimde aktif. |
| Store vocabulary dar | App Store'da bu iş için arama önerisi üreten ifade çok az. |
| Giriş dalgası 0 rating | Son 12 ayda çıkan 16 uygulamanın 15'i 13 veya daha az değerlendirmede kaldı. |
| CAC negatif | Müşteriden beklenen gelir, müşteriyi kazanmak için yapılan harcamayı karşılamıyor. |
| BELIRSIZ — park et | Geliştirmeye başlamayı önermiyoruz; çünkü ... |

- Türkçe karşılığı anlamı taşıyan terim Türkçeleştirilir. Türkçe cümleye
  açıklamasız İngilizce sözcükler eklenmez. Gerekli teknik terim ilk kullanıldığı
  yerde açıklanır ve Ek A'ya yazılır. Ürün adları, API adları, gerçek arama
  sorguları ve özgün alıntılar korunur; çeviri veya özet ayrıca etiketlenir:

| Terim | Türkçe karşılık / açıklama |
|---|---|
| wedge | ayırt edici avantaj: kullanıcının bizi seçmesini sağlayacak belirgin üstünlük |
| CAC | müşteri edinme maliyeti: ödeme yapan bir müşteriyi kazanmanın maliyeti |
| LTV | bir müşteriden beklenen toplam net gelir |
| concierge | işlemlerin ekip tarafından elle yürütüldüğü hizmet |
| on-device | cihaz üzerinde çalışma: işlemin şirket sunucusu yerine kullanıcının cihazında yapılması |
| opt-out | kaldırma talebi |
| data broker | veri simsarı |
| affiliate | satış ortaklığı |
| paywall | ödeme ekranı |
| retention / churn | elde tutma / aboneliği bırakma |
| fatal gate | durdurucu engel |
| JTBD | kullanıcının yapmak istediği iş |
| ASO | uygulama mağazası optimizasyonu |
| IAP | uygulama içi satın alma |
| benchmark | karşılaştırma ölçütü; bağlama göre sektör ortalaması veya karşılaştırmalı ölçüm |
| SERP | arama sonuç sayfası |

- Tablolar kısa olabilir ama okurun anlamı tahmin etmesini gerektirmez:
  "6/30" yerine "incelenen 30 reklamın 6'sı".
- Her oranda pay ve payda yazılır; örneklem rastgele değilse "örneklem içi" denir.
- Sayı biçimi Türkçedir: `1.000`, `%2,7`, `95,88 $`.
- Yazım TDK'ya uyar: yabancı cins isimlere kesme işareti konmaz (`spamin`),
  `kendin yap` ayrı yazılır. Aynı kavram rapor boyunca tek adla anılır.
- Karar ve durum kodları (`BELIRSIZ`, `DESK_RESEARCH_COMPLETE`) ilk geçtiği yerde
  sade karşılığıyla verilir.
- Dil düzeltmesi bulguyu değiştirmez: gözlem, şirket beyanı, varsayım ve yazar
  yorumu arasındaki ayrım; belirsizlik, olumsuzluk, koşullar, sayılar ve karar
  korunur. Kaynakta bulunmayan bir anlam eklenmez; belirsiz ifade kaynağından
  çözülemiyorsa kesinleştirilmez.
- Son okumada her cümle için "Kim, neyi, hangi koşulda yapıyor; bu bir gözlem mi,
  yorum mu, plan mı?" soruları yanıtlanır. `REPORT.md`, üretilen özet, portföy
  panosu ve varsa HTML/PDF kopyası aynı düzeltmeleri yansıtmalıdır.

## 8. Puan, Not ve Ekonomi Anlatimi

- Firsat Cekiciligi icin yazilir: olcek **20-100** (tum boyutlar 1 ise 20, 5 ise
  100), formul, bir ornek hesap, kotumser/temel/iyimser anlami, sinif esikleri ve
  "basari olasiligi degildir" uyarisi.
- Boyut tablosunda `Ne ölçüyor?` sutunu ve sade gerekce bulunur.
- Kanit Gucu icin A-D tablosu, en riskli varsayimlar sade cumlelerle ve genel
  notun "en riskli uc varsayimin en dusugu" oldugu yazilir.
- Masa basi karar kurallari sirasiyla listelenir; bu fikre hangisinin uygulandigi
  soylenir.
- Rapor `assessment.json` ile ayni firsat araligini (`33 / 46 / 62` bicimi),
  karari ve notu gosterir.
- Ekonomi senaryosunda her girdi `Türü` sutunuyla (bagimsiz kaynak / varsayim /
  sektor ortalamasi) verilir; formul ve sonucun sade okunusu yazilir. Senaryo
  kanit gibi sunulmaz.

## 9. Karar Bolumu

`## N. Karar ve öneri` su alt basliklari tasir:

1. `### Şimdi ne yapmayı öneriyoruz?`
2. `### Bu öneriyi hangi bulgulara dayandırıyoruz?` (bulgu/bolum referansiyla)
3. `### Belirsiz olan tam olarak ne?` — talep, teknik yapilabilirlik, karlilik ve
   kullanicinin bizi tercih etmesi ayri satirlarda
4. `### Hangi yeni bilgi önerimizi değiştirebilir?`
5. Varsa sonraki test: Faz 5.5 sozlesme alanlari sade Turkce tabloyla. Test
   yapilmamissa plan olarak anlatilir; sonucu varmis gibi yazilmaz. Planda belliyse
   deneyi yurutecek insan rolu ve on kosullar yazilir; belli degilse bu acikca
   soylenir, sorumlu uydurulmaz.
6. `### Bu projeyi hayata geçirmek mantıklı mı?` — dogrudan cevap

## 10. Rakip ve Pazar Anlatimi

Toplama adimlari `data-collection-protocol.md` icindedir. Raporda:

- **Rakip profili tablosu:** bu iste ne zamandan beri, sahiplik/fonlama/buyukluk,
  platformlar, fiyat.
- **Isleyis tablosu:** nasil calisiyor ve neyi kapsiyor (sirket beyani), iyi
  yaptigi, yetersiz kaldigi.
- **Ne kadar iyi calisiyorlar:** bagimsiz olcumler; basin testlerinin bagimsizligi
  ve satis ortakligi iliskisi.
- **Ihtiyac tablosu:** hangi kullanici ihtiyacini kim karsiliyor, ne eksik.
- Bolum sonucu rakiplerin bizim urunumuzu neden zorlastirdigini soyler.
- **Pazar:** buyukluk tahminlerinin dagilimi ve bagimsizligi, daha saglam
  dayanaklar, hesaplanamayanlar; harekete gecen kisi/talep sayilari; arz tarafi;
  oyuncularin konumu tablosu; zamanlama.
- **Kanallar:** magaza aramasi ve anahtar kelimeler, web aramasi ve sonuc sayfasi
  sahipligi, ucretli reklam, satis ortakligi ve icerik ureticileri, topluluklar,
  yeni girenlerin sonucu; `Kanal | Kim hâkim? | Hâkimiyet | Yeni bir uygulama için
  gerçekçi mi?` ozet tablosu. `web_saas` ve `service` raporlarinda magaza aramasi
  zorunlu degildir; web aramasi, dogrudan satis/LOI ve hizmet kanallari anlatilir.
  Ozet tablonun sutun basliklari validator icin her urun turunde aynidir.

## 11. Validator Kontrolleri

`python3 scripts/evidence_tool.py validate` `analysis_date` degeri **2026-10-20 ve
sonrasi** olan raporlarda su kurallari uygular. Daha eski v4.0 raporlari geriye
donuk kontrol edilmez; yeniden yazilirlarsa bu sozlesmeye uyulur. Tek istisna okur
incelemesidir: Standard/Deep kosusunda `data/reader-review.md` varsa tarihten
bagimsiz olarak asagidaki okur incelemesi kurallariyla kontrol edilir.

Hata:

- Zorunlu basliklar: `## Kısa cevap`, `## Bu rapor nasıl okunmalı?`,
  `Kapsam dışında kalanlar`, `## N. Karar ve öneri`, `## N. Kanıtın sınırları`,
  `## Ek A — Terimler sözlüğü`.
- Her numarali bolumde acilis sorusu ve uc etiketli `Bu bölümün sonucu` kutusu.
- En az bir `Bulgu N` ve her bulguda uc parca.
- Govdede (ilk `## Ek` basligindan once) evidence/claim kimligi veya `phases/` yolu
  yok.
- Govdede en az bir tiklanabilir kaynak.
- Firsat araligi `assessment.json` ile ayni.
- Govdede kullanilan teknik terim (wedge, CAC, LTV, ARPU, concierge, opt-out,
  data broker, affiliate, fatal gate, JTBD, RAT, ASO, IAP, MDE, payback, churn,
  paywall) Ek A'da tanimli.
- Arastirma kaniti (tum modlar): `evidence.jsonl` icinde `<prefix>-competitor-profile`
  claim'li en az bir kayit; raporda rakip profili tablosu (`Bu işte ne zamandan
  beri?` ve `Platformlar` sutunlari) ve kanal ozeti tablosu (`Kim hâkim?` ve
  `Yeni bir uygulama için gerçekçi mi?` sutunlari).
- Arastirma kaniti (Standard/Deep): `<prefix>-market-size` claim'li en az bir kayit
  ve `<prefix>-distribution` claim'inde en az bir web/video arama sonucu kaydi
  (Google, Bing, DuckDuckGo arama sayfasi veya YouTube sonuc sayfasi URL'si).
- Okur incelemesi (Standard/Deep): 2026-10-20 ve sonrasi raporlarda
  `data/reader-review.md` zorunludur; daha eski raporlarda yoksa hata olmaz, varsa
  ayni kurallarla kontrol edilir. `İnceleyen:` dolu;
  `- İncelenen revizyon: <hash>` satiri var ve guncel rapor/kanit revizyonuna esit;
  11 olcutun hepsi `GEÇTİ`; `Açık` sorun yok; `Kabul edilmedi` sorunlarin gerekcesi
  var; en az 10 benzersiz iddia kontrolu var ve hicbiri `Hayır` degil. Iddia ve yer
  hucresi bos olamaz; tekrar eden kontrol hata verir ve sayilmaz; `Kanıt kaydı`
  hucresi yalniz `evidence.jsonl`'de bulunan evidence ID'lerini tasir, kimliksiz
  satir veya bilinmeyen kimlik hatadir (§13). Quick incelemesi kontrol edilmez.
- `## Özet` var ve bolum sonuc kutulari ile `assessment.json` ile guncel (§14).
  Ozet disindaki kontroller yalniz yazarin yazdigi metne bakar; ozet karar ve firsat
  araligi kontrollerini karsilamaz.

Uyari:

- Govdedeki URL `evidence.jsonl` kayitlarinda yok.
- Standard/Deep'te 8'den az farkli arama sonucu sayfasi kaydedilmis
  (`data-collection-protocol.md` organik kanal adimi en az 8 sorgu ister).
- Okur incelemesinde hic sorun kaydedilmemis.

## 12. PDF

Paylasim kopyasi icin:

```bash
python3 scripts/evidence_tool.py pdf output/{tarih}-{konu}
```

Komut once `validate` calistirir; gecmezse PDF uretmez. `pandoc` ve bir Chromium
tabanli tarayici gerekir (`--browser` veya `REPORT_PDF_BROWSER` ile secilir).
Stil: `templates/report-pdf.css`.

## 13. Okur Incelemesi (Standard/Deep)

Rapor yazildiktan ve `validate` disindaki tum adimlar bittikten sonra, raporu
yazmamis bir okur (ayri alt ajan veya kisi) raporu bu sozlesmeye gore inceler.
Yazarin kendisi okur olamaz.

1. Inceleyen once yalniz `REPORT.md`'yi okur; anlamak icin `data/` veya `phases/`
   acmaz. Iddia kontrolu icin `data/evidence.jsonl` acilir.
2. Sonuc `templates/reader-review-template.md` bicimiyle `data/reader-review.md`
   dosyasina yazilir: 11 olcut, bulunan sorunlar ve iddia kontrolu. Inceleyen
   sorunlari `Açık` durumuyla yazar ve rapora dokunmaz.
3. Yazar her sorunu duzeltir ve durumunu `Düzeltildi` yapar ya da gerekcesiyle
   `Kabul edilmedi` yazar. `Hayır` iddialar duzeltilip `Düzeltildi` olur. Yazar
   `İncelenen revizyon` satirini yazmaz ve degistirmez.
4. Ayni bagimsiz okur guncel `REPORT.md`'yi yeniden okur; duzeltmeleri ve iddia
   kontrollerini guncel kanitla dogrular. Duzeltmeler `KALDI` olcutleri ortadan
   kaldiriyorsa olcut `GEÇTİ` yapilir ve Not sutununa duzeltmenin yeri yazilir.
5. Okur ancak bu kontrolden sonra incelemeyi guncel revizyona baglar (asagida).
6. `validate` bu dosyayi §11'deki kurallarla kontrol eder; gecmeden rapor
   tamamlanmis sayilmaz.

Var olan inceleme ile zorunlu inceleme ayridir: `data/reader-review.md`
2026-10-20 ve sonrasi Standard/Deep raporlarda zorunludur. Daha eski bir
Standard/Deep kosusunda dosya yoksa hata olmaz; dosya varsa tarihten bagimsiz
olarak ayni kurallarla dogrulanir, boylece eski incelemede bulunan sorun veya
eskimis revizyon sessizce gecmez.

### Iddia kontrolu: 10 asgari, 12 hedef

Okur Bolum 2-10'a yayilan 12 iddiayi hedefler; validator en az 10 benzersiz
kontrol ister. Bir kontrolun kimligi normalize iddia metni ile normalize yerin
ciftidir; normalizasyon Markdown vurgusunu, backtick'i, baglanti bicimini ve
kacislari kaldirir, Turkce kurallariyla buyuk/kucuk harf farkini ve fazla
boslugu yok sayar. Ayni kaynak farkli iddialari destekleyebildigi icin ayni
evidence ID birden fazla satirda kullanilabilir; ayni iddia ve yerin tekrari ise
hata verir ve sayilmaz. `Kanıt kaydı` hucresine yalniz evidence ID'leri (virgul,
noktali virgul veya boslukla ayrilmis, istege bagli backtick) yazilir; aciklama
`Uyuyor mu?` sutununa gider.

### Inceleme revizyonu

`- İncelenen revizyon: <hash>` satiri incelemeyi raporun ve kanitin belirli bir
surumune baglar. Revizyon 64 karakterlik kucuk harfli SHA-256 degeridir
(`scripts/evidence_tool.py` `report_revision`) ve su JSON'un UTF-8 baytlarindan
hesaplanir (`ensure_ascii=False`, `sort_keys=True`, ayiricilar `,` ve `:`):

- `report`: `REPORT.md`'nin yazar metni, su sirayla kanonik hale getirilir:
  1. otomatik `## Özet` blogu cevresindeki bos satirlarla birlikte cikarilir,
     yerine tek bos satir (`\n\n`) konur;
  2. `\r\n` satir sonlari `\n` olur;
  3. ilk `## Ek <Harf>` basligi varsa, ondan onceki metnin sonundaki bosluk ve
     satir sonlari kirpilir ve baslikla arasina tam bir bos satir (`\n\n`) konur.
     `render` Ozet'i eklerken bu boslugu ayni bicimde yeniden yazar; bu adim
     sayesinde ilk `render` de sonrakiler de revizyonu degistirmez;
  4. bas/son bosluk kirpilir.

  Bunun disinda hicbir yerde bosluk normallestirilmez. Ozet ayrica tazelik
  kontrolunden gecer (§14).
- `evidence`: `data/evidence.jsonl` kayitlari, `evidence_id`'ye gore sirali.

Guncel revizyonu yazdirmak icin:

```bash
python3 scripts/evidence_tool.py revision output/{tarih}-{konu}
```

Komut yalniz degeri yazdirir; `reader-review.md`'ye yazmaz ve incelemeyi
onaylamaz. `REPORT.md` veya `evidence.jsonl` eksik ya da yapisal olarak
gecersizse deger uretmez ve hata verir. `render` dahil hicbir komut incelemeyi
onaylamaz veya revizyonu yeniden baglamaz. Degeri satira, guncel raporu okuyup
duzeltmeleri ve iddialari kontrol etmis bagimsiz okur yazar.

Yukaridaki kanonik adimlar disinda yazar metninde (bosluk dahil) veya
`evidence.jsonl` kayitlarinda yapilan her degisiklik revizyonu degistirir. Satir
eksikse veya eskimisse `validate` hata verir; inceleme guncel surum icin
yenilenmeden rapor tamamlanmis sayilmaz. `render` ilk calismada da sonrakilerde
de yalniz Ozet'i ve ilk ekten onceki boslugu yeniden yazar; bu incelemeyi
bayatlatmaz.

Quick Scan'de okur incelemesi istege baglidir; Quick'te `data/reader-review.md`
varsa validator onu kontrol etmez.

## 14. Ozet (Otomatik)

Raporun sonunda, eklerden once `## Özet` bolumu bulunur. Yazar bu bolumu yazmaz:
`python3 scripts/evidence_tool.py render <output-dir>` her calistiginda bolumu
`<!-- ozet:start ... -->` / `<!-- ozet:end -->` isaretleri arasina yeniden uretir.

- Ilk paragraf `assessment.json`'dan gelir: karar ve anlami, Firsat Cekiciligi
  araligi ve sinifi, Kanit Gucu, durum.
- Ardindan her numarali bolum icin `Bu bölümün sonucu` kutusunun `Ne öğrendik` ve
  `Karara etkisi` kisimlari listelenir; son satir `Karar ve öneri` bolumune
  yonlendirir.
- Ozeti degistirmek icin kutulari veya `assessment.json`'u duzelt, sonra `render`'i
  yeniden calistir. Elle yapilan degisiklik bir sonraki `render`'da silinir;
  `validate` eskimis veya eksik ozeti hata sayar.
- `render`, bolum sonuc kutusu olmayan eski raporlara dokunmaz. Kutulu eski raporlar
  da `render` ile ozet alir; ozet bir kez eklendikten sonra guncel tutulmasi
  `validate` ile kontrol edilir.
