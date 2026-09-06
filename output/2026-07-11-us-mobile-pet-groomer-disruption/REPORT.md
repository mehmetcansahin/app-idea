# US Mobile Pet Groomer Disruption Recovery — Quick Scan v4.0

## Karar

**TESTE_DEGER · PREBUILD_PENDING**

Genel grooming CRM'i değil; **offline-first day sheet + hizmet süresini hesaba katan
van arızası/hastalık sonrası dinamik yeniden planlama** davranış testine değer. Build izni yoktur.

## Kontrat ve problem

- ABD / US storefront / iOS; solo veya küçük mobile pet groomer
- Arketip: `b2b_prosumer`; modifier: `sensitive_data`, `platform_dependency`
- Kullanım: sıradaki adres/pet notu → gün bozulunca yeni sıra → müşteri teyidi
- İkame: mevcut CRM, Maps/Calendar, SMS ve manuel arama

Census 2023'te geniş pet-care kodunda 146.763 nonemployer ve $3,62 milyar receipts
bulunuyor; yalnız 40.936 işletme $25 bin+ receipts üretiyor. Kod grooming yanında boarding,
sitting ve training içerdiği için mobile-groomer sayısı değildir. MoeGo ve DaySmart yorumları
saha yavaşlığı/booking sorunları gösterirken, MoeGo'nun rota dokümanı service duration ve
buffer'ın hâlâ manuel olduğunu gösteriyor.

## Top 5 rakip/ikame

| Ürün | Resmi liste fiyatı | Kapsam |
|---|---:|---|
| [MoeGo](https://www.moego.pet/pricing) | $49/ay | Mobile grooming CRM ve rota |
| [Pawfinity](https://www.pawfinity.com/pricing/) | $55–$60/ay | Mapping, POS, SMS |
| [DaySmart Pet](https://www.daysmart.com/pet/pricing/) | $29–$39/ay | Booking, reminder, payment |
| [Gingr](https://www.gingrapp.com/pricing) | $100–$109/ay | Spa operasyon paketi |
| [Square Appointments](https://squareup.com/us/en/appointments/pricing) | $0 / $49 / $149 | Genel scheduling ikamesi |

## v4.0 değerlendirme

| Boyut | Low | Base | High |
|---|---:|---:|---:|
| Problem/talep | 3 | 4 | 4 |
| Monetizasyon/ekonomi | 2 | 2 | 3 |
| Rekabet/wedge | 2 | 3 | 3 |
| Dağıtım erişimi | 2 | 3 | 3 |
| Tekrarlanan değer | 3 | 3 | 3 |
| Zamanlama | 2 | 3 | 3 |

**Fırsat Çekiciliği: 48 / 60 / 65 · borderline · Kanıt Gücü: C.**

## Gate, test ve durdurma

Dört fatal gate `clear`; adres, gate code, pet sağlık notları ve rota sağlayıcısı başlıca
risklerdir. Kart verisi tutulmamalı; consent, retention ve redaction tanımlanmalıdır.

12 ücretli CRM kullanıcısına bir haftalık concierge disruption recovery sun ve gerçek
bozulmuş günler için **$25–39 depozito** iste. En az 3 depozito ve en az 2 ikinci doğal
kullanım çıkmazsa durdur. Bu test E3 üretebilir; waitlist üretemez.

Exact mobile-groomer alt segmenti yapısal olarak gözlenemiyor; review/Reddit sinyalleri
temsili değildir. Ayrıntı: [kanıt defteri](data/evidence-ledger.md).

