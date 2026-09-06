# Faz 8 — ASO Research

## Scope ve protokol

- Tarih: 2026-07-18
- Storefront/platform: US / iOS
- Apple iTunes Search API: `country=us`, `entity=software`, `limit=20`
- İlk 17–20 sonuç manuel relevance coding
- Apple web cards ve autocomplete/search-hints destekleyici kontrol

Public API sırası App Store client rank'i değildir. Result count, exact-title count ve ratings keyword hacmi değildir.

Structured snapshot: [keyword-results.json](../data/keyword-results.json)  
Raw protocol: [raw-search-results.md](../data/raw-search-results.md)

## Query özeti

| Query | İlgili / dönen | Video/timelapse | Exact title | Kullanım |
|---|---:|---:|---:|---|
| `before after video` | 15/18 | 12 | 3 | Primary |
| `before and after video maker` | 7/20 | 6 | 2 | Primary long-tail |
| `progress photo` | 18/19 | 4 | 1 + plural variants | Primary capture intent |
| `photo comparison` | 5/18 | düşük | 1 | Secondary |
| `before after reel` | 12/18 | 9–10 | 0 | Creative copy; volume unknown |
| `hair growth progress` | 8/17 | 0 | 0 | Tracker/segment intent |
| `fitness progress video` | 4/19 | 1 | 0 | Creative segment |
| `home renovation progress` | 1/18 | 0 | 0 | ASO zayıf; channel segment |
| `progress video` | 4/19 | 1 | 0 | Broad/avoid |
| `transformation video` | 0/18 | 0 | 0 | AI/editor wrong intent |
| `glow up video` | 0/18 | 0 | 0 | Beauty/fantasy wrong intent |

## Autocomplete

Gözlenen güçlü aileler:

- `before and after video`
- `before and after photo compare`
- `before after photo`
- `progress photo tracker`
- `body progress photos`
- `progress photos`
- `progress pics`
- `hair growth tracker`
- `hair growth timelapse`

`before after reel`, `transformation v` ve gerçek `progress video` işi için güvenilir öneri gözlenmedi. Search-hints kararlı dokümante API değildir ve hacim sayılmaz.

## Search Popularity gap

Apple, Search Popularity'yi 1–5 olarak tanımlar ve 5'i en yüksek seviye olarak açıklar. Ancak bu çalışma için:

- Apple Ads keyword recommendations yok.
- Search Popularity export yok.
- Search-term, impression, tap, install, CPT, CPA yok.
- Exact aylık organik query count public değil.

Status: `structurally_unobservable`. Search API result count/rank/rating bu verinin ikamesi değildir.

## Positioning

En iyi birleşik job:

> Progress photos'u otomatik hizalayıp before/after Reel'e çevir.

Yalnız “Reel maker” capture/repeat intent'i kaçırır; yalnız “tracker” shareable output'u zayıflatır.

### Metadata hipotezi

- Name: `Progress Reel: Before & After` — 29 karakter.
- Subtitle: `Align Photos Into Timelapses` — 28 karakter.
- Keyword field: `video,maker,compare,tracker,pics,fitness,body,hair,growth,renovation,home,journey`

Apple name 30, subtitle 30 ve keyword field 100 karakter sınırlarını uygular. Name/subtitle'da bulunan kelimeler keyword field'de tekrarlanmadı.

### Primary set

`before after video`, `before and after video`, `progress photo`, `progress photos`, `progress photo tracker`, `progress pics`, `before after photo compare`.

### Secondary/use-case set

`hair growth tracker`, `hair growth timelapse`, `fitness progress tracker`, `body progress photos`, `home renovation before after`, `photo comparison`.

### Kaçınılacak

`transformation video`, `glow up video`, broad `progress video`; `home renovation progress` primary ASO olmamalı.

## Creative concepts

### Stop the Jitter

Önce sağa-sola zıplayan altı progress fotoğrafı; sonra overlay/align ve sabit anchor'lı 9:16 output. Hook: `Your progress changed. Your framing shouldn't.`

### One App, Three Transformations

Art/DIY, hair-growth ve room-renovation için aynı pair→align→reveal formatı. Bu bir brand kararı değil, segment başına qualified-task maliyetini ölçen creative testidir.

### Private Camera Roll to Shareable Reel

Camera roll→iki foto seç→align→export; hesap yok ve local processing. Body/hair için “save privately or share” dili.

## Channel evidence

- Reddit'te stabil omuz anchor'ı ve ghost overlay doğrudan istendi.
- Hair community aynı angle/light consistency job'ını tartışıyor.
- TikTok Creative Center #hairgrowth büyük content supply gösteriyor; app demand değildir.
- Home renovation yüksek content supply taşıyabilir fakat App Store query'si oyun/design niyetine kayıyor.

## Düşük maliyetli acquisition ölçümü

Landing waitlist ana kanıt değildir. Teknik RAT sonrası her segment için ayrı creative çalıştırılabilir; ancak ilk behavior cohort Art/DIY olarak sabit kalır.

İzlenecek acquisition metriği:

- Creative → real-pair qualified task maliyeti.
- Qualified task completion.
- Deposit conversion.
- Source/segment ayrımı.

CTR ve universal conversion için baseline yoktur; ilk tur yalnız yönsel kalibrasyon üretir.

## Apple Ads erişimi geldiğinde exact paket

`before after video`, `before and after video`, `before and after video maker`, `progress photo`, `progress photo tracker`, `progress photos`, `progress pics`, `before after photo`, `photo comparison`, `hair growth tracker`, `hair growth timelapse`, `fitness progress tracker`, `body progress photos`.

Kontrol/negatif: `transformation video`, `glow up video`, `progress video`, `home renovation progress`.

## Kaynaklar

- [Apple iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/Searching.html)
- [App Store search guidance](https://developer.apple.com/app-store/search/)
- [App information limits](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information/)
- [Apple Ads Search Popularity](https://ads.apple.com/app-store/best-practices/recommendations)
- [Apple Ads match types](https://ads.apple.com/app-store/help/keywords/0059-understand-keyword-match-types)

