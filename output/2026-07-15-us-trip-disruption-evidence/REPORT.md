# US Trip Disruption Evidence — Quick Scan

**Tarih:** 2026-07-15  
**Kapsam:** ABD / US App Store / iPhone  
**Arketip:** Consumer Utility  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

Doküman işi gerçek: [Travel Guard](https://www.travelguard.com/help-center/claims/required-claim-documents) itinerary, receipts, carrier delay report ve refund/credit records istiyor. Fakat [RefundMe](https://apps.apple.com/us/app/refundme-ai-travel-claims/id6746415139) screenshot import, gap finder, claim prep/submission, escalation ve timeline'ı zaten sunuyor; Flighty ve TripIt upstream akışı sahipleniyor.

En güvenli scope yalnız evidence organizer'dır. Eligibility, insurance coverage, legal claim veya “ne kadar alırsın” hesabı yapılırsa [DOT](https://www.transportation.gov/individuals/aviation-consumer-protection/refunds) kuralları, policy terms ve carrier contract değişimleri ciddi bakım ve doğruluk riski yaratır.

## Skor

| Boyut | Low | Base | High |
|---|---:|---:|---:|
| Problem/talep | 2 | 3 | 4 |
| Monetizasyon | 1 | 2 | 3 |
| Wedge | 1 | 2 | 3 |
| Dağıtım | 2 | 2 | 3 |
| Tekrar değeri | 1 | 2 | 3 |
| Zamanlama | 2 | 3 | 4 |

**Fırsat Çekiciliği:** **32 / 47 / 67 — borderline**  
**Kanıt Gücü:** **C**

## Sonraki test

İki airport/traveler community kanalında 20 disrupted traveler'a **$9 manuel evidence-pack service** sat; itinerary, receipt, carrier notice ve refunds'ı düzenle, fakat eligibility tavsiyesi verme.

**Stop:** 6'dan az ödeme, 5'ten az completed packet veya airline/insurer/card-benefit claim'inde kullanılan 3'ten az packet varsa durdur.

Bu masa başı karar build izni değildir.
