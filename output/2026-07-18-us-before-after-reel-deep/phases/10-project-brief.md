# Faz 10 — Conditional Project Brief

> **Durum: PREBUILD_PENDING.** Bu brief implementation authorization değildir. Teknik RAT ve gerçek davranış/ödeme testi geçmeden geliştirme backlog'u sayılmaz.

## Product statement

US iPhone kullanıcıları için, camera roll'daki iki eski ve uyumsuz before/after fotoğrafını cihaz içinde dürüstçe subject/anchor hizalayıp iki dakikadan kısa sürede tam-kadraj 9:16 video üreten import-first registration utility.

## İlk doğrulanacak segment

Art/DIY creator/hobbyist:

- En az iki bitmiş proje before/after çifti var.
- Sonucu portföyde, sosyal kanalda veya müşteri iletişiminde kullanmak istiyor.
- CapCut/Canva/manual crop ile sürtünme yaşıyor.

Hair/beauty professional ayrı ikinci WTP hipotezidir; aynı cohort'a katılmaz.

## Job story

“Bitmiş işimin before ve after fotoğrafları farklı framing'le çekildiğinde, generic editörde uğraşmadan aynı anchor'a oturmuş güvenilir bir dikey video istiyorum; böylece sonucu profesyonel gösterebilirim.”

## Value proposition

- Pick two photos.
- Honest auto-align; manual control always available.
- Full-frame 1080p Reel in under two minutes.
- No account; media stays on device.
- Şeffaf one-time teklif; fiyat güven tercihi, ürün moat'i değil.

## Success definition before build

### Technical

- Aynı 20 zor pair'de Qvyshift/DiffPix/CapCut/Edits medianından ≥%30 hızlı.
- Kör competitor benchmark alignment tercihinde prototip ≥%70.
- Static align blind better/equal ≥85%.
- Catastrophic confident warp <2%.
- 200 exports, 0 crash.
- Old-device export p95 ≤15 seconds.
- No location/original filename in output.

### Behavioral — Art/DIY n=12

- ≥8 two-minute export.
- ≥6 verified real use/share.
- ≥4 refundable $5 deposit.
- ≥6 second distinct pair in 14 days.
- Auto result retained ≥70%.
- Refund ≤20%.

Baseline/MDE bilinmediği için sonuç yönseldir; formal BUILD_SMALL için yeniden v4 assessment gerekir.

## Conditional MVP

### Screens — max four

1. Pick Pair.
2. Align.
3. Preview.
4. Export/Pay.

### Core features — max three

1. Segment-aware auto alignment + manual fallback.
2. Slider/fade/hard-cut preview.
3. Local 1080p export/save/share.

### Paywall

- Preview ve bir watermark export ücretsiz.
- $9.99 lifetime hypothesis.
- Fiyat iddiası Qvyshift $3.99 one-time, Lapsey $9.99 one-time ve ücretsiz Edits/CapCut status quo'suna karşı test edilir.
- Price, render öncesi görünür.
- No weekly subscription.

### Non-goals

- Camera capture/ghost-guided recapture.
- Multi-date project tracker.
- Cloud/account/sync.
- Music/template marketplace.
- AI generation.
- 4K/GIF.
- Health/body/skin/hair measurement.
- Social network.

## Technical stack

- Swift + SwiftUI, minimum iOS 17.
- PhotosPicker for selected media.
- Image I/O proxy/downsample.
- Vision translation/homography for statics.
- Vision face/body landmarks + similarity transform for humans.
- Core Image rendering.
- AVAssetWriter H.264/MP4.
- StoreKit 2 or RevenueCat only after pricing experiment; one SDK at most.
- No backend in MVP.

## Privacy requirements

- Selected-media access only.
- All pixels and landmarks remain on device.
- Temp files deleted after export/cancel.
- Export strips location and original filename.
- No face/body analytics.
- Privacy label matches actual SDK/network behavior.

## Analytics events if needed

- `import_succeeded`
- `auto_align_retained`
- `manual_adjustment_used`
- `export_succeeded`
- `share_sheet_opened`
- `second_pair_exported`

Never log media, filename, capture date, GPS, image hash, landmark or biometric inference.

## Launch positioning hypothesis

- Name: `Progress Reel: Before & After`.
- Subtitle: `Align Photos Into Timelapses`.
- Primary promise: stable progress photos → shareable Reel.
- Screenshot 1: jitter vs aligned result.
- Screenshot 2: manual control and raw/aligned trust.
- Screenshot 3: private/local export.

Search Popularity ve query conversion olmadan metadata final değildir.

## Go/no-go ownership

- Desk decision: TESTE_DEGER.
- Next owner: founder/researcher runs RAT and prebuild contract.
- Build authorization: yalnız new assessment `BUILD_SMALL` üretirse.
- Stop owner: founder applies pre-registered thresholds; failed threshold sonrası feature expansion yapmaz.
