# Faz 1 — Market Scan

## Research Contract Preflight

- Karar sorusu: “Camera roll'dan iki gerçek fotoğrafı otomatik fakat dürüst biçimde hizalayıp 9:16 before/after videosu üreten dar iOS utility, solo geliştiricinin gerçek ödeme ve paylaşım davranışıyla rekabet edebileceği bir ürün müdür?”
- Primary archetype: `consumer_utility`
- Modifier'lar: `sensitive_data`, `platform_dependency`
- Geo/storefront/platform: US / US App Store / iOS, iPhone-first
- Stage/mode: desk_research / Deep
- Kullanıcı: Gerçek before/after çifti hazır olan, sonucu kaydetmek veya paylaşmak isteyen iPhone kullanıcısı.
- Tetikleyici: Framing farkı yüzünden manuel geçiş amatör görünür veya generic editörde gereğinden uzun sürer.
- Ana ikame: CapCut, Canva, Photos, manual crop/overlay, iki-foto compare app'i veya videoyu hiç yapmamak.
- İstenen sonuç: İki dakikadan kısa sürede güvenilir, tam-kadraj, 9:16 video.

## Use case ve ürün ayrımı

“Progress photos çekmek”, “before/after karşılaştırmak” ve “Reel üretmek” aynı ürün değildir:

- Tracker job'ı capture reminder, timeline ve privacy vault ister.
- Compare job'ı zoom/align/full-frame kontrolü ister.
- Reel job'ı dikey canvas, transition, süre ve export kalitesi ister.

Deep araştırma, tracker özelliklerinin yeni rakiplerde yoğunlaştığını gösterdi. Bu yüzden ürün import-first compare→Reel utility olarak daraltıldı.

## Doğrudan talep gözlemleri

- Photo Compare 2,580; Instant Watermark 2,218; Before and after compare 2,074 US rating gösterdi.
- Bir Reddit kullanıcısı progress GIF'inde omuzların aynı yerde kalmasını ve ghost overlay'i açıkça istedi.
- Hair-progress community'sinde aynı ışık, mesafe ve açı problemi güncel olarak tartışıldı.
- Apple public Search API'de `before after video` için 15/18; `progress photo` için 18/19 sonuç iş ailesiyle ilgili kodlandı.

Rating, community post ve API relevance birlikte job'ın varlığını destekler; hiçbiri product-specific conversion değildir.

## Segment seçimi

| Segment | Neden var? | Neden ilk değil/ilk? |
|---|---|---|
| Art/DIY | Statik anchor, hazır proje çiftleri, düşük privacy | İlk teknik ve davranış testi; düşük distortion riski |
| Hair/beauty professional | Müşteri kanıtı, tekrar ve WTP hipotezi | İkinci ayrı test; consent ve outcome-claim riski |
| Home/garden | Reveal içeriği doğal | Döngü yavaş, büyük sahne değişimi align'ı bozar |
| Fitness | Progress-photo intent güçlü | Hassas beden verisi, farklı poz/kıyafet, saturated tracker rekabeti |

Farklı segmentler tek davranış örnekleminde karıştırılmayacaktır. Teknik corpus algoritma sınırını ölçmek için dört segmentli olabilir; ödeme/tercih testi tek segmentli olmalıdır.

## Pazarın görünür yapısı

- Yerleşik utilities binlerce rating taşır fakat bazıları 2020–2022'den beri güncellenmemiştir.
- 2025–2026 entrant'ları Reels/TikTok, 9:16, slider, local processing, alignment ve ghost overlay dilini kullanır.
- Bu girişler timing sinyali kadar copycat hızını da gösterir.
- Exact pazar büyüklüğü, install ve revenue public kaynaklarla gözlenemez.

## Faz sonucu

Problem ailesi gerçektir; fakat ürün fırsatı yalnız dar hız/kalite tezi olarak kalmıştır. Market scan tek başına build önermez.

