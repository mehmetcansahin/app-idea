# Faz 5.5 — Occasion Reel Deney Sözleşmesi

**Fikir:** `us-occasion-reel` · **Masa başı kararı:** TESTE_DEGER · **Durum:** PREBUILD_PENDING
**Metodoloji:** v4.0 · **Sözleşme tarihi:** 2026-09-07
**Kaynak assessment:** [`data/assessment.json`](../data/assessment.json) · **Kanıt:** [`data/evidence-ledger.md`](../data/evidence-ledger.md)

Bu dosya deney tasarımıdır; sonuç kaydı değildir. Hiçbir eşik burada "geçmiş"
sayılamaz. Deney insan tarafından yürütülür; sonuçlar `data/evidence.jsonl` ve
`data/assessment.json` içine işlenmeden `status` değişmez.

## 1. Giriş koşulu kontrolü

| Koşul | Durum |
|---|---|
| Faz 5 kararı `TESTE_DEGER` veya `TEST_ONCELIKLI` | ✅ `TESTE_DEGER` |
| Dört fatal gate `blocked` değil | ✅ dördü `clear` |
| Genel Kanıt Gücü D değil | ✅ `C` |

Giriş koşulu karşılanıyor, plan üretilebilir.

## 2. RAT sıralaması

Assessment üç varsayımı da `impact 3 × uncertainty 3 = 9` ile eşit veriyor. Eşitlik
`pre-build-validation.md` §2 kuralıyla çözülür: önce fatal olma potansiyeli, sonra en
düşük test maliyeti.

| Sıra | claim_id | Risk sınıfı | Neden bu sırada | Deney |
|---|---|---|---|---|
| 1 | `occasion-wedge` | usability | Ücretsiz ikame (iMovie/Photos, CapCut/Canva) yeterliyse ürünün var olma nedeni yok; en fatal ve en ucuz gözlenebilir varsayım | E1 karşılaştırmalı görev prototipi |
| 2 | `occasion-economics` | business_viability | Wedge tercih edilse bile lifetime fiyat hipotezine gerçek para riski yoksa ekonomi yok; aynı kohortta ölçülebilir | E2 iade edilebilir preorder |
| 3 | `occasion-distribution` | distribution | Fatal olabilir fakat gerçek para/creative gerektirir ve E1/E2 kalırsa harcaması boşa gider | E3 kanal probe (koşullu) |
| — | `occasion-retention` | retention | Boyut zaten `low 1`; doğal ikinci occasion 30 günde beklenmiyor. Bu sözleşmede **test edilmiyor**, ayrı sözleşmeye ertelendi | — |

Teknik fizibilite RAT'ı yoktur: `CORE_FEASIBILITY_BLOCKED` gate'i
`occasion-local-feasibility` ile `clear`. İki günlük prototip spike'ı deneyin
maliyetidir, kanıt kapısı değildir.

## 3. Segment kilidi

İlk arm yalnız **doğum günü** occasion'ı. Gerekçe:

- En sık tekrar eden occasion; recruitment 30 günlük pencerede gerçekten mümkün.
- Anma (memorial) videosu duygusal ve `sensitive_data` açısından ayrı protokol
  gerektirir; aynı örneklemde karıştırılmaz.
- Mezuniyet ve yıldönümü mevsimsel/dar; ayrı arm olarak sonra açılır.

Segmentler karıştırılmaz; her ek occasion tipi yeni `experiment_id` ile kaydedilir.
Doğum günü fotoğrafları çocuk görüntüsü içerebildiği için `children` riski §7'deki
veri minimizasyonu ile kapatılır.

## 4. E1 — Karşılaştırmalı görev prototipi

```text
experiment_id: occ-e1-comparative-task
claim_id: occasion-wedge
segment: Önündeki 30 günde gerçek bir doğum günü olan, telefonunda 8-30 hazır fotoğrafı bulunan ABD'li iPhone kullanıcısı
channel_or_recruitment: Yerel topluluk grupları ve occasion planlama toplulukları; profesyonel tester ve arkadaş kolaylık örneklemi ayrı source etiketiyle tutulur, mümkünse dışarıda bırakılır
method: Within-subject karşılaştırmalı görev; iki farklı fotoğraf seti (biri yaklaşan gerçek doğum günü, biri en az 6 ay önceki bir occasion), sıra 6/6 dengelenir. Bir set kullanıcının mevcut yöntemiyle (iMovie/Photos/CapCut/Canva - kendi seçimi), diğeri prototiple yapılır
target_evidence_level: E2
sample_target: 12 kişi, iki turda; Tur 1 = 6 kişi problem ve geçmiş davranış, Tur 2 = 6 kişi yeni yüksek etkili tema ve karşıt örnek kontrolü. Güç hesabı yok; hedef tema doygunluğu
metric: Ana metrik = ilk paylaşılabilir export'a kadar aktif görev süresi ve tamamlanan export. İkincil = kör çıktı kalitesi tercihi (kendi yöntemi vs prototip), otomatik kompozisyonun elde tutulma oranı, kesintiden sonra devam edebilme
threshold_and_derivation: Popülasyon baseline'ı ve MDE bilinmiyor; baseline her katılımcının kendi yöntemiyle ölçülen süresidir. Bu nedenle eşikler exploratory/directional: >=8/12 prototiple beş dakikada export; >=6/12 videoyu gerçekten paylaşır; medyan prototip süresi aynı kullanıcının kendi baseline'ından kısa; kör kalite tercihinde çoğunluk prototipi seçer; export'ların >=%70'inde otomatik kompozisyon elde tutulur
guardrails: Fotoğraf araştırmacı sunucusuna yüklenmez; cihazda çalışılır. İkinci görevde öğrenme etkisi sınırlama olarak kaydedilir. Prototip setinin sistematik olarak kolay olmadığı kör kodlamayla kontrol edilir. Crash veya export hatası guardrail ihlalidir
stopping_rule: <8/12 beş dakikada export veya <6/12 gerçek paylaşım ya da çoğunluk kendi mevcut yöntemini tercih ederse E2'ye geçilmez; fikir park edilir
pass_action: E2'yi aynı kohortta çalıştır
fail_action: Wedge çöktü. Ücretsiz ikame yeterli demektir; occasion otomasyonu yerine kullanıcıların adlandırdığı tek somut friction'a (proje kaybı, export başarısızlığı) daralt veya fikri kapat
privacy_disclosure_refund: Ürünün hazır olmadığı, prototipin araştırma amaçlı olduğu, hangi event'lerin tutulduğu ve fotoğrafların saklanmadığı yazılı olarak açıklanır
owner: Kurucu (tek geliştirici)
planned_dates: Recruitment 3 gün, görevler 5 gün, paylaşım doğrulaması ve friction görüşmesi 4 gün
```

Prototip sınırı solo MVP sınırıyla aynıdır: Occasion seçimi, Photo Picker,
Preview/Edit, Export. Paywall yalnız görünüm olarak bulunur; TestFlight IAP sandbox
gerçek ödeme sayılmaz.

## 5. E2 — İade edilebilir preorder

```text
experiment_id: occ-e2-refundable-preorder
claim_id: occasion-economics
segment: E1'i tamamlayan aynı 12 kişilik doğum günü kohortu
channel_or_recruitment: E1 kohortu; ek recruitment yok
method: Görevden önce gelecek $9.99-$14.99 lifetime fiyatı açıkça gösterilir; görevden sonra ayrı ödeme sayfasında $9.99 iade edilebilir founding-license preorder'ı alınır. Preorder prototip erişiminin şartı değildir; ödeyen ve ödemeyen görevi tamamlayabilir
target_evidence_level: E3
sample_target: 12 (E1 kohortu); ek örneklem yok
metric: Ana metrik = gerçek para riske eden kişi sayısı. İkincil = 14 gün içindeki refund oranı ve fiyat itirazının gerekçesi
threshold_and_derivation: >=4/12 preorder ve refund <=%20. Bu eşik ekonomiden türetilmemiştir: Quick Scan'de finansal model yok, kanal maliyeti (CPI/CPC), hedef payback ve $9.99 lifetime'ın brüt katkısı (platform komisyonu dahil) gözlenmedi. Bu nedenle deney `exploratory`dir ve tek başına `BUILD_SMALL` üretemez
guardrails: Waitlist veya e-posta E1 seviyesindedir ve bu eşikte sayılmaz. Sandbox IAP sayılmaz. Kullanıcı kandırılmaz: teslim edilmezse tam iade, iade süresi ve iletişim yolu yazılıdır. Sosyal baskı yaratan grup ortamında ödeme istenmez
stopping_rule: <4/12 preorder veya refund >%20 ise fiyat/paket hipotezi çürüktür; E3 kanal harcaması yapılmaz
pass_action: E3 kanal probe'unu çalıştır ve occasion-economics'i E3 kaydıyla yeniden puanla
fail_action: Ücretsiz+occasion-başına ödeme veya hediye/organizatör ödeyeni gibi ayrı ödeyen hipotezini yeni experiment_id ile test et; sonuçlar birleştirilmez
privacy_disclosure_refund: Ödeme sayfasında ürünün yayınlanmadığı, tahsilat ve iade koşulları, verinin yalnız araştırma için kullanıldığı açık yazılır
owner: Kurucu
planned_dates: E1 görevleriyle aynı iki hafta; iade penceresi kapanışı 14. gün
```

## 6. E3 — Kanal probe (koşullu)

```text
experiment_id: occ-e3-channel-probe
claim_id: occasion-distribution
segment: ABD, doğum günü occasion niyeti sinyali veren kitle
channel_or_recruitment: UTM etiketli tek landing page; ücretli sosyal (occasion planlama ilgi hedeflemesi) ve occasion toplulukları. App Store'da yayınlanmış ürün olmadığı için Apple Ads exact-match testi bu aşamada çalıştırılamaz
method: 150-300 USD sınırlı harcamayla kanal-spesifik acquisition testi; dönüşüm hedefi §5'teki açıklanmış iade edilebilir preorder'dır
target_evidence_level: Talep için E1; kanal maliyeti (CPC/CPM/cost-per-preorder) için E2
sample_target: Harcama tavanı ve en az 1.000 UTM'li oturum; güç hesabı yok
metric: Ana metrik = cost per iade edilebilir preorder. İkincil = CTR, landing->payment start, mesaj varyantı farkı
threshold_and_derivation: Eşik türetilemez; hedef payback ve brüt katkı için first-party veri yok. Sonuç `directional` olarak kaydedilir ve occasion-distribution claim'ini C'nin üzerine taşımaz. Karar için kullanılan tek sayı, cost-per-preorder'ın $9.99 lifetime fiyatının üzerinde mi altında mı olduğudur
guardrails: Landing page tek başına ana test değildir ve `BUILD_SMALL` üretemez; yalnız mesaj ve kanal maliyeti öğretir. Ürünün hazır olmadığı sayfada görünür
stopping_rule: Harcama tavanı dolduğunda dur; cost-per-preorder lifetime fiyatının iki katından yüksekse kanal hipotezi kalır
pass_action: Occasion-distribution'ı ölçülen maliyetle yeniden puanla ve BUILD_SMALL ön koşullarını tekrar kontrol et
fail_action: Organik/ASO odaklı ikinci hipotez veya occasion topluluk dağıtımı ayrı experiment_id ile test edilir
privacy_disclosure_refund: E2 ile aynı açıklama metni
owner: Kurucu
planned_dates: E2 iade penceresi kapandıktan sonra 7-10 gün
```

## 7. Veri minimizasyonu ve `children` riski

- Fotoğraflar cihazda kalır; araştırmacıya yüklenmez, kopyalanmaz, hash'lenmez.
- Yüz/kişi verisi, dosya adı, GPS ve orijinal metadata toplanmaz.
- Doğum günü setleri çocuk görüntüsü içerebilir: araştırmacı hiçbir çocuk
  görüntüsünü almaz, ekran kaydı yapmaz; gözlem yalnız süre, tamamlama ve
  kullanıcının sözlü/yazılı geri bildirimidir.
- Tutulan event'ler: qualified, task start/end, export, doğrulanmış gerçek paylaşım,
  preorder paid/refunded, otomatik kompozisyon retained/override.
- Share sheet'in açılması gerçek paylaşım sayılmaz; hedefte sonucun görünmesi veya
  kullanıcının paylaşımı doğrulaması gerekir.

## 8. Karar kuralı

`scoring-model.md` build-öncesi matrisi uygulanır:

- Problem/talep E3+ ile çürütülürse → `KILL`.
- Problem B+ fakat wedge E3+ ile çürütülürse → `PIVOT`.
- `opportunity.low >= 60` + genel kanıt B+ + en riskli varsayım B+ + ürün-spesifik
  E3+ davranış → `BUILD_SMALL`.
- Diğer tüm durumlar → `TESTE_DEVAM`.

Bu sözleşme tümüyle geçse bile `BUILD_SMALL` üretmez: mevcut `opportunity.low = 46`
ve genel kanıt `C`. Build izni için yeniden assessment, `low >= 60`, en riskli
varsayımda B+ ve ürün-spesifik E3+ davranış gerekir. E1+E2 geçerse beklenen sonuç
`TESTE_DEVAM`; occasion-wedge ve occasion-economics E2/E3 kayıtlarıyla yeniden
puanlanır ve `occasion-retention` için ayrı ikinci-döngü sözleşmesi açılır.

Eşikler sonuç görüldükten sonra değiştirilmez. Değişiklik gerekirse ilgili deney
kapatılır ve yeni `experiment_id` ile yeniden kaydedilir.
