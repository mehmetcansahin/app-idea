# ABD iOS Consumer Camera & Media Fikirleri — v4.0 Compare

**Tarih:** 2026-07-18  
**Karar aşaması:** Desk research / Compare  
**Hedef:** ABD, iPhone, geniş tüketici davranışı; tek geliştirici; fiziksel operasyon yok  
**Ortak arketip:** `consumer_utility`  
**Metodoloji:** v4.0

## Cevap

Önceki önerilerin sorunu talebi olmayan fikirler bulmak değildi; kullanıcının istediği **ürün sınıfını** yanlış okumaktı. Aranan sınıf: kullanıcı App Store'da ne yaptığını tek cümlede anlayacak, kamera/fotoğraf/video ile anında çıktı üreten ve sosyal paylaşım veya güçlü mahremiyet niyeti taşıyan consumer app.

Bu filtreyle net sonuç:

1. **Occasion Reel** — tek kişi için en yüksek başarı olasılığına göre ilk test.
2. **MemoryMotion** — en yüksek ticari/viral tavan; önce kalite ve inference maliyeti RAT'ı.
3. **Before/After Reel** — en hızlı build/test; daha dar pazar.
4. **RoomCheck** — yüksek niyetli kategori, fakat teknik fatal gate `unknown`; ürün değil RAT adayı.

“Tutan garanti fikir” masa başından üretilemez. Rating, chart ve fiyat yalnız mevcut davranışın `E2/supporting` proxy'sidir. Bu rapor build kararı değil, hangi gerçek davranış testine para/zaman ayrılacağını seçer.

## Research Contract

- **JTBD:** Kullanıcı birkaç dokunuşla duygusal, paylaşılabilir veya güven artıran bir medya çıktısı elde eder.
- **Platform/storefront:** iPhone, US App Store.
- **Kurucu sınırı:** Tek geliştirici; marketplace, fiziksel servis, community moderation ve sürekli manuel operasyon yok.
- **MVP sınırı:** En fazla dört core ekran ve üç ana özellik.
- **Ortak arketip:** Consumer Utility; bu sayede skorlar aynı ağırlıkla karşılaştırılabilir.
- **Risk modifier'ları:** Fotoğraf/oda verisi için `sensitive_data`; AI'da `ai_variable_cost`; iOS kısıtlarında `platform_dependency`.

## 18 problemden shortlist'e

| # | Kategori | Gözlenen/tasarlanan problem | Masa başı sonucu |
|---:|---|---|---|
| 1 | Privacy camera | Otel/rental içinde şüpheli kamera kontrolü | **RoomCheck shortlist**; universal detection savunulamaz iddia |
| 2 | Privacy camera | Gizli/background kayıt | **ELENDIR**; App Review, background ve hukuk riski |
| 3 | Privacy camera | Hangi app kamera/mikrofona erişti? | Küçük utility; talep ölçeği bu turda zayıf |
| 4 | Privacy camera | Şüpheli cihazı delil paketiyle belgelemek | RoomCheck modülü olabilir; bağımsız pazar zayıf |
| 5 | Photo choice | Grup fotoğrafında herkesin en iyi karesi | Teknik olarak uygun; ürün talep sinyali daha zayıf |
| 6 | AI photo/video | Eski aile fotoğrafını ciddi şekilde canlandırmak | **MemoryMotion shortlist** |
| 7 | Photo/video | Doğum günü/anma/mezuniyet reel'i | **Occasion Reel shortlist** |
| 8 | Photo/video | Bebek/pet büyüme morph'u | Before/After altında use-case olabilir |
| 9 | Photo/video | Fitness/renovation/progress dönüşüm videosu | **Before/After Reel shortlist** |
| 10 | Seller media | Ürün fotoğrafından satış reel'i | Prosumer; kullanıcının consumer hedefinden sapıyor |
| 11 | Photo/video | Generic slideshow | Talep var; ancak generic konum doygun |
| 12 | Photo/video | Live Photo / wallpaper animator | OS/commodity riski yüksek |
| 13 | Camera filter | Vintage kamera | Dazz/Lapse gibi güçlü incumbent; wedge yok |
| 14 | Camera ritual | Gecikmeli disposable roll | Davranış kanıtlı; yenilik ve retention maliyeti yüksek |
| 15 | Shared camera | QR ile party guest camera | Backend, UGC, abuse ve event support yükü |
| 16 | Capture | Stop-motion/brickfilm kamera | Güçlü incumbent; daha küçük tavan |
| 17 | Video utility | Hedef MB'ye güvenilir sıkıştırma | Solo için mantıklı fakat istenen aspirasyon sınıfı değil |
| 18 | Memory | Fotoğraf tarama + otomatik aile hikâyesi | Güçlü kategori; scanning incumbent'ları ve büyük scope |

Havuz üç ana kategoriyi kapsar: privacy camera, photo-to-video/AI ve capture/edit utility. Shortlist, yalnız büyük davranış sinyali değil, tek kişinin ürün ve operasyon sınırını birlikte kullanır.

## Pazar davranisi sinyalleri

- US Photo & Video chart'ta [AI Video](https://apps.apple.com/us/app/ai-video-ai-video-generator/id6478868302) yaklaşık #12 ve 24K rating; [Dazz Cam](https://apps.apple.com/us/app/dazz-cam-vintage-camera/id1422471180) yaklaşık 111K rating ve aktif chart görünürlüğü gösterdi. Bu, consumer camera/media davranışının hâlâ güçlü olduğuna dair güncel proxy'dir.
- [SlideShow Maker Photo to Video](https://apps.apple.com/us/app/slideshow-maker-photo-to-video/id924826256) yaklaşık 104K rating ve weekly IAP seçenekleri; visible yorumlar project-loss, ödeme ve cancellation problemleri gösterdi.
- [Motionleap](https://apps.apple.com/us/app/motionleap-3d-photo-animator/id1381206010) yaklaşık 117K; [Kling AI](https://apps.apple.com/us/app/kling-ai-ai-image-video-maker/id6738049229) yaklaşık 26K rating gösterdi. Generic AI/photo animation'da incumbent gücü yüksektir.
- [Hidden Spy Camera Finder Pro](https://apps.apple.com/us/app/hidden-spy-camera-finder-pro/id1560989782) yaklaşık 12K rating ve subscription seçenekleri gösterdi; görünür yorumlarda test kamerasını kaçırma ve açıklanamayan sonuç şikâyetleri vardı.
- [Before and After: Compare Photo](https://apps.apple.com/us/app/before-and-after-compare-photo/id1500915148) ve [BeforeAfter: Instant Watermark](https://apps.apple.com/us/app/beforeafter-instant-watermark/id1023269035) yaklaşık 2.1K–2.2K rating ile daha küçük ama doğrudan davranış sinyali gösterdi.

Erişim tarihi 2026-07-18; rating ve chart pozisyonları değişebilir ve gelir değildir.

## Ayni arketiple skor

Consumer Utility ağırlıkları: talep %25, ekonomi %15, wedge %20, dağıtım %25, tekrar %5, zamanlama %10.

| Ürün | Fatal gate | Kanıt | Low / Base / High | Desk kararı | Solo operasyon | Ürün sırası |
|---|---|---:|---:|---|---|---:|
| Occasion Reel | Tümü clear | C | **46 / 64 / 84** | TESTE_DEGER | Low | **1** |
| MemoryMotion | Tümü desk'te clear | C | **48 / 66 / 86** | TESTE_DEGER | Medium-high | **2** |
| Before/After Reel | Tümü clear | C | **42 / 60 / 80** | TESTE_DEGER | Low | **3** |
| RoomCheck | Core feasibility **unknown** | D | **46 / 64 / 79** | **BELIRSIZ** | Medium | **4** |

Ham base skor sırası `MemoryMotion > Occasion Reel = RoomCheck > Before/After`dır. Ürün sırası farklıdır; metodoloji fatal gate, Kanıt Gücü, test maliyeti ve kurucu operasyonunu ham skorun önüne koyar.

## 1. Occasion Reel — en dengeli bahis

**Promise:** “8–30 fotoğrafı beş dakikada paylaşılabilir occasion videosuna dönüştür.”

**Neden rekabet edilebilir:** Genel editör değil; birthday, memorial, graduation ve anniversary için opinionated akış. Local/no-account, autosave, doğru kırpma ve açık one-time price, görünen rakip şikâyetlerine doğrudan karşılık verir.

**MVP:** Occasion → Photo Picker → Preview/Edit → Export; otomatik crop/motion, date/narration, autosave+iki oran.

**Killer risk:** iMovie/Photos/Canva/CapCut zaten yeterli olabilir. Bu nedenle ekran tasarımından önce gerçek export ve sharing davranışı ölçülür.

Detay: [Quick Scan](2026-07-18-us-occasion-reel/REPORT.md)

## 2. MemoryMotion — en yuksek tavan

**Promise:** “Eski aile fotoğrafını dans ettirmeden, kimliği bozmadan beş saniyelik nazik bir anıya çevir.”

**Neden rekabet edilebilir:** Generic prompt/video yerine üç bounded serious motion; identity check; failed job'da otomatik credit refund; açık silme. Visible kullanıcı yorumu tam bu serious old-photo ihtiyacını işaret ediyor.

**Killer risk:** Model kalitesi ve delivered inference maliyeti. [Runway fiyatı](https://docs.dev.runwayml.com/guides/pricing/) seçili modellerde beş saniye için kabaca $0.25–$0.60 provider cost gösterirken, farklı modeller [fal kataloğunda](https://fal.ai/explore/image-to-video-apis) daha geniş aralıkta. Retry/support/refund marjı kolayca bozabilir.

**Kurucu seçimi:** Maksimum upside istiyor ve backend/provider operasyonunu kabul ediyorsan ilk teknik araştırma buna yapılır; doğrudan app build edilmez.

Detay: [Quick Scan](2026-07-18-us-memorymotion/REPORT.md)

## 3. Before/After Reel — en hizli test

**Promise:** “2–24 progress fotoğrafını otomatik hizala; iki dakikada tarihli 9:16 dönüşüm videosu çıkar.”

**Neden rekabet edilebilir:** İki-fotoğraf compare yerine timeline; yüz/nesne/oda anchor'ı; local export. Teknik scope küçük ve AI provider yok.

**Killer risk:** Doğrudan yeni rakipler var ve CapCut/Canva ikamesi güçlü. Auto-align gerçekten zaman kazandırmıyorsa ürünün nedeni kalmaz.

Detay: [Quick Scan](2026-07-18-us-before-after-reel/REPORT.md)

## 4. RoomCheck — demand var, ürün karari yok

**Promise:** “Beş dakikalık açıklanabilir oda gizlilik kontrolü; ne gördüğünü ve neyi göremediğini söyle.”

**Neden detector değil:** Apple [TN3111](https://developer.apple.com/documentation/technotes/tn3111-ios-wifi-api-overview), [TN3179](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy) ve [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth/) belgeleri genel yakın ağ taraması, eksiksiz device inventory ve non-advertising BLE görünürlüğü sağlamıyor. Universal camera detection teknik olarak savunulamaz.

**Covert recorder:** Apple [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) açık consent ve recording indicator ister. Gizli/background recorder solo ürün shortlist'inden elendi.

**Killer risk:** Kullanıcı `yetersiz veri` sonucunu değerli bulmayabilir; yanlış güven veya korku üretebilir. Önce kontrollü corpus RAT'ı.

Detay: [Quick Scan](2026-07-18-us-roomcheck/REPORT.md)

## Ogrenme sirasi

Ürün sırası ile deney sırası aynı olmak zorunda değil:

| Sıra | Aday | İlk deney | Directional geçiş | Fail aksiyonu |
|---:|---|---|---|---|
| 1 | MemoryMotion | 40 fotoğraf, 2 provider teknik RAT | ≥%80 kabul, 0 ağır identity swap, ≤$1.20 delivered cost | Provider/scope pivot veya park |
| 2 | Occasion Reel | 12 gerçek occasion kullanıcısı | 8 hızlı export, 6 gerçek share, 4 refundable preorder | Park |
| 3 | Before/After Reel | 12 kişi, 20 gerçek progress set | 8 hızlı export, 6 gerçek use/share, 4 preorder | Park veya use-case pivot |
| 4 | RoomCheck | 20 oda / 30 bilinen kamera corpus'u | Görünür subset'te ≥%80 inspect flag, ≤%10 high-risk false positive | Detector claim'i çıkar veya ele |

Bu eşiklerin baseline/MDE'si yoktur; exploratory'dir ve nüfus genellemesi üretmez. Waitlist tek başına yeterli değildir. Ödeme teklifinde ürünün hazır olmadığı, iade koşulu ve veri kullanımı açıkça belirtilir.

## Net tercih

- **Tek ürün seçip kullanıcı testi yapacaksan:** Occasion Reel.
- **Önce 1–2 günlük teknik spike yapıp maksimum upside kovalayacaksan:** MemoryMotion.
- **En kısa sürede işleyen local prototype görmek istiyorsan:** Before/After Reel.
- **Hidden camera kategorisine girmek istiyorsan:** RoomCheck RAT'ı; covert recorder veya “her kamerayı bulur” ürünü değil.

Bugünkü doğru sonraki adım tam app geliştirmek değil, Occasion Reel'in gerçek occasion görev prototipi ile MemoryMotion'ın teknik RAT'ını paralel olarak ucuz biçimde kapatmaktır.
