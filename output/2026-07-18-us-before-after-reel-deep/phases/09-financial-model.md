# Faz 9 — Financial Model

## Sınıflandırma

Bu model **pre-launch planning scenario**'dur; forecast, market benchmark veya rakip gelir tahmini değildir. First-party install, conversion, refund, retention ve support verisi yoktur.

Structured model: [financial-scenarios.json](../data/financial-scenarios.json)

## Offer hipotezi

- Ücretsiz: sınırsız preview + bir watermark'lı export.
- Pro Lifetime: **$9.99 one-time**.
- Unlock: watermark removal, aspect options, unlimited exports.
- Weekly subscription yok.

Bu fiyat bir “ucuz rakip” iddiası değildir. US storefront taramasında Qvyshift **$3.99 one-time**, Lapsey **$9.99 one-time** sunarken Edits ücretsiz ve CapCut free-tier bir status quo oluşturuyor. Dolayısıyla $9.99, yalnızca gerçek ödeme davranışıyla sınanacak bir trust/offer hipotezidir; rekabet avantajı veya doğrulanmış willingness-to-pay değildir.

Aboneliğe ancak şu ürün davranışıyla dönülür:

- Paid users'ın ≥%30'u D30'da ikinci proje.
- Professionals aylık ≥3 export.
- Brand preset, batch workflow veya template updates gibi gerçek ongoing value.

Bu durumda $19.99–$24.99/year Creator hipotezi ayrı test edilir.

## Formüller

```text
Developer proceeds = installs × conversion × (1-refund) × $9.99 × 0.85
Paid spend        = installs × paid share × paid CPI
Support labor     = purchasers × ticket rate × minutes/60 × $30/hour
Contribution      = proceeds - paid spend - support labor
```

`0.85`, Apple Small Business Program'a kabul ve %15 komisyon varsayımıdır. Uygunluk/acceptance ayrıca doğrulanır.

## Senaryolar

| Girdi/çıktı | Low | Base | High |
|---|---:|---:|---:|
| Aylık install | 1,000 | 10,000 | 50,000 |
| Organic / paid | 60% / 40% | 80% / 20% | 90% / 10% |
| Paid CPI varsayımı | $2.50 | $1.50 | $1.25 |
| Purchase conversion | 2% | 4% | 6% |
| Refund | 8% | 5% | 3% |
| Purchasers | 20 | 400 | 3,000 |
| Developer proceeds | $156 | $3,227 | $24,710 |
| Paid spend | $1,000 | $3,000 | $6,250 |
| Support | $16 | $150 | $540 |
| **Contribution** | **-$860** | **+$77** | **+$17,920** |

Support varsayımları:

- Low: %8 ticket × 20 dk.
- Base: %5 × 15 dk.
- High: %3 × 12 dk.
- Saatlik kurucu/support opportunity cost: $30.

## Unit economics yorumu

Base durumda:

- Net proceeds/install ≈ $0.323.
- Support/install ≈ $0.015.
- Support sonrası paid CPI tavanı ≈ **$0.31**.
- Varsayılan paid CPI $1.50 ise paid cohort tek başına zarar eder.
- Toplamın başa baş görünmesi %80 organic install varsayımındandır.

Low durumda paid share yüksekken model ağır zarar eder. High durumda contribution iyi görünür; fakat 50K aylık install ve %90 organic bilinmeyen, agresif varsayımlardır.

## Commission sensitivity

Small Business %15 yerine %30 komisyon olursa base proceeds yaklaşık $2,657, contribution yaklaşık **-$493** olur. Bu sensitivity tek başına riskin Apple fee olmadığını; asıl hassasiyetin distribution mix ve conversion olduğunu gösterir.

## Hariç tutulanlar

- Vergi ve FX.
- App Store adjustments/refunds dışı settlement farkları.
- $99 Apple Developer annual fee.
- Test cihazı, design/software tool maliyeti.
- Development time.
- Content production ve organic founder labor.
- Legal/privacy review.

## Ekonomik karar

- Paid acquisition birincil ölçek motoru olmamalı.
- ASO, export/share attribution loop, creator demo content ve segment referral kanalları test edilmeli.
- $9.99 lifetime fiyatı, $3.99 direct alternatif ve ücretsiz editörler açıkça gösterilerek prebuild'de gerçek depozitoyla ölçülmeli.
- Revenue olmadan rakip weekly/lifetime SKU'ları benchmark diye kullanılmamalı.
- D30 repeat yoksa subscription açılmamalı.

Desk monetization/economics score bu nedenle 1/2/3 ve evidence C'dir.
