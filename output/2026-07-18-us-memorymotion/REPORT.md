# US MemoryMotion — Quick Scan

**Tarih:** 2026-07-18  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** Consumer Utility  
**Risk modifier:** Sensitive data, AI variable cost, platform dependency  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

**MemoryMotion**, dört aday içindeki en yüksek ticari/viral tavana fakat en ağır teknik ve ekonomik riske sahip üründür. Generic “prompt yaz, her şeyi videoya çevir” uygulaması değildir. Kullanıcı eski bir aile fotoğrafını seçer ve yalnız üç ciddi hareketten birini üretir: hafif bakış, doğal gülümseme veya yavaş kamera yaklaşması.

Kritik fark, eğlenceli dans filtresi değil **saygılı anı, kimlik koruma ve hatalı üretimde otomatik kredi iadesi**dir. Masa başı araştırması bu wedge'i test etmeye değer buluyor; AI çıktısının yeterli kalitede ve kârlı üretilebildiğini henüz kanıtlamıyor.

## Kullanici, an ve yapilacak is

- Segment: Vefat etmiş veya uzak bir yakının eski fotoğrafını kısa, duygusal ve paylaşılabilir bir anıya çevirmek isteyen ABD'li iPhone kullanıcısı.
- Tetikleyici: Anma, doğum günü, aile grubu paylaşımı, eski albüm taraması.
- Mevcut ikameler: AI Video/Kling/Revive, Motionleap'in manuel hareketi, slideshow veya hiç dokunmamak.
- İstenen sonuç: Kişiyi başka birine dönüştürmeden ve komik/dans eden içerik üretmeden beş saniyelik güvenilir bir anı klibi.

## Dogrudan gozlemler

- [AI Video](https://apps.apple.com/us/app/ai-video-ai-video-generator/id6478868302) yaklaşık 24K rating, 4.5 ve US Photo & Video chart'ta yaklaşık #12 gösterdi; haftalık $4.99–$14.99 ve coin seçenekleri vardı ([memory-ai-video-leader], [memory-ai-video-pricing]).
- Aynı listing'deki görünür bir yorum, vefat etmiş kişilerin fotoğraflarını canlandırdığını ve dans yerine daha ciddi old-photo hareketleri istediğini belirtiyordu ([memory-serious-use-review]). Bu tek, seçilmiş bir yorumdur; segment prevalansı değildir.
- Görünür olumsuz yorumlarda kimlik bozulması, başarısız işlem ve abonelikten sonra ek coin tüketimi vardı ([memory-quality-complaints]).
- [Motionleap](https://apps.apple.com/us/app/motionleap-3d-photo-animator/id1381206010) yaklaşık 117K rating; [Revive](https://apps.apple.com/us/app/revive-ai-face-photo-animator/id1616862692) yaklaşık 25K rating; [Kling](https://apps.apple.com/us/app/kling-ai-ai-image-video-maker/id6738049229) yaklaşık 26K rating ve güçlü kategori görünürlüğü gösterdi ([memory-motionleap-incumbent], [memory-revive-pricing], [memory-kling-current]).
- Resmî fiyat dokümanında seçilen Runway modellerinin beş saniyelik üretimi kabaca $0.25–$0.60 provider maliyetine denk geliyor; fal kataloğunda seçili modeller yaklaşık $0.35–$2.00 aralığı gösterdi ([memory-runway-pricing], [memory-fal-pricing]). Retry, başarısız iş, storage, ödeme ve destek bu tutarlara dahil değildir.

Bu gözlemler kategori ilgisini ve fiyat mimarisini destekler; gelir, başarılı üretim oranı veya yeni ürünün ödeme dönüşümü değildir.

## Cikarim ve wedge

Generic AI video pazarı güçlü incumbent'lar, yüksek pazarlama bütçesi ve sürekli model/şablon operasyonu gerektiriyor. Tek kişinin rekabet edebileceği ürün daha dar olmalı:

1. Yalnız eski aile portresi ve grup fotoğrafı.
2. Üç ciddi, konuşmasız hareket; prompt kutusu yok.
3. Yüz/kimlik karşılaştırmalı kalite kapısı; düşük skor otomatik reddedilir.
4. Teknik başarısızlıkta kredi otomatik geri gelir.
5. Yüklenen fotoğrafın otomatik silinmesi ve açık AI disclosure.
6. “Unlimited weekly subscription” yerine örneğin **5 klip $9.99** kredi paketi hipotezi.

Wedge'in kullanıcı tarafından tercih edildiği ve kabul edilebilir üretimin maliyet eşiğinde çalıştığı gözlenmedi.

## Top 5 rakip ve ikame

| Rakip / ikame | Güçlü taraf | MemoryMotion için sonuç |
|---|---|---|
| [AI Video](https://apps.apple.com/us/app/ai-video-ai-video-generator/id6478868302) | Aktif chart, geniş model seti | Ciddi old-photo review'u wedge sinyali; kalite/kredi şikâyeti risk |
| [Motionleap](https://apps.apple.com/us/app/motionleap-3d-photo-animator/id1381206010) | Büyük installed-behavior proxy'si, manuel kontrol | Generic animation'a karşı güçlü incumbent |
| [Revive](https://apps.apple.com/us/app/revive-ai-face-photo-animator/id1616862692) | Face animation, weekly+lifetime fiyat | Aynı dikkat bütçesi; episodik ödeme ikamesi |
| [Kling AI](https://apps.apple.com/us/app/kling-ai-ai-image-video-maker/id6738049229) | Güçlü model/brand ve chart | Model kalitesi beklentisini yükseltir |
| [Photo Scanner Plus](https://apps.apple.com/us/app/photo-scanner-plus/id951627022) / slideshow | Aile fotoğrafı tarama ve hikâye ikamesi | Anı işi AI olmadan da çözülebilir |

## Solo MVP siniri

**Dört core ekran:** Photo Pick/Crop, Motion Choice, Generating/Quality Check, Result/Credits.

**Üç ana özellik:**

1. Üç bounded motion mode.
2. Provider çağrısı + kimlik/başarı kontrolü + otomatik refund.
3. Beş saniyelik export ve güvenli silme akışı.

İlk sürümde prompt marketplace, sosyal feed, konuşan avatar, public-figure deepfake, uzun video, kullanıcı galerisi veya sürekli template operasyonu yoktur. Buna rağmen backend job queue, ödeme, fotoğraf lifecycle'ı, provider failover ve support gerekir; bu yüzden solo işletme yükü `medium-high`tır.

## Skor ve fatal gate

| Boyut | Low | Base | High |
|---|---:|---:|---:|
| Problem / talep | 3 | 4 | 5 |
| Monetizasyon / ekonomi | 2 | 3 | 4 |
| Rekabet / wedge | 2 | 3 | 4 |
| Dağıtım | 2 | 3 | 4 |
| Tekrar değeri | 1 | 2 | 3 |
| Zamanlama | 4 | 4 | 5 |

**Fırsat Çekiciliği:** **48 / 66 / 86 — borderline**  
**Kanıt Gücü:** **C**

Dört fatal gate masa başında `clear`, ancak bu yalnız dar scope içindir: kullanıcı-seçimli fotoğraf, konuşmasız hareket, AI disclosure, silme ve public-figure/deceptive use'u dışlama. Provider erişimi ve mevcut App Store emsalleri teknik/yayın yolunun varlığını destekler; güvenli kalite veya sürdürülebilir marjı kanıtlamaz.

## Sonraki gercek davranis testi

Önce ödeme testi değil **40 fotoğraflık teknik RAT**:

- Corpus: portre, grup, düşük çözünürlük, hasarlı fotoğraf ve farklı cilt tonları.
- Karşılaştırma: iki provider; sabit üç hareket ve aynı kabul rubric'i.
- Geçiş: en az %80 kabul edilebilir çıktı ilk deneme veya tek retry içinde; sıfır ağır wrong-person/identity swap; teslim edilen ortalama inference maliyeti en fazla $1.20.
- Durdurma: Bu eşiklerden biri kalırsa provider/scope pivotu veya park.

Teknik geçişten sonra 12 hedef kullanıcı kendi fotoğrafıyla deneme yapar ve hazır olmadığı açıkça belirtilen beş-klip kredi paketi için refundable preorder görür. En az 4/12 gerçek preorder yoksa build yatırımı yapılmaz. Baseline/MDE bilinmediği için bu da directional'dır; tek geçiş `BUILD_SMALL` vermez.

## Kanit sinirlari

API fiyatı teslim edilmiş klip maliyeti değildir. Görünen App Store yorumları random veya stratified değildir. Duygusal zarar, consent, silme doğruluğu, fraud/chargeback, model değişimi, moderation ve support yükü test edilmedi. Ham skor, bu operasyon risklerini tek başına temsil etmez.
