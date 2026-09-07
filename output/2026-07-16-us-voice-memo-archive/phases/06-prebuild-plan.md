# Faz 5 → 5.5 Geçişi — Voice Memo Archive Teknik Gate Sözleşmesi

**Fikir:** `us-voice-memo-archive` · **Masa başı kararı:** BELIRSIZ · **Durum:** DESK_RESEARCH_COMPLETE
**Metodoloji:** v4.0 · **Sözleşme tarihi:** 2026-09-07
**Kaynak assessment:** [`data/assessment.json`](../data/assessment.json) · **Kanıt:** [`data/evidence-ledger.md`](../data/evidence-ledger.md)

Bu dosya bir Faz 5.5 kullanıcı deneyi sözleşmesi **değildir**. `CORE_FEASIBILITY_BLOCKED`
gate'i `unknown` olduğu için `pre-build-validation.md` §1 uyarınca önce eksik kanıt
kapatılır; kullanıcı ve ödeme deneyi bu kapı açılmadan çalıştırılmaz. Belge iki
parçadır: masa başında kapatılan/kapatılamayan belirsizliklerin dökümü ve kalan
belirsizlik için teknik spike sözleşmesi.

## 1. Giriş koşulu kontrolü

| Koşul | Durum |
|---|---|
| Faz 5 kararı | ⚠️ `BELIRSIZ` — kullanıcı deneyi henüz açılamaz |
| Fatal gate `blocked` var mı | ✅ hayır; biri `unknown` |
| `CORE_FEASIBILITY_BLOCKED` | ⚠️ `unknown` (`memo-technical-multi-share`, `memo-technical-metadata`, `memo-technical-extension-limits`) |
| Genel Kanıt Gücü | `C` |

## 2. Masa başı protokolünün sınırı

Gate'i `unknown` yapan üç alt sorunun ikisi masa başında kapandı; belirleyici olan
üçüncüsü kapanamaz.

| Alt soru | Masa başı durumu | Kaynak |
|---|---|---|
| Çoklu memo paylaşımı API/UI olarak mümkün mü | ✅ Kapandı: Rendered ve Editable paylaşım belgeli | `memo-technical-multi-share` |
| `creationDate` yapısal olarak boş olabilir mi | ✅ Kapandı: Apple `nil` olabileceğini söylüyor | `memo-technical-metadata` |
| Share Extension bellek limiti ve sonlandırma riski var mı | ✅ Kapandı: limitler ve sistem sonlandırması belgeli | `memo-technical-extension-limits` |
| **Gerçek kütüphanelerde tarih kapsaması yüzde kaç** | ❌ Kapanamaz: başka kullanıcının Voice Memos kütüphanesi dokümanla gözlemlenemez | — |
| **2 GB batch cihazda hayatta kalıyor ve resume ediyor mu** | ❌ Kapanamaz: davranış ölçümü cihaz gerektirir | — |

Yani API'nin ne yapabildiği belgeli; **gerçek dosyalarda ne olduğu** belgeli değil.
Bu iki soru ölçülmeden gate `unknown` kalır ve karar kalıcı olarak `BELIRSIZ`dir.
Ek masa başı arama bu boşluğu kapatmaz; ürünün satış vaadi ("tarihleri koruyan
toplu arşiv") tam olarak bu iki ölçüme dayanıyor.

## 3. RAT sıralaması

Assessment üç varsayımı `3 × 3 = 9` ile eşitliyor. `claim-technical` fatal olma
potansiyeli en yüksek olan ve maliyeti en düşük olandır: kod yazma maliyeti 1-2 gün,
sonuç ise fikri doğrudan öldürebilir.

| Sıra | claim_id | Risk sınıfı | Deney | Ön koşul |
|---|---|---|---|---|
| 1 | `claim-technical` | technical_feasibility | G0 teknik spike | — |
| 2 | `claim-wedge` | usability | E1 ikame karşılaştırmalı görev | G0 geçer |
| 3 | `claim-economics` | business_viability | E2 iade edilebilir preorder | E1 geçer |

## 4. G0 — Teknik spike (gate kapatma)

```text
experiment_id: memo-g0-metadata-batch-spike
claim_id: claim-technical
segment: İnsan katılımcı yok; ölçüm nesnesi gerçek Voice Memos dosyaları ve cihaz davranışı
channel_or_recruitment: Kurucunun kendi kütüphanesi + açık rıza veren gönüllülerin cihazları; ses araştırmacıya aktarılmaz, ölçüm gönüllünün cihazında çalıştırılır
method: UI'sız Swift prototip. (1) iOS 17/18/26 kaynaklı 50 gerçek memo: yeniden adlandırılmış, edited, layered, Apple Watch kaynaklı ve eski kayıtlar dahil. (2) Voice Memos UI'da görünen başlık/tarih ile extracted metadata timezone normalize edilerek karşılaştırılır; Rendered ve Editable paylaşım modları ayrı ayrı ölçülür. (3) En eski desteklenen cihazda 25 dosya ve toplam 2 GB batch App Group kuyruğuna sırayla kopyalanır; extension zorla sonlandırılır ve resume doğrulanır
target_evidence_level: E2
sample_target: 50 memo (denominator = ölçülen dosya sayısı), 2 paylaşım modu, 1 adet 2 GB batch, en az 3 zorla sonlandırma
metric: Doğru tarih kapsaması, yanlış tarih sayısı, eksik/şüpheli alan işaretleme oranı, 2 GB job'da kayıpsız resume, extension peak memory
threshold_and_derivation: Bu deneyin denominator'ı gerçek olduğu için eşikler ölçülmüş orandır, directional değil: doğru tarih kapsaması >= %95, yanlış tarih = 0, eksik/şüpheli alanların işaretlenmesi = %100, 2 GB job'da kayıpsız resume = evet. Eşikler Quick Scan'de sonuç görülmeden kaydedildi. "Yanlış tarih = 0" ürünün tek dürüstlük vaadidir: eksik tarih kabul edilebilir, uydurulmuş tarih kabul edilemez
guardrails: Orijinal dosyalar değiştirilmez, silinmez; yalnız kopya işlenir. Ses araştırmacının sunucusuna gitmez, transkribe edilmez, saklanmaz. Gönüllü cihazından yalnız sayısal sonuç (kapsama, hata sayısı, süre, bellek) alınır; dosya adı, içerik ve konuşmacı bilgisi alınmaz. Transfer tarihi hiçbir koşulda orijinal tarih gibi sunulmaz
stopping_rule: Dört eşikten biri kalırsa dur. Kullanıcı görüşmesi, demo veya ödeme testi yapılmaz
pass_action: Gate'i `clear` yap, claim-technical'i E2 kaydıyla güncelle, assessment'i yeniden puanla ve E1'i aç
fail_action: Gate `blocked` olur ve masa başı kararı `ELENDIR`e döner. Alternatif olarak scope "tarih koruma" yerine "eksik metadata'yı dürüstçe raporlayan taşınabilir arşiv"e daralabilir; bu ayrı fikir sayılır ve yeni assessment gerektirir
privacy_disclosure_refund: Gönüllüye hangi sayısal alanların alındığı, sesin cihazdan çıkmadığı ve ölçüm bittiğinde prototipin silineceği yazılı bildirilir
owner: Kurucu (tek geliştirici)
planned_dates: 1-2 gün prototip, 2 gün ölçüm ve raporlama
```

## 5. E1 — İkame karşılaştırmalı görev (yalnız G0 geçerse)

```text
experiment_id: memo-e1-substitute-comparison
claim_id: claim-wedge
segment: Apple Voice Memos içinde en az 100 kaydı olan ABD'li gazeteci, müzisyen, araştırmacı veya arşiv meraklısı
channel_or_recruitment: Gazetecilik, müzik prodüksiyon ve arşiv toplulukları; kolaylık örneklemi ayrı source etiketiyle tutulur
method: Katılımcı aynı arşivleme işini iki yolda dener: kendi mevcut yolu (AirDrop/Files/iCloud, iMazing veya Mac aracı) ve prototip. Sıra 6/6 dengelenir. Çıktı, katılımcının kendi dosyaları üzerinde denetlenir: hangi alanların gerçekten korunduğu, manifest'in okunabilirliği, checksum'ın doğrulanabilirliği
target_evidence_level: E2
sample_target: 12 kişi, iki turda (Tur 1 = 6, Tur 2 = 6 yeni tema ve karşıt örnek kontrolü)
metric: Ana metrik = işi prototiple tamamlayan ve çıktısını gerçekten saklayan kişi sayısı. İkincil = mevcut yola kıyasla aktif süre, manifest/checksum'ın anlaşılırlığı, iMazing/Mac aracına rağmen telefonda kalmayı seçme gerekçesi
threshold_and_derivation: Baseline her katılımcının kendi mevcut yolu; popülasyon MDE'si yok, eşikler exploratory: >=8/12 prototiple işi tamamlar, >=6/12 çıktıyı gerçekten saklar/taşır, çoğunluk çıktı güvenilirliğinde prototipi tercih eder
guardrails: Bilgisayarı kabul eden kullanıcı için iMazing güçlü ve ücretsiz olmayan ama yerleşik ikamedir; karşılaştırma bu ikameye karşı yapılır. Ses cihazdan çıkmaz. Prototip orijinalleri silmez
stopping_rule: <8/12 tamamlama veya <6/12 gerçek saklama ya da çoğunluk mevcut yolu tercih ederse ödeme testine geçme
pass_action: E2 preorder'ı sun
fail_action: Segmenti daralt (yalnız Windows kullanan veya bilgisayarsız kullanıcı) ve yeni experiment_id ile tekrar test et; sonuçlar birleştirilmez
privacy_disclosure_refund: Ürünün hazır olmadığı, sesin cihazda kaldığı ve tutulan event listesi yazılı açıklanır
owner: Kurucu
planned_dates: Recruitment 4 gün, oturumlar 6 gün
```

## 6. E2 — İade edilebilir preorder (yalnız E1 geçerse)

```text
experiment_id: memo-e2-refundable-preorder
claim_id: claim-economics
segment: E1'i tamamlayan aynı 12 kişilik kohort
channel_or_recruitment: E1 kohortu
method: Gelecek $9.99 lifetime fiyatı açıkça gösterilir; ayrı ödeme sayfasında $9.99 iade edilebilir preorder alınır. Preorder prototip erişiminin şartı değildir
target_evidence_level: E3
sample_target: 12
metric: Ana metrik = gerçek para riske eden kişi sayısı. İkincil = 14 günlük refund oranı ve fiyat itirazı gerekçesi
threshold_and_derivation: >=5/12 preorder ve refund <=%20. Eşik 5'tir çünkü komşu araçların gözlenen fiyatları $1.99-$4.99 ve Mac ikamesi $49; $9.99 lifetime bu aralığın ortasında test edilmemiş bir hipotezdir. Finansal model, kanal maliyeti ve komisyon sonrası brüt katkı gözlenmediği için deney `exploratory`dir
guardrails: Waitlist/e-posta E1 seviyesidir, sayılmaz. Sandbox IAP gerçek ödeme değildir. Teslim edilmezse tam iade ve iade süresi yazılıdır
stopping_rule: <5/12 preorder veya refund >%20 ise fiyat hipotezi çürüktür; fikri park et
pass_action: claim-economics'i E3 kaydıyla yeniden puanla ve build-öncesi matrisi uygula
fail_action: $4.99 veya per-archive fiyat hipotezini yeni experiment_id ile test et; eski deney kapatılır
privacy_disclosure_refund: Ödeme sayfasında ürünün yayınlanmadığı, tahsilat/iade koşulları ve verinin yalnız araştırma için kullanıldığı açık yazılır
owner: Kurucu
planned_dates: E1 bitiminden sonraki 3 gün, iade penceresi 14 gün
```

## 7. Karar kuralı

- G0 kalır → gate `blocked`, masa başı kararı `ELENDIR`. Tarih koruma vaadi
  ölçümle çürütülmüş olur.
- G0 geçer, E1/E2 çalışmamış → gate `clear`, karar `TESTE_DEGER`, durum
  `PREBUILD_PENDING`.
- G0 + E1 + E2 geçer → build-öncesi matris uygulanır. `opportunity.low = 52` ve genel
  kanıt `C` olduğu için otomatik `BUILD_SMALL` yok; yeniden puanlamada `low >= 60`,
  genel kanıt B+ ve en riskli varsayımda B+ gerekir. Aksi halde `TESTE_DEVAM`.

Zamanlama riski karar kuralının parçası değil ama sözleşmede kayıtlı: Apple export
metadata davranışını düzeltirse wedge daralır (`memo-timing-2026-breakage`). G0
sonucu üç aydan eski olduğunda tekrar ölçülür.

Eşikler sonuç görüldükten sonra değiştirilmez. Değişiklik gerekirse ilgili deney
kapatılır ve yeni `experiment_id` ile yeniden kaydedilir.
