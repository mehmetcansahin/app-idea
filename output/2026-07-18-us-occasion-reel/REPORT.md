# US Occasion Reel — Quick Scan

**Tarih:** 2026-07-18  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** Consumer Utility  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

**Occasion Reel**, bu karşılaştırmada tek geliştirici için en dengeli adaydır. Kullanıcı 8–30 fotoğraf seçer; uygulama doğum günü, anma, mezuniyet veya yıldönümü için beş dakikadan kısa sürede paylaşılabilir bir video üretir. İlk sürüm üretken video AI'ı kullanmaz: kırpma, Ken Burns hareketi, tarih başlıkları, sesli anlatım ve 9:16/16:9 export cihazda çalışır.

Bu seçim “en yüksek viral tavan” demek değildir. Fotoğraftan AI video daha yüksek tavanlı olabilir; Occasion Reel'in avantajı düşük değişken maliyet, hesap/backend zorunluluğunun olmaması ve kullanıcı şikâyetlerine doğrudan cevap veren güvenilir bir iş akışıdır.

## Kullanici, an ve yapilacak is

- Segment: Önündeki 30 gün içinde gerçek bir doğum günü, anma, mezuniyet veya yıldönümü olan ABD'li iPhone kullanıcısı.
- Tetikleyici: Fotoğraflar telefonda hazırdır fakat zaman çizelgesi kurmak, her fotoğrafı kırpmak, müzik ayarlamak ve export sorunlarıyla uğraşmak istemez.
- Mevcut ikameler: iMovie/Photos, Canva/CapCut şablonları, genel slideshow uygulamaları veya bir yakından yardım istemek.
- İstenen sonuç: Fotoğrafları bulut hesabına yüklemeden, proje kaybetmeden ve haftalık abonelik tuzağı hissetmeden paylaşılabilir bir anı videosu.

## Dogrudan gozlemler

- [SlideShow Maker Photo to Video](https://apps.apple.com/us/app/slideshow-maker-photo-to-video/id924826256) yaklaşık 104K US rating ve haftalık $4.99–$9.99 liste seçenekleri gösterdi ([occasion-slideshow-leader], [occasion-slideshow-pricing]).
- Bağımsız ikinci ürün [Slideshow Maker Video & Photo](https://apps.apple.com/us/app/slideshow-maker-video-photo/id1471839831) yaklaşık 17K rating gösterdi ([occasion-second-competitor]).
- Görünen yorumlarda proje kaybı, yeniden başlama, ödeme sonrasında çıktı alamama, abonelik/iptal karmaşası ve cloud/privacy itirazları vardı ([occasion-reliability-wedge], [occasion-privacy-wedge]). Bu Quick Scan sistematik review-mining değildir; tema oranı çıkarılamaz.
- [Dazz Cam](https://apps.apple.com/us/app/dazz-cam-vintage-camera/id1422471180) yaklaşık 111K rating ve aktif Photo & Video chart görünürlüğüyle kişisel medyayı stilize edip paylaşma davranışının canlı kaldığını destekledi ([occasion-dazz-social]).
- Yeni ve küçük bir [offline before/after video app'i](https://apps.apple.com/us/app/before-after-video-maker/id6779032596), cihazda video üretmenin teknik olarak küçük bir paket ve tek seferlik fiyatla sunulabildiğini gösteriyor ([occasion-local-feasibility]).

Rating, fiyat ve chart konumu yalnız `E2/supporting` proxy'dir; satış, gelir, retention veya yeni bir ürünün kazanacağını kanıtlamaz.

## Cikarim ve wedge

Pazar davranışı kanıtı, “fotoğrafları videoya çevirme” işinin yerleşik olduğunu gösteriyor. Yeni ürünün fırsatı generic slideshow yapmak değildir. Test edilecek wedge şudur:

1. Yalnız dört yüksek-niyetli occasion akışı.
2. Hesapsız ve varsayılan olarak cihazda işleme.
3. Her seçimden sonra autosave ve kesintiden güvenli devam.
4. Fotoğraf başına uğraş yerine otomatik kompozisyon; kullanıcı yalnız kötü kırpmayı düzeltir.
5. Haftalık abonelik yerine **$9.99–$14.99 lifetime** veya proje başına açık ödeme hipotezi.

Bu özelliklerin tercih edildiğine veya fiyatın ödendiğine dair ürün-spesifik davranış henüz yoktur.

## Top 5 rakip ve ikame

| Rakip / ikame | Güçlü taraf | Açık veya risk |
|---|---|---|
| [SlideShow Maker Photo to Video](https://apps.apple.com/us/app/slideshow-maker-photo-to-video/id924826256) | Büyük rating proxy'si, yerleşik kategori | Görünen reliability ve abonelik şikâyetleri |
| [Slideshow Maker Video & Photo](https://apps.apple.com/us/app/slideshow-maker-video-photo/id1471839831) | İkinci bağımsız talep sinyali | Genel slideshow konumu |
| [Slideshow Maker & Creator](https://apps.apple.com/us/app/slideshow-maker-creator/id1419462900) | Hazır tema ve edit akışı | Cloud/privacy ve subscription itirazı |
| iMovie / Photos | Ücretsiz ve cihazda | Occasion'a özel otomasyon sınırlı; yine de en güçlü ikame |
| Canva / CapCut | Şablon zenginliği ve marka | Daha geniş editör; hesap, seçim ve öğrenme yükü |

## Solo MVP siniri

**Dört core ekran:** Occasion seçimi, Photo Picker, Preview/Edit, Export/Upgrade.

**Üç ana özellik:**

1. 8–30 fotoğraftan otomatik kırpma, süre ve hareket.
2. Tarih/metin + tek parça sesli anlatım.
3. Güvenli autosave ile 9:16 ve 16:9 export.

İlk sürümde AI video generation, sosyal ağ, kullanıcı hesabı, cloud sync, lisanslı müzik kataloğu veya template marketplace yoktur.

## Skor ve fatal gate

| Boyut | Low | Base | High |
|---|---:|---:|---:|
| Problem / talep | 3 | 4 | 5 |
| Monetizasyon / ekonomi | 2 | 3 | 4 |
| Rekabet / wedge | 2 | 3 | 4 |
| Dağıtım | 2 | 3 | 4 |
| Tekrar değeri | 1 | 2 | 3 |
| Zamanlama | 3 | 3 | 4 |

**Fırsat Çekiciliği:** **46 / 64 / 84 — borderline**  
**Kanıt Gücü:** **C**

Dört fatal gate `clear`: kullanıcı-seçimli medya ve telifsiz/kullanıcı-sahipli ses scope'u; standart local media pipeline; App Store'da çalışan kategorik emsaller; public feed veya yanıltıcı iddia yok. Bu bir hukuk görüşü veya build izni değildir.

## Sonraki gercek davranis testi

Önündeki 30 günde gerçek occasion'ı olan 12 ABD'li iPhone kullanıcısı, kendi 8–30 fotoğrafıyla çalışan prototipte görev yapar. Baseline ve population MDE bilinmediği için test **exploratory/directional**dır.

- Ana metrik: İlk export'a kadar süre ve tamamlanan export.
- Davranış: Videoyu gerçekten mesaj, sosyal ağ veya etkinlik ekranında paylaşma.
- Ödeme: Ürünün hazır olmadığı ve iade koşulu açıkça anlatılarak $9.99 refundable preorder.
- Geçiş: En az 8/12 kişi beş dakikada export, en az 6/12 gerçek paylaşım, en az 4/12 preorder.
- Durdurma: Üç eşikten biri kalırsa park et. Geçerse ikinci doğal occasion döngüsünde tekrar kullanımı test et ve yeniden puanla; tek test `BUILD_SMALL` vermez.

Deney sözleşmesi: [phases/06-prebuild-plan.md](phases/06-prebuild-plan.md). Sözleşme ilk arm'ı yalnız **doğum günü** occasion'ına kilitler (anma/mezuniyet/yıldönümü ayrı `experiment_id`), üç deneyi RAT sırasına dizer ve `occasion-retention`'ı ayrı ikinci-döngü sözleşmesine erteler.

## Kanit sinirlari

Storefront rating'leri gelir değildir. Quick Scan'de stratified review mining yapılmadı. Occasion bazlı arama hacmi, organik install conversion, CAC, gerçek ödeme ve ikinci-döngü kullanımı gözlenemedi. Generic editörlerin ücretsiz ikame gücü çözülmedi.
