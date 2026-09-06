# ABD iOS Mobil Uygulama Fikirleri — Detayli Karsilastirma

**Tarih:** 2026-07-15  
**Kapsam:** ABD / US App Store / iPhone-first  
**Metodoloji:** v4.0  
**Asama:** Desk research; build izni yok

## Karar ozeti

Tek bir fikre test bütçesi ayıracaksak **Dog Rehab Capture**. İkinci düşük-maliyetli test **Card Condition & Custody**. **Tox Motion Passport** ham skorda Card'dan bir puan yüksek olsa da farklı arketip, health-data riski, ücretsiz brand incumbents ve sekiz haftalık retention testi nedeniyle üçüncü sırada.

Portföy kararı:

1. **Dog Rehab Capture — TEST NOW.** Klinik tarafından atanmış, non-diagnostic standardized video capture ve therapist handoff.
2. **Card Condition & Custody — TEST NEXT.** Official grade değil; active raw-card seller için listing + packing passport.
3. **Tox Motion Passport — HOLD / TARGETED TEST.** Yalnız motion-specific, local-first ve provider-neutral scope.
4. **Package Damage Claim Kit — PARTNER-DEPENDENT.** Mobil anı güçlü, repeat zayıf; reseller kanalı bulunursa pay-per-case test.
5. **RefundLoop — PARK.** Problem büyük ama exact-product wedge neredeyse kapanmış.
6. **Trip Disruption Evidence — PARK.** Belge işi gerçek; RefundMe ve değişken kural katmanı upside'ı daraltıyor.

## Research contract

- Karar: Hangi fikre bir sonraki gerçek davranış testi bütçesi verilmeli?
- Hedef: ABD, US App Store, iPhone-first; Android veya global pazar genellenmedi.
- Kanıt cutoff: 2026-07-15.
- Masa başı karar enum'u: `ELENDIR`, `BELIRSIZ`, `TESTE_DEGER`, `TEST_ONCELIKLI`.
- Rating yalnız E2/supporting proxy; traction veya ödeme kanıtı değil.
- Farklı arketipler çıplak skorla sıralanmadı; fatal gate → evidence grade → interval → risk/test cost sırası kullanıldı.

## Karsilastirma tablosu

| Test sirasi | Fikir | Arketip | Skor low/base/high | Kanit | Desk karari | Portfoy aksiyonu | Ana risk |
|---:|---|---|---:|---|---|---|---|
| 1 | Dog Rehab Capture | B2B/Prosumer | 46 / 65 / 77 | C | TESTE_DEGER | Test now | Yakın rakipler; clinic payment bilinmiyor |
| 2 | Card Condition & Custody | B2B/Prosumer | 37 / 57 / 73 | C | TESTE_DEGER | Test next | TCG Grading certificate/QR overlap |
| 3 | Tox Motion Passport | Consumer Subscription | 38 / 58 / 77 | C | TESTE_DEGER | Hold / narrow test | Health data, brand apps, retention süresi |
| 4 | Package Damage Claim Kit | Consumer Utility | 31 / 50 / 68 | C | TESTE_DEGER | Partner-dependent | Seyrek olay; shipper/recipient rolü |
| 5 | RefundLoop | Consumer Subscription | 34 / 51 / 58 | C | TESTE_DEGER | Park | Exact competitors; high skor <60 |
| 6 | Trip Disruption Evidence | Consumer Utility | 32 / 47 / 67 | C | TESTE_DEGER | Park | RefundMe overlap; rule maintenance |

Tüm fatal gate'ler yalnız raporlarda tanımlı dar scope için `clear`. Hiçbir fikir `TEST_ONCELIKLI` değil; low bound 60'a ulaşmıyor ve hiçbirinde product-specific E3/E4 davranış kanıtı yok.

## Onceki varsayimlari degistiren bulgular

### CardProof boş pazar değil

[TCG Grading](https://apps.apple.com/us/app/tcg-grading-card-ai-scanner/id6742651049) condition değerlendirmesi, professional PDF, certificate number, QR verification ve secure register sunuyor. Bu, ilk “scan + certificate” fikrinin wedge'ini doğrudan kapatıyor. [CollX](https://apps.apple.com/us/app/collx-sports-card-scanner/id1581164444), Collectr ve LUDEX de collection/price/seller workflow'u sahiplenmiş durumda.

Kalan hipotez yalnız **listing condition + packing custody**. Satıcı bu ek adımı tekrar etmeyecekse ürün yok.

### RefundLoop 2026'da commoditize oluyor

[ReturnTrack](https://apps.apple.com/us/app/returntrack-refund-tracker/id6754392016), [Return Proof](https://typeswitch.net/return-proof-app/), Returno Refundo, BackBye, Returnful ve Jareon aynı deadline/refund/evidence işinin farklı kombinasyonlarını sunuyor. [NRF'nin](https://nrf.com/research/2025-retail-returns-landscape) $849.9B return hacmi app talebiyle karıştırılmamalı.

### Tox diary değil, olsa olsa motion

[TouchUp](https://apps.apple.com/us/app/touchup-botox-filler-log/id6777471839), Aesthetic Diary ve LIRA neutral/private treatment log'u; [PixioDoc](https://apps.apple.com/us/app/pixiodoc-clinical-photo-app/id6754819857) ghost-overlay clinical capture'ı çözüyor. Motion sequence görülmeyen dar parça, fakat bunun haftalık kullanım değeri henüz varsayım.

## 1. Dog Rehab Capture derinlestirmesi

### En dar urun tezi

Klinik bir protokol seçer: örneğin düz zeminde soldan 10 saniye yürüyüş, sağdan dönüş, otur-kalk. Owner uygulaması geçen çekimi ghost overlay olarak gösterir, mesafe/ışık/kadraj checklist'i uygular ve klibi terapistin haftalık packet'ına ekler. Sistem skor, diagnosis veya exercise değişikliği önermez.

### Top 10 rakip ve ikame

| Rakip/ikame | Tip | Gozlenen is | Bosluk/tehdit |
|---|---|---|---|
| [anisteps](https://www.anisteps.com/) | Yakın direct | Smartphone gait, owner app, vet portal, score | En güçlü direct tehdit |
| [Wibbi Vet](https://wibbi.com/veterinary/) | Klinik software | Exercise plan, owner app, progress | HEP/handoff zaten var |
| [Tendiboots](https://apps.apple.com/us/app/tendiboots-canine/id6474444290) | Hardware + app | Objective gait, hydro, PDF | Ölçüm güçlü; hardware friction |
| [The Dog Rehab App](https://apps.apple.com/us/app/the-dog-rehab-app/id6479981352) | DTC content | Home rehab programs | Content wedge değil |
| [Canine Health Hub](https://apps.apple.com/us/app/canine-health-hub/id6470127033) | DTC content/tracker | Exercises, plans, progress | Owner subscription ikamesi |
| [Peqaboo](https://apps.apple.com/us/app/peqaboo-pet-ai-vet-health/id6503051946) | AI pet health | Video/gait health claims | AI analysis kalabalığı |
| [Tractive](https://apps.apple.com/us/app/tractive-gps-for-dogs-and-cats/id921588809) | Hardware activity | GPS/activity monitoring | Sürekli passive-data ikamesi |
| [Dogo](https://apps.apple.com/us/app/dogo-dog-training-clicker/id1153294767) | Video feedback | Owner video + trainer feedback | Video-coaching behavior komşusu |
| [GoDog](https://apps.apple.com/us/app/godog-puppy-dog-training/id1462026646) | Consumer app | Lessons, health diary, activity | Genel pet-owner attention rakibi |
| iMessage/email | Manuel | Owner sends ad-hoc clips | Ücretsiz, en güçlü habit ikamesi |

### Review mining: erisilebilen sinyal

Wibbi'nin açık Apple RSS akışında toplam 15 review bulundu; yalnız ikisi 4–5 yıldız, altısı 3 yıldız, yedisi 1–2 yıldız. Tüm tarih aralığı 2017–2026 olduğu için son-12-ay stratification karşılanmadı. Keyword coding yalnız bu örneklem içinde:

- therapy/exercise/program: 10/15
- login/refresh/access: 7/15
- 2025–2026 pozitif örnekler therapist'in gönderdiği exercises/documents'ın elde olmasını değerli buluyor.
- 2026 neutral örnek timer sırasında refresh sorununu anlatıyor.

Bu sonuç “kullanıcıların %X'i böyle düşünüyor” demek değildir. Yine de capture akışının login, timer ve fazla tap yüzünden bozulmaması gerektiğini gösteren usability input'tur.

### Neden birinci?

- Problem resmi klinik guidance içinde mevcut: owner video + gait + reassessment.
- Aktif vakada doğal haftalık tekrar var.
- CRI/AARV/clinic directories ile dar bir satış listesi yapılabilir.
- Değer AI modelinden önce concierge olarak üretilebilir.
- Üç haftada ödeme, completion ve therapist action aynı testte ölçülebilir.

### Ne olursa vazgeceriz?

Klinikler zaten Wibbi/anisteps/WhatsApp ile yeterince iyi çözüyorsa veya therapist packet'ı follow-up kararında açmıyorsa. Owner video kalitesi değil, **therapist action** esas success metric olmalı.

## 2. Card Condition & Custody derinlestirmesi

### En dar urun tezi

Raw-card seller için ilan öncesi condition views ile kargolama sırasındaki sleeve/toploader/seal/label görüntülerini aynı case'te tutar. Buyer bir QR/link ile packet'ı açabilir. Ürün grade vermez, resmi authentication iddia etmez ve dispute sonucu garanti etmez.

### Top 10 rakip ve ikame

| Rakip/ikame | Gozlenen is | Bosluk/tehdit |
|---|---|---|
| [CollX](https://apps.apple.com/us/app/collx-sports-card-scanner/id1581164444) | Scan, price, marketplace, seller tools | Büyük incumbent/channel |
| [Collectr](https://apps.apple.com/us/app/collectr-tcg-collector-app/id1603892248) | Portfolio and values | Collector attention |
| [LUDEX](https://apps.apple.com/us/app/ludex-sports-card-scanner-tcg/id1616691213) | Scan, track, eBay list | Seller workflow overlap |
| [TCG Grading](https://apps.apple.com/us/app/tcg-grading-card-ai-scanner/id6742651049) | Condition, PDF, QR verify | Certificate wedge kapalı |
| [Mint](https://apps.apple.com/us/app/trading-card-scanner-mint/id6751779804) | AI grading, sharing | Grading commoditization |
| [GradeX](https://apps.apple.com/us/app/gradex-sports-card-scanner/id6758254887) | Scanner/grading | New entrant |
| [Card Grading AI](https://apps.apple.com/us/app/card-grading-ai/id6752859834) | AI grade | Feature-level competition |
| Center Stage | Identification | Free scan substitute |
| Sports Card Investor | Market/price intelligence | Power-seller budget competitor |
| eBay listing photos/messages | Condition disclosure | Free built-in primary substitute |

### Review mining: erisilebilen sinyal

Apple RSS'de en güncel 50'şer US review:

| App | Tarih araligi | 1–2 star | 3 star | 4–5 star | Sample-ici temalar |
|---|---|---:|---:|---:|---|
| CollX | 2026-06-22–07-13 | 20 | 1 | 29 | scan/recognition 20/50; marketplace/selling 16/50; price/paywall 13/50 |
| LUDEX | 2026-05-13–07-13 | 22 | 6 | 22 | scan/recognition 23/50; price/paywall 19/50; bugs/access 5/50 |

Gözlenen tradeoff: kullanıcı catalog/marketplace değerini sevse bile yanlış identification veya valuation tüm akışı manuel düzeltmeye çeviriyor. Bu nedenle ilk testte AI card identification zorunlu olmamalı; seller kart adını/ilan linkini mevcut araçtan getirip yalnız proof capture yapabilmeli.

CollX'te yalnız bir 3-star review ve TCG Grading/Mint'te erişilebilir 15 review olmadığı için formal Standard stratification karşılanmadı.

### Neden ikinci?

- High-value condition mismatch iş sonucu doğurabiliyor.
- Active seller segmentinde ilan başına tekrar var.
- $19, iki haftalık concierge test ucuz ve hızlı.
- Health/regulatory yükü Tox'tan düşük.

Ancak TCG Grading'in QR certificate'ı nedeniyle buyer trust değil, **seller workflow adoption** kanıtlanmalı. Satıcı 10–12 ek fotoğrafı düzenli çekmiyorsa ürün yok.

## 3. Tox Motion Passport

ASPS procedure volume güçlü bir market context, fakat unique-user ve subscription demand değildir. Üç yeni local/private diary ve iki büyük free brand app varken yalnız motion-sequence davranışı test edilmeli. Sekiz haftalık completion ve provider kullanım kanıtı olmadan subscription tasarlamak erken.

Guardrail:

- on-device default; export user-controlled
- diagnosis, dosage, treatment recommendation yok
- “wear-off score” veya outcome accuracy claim yok
- FTC health-data ve Apple privacy disclosure review'ü build öncesi

## 4. Package Damage Claim Kit

UPS'nin üç fotoğrafı ve ayrıntılı belge isteği mobil checklist için iyi kaynak. Fakat claim payment shipper'a gidebilir; recipient ürünün claim sahibi olduğunu sanmamalı. En iyi model subscription değil, reseller/merchant partnership veya pay-per-case.

## 5. RefundLoop

High score 58; exact competitors çok. Yalnız mevcut aracı gerçekten bıraktıran paid switch test pozitifse tekrar düşünülmeli. App Store'a yeni bir deadline tracker koymak için kanıt yok.

## 6. Trip Disruption Evidence

Travel Guard requirements gerçek bir packet işine dönüşüyor, fakat RefundMe daha geniş işi sunuyor ve DOT eligibility şartları traveler choice'a göre değişiyor. Evidence-only scope güvenli ama value capture düşük; bu nedenle park.

## Standard neden tamamlanmadi?

Metodoloji Standard/Deep için top-5 rakibin her birinde hedef 30/minimum 15, yıldız katmanlı ve son-12-ay review mining ister. Dog ve Card alanındaki en yakın yeni rakiplerin bir kısmında kamuya açık review sayısı bu tabanın altında. Review'u olan daha uzak substitute'ları seçerek protokolü yapay biçimde “geçmiş” göstermek selection bias yaratırdı.

Bu nedenle:

- altı fikir geçerli v4 Quick Scan olarak tamamlandı;
- Dog ve Card için top-10 competitor ve erişilebilen review sinyali eklendi;
- çıktı **Standard öncesi derinleştirme** olarak etiketlendi;
- insan deneyi yapılmadığı için tüm adaylar `PREBUILD_PENDING` kaldı.

## Onerilen test sirasi ve butce kapisi

| Sira | Fikir | Teklif | Sure | Birincil success | Stop |
|---:|---|---|---|---|---|
| 1 | Dog Rehab | 8 clinic × $49 paid concierge | 3 hafta | ≥4 pay; ≥30 valid clips; ≥3 therapist actions | Herhangi biri altı |
| 2 | Card Custody | 10 sellers × $19 | 2 hafta | ≥5 pay; ≥50 packets; buyer/dispute use | Herhangi biri altı |
| 3 | Tox Motion | 12 users × $10 prepay | 8 hafta | ≥6 prepay; ≥4 W4 completion; ≥3 provider use | Herhangi biri altı |
| 4 | Claim Kit | 20 cases × $9 | 4–6 hafta | ≥8 pay; ≥6 early completion; ≥4 accepted packets | Herhangi biri altı |
| 5 | RefundLoop | 30 users × $5 deposit | 4 hafta | Existing-tool replacement | <8 deposit veya <4 replacement |
| 6 | Trip Evidence | 20 cases × $9 | 4–6 hafta | ≥6 pay; ≥3 real claim use | Herhangi biri altı |

İlk test fail olursa otomatik olarak ikinci fikri build etmeyiz; onun da kendi paid behavior gate'i vardır.

## Kaynak ve veri sinirlari

- App Store fiyat/rating/feature'ları `E2/supporting`; revenue ve retention değildir.
- Vendor sayfalarındaki AI/accuracy/outcome iddiaları bağımsız doğrulanmadı.
- Public review sample self-selected ve bazı app'lerde RSS erişimi eksik.
- NRF/ASPS gibi büyük aggregate sayılar hedef iPhone segmentini izole etmiyor.
- Legal/medical/insurance yorumları scope guardrail'idir; hukuk veya tıp tavsiyesi değildir.
- Fırsat skorları karar modeli girdisidir, forecast değildir.

## Kanit paketleri

- [Dog Rehab Capture](2026-07-15-us-dog-rehab-capture/REPORT.md)
- [Card Condition & Custody](2026-07-15-us-card-condition-custody/REPORT.md)
- [Tox Motion Passport](2026-07-15-us-tox-motion-passport/REPORT.md)
- [RefundLoop](2026-07-15-us-refund-loop/REPORT.md)
- [Package Damage Claim Kit](2026-07-15-us-package-damage-claim-kit/REPORT.md)
- [Trip Disruption Evidence](2026-07-15-us-trip-disruption-evidence/REPORT.md)
- [Reproducible scoring notebook](2026-07-15-us-ios-mobile-native-detailed-report/analysis/scoring.ipynb)

## Nihai tavsiye

Arayüz veya MVP tasarımına geçmeden önce Dog Rehab için $49 clinic pilotunu çalıştır. İlk değer önerisi şu kadar dar olmalı:

> “Sahibin her hafta aynı videoyu doğru çekmesini sağla; terapiste karşılaştırılabilir bir follow-up paketi gönder.”

AI gait score, diagnosis, clinic integration, chat ve geniş pet-health özellikleri bu testte yok. Ödeme + owner completion + therapist action birlikte geçerse Standard araştırma ve en fazla dört ekranlık prototype scope'u hak eder.
