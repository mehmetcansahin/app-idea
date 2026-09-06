# US Before/After Reel — Quick Scan

**Tarih:** 2026-07-18  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** Consumer Utility  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

**Before/After Reel**, en hızlı üretilebilecek ve en ucuz test edilebilecek adaydır. Kullanıcı iki fotoğrafı yan yana koymak yerine 2–24 ilerleme fotoğrafı seçer; uygulama aynı yüzü, nesneyi veya oda noktasını hizalayıp tarih etiketli dikey dönüşüm videosu üretir.

Kategori davranışı gözleniyor, fakat rating ölçeği slideshow ve AI video liderlerinden düşük; yeni local/one-time rakipler de giriyor. Bu nedenle fikir “boş pazar” değil, spesifik hız ve hizalama wedge'inin görev testinde kanıtlanması gereken dar bir utility'dir.

## Kullanici, an ve yapilacak is

- Segment: Fitness, sanat, bahçe, oda yenileme, restorasyon veya kişisel proje ilerlemesi paylaşan ABD'li iPhone kullanıcısı.
- Tetikleyici: Aynı konunun farklı tarihlerde çekilmiş fotoğrafları vardır; framing farkı yüzünden geçiş amatör görünür.
- Mevcut ikameler: CapCut/Canva template'i, manuel crop, iki-fotoğraf compare app'i veya hiç video yapmamak.
- İstenen sonuç: İki dakikadan kısa sürede hizalanmış, tarihli, 9:16 video.

## Dogrudan gozlemler

- [Before and After: Compare Photo](https://apps.apple.com/us/app/before-and-after-compare-photo/id1500915148) yaklaşık 2.1K rating ve 4.7 gösterdi ([before-compare-leader]).
- [BeforeAfter: Instant Watermark](https://apps.apple.com/us/app/beforeafter-instant-watermark/id1023269035) yaklaşık 2.2K rating ve 4.8 gösterdi; davranış tek bir ürüne özgü değil ([before-watermark-leader]).
- Yeni [Before & After Video Maker](https://apps.apple.com/us/app/before-after-video-maker/id6779032596) 5.5 MB, offline, data-not-collected ve $3.99 one-time olarak listelendi. Bu, local implementation'ı desteklerken “local ve one-time tek başına wedge” iddiasını zayıflatır ([before-local-newcomer]).
- Başka bir yeni [Before and After Video Maker](https://apps.apple.com/us/app/before-and-after-video-maker/id6761030222) $7.99/hafta, $19.99/ay ve $99.99 lifetime seçenekleri gösterdi fakat anlamlı rating sinyali yoktu ([before-subscription-newcomer]). Fiyat etiketi ödeme davranışı değildir.
- Mevcut listing'ler çoğunlukla iki-fotoğraf karşılaştırmasını öne çıkarıyor; 2–24 fotoğrafı tek anchor'a auto-align edip tarihli 9:16 export etme akışı test edilebilir bir boşluk hipotezidir ([before-autoalign-gap]).

## Cikarim ve wedge

Yeni ürünün farkı “daha güzel before/after” olmamalı. Görev düzeyindeki iddia:

1. Kullanıcı yüz, nesne veya oda anchor'ını bir kez seçer.
2. Uygulama 2–24 fotoğrafı otomatik ölçekler, döndürür ve hizalar.
3. Kullanıcı timeline, tarih görünümü ve hız dışında edit yapmaz.
4. 9:16 video, GIF veya Live Photo export alır.
5. İşleme cihazda; hesap yok; $9.99–$14.99 lifetime hipotezi.

Auto-align kalitesi veya kullanıcının generic editörden geçişi henüz gözlenmedi.

## Top 5 rakip ve ikame

| Rakip / ikame | Güçlü taraf | Risk / açık |
|---|---|---|
| [Before and After: Compare Photo](https://apps.apple.com/us/app/before-and-after-compare-photo/id1500915148) | Yerleşik iki-fotoğraf davranışı | Multi-date vertical story wedge'i test edilebilir |
| [BeforeAfter: Instant Watermark](https://apps.apple.com/us/app/beforeafter-instant-watermark/id1023269035) | Yüksek rating proxy'si, watermark use case | Daha profesyonel/iş odaklı ikame |
| [Before & After Video Maker](https://apps.apple.com/us/app/before-after-video-maker/id6779032596) | Offline ve one-time | Doğrudan yeni rakip; privacy tek başına fark değil |
| [Before and After Video Maker](https://apps.apple.com/us/app/before-and-after-video-maker/id6761030222) | Geniş price architecture | Traction belirsiz; yine de keyword rekabeti |
| CapCut / Canva / Photos | Ücretsiz veya zaten yüklü | En güçlü ikame; manuel ama esnek |

## Solo MVP siniri

**Dört core ekran:** Project Grid, Photo/Anchor Select, Aligned Timeline Preview, Export/Upgrade.

**Üç ana özellik:**

1. Anchor tabanlı otomatik hizalama ve manuel düzeltme.
2. Tarih etiketli 2–24 fotoğraf timeline'ı.
3. Local 9:16 video/GIF export.

İlk sürümde sosyal ağ, cloud sync, health outcome skoru, AI video generation veya creator marketplace yoktur.

## Skor ve fatal gate

| Boyut | Low | Base | High |
|---|---:|---:|---:|
| Problem / talep | 2 | 3 | 4 |
| Monetizasyon / ekonomi | 2 | 3 | 4 |
| Rekabet / wedge | 2 | 3 | 4 |
| Dağıtım | 2 | 3 | 4 |
| Tekrar değeri | 2 | 3 | 4 |
| Zamanlama | 3 | 3 | 4 |

**Fırsat Çekiciliği:** **42 / 60 / 80 — borderline**  
**Kanıt Gücü:** **C**

Dört fatal gate `clear`: kullanıcı-seçimli medya, local rendering, mevcut App Store emsalleri ve public feed/health claim'in scope dışı olması. Hassas beden fotoğrafları nedeniyle privacy uygulaması yine de doğrulanmalıdır.

## Sonraki gercek davranis testi

12 hedef kullanıcıdan toplam 20 gerçek progress set'i al. Aynı seti mevcut editörleriyle ve auto-align prototipiyle tamamlat. Baseline/MDE bilinmediği için eşikler exploratory'dir.

- Geçiş: En az 8/12 kişi iki dakikada export; en az 6/12 sonucu gerçekten paylaşır veya projesinde kullanır; en az 4/12 açık koşullu $9.99 refundable preorder bırakır.
- Guardrail: Hassas fotoğraflar araştırmacıya yüklenmez; test mümkün olduğunca cihazda çalışır.
- Durdurma: Üç eşikten biri kalırsa park et. Auto-align tercih edilir fakat ödeme kalırsa daha dar bir use case'e pivot et.

Tek test doğrudan build izni vermez; ikinci doğal progress döngüsünde tekrar kullanım ve yeniden puanlama gerekir.

## Kanit sinirlari

Rakip rating'leri gelir ve retention değildir. Yeni rakiplerde rating olmaması başarısızlık kanıtı değildir. Keyword hacmi, creator distribution, auto-align accuracy, gerçek ödeme ve ikinci-döngü kullanım gözlenmedi.
