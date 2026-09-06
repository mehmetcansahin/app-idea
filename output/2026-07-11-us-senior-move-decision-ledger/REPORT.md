# US Senior Move Decision Ledger — Quick Scan v4.0

## Karar

**TESTE_DEGER · PREBUILD_PENDING**

Genel bir inventory veya organizer CRM'i değil; yaşlı müşterinin son sözünü koruyan
**karar yetkisi, aile onayı ve vendor teslim zinciri** test edilmeye değer. Build izni yoktur.

## Araştırma kontratı

- Geo/storefront/platform: ABD / US App Store / iOS-first
- Segment: bağımsız senior move manager ve professional organizer
- Arketip: `b2b_prosumer`
- Risk modifier'ları: `sensitive_data`, `platform_dependency`
- Kullanım anı: evde eşya yakalama → uzaktaki aile onayı → kapıda vendor manifest/teslim
- İkame: DriveSales, Scanlily, Pro Organizer Toolkit, Sortly, Trello ve spreadsheet

## Gözlenen sinyaller

- [NASMM](https://www.nasmm.org/become-a-move-manager/join-nasmm/vendor-membership-info/industry-partner-membership/)
  North America'da 1.000+ üye; [NAPO](https://www.napo.net/page/professional) ise 3.500+
  organizer/productivity consultant bildiriyor. Bunlar ABD şirket sayısı değildir.
- [NASMM workflow'u](https://www.nasmm.org/faqs/) sorting, downsizing, sale/donation/storage,
  mover koordinasyonu ve pack/unpack boyunca çok taraflı karar ve handoff içeriyor.
- ABD'de 65+ nüfus 2024'te 61,2 milyon ve nüfusun %18'i; bu yalnız talep-popülasyon
  proxy'sidir, uygulama ödeme davranışı değildir. [U.S. Census](https://www.census.gov/newsroom/press-releases/2025/older-adults-outnumber-children.html)

## Top 5 rakip/ikame

| Ürün | Resmi liste fiyatı | Bu fikirle çakışma |
|---|---:|---|
| [DriveSales](https://drivesales.com/pricing) | Ops $299/ay; AI survey $120/kullanıcı/ay | Senior-move CRM, inventory, portal, disposition |
| [Scanlily](https://www.scanlily.com/en/pricing) | Pro $9/ay; Ultra $35/ay | Foto envanteri ve aile paylaşımı |
| [Pro Organizer Toolkit](https://apps.apple.com/us/app/pro-organizer-toolkit/id6759227781) | $19,99/yıl veya $29,99 lifetime | iPhone/iPad client-room-disposition akışı |
| [Sortly](https://www.sortly.com/pricing/) | $24/ay yıllık ilk yıl; aylık $49 | Genel mobil envanter |
| [Trello](https://trello.com/en/pricing?lang=en) | $5/user/ay yıllık | Aile onayı ve vendor task-board ikamesi |

Bu nedenle inventory tek başına wedge değildir. [Scanlily App Store](https://apps.apple.com/us/app/scanlily-organize-with-ai/id1627766472)
sayfasındaki tek organizer örneği büyük müşteri taşınmalarında kullanım gösteriyor; listing'in
26 rating'i ve tek yorum pazar prevalansı değildir.

## Dar ürün hipotezi

1. Oda/eşya fotoğrafı ve `keep / family / donate / sell / storage` kararı.
2. Her karar için yetkili kişi, consent ve yaşlı müşterinin final approval'ı.
3. Aileye uygulama kurdurmayan sınırlı onay linki.
4. Vendor pickup için QR/PDF manifest, teslim alan ve timestamp.
5. Değişiklik ile teslim geçmişi; appraisal, capacity veya mülkiyet kararı yok.

## v4.0 değerlendirme

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem/talep | 2 | 3 | 4 | Çok taraflı ve eşya-bazlı workflow var; kişi başı yıllık proje frekansı yok |
| Monetizasyon/ekonomi | 1 | 2 | 3 | Yalnız rakip fiyatları ve association proxy'leri |
| Rekabet/wedge | 1 | 2 | 3 | Generic inventory kalabalık; decision-rights ve chain-of-custody test edilmedi |
| Dağıtım erişimi | 2 | 3 | 3 | NASMM/NAPO erişilebilir; traction ve CAC yok |
| Tekrarlanan değer | 2 | 3 | 3 | Proje içinde tekrar güçlü, projeler arası retention bilinmiyor |
| Zamanlama | 2 | 3 | 3 | Yaşlanan nüfus destekleyici, ürün-spesifik göç yok |

**Fırsat Çekiciliği: 32 / 52 / 65 · borderline · Kanıt Gücü: C.**

## Gate ve guardrail'ler

Dört fatal gate bu dar kapsamda `clear`. [NASMM etik kodu](https://www.nasmm.org/about/about/ethics/)
asıl müşterinin geçiş yapan kişi olduğunu ve self-determination'ın korunmasını gerektiriyor.
Ürün capacity, appraisal, hukuki sahiplik veya disposal kararı vermemeli; adres, değerli eşya
ve ev fotoğrafları için encryption, least privilege, export/delete ve açık consent kullanmalıdır.
[Apple kuralları](https://developer.apple.com/app-store/review/guidelines/) izlenmelidir.

## Sonraki gerçek davranış testi

8 NASMM/NAPO profesyonelinin son işini gözlemle; ardından bir canlı taşınmada ledger'ı
concierge olarak yürüt. İlk örnekten sonra sonraki üç proje için **$99 peşin** iste.
İlerleme şartı: en az 4 ödeme, 3 tamamlanmış canlı proje ve en az 2 doğal sonraki projede
tekrar. Aksi durumda generic inventory/CRM yönünü ele.

## Kanıt ve sınırlamalar

Exact ABD senior-move-manager sayısı ve profesyonel başına yıllık proje frekansı yapısal
olarak gözlenemiyor. Association üyeliği pazarın tamamı değildir; rakip liste fiyatı bu
ürüne ödeme kanıtı değildir. Ayrıntılar: [kanıt defteri](data/evidence-ledger.md).
