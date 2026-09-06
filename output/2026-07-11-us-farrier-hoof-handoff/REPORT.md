# US Farrier Hoof Handoff — Quick Scan v4.0

## Karar

**TESTE_DEGER · PREBUILD_PENDING · alternatifler içinde 2. sıra**

Yeni bir scheduling/invoice uygulaması değil; therapeutic-case ağırlıklı farrier için
**standart dört-hoof before/after paketi ve owner-consented vet handoff** test edilmeye değer.
Build izni yoktur.

## Araştırma kontratı

- Geo/storefront/platform: ABD / US App Store / iOS-first, offline saha kullanımı
- Segment: veterinerle düzenli koordinasyon yapan bağımsız farrier
- Arketip: `b2b_prosumer`
- Risk modifier'ları: `regulated`, `sensitive_data`, `platform_dependency`
- Kullanım anı: ayağı bıraktıktan sonra dört foto + kısa not → önceki cycle → vet/client linki
- İkame: The Farriers App, Best Farrier, FarrierIQ, Hoofproof, EQUINET, kâğıt/mesajlaşma

## Gözlenen sinyaller

- Census 2023 geniş NAICS 115210 kategorisinde yaklaşık 62 bin nonemployer ve $3,23 milyar
  receipts gösterir. Kod farrier/hoof trimming yanında boarding, breeding ve başka hizmetleri
  de içerir; exact farrier sayısı değildir. [Census dosyası](https://www2.census.gov/programs-surveys/nonemployer-statistics/data/2023/NS2300NONEMP.zip),
  [NAICS manual](https://www.census.gov/naics/reference_files_tools/2022_NAICS_Manual.pdf)
- [University of Minnesota](https://extension.umn.edu/horse-care-and-management/caring-your-horses-hooves)
  yazın 6–8, kışın 6–12 haftada bir hoof bakımını öneriyor; doğal tekrar döngüsü var.
- [American Farriers Journal 2025](https://www.americanfarriers.com/articles/14720-footcare-and-farrier-business-insights)
  tipik at için yılda sekiz cycle ve full-time farrier için haftada yaklaşık 370 mil/301 at
  bildiriyor. Public sayfada sample n/response rate yoktur.

## Top 5 rakip/ikame

| Ürün | Resmi liste fiyatı | Kapsam |
|---|---:|---|
| [The Farriers App](https://www.thefarriersapp.com/pricing) | $59/ay; ek user $25 | Foto, X-ray/vet doc, cycle, report |
| [Best Farrier](https://bestfarrierapp.com/pricing/) | $30,99/ay | Horse history, foto, route, invoice |
| [FarrierIQ](https://www.farrieriq.com/pricing) | Free; $39/$79 | Measurement, route, referral, AI, portal |
| [Hoofproof](https://apps.apple.com/us/app/hoofproof/id1402097774) | Ücretsiz | Foto/video, annotation, compare, voice |
| [EQUINET](https://apps.apple.com/us/app/equinet-mustad-farrier-app/id1459492568) | Ücretsiz/IAP | Horse log, foto, cycle, schedule, invoice |

[Hoofy](https://apps.apple.com/us/app/hoofy/id6760443944) de $12,99/ay ile aynı alana giriyor.
Dolayısıyla fotoğraf + history + route/schedule wedge değildir. [Haziran 2026 trade araştırması](https://www.americanfarriers.com/articles/15546-farrier-business-trends-reveal-shifting-priorities)
schedule, invoice ve horse records için kâğıt tercihinin sürdüğünü, dijital kullanımın 2024'ten
beri gerilediğini bildiriyor: problem sinyali olduğu kadar adoption karşı sinyalidir.

## Dar ürün hipotezi

1. Farrier işi bitirince yönlendirilmiş dört hoof fotoğrafı.
2. Eldiveni çıkarmadan kısa voice note ve önceki cycle ile side-by-side.
3. Owner consent ile client/vet için standart PDF/link, açılma ve yanıt kaydı.
4. Mevcut takvim/invoice aracına export; business manager olmama.
5. Lameness diagnosis, pathology detection veya shoeing prescription üretmeme.

## v4.0 değerlendirme

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem/talep | 3 | 4 | 4 | Doğal 6–12 haftalık döngü ve trade workflow; exact dijital alt segment yok |
| Monetizasyon/ekonomi | 1 | 2 | 3 | Yalnız rakip fiyatı/public proxy |
| Rekabet/wedge | 1 | 2 | 3 | Foto/history kalabalık; therapeutic handoff test edilmedi |
| Dağıtım erişimi | 2 | 3 | 3 | AFA chapter/retailer/clinic kanalı; traction yok |
| Tekrarlanan değer | 2 | 3 | 3 | Aynı at için doğal cycle; ürün retention'ı yok |
| Zamanlama | 2 | 2 | 3 | Paper devam ediyor ve dijital kullanım gerilemiş |

**Fırsat Çekiciliği: 37 / 56 / 65 · borderline · Kanıt Gücü: C.**

## Gate ve guardrail'ler

Dört gate yalnız administratif observation/handoff kapsamında `clear`.
[AAEP](https://aaep.org/resource/position-on-roles-of-healthcare-providers-in-veterinary-medicine/)
farrier'ı unlicensed allied provider olarak ele alır ve veteriner sağlık kapsamındaki vakalarda
attending veterinarian gözetimini vurgular. AI diagnosis/prescription eklenirse legal/safety
gate yeniden `unknown` olur. X-ray ve vet belgeleri için owner consent, erişim kaydı, encryption
ve silme politikası gerekir. [Apple kuralları](https://developer.apple.com/app-store/review/guidelines/)
uygulanmalıdır.

## Sonraki gerçek davranış testi

Therapeutic vakalarda veterinerle çalışan 8 ABD'li iPhone farrier'a üç haftalık concierge sat:
dört foto + nottan 10 dakika içinde handoff paketi; **$29 peşin/iade edilebilir**. İlerleme
şartı: 4 ödeme; bunların 3'ünün iki haftada 10+ gerçek at kullanması; en az iki owner/vet'in
paketi açıp yanıtlaması. Aynı atın 6–8 haftalık sonraki cycle'ı retention için ayrıca izlenmeli.

## Kanıt ve sınırlamalar

Exact farrier/iPhone alt segmenti, public survey sample n ve response rate bulunamadı. Rakip
liste fiyatı ödeme/retention kanıtı değildir. Trade survey tüm mesleğe genellenemez. Ayrıntılar:
[kanıt defteri](data/evidence-ledger.md).
