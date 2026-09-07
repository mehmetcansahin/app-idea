# US RoomCheck — Quick Scan

**Tarih:** 2026-07-18  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** Consumer Utility  
**Risk modifier:** Sensitive data, platform dependency  
**Metodoloji:** v4.0  
**Karar:** **BELIRSIZ**  
**Durum:** **DESK_RESEARCH_COMPLETE**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

“Hidden camera” keyword'ünde gerçek kullanıcı ilgisi ve ödeme mimarisi var. Fakat iPhone ile **odadaki her kamerayı bulma** vaadi teknik olarak doğrulanabilir değildir. Bu nedenle önerilen ürün detector klonu değil, **RoomCheck: beş dakikalık açıklanabilir oda gizlilik kontrolü**dür.

RoomCheck her sinyali `normal`, `incelemeye değer` veya `yetersiz veri` olarak gösterir. “Kamera bulundu” demez; ağda görünmeyen, reklam yapmayan, izole veya kablolu cihazların kaçabileceğini açıkça anlatır. Core feasibility gate'i kontrollü corpus test edilene kadar `unknown`; masa başı kararı bu yüzden `BELIRSIZ`dir.

## Hidden camera recorder neden elendi

Gizli veya background kayıt yapan uygulama bu raporun adayı değildir. [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) kayıt için açık kullanıcı onayı ve görünür/işitilebilir gösterge ister; [AVFoundation](https://developer.apple.com/documentation/avfoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground) kamera cihazının background'da kullanılamadığı kesinti durumunu belgeler. [Reporters Committee for Freedom of the Press'in eyalet rehberi](https://www.rcfp.org/introduction-to-reporters-recording-guide/) ABD'de kayıt/onay kurallarının eyalet ve bağlama göre değiştiğini gösterir. Tek kişinin taşıması gerekmeyen platform, güven ve hukuk riski yaratır.

RoomCheck hiçbir üçüncü kişiyi gizlice kaydetmez; yalnız kullanıcının odayı incelemesine yardım eder ([room-app-review], [room-scope-boundary]).

## Kullanici, an ve yapilacak is

- Segment: Otel, short-term rental, soyunma/tedavi alanı veya yeni mekânda mahremiyet kontrolü yapmak isteyen ABD'li iPhone kullanıcısı.
- Tetikleyici: Odaya ilk giriş, beklenmedik cihaz/ışık veya yüksek mahremiyet ihtiyacı.
- Mevcut ikameler: Gözle kontrol listesi, Wi-Fi router ekranı, flashlight/lens taraması, detector app'i veya fiziksel RF cihazı.
- İstenen sonuç: Ne görüldüğünü, neden şüpheli olabileceğini ve neyin görünemediğini anlayarak bir sonraki güvenli adımı seçmek.

## Dogrudan gozlemler

- [Hidden Spy Camera Finder Pro](https://apps.apple.com/us/app/hidden-spy-camera-finder-pro/id1560989782) yaklaşık 12K rating, 4.4 ve $2.99/hafta, $5.99/ay, $14.99/yıl seçenekleri gösterdi ([room-finder-leader], [room-finder-pricing]).
- [Hidden Camera Scanner Detector](https://apps.apple.com/us/app/hidden-camera-scanner-detector/id1468725639) yaklaşık 2.3K rating; [Hidden Camera DETECTOR — WLAN](https://apps.apple.com/us/app/hidden-camera-detector-wlan/id1645273817) yaklaşık 1.9K rating gösterdi. Kategori birden fazla ürünle yüksek-niyetli keyword rekabetine sahip ([room-second-competitor], [room-third-competitor]).
- Lider listing'deki görünür yorumlarda bilinen test kamerasını bulamayan lens modu, boş/stale ağ sonuçları ve açıklanamayan çıktılar vardı ([room-finder-test-failure]). Quick Scan yorumları random/stratified değildir; tema oranı çıkarılmaz.
- Apple [TN3111](https://developer.apple.com/documentation/technotes/tn3111-ios-wifi-api-overview) genel amaçlı tüm yakın Wi-Fi ağları/kameraları tarama API'si olmadığını; [TN3179](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy) yerel ağ izni ve service-discovery sınırlarını; [Core Bluetooth](https://developer.apple.com/documentation/corebluetooth/) ise yalnız reklam yapan BLE cihazlarının görünürlüğünü belgeliyor ([room-tn3111-limit], [room-tn3179-limit], [room-bluetooth-limit]).

Bu resmî sınırlar “görünmedi = kamera yok” sonucunu geçersiz kılar. Görülebilen sinyallerin kullanıcıya yararlı bir `inspect further` uyarısı üretip üretemediği ise masa başında bilinmiyor.

## Cikarim ve wedge

Yeni ürünün fırsatı daha çok alarm üretmek değil, kategorinin güven açığını çözmektir:

1. Oda tipine göre kontrol noktaları: duman alarmı, saat, USB adaptörü, priz, TV çevresi.
2. Kullanıcı izin verirse yalnız görünür local-network ve BLE sinyalleri.
3. Lens yansıması için yönlendirmeli, kalibre edilmiş kamera görünümü.
4. Her sonucun “neden normal / neden incele / neden yetersiz” açıklaması.
5. Güvenli cihaz etiketleme ve iki tarama arasındaki değişiklik.
6. Hesap, reklam SDK'sı ve kesin-detection vaadi yok.
7. Haftalık fear subscription yerine **$2.99 trip pass** veya **$7.99–$9.99 lifetime** hipotezi.

Bu wedge kullanıcı tercihine ve kontrollü accuracy testine sahip değildir.

## Top 5 rakip ve ikame

| Rakip / ikame | Gözlenen sinyal | RoomCheck için sonuç |
|---|---|---|
| [Hidden Spy Camera Finder Pro](https://apps.apple.com/us/app/hidden-spy-camera-finder-pro/id1560989782) | ~12K rating, subscription | Güçlü talep proxy'si; trust/accuracy açığı |
| [Hidden Camera Scanner Detector](https://apps.apple.com/us/app/hidden-camera-scanner-detector/id1468725639) | ~2.3K rating | Keyword rekabeti |
| [Hidden Camera DETECTOR — WLAN](https://apps.apple.com/us/app/hidden-camera-detector-wlan/id1645273817) | ~1.9K rating | Ağ tarama beklentisini yükseltir |
| [Hidden Camera Detector](https://apps.apple.com/us/app/hidden-camera-detector/id532882360) | ~1.8K, 3.6 | Olgun fakat güven sorunu yaşayan kategori |
| Manuel checklist + fiziksel RF detector | App iznine bağlı değil | En güvenilir ikame olabilir; fiziksel donanım bazı cihazlarda üstün |

## Solo MVP siniri

**Dört core ekran:** Room Type, Guided Checklist, Visible Signals, Result/Next Steps.

**Üç ana özellik:**

1. Room-specific inspection checklist.
2. İzinli local-network/BLE/lens sinyallerini açıklayan inspection queue.
3. Normal/inspect/insufficient sonuç özeti ve güvenli sonraki adım.

İlk sürümde covert recording, magnetic “camera score”, universal detection, cloud scan history, public incident map veya otomatik suç bildirimi yoktur.

## Skor ve fatal gate

| Boyut | Low | Base | High |
|---|---:|---:|---:|
| Problem / talep | 3 | 4 | 4 |
| Monetizasyon / ekonomi | 2 | 3 | 4 |
| Rekabet / wedge | 2 | 3 | 4 |
| Dağıtım | 2 | 3 | 4 |
| Tekrar değeri | 1 | 2 | 3 |
| Zamanlama | 3 | 3 | 4 |

**Fırsat Çekiciliği:** **46 / 64 / 79 — borderline**  
**Kanıt Gücü:** **D**

| Fatal gate | Durum | Gerekçe |
|---|---|---|
| LEGAL_BLOCKED | clear | Kayıt/dinleme yok; inspection scope'u |
| CORE_FEASIBILITY_BLOCKED | **unknown** | iOS görünürlüğü eksik; yararlı accuracy corpus'u yok |
| PLATFORM_BLOCKED | clear | Inspection emsalleri var; copy misleading olmayacak |
| SAFETY_ETHICS_BLOCKED | clear | Kesinlik yok, yetersiz veri açık, tüm scan local — uygulamada doğrulanmalı |

## Sonraki teknik RAT

20 kontrollü oda, 30 bilinen kamera ve normal elektroniklerden oluşan corpus kur. Yalnız teknik olarak görünür olması beklenen kamera alt kümesini ayrı etiketle; görünmez vakaları recall denominator'ına sessizce katma veya “temiz” sayma.

- Ana metrik: Görülebilir kameraların en az %80'ini `incelemeye değer` kuyruğuna alma.
- Guardrail: Yüksek-risk false positive en fazla %10; görünmez/yetersiz her vakada %100 açık disclosure.
- Durdurma: Eşik kalırsa detector iddiasını çıkar ve ürünü saf checklist'e pivot et veya `ELENDIR`.
- Geçiş: Teknik eşik geçse bile 10–15 gezginle comprehension ve $7.99 refundable preorder testi gerekir.

Baseline/MDE bilinmediği için RAT exploratory'dir ve `BUILD_SMALL` yetkisi vermez.

Teknik gate sözleşmesi: [phases/06-prebuild-plan.md](phases/06-prebuild-plan.md). Sözleşme `room-core-feasibility` D derecesinin nedenini (üç kaydın tamamı çürütücü), masa başında yapısal olarak D kalan `room-legal`/`room-safety` claim'lerini ve G0 corpus'unun ön-kayıtlı eşiklerini ayırır. Kullanıcı ve ödeme deneyleri gate `clear` olmadan açılmaz.

## Kanit sinirlari

Rakip rating/fiyatları revenue değildir. App Store yorumları accuracy benchmark'ı değildir. iOS dokümanları API sınırını açıklar fakat RoomCheck'in kontrollü precision/recall değerini vermez. ABD hukuk değerlendirmesi scope ile sınırlıdır ve hukuk görüşü değildir.
