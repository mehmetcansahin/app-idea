# ABD iOS — Tek Gelistiriciyle Rekabet Edilebilir App Fikirleri

**Araştırma tarihi:** 2026-07-16  
**Kapsam:** ABD / US App Store / iPhone-first / solo geliştirici  
**Metodoloji:** v4.0 Quick Compare

## Karar

İlk gerçek davranış testini **Quilt Layout Lock** ile yap. **Resin Calibration Ladder** ikinci, **Laser Scrap Passport** üçüncü test adayıdır. Üçü de masa başında `TESTE_DEGER`, Kanıt Gücü C ve `PREBUILD_PENDING` durumundadır; hiçbiri henüz build izni almamıştır.

Quilt'i ilk sıraya ham skor koymuyor. Resin'in low skoru biraz daha yüksek, fakat Quilt donanım bağımlılığı taşımıyor, v1'de OCR gerektirmiyor, ücretsiz ikame ile ürün arasındaki fark tek gerçek assembly seansında görülebiliyor ve $9.99 depozito testi daha ucuz. Laser ise farklı arketipte olduğu için çıplak skorla karşılaştırılmadı; kataloglama sürtünmesi ve xTool genişleme tehdidi test önceliğini düşürüyor.

## Karsilastirma

| Test sırası | Fikir | Arketip | Low / Base / High | Kanıt | Masa başı karar | Neden burada? |
|---:|---|---|---:|---|---|---|
| 1 | [Quilt Layout Lock](2026-07-16-us-quilt-layout-lock/REPORT.md) | Consumer Utility | 54 / 65 / 65 | C | TESTE_DEGER | En yalın MVP, net kamera anı, düşük test maliyeti |
| 2 | [Resin Calibration Ladder](2026-07-16-us-resin-calibration-ladder/REPORT.md) | Consumer Utility | 56 / 65 / 65 | C | TESTE_DEGER | Problem güçlü; logging sürtünmesi ve free profile ikamesi daha yüksek |
| 3 | [Laser Scrap Passport](2026-07-16-us-laser-scrap-passport/REPORT.md) | B2B/Prosumer | 52 / 60 / 65 | C | TESTE_DEGER | Malzeme tasarrufu ölçülebilir; capture maliyeti ve platform tehdidi yüksek |

Skorlar başarı olasılığı veya güven aralığı değildir. Laser farklı arketip ağırlıkları kullanır; test sırası fatal gate → Kanıt Gücü → skor aralığı → en riskli varsayım/test maliyeti → solo operasyon kısıtlarıyla verildi.

## Kullandigim solo-gelistirici filtresi

Bir fikri kısa listeye almak için şunların birlikte bulunmasını aradım:

1. Problem telefonun bulunduğu fiziksel anda yaşanıyor: kamera, offline kayıt, QR, timer veya hızlı karşılaştırma anlamlı olmalı.
2. İlk sürüm dört core ekran ve üç ana özellikte kalmalı; 6–8 haftalık teknik scope hedefi aşılmamalı.
3. Marketplace, lisanslı geniş content catalog, regüle karar, enterprise entegrasyon, özel donanım kontrolü veya AI doğruluğu çekirdek olmamalı.
4. Kullanıcıya Reddit/Discord/Facebook, kulüp, mağaza, eğitmen veya üretici topluluğu gibi adlandırılmış bir kanaldan erişilebilmeli.
5. Değer gerçek bir görevde gözlenebilmeli ve açık/iade edilebilir ödeme davranışıyla test edilebilmeli.
6. 2025–2026 tarihli exact iOS rakipleri aynı wedge'i dolduruyorsa fikir, yalnız “daha güzel UI” ile tutulmamalı.

## Neden Quilt Layout Lock?

Quilter'lar fiziksel blok sırasını korumak için telefon fotoğrafı, maskeleme bandı, etiket ve pin kullanıyor; ayrı kullanıcılar yön/sıra hatalarını geç fark ettiklerini anlatıyor ([workaround](https://www.reddit.com/r/quilting/comments/1342d91), [geç fark edilen hata](https://www.reddit.com/r/quilting/comments/196bawg), [baş aşağı blok](https://www.reddit.com/r/quilting/comments/1menlku)). Mevcut ücretli ürünler [Quiltography](https://apps.apple.com/us/app/quiltography-quilt-design-made-simple/id585991997), [Quiltler](https://apps.apple.com/us/app/quiltler-quilt-designer/id1120958195) ve [Quiltler 3](https://apps.apple.com/us/app/quiltler-3-quilt-design/id6755831082) dijital design işine odaklanıyor. Kalan dar hipotez, fiziksel assembly sırasında referans overlay + satır checklist'inin normal fotoğraftan daha değerli olmasıdır.

**V1:** Projects, Reference Capture, Row Mode, Compare; manuel grid/yön işareti, yarı saydam overlay, satır checklist. AI/CV yok.

**Killer risk:** Normal fotoğraf ve Post-it yeterli.

**Test:** İki turda toplam sekiz aktif quilter; gerçek assembly görevi; $9.99 iade edilebilir depozito. En az dört depozito ve en az üç gerçek hata önleme/yakalama olmadan devam etme. Bu exploratory eşik geçilse bile ikinci doğal proje döngüsü ve yeniden puanlama gerekir.

## Neden Resin Calibration Ladder ikinci?

[CHITUBOX](https://docs.chitubox.com/en-US/chitubox/latest/configure-print-settings), üretici exposure önerisinin belirli işe uymayabileceğini ve printing test gerekebileceğini açıkça belirtiyor. Kullanıcılar güvenilir ayar ararken resin harcadıklarını, üretici değerinden farklı calibration bulduklarını ve test yorumlamakta zorlandıklarını anlatıyor ([ayar arama](https://www.reddit.com/r/resinprinting/comments/1qvfiph/new_to_resin_printing_trying_to_find_reliable/), [başlangıç noktası](https://www.reddit.com/r/resinprinting/comments/1txg4qa/follow_provided_resin_settings/), [yorumlama](https://www.reddit.com/r/resinprinting/comments/1sxi1qb/validation_test/)).

Wedge slicer veya remote control değil; aynı printer/resin çifti için deneme fotoğrafı + failure taxonomy + A/B karşılaştırma + winning profile geçmişidir. [Resin Control](https://apps.apple.com/us/app/resin-control/id6740918122), [3D Print Log](https://www.3dprintlog.com/) ve community profile'ları önemli ikamelerdir.

**Killer risk:** Kayıt sürtünmesi, ücretsiz profile'dan daha pahalı gelir.

**Test:** On kullanıcı, iki gerçek calibration döngüsü, $14.99 iade edilebilir ön sipariş. Beş ön sipariş + altı iki-döngü tamamlama + dört geçmiş kayda dönüş olmadan devam etme.

## Neden Laser Scrap Passport ucuncu?

Laser kullanıcıları odd-shaped offcut'ları çekmece, yığın, etiket ve harici CAD referanslarıyla yönetiyor ([organizasyon](https://www.reddit.com/r/lasercutting/comments/15z9v06), [lojistik](https://www.reddit.com/r/lasercutting/comments/lsuo9x), [etiketleme](https://www.reddit.com/r/lasercutting/comments/tzwyua)). Fakat küçük scrap'ı değerlendirme emeğinin değerini aşabildiğine dair güncel karşı kanıt da var ([karşı örnek](https://www.reddit.com/r/lasercutting/comments/1t857wa/whats_the_smartest_way_to_turn_small_lasercut/)). [Offcuts](https://apps.apple.com/us/app/offcuts/id1480164923) rectangular stock/cut planning'i, [xTool Smart Nesting](https://support.xtool.com/article/3481) ise belirli cihazlarda fotoğraf-contour akışını kapsıyor.

**V1:** Manuel bounding width/height + material/thickness, shelf/bin QR, gereken dikdörtgene göre scrap eşleştirme. Auto segmentation, SVG nesting veya machine control yok.

**Killer risk:** 20 scrap kaydetmek, kurtarılan materyalden daha pahalıdır; xTool wedge'i kapatır.

**Test:** En az 30 offcut'ı olan sekiz ürün satan solo mikro-işletme; kişi başı 20 kayıt ve üç gerçek iş; $19 iade edilebilir depozito. Dört depozito + beş sürdürülen katalog + dört önlenen yeni sheet olmadan devam etme.

## Park edilen kosullu fikirler

| Fikir | Neden park? | Yeniden açma koşulu |
|---|---|---|
| Astronomical League Program Logger | Program content/marka izni ve [SkySafari](https://apps.apple.com/us/app/skysafari-7-plus/id1567654881) tehdidi | Bir program koordinatöründen yazılı pilot/izin |
| POTA Rove Planner | [POTAontheGO](https://apps.apple.com/us/app/potaonthego-pota-ham-radio/id6761618786) çoklu park alanına girdi; data/trespass riski | Üç kulüpten rove pilotu ve resmî data kullanım yolu |
| FitReplay | [Dart](https://dartsewing.com/) fitting-session alanına, [Pattern Projects](https://apps.apple.com/us/app/pattern-projects-sew-knit/id6754258425) alteration notlarına girdi | Bir fitting eğitmeninin ücretli cohort pilotu |
| Stained Glass Remnant Match | [Molten](https://apps.apple.com/us/app/molten-glass/id6754231339) inventory, location ve QR'ı kapsıyor | Molten kullanıcılarından tekrarlanan geometry-match eksikliği |

## Bilerek eledigim kalabalik alanlar

Güncel exact veya çok yakın iOS ürünleri nedeniyle şu alanlara girmem: candle burn-test lab; pottery/kiln/glaze log; fly-tying inventory/pattern; fountain-pen ink tracker; miniature-paint inventory/recipe; craft-fair booth analytics; needlepoint/thread stash; picture-frame calculator; generic laser settings; generic cut-list optimizer; darkroom film development; RC setup/LiPo log; watch collection/accuracy; antique-booth inventory; leathercraft hide inventory; bonsai/coral tracker; beekeeping logger; metal-detecting map/permission log; sailing log; archery scorer; equestrian course walk; model-rocketry log; dog-agility video tagger.

Bu eleme “pazar yok” demek değildir. Sonuç daha dardır: 2025–2026 rakipleri aynı mobile-native işi zaten yaptığı için solo geliştiricinin yalnız UI kalitesiyle savunabileceği bir wedge görülmedi.

## Sonraki karar kapisi

Üç testi paralel çalıştırma. Önce Quilt testini yap; başarısız olursa Resin'e geç. Quilt testi geçerse ikinci doğal quilt döngüsünde tekrar kullanım ve daha güçlü ödeme kanıtı topla, sonra skorları yeniden hesapla. v4.0'a göre `BUILD_SMALL` için low skorun en az 60, genel/top-risk kanıtın B+ ve en az bir ürün-spesifik E3+ davranış gerekir; mevcut üç paket bu koşulları karşılamıyor.

## Kanit sinirlari

App Store fiyat/rating verileri revenue veya retention değildir. Community kaynakları self-selected'dır. “Exact rakip bulunamadı” zayıf karşı kanıttır, yokluk kanıtı değildir. Test eşikleri baseline ve MDE olmadığı için exploratory/directional'dır; nüfus oranı üretmez. Sonuç “tutacak app” garantisi değil, en ucuz şekilde yanlışlanabilecek üç rekabet hipotezidir.
