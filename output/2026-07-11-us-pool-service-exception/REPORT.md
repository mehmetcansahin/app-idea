# US Pool-Service Capture/Export — Quick Scan v4.0

## Karar

**TESTE_DEGER · PREBUILD_PENDING · alternatifler içinde 1. sıra**

Kimyasal öneri veren yeni bir pool-management suite değil; ölçüm, fotoğraf, timestamp ve
müşteri raporunu **mevcut sisteme taşıyan 30–60 saniyelik capture/export katmanı** test
edilmeye değer. Build izni yoktur.

## Araştırma kontratı

- Geo/storefront/platform: ABD / US App Store / iOS-first, offline saha kullanımı
- Segment: mevcut billing/route yazılımını bırakmak istemeyen solo pool-service operator
- Arketip: `b2b_prosumer`
- Risk modifier'ları: `sensitive_data`, `platform_dependency`
- Kullanım anı: havuz başında ölçüm → foto → yapılan iş → müşteri raporu/export
- İkame: Skimmer, Pool Office Manager, Paythepoolman, PoolCarePRO, PoolDial, kâğıt/Excel

## Gözlenen sinyaller

- Census 2023 NES'te geniş NAICS 561790 kategorisi yaklaşık 142 bin nonemployer ve
  $5,81 milyar receipts gösteriyor. Kod pool cleaning yanında birçok bina hizmetini içerir;
  exact segment sayısı değildir. [Census dosyası](https://www2.census.gov/programs-surveys/nonemployer-statistics/data/2023/NS2300NONEMP.zip),
  [NAICS tanımı](https://www.census.gov/naics/?details=561790&input=561790&year=2022)
- [CDC](https://www.cdc.gov/healthy-swimming/about/home-pool-and-hot-tub-water-treatment-and-testing.html)
  su kimyasının rutin ölçümünü ve belgelendirmeyi temel bakım davranışı olarak tanımlar.
- [Skimmer 2026](https://www.getskimmer.com/stateofpoolservice) 1.600+ profesyonel ile
  35.000+ platform kullanıcısı ve 1 milyon+ pool kapsadığını; katılımcıların %63'ünün
  dijital/photo-video rapor beklentisi gördüğünü bildiriyor. Vendor araştırmasıdır.

## Top 5 rakip/ikame

| Ürün | Resmi liste fiyatı | Kapsam |
|---|---:|---|
| [Skimmer](https://www.getskimmer.com/pricing) | $1/pool, min $49; gelişmiş min $98 | Reading, dose, foto, rapor, rota, invoice |
| [Pool Office Manager](https://poolofficemanager.com/) | $125/ay ilk kullanıcı | Kimyasal, envanter, proof, rota |
| [Paythepoolman](https://www.paythepoolman.com/) | $50 baz + $15/teknisyen | Rota, billing, GPS, service log |
| [PoolCarePRO](https://www.poolcarepro.com/pricing) | $39,95–$99,95/ay | Solo'dan enterprise'a yönetim |
| [PoolDial](https://pooldial.com/pricing) | $2/pool, min $40 | Kimya, rota, CRM, portal |

[Skimmer Pro](https://apps.apple.com/us/app/skimmer-pro/id1249069756) 4,6 puan ve yaklaşık
3,1 bin rating ile ölçüm, geçmiş, fotoğraf ve proof-of-service parity'si gösteriyor. Tek bir
yorum Excel export istiyor; bu yalnız yön gösteren mikro-wedge sinyalidir. Skimmer'ın raporunda
yazılım arayanların %68'inin all-in-one istemesi point-solution'a güçlü karşı kanıttır.

## Dar ürün hipotezi

1. Offline pool/customer açılışı; test değerleri ve fotoğraf capture.
2. Yapılan işi işaretleyip timestamp'li müşteri proof'u üretme.
3. Share Sheet/CSV/PDF ile incumbent'a gerçekten aktarma.
4. Kimyasal doz, karışım veya güvenlik tavsiyesi vermeme.
5. CRM, route, billing ve invoice'ı ilk üründen çıkarma.

## v4.0 değerlendirme

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem/talep | 3 | 4 | 5 | Tekrarlanan saha zorunluluğu ve ölçekli incumbent kullanımı; exact solo segment yok |
| Monetizasyon/ekonomi | 1 | 2 | 3 | Yalnız rakip fiyatı/vendor metriği |
| Rekabet/wedge | 1 | 2 | 3 | Full parity güçlü; yalnız zero-switch export boşluğu test edilebilir |
| Dağıtım erişimi | 2 | 3 | 3 | IPSSA/PHTA kanalı var; traction ve CAC yok |
| Tekrarlanan değer | 2 | 3 | 3 | Her servis ziyaretinde döngü; ürün retention'ı yok |
| Zamanlama | 2 | 3 | 4 | Dijital müşteri raporu yönü var; all-in-one tercihi karşı sinyal |

**Fırsat Çekiciliği: 37 / 57 / 71 · borderline · Kanıt Gücü: C.**

## Gate ve guardrail'ler

Dört gate, ürün yalnız kayıt/export ise `clear`. [CDC chemical safety](https://www.cdc.gov/healthy-swimming/toolkit/pool-chemical-safety.html)
kimyasal yaralanma riskini ve eğitimli kullanım gereğini vurgular. Doz veya karışım önerisi
eklenirse safety/legal gate yeniden `unknown` olur. Adres, konum ve ev fotoğrafı için açık izin,
retention/deletion ve veri minimizasyonu gerekir. [Apple kuralları](https://developer.apple.com/app-store/review/guidelines/)
uygulanmalıdır.

## Sonraki gerçek davranış testi

Mevcut yazılımından memnun olmayan 8–10 solo iPhone operatörüne iki gerçek haftalık rota
boyunca concierge capture/export sat; **$29 iade edilebilir peşin ödeme** al. İlerleme şartı:
en az 4 ödeme ve bunların en az 3'ünün uygun ziyaretlerin %70+'ında iki hafta kullanıp çıktıyı
gerçek sisteme aktarması. İkinci ücretli rota döngüsü görülmeden build kararı yok.

## Kanıt ve sınırlamalar

Exact US solo-pool-service/iPhone sayısı bulunamadı. Skimmer metrikleri vendor self-report,
App Store yorumu self-selected ve fiyatlar ödeme/retention kanıtı değildir. Ayrıntılar:
[kanıt defteri](data/evidence-ledger.md).
