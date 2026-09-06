# US Mobile Auto Detail Authorization Proof — Quick Scan v4.0

## Karar

**TESTE_DEGER · PREBUILD_PENDING · düşük öncelik**

Before/after ve damage-proof pazarı beklenenden kalabalık. Yalnız mevcut CRM'i değiştirmeyen,
**üç dakikadan kısa guided capture → fotoğrafa bağlı add-on onayı → paired after** katmanı
ucuz davranış testine değer. Build izni yoktur.

## Araştırma kontratı

- Geo/storefront/platform: ABD / US App Store / iOS-first
- Segment: ayda 20+ ücretli işi olan solo mobile detailer
- Arketip: `b2b_prosumer`
- Risk modifier'ları: `sensitive_data`, `platform_dependency`
- Kullanım anı: driveway'da iş öncesi walkaround → scope/add-on onayı → handoff proof
- İkame: DetailProof, DetailFlash, DetailDeck, Mobile Tech RX, Urable, Camera Roll/waiver

## Gözlenen sinyaller

- Census 2023 CBP'de NAICS 811192 altında 19.807 employer establishment var. Kod detail shop,
  car wash ve mobile car/truck wash'ı birlikte içerir; solo mobile detailer sayısı değildir.
  [Census CBP](https://www.census.gov/data/datasets/2023/econ/cbp/2023-cbp.html),
  [NAICS tanımı](https://www.census.gov/naics/resources/archives/sect81.html)
- Public detailer tartışmalarında [chargeback](https://www.reddit.com/r/AutoDetailing/comments/xa88wb),
  [pre-existing damage](https://www.reddit.com/r/Detailing/comments/12y9q1e) ve
  [damage claim](https://www.reddit.com/r/Detailing/comments/1rqw9nx/why_preexisting_damage_waivers_is_not_enough/)
  için fotoğraf/walkaround/imzalı kayıt önerileri tekrar ediyor. Örnekler self-selected,
  denominatörsüz ve pazar prevalansı değildir.

## Top 5 rakip

| Ürün | Resmi liste fiyatı | Kapsam |
|---|---:|---|
| [DetailProof](https://www.detailproof.app/) | $14,99/ay; $129,99/yıl | Guided before/after, damage, signature, PDF |
| [DetailFlash](https://detailflash.com/) | $29/ay | <3 dakika walkaround, signed baseline, offline |
| [DetailDeck](https://www.mydetaildeck.com/) | $29/ay | Conditional photos, after sign-off, CRM |
| [Mobile Tech RX](https://www.mobiletechrx.com/plans/) | $39/ay başlangıç | Estimate, payment, timestamped before/after |
| [Urable](https://urable.com/pricing/) | $70/ay; video inspection $183/ay | Approval, image storage, route, inspection |

Üstelik [Menutize](https://menutize.ai/use-case/auto-detailing) CRM, estimate, invoice, payment
ve before/after log'u ücretsiz sunuyor. [DetailProof App Store](https://apps.apple.com/us/app/detailproof/id6766636855)
Mayıs 2026 itibarıyla 1 rating'li exact iOS rakip: traction bilinmiyor ama feature wedge'ini
çürütüyor.

## Dar ürün hipotezi

1. Sekiz yönlendirilmiş before fotoğrafı ve mevcut hasar işareti.
2. Fotoğrafa bağlı, fiyatlı add-on; müşterinin aynı iPhone/link üzerinde approve/decline'ı.
3. Aynı açıları eşleyen after capture ve timestamp'li handoff linki.
4. Plaka/yüz redaksiyonu; CRM, booking, invoice ve payment yok.
5. AI damage kararı veya “hukuki feragat garantisi” iddiası yok.

## v4.0 değerlendirme

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem/talep | 2 | 3 | 4 | Uyuşmazlık örnekleri ve ürünleşmiş workflow var; frekans yok |
| Monetizasyon/ekonomi | 1 | 2 | 3 | Yalnız rakip fiyatı; ücretsiz baskı var |
| Rekabet/wedge | 1 | 1 | 2 | Exact özellikler commodity; standalone hız hipotezi test edilmedi |
| Dağıtım erişimi | 2 | 3 | 3 | IDA/MTE/supplier/community kanalı; traction yok |
| Tekrarlanan değer | 2 | 3 | 3 | Her araç doğal döngü; ürün retention'ı yok |
| Zamanlama | 2 | 2 | 3 | Yeni exact ürünler var, fakat yapısal pencere kanıtlanmadı |

**Fırsat Çekiciliği: 32 / 48 / 62 · borderline · Kanıt Gücü: C.**

## Gate ve guardrail'ler

Dört gate bu dar kapsamda `clear`. Kamera, offline storage, paired capture ve SMS linki canlı
rakiplerle teknik olarak doğrulanıyor. Müşteri onayı, fotoğraf/konum retention ve silme açık
olmalı; signature hukuki koruma garantisi diye pazarlanmamalıdır. AI yalnız “review suggested”
üretebilir; detailer ve müşteri doğrular. [Apple kuralları](https://developer.apple.com/app-store/review/guidelines/)
uygulanmalıdır.

## Sonraki gerçek davranış testi

Son 30 günde 20+ ücretli işi ve son 6 ayda en az bir scope/damage uyuşmazlığı olan 12 kişiyi
tara; 6 detailer'a 10 gerçek işlik concierge pilotu **$29 peşin** sat. İlerleme: 4 ödeme;
en az 3'ünün ikinci ve beşinci doğal işte kullanması; medyan başlangıç capture'ı <3 dakika;
customer approval completion ≥%80. Eşiklerden biri kalırsa dur/pivot.

## Kanıt ve sınırlamalar

Census kategorisi broad; community örnekleri self-selected; exact iPhone alt segmenti ve
dispute frekansı yok. Rakip liste fiyatı ödeme/retention değildir. Ayrıntılar:
[kanıt defteri](data/evidence-ledger.md).
