# US Laser Scrap Passport — Quick Scan

**Tarih:** 2026-07-16  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** B2B/Prosumer  
**Risk modifier:** Hardware dependency  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

**Laser Scrap Passport** üçüncü test adayıdır. CAD veya nesting yazılımı değildir; laser cutter'dan çıkan fiziksel offcut'ı fotoğraf, yaklaşık bounding rectangle, materyal/kalınlık ve raf/bin QR'ıyla tekrar bulunabilir bir “scrap passport”a dönüştürür.

Sorun davranışsal olarak görünür: kullanıcılar düzensiz parçaları yığın, çekmece, label ve ayrı CAD referanslarıyla yönetiyor. Buna karşı iki güçlü risk var: kataloglama maliyeti kurtarılan malzemeden pahalı olabilir ve xTool gibi donanım üreticileri kamera tabanlı contour/nesting özelliklerini genişletiyor. Bu nedenle fikir dar manuel MVP ve gerçek malzeme tasarrufu testi dışında büyütülmemeli.

## Kullanici, an ve JTBD

- Segment: Ürün satan, düzenli laser cutting yapan ve en az 30 kullanılabilir offcut tutan ABD'li solo mikro-işletme sahibi.
- Tetikleyici: İş bittiğinde offcut'ı kaldırmak veya yeni bir parça için uygun scrap aramak.
- Mevcut iş: Boyuta göre yığın/çekmece, marker etiketi, tekrar ölçüm veya doğrudan yeni sheet kullanmak.
- İstenen sonuç: Gerekli dikdörtgeni alabilecek doğru materyal ve kalınlıktaki scrap'ı rafta hızla bulmak.
- Mobile-native an: Makine yanında capture, rafta QR scan ve iş öncesi ihtiyaç ölçüsü arama.

## Dogrudan gozlemler

- Kullanıcılar odd-shaped parçaların saklanması ve gözle taranmasının zor olduğunu; çekmece, boyut yığını ve duvar depolaması kullandıklarını anlatıyor ([laser-demand-odd-shapes], [kaynak](https://www.reddit.com/r/lasercutting/comments/15z9v06)).
- Bir kullanıcı rastgele malzeme ve yarı kullanılmış scrap yığınını lojistik kabus olarak tanımlıyor; yorumlarda etiket, Illustrator dosyası ve fiziksel yığınlar görülüyor ([laser-demand-logistics], [kaynak](https://www.reddit.com/r/lasercutting/comments/lsuo9x)).
- Başka bir tartışmada kullanıcılar sheet ve scrap'ı etiketliyor ve CAD referansı tutuyor ([laser-demand-labels], [kaynak](https://www.reddit.com/r/lasercutting/comments/tzwyua)).
- 2026 tarihli karşı kanıt, çok küçük offcut'ları değerlendirmek için harcanan emeğin bazen değerinden yüksek olduğunu ve yeni sheet çekmenin daha kolay olabildiğini gösteriyor ([laser-usability-counter], [kaynak](https://www.reddit.com/r/lasercutting/comments/1t857wa/whats_the_smartest_way_to_turn_small_lasercut/)).
- [Offcuts](https://apps.apple.com/us/app/offcuts/id1480164923) sheet/lumber envanteri ve rectangular cut planning için ücretli unlock sunuyor; düzensiz fiziksel scrap'ı rafta bulma loop'u değildir ([laser-economics-offcuts], [laser-wedge-offcuts]).
- xTool'un resmî Smart Nesting özelliği fotoğraftan contour yakalamayı yalnız belirli cihazlarda destekliyor; bu hem teknik precedent hem de platform sahibinin genişleme tehdididir ([laser-timing-xtool], [kaynak](https://support.xtool.com/article/3481)).

## Cikarim

Scrap yönetimi problemi gerçek olabilir; ancak app'in sürdürülebilir değeri ancak kullanıcı kaydı sürdürür ve gerçek işlerde yeni sheet kullanımını önlerse oluşur. “Fotoğraftan her düzensiz şekli otomatik ölç ve SVG nest et” vaadi solo v1'i teknik olarak şişirir ve xTool/LightBurn ile doğrudan rekabete sokar.

## Rakip ve ikameler

| Urun / ikame | Gozlenen is | Bu fikir icin anlamı |
|---|---|---|
| Offcuts | Rectangular sheet/lumber inventory ve cut plan | Ücretli komşu ürün; odd scrap retrieval değil |
| xTool Smart Nesting | Belirli cihazlarda kamera contour/nesting | En büyük platform genişleme riski |
| LightBurn | $99/$199 desktop laser workflow | Kullanıcı bütçesi var; CAD alanına girilmemeli |
| Deepnest | Ücretsiz desktop nesting | Shape packing ücretsiz ikame |
| Etiket + çekmece + yığın | Fiziksel organizasyon | Sıfır fiyat ve düşük capture maliyeti |

### Arama protokolu

`laser scrap inventory app`, `laser offcut photo QR inventory`, `odd shaped scrap finder iOS` ve US App Store sorgularında rectangular stock/cut-list, CAD/nesting ve machine-camera çözümleri bulundu; manuel bounding box + shelf QR + physical retrieval loop'una odaklanan exact iPhone ürünü bulunamadı ([laser-wedge-search]). Bu, rakip olmadığı anlamına gelmez.

## Solo MVP siniri

**Dört core ekran:** Capture, Scrap Inventory, Needed Shape, Matches.

**Üç ana özellik:**

1. Fotoğraf + kullanıcı girdiği bounding width/height, materyal ve kalınlık.
2. Raf/bin QR etiketi ve hızlı konum güncelleme.
3. Gerekli dikdörtgene göre uygun scrap eşleştirme.

İlk sürümde irregular auto-segmentation, SVG nesting, machine control, kamera kalibrasyonu, marketplace veya ekip workflow'u yoktur. Manuel scope 6–8 haftalık solo MVP'ye uygundur; hardware dependency yalnız kullanım bağlamıdır.

**Fiyat hipotezi:** $14.99–$24.99 lifetime. Small-business tier ancak gerçek tekrar ve tasarruf sonrası düşünülür.

## Skor

| Boyut | Low | Base | High | Gerekce |
|---|---:|---:|---:|---|
| Problem / talep | 3 | 3 | 4 | Birden fazla manuel organizasyon davranışı; maliyet bilinmiyor |
| Monetizasyon | 2 | 3 | 3 | Komşu paid tools var; ürün-spesifik ödeme yok |
| Rekabet / wedge | 2 | 3 | 3 | Dar retrieval wedge'i var; prototip tercihi yok |
| Dağıtım | 3 | 3 | 3 | Laser toplulukları/makerspace erişilebilir; traction/CAC yok |
| Tekrar değeri | 3 | 3 | 3 | Her işte capture/search için doğal döngü hipotezi |
| Zamanlama | 3 | 3 | 3 | Kamera özellikleri ilerliyor; yapısal avantaj kanıtı yok |

**Fırsat Çekiciliği:** **52 / 60 / 65 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear — kullanıcı kendi materyal kayıtlarını tutar; vendor material database kopyalanmaz.
- Core feasibility: clear — manuel ölçü, fotoğraf, local DB ve QR standart iOS yetenekleridir.
- Platform: clear — benzer inventory/cut-planning uygulaması US App Store'da yayınlanıyor.
- Safety/ethics: clear — ürün machine safety, cut setting veya yangın güvenliği tavsiyesi vermez.

## Sonraki gercek davranis testi

En az 30 offcut'ı olan sekiz maker/atölye seç. Her biri için concierge olarak 20 scrap kaydet; üç gerçek iş boyunca Needed Shape araması yaptır. Ürün hazır değil ve iade koşulları açık denerek **$19 iade edilebilir depozito** teklif et.

Exploratory ilerleme eşiği: en az dört depozito, en az beş katılımcının üç iş sonunda 15+ güncel kayıt tutması ve en az dört katılımcının sistem üzerinden bulunan scrap ile yeni sheet kullanımını önlemesi. Eşiklerden biri kalırsa dur. Geçerse capture süresini ve iki doğal döngüde retention'ı ölçen ikinci test yap; sonuç doğrudan build izni değildir.

## Kanit sinirlari

Reddit örnekleri self-selected'dır ve parasal kaybı ölçmez. App Store ve desktop yazılım fiyatları ürün-spesifik ödeme davranışı değildir. xTool desteği cihazlara göre değişir. Manuel kataloglamanın gerçek maliyeti ve material savings first-party pilot olmadan bilinemez.
