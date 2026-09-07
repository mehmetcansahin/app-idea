# US Mobile Notary Scanback Gate — Quick Scan v4.0

## Karar

**BELIRSIZ · DESK_RESEARCH_COMPLETE**

Problem gerçek; fakat SigningOS aynı AI scanback kontrolünü sunuyor ve gerçek kredi paketinin
üçüncü taraf uygulamada işlenmesine izin verilip verilmeyeceği bilinmiyor. Kullanıcı testi
öncesi **title/signing-service veri-işleme izni** çözülmelidir. Build izni yoktur.

## Araştırma kontratı

- Geo/storefront/platform: ABD / US App Store / iOS-first
- Segment: son 60 günde 10+ scanback-required iş yapan mobile notary/loan signing agent
- Arketip: `b2b_prosumer`
- Risk modifier'ları: `regulated`, `sensitive_data`, `ai_variable_cost`, `platform_dependency`
- Kullanım anı: imzalama sonrası, FedEx/UPS drop öncesi PDF completeness/QC
- İkame: SigningOS, Snapdocs, NotaryGadget, NotaryAssist, Notary Tracker, manuel checklist

## Gözlenen sinyaller

- California SOS'nin 10 Temmuz 2026 aktif listesinde 137.134 commission bulunuyor; tek eyalet
  ve tüm notary'lerdir, mobile/signing-agent alt kümesi değildir. [Liste](https://www.sos.ca.gov/notary/notary-public-listing),
  [ZIP](https://notary.cdn.sos.ca.gov/export/active-notary.zip)
- [Snapdocs](https://www.snapdocs.com/notaries) ayda 60 bin signing-agent işi bildiriyor;
  vendor self-report'tur. [Scanback rehberi](https://support.snapdocs.com/scanbacks-are-required)
  gereksinimin sipariş veya özel talimatta bulunabildiğini gösteriyor.
- [NNA 2026](https://www.nationalnotary.org/notary-bulletin/blog/2026/03/common-mistakes-new-notary-signing-agents-make-and-how-to-fix-them)
  kaçırılmış signature/date'in gecikme veya re-sign doğurabildiğini anlatıyor; frekans yoktur.

## Top 5 rakip/ikame

| Ürün | Resmi liste fiyatı | Kapsam |
|---|---:|---|
| [SigningOS](https://signingos.app/pricing) | Elite $19,99/ay veya $159,99/yıl | Checklist, mileage, AI missing signature/initial/date |
| [Snapdocs](https://support.snapdocs.com/snapdocs-cost) | Agent için $0 | Order, document transfer, scanback, calendar |
| [NotaryGadget](https://www.notarygadget.com/Pricing) | İlk 15 signing free; $11,95/ay | Appointment, scanback status, mileage, invoice |
| [NotaryAssist](https://notaryassist.com/) | $8,99/ay veya $95/yıl | Calendar, mileage, package/barcode tracking |
| [Notary Tracker](https://notarytracker.com/) | Ücretsiz indirme | Appointment, mileage, expenses, journal |

[SigningOS App Store](https://apps.apple.com/us/app/signingos/id6761114943) sayfası 21 Nisan
2026 çıkışlı ve 1 rating'li exact rakip gösteriyor. Traction kanıtı zayıf olsa da önerilen
özelliğin yeni olmadığını kanıtlıyor.

## Dar ürün hipotezi

**Zero-retention Scanback Gate:** iOS Share Sheet ile PDF al; sayfa bütünlüğü ve boş
signature/initial/date/stamp adaylarını yalnız clerical review olarak işaretle; ham belgeyi
otomatik sil. Rota, takvim, muhasebe, notarial-act tavsiyesi ve kredi değerlendirmesi yok.

## v4.0 değerlendirme

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem/talep | 2 | 3 | 4 | Scanback ve hata maliyeti sinyali var; frekans denominator'u yok |
| Monetizasyon/ekonomi | 1 | 2 | 3 | Yalnız rakip fiyatı/vendor job metriği |
| Rekabet/wedge | 1 | 1 | 2 | SigningOS birebir; on-device/no-retention izin ve tercih kanıtı yok |
| Dağıtım erişimi | 1 | 2 | 3 | NNA/community/service kanalları var; sponsor erişimi belirsiz |
| Tekrarlanan değer | 2 | 3 | 3 | Aktif agent için iş-bazlı döngü; ürün retention'ı yok |
| Zamanlama | 2 | 2 | 3 | Yeni exact rakip var; yapısal pencere kanıtlanmadı |

**Fırsat Çekiciliği: 29 / 45 / 62 · borderline · Kanıt Gücü: D.**

## Fatal gate ve izin sorunu

`LEGAL_BLOCKED` ve `PLATFORM_BLOCKED` **unknown**. Kredi paketleri hassas finansal bilgi taşır;
[NNA background screening](https://www.nationalnotary.org/knowledge-center/signing-agent-resources/background-screenings)
agent'ların özel güven gereksinimini gösterir fakat üçüncü taraf app izni vermez.
[Apple 5.1](https://developer.apple.com/app-store/review/guidelines/) hassas bilgi isteyen app'in
legal entity tarafından sunulmasını ve üçüncü taraf AI paylaşımında açık izin istemeyi
gerektirebilir. `CORE` clear; `SAFETY` yalnız clerical QC kapsamında clear.
[California handbook](https://notary.cdn.sos.ca.gov/forms/notary-handbook-2025.pdf) kapsamında
notarial act veya kredi şartı tavsiyesi verilmemelidir.

## Sonraki RAT

5 title/signing service ile zero-retention/on-device veri-işleme RAT'i yap. En az 2 yazılı
pilot izni çıkmazsa dur. İzin çıkarsa sanitized paket ve izinli gerçek işlerle 8 agent'a bir
aylık **$29 peşin** pilot sat; 4 ödeme, 3 ikinci doğal kullanım, medyan <5 dakika ve sıfır
ham-belge retention iste. Herhangi bir hiring-party yasağında dur.

## Kanıt ve sınırlamalar

Exact commercial mobile-notary sayısı, scanback-required pay ve hata frekansı yapısal olarak
gözlenemiyor. Vendor işleri/fiyatları bu ürüne ödeme değildir. İzin claim'i D olduğundan masa
başı kararı ilerlemeye yetmez. Ayrıntılar: [kanıt defteri](data/evidence-ledger.md).

## Kapatma dispozisyonu — 2026-09-07

Bu fikre Faz 5.5 sözleşmesi yazılmadı. Gerekçe kanıt yapısında:

| Engel | Kayıt | Masa başında kapanır mı |
|---|---|---|
| `claim-permission` = D | `notary-permission-nna` (E1, `structurally_unobservable`) + `notary-platform-apple` (E2, neutral) | **Hayır.** Karar mercii hiring party; cevap yalnız yazılı pilot izniyle alınır. Doküman taraması bu izni üretemez |
| `claim-wedge` = D | `notary-wedge-signingos` (E2, contradicts) | Hayır. SigningOS birebir aynı AI scanback kontrolünü listeliyor; wedge ancak tercih davranışıyla kurtulur |
| Skor tavanı | `opportunity` 29 / 45 / 62 | İlgisiz; portföyün en zayıf tavanı |

Sıradaki tek anlamlı hamle bir deney değil, bir **erişim testi**dir: 5 title/signing
service'ten zero-retention/on-device işleme için yazılı pilot izni istemek. İki yazılı
izin çıkmadan prototip, kullanıcı testi veya fiyat testi yapılmaz. İzin çıkarsa fikir
yeniden puanlanır ve o zaman sözleşme yazılır.

Bu bir `ELENDIR` değildir: `opportunity.high = 62`, yani eleme kuralı (`high < 40`)
karşılanmıyor ve hiçbir fatal gate `blocked` değil. Karar `BELIRSIZ` olarak kalır,
aktif backlog dışıdır.
