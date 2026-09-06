# Faz 5.5 / 6 — Pre-build Validation Plan

Bu plan iki kapılıdır. Teknik kapı geçmeden kullanıcı ödeme testine başlanmaz.

## Teknik ön-benchmark — “yeni app indirmeye değer mi?”

80-pair robustness RAT'ından önce aynı 20 zor Art/DIY/home çifti şu beş yolda tamamlanır:

1. Qvyshift Before & After Video Maker
2. DiffPix
3. CapCut Before & After template/manual flow
4. Edits Fuse/transition flow
5. Yerel alignment prototipi

Her koşulda aktif görev süresi, ilk kullanılabilir 1080×1920 export, kör subject/anchor alignment tercihi, beklenmeyen crop, export failure ve paywall'a kadar tamamlanabilen görev kaydedilir. Yönsel geçiş:

- Prototip median aktif sürede rakip medianından en az %30 hızlı.
- Kör alignment tercihinde prototip en az %70 seçilir.
- Beklenmeyen crop veya export failure, en iyi rakipten kötü değildir.

Bu ön-benchmark kalırsa 80-pair RAT'a geçilmez. Sonuç pazar talebi veya WTP kanıtı değildir; yalnız “generic editörden daha iyi görev aracı” teknik iddiasını sınar.

## Kapı 1 — Beş günlük teknik RAT

### En riskli teknik iddia

“Gerçek before/after çiftlerinde otomatik hizalama, manuel başlangıçtan daha hızlı ve görsel olarak güvenilir olur; insanı veya sonucu yanıltıcı biçimde bozmaz.”

### Corpus

- İzinli 80 gerçek çift.
- Art/DIY, hair/skin, home/garden ve fitness için 20'şer.
- Farklı iPhone source, aspect ratio, ışık ve crop örnekleri.
- Fotoğraflar paylaşılmadan cihazda test edilebiliyorsa bu yol tercih edilir.

Teknik corpus segment ödeme sonucunu birleştirmez; yalnız algoritma robustness'ını ölçer.

### Varyantlar

1. No-auto, manual overlay baseline.
2. Vision translation.
3. Vision homography — yalnız statik sahne.
4. Face/body landmarks similarity transform — yalnız insan.

### Pre-registered teknik eşikler

| Ölçüm | Geçiş |
|---|---:|
| Local JPEG/PNG/HEIC import | %100 |
| iCloud failure graceful recovery | %100 |
| Static blind better/equal vs manual start | ≥%85 |
| Human blind better/equal | ≥%70 |
| Confident catastrophic warp | <%2 |
| 5s 1080p export p95 old device | ≤15 sn |
| 5s 1080p export p95 current device | ≤7 sn |
| Stress export | 200'de 0 crash |
| Peak memory | <350 MB |
| GPS/original filename leak | 0 |

### Teknik durdurma/pivot

- Static <85%, catastrophic warp ≥2% veya crash varsa davranış testine geçme.
- Static pass, human fail: Art/DIY/home scope; hair/fitness auto-align'ı çıkar.
- Homography güvensiz: translation/similarity + manual overlay.
- Manual fallback ile görev süresi düşmüyorsa core wedge çöker.

## Kapı 2 — Tek segmentli gerçek davranış ve ödeme deneyi

### Segment

İlk arm yalnız **Art/DIY**. Katılımcıların iki ayrı tamamlanmış proje çifti olmalıdır; farklı segmentler karıştırılmaz.

Art/DIY seçilme nedeni:

- Statik geometri teknik iddiayı en adil biçimde ölçer.
- Sensitive body/face privacy riski düşüktür.
- İki eski pair ile 14 günlük tekrar davranışı beklenebilir.
- Ödeme sinyali zayıf kalırsa hair/beauty professionals için yeni ve ayrı sözleşme gerekir; sonuçlar birleştirilmez.

### Karar sorusu

“Hazır Art/DIY before/after çifti olan kullanıcı, CapCut/Canva/manual crop yerine bu hizalanmış Reel akışını seçip $9.99 lifetime değerine gerçek para riske eder mi?”

### En riskli varsayım

Auto-align + manual fallback, mevcut yönteme kıyasla iki dakikadan kısa güvenilir export ve gerçek save/share üretir; kullanıcı bunu $9.99 değerinde görür.

### Katılımcı ve baseline

- 12 US iPhone kullanıcısı.
- Son 90 günde en az iki Art/DIY projesi tamamlamış.
- Her proje için gerçek before/after çifti var.
- Önümüzdeki yedi günde sonucu paylaşma, portföyde kullanma veya müşteriye gösterme niyeti var.
- Professional tester/arkadaş kolaylık örneklemi ayrı source etiketiyle tutulur; mümkünse dışarıda bırakılır.

Her kişi bir pair'i mevcut yöntemiyle, diğer pair'i prototiple yapar. Sıra 6/6 dengelenir. Pair zorluğu kör kodlanır; prototype pair'in sistematik olarak kolay olmaması kontrol edilir.

### Prototip

- Pick Pair.
- Auto/manual align.
- Slider/fade/cut preview.
- 1080p save/share.
- Sandbox paywall görünümü.

TestFlight IAP sandbox gerçek ödeme değildir.

### Gerçek ödeme mekanizması

- Gelecekteki $9.99 lifetime fiyatı görevden önce açıkça gösterilir.
- $5 **iade edilebilir founding-license depozitosu** ayrı ödeme sayfasında alınır.
- Depozito prototip erişiminin zorunlu şartı değildir; payer ve non-payer görevi tamamlayabilir.
- Refund süreci ve teslimat koşulu açık yazılır.
- Waitlist E1; depozito gerçek para riski taşıdığı için E3 davranış sinyalidir, production IAP değildir.

### Veri minimization

- Fotoğraflar araştırmacının sunucusuna yüklenmez.
- Event'ler: qualified, deposit paid/refunded, import, auto retained/manual override, export, verified real use/share, second distinct pair.
- Filename, GPS, image hash, landmark, face/body data tutulmaz.
- Share sheet açılması tek başına gerçek paylaşım sayılmaz; hedefte sonuç veya gerçek kullanım bağlamı doğrulanır.

### Plan

| Gün | İş |
|---|---|
| 1–3 | Recruitment ve pair qualification |
| 4–6 | Baseline + prototype task, dengeli sıra |
| 7–10 | Gerçek save/share/use doğrulama, friction görüşmesi |
| 11–13 | İkinci farklı pair ile tekrar |
| 14 | Deposit/refund ve karar kapanışı |

### Yönsel eşikler

Baseline ve MDE bilinmediği için bu eşikler exploratory/directional'dır:

- ≥8/12 prototype task'i iki dakikada export.
- ≥6/12 gerçek save/share/proje/müşteri kullanımı.
- ≥4/12 $5 depozito.
- ≥6/12 ikinci farklı pair ile 14 günde tekrar.
- Export'ların ≥%70'inde auto-align sonucu retained.
- Refund ≤%20.
- Medyan prototype task time, aynı kullanıcı baseline'ından daha kısa.
- Çoğunluk outcome quality'de prototipi tercih eder.

### Karar

- **TESTE_DEVAM:** Tüm yönsel eşikler geçer; hair/beauty professional için ayrı WTP arm'ı ve gerçek Apple Ads exact-match testi aç.
- **PIVOT:** Kullanım/time geçer, depozito kalır; professional veya manual-first use case'i ayrı test et.
- **KILL/PARK:** <8 hızlı export, <6 gerçek kullanım, <4 depozito, <6 repeat veya çoğunluk status quo'yu seçerse scope genişletme.

Bu tek deney, opportunity low 28 ve evidence C iken `BUILD_SMALL` veremez. BUILD_SMALL için yeniden assessment, low ≥60, B+ top-risk evidence ve product-specific E3 davranış gerekir.
