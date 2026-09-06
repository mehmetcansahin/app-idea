# US Resin Calibration Ladder — Quick Scan

**Tarih:** 2026-07-16  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** Consumer Utility  
**Risk modifier:** Hardware dependency  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

**Resin Calibration Ladder** ikinci test adayıdır. Slicer veya printer remote-control ürünü değildir; bir printer + resin + sıcaklık kombinasyonu için calibration denemelerini fotoğraf, ayar ve failure tag'leriyle karşılaştırmalı bir deney günlüğüne dönüştürür.

Problem teknik olarak gerçektir: üretici ayarı her işte doğru sonuç vermeyebilir ve kullanıcılar birden fazla exposure testi yapar. Mobil an da nettir; basılı test parçası printer'ın yanında incelenir. Ancak ücretsiz community profile'ları ve genel print log'ları güçlü ikamedir. Kullanıcının her denemeyi kaydetme sürtünmesi, ürünün en büyük riski olabilir.

## Kullanici, an ve JTBD

- Segment: Evde resin 3D printer kullanan ve yeni resin, sıcaklık veya layer height için exposure calibration yapan ABD'li iPhone sahibi maker.
- Tetikleyici: Yeni resin/printer profili, ortam sıcaklığı değişimi veya detay/adhesion sorunu.
- Mevcut iş: Üretici/community ayarından başlamak, birden fazla test basmak, slicer screenshot'u ve fotoğrafları dağınık tutmak.
- İstenen sonuç: Hangi denemenin neden daha iyi olduğunu hatırlayıp kazanmış profili tekrar kullanmak.
- Mobile-native an: Test parçasının printer yanında fotoğrafı, hızlı failure tag'i ve önceki denemeyle A/B karşılaştırma.

## Dogrudan gozlemler

- CHITUBOX dokümanı exposure'ın adhesion ve detail'i etkilediğini, birçok faktöre bağlı olduğunu ve üretici önerisinin belirli bir işe uygun olmayabileceğini belirtiyor ([resin-demand-chitubox], [kaynak](https://docs.chitubox.com/en-US/chitubox/latest/configure-print-settings)).
- Kullanıcılar güvenilir ayarı bulurken resin harcadıklarını ve sonuçları yorumlamakta zorlandıklarını bildiriyor ([resin-demand-reliable], [kaynak](https://www.reddit.com/r/resinprinting/comments/1qvfiph/new_to_resin_printing_trying_to_find_reliable/)).
- Bir tartışmada üretici ayarının yalnız başlangıç noktası olduğu ve gerçek calibration sonucunun belirgin biçimde farklı çıkabildiği anlatılıyor ([resin-demand-startpoint], [kaynak](https://www.reddit.com/r/resinprinting/comments/1txg4qa/follow_provided_resin_settings/)).
- Bir kullanıcı validation test sonucunu nasıl yorumlayacağını bilmediğini soruyor; yanıtlar ladder/RERF gibi karşılaştırmalı testleri öneriyor ([resin-usability-interpretation], [kaynak](https://www.reddit.com/r/resinprinting/comments/1sxi1qb/validation_test/)).
- [Resin Control](https://apps.apple.com/us/app/resin-control/id6740918122) gibi iOS araçları printer monitoring/control alanını, [3D Print Log](https://www.3dprintlog.com/) ve [Gyroid](https://gyroid.app/) ise genel print kayıt alanını kapsıyor ([resin-economics-control], [resin-wedge-printlog]).

## Cikarim

Problem kanıtı, calibration ihtiyacını destekler; bu uygulamanın satın alınacağını desteklemez. Dar wedge “doğru ayarı otomatik söylemek” değil, kullanıcının kendi denemelerini karşılaştırmasını ve kazanan profilin bağlamını korumasını sağlamaktır. İlk sürüm sonuç doğruluğu veya print safety garantisi veremez.

## Rakip ve ikameler

| Urun / ikame | Gozlenen is | Bu fikir icin anlamı |
|---|---|---|
| CHITUBOX / Lychee | Slicing, profile ve calibration guidance | Kullanıcı zaten desktop ekosisteminde |
| Resin Control | iOS monitoring/control | Teknik ve platform uygulanabilirliği; exact loop değil |
| 3D Print Log / Gyroid | Genel print ve resin log | Veri saklama ihtiyacını kısmen çözüyor |
| Community profiles | Hazır başlangıç ayarları | Ücretsiz güçlü ikame |
| Photos + Notes | Screenshot ve test fotoğrafı | Sıfır fiyat, düşük yapı |

### Arama protokolu

`resin exposure calibration tracker app`, `resin printer calibration experiment log iOS` ve US App Store odaklı sorgularda monitoring, slicer ve genel log ürünleri bulundu; fotoğraf + failure taxonomy + A/B calibration loop'una odaklanan exact iOS ürün bulunamadı ([resin-wedge-search]). Bu sonuç eksiksiz pazar sayımı değildir.

## Solo MVP siniri

**Dört core ekran:** Printer/Resin Pairs, Experiment Capture, Ladder Compare, Winning Profile.

**Üç ana özellik:**

1. Ayarları manuel girme veya slicer screenshot'undan kullanıcı onaylı capture.
2. Calibration fotoğrafı ve sınırlı failure tag seti.
3. İki denemeyi yan yana karşılaştırma ve kazanan profili export etme.

İlk sürümde printer kontrolü, cloud profile marketplace, otomatik “doğru exposure” kararı, genel print inventory veya geniş slicer yoktur. OCR ilk teknik spike'ta güvenilir değilse manuel alanlara düşürülür. Bu scope 6–8 haftalık solo iOS MVP'sine uygundur; donanımla entegrasyon yapılmaz.

**Fiyat hipotezi:** $14.99 lifetime veya $9.99/yıl. Liste fiyatı hipotezdir.

## Skor

| Boyut | Low | Base | High | Gerekce |
|---|---:|---:|---:|---|
| Problem / talep | 3 | 4 | 4 | Resmî doküman + bağımsız calibration davranışları |
| Monetizasyon | 2 | 3 | 3 | Komşu araç fiyatları var; ürün-spesifik ödeme yok |
| Rekabet / wedge | 3 | 3 | 3 | Dar deney loop'u var; prototip tercihi henüz yok |
| Dağıtım | 3 | 3 | 3 | Maker ve printer brand kanalları erişilebilir; traction/CAC yok |
| Tekrar değeri | 2 | 3 | 3 | Resin/ısı/profil değişiminde doğal tekrar hipotezi |
| Zamanlama | 3 | 3 | 3 | Aktif tool ekosistemi; yapısal pencere kanıtı yok |

**Fırsat Çekiciliği:** **56 / 65 / 65 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear — kullanıcı kendi ayar ve fotoğraflarını kaydeder; vendor profile veritabanı kopyalanmaz.
- Core feasibility: clear — manuel capture ve fotoğraf karşılaştırma standart iOS işidir; OCR fallback'i vardır.
- Platform: clear — resin-printer companion uygulamaları US App Store'da yayınlanıyor.
- Safety/ethics: clear — ürün ayar önermez veya printer'ı kontrol etmez; kullanıcı onayı ve üretici güvenlik talimatları esas alınır.

## Sonraki gercek davranis testi

Yeni resin veya profil kalibrasyonu yapacak on kullanıcıyı iki gerçek calibration döngüsünde concierge prototiple takip et. Fotoğraf ve ayarları manuel olarak karşılaştırma kartına dönüştür; ikinci döngüde eski kayda geri dönüp dönmediklerini gözle. Ürünün hazır olmadığı ve iade koşulları açıkça belirtilerek **$14.99 iade edilebilir ön sipariş** teklif et.

Exploratory ilerleme eşiği: en az beş ön sipariş, en az altı kişinin iki calibration döngüsünü tamamlaması ve en az dört kişinin geçmiş karşılaştırmayı kazanan profili seçmek veya yeniden kullanmak için açması. Eşiklerden biri kalırsa dur; geçerse capture sürtünmesini azaltan ikinci test ve yeniden puanlama yap. Bu eşikler baseline/MDE olmadan population sonucu veya build izni üretmez.

## Kanit sinirlari

Community örnekleri self-selected'dır. CHITUBOX dokümanı calibration ihtiyacını açıklar fakat app talebini ölçmez. Rakip liste fiyatları ve rating'leri gerçekleşmiş ödeme/retention değildir. Printer/resin kombinasyonlarının çeşitliliği ve kayıt sürtünmesi yalnız insan testiyle ölçülebilir.
