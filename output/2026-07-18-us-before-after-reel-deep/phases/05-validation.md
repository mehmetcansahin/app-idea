# Faz 5 — Evidence Audit ve Validation

## Claim reconciliation

Quick Scan'deki şu çıkarım Deep'te kısmen çürütüldü:

> “2–24 fotoğrafı tek anchor'a auto-align edip tarihli 9:16 export etmek test edilebilir bir feature boşluğudur.”

Deep gözlem:

- Metamorph: automatic alignment + overlay + reminder + timelapse/GIF/video.
- Body Tracker: pose auto-alignment + timeline + timelapse.
- SideLens: ghost overlay + multi-stage timeline + journey video.
- Then & Now ve MatchFrame: ghost overlay, projects/import ve animated output.

Sonuç: generic feature-gap claim'i desteklenmiyor. Yalnız import-first, iki-photo, fast/full-frame export kombinasyonunun **tercih farkı** test edilmeye devam edebilir.

## Doğrudan gözlem / çıkarım ayrımı

| Konu | Doğrudan gözlem | İzin verilen çıkarım | İzin verilmeyen iddia |
|---|---|---|---|
| Demand | Üç app 2K+ rating | Job tek ürüne özgü değil | Kategori aylık X install üretir |
| Review | n=11'de alignment/export/paywall pain | Quality wedge test edilmeli | Pain pazarın %Y'sinde var |
| Competition | Exact entrants feature listeliyor | Generic wedge zayıf | Feature'lar iyi çalışıyor veya satıyor |
| ASO | API ilgili sonuçlar döndürüyor | Keyword-family relevance var | Exact keyword hacimli veya rank kolay |
| Price | $0.99 one-time–$7.99 weekly/$99.99 lifetime | Offer test alanı geniş | Kullanıcı bu fiyatları ödüyor |
| Technology | Apple API'leri mevcut | Cihaz-içi prototip mümkün | Gerçek pairlerde accuracy/performance geçer |

## Source independence

- Aynı Apple ürün sayfasını aktaran üçüncü taraf listing'ler bağımsız kaynak sayılmadı.
- Her rakipte `independence_root` seller/legal entity'dir.
- Apple official dokümanları tek `Apple Inc.` root'u olarak ele alındı.
- Builder Reddit post'ları o ürünün feature/timing kaynağıdır; bağımsız demand değildir.
- Review author ID, tek review düzeyinde ayrı gözlem olabilir; review sampling root'u Apple RSS'dir.

## Review audit

Standard hedef app başına 10 düşük / 5 orta / 10 yüksek yıldız review'dur. Page 1–10 cap sonrasında:

- Top five all-time accessible: 322.
- Son 12 ay: 11.
- 1–2★: 11; 3★: 0; 4–5★: 0.
- Minimum karşılanmadı; `not_found_after_protocol`.

Bu eksik, overall evidence grade'i C'de tutar. Gains yokluğu negatif pazar kanıtı olarak kullanılmadı.

## ASO audit

- Apple public Search API query relevance için kullanıldı.
- Public API sıra ve result count'u rank/volume olarak sunulmadı.
- Apple Ads Search Popularity 1–5 ve search-term export erişilemedi.
- Exact monthly organic query count `structurally_unobservable`.
- Google Trends endpoint'i HTTP 429; `not_found_after_protocol` ve rapordan çıkarıldı.

## Fatal gates

### LEGAL_BLOCKED — clear

Kullanıcı-seçimli fotoğrafları cihazda dönüştürmeye genel bir yasak gözlenmedi. Uygulanacak kurallar: privacy/data minimization, content rights, subscription ongoing value, copycat ve minimum functionality. Müzik ilk scope'ta yoktur.

### CORE_FEASIBILITY_BLOCKED — clear

PhotosPicker, Vision registration/landmarks, Core Image ve AVAssetWriter resmi teknik yolu sağlar. Gate “blok yok” anlamındadır; accuracy/memory/export RAT'ı hâlâ zorunludur.

### PLATFORM_BLOCKED — clear

PhotosPicker seçili medyayı, AVFoundation output'u ve Share Sheet/Photos add-only dağıtımı destekler. Full Photos read access, backend veya özel entitlement gerekmiyor.

### SAFETY_ETHICS_BLOCKED — clear

Human image'da yalnız similarity transform; non-rigid warp yok. Body fat, skin age, hair growth veya medical outcome ölçümü/iddiası yok. Professional hair/beauty kullanımında client consent gerekir.

## Policy risk register

| Risk | Önlem | Test |
|---|---|---|
| 4.1/4.2 copycat/minimum functionality | Align quality, manual fallback, metadata stripping, reliable export | Review Notes + actual binary |
| Subscription ongoing value | İlk offer lifetime; weekly yok | D30 repeat olmadan subscription açma |
| Photo privacy | PhotosPicker, local processing, temp delete | Privacy manifest/label + network audit |
| Misleading transformation | Human non-rigid warp yok; Raw/Aligned compare | Catastrophic-warp blind audit |
| Content rights/music | User-selected media; MVP'de music yok | Metadata ve review checklist |
| Paywall deception | Fiyat export öncesi açık; watermark path net | Usability + Store screenshot audit |

## Reproducibility

- Structured inputs: `data/competitors.json`, `data/review-sample.json`, `data/keyword-results.json`, `data/financial-scenarios.json`.
- Score ve finans formülleri: `analysis/before_after_deep_analysis.ipynb`.
- Evidence: `data/evidence.jsonl`; ledger script ile deterministik üretilir.
- Validation: `python3 scripts/evidence_tool.py render <dir>` ardından `validate`.

## Validation sonucu

Desk evidence paylaşılabilir fakat iki kritik erişim açığı vardır: Apple Ads Search Popularity ve review stratified minimum. Karar **TESTE_DEGER**, durum **PREBUILD_PENDING** kalır.

