# ABD iOS Davranışsal Ödeyen Segmentler — Compare v4.0

**Araştırma tarihi:** 2026-07-11  
**Karar aşaması:** desk research  
**Ortak kontrat:** ABD, iOS-first saha/iş akışı, `b2b_prosumer`, yaş değil tekrarlanan
problem ve mevcut ödeme davranışı.

## Yönetici sonucu

Yaş veya gelir hedeflemesi yerine **iş başına para kazanan ve telefonda tekrar eden bir
workflow'u olan profesyonel** daha savunulabilir başlangıç segmentidir. Altı fikirden ikisi
aynı base skorda öne çıktı:

1. **Home inspector capture/export companion — 51/60/65, C, TESTE_DEGER.**
2. **Mobile pet groomer disruption recovery — 48/60/65, C, TESTE_DEGER.**

İlk davranış testi home inspector ile yapılmalı: doğrudan akşam raporu problemi, iş başına
yaklaşık $457 vendor proxy'si ve $50–$109/ay ücretli incumbent bütçesi var. Fakat ürün full
raporlama platformu değil, incumbent'a bağlanan güvenli companion olmalıdır. Pet groomer
ikinci paralel adaydır; dar wedge service-duration-aware disruption recovery'dir.

Hiçbir fikir build izni almadı. Beş aday `PREBUILD_PENDING`; photographer overall evidence D
olduğu için `BELIRSIZ` kaldı.

## Karşılaştırma

| Sıra | Segment / dar wedge | Skor low/base/high | Kanıt | Karar | Başlıca risk |
|---:|---|---:|:---:|---|---|
| 1 | Home inspector incumbent capture/export | 51 / 60 / 65 | C | TESTE_DEGER | E&O; hatalı defect ve entegrasyon |
| 2 | Mobile pet groomer disruption recovery | 48 / 60 / 65 | C | TESTE_DEGER | Alt segment belirsiz; rota/privacy |
| 3 | Solo handyman capture/export | 46 / 57 / 66 | C | TESTE_DEGER | Aynı wedge'de güçlü yakın rakipler |
| 4 | Hybrid trainer check-in triage | 49 / 52 / 63 | C | TESTE_DEGER | Sağlık verisi, güven ve incumbent AI |
| 5 | Residential cleaning quote-to-proof | 48 / 51 / 65 | C | TESTE_DEGER | Generic özellikler commodity; Android ekip |
| 6 | Real-estate photographer shoot QA | 31 / 51 / 52 | D | BELIRSIZ | Shot-list ödeme kanıtı yok; $5/job suite |

Skorlar başarı olasılığı değildir. Aynı v4.0 B2B/prosumer ağırlıkları kullanılmıştır.
Masa başında repeat en fazla 3, monetizasyon yalnız rakip fiyatına dayanıyorsa base 2 tutuldu;
bu nedenle kaba vendor puanları aşağı kalibre edildi.

## 15 problem havuzu

### Saha dokümantasyonu

1. Inspector'ın akşam raporu yazması.
2. Fotoğraf ile sesli notun doğru sisteme/odaya bağlanmaması.
3. Kaynaksız AI defect dili ve E&O riski.
4. Incumbent şablonuna veri taşıma maliyeti.
5. Photographer'ın benzer odaları/çekimleri atlaması.

### Mobil yerel hizmet

6. Grooming van arızasında tüm günün yeniden kurulması.
7. Service duration ve buffer'ı hesaba katmayan rota.
8. Sahada sıradaki adres/pet notuna yavaş erişim.
9. Cleaning'de site-unseen teklif hatası.
10. Before/after kanıtının kaybolması veya çoğalması.

### Solo profesyonel yönetimi

11. Handyman'ın saha notundan quote üretme süresi.
12. Estimate/change-order kaybı ve teslim hatası.
13. Koçun check-in inbox'ını önceliklendirememesi.
14. Mesaj/voice-note transkripsiyon ve sync boşlukları.
15. Otomasyon ile insan koçluğu ve safety arasındaki gerilim.

## Neden zengin emekli yerine bu yaklaşım?

- Pew'in 2025 verisinde 65+ smartphone sahipliği %78 iken 18–29'da %97 ve 30–49'da
  %96'dır; sahiplik ödeme niyeti değildir.
- YouGov'un ABD mobil abonelik anketinde en az bir ücretli abonelik 65+ için %44, 18–29
  için %77'dir; metrik iOS/App Store billing'e özel değildir.
- RevenueCat 2026 verisinde North America subscription projelerinin %75,1'i gelirinin
  %80'den fazlasını App Store'dan alıyor. Ancak kategori ve iş modeli farkı yaş hedefinden
  daha kullanışlıdır: D60 median RPI Health & Fitness'ta $0,66, Business'ta $0,50'dir.

Kaynaklar: [Pew Mobile Fact Sheet](https://www.pewresearch.org/internet/fact-sheet/mobile/),
[YouGov](https://yougov.com/en-us/articles/52810-reality-checks-talkshow-paid-app-subscriptions-jon-yantz),
[RevenueCat 2026](https://www.revenuecat.com/state-of-subscription-apps-2026-health-and-fitness/).

## Önerilen sıra ve ürün yüzeyi

1. **Önce chat/concierge:** 8 home inspector ile gerçek, redacted işler ve $49 peşin test.
2. **Sonra küçük native arayüz:** test geçerse kamera, ses, kaynak eşleme ve approve/export
   için 4 core ekranı geçmeyen iOS companion. Chat yardımcı giriş olabilir; ana arayüz olamaz.
3. **İkinci RAT:** inspector işe alımı başarısızsa mobile pet groomer $25–39 disruption
   concierge testi.

## Sınırlamalar ve doğrulama sonucu

**Share with caveats.** Exact alt segment sayıları kamu kodlarında çoğunlukla yapısal olarak
gözlenemiyor. App Store/Reddit temaları self-selected ve prevalans değildir. Rakip fiyatı,
bu yeni ürüne ödeme davranışı değildir. RevenueCat verisi kendi SDK'sını kullanan subscription
apps evrenidir; ABD+iOS-only kesit değildir. Gerçek karar için depozito ve ikinci doğal kullanım
gerekir.

Quick paketleri: [home inspector](2026-07-11-us-home-inspector-companion/REPORT.md),
[mobile pet](2026-07-11-us-mobile-pet-groomer-disruption/REPORT.md),
[handyman](2026-07-11-us-solo-handyman-capture/REPORT.md),
[trainer](2026-07-11-us-hybrid-trainer-triage/REPORT.md),
[cleaning](2026-07-11-us-residential-cleaning-proof/REPORT.md),
[photographer](2026-07-11-us-real-estate-photographer-qa/REPORT.md).

