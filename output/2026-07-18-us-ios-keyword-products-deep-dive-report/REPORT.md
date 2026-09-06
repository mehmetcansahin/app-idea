# US iOS Keyword Ürünleri — Detaylı Solo Geliştirici Analizi

**Tarih:** 2026-07-18  
**Storefront:** United States  
**Platform:** iPhone / iOS  
**Kurucu kısıtı:** Tek geliştirici, fiziksel operasyon yok  
**Durum:** `PARTIAL_PUBLIC_PROXY` — Apple Ads Search Popularity ve search-term export bekleniyor

## Net sonuç

Bugün tek bir ürünü doğrudan geliştirmeye başlamazdım. **İlk gerçek kullanıcı testini `Before/After Reel` ile**, ilk teknik testi ise **`Exact-MB Video Compressor` ile** yapardım. İkisinin nedeni farklıdır:

- `Before/After Reel`, kullanıcının istediği görsel/dönüşüm uygulaması sınıfına en yakın, backend gerektirmeyen ve gerçek davranış testine en ucuza indirilebilen adaydır.
- `Exact-MB Video Compressor`, kamu sinyalinde daha büyük ve satın alma işi daha nettir; fakat “25 MB altına güvenilir indir” vaadi codec corpus testini geçmeden ürün değildir.

İkinci görsel davranış adayı `Birthday / Occasion Reel`; daha düşük operasyonlu AI adayı ise **yüz geometrisini değiştirmeyen cihaz-içi `Family Photo Colorizer`**dır. `MemoryMotion / animate old photos` en yüksek viral tavana, aynı zamanda açık ara en ağır retry, kimlik, gizlilik, kredi ve destek yüküne sahiptir.

`Family Archive Scanner` ve `US Baby Passport Capture Coach` ticari açıdan gerçek problemlerdir; fakat ilki ücretsiz Google ve güçlü Photomyne karşısında, ikincisi de resmî uygunluk ve ret riski altında çalışır. `Batch Watermark` en kolay ürünlerden biridir fakat sizin aradığınız tüketici/görsel ürün sınıfına uymadığı için yalnız ticari yedek olarak tutulmalıdır.

Bu rapor **build izni vermez**. Var olan üç resmî Quick Scan de `TESTE_DEGER / PREBUILD_PENDING` durumundadır; diğer beş aday burada formal v4 skoru almadı.

## Karar tablosu

Puanlar 1–5 kamu proxy’sidir. `Rekabet` için 5 en zor; diğer olumlu alanlarda 5 en güçlü düzeydir. Bu tablo bir v4 fırsat skoru veya başarı olasılığı değildir.

| Araştırma sırası | Ürün | Talep proxy | Ödeme niyeti | Rekabet | Solo hazırlık | Tarz uyumu | İlk kapı |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | **Before/After Reel** | 3 | 5 | 2 | 5 | 5 | Gerçek görev + refundable preorder |
| 2 | **Exact-MB Video Compressor** | 4 | 4 | 4 | 4 | 3 | Codec/target-size teknik RAT |
| 3 | **Birthday / Occasion Reel** | 3 | 4 | 2 | 5 | 5 | Gerçek occasion + paylaşım + ödeme |
| 4 | **Family Photo Colorizer** | 3 | 5 | 3 | 4 | 5 | Cihaz-içi model/kimlik RAT’ı |
| 5 | **Family Archive Scanner** | 4 | 4 | 4 | 3 | 4 | Rakiple görev + gerçek archive ödemesi |
| 6 | **US Baby Passport Capture Coach** | 4 | 5 | 5 | 3 | 3 | Gerçek başvuru/compliance testi |
| 7 | **MemoryMotion** | 4 | 5 | 4 | 2 | 5 | 40 fotoğraflık provider/kimlik/COGS RAT’ı |
| 8 | **Batch Watermark** | 4 | 4 | 4 | 5 | 2 | Tercih değişirse seller ödeme testi |

Sıra ham puan toplamından gelmiyor. Fatal risk, kanıt gücü, en ucuz belirleyici test, tek kişilik operasyon ve sizin ürün tercihiniz sırayla uygulandı.

## 1. Before/After Reel — ilk gerçek davranış testi

### Doğrudan gözlem

- [Photo Compare – Before & After](https://apps.apple.com/us/app/photo-compare-before-after/id1537250336) yaklaşık 2.6K, [BeforeAfter, Instant Watermark](https://apps.apple.com/us/app/beforeafter-instant-watermark/id1023269035) yaklaşık 2.2K ve [Before and after compare photo](https://apps.apple.com/us/app/before-and-after-compare-photo/id1500915148) yaklaşık 2.1K US rating gösteriyor.
- Son uygulama $2.99–$5.49 haftalık, $7.49 aylık, $29.49–$34.99 yıllık ve $39.99–$59.99 lifetime teklifler taşıyor. Fiyat merdiveni güçlüdür; gerçekleşen satış miktarı değildir.
- Rastgele olmayan görünür yorumlarda hizalanmayan fotoğraflar, düşük çözünürlük, sonsuz yükleme, crash ve ücretsiz oluşturulan işi kaydetmek için sürpriz abonelik şikâyetleri var. [Apple review akışı](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1500915148/sortBy=mostRecent/json).

### Çıkarım ve rekabet edilebilir ürün

İki fotoğrafı yan yana koyan başka bir editör yapılmamalı. Ürün şu işi sahiplenmeli:

> Aynı yüzü, saçı, bahçeyi, restorasyonu veya odayı 2–24 tarihli fotoğrafta hizala; tek dokunuşla dikey ilerleme videosu üret.

Asıl değer `ghost overlay + auto-align + tarihli timeline` üçlüsüdür. Privacy ve one-time fiyat tek başına fark değildir; yeni küçük rakipler bunları zaten sunuyor.

### Dört ekran / üç özellik

**Ekranlar:** Project Grid → Photo/Anchor Select → Aligned Timeline Preview → Export/Upgrade.

**Özellikler:**

1. Anchor tabanlı auto-align ve manuel düzeltme.
2. 2–24 fotoğraf, çekim tarihi ve basit ölçüm etiketi.
3. Cihazda 9:16 video/GIF export.

AI video, hesap, cloud, sosyal feed ve health-outcome skoru MVP dışında kalmalı.

### Para ve test

Fiyat hipotezi: **$9.99–$14.99 lifetime** veya tek proje için **$4.99**; kullanılabilir ücretsiz preview’den önce paywall yok.

En riskli varsayım hacim değil, kullanıcının auto-align farkını gerçekten kullanıp ödeme yapmasıdır. 12 ABD’li iPhone kullanıcısı 20 gerçek progress setini mevcut editörü ve prototiple tamamlar. Geçiş: en az 8/12 iki dakikada export, 6/12 gerçek paylaşım/kullanım, 4/12 açık koşullu $9.99 refundable preorder. Tek test `BUILD_SMALL` üretmez; ikinci doğal progress döngüsü de görülmelidir.

**Karar:** Bugünkü en iyi ilk kullanıcı testi.

## 2. Exact-MB Video Compressor — güçlü utility, önce teknik gerçeklik

### Doğrudan gözlem

- [Compress Videos & Resize Video](https://apps.apple.com/us/app/compress-videos-resize-video/id1473857051) yaklaşık 17K rating ve $4.99 aylık, $5.99 yıllık, $12.99 lifetime teklif gösteriyor.
- [Video Compressor – HQ Compress](https://apps.apple.com/us/app/video-compressor-hq-compress/id1546946937) yaklaşık 2.1K; [Video Compressor & Reduce size](https://apps.apple.com/us/app/video-compressor-reduce-size/id1135183644) yaklaşık 1.3K rating ve ücretli unlock/abonelikler taşıyor.
- En güncel rastgele olmayan review örneklerinde bazı videoların picker’da görünmemesi, 6 GB dosyanın alınmaması, yaklaşık bir saat sonra %99’da hata ve 7.1 MB girdiden 9.5 MB çıktı üretimi raporlanıyor. [Apple review akışı](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1473857051/sortBy=mostRecent/json).

### Çıkarım ve rekabet edilebilir ürün

`Video Compressor` adıyla generic klon yapılmamalı. Kullanıcının gerçek işi şudur:

> Bu videoyu email, Discord veya upload limiti için 25 MB’ın altına indir; tarihi, sesi ve yönü bozma.

Ürün başlangıçta çıktı tahmini, geçici disk ihtiyacı ve kaynak zaten hedefin altındaysa açık uyarı vermelidir. Tam Photos erişimi yerine seçici kullanılmalıdır.

### Dört ekran / üç özellik

**Ekranlar:** Video Select → Target MB/Quality Estimate → Progress/Cancel → Result/Save/Share.

**Özellikler:**

1. PhotosPicker veya Files preflight.
2. Kullanıcı tanımlı MB hedefi ve kalite tahmini.
3. Cihaz-içi export, audio/orientation/metadata koruma.

İlk sürümde URL’den YouTube/Instagram indirme, cloud queue, batch ve “lossless” iddiası yok.

### Para ve test

Fiyat hipotezi: iki başarılı export ücretsiz, ardından **$9.99–$12.99 lifetime**.

İlk kapı UI değil, 30 videoluk corpus’tur: H.264/HEVC, SDR/HDR, 720p–4K, 30/60 fps, Photos-edited, iCloud ve 2–6 GB. Geçiş: 27/30 çıktı hedefin en fazla %2 üstünde, hiçbir çıktı kaynaktan büyük değil, audio/orientation kaybı yok, crash/%99 stall yok ve P90 export süresi test cihazında video süresinin 2 katını aşmıyor.

[AVAssetExportSession](https://developer.apple.com/documentation/avfoundation/avassetexportsession) işi mümkün kılar; “exact” güvenilirlik codec ve bitrate gerçekliğiyle kanıtlanmalıdır.

**Karar:** Teknik RAT geçerse en sağlam bounded utility yedeği.

## 3. Birthday / Occasion Reel — doğru occasion’da basitlik satabilir

### Doğrudan gözlem

- [Birthday Video](https://apps.apple.com/us/app/birthday-video/id1544604029) yaklaşık 1.6K rating ve $0.99 haftalık, $1.99 aylık, $9.99 yıllık fiyatlar gösteriyor.
- [Video Maker Birthday Slideshow](https://apps.apple.com/us/app/video-maker-birthday-slideshow/id1508296694) yaklaşık 1.2K rating; broad slideshow liderleri yaklaşık 17K ve 104K rating seviyesinde.
- Görünür yorumlarda kolay kullanımın yanında reklamı kapatamama, gönderilen videonun alıcıda açılmaması, gallery export bozulması ve hiç çalışmayan video üretimi var. [Apple review akışı](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1544604029/sortBy=mostRecent/json).

### Çıkarım ve rekabet edilebilir ürün

Template kataloğu yarışı yerine bounded promise:

> 12–30 fotoğraf + isim + tek voice message → güvenilir 60–120 saniyelik doğum günü videosu.

Lisanslı müzik kataloğu eklemek solo operasyonu ve telif riskini gereksiz büyütür. Kullanıcı kendi sesini veya hak sahibi olduğu sesi kullanmalı.

### Dört ekran / üç özellik

**Ekranlar:** Occasion/Recipient → Photo Picker → Name/Voice → Preview/Export/Pay.

**Özellikler:** otomatik sequence/crop, isim-tarih-voice overlay, autosave ile 9:16/16:9 local export.

Fiyat hipotezi: **$4.99 proje** veya **$9.99 lifetime**. Haftalık abonelik bu epizodik iş için zayıf bir güven sinyalidir.

12 gerçek occasion kullanıcısında geçiş: 8/12 beş dakikada export, 6/12 gerçekten paylaşım, 4/12 refundable $9.99 ödeme.

**Karar:** Before/After zayıf kalırsa ikinci görsel davranış testi; generic slideshow yapılmamalı.

## 4. Family Photo Colorizer — daha solo-uygun AI açısı

### Doğrudan gözlem

- [Colorize – Color to Old Photos](https://apps.apple.com/us/app/colorize-color-to-old-photos/id1464665765) yaklaşık 7.5K rating ve $5.99–$39.99 arası görünen teklifler taşıyor.
- [RetroFix](https://apps.apple.com/us/app/retrofix-old-picture-restore/id6478808149) yaklaşık 6.8K, [Colorize – Restore Old Photos](https://apps.apple.com/us/app/colorize-restore-old-photos/id1518920566) yaklaşık 979 rating gösteriyor.
- Güncel rastgele olmayan yorumlarda yanlış renk, yüzün değişmesi, farklı kişi/kıyafet üretimi, ekstra el/parmak ve istenmeyen bıyık gibi ağır kimlik/geometri sorunları var. Buna karşılık olumlu yorumlar aile fotoğraflarını canlandırıp Facebook’ta paylaşma davranışını açıkça anlatıyor. [Apple review akışı](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1464665765/sortBy=mostRecent/json).

### Çıkarım ve rekabet edilebilir ürün

“AI restore everything” değil:

> Yeni yüz üretmeyen, geometriyi kilitleyen ve saç/ten/kıyafet rengini lokal düzeltmeye izin veren colorizer.

Bu ürünün `animate old photos`tan avantajı; uygun model bulunursa [Core ML](https://developer.apple.com/documentation/coreml) ile cihazda çalışabilmesi, backend/retry/kredi operasyonunu büyük ölçüde kaldırmasıdır.

### Dört ekran / üç özellik

**Ekranlar:** Import/Scan → Automatic Preview → Mask/Palette Correction → Compare/Export.

**Özellikler:** geometri-korumalı cihaz-içi model adayı, lokal renk düzeltme, orijinali koruyan before/after export.

Fiyat hipotezi: üç ücretsiz fotoğraftan sonra cihaz-içi modelde **$14.99 lifetime**; cloud zorunluysa şeffaf **$2.99 / 10 fotoğraf** paketi.

İlk kapı: 50 tarihî fotoğrafta teknik RAT + 10 gerçek fotoğraf sahibinin kör değerlendirmesi. Geçiş: fotoğrafların en az %85’inde kimlik/geometri değişimi yok ve en az 8/10 kullanıcı bir çıktıyı saklıyor; eski cihaz latency/model-size sınırı ayrıca geçmeli.

**Karar:** Görsel/AI isteyen solo geliştirici için MemoryMotion’dan önce test edilecek aday.

## 5. Family Archive Scanner — scanner değil, taşınabilir arşiv

### Doğrudan gözlem

- [Photo Scan App by Photomyne](https://apps.apple.com/us/app/photo-scan-app-by-photomyne/id1037784828) yaklaşık 93K, ücretsiz [PhotoScan by Google Photos](https://apps.apple.com/us/app/photoscan-by-google-photos/id1165525994) yaklaşık 89K ve [Photo Scanner Plus](https://apps.apple.com/us/app/photo-scanner-plus/id951627022) yaklaşık 22K rating gösteriyor.
- Photomyne; tek çekimde çoklu tarama, otomatik crop, arka yüz, kişi/tarih/konum, cloud ve AI araçlarını zaten sunuyor. “Bir özellik daha” wedge değildir.
- Görünür yorumlarda kenara yazılmış tarihin crop edilmesi, dışa aktarma ve dosya adlandırmanın hantallığı, albüm/ailenin zayıf organize edilmesi ve uygulama/abonelik kapanırsa arşiv kaybı endişesi var.

### Çıkarım ve rekabet edilebilir ürün

> Orijinal tam kare + crop, ön/arka eşleme, kullanıcı onaylı metadata ve JPG + CSV/JSON manifest içeren taşınabilir ZIP.

Ürün cloud lock-in yerine arşiv teslimatını sahiplenmelidir. [VisionKit](https://developer.apple.com/documentation/visionkit) yakalama tabanını kolaylaştırır; çoklu kenar algısı, glare, yüzlerce dosyada atomik kayıt ve export doğrulaması asıl iştir.

### Dört ekran / üç özellik

**Ekranlar:** Archive Setup → Batch Capture → Review/Pair/Annotate → Structured Export.

**Özellikler:** çoklu crop/perspective, ön-arka eşleme + manuel tarih/not, local ZIP + manifest.

Fiyat hipotezi: ilk 20 tarama ücretsiz, ardından **$19.99 one-time Full Archive Export**.

Test: en az 100 fiziksel fotoğrafı olan 12 kullanıcı, 50 fotoğrafı mevcut araçla ve 50’sini prototiple tarar. Geçiş: 6/12 gerçek $19.99 ödeme, 8/12 arşiv teslimatını tercih, kritik crop/eşleme kaybı <%2 ve süre incumbent’tan en fazla %20 yavaş.

**Karar:** Gerçek problem; güçlü ücretsiz/yerleşik ikameler nedeniyle ancak export-first wedge ile test edilir.

## 6. US Baby Passport Capture Coach — yüksek niyet, yüksek sorumluluk

### Doğrudan gözlem

- [Passport Photo – ID Photo](https://apps.apple.com/us/app/passport-photo-id-photo/id917389447) yaklaşık 21K, [Passport Photo · ID Maker](https://apps.apple.com/us/app/passport-photo-id-maker/id1620319650) yaklaşık 4.3K ve [Passport Photo & ID Maker](https://apps.apple.com/us/app/passport-photo-id-maker/id1483750251) yaklaşık 1.5K rating gösteriyor.
- Görünen fiyatlar $4.99–$19.90 ve daha yüksek lifetime seçeneklerine kadar uzanıyor. Bu transaction intent için güçlü, fakat satış miktarı olmayan bir proxy’dir.
- Görünür yorumlarda bebek saçının kötü ayrılması, uygulama kılavuzuna rağmen yüz ölçümü reddi, sürpriz export paywall ve tekrar tekrar crop denemesi var.

### Resmî sınır ve doğru ürün

[ABD Dışişleri Bakanlığı](https://travel.state.gov/en/passports/apply/help/photos.html) 2x2 inç fotoğraf, 1–1⅜ inç baş yüksekliği, düz beyaz/kırık beyaz gölgesiz arka plan ve **orijinal, değiştirilmemiş görüntü** ister. Telefon uygulaması, filtre veya AI ile dijital değişikliği; özellikle dijital background replacement’ı kabul edilemez gösterir.

Bebek beyaz/kırık beyaz çarşafa veya çarşafla kaplı oto koltuğuna yerleştirilebilir; başka kişi görünmemeli. Bebeğin gözlerinin tamamen açık olması zorunlu değildir.

Dolayısıyla ürün AI passport editor değil:

> Fiziksel kurulumu anlatan, burst içinden net/önden/yüzü açık kareyi sıralayan ve pikselleri değiştirmeden export eden US-only baby capture coach.

### Dört ekran / üç özellik

**Ekranlar:** Baby Setup → Live Guidance → Best Burst Frames → Unedited Export/Print Sheet.

**Özellikler:** ışık/poz/fiziksel kurulum rehberi, local blur/face/pose ranking, piksel içeriğini değiştirmeyen crop/4x6 layout.

Background removal, beautification, generative fill, kabul garantisi ve çok ülke şablonu ilk sürümde yok.

Fiyat hipotezi: **$6.99 one-time export**. Test: önündeki 60 günde gerçek çocuk pasaport başvurusu yapacak 15 ebeveyn; 10/15 ödeme, medyan çekim <5 dakika ve fotoğraf kaynaklı yeniden gönderim isteği <%10. Bu küçük test hiçbir zaman “%90 kabul garantisi” diye pazarlanamaz.

**Karar:** Satın alma anı güçlü; compliance ve refund/support yükü nedeniyle ilk ürün değil.

## 7. MemoryMotion — en yüksek tavan, en ağır solo operasyon

### Doğrudan gözlem

- [Motionleap](https://apps.apple.com/us/app/motionleap-3d-photo-animator/id1381206010) yaklaşık 117K, [Photo Revive](https://apps.apple.com/us/app/photo-revive-ai-alive-moment/id6738237021) yaklaşık 12.6K ve [Photica](https://apps.apple.com/us/app/photica-live-photo-ai-animator/id6673907297) yaklaşık 9.2K rating sinyali gösteriyor.
- Görünür yorumlarda kredi bitmesi, abonelikten sonra yeniden ödeme, çıktının kişiye benzememesi, ödeme alınıp çıktı üretilmemesi ve crash var. [AI Video review akışı](https://itunes.apple.com/us/rss/customerreviews/page=1/id=6478868302/sortBy=mostRecent/json).
- [Runway fiyatı](https://docs.dev.runwayml.com/guides/pricing/) kredi başına $0.01’dir. Beş saniye Gen-4 Turbo yaklaşık $0.25, Gen-4.5 yaklaşık $0.60 ham inference demektir; tek tam retry bunları $0.50 ve $1.20’ye çıkarır. Storage, Apple payı, başarısız iş, support ve refund dahil değildir.

### Çıkarım ve rekabet edilebilir ürün

Prompt kutulu generic AI video yapılmamalı. Ürün yalnız üç ciddi, konuşmasız hareket sunmalı: blink, soft smile, slight head turn. Kimlik karşılaştırması düşükse iş reddedilmeli ve kredi otomatik dönmelidir. Fotoğrafın üçüncü taraf provider’a gönderildiği, ne kadar tutulduğu ve ne zaman silindiği açıkça anlatılmalıdır.

### Dört ekran / üç özellik

**Ekranlar:** Photo/Consent → Three Motions → Generation/Quality Check → Result/Credits.

**Özellikler:** üç bounded motion, provider + identity/failure gate + automatic refund, beş saniyelik export ve deletion flow.

Fiyat hipotezi: **5 klip $9.99**; “unlimited” abonelik yok.

İlk kapı 40 izinli fotoğrafta iki provider’dır. Geçiş: en az %80 kabul edilebilir çıktı ilk deneme veya tek retry’da, sıfır ağır wrong-person/identity swap ve ortalama delivered inference ≤$1.20. Geçmeden ödeme, queue veya tam UI yapılmaz.

**Karar:** Build adayı değil; maksimum upside için yalnız teknik RAT adayı.

## 8. Batch Watermark — iyi solo işi, yanlış ürün tercihi

### Doğrudan gözlem

- [Watermark Maker: Add Signature](https://apps.apple.com/us/app/watermark-maker-add-signature/id1160624432) yaklaşık 32K, [Watermark Maker X](https://apps.apple.com/us/app/watermark-watermark-maker-x/id1100583565) yaklaşık 19K rating gösteriyor.
- Fiyatlar basit $3.99 unlock’tan $5.99 haftalık ve $39.99 yıllık tekliflere kadar uzanıyor.
- Güncel görünür yorumlarda blur export, batch’te renk kısıtı, ödeme sonrası uygulamanın açılmaması, beş fotoğraf limiti ve app’in kendi logosunu export’a eklemesi var. [Apple review akışı](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1160624432/sortBy=mostRecent/json).

### Çıkarım ve rekabet edilebilir ürün

`Add watermark` değil, **Etsy/eBay/Marketplace için 1–100 fotoğrafta kalite kaybetmeyen relative-position preset** ürünüdür. Backend, AI ve moderasyon gerektirmez; bu yüzden teknik/operasyon olarak listedeki en güvenli adaylardandır.

**MVP:** Preset/Batch Picker → Text/PNG Editor → Batch Preview → Export/Retry. Üç özellik: 100 fotoğraf seçimi, relative-position reusable preset, full-resolution batch export.

Fiyat hipotezi: üç fotoğraf ve bir preset ücretsiz, ardından **$7.99 lifetime**. Test: 15 aktif satıcının 20–50 fotoğraflık gerçek batch’i; 10/15 üç dakikada yardımsız bitirir ve 4 kişi $5 refundable deposit bırakır.

**Karar:** Ticari olarak credible; sizin istediğiniz consumer transformation sınıfına uymadığı için şimdilik park.

## Monetizasyon sonucu

Bu sekiz adayın çoğu epizodiktir. Apple, auto-renewable subscription için kullanıcıya devam eden değer sunulmasını ister. [App Review 3.1.2](https://developer.apple.com/app-store/review/guidelines/). Bu nedenle:

| Ürün sınıfı | Başlangıç modeli |
|---|---|
| Local, epizodik utility | Free preview/limit + lifetime unlock |
| Occasion | Project export + lifetime alternatif |
| Cloud AI, değişken maliyet | Açık consumable credit; teknik başarısızlıkta otomatik iade |
| Gerçek sürekli cloud/team değeri | Ancak o zaman abonelik |

Haftalık abonelik rakiplerde görünmesi nedeniyle kopyalanmamalı. Görünür review örneklerinde sürpriz paywall, “unlimited” sonrası coin ve iptal sorunları doğrudan güven açığıdır. Paywall’da export öncesi neyin ücretsiz olduğu ve satın almanın tam olarak ne verdiği açık olmalıdır.

## Teknik ve operasyon ayrımı

| Aday | Cihaz-içi mümkün mü? | Backend zorunlu mu? | Ana support kaynağı |
|---|---|---|---|
| Before/After | Evet | Hayır | Alignment/export edge-case |
| Video Compressor | Evet | Hayır | Codec, HDR, büyük dosya, disk/thermal |
| Birthday Reel | Evet | Hayır | Export ve medya/telif beklentisi |
| Colorizer | Model uygunsa evet | Hayır | Kimlik/renk kalitesi, eski cihaz |
| Archive Scanner | Evet | Hayır | Veri kaybı, crop ve export güveni |
| Baby Passport | Evet | Hayır | Ret/compliance/refund beklentisi |
| MemoryMotion | Hayır, pratik MVP cloud | **Evet** | Identity drift, retry, credit, deletion, provider outage |
| Watermark | Evet | Hayır | Büyük batch, color profile ve metadata |

Apple, üçüncü taraf AI’a kişisel veri gönderildiğinde bunun açıkça açıklanmasını ve izin alınmasını ister. [App Review 5.1.2](https://developer.apple.com/app-store/review/guidelines/). Aile ve bebek fotoğraflarında varsayılan tercih PhotosPicker, cihaz-içi işlem, hesapsız kullanım ve orijinali overwrite etmemektir.

## Neyi ayrı uygulama yapmamalıyız?

### `memorial slideshow`

Aciliyet yüksek fakat dedicated exact-query traction zayıf. Apple Ads Search Popularity ve paid conversion kanıtlamadan ayrı app değil, `Occasion Reel` içinde bir template/landing-message testi olmalıdır.

### `hidden camera detector`

Önceki formal Quick Scan’de Kanıt Gücü `D`, core feasibility gate `unknown` ve karar `BELIRSIZ`dir. iOS bütün yakındaki Wi‑Fi kameralarını tarayan genel bir API sunmaz; BLE/magnetometer da kamera kimliği değildir. Detector klonu yapılmamalı. Yalnız `normal / incele / yetersiz veri` diyen guided room check, kontrollü corpus geçerse değerlendirilebilir. [Apple TN3111](https://developer.apple.com/documentation/technotes/tn3111-ios-wifi-api-overview), [TN3179](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy), [App Review 1.1.6](https://developer.apple.com/app-store/review/guidelines/).

## Önerilen araştırma sırası

1. **Before/After:** görev prototipi + real share + refundable preorder.
2. **Video Compressor:** aynı dönemde 30 videoluk teknik corpus; exact promise geçmezse hemen bırak.
3. **Colorizer:** görsel AI yönü isteniyorsa 50 fotoğraflık cihaz-içi kimlik/geometri RAT’ı.
4. **Birthday Reel:** Before/After ödeme üretmezse ikinci occasion davranış testi.
5. Scanner ve Passport yalnız hedef kullanıcıya erişim hazırsa; MemoryMotion yalnız provider RAT’ı için.

Bu sıra ürün geliştirme sırası değil, **en az para ve zamanda en çok belirsizlik kapatan test sırası**dır.

## Kanıt sınırları

- Apple exact aylık organik keyword hacmi kamuya açık değildir. Apple Ads `Search Popularity` 1–5 gösterir; 5 en popülerdir. [Apple Ads metric definitions](https://ads.apple.com/app-store/help/reporting/0023-reporting-options-and-definitions).
- Rating; revenue, aktif kullanıcı, yeni indirme hızı, retention veya keyword rank değildir.
- IAP listesi teklif mimarisidir; satın alma sayısı değildir.
- İncelenen review’lar App Store web/RSS yüzeyinden seçilmiş rastgele olmayan örneklerdir; tema frekansı veya pazar prevalansı çıkarılmadı.
- Bu çalışma formal Standard değildir; top-5 rakip başına stratified minimum review örneklemi tamamlanmadı.
- Yalnız Before/After, Occasion Reel ve MemoryMotion için formal v4 Quick Scan vardır. Bunların skorları sırasıyla 42/60/80, 46/64/84 ve 48/66/86; üçü de `borderline`, Kanıt `C`, masa başı kararı `TESTE_DEGER`dir. Ham skor ürün sırası değildir.
- Baseline/MDE bulunmayan insan testlerinin eşikleri exploratory/directional’dır. Sonuçlar evidence kayıtlarına işlenmeden hiçbir aday `BUILD_SMALL` alamaz.

## Destekleyici dosyalar

- [Makine-okunur aday analizi](data/candidate_analysis.json)
- [Çalıştırılmış karşılaştırma notebook’u](analysis/product_comparison.ipynb)
- [Önceki keyword shortlist](../2026-07-18-us-app-store-keyword-opportunities-report/REPORT.md)
