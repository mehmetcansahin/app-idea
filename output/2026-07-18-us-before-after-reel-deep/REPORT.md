# US Before/After Reel — Deep Analysis

**Tarih:** 2026-07-18  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** Consumer Utility  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kayıtlar: [kanıt defteri](data/evidence-ledger.md) · [assessment](data/assessment.json) · [ham arama protokolü](data/raw-search-results.md)

## Sonuç

**Genel “Before/After Reel” fikri build-ready değil.** Quick Scan'deki 42/60/80 skor, Deep araştırmada **28/48/66**'ya indi. Genişletilmiş taramada seçilmiş **15 doğrudan app, 14 alignment/progress komşusu ve 7 genel editör ikamesi** incelendi. Qvyshift iki fotoğrafı offline videoya çevirip $3.99 one-time sunuyor; DiffPix 1080p slider Reel üretiyor; Momentum 9:16, GIF, template ve müziği birleştiriyor; Body Tracker ve Metamorph ise auto-align vaat ediyor. Böylece privacy, ghost overlay, timelapse, vertical export ve şeffaf fiyatın hiçbiri tek başına boşluk değil.

Yine de küçük ve ucuz bir teste değer tek tez kaldı:

> Kullanıcı camera roll'undaki iki gerçek fotoğrafı seçer; uygulama insanı veya nesneyi yanıltıcı biçimde bükmeden hizalar ve iki dakikadan kısa sürede tam-kadraj, yüksek kaliteli 9:16 dönüşüm videosu üretir.

Bu, progress tracker değil **import-first registration utility** olmalıdır. İncelediğimiz direct listing'lerde açıkça reklamı yapılmayan dar iş, camera roll'daki iki eski ve uyumsuz fotoğrafı otomatik subject/anchor hizalama ile hazırlamaktır. Fark; **ölçülebilir hizalama kalitesi + confidence gate + manual fallback + kırpma sürprizi olmayan 1080p export** kombinasyonudur. One-time fiyat güven tercihi olabilir, fakat $3.99 direct rakip nedeniyle moat değildir.

## Neden hâlâ teste değer?

- Üç yerleşik doğrudan rakip 2K+ US rating gösteriyor; bu, before/after compare işinin tek uygulamaya özgü olmadığını destekliyor. Rating gelir veya retention değildir.
- Seçilmiş direct kümedeki yedi 2025–2026 girişinin altısı görünür rating taşımıyor; kategori arzının canlı fakat yeni ürün dağıtımının belirsiz olduğunu gösteriyor.
- Erişilebilen küçük ve negatif review örnekleminde alignment/zoom, full-frame, resolution, crash ve paywall/cancellation sorunları doğrudan geçiyor.
- Direct iki-photo app'lerde advertised automatic subject alignment gözlenmezken tracker komşularında var; bu, “tracker karmaşıklığı olmadan import alignment” için test edilebilir bir seam bırakıyor.
- `before after video` ve `progress photo` Apple public Search API'de doğru iş ailesine gidiyor; ancak Search Popularity ve conversion olmadan hacim iddiası yapılamaz.
- Apple'ın PhotosPicker, Vision ve AVFoundation API'leri cihaz-içi MVP'yi mümkün kılıyor; gerçek dönüşüm çiftlerinde doğruluk ve eski cihaz performansı ölçülmedi.

## Neden hemen build etmemeliyiz?

- Exact-feature girişleri eski wedge'i kapatıyor; CapCut doğrudan Before & After template sunuyor, Edits ise ücretsiz 4K/no-watermark baseline oluşturuyor.
- Qvyshift'in $3.99 one-time teklifi ve DiffPix'in 1080p Reel'i, price/privacy/export iddialarını farklılaştırıcı olmaktan çıkarıyor.
- Son 12 ay review protokolü yalnız 11 yazılı review'a erişti; pozitif gain katmanı yoktu. Bu “pozitif kullanıcı yok” değil, veri açığıdır.
- Rakip fiyatları gerçek satın alma değildir; haftalık fiyatlara yönelik görünür sürtünme vardır.
- $9.99 lifetime senaryosunda base paid-CPI tavanı support sonrası yaklaşık $0.31/install'dır. Paid acquisition ana büyüme motoru olamaz.
- Apple Ads Search Popularity 1–5 ve exact-query conversion yoktur.

## Skor

| Boyut | Low | Base | High | Ana gerekçe |
|---|---:|---:|---:|---|
| Problem / talep | 2 | 3 | 4 | Yerleşik rating proxy'leri ve doğrudan consistency job'ları var; ürün-spesifik davranış yok |
| Monetizasyon / ekonomi | 1 | 2 | 3 | Çok sayıda fiyat mimarisi var; satış bilinmiyor, paywall şikâyeti yüksek |
| Rekabet / wedge | 1 | 2 | 3 | Alignment/export pain gözleniyor; exact-feature entrant'lar farkı daraltıyor |
| Dağıtım | 1 | 2 | 3 | Relevant keyword ve content channel var; hacim/CPI/conversion yok |
| Tekrar değeri | 2 | 3 | 4 | Progress timeline doğal tekrar job'ı; first-party cohort yok |
| Zamanlama | 2 | 3 | 3 | 2025–2026 girişleri kategori canlılığını ve copycat hızını birlikte gösteriyor |

**Fırsat Çekiciliği:** **28 / 48 / 66 — borderline**  
**Kanıt Gücü:** **C**  
**Masa başı karar:** **TESTE_DEGER**; build veya scale izni değildir.

## Pazar ve rekabet resmi

Rekabet dört katmanlıdır:

1. **Yerleşik demand proxy'leri:** Photo Compare (2,580 rating), Instant Watermark (2,218) ve Before and after compare (2,074). Bunlar iş ailesinin geçmişini gösterir; install/revenue değildir ve ikisi uzun süredir güncellenmemiştir.
2. **Yeni direct Reel maker'lar:** Qvyshift, DiffPix, Momentum, CompareKit, Reveal ve Before After Before-After; slider/wipe, 9:16, template, music, branding, local ve farklı fiyat modellerini dolduruyor.
3. **Alignment/progress komşuları:** PhotoJourney, Metamorph, Body Tracker, Then & Now, MatchFrame, Progress AI ve Lapsey; auto-align/ghost/guide, timeline ve timelapse kombinasyonlarını sunuyor.
4. **Status quo editörleri:** CapCut'ın dedicated Before & After template'i, Edits'in ücretsiz 4K/no-watermark export'u, Instagram Align ve InShot/Canva/VN/Adobe Express'in genel workflow'ları yeni app için geçiş maliyeti yaratıyor.

Seçilmiş direct kümede 15 app var; yedisi 2025 veya sonrasında yayınlandı. Yeni yedinin altısı görünür US rating taşımıyor, biri yalnız bir rating taşıyor. Bu arz ve copy speed sinyalidir; sıfır kullanıcı veya sıfır revenue kanıtı değildir.

Solo geliştiricinin rekabet edebileceği daha küçük ürün:

- Camera-roll import ile başlar; yeni fotoğraf çekmeye veya timeline kurmaya zorlamaz.
- İlk sürümde yalnız iki fotoğraf kullanır; tracker, template marketplace veya video editor olmaz.
- Subject/anchor türünü seçer; statik sahnede translation/homography, insanlarda yalnız similarity transform kullanır.
- Güven düşükse otomatiği reddeder; opacity overlay + pinch/drag/rotate ile geri alınabilir kontrol verir.
- Orijinal kadrajın ne kadarının korunacağını export öncesinde açıkça gösterir.
- 1080×1920, 4–6 saniye, H.264/MP4; slider, fade ve hard cut üretir.
- Hesap, backend, bulut, reklam SDK'sı, müzik ve generative transition içermez.

Bu scope bile ancak aynı zor fotoğraf çiftlerinde Qvyshift, DiffPix, CapCut ve Edits'ten daha hızlı ve daha iyi hizalanmış sonuç verirse anlamlıdır.

Rakip ayrıntıları: [Genişletilmiş Faz 2](phases/02-competitor-analysis.md) · [expanded data](data/competitor-expanded.json) · [canonical liste](data/competitors.json)

## Review mining

Top five için Apple Customer Reviews RSS sayfa 1–10, 2025-07-18–2026-07-18 aralığında tarandı. All-time 322 benzersiz written review erişilebildi; son 12 ayda yalnız **11** review vardı ve tamamı 1–2 yıldızdı. Hedeflenen app başına 10 düşük, 5 orta, 10 yüksek yıldız katmanı karşılanmadı.

Erişilen 11 review içinde çoklu kodla:

- Monetization friction: 7
- Eksik kontrol/source erişimi: 4
- Export/framing/resolution: 2
- Crash/stability: 2
- UX complexity: 2
- Support/cancellation: 2

Bu sayılar yalnız örneklem içindir; pazar yüzdesi değildir. Pozitif gain `not_found_after_protocol` durumundadır.

Review ayrıntıları: [Faz 3](phases/03-review-mining.md) · [review-sample.json](data/review-sample.json)

## ASO ve acquisition

En iyi metadata kesişimi:

- Primary: `before after video`, `before and after video`, `progress photo(s)`, `progress photo tracker`, `progress pics`
- Secondary: `photo comparison`, `hair growth tracker/timelapse`, `fitness progress tracker`, `body progress photos`
- Kaçınılacak: `transformation video`, `glow up video`, broad `progress video`

`before after reel` semantic olarak ilgili sonuçlar getiriyor fakat exact-title kullanımı yok ve hacmi bilinmiyor. Bu yüzden creative copy olabilir; “hacimli keyword” diye sunulmamalı.

Metadata hipotezi:

- Name: `Progress Reel: Before & After` (29 karakter)
- Subtitle: `Align Photos Into Timelapses` (28 karakter)
- Keyword field: `video,maker,compare,tracker,pics,fitness,body,hair,growth,renovation,home,journey`

Search Popularity export'u geldikten sonra exact-match doğrulama gerekir. Ayrıntı: [Faz 8](phases/08-aso-research.md).

## Segment kararı

| Segment | Teknik uyum | Privacy/policy | Tekrar/paylaşım | Ödeme ihtimali | Rol |
|---|---|---|---|---|---|
| Art/DIY | En iyi; statik anchor | Düşük risk | Hazır proje çiftleri bulunabilir | Düşük–orta | **İlk teknik + davranış testi** |
| Hair/beauty professional | Orta; face similarity | Consent/claim riski | Müşteri kanıtı tekrarlı | Orta–yüksek hipotez | İkinci, ayrı WTP testi |
| Home/garden | Orta–yüksek | Düşük–orta | Proje döngüsü yavaş | Orta hipotez | Channel creative |
| Fitness | Orta–düşük; poz farkı | Hassas beden verisi | Motivasyon var, paylaşım seçici | Orta hipotez | İlk test değil |

ASO'da fitness/hair kelimeleri daha görünür olsa da ilk davranış testini Art/DIY seçmenin amacı teknik gerçeği düşük privacy ve düşük distortion riskiyle ölçmektir. Segmentler aynı örneklemde karıştırılmayacaktır. Art/DIY geçerse hair/beauty professional için ayrı ödeme deneyi açılır.

## Dört ekran / üç özellik scope

**Ekranlar:** Pick Pair → Align → Preview → Export/Pay.

**Ana özellikler:**

1. Dürüst, segment-aware auto-align + manual fallback.
2. Slider, fade ve hard cut preview.
3. Local, full-frame 1080p export ve share.

**Kapsam dışı:** kamera capture, project history, 2+ foto timeline, cloud/account, müzik, AI generation/restoration, 4K/GIF, body/skin ölçümü, sosyal feed.

## Teknik RAT

Build öncesi beş günlük RAT, izinli **80 gerçek çift** kullanır: Art/DIY, hair/skin, home/garden ve fitness için 20'şer. Bu teknik corpus segment kararı üretmez; yalnız algoritma sınırını ölçer.

İlk 20 zor çiftte prototip ayrıca Qvyshift, DiffPix, CapCut ve Edits ile aynı görev üzerinden benchmark edilir. “Daha hızlı ve daha güvenilir” tezi için yönsel kapı: kullanılabilir 1080×1920 export'a aktif sürede rakip medianından en az %30 daha hızlı olmak ve kör alignment tercihinde en az %70 seçilmek. Bu eşikler küçük teknik benchmark içindir; pazar tercihi veya WTP kanıtı değildir.

Geçiş eşikleri:

- Local JPEG/PNG/HEIC import: %100; iCloud hatası crash değil anlaşılır recovery.
- Statik çiftlerde kör değerlendirmede auto-align manuel başlangıçtan daha iyi/eşit: ≥%85.
- İnsan çiftlerinde: ≥%70.
- Yanlış fakat yüksek güvenli catastrophic warp: <%2.
- Beş saniye 1080p export p95: eski cihaz ≤15 sn, güncel cihaz ≤7 sn.
- 200 export: 0 crash; peak memory <350 MB.
- Export metadata: GPS/orijinal filename yok.

Statik pass, insan fail olursa yalnız Art/DIY/home scope'uyla devam edilir. Ayrıntı: [Faz 7](phases/07-feature-matrix.md).

## Finans

İlk offer hipotezi: bir watermark'lı export ücretsiz, **$9.99 lifetime** unlock. Bu fiyat artık “rakiplerden ucuz” değildir: Qvyshift $3.99 one-time, Lapsey $9.99 one-time, Edits ücretsiz ve CapCut free-tier status quo sunuyor. Küçük pre-build örneklemde fiyat A/B yapılmayacak; $9.99 sabit tutularak gerçek para riski ölçülecek. Haftalık subscription önerilmiyor. Subscription ancak ücretli kullanıcıların ≥%30'u D30'da ikinci proje yapar ve profesyoneller aylık ≥3 export üretirse yeniden test edilir.

| Senaryo | Aylık install | Conversion | Proceeds | Paid spend | Support | Katkı |
|---|---:|---:|---:|---:|---:|---:|
| Low | 1,000 | %2 | $156 | $1,000 | $16 | **-$860** |
| Base | 10,000 | %4 | $3,227 | $3,000 | $150 | **+$77** |
| High | 50,000 | %6 | $24,710 | $6,250 | $540 | **+$17,920** |

Bunlar benchmark veya forecast değildir; $9.99, %15 Apple komisyonu, organic/paid mix, CPI, conversion ve refund varsayımlarıdır. Ana çıkarım: ekonomi **organik ASO/share loop'a bağımlıdır**. Ayrıntı: [Faz 9](phases/09-financial-model.md).

## Bir sonraki gerçek davranış testi

Teknik RAT geçerse, yalnız Art/DIY segmentinde 12 ABD'li kullanıcı:

- İki ayrı gerçek before/after çifti ve önümüzdeki 7 günde kullanma/paylaşma niyetiyle alınır.
- Bir çifti mevcut yöntemiyle, bir çifti çalışan prototiple tamamlar; sıra dengelenir.
- $9.99 gelecek lifetime fiyatı açıkça gösterilir; **$5 iade edilebilir founding-license depozitosu** gerçek ödeme mekanizmasıdır.
- TestFlight sandbox satın alması ödeme kanıtı sayılmaz.

Yönsel geçiş: ≥8/12 iki dakikada export, ≥6/12 gerçek save/share/projede kullanım, ≥4/12 depozito, ≥6/12 14 günde ikinci farklı çift, auto-align sonucu ≥%70 korunma, refund ≤%20.

Baseline/MDE yoktur; sonuç en fazla C kanıt gücü üretir ve tek başına `BUILD_SMALL` izni vermez. Ayrıntı: [Faz 6](phases/06-prebuild-plan.md).

## Fatal gate ve riskler

Dört fatal gate masa başında `clear`: genel yasal engel gözlenmedi, PhotosPicker/AVFoundation erişimi var, cihaz-içi teknik yol mevcut ve non-rigid human warp/health claims scope dışı. Bu “risksiz” demek değildir; gerçek binary, algoritma ve metadata tekrar denetlenmelidir.

En büyük üç belirsizlik:

1. Kullanıcı generic editör yerine dar akışı gerçekten tercih edecek mi? — C
2. Şeffaf $9.99 lifetime için gerçek para riske edecek mi? — C
3. Search/creator kanalları solo geliştiriciye yeterli qualified task getirecek mi? — C

## Kanıt sınırları

- Apple Search Popularity, exact-query volume ve query conversion yok.
- Rakip install, revenue, retention ve paid conversion yok.
- Review minimumları karşılanmadı; pozitif gains gözlenemedi.
- Finance tablosu first-party veri değil senaryodur.
- Technical RAT, depozito, export/share ve ikinci kullanım henüz yürütülmedi.
- Share sheet açılması gerçek paylaşım değildir; mümkünse kullanıcı sonucu hedef kanalda göstermelidir.

Bu nedenle doğru karar **TESTE_DEGER / PREBUILD_PENDING**; genel ürünü geliştirmeye başlamak değil, dar tezin önce teknik ve sonra davranış testini yapmaktır.

## Faz dosyaları

- [01 Market Scan](phases/01-market-scan.md)
- [02 Competitor Analysis](phases/02-competitor-analysis.md)
- [03 Review Mining](phases/03-review-mining.md)
- [04 Scoring](phases/04-scoring.md)
- [05 Validation](phases/05-validation.md)
- [06 Pre-build Plan](phases/06-prebuild-plan.md)
- [07 Feature Matrix](phases/07-feature-matrix.md)
- [08 ASO Research](phases/08-aso-research.md)
- [09 Financial Model](phases/09-financial-model.md)
- [10 Conditional Project Brief](phases/10-project-brief.md)
- [11 Devil's Advocate](phases/11-devils-advocate.md)
