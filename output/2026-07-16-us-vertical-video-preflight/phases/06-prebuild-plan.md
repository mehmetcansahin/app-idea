# Faz 5.5 — Vertical Video Preflight Deney Sözleşmesi

**Fikir:** `us-vertical-video-preflight` · **Masa başı kararı:** TESTE_DEGER · **Durum:** PREBUILD_PENDING
**Metodoloji:** v4.0 · **Sözleşme tarihi:** 2026-09-07
**Kaynak assessment:** [`data/assessment.json`](../data/assessment.json) · **Kanıt:** [`data/evidence-ledger.md`](../data/evidence-ledger.md)

Bu dosya deney tasarımıdır; sonuç kaydı değildir. Eşikler sonuç görüldükten sonra
değiştirilmez. Sonuçlar `data/evidence.jsonl` ve `data/assessment.json` içine
işlenmeden `status` değişmez.

## 1. Giriş koşulu kontrolü

| Koşul | Durum |
|---|---|
| Faz 5 kararı `TESTE_DEGER` veya `TEST_ONCELIKLI` | ✅ `TESTE_DEGER` |
| Dört fatal gate `blocked` değil | ✅ dördü `clear` |
| Genel Kanıt Gücü D değil | ✅ `C` |

## 2. RAT sıralaması

Assessment üç varsayımı `3 × 3 = 9` ile eşitliyor; sıra `pre-build-validation.md` §2
eşitlik kuralıyla (fatal potansiyeli → test maliyeti) çözülür.

| Sıra | claim_id | Risk sınıfı | Mevcut derece | Neden bu sırada | Deney |
|---|---|---|---|---|---|
| 1 | `claim-wedge` | usability | C | Killer risk false positive: kullanıcı "intentional black frame" uyarısını sürekli reddediyorsa ürün güveni ölür. Ölçülebilir denominator'ı olan tek deney | G0 doğruluk corpus'u, sonra E1 |
| 2 | `claim-economics` | business_viability | C | Uyarılar doğru olsa bile $9.99 lifetime'a gerçek para riski yoksa ekonomi yok | E3 iade edilebilir preorder |
| 3 | `claim-demand` | value | B | Zaten B; ayrı deney açmaya değmez. Kohortun **gerçek** export'larında hakiki sorun bulunup bulunmadığı E1 içinde bedava ölçülür | E1 içinde frekans ölçümü |
| — | `claim-retention` | retention | — | Boyut low 3 / base 4; her final export doğal döngü. İkinci export dönüşü E2 olarak izlenir | E2 ikinci-export dönüşü |

Teknik fizibilite gate'i `clip-technical-vision` ve `clip-technical-codecaudit` ile
`clear`; ancak "clear" yalnız API'nin var olduğunu söylüyor, **doğruluğu** söylemez.
Bu yüzden ilk kapı bir kullanıcı deneyi değil, ölçülebilir doğruluk corpus'udur.

## 3. G0 — Doğruluk kapısı (kullanıcıdan önce)

```text
experiment_id: clip-g0-accuracy-corpus
claim_id: claim-wedge
segment: Deney kohortunun kendi export'larından ve kurucunun hazırladığı kontrollü setten oluşan video corpus'u; insan katılımcı yok
channel_or_recruitment: Corpus; 12 editörün son üçer export'u (36 gerçek dosya) + kontrollü hata enjekte edilmiş en az 24 dosya = en az 60 video
method: Prototip her videoyu cihazda tarar. Kontrollü sette bilinen sayıda black/freeze/silence, yanlış codec/aspect/duration ve UI-zone çakışması enjekte edilir; enjeksiyon kaydı kör tutulur. Clean sette hiçbir critical beklenmez. Her finding insanla doğrulanır
target_evidence_level: E2
sample_target: >=60 video, >=24 kontrollü hata; denominator bilinen enjeksiyon sayısıdır
metric: Kontrollü sorun recall'ü, clean videoda yanlış `critical` oranı, severity doğruluğu
threshold_and_derivation: Bu deneyin denominator'ı gerçek (enjekte edilen hata sayısı), bu yüzden eşik directional değil ölçülmüş orandır: recall >= %90 ve clean videoda yanlış critical <= %10. Eşikler Quick Scan'de sonuç görülmeden kaydedildi
guardrails: 9:16, <=3 dakika, MP4/MOV scope'u dışına çıkılmaz. Kullanıcı videoları buluta yüklenmez, cihazda taranır. Ürün "platform kabul garantisi" dili kullanmaz; yalnız risk uyarısı verir
stopping_rule: Recall <%90 veya yanlış critical >%10 ise editör kohortu çalıştırılmaz; wedge teknik olarak yaşamıyor demektir
pass_action: E1 editör kohortunu başlat
fail_action: Yalnız safe-zone veya yalnız metadata uygulamasına pivot etme (o alanlar kalabalık). Ya conservative severity modelini yeniden kur ya da fikri kapat
privacy_disclosure_refund: Katılımcıya videoların cihazdan çıkmadığı, hangi metriklerin tutulduğu ve corpus'un silinme zamanı yazılı bildirilir
owner: Kurucu (tek geliştirici)
planned_dates: Corpus hazırlığı 3 gün, tarama ve insan doğrulaması 4 gün
```

## 4. E1 — Gerçek export kohortu

```text
experiment_id: clip-e1-editor-cohort
claim_id: claim-wedge
segment: Haftada en az üç kısa video yayınlayan ABD'li freelance editor, social media manager veya creator-business operator; masaüstünde export edip iPhone'dan yayınlıyor
channel_or_recruitment: Editör ve creator toplulukları, freelance ağları. Arkadaş/kolaylık örneklemi ayrı source etiketiyle tutulur, mümkünse dışarıda bırakılır
method: 12 editörün her biri kendi son üç final export'unu prototipten geçirir. Her uyarı katılımcıyla birlikte doğru/yanlış ve faydalı/gürültü olarak kodlanır. Katılımcı gerçek bir düzeltme yaparsa (yeniden export, caption taşıma, codec değişimi) kaydedilir
target_evidence_level: E2
sample_target: 12 kişi, iki turda (Tur 1 = 6 problem ve mevcut iş akışı, Tur 2 = 6 yeni yüksek etkili tema ve karşıt örnek kontrolü). Güç hesabı yok; hedef tema doygunluğu
metric: Ana metrik = editör tarafından doğru ve faydalı bulunan uyarı oranı ve gerçek düzeltme sayısı. İkincil (claim-demand) = gerçek export'larda hakiki sorun bulunan kohort payı
threshold_and_derivation: Popülasyon baseline'ı yok, MDE hesaplanamaz; eşikler exploratory/directional: uyarıların >=%85'i doğru ve faydalı; >=6/12 gerçek düzeltme. claim-demand için: gerçek export'larda en az 8 hakiki sorun bulunmazsa problem frekansı B derecesini hak etmiyor demektir ve boyut yeniden puanlanır
guardrails: Mevcut iş akışı (private/draft upload + gözle izleme) ücretsiz ve gerçek ikamedir; karşılaştırma bu ikameye karşı yapılır. Dismiss edilen uyarı gürültü sayılır. Prototip editing/transkripsiyon/yayın yapmaz
stopping_rule: <%85 doğrulama, <6 gerçek düzeltme veya kohortun gerçek export'larında toplam <8 hakiki sorun varsa E2/E3'e geçme
pass_action: E2 ikinci-export dönüşünü izle, ardından E3 preorder'ı sun
fail_action: Uyarılar doğru ama faydasızsa severity/sunum problemidir, bir kez yeniden tasarla; uyarılar yanlışsa G0'a dön ve fikri kapatmayı değerlendir
privacy_disclosure_refund: Ürünün hazır olmadığı, prototipin araştırma amaçlı olduğu, videoların cihazda kaldığı ve tutulan event listesi yazılı açıklanır
owner: Kurucu
planned_dates: Recruitment 4 gün, oturumlar 6 gün
```

## 5. E2 — İkinci export dönüşü

```text
experiment_id: clip-e2-second-export
claim_id: claim-retention
segment: E1'i tamamlayan aynı 12 kişilik editör kohortu
channel_or_recruitment: E1 kohortu; ek recruitment yok
method: 14 gün boyunca hatırlatma yapılmaz. Katılımcı yeni bir final export ürettiğinde prototipe kendiliğinden dönüp dönmediği izlenir. Dönüş yalnız gerçek yeni dosya taramasıyla sayılır
target_evidence_level: E2
sample_target: 12; ek örneklem yok
metric: Ana metrik = ikinci gerçek export'ta kendiliğinden dönen kişi sayısı. İkincil = dönüş süresi ve dönmeyenlerin gerekçesi
threshold_and_derivation: Baseline yok; directional eşik >=6/12 kendiliğinden dönüş. Retention boyutu (low 3 / base 4) bu deney olmadan first-party kanıt taşımıyor
guardrails: Hatırlatma, teşvik veya ödeme dönüşü sayılmaz. Araştırmacının sorusu üzerine yapılan tarama "kendiliğinden" değildir
stopping_rule: <6/12 dönüş varsa retention boyutu düşürülür ve lifetime fiyat hipotezi tek satın alma davranışına göre yeniden kurulur
pass_action: Retention claim'ini E2 kaydıyla güncelle
fail_action: Episodik kullanım kabul edilir; abonelik hipotezi tamamen kapatılır
privacy_disclosure_refund: E1 ile aynı açıklama metni
owner: Kurucu
planned_dates: E1 bitiminden sonraki 14 gün
```

## 6. E3 — İade edilebilir preorder

```text
experiment_id: clip-e3-refundable-preorder
claim_id: claim-economics
segment: E1'i tamamlayan editör kohortu
channel_or_recruitment: E1 kohortu
method: Gelecek $9.99 lifetime fiyatı ve ilk taramanın ücretsiz olacağı açıkça gösterilir; ayrı ödeme sayfasında $9.99 iade edilebilir preorder alınır. Preorder prototip erişiminin şartı değildir
target_evidence_level: E3
sample_target: 12
metric: Ana metrik = gerçek para riske eden kişi sayısı. İkincil = 14 günlük refund oranı ve fiyat itirazının gerekçesi
threshold_and_derivation: >=4/12 preorder ve refund <=%20. Eşik ekonomiden türetilmemiştir: quick modda finansal model, kanal maliyeti ve $9.99 lifetime'ın komisyon sonrası brüt katkısı gözlenmedi. Deney `exploratory`dir ve tek başına `BUILD_SMALL` üretemez
guardrails: Waitlist/e-posta E1 seviyesidir ve sayılmaz. Sandbox IAP gerçek ödeme değildir. Teslim edilmezse tam iade, iade süresi ve iletişim yolu yazılıdır
stopping_rule: <4/12 preorder veya refund >%20 ise fiyat/paket hipotezi çürüktür; kanal harcaması yapılmaz
pass_action: claim-economics'i E3 kaydıyla yeniden puanla ve build-öncesi matrisi tekrar uygula
fail_action: Per-scan veya ajans/çoklu-hesap ödeyeni gibi ayrı ödeyen hipotezini yeni experiment_id ile test et; sonuçlar birleştirilmez
privacy_disclosure_refund: Ödeme sayfasında ürünün yayınlanmadığı, tahsilat ve iade koşulları, verinin yalnız araştırma için kullanıldığı açık yazılır
owner: Kurucu
planned_dates: E1 bitiminden sonraki 3 gün, iade penceresi 14 gün
```

## 7. Kapsam dışı bırakılanlar

- Apple Ads exact-match dağıtım testi: yayınlanmış ürün gerektirir, bu sözleşmede yok.
- Platform preset güncellemesi ve false-positive desteği kalıcı operasyon yüküdür;
  deney değil, maliyet kalemidir.
- Brand asset/logo tespiti, transkripsiyon, grammar AI ve cloud upload V1 scope'unda
  değil, deneyde de yok.

## 8. Karar kuralı

`scoring-model.md` build-öncesi matrisi uygulanır:

- Problem/talep E3+ ile çürütülürse → `KILL`.
- Problem B+ fakat wedge E3+ ile çürütülürse → `PIVOT`.
- `opportunity.low >= 60` + genel kanıt B+ + en riskli varsayım B+ + ürün-spesifik
  E3+ davranış → `BUILD_SMALL`.
- Diğer tüm durumlar → `TESTE_DEVAM`.

Dört deney de geçse `BUILD_SMALL` otomatik değildir: `opportunity.low = 52` ve genel
kanıt `C`. G0+E1+E2+E3 geçerse `claim-wedge` E2, `claim-retention` E2 ve
`claim-economics` E3 kayıtlarıyla yeniden puanlanır; `low >= 60` ve genel kanıt B+
çıkarsa build-öncesi matris `BUILD_SMALL` verebilir. Aksi halde sonuç `TESTE_DEVAM`.
