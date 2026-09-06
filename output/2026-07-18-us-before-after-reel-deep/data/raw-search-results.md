# Raw Search Results — US Before/After Reel Deep

**Erişim:** 2026-07-18  
**Storefront:** US  
**Platform:** iOS/iPhone  
**Public API:** Apple iTunes Search API, `country=us`, `entity=software`, `limit=20`

## Okuma uyarısı

Bu dosyadaki sıra Apple public Search API yanıt sırasıdır; App Store istemcisi organik rank'i değildir. `resultCount`, rating sayısı ve autocomplete önerisi keyword hacmi, impression, tap, install, conversion veya gelir değildir. “İlgili” sınıfı listing'in before/after compare, progress-photo tracking veya video/GIF/timelapse işini açıkça desteklemesine göre manuel kodlanmıştır.

Apple Ads hesabına ait Search Popularity 1–5, keyword recommendation, search-term, impression, tap, install, CPT ve CPA export'ları workspace'te yoktur. Exact aylık organik query count Apple tarafından public sunulmadığı için `structurally_unobservable` kaydedildi.

## Apple public Search API özeti

| Query | Dönen | İlgili | Video/timelapse | Exact title | İlk üç API sonucu | Karar |
|---|---:|---:|---:|---:|---|---|
| `before after video` | 18 | 15 | 12 | 3 | Before After Effect; Doposler; PhotoGrid | Primary intent |
| `before and after video maker` | 20 | 7 | 6 | 2 | Before and After Video Maker; Before & After Video Maker; T-Jam | Primary long-tail |
| `progress video` | 19 | 4 | 1 | 0 | Combine Videos; VideoNext; VideoCam+ | Broad; kaçın |
| `transformation video` | 18 | 0 | 0 | 0 | Filmora; DigiArt; YouCam Video | Yanlış AI/editor intent |
| `photo comparison` | 18 | 5 | düşük | 1 | Photo Compare; Pic Stitch; Side by Side Photo Editor | Secondary |
| `before after reel` | 18 | 12 | 9–10 | 0 | After Effects Tutorials; ReelSa; DiffPix | Creative copy; hacim değil |
| `progress photo` | 19 | 18 | 4 | 1 (+3 plural) | Metamorph; Progress Body Tracker; Selfie A Day | Primary intent |
| `glow up video` | 18 | 0 | 0 | 0 | GlowUp Makeup; GlowUp Photo Editor; PrettyMe | Yanlış intent |
| `fitness progress video` | 19 | 4 | 1 | 0 | AFLETE; Macrofit; Pvolve | Creative segment |
| `home renovation progress` | 18 | 1 | 0 | 0 | Property Brothers; Renovation Day; House Renovation Master | ASO için zayıf |
| `hair growth progress` | 17 | 8 | 0 | 0 | Shea; Hair Growth Journal; Follicle | Tracker intent |

### İlk üç sonucun rating-count bağlamı

- `before after video`: 382 / 29 / 116,568
- `before and after video maker`: 0 / 0 / 10,669
- `progress video`: 24,743 / 4 / 4,227
- `transformation video`: 89,165 / 12,178 / 14,267
- `photo comparison`: 2,580 / 65,225 / 7,946
- `before after reel`: 18 / 7 / 0
- `progress photo`: 66 / 9,247 / 4,002
- `glow up video`: 13,491 / 1,180 / 0
- `fitness progress video`: 12,884 / 5,770 / 9,098
- `home renovation progress`: 520,583 / 12,887 / 3,600
- `hair growth progress`: 80 / 0 / 0

Rating bağlamı yalnız storefront proxy'sidir; download, revenue, retention veya query volume değildir.

## Apple autocomplete/search hints

Apple-hosted search-hints endpoint'i US storefront header'ıyla gözlendi. Dokümante edilmiş kararlı bir API değildir; öneriler app isimlerinden etkilenebilir ve hacim değildir.

| Prefix | Gözlenen öneri |
|---|---|
| `before a` | before and after video; before and after photo compare; before after photo |
| `before after v` | before after video compare kit; before & after video maker; app-name varyantları |
| `before after r` | öneri yok |
| `progress p` | progress photo tracker; body progress photos; progress photos; progress pics |
| `progress v` | progress-video işi yok; vocabulary/timer sonuçları |
| `photo comp` | photo compare; photo comparison; compressor varyantları |
| `fitness progress` | fitness progress tracker; fitness progress |
| `hair growth` | hair growth tracker; hair growth journal; hair growth AI; hair growth timelapse |
| `glow up v` | video niyetini desteklemeyen varyantlar |

## Community ve channel sorguları

### Direkt job gözlemleri

- [Reddit /beginnerfitness — Best app for progress photos?](https://www.reddit.com/r/beginnerfitness/comments/1qp335k/best_app_for_progress_photos/) (2026-01-28): kullanıcı altı aylık fotoğraflardan jitter'sız GIF, omuz anchor'ı ve ghost overlay istiyor. Tek community post; ödeme kanıtı değil.
- [Reddit /tressless — Best lighting for progress pictures](https://www.reddit.com/r/tressless/comments/1ud01yi/best_lighting_for_progress_pictures/) (2026-06-22): aynı ışık, mesafe ve açı job'ı tartışılıyor. App talebi değildir.
- [Reddit /fitness30plus — same poses, same lighting](https://www.reddit.com/r/fitness30plus/comments/1olcdne/) (2025-11-01): aynı açı/pozla side-by-side video paylaşımı gözlendi.
- [Reddit /Renovations — Slow but steady improvements](https://www.reddit.com/r/Renovations/comments/1f5xg5c/) (2024-08-31): aynı mekânın before/after paylaşımı; 12 aydan eski ve weak channel sinyali.

### Builder self-promo: yalnız rekabet/timing

- [SideLens builder post](https://www.reddit.com/r/SideProject/comments/1rxoh33/i_built_sidelens_a_beforeafter_photo_comparison/)
- [Evogram builder post](https://www.reddit.com/r/SideProject/comments/1s2kt7p/i_built_a_progress_photo_app_because_i_was_tired/)
- [Then & Now builder post](https://www.reddit.com/r/iosapps/comments/1rsymv9/i_built_a_progress_photo_app_with_ghost_overlays/)
- [MatchFrame builder post](https://www.reddit.com/r/Appstore/comments/1ujivvb/selfpromotion_i_built_a_ghost_overlay_camera_app/)

Bu dört kayıt kullanıcı talebi veya bağımsız ödeme kanıtı sayılmadı; yalnız exact-feature girişlerinin güncelliğini destekler.

### TikTok content-supply proxy'leri

- [#hairgrowth — TikTok Creative Center, US, 120 gün](https://ads.tiktok.com/business/creativecenter/hashtag/hairgrowth/pc/en?countryCode=US&period=120): erişimde yaklaşık 262K son-120-gün postu ve 2M overall post gösterildi.
- [#homerenovation — TikTok Creative Center, US](https://ads.tiktok.com/business/creativecenter/hashtag/homerenovation/pc/en?countryCode=US&period=30): yaklaşık Mayıs 2026 snapshot'ında 16K son-30-gün ve 985K overall gösterildi; canlı 18 Temmuz sayacı değildir.

Bunlar content supply/channel ölçeğidir; app install veya ödeme talebi değildir.

## Başarısız/eksik protokoller

- [Google Trends US five-year comparison](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=before%20after%20video,progress%20photo,hair%20growth%20tracker,transformation%20video,glow%20up%20video): endpoint HTTP 429 döndürdü; `not_found_after_protocol`. Trends yönü rapora eklenmedi.
- Apple Ads Search Popularity ve search-term export: hesap/export yok; exact aylık organik hacim public olmadığı için `structurally_unobservable`.

## Apple Ads erişimi geldiğinde exact-match paketi

```text
[before after video]
[before and after video]
[before and after video maker]
[progress photo]
[progress photo tracker]
[progress photos]
[progress pics]
[before after photo]
[photo comparison]
[hair growth tracker]
[hair growth timelapse]
[fitness progress tracker]
[body progress photos]
```

Kontrol/negatif adayları:

```text
[transformation video]
[glow up video]
[progress video]
[home renovation progress]
```

## 2026-07-18 genişletilmiş competitor protocol

Karar odaklı ikinci tarama üç kümeyi ayrı tuttu:

1. `before after video maker`, `before after slider`, `before after transition`, `photo compare video` sorgularıyla direct two-photo maker'lar.
2. `progress photos auto alignment`, `ghost overlay camera`, `progress timelapse`, `daily selfie movie` sorgularıyla alignment/progress komşuları.
3. CapCut, Edits, Instagram, InShot, Canva, VN ve Adobe Express için resmi product/help akışlarıyla status quo ikameleri.

### Yeni direct listing'ler

- [Qvyshift Before & After Video Maker](https://apps.apple.com/us/app/before-after-video-maker/id6779032596): offline slider, resolution control, $3.99 one-time, no-subscription beyanı.
- [DiffPix](https://apps.apple.com/us/app/before-after-photo-diffpix/id6749657709): 7 saniyelik 1080p Reel, 4K JPG, local history.
- [Momentum Before and After Video Maker](https://apps.apple.com/us/app/before-and-after-video-maker/id6761030222): dört compare modu, 9:16, GIF/slideshow, 100+ template ve müzik.
- [Before After Before-After](https://apps.apple.com/us/app/before-after-before-after/id6778806327): timeline, opacity ile manual alignment, 14 template ve HD export.
- [CompareKit](https://apps.apple.com/us/app/before-after-video-compare-kit/id6752835989): foto/video input, template, timing, music, logo ve social export.
- [Reveal](https://apps.apple.com/us/app/reveal-before-after-effects/id6758911857): wipe/radial/shape/split/pixelate/zoom-blur/sparkle efektleri.

### Alignment/progress komşuları

- [Body Tracker](https://apps.apple.com/us/app/body-tracker-progress-photos/id6758867697): pose-detection auto crop/rotate alignment.
- [Metamorph](https://apps.apple.com/us/app/progress-pic-photos-metamorph/id6544789120): automatic alignment, overlay, timelapse, GIF/video.
- [Then & Now](https://apps.apple.com/us/app/progress-pics-photo-then-now/id6758411454): bulk import, ghost overlay, slider/timelapse ve 1080p/1440p/original export.
- [MatchFrame](https://apps.apple.com/us/app/matchframe-overlay-camera/id6780443451): photo/video ghost overlay, 9:16/4:5/1:1 ve slideshow/GIF.
- [PhotoJourney](https://apps.apple.com/us/app/my-body-tracker-photojourney/id6499454966): Ghost Mode, import, compare zoom, HD timelapse/GIF.
- [Lapsey](https://apps.apple.com/us/app/lapsey-daily-selfie-photo/id1640066649): guides/import/compare ve $9.99 one-time.

### Resmi status quo kaynakları

- [CapCut official Before & After guide](https://www.capcut.com/resource/before-after-video): manual timeline ve template/batch-replace akışı.
- [CapCut Before & After templates](https://www.capcut.com/explore/before-and-after-video-maker): dedicated use-case template supply.
- [Meta — one year of Edits](https://about.fb.com/news/2026/04/one-year-of-edits-built-for-and-with-creators/): template, overlay ve keyframe ürün genişlemesi.
- [Instagram Reels Align](https://about.fb.com/news/2020/08/introducing-instagram-reels/amp/): önceki klibe göre yeni klip çekim hizası.
- [Canva video effects](https://www.canva.com/features/video-effects/) ve [video transitions](https://www.canva.com/features/video-transitions/): genel template/upload → timeline → effect/timing → export yolu.
- [Adobe Express Reel maker](https://www.adobe.com/express/create/video/instagram/reel): branded Reel template ve resize akışı.

Bu ikinci tarama selected universe'tür; App Store'un eksiksiz census'u veya pazar payı listesi değildir. Yapılandırılmış kayıt: [competitor-expanded.json](competitor-expanded.json).

## Birincil kaynaklar

- [Apple iTunes Search API documentation](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html)
- [Apple App Store search guidance](https://developer.apple.com/app-store/search/)
- [Apple App information limits](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information/)
- [Apple Ads Search Popularity](https://ads.apple.com/app-store/best-practices/recommendations)
- [Apple Ads match types](https://ads.apple.com/app-store/help/keywords/0059-understand-keyword-match-types)
