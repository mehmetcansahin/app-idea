# Report chart map

Delivery surface: MCP app report. Audience: product stakeholders. Snapshot: 2026-07-18.

| Report segment | Analytical question | Family / type | Fields | Supported claim | Palette | Provenance |
|---|---|---|---|---|---|---|
| Deep score calibration | Quick ve Deep opportunity range'i nasıl değişti? | Comparison / grouped vertical bar | `bound`, `quick_score`, `deep_score`, `delta` | Deep research lowered all three bounds under the same v4 methodology | Two-root categorical | `score-source` |
| Direct competitor traction | Seçilmiş direct rakiplerde görünür rating traction nerede yoğunlaşıyor? | Ranking / horizontal bar | `app`, `rating_count`; release/update/price/output in tooltip | Visible rating counts sit in older utilities; recent exact entrants have little observable rating traction | Single-root blue | `competitor-traction-source` |
| Recent review pains | Erişilebilen küçük recent-review örnekleminde hangi temalar tekrarlandı? | Comparison / horizontal bar | `theme`, `count`; `sample_n`, window and coverage in tooltip | Monetization friction dominates the accessible n=11 negative sample; prevalence cannot be inferred | Single-root blue | `review-themes-source` |

The two horizontal bars answer different questions: one ranks apps by a storefront proxy, the other ranks coded themes within a review sample. Tables are used for exact feature/price/workflow lookup. No time-series chart is used because the evidence does not contain a sufficiently dense historical series. No scatter is used because rating count and price do not share a causal or comparable denominator and would invite false inference.

QA contract:

- Rating count is labeled as a proxy, never installs, revenue or retention.
- Bars start at zero; zero-rating recent entrants remain in source rows and visible labels/table detail.
- Long app/theme labels use horizontal orientation.
- Each chart has an adjacent narrative block in the report reading path.
- The direct-competitor chart source dataset retains release date, update date, price model, output and advertised-alignment context beyond the plotted fields.
