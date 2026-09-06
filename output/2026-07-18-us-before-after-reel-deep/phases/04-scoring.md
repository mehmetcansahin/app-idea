# Faz 4 — Scoring

## Model

Primary archetype `consumer_utility`; v4.0 ağırlıkları:

| Boyut | Ağırlık |
|---|---:|
| Problem / demand | 25 |
| Monetization / economics | 15 |
| Competitive wedge | 20 |
| Distribution access | 25 |
| Repeat value | 5 |
| Timing | 10 |

Her bound için `Σ(weight × score / 5)` kullanıldı ve yarım yukarı yuvarlandı.

## Boyut puanları

| Boyut | Low | Base | High | Claim'ler | Kalibrasyon |
|---|---:|---:|---:|---|---|
| Problem / demand | 2 | 3 | 4 | `before-demand`, `before-review-pains` | Üç 2K+ rating proxy; direct job/thread; product behavior yok |
| Monetization / economics | 1 | 2 | 3 | `before-paid-demand` | Price architecture var; satış yok; negatif paywall signal |
| Competitive wedge | 1 | 2 | 3 | `before-wedge-preference` | Direct app'ler price/privacy/9:16'i, tracker'lar auto-align'ı kapatıyor; yalnız import-first registration quality seam'i test edilebilir |
| Distribution access | 1 | 2 | 3 | `before-distribution` | Relevant API result ve content supply var; Search Popularity/conversion yok |
| Repeat value | 2 | 3 | 4 | `before-repeat` | Timeline/reminder job'ı var; cohort yok |
| Timing | 2 | 3 | 3 | `before-timing` | Yeni entrants aktif; kategori büyümesi bilinmiyor |

## Hesap

```text
Low  = 25×2/5 + 15×1/5 + 20×1/5 + 25×1/5 + 5×2/5 + 10×2/5 = 28
Base = 25×3/5 + 15×2/5 + 20×2/5 + 25×2/5 + 5×3/5 + 10×3/5 = 48
High = 25×4/5 + 15×3/5 + 20×3/5 + 25×3/5 + 5×4/5 + 10×3/5 = 66
```

**Opportunity:** 28 / 48 / 66 — `borderline`.

## Quick → Deep delta

| Çalışma | Low | Base | High | Evidence | Decision |
|---|---:|---:|---:|---|---|
| Quick Scan | 42 | 60 | 80 | C | TESTE_DEGER |
| Deep | 28 | 48 | 66 | C | TESTE_DEGER |
| Delta | -14 | -12 | -14 | — | Aynı karar, daha dar tez |

Downgrade nedenleri:

1. Metamorph, Body Tracker, SideLens, Then & Now ve MatchFrame eski feature gap'ini doğrudan kapatıyor.
2. Review stratification hedefi karşılanmadı; positive-gain evidence yok.
3. Search Popularity/keyword conversion bulunamadı.
4. Rakip fiyatları WTP olarak kullanılamadı; Qvyshift $3.99 one-time ve ücretsiz Edits/CapCut, $9.99 teklifin “ucuzluk” farkı olmadığını gösterdi.
5. $9.99 lifetime paid acquisition'ı taşıyamıyor; organic dağıtım varsayımı yüksek.

## Evidence grade ve karar

En riskli üç claim:

| Claim | Grade | Impact×uncertainty | Durum |
|---|---|---:|---|
| Wedge preference | C | 9 | Partial |
| Paid demand | C | 9 | Partial |
| Distribution | C | 9 | Partial |

Overall grade top üç claim'in minimumu: **C**.

Fatal gate'ler clear, high ≥40, low <60 ve grade C olduğu için desk karar matrisi **TESTE_DEGER** üretir. `TEST_ONCELIKLI` veya `BUILD_SMALL` koşulu yoktur.
