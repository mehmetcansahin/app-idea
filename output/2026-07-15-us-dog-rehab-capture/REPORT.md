# US Dog Rehab Capture — Quick Scan

**Tarih:** 2026-07-15  
**Kapsam:** ABD / US App Store / iPhone  
**Arketip:** B2B/Prosumer  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

Altı fikir içindeki en iyi test adayı bu, fakat “AI köpeğin yürüyüşünü teşhis eder” ürünü olarak değil. Savunulabilir ilk kapsam; rehabilitasyon kliniğinin belirlediği açı, mesafe ve hareket protokolünü sahibin doğru çekmesini sağlayan, haftalık videoları yan yana getiren ve terapiste düzenli paket veren bir capture/export aracıdır.

AAHA, ev videosu ve fotoğrafını, aktiviteyi, gait gözlemini ve sahibin bildirimlerini değerlendirme girdileri arasında sayıyor. Bu doğrudan problem sinyalidir. Ancak anisteps, Wibbi, Tendiboots, The Dog Rehab App ve Canine Health Hub alanın parçalarını şimdiden kapsıyor. Wedge bu nedenle “gait AI” değil; **terapist tarafından atanmış, tekrarlanabilir çekim ve karar-handoff iş akışı**dır.

## Kim, hangi anda kullanir?

- Alıcı: canine-rehab kliniği veya bağımsız CCRT/rehab veterineri.
- Son kullanıcı: klinikten ev egzersizi alan iPhone sahibi.
- Tetikleyici: ilk değerlendirme veya ameliyat sonrası plan verildiğinde.
- Tekrarlanan iş: aynı yürüyüş/hareketi haftalık aynı koşullarda çekmek.
- Çıktı: önce/sonra karşılaştırma, çekim kalite kontrolü, kısa owner notu ve terapist PDF/link paketi.

## Dogrudan gozlemler

- [AAHA rehberi](https://www.aaha.org/trends-magazine/april-2022/f2-pm-guidelines/) ev videosu/fotoğrafı, owner input, gait ve tekrar değerlendirmeyi açıkça içeriyor.
- [CRI](https://www.caninerehabinstitute.com/find-therapist) değerlendirme, kişiselleştirilmiş plan ve evde yürütülebilen rehabilitasyon akışını tarif ediyor; ayrıca erişilebilir bir profesyonel dizini var.
- [anisteps](https://www.anisteps.com/) akıllı telefonla gait capture, owner app ve vet portal iddiasıyla doğrudan yakın rakip.
- [Wibbi](https://wibbi.com/veterinary/) egzersiz planı, owner mobile deneyimi ve ilerleme takibini kapsıyor.
- [Tendiboots](https://apps.apple.com/us/app/tendiboots-canine/id6474444290) sensör donanımıyla objektif gait takibi ve PDF export sunuyor.
- [Apple Vision](https://developer.apple.com/documentation/vision/detectanimalbodyposerequest) hayvan body-pose isteği sunuyor; bu capture guidance için teknik yol, klinik doğruluk kanıtı değil.

## Cikarim

İlk sürümün teşhis, lameness score veya tedavi önerisi vermemesi gerekir. Kamera overlay, zemin/ışık kontrolü, hayvanın kadrajda kalması, klibin süresi ve terapistin seçtiği protokol yeterli olabilir. Böylece FDA/Apple doğruluk iddiası riski azalır ve gerçek değer “daha kıyaslanabilir follow-up” olarak test edilir.

## Rakip ve ikameler

| Urun/ikame | Gozlenen kapsam | Bu fikir icin anlamı |
|---|---|---|
| anisteps | Kamera gait, skor, owner app, vet portal | En yakın ürün; AI skor wedge'ini zayıflatıyor |
| Wibbi Vet | Egzersiz planı, video talimatı, progress | Klinik dağıtım ve HEP zaten çözülüyor |
| Tendiboots | Sensörlü objektif gait | Daha güçlü ölçüm, fakat hardware bağımlı |
| The Dog Rehab App | Ev egzersiz içerikleri | DTC içerik wedge değil |
| Canine Health Hub | Egzersiz, rehab planı, progress | Genel consumer rehab alanı doluyor |
| Peqaboo | AI pet-health ve gait video iddiası | Otomatik analiz kalabalıklaşıyor |
| Tractive | GPS/aktivite donanımı | Sürekli aktivite ikamesi |
| Dogo | Video gönderip eğitmen geri bildirimi | Owner video-feedback davranışının komşu kanıtı |
| GoDog | Egzersiz/health diary | Genel pet-owner ikamesi |
| Manuel workflow | SMS/e-posta/iMessage videoları | Ücretsiz ve güçlü alışkanlık ikamesi |

## Review sinyali ve protokol siniri

Apple'ın açık RSS akışında Wibbi için 15 yorum bulunabildi: 1–2 yıldız 7, 3 yıldız 6, 4–5 yıldız 2. Bunların yalnız küçük bir bölümü son 12 ayda. 15 yorumun 10'unda terapi/egzersiz/program, 7'sinde login/refresh/erişim teması görüldü. Bu oranlar yalnız bu self-selected örnekleme aittir; pazar prevalansı değildir. Yakın rakiplerin çoğunda kamuya açık 15 yorum bile olmadığı için **Standard review minimumu karşılanmadı**.

## Skor

| Boyut | Low | Base | High | Gerekce |
|---|---:|---:|---:|---|
| Problem/talep | 3 | 4 | 4 | Klinik rehberde owner video ve reassessment gerçek |
| Monetizasyon | 2 | 3 | 4 | Rehab episode spend var; yazılım bütçesi yok |
| Wedge | 1 | 2 | 3 | Yakın rakipler var; protocol capture daha dar |
| Dağıtım | 2 | 3 | 4 | CRI/AARV/klinik kanalı erişilebilir, dönüşüm bilinmiyor |
| Tekrar değeri | 3 | 4 | 4 | Aktif vakada haftalık döngü güçlü; episode sonrası zayıf |
| Zamanlama | 3 | 3 | 4 | Mobil capture olgun; kategori aynı anda kalabalıklaşıyor |

**Fırsat Çekiciliği:** **46 / 65 / 77 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear, yalnız non-diagnostic capture/export kapsamında.
- Core feasibility: clear, fakat cihaz üstünde capture-quality testi şart.
- Platform: clear, accuracy ve medical claim kullanılmazsa.
- Safety/ethics: clear, klinisyen planı değiştirilmez; owner videosu için açık consent ve silme gerekir.

## Sonraki gercek davranis testi

Sekiz ABD canine-rehab kliniğine **$49 ücretli, üç haftalık concierge pilot** sat. On gerçek vaka için terapist capture protokolünü manuel hazırla; owner kliplerini kalite checklist'iyle değerlendir; haftalık karşılaştırmalı paketi terapiste gönder.

**Stop:** 4'ten az klinik ödeme yaparsa, 30'dan az owner videosu checklist'i geçerse veya 3'ten az terapist paketi bir follow-up kararını kaydetmek için kullanırsa durdur.

Bu masa başı karar build izni değildir.
