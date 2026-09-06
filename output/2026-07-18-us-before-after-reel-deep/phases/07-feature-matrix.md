# Faz 7 — Feature Matrix ve Technical Design

## Feature matrix

`✓` listing'de gözlenen vaat; kalite doğrulaması değildir. `?` net gözlenmedi.

| Ürün | Import pair | Ghost/manual overlay | Auto alignment | Timeline | Video/timelapse | 9:16 | Local/privacy | One-time offer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Photo Compare | ✓ | ? | ? | — | sınırlı | ✓ | ? | ? |
| Instant Watermark | ✓ | manuel ihtiyaç review'da | — | — | — | ✓ | ? | ✓ |
| Before and after compare | ✓ | ? | ? | — | ✓ | ✓ | ? | ✓ |
| Qvyshift Video Maker | ✓ | slider/manual | ? | — | ✓ | ? | ✓/offline | ✓/$3.99 |
| DiffPix | ✓ | slider | ? | — | ✓ | ✓ | ✓ | ✓ |
| Momentum Video Maker | ✓ | compare modes | ? | ✓ | ✓ | ✓ | ✓ | ✓ |
| CapCut | ✓ | manual crop/overlay | dedicated registration ? | ✓ | ✓ | ✓ | cloud/account mix | free + sub |
| Edits | ✓ | Fuse/transition | dedicated registration ? | ✓ | ✓/4K | ✓ | Meta account | free |
| Then & Now | ✓/bulk | ✓ | ? | ✓ | ✓ | ✓ | ✓/iCloud | ✓ |
| Body Tracker | ✓ | ✓ | pose ✓ | ✓ | ✓ | ✓ | ✓ | ? |
| Metamorph | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓/iCloud | ? |
| SideLens | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ |
| MatchFrame | ✓ | ✓ | camera anchor | ✓ | ✓ | ✓ | ✓ | ? |
| **Önerilen MVP** | **2 foto** | **✓** | **segment-aware ✓** | **—** | **3 transition** | **✓** | **✓** | **$9.99** |

Bu matris eski “alignment + timeline + timelapse boşluğu” iddiasını reddeder. Qvyshift şeffaf one-time fiyatı, DiffPix exact 1080p Reel'i, CapCut template status quo'yu ve Edits ücretsiz 4K baseline'ı kapatır. İncelenen direct two-photo listing'lerde imported pair için dedicated automatic subject/anchor registration açıkça reklam edilmedi; tracker komşularında auto-align var. Önerilen MVP'nin farkı daha az feature ile ölçülebilir registration hızı, dürüst transform ve output reliability'dir.

## Platform kararı

- Swift + SwiftUI.
- Minimum iOS 17 önerisi; iPhone XS/XR ve SE 2 düşük uç test cihazları.
- Backend/account/cloud yok.
- Local event analytics bile gerekli değil; eklenirse yalnız import/align/export/share outcome event'leri ve medya içermeyen payload.

## Veri akışı

```text
PhotosPicker
  → app temp dosyasına kopya
  → EXIF orientation + color normalization
  → 1024–2048 px analysis proxy
  → segment-aware Vision alignment
  → confidence gate + manual correction
  → Core Image frame render
  → AVAssetWriter H.264/MP4
  → Share Sheet veya Photos add-only
  → temp dosyaları sil
```

## Import ve bellek

- PhotosPicker yalnız seçilen medyayı verir; full Photos read izni gerekmez.
- iCloud-only media için loading/retry/recovery state gerekir.
- 48 MP HEIC/ProRAW tam `UIImage` decode edilmez; Image I/O thumbnail/downsample.
- Analysis proxy uzun kenar 1024–2048 px; export decode yalnız 1080×1920 canvas'ı dolduracak kadar.
- EXIF orientation koordinata normalize edilir.
- P3/HDR source MVP'de sRGB/SDR output'a tone-map edilir.
- Tek reusable `CIContext` ve pixel-buffer pool.

## Hizalama

### Statik Art/DIY, home

1. Translation registration.
2. Quality yetersizse homography.
3. Common visible crop.
4. Confidence düşükse auto result reddi ve manual overlay.

Apple, registration'ın en iyi sonucu iki görüntü içeriği çok benzerken verdiğini belirtir. Dramatik dönüşüm, feature matching'i zorlaştırır.

### İnsan hair/fitness

- Face landmarks veya body pose üzerinden translation + uniform scale + sınırlı rotation.
- Non-rigid warp, inceltme veya perspective body deformation yok.
- Raw/Aligned compare görünür.
- Hizalama ölçüm, medical outcome veya gerçeklik doğrulaması olarak sunulmaz.

## Video output

- 1080×1920, 9:16.
- 30 fps, 4–6 saniye.
- H.264/MP4, ses yok.
- Slider, fade, hard cut.
- Export actor/task; progress ve cancel.
- Background completion varsayılmaz; export kısa tutulur.
- Low disk/thermal/iCloud/Live Photo/mirrored selfie/different aspect ratio edge-case'leri test edilir.

## Dört ekran

1. **Pick Pair:** Before ve After seç.
2. **Align:** Raw/Auto, opacity, pinch/drag/rotate.
3. **Preview:** Transition, aspect ve süre.
4. **Export/Pay:** Watermark preview, unlock, save/share.

## Üç core feature

1. Honest auto-align + manual fallback.
2. Three-transition real-time preview.
3. Local 1080p export/share.

## Explicit non-goals

- Camera-guided recapture.
- Project/timeline history.
- Multi-photo progress reel.
- Cloud, account, sync.
- Music and licensed assets.
- AI generation/restoration.
- 4K, GIF, Live Photo.
- Body, hair veya skin measurement.
- Social feed veya auto-post.

Scope azaltımı yalnız solo geliştirme kolaylığı için değil, exact entrant'larla feature yarışına girmemek içindir.

## Technical sources

- [Apple PhotosPicker](https://developer.apple.com/documentation/photosui/photospicker)
- [Apple Vision — Aligning Similar Images](https://developer.apple.com/documentation/vision/aligning-similar-images)
- [VNHomographicImageRegistrationRequest](https://developer.apple.com/documentation/vision/vnhomographicimageregistrationrequest)
- [Face landmarks](https://developer.apple.com/documentation/vision/vndetectfacelandmarksrequest)
- [Human body pose](https://developer.apple.com/documentation/Vision/detecting-human-body-poses-in-images)
- [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter)
- [Pixel buffer adaptor](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor)
