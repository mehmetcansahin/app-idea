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

## Sözleşme kayıtları

`pre-build-validation.md` §7 şablonunun makine-okunur karşılığı. Eşikler yukarıdaki
bölümlerden **değiştirilmeden** kopyalanmıştır; burada yeni eşik tanımlanmaz.

```text
experiment_id: before-g0-status-quo-benchmark
claim_id: before-wedge-preference
segment: 20 zor Art/DIY/home before/after çifti; insan katılımcı yok
channel_or_recruitment: Kurucunun hazırladığı corpus; beş yol (Qvyshift, DiffPix, CapCut template/manual, Edits fuse/transition, yerel alignment prototipi)
method: Aynı 20 çift beş yolda tamamlanır; her koşulda aktif görev süresi, ilk kullanılabilir 1080x1920 export, kör subject/anchor alignment tercihi, beklenmeyen crop, export failure ve paywall'a kadar tamamlanabilen görev kaydedilir
target_evidence_level: E2
sample_target: 20 çift x 5 yol = 100 görev; denominator = tamamlanan görev sayısı
metric: Median aktif süre, kör alignment tercih oranı, beklenmeyen crop ve export failure sayısı
threshold_and_derivation: Prototip median aktif sürede rakip medianından >=%30 hızlı; kör alignment tercihinde prototip >=%70 seçilir; beklenmeyen crop veya export failure en iyi rakipten kötü değil
guardrails: Sonuç pazar talebi veya WTP kanıtı değildir; yalnız "generic editörden daha iyi görev aracı" teknik iddiasını sınar
stopping_rule: Ön-benchmark kalırsa 80-pair teknik RAT'a geçilmez
pass_action: Kapı 1 teknik RAT'ını başlat
fail_action: Core wedge teknik olarak yok; scope daralt veya fikri kapat
privacy_disclosure_refund: Corpus kurucuya ait; üçüncü kişi verisi yok
owner: Kurucu
planned_dates: Kapı 1 öncesi 2-3 gün
```

```text
experiment_id: before-g1-alignment-rat
claim_id: before-autoalign-feasibility
segment: İzinli 80 gerçek before/after çifti; Art/DIY, hair/skin, home/garden ve fitness için 20'şer
channel_or_recruitment: İzinli corpus; fotoğraflar paylaşılmadan cihazda test edilebiliyorsa bu yol tercih edilir
method: Dört varyant karşılaştırılır: no-auto manual overlay baseline, Vision translation, Vision homography (yalnız statik sahne), face/body landmarks similarity transform (yalnız insan)
target_evidence_level: E2
sample_target: 80 çift, 4 varyant, 200 stress export
metric: Import başarısı, iCloud failure recovery, statik ve insan körlemesinde better/equal oranı, confident catastrophic warp, 5s 1080p export p95, crash, peak memory, metadata leak
threshold_and_derivation: Import %100; iCloud graceful recovery %100; statik blind better/equal >=%85; human blind >=%70; confident catastrophic warp <%2; export p95 eski cihazda <=15 sn, güncel cihazda <=7 sn; 200 export'ta 0 crash; peak memory <350 MB; GPS/orijinal dosya adı sızıntısı 0
guardrails: Teknik corpus segment ödeme sonucuyla birleştirilmez; yalnız algoritma robustness'ı ölçülür
stopping_rule: Statik <%85, catastrophic warp >=%2 veya crash varsa davranış testine geçilmez
pass_action: Kapı 2 Art/DIY davranış ve ödeme deneyini başlat
fail_action: Statik geçer insan kalırsa scope Art/DIY/home; homography güvensizse translation/similarity + manual overlay; manual fallback ile süre düşmüyorsa core wedge çöker
privacy_disclosure_refund: Fotoğraflar cihazda test edilir; corpus sahibine izin ve silme koşulu yazılı bildirilir
owner: Kurucu
planned_dates: 5 gün
```

```text
experiment_id: before-e1-artdiy-behavior-deposit
claim_id: before-paid-demand
segment: Son 90 günde en az iki Art/DIY projesi tamamlamış, her proje için gerçek before/after çifti olan 12 ABD'li iPhone kullanıcısı; yalnız Art/DIY arm'ı
channel_or_recruitment: Art/DIY toplulukları; professional tester ve arkadaş kolaylık örneklemi ayrı source etiketiyle tutulur, mümkünse dışarıda bırakılır
method: Her kişi bir pair'i mevcut yöntemiyle, diğerini prototiple yapar; sıra 6/6 dengelenir ve pair zorluğu kör kodlanır. Görevden önce $9.99 lifetime fiyatı gösterilir, ayrı ödeme sayfasında $5 iade edilebilir founding-license depozitosu alınır. 14 gün içinde ikinci farklı pair ile tekrar izlenir
target_evidence_level: E3
sample_target: 12 kişi, kişi başı 2 pair
metric: İki dakikada export, gerçek save/share/proje kullanımı, $5 depozito, ikinci pair ile tekrar, auto-align retained oranı, refund oranı, medyan görev süresi, çıktı kalitesi tercihi
threshold_and_derivation: Baseline ve MDE bilinmediği için exploratory/directional: >=8/12 iki dakikada export; >=6/12 gerçek kullanım; >=4/12 depozito; >=6/12 14 günde ikinci pair; export'ların >=%70'inde auto-align retained; refund <=%20; medyan prototip süresi kullanıcının kendi baseline'ından kısa; çoğunluk çıktı kalitesinde prototipi tercih eder
guardrails: TestFlight IAP sandbox gerçek ödeme değildir; waitlist E1'dir. Depozito prototip erişiminin şartı değildir. Share sheet açılması gerçek paylaşım sayılmaz. Fotoğraflar araştırmacı sunucusuna yüklenmez; filename, GPS, image hash ve face/body verisi tutulmaz
stopping_rule: <8 hızlı export, <6 gerçek kullanım, <4 depozito, <6 tekrar veya çoğunluk status quo'yu seçerse scope genişletilmez
pass_action: TESTE_DEVAM; hair/beauty professional için ayrı WTP arm'ı ve gerçek Apple Ads exact-match testi açılır
fail_action: Kullanım/süre geçer depozito kalırsa professional veya manual-first use case ayrı sözleşmeyle test edilir; sonuçlar birleştirilmez
privacy_disclosure_refund: Ürünün hazır olmadığı, refund süreci ve teslimat koşulu açık yazılır; toplanan event listesi bildirilir
owner: Kurucu
planned_dates: 14 gün (1-3 recruitment, 4-6 görevler, 7-10 doğrulama, 11-13 tekrar, 14 depozito/karar kapanışı)
```

