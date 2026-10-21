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
  basliklar kullanilmaz.
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
| 14 | `## Ek A — Terimler sözlüğü` | Terimler |
| 15 | `## Ek B — Ana kaynaklar (türüne göre)` | Kaynaklar |
| 16 | `## Ek C — Araştırma arşivi (denetim için)` | Claim/evidence kimlikleri, faz dosyalari |

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
- Gozlem cumlelerinde kaynagin turu belirtilir:

| Etiket | Anlami |
|---|---|
| gözlem | Arastirmacinin dogrudan gordugu: store sayfasi, fiyat sayfasi, reklam kutuphanesi, form |
| şirket beyanı | Sirketin kendisi hakkinda soyledigi, bagimsiz dogrulanmamis bilgi |
| bağımsız kaynak | Resmi kurum, mahkeme, SEC dosyasi, basin, test kurulusu, akademik calisma |
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

## 7. Dil Kurallari

- Tam cumle kullanilir; kimin ne yaptigi, neyin olculdugu ve neden onemli oldugu
  yazilir. Telgraf dili kullanilmaz:

| Kullanma | Kullan |
|---|---|
| Paid/affiliate doymus | Buyuk rakipler reklam ve satis ortakligi kanallarinda yogun bicimde aktif. |
| Store vocabulary dar | App Store'da bu is icin arama onerisi ureten ifade cok az. |
| Giris dalgasi 0 rating | Son 12 ayda cikan 16 uygulamanin 15'i 13 veya daha az degerlendirmede kaldi. |
| CAC negatif | Musteriden beklenen gelir, musteriyi kazanmak icin yapilan harcamayi karsilamiyor. |
| BELIRSIZ — park et | Gelistirmeye baslamayi onermiyoruz; cunku ... |

- Turkce karsiligi anlami tasiyan terim Turkcelestirilir. Gerekli teknik terim ilk
  kullanildigi yerde aciklanir ve Ek A'ya yazilir:

| Terim | Turkce karsilik / aciklama |
|---|---|
| wedge | ayirt edici avantaj: kullanicinin bizi secmesini saglayacak belirgin ustunluk |
| CAC | musteri edinme maliyeti: odeme yapan bir musteriyi kazanmanin maliyeti |
| LTV | bir musteriden beklenen toplam net gelir |
| concierge | islemlerin ekip tarafindan elle yurutuldugu hizmet |
| on-device | cihaz uzerinde calisma: islemin sirket sunucusu yerine kullanicinin cihazinda yapilmasi |
| opt-out | kaldirma talebi |
| data broker | veri simsari |
| affiliate | satis ortakligi |
| paywall | odeme ekrani |
| retention / churn | elde tutma / aboneligi birakma |
| fatal gate | durdurucu engel |
| JTBD | kullanicinin yapmak istedigi is |
| ASO | uygulama magazasi optimizasyonu |
| IAP | uygulama ici satin alma |
| benchmark | sektor ortalamasi |
| SERP | arama sonuc sayfasi |

- Tablolar kisa olabilir ama okurun anlami tahmin etmesini gerektirmez:
  "6/30" yerine "incelenen 30 reklamin 6'si".
- Her oranda pay ve payda yazilir; orneklem rastgele degilse "orneklem ici" denir.
- Sayi bicimi Turkcedir: `1.000`, `%2,7`, `95,88 $`.
- Yazim TDK'ya uyar: yabanci cins isimlere kesme isareti konmaz (`spamin`),
  `kendin yap` ayri yazilir. Ayni kavram rapor boyunca tek adla anilir.
- Karar ve durum kodlari (`BELIRSIZ`, `DESK_RESEARCH_COMPLETE`) ilk gectigi yerde
  sade karsiligiyla verilir.

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
5. Varsa sonraki test: Faz 5.5 sozlesme alanlari sade Turkce tabloyla
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
  gerçekçi mi?` ozet tablosu.

## 11. Validator Kontrolleri

`python3 scripts/evidence_tool.py validate` `analysis_date` degeri **2026-10-20 ve
sonrasi** olan raporlarda su kurallari uygular. Daha eski v4.0 raporlari geriye
donuk kontrol edilmez; yeniden yazilirlarsa bu sozlesmeye uyulur.

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

Uyari:

- Govdedeki URL `evidence.jsonl` kayitlarinda yok.

## 12. PDF

Paylasim kopyasi icin:

```bash
python3 scripts/evidence_tool.py pdf output/{tarih}-{konu}
```

Komut once `validate` calistirir; gecmezse PDF uretmez. `pandoc` ve bir Chromium
tabanli tarayici gerekir (`--browser` veya `REPORT_PDF_BROWSER` ile secilir).
Stil: `templates/report-pdf.css`.
