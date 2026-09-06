# US RefundLoop — Quick Scan

**Tarih:** 2026-07-15  
**Kapsam:** ABD / US App Store / iPhone  
**Arketip:** Consumer Subscription  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

Problem büyük, ürün alanı ise artık kalabalık. [NRF](https://nrf.com/research/2025-retail-returns-landscape) online satışların %19.3'ünün iade edileceğini tahmin ediyor; ancak bu aggregate hacim unutulan refund veya app subscription talebi değildir. ReturnTrack, Return Proof, Returno Refundo, BackBye, Returnful ve Jareon deadline, receipt, package, refund status ve evidence işlerini büyük ölçüde kapsıyor.

Özellikle [ReturnTrack](https://apps.apple.com/us/app/returntrack-refund-tracker/id6754392016) receipt/label OCR, deadline, package/refund tracking ve $6.99/ay–$39.99/yıl fiyatıyla; [Return Proof](https://typeswitch.net/return-proof-app/) ise condition, packing, drop-off ve PDF evidence ile ilk fikrin çekirdeğini doğrudan karşılıyor.

## Degerlendirme

| Boyut | Low | Base | High |
|---|---:|---:|---:|
| Problem/talep | 3 | 4 | 4 |
| Monetizasyon | 1 | 2 | 3 |
| Wedge | 1 | 1 | 2 |
| Dağıtım | 1 | 2 | 2 |
| Tekrar değeri | 2 | 3 | 3 |
| Zamanlama | 3 | 4 | 4 |

**Fırsat Çekiciliği:** **34 / 51 / 58 — borderline**  
**Kanıt Gücü:** **C**

High senaryonun bile 60'a ulaşmaması ve exact-product yoğunluğu bu fikri alt sıraya indiriyor. Metodoloji gereği yüksek skor 40'ın üstünde kaldığından masa başında otomatik `ELENDIR` çıkmıyor; bu, bütçe ayırmamız gerektiği anlamına gelmez.

## Sonraki test

Yalnız ucuz bir switch testi mantıklı: 30 frequent returner'dan **$5 deposit** alıp beş canlı iade için no-code concierge sun. Kullanıcının Notes, spreadsheet, retailer app veya mevcut tracker'ını gerçekten bırakıp bırakmadığını ölç.

**Stop:** 8'den az deposit, 5'ten az üç-live-return completion veya 4'ten az gerçek tool replacement varsa durdur. Dog Rehab/CardProof testlerinden önce bütçe verilmemeli.

Bu masa başı karar build izni değildir.
