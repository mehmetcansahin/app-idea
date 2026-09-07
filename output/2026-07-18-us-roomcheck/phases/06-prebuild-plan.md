# Faz 5 → 5.5 Geçişi — RoomCheck Teknik Gate Sözleşmesi

**Fikir:** `us-roomcheck` · **Masa başı kararı:** BELIRSIZ · **Durum:** DESK_RESEARCH_COMPLETE
**Metodoloji:** v4.0 · **Sözleşme tarihi:** 2026-09-07
**Kaynak assessment:** [`data/assessment.json`](../data/assessment.json) · **Kanıt:** [`data/evidence-ledger.md`](../data/evidence-ledger.md)

Bu bir Faz 5.5 kullanıcı deneyi sözleşmesi değildir. `CORE_FEASIBILITY_BLOCKED`
gate'i `unknown`, `room-core-feasibility` claim'i `D`; `pre-build-validation.md` §1
uyarınca önce bu kapı ölçülür. Kullanıcı ve ödeme deneyi kapı açılmadan
çalıştırılmaz.

## 1. D derecesinin gerçek nedeni

`room-core-feasibility` derecesi kanıt yokluğundan değil, **var olan tüm kanıtın
iddianın güçlü versiyonunu çürütmesinden** D:

| Kayıt | Seviye | Yön | Ne diyor |
|---|---|---|---|
| `room-tn3111-limit` | E2 | contradicts | Apple genel amaçlı "tüm yakın ağları/kameraları tara" API'si sunmuyor |
| `room-tn3179-limit` | E2 | contradicts | Local-network erişimi izinli ve Bonjour yalnız reklam edilen servisleri buluyor; tam envanter garanti değil |
| `room-bluetooth-limit` | E2 | contradicts | Core Bluetooth yalnız advertising yapan cihazı görüyor; görünürlük "bu bir kameradır" demiyor |

Üç kayıt da destekleyici değil çürütücü olduğu için claim `D`. Bu doğru bir
derecelendirmedir: **"odadaki her kamerayı bul" vaadi ölü.** Açık kalan soru daha dar:
*görünebilen* sinyaller kullanıcıya yararlı bir `incelemeye değer` kuyruğu üretiyor mu?

Hiçbir doküman bu soruyu kapatamaz — cevap kontrollü ölçümdedir. Bu yüzden ek masa
başı arama gate'i açmaz.

## 2. Yapısal olarak D kalan iki claim

`room-legal` ve `room-safety` de D, fakat bunlar teknik spike'ın konusu değildir:

- `room-legal`: tek kayıt `room-us-recording-law` (E2, contradicts) ve o da **covert
  recorder** ürününe ait riski gösteriyor; RoomCheck bu davranışı kapsam dışı bırakıyor.
  Kapsam dışı bırakılan bir riskin yokluğu pozitif kanıtla gösterilemez. Bu claim masa
  başında B/C'ye çıkmaz; tek yükseltme yolu avukat incelemesidir ve o bir **yayın öncesi
  görev**dir, deney değil.
- `room-safety`: tek destek `room-scope-boundary` (E1, kendi araştırma kontratı). Kendi
  scope beyanı bağımsız kök sayılmaz. Güvenlik iddiası ancak uygulama davranışı
  ölçülünce (G0 disclosure metriği) E2 kazanır.

`sensitive_data` risk modifier'ı taşıyan bir fikirde bu iki claim'in D olduğu
raporda görünür kalmalı; gate açıldı diye kapanmış sayılmaz.

## 3. RAT sıralaması

| Sıra | claim_id | Risk sınıfı | Derece | Deney | Ön koşul |
|---|---|---|---|---|---|
| 1 | `room-core-feasibility` | technical_feasibility | D | G0 kontrollü corpus | — |
| 2 | `room-wedge` | usability | C | E1 anlama (comprehension) testi | G0 geçer |
| 3 | `room-economics` | business_viability | C | E2 iade edilebilir preorder | E1 geçer |

## 4. G0 — Kontrollü doğruluk ve dürüstlük corpus'u

```text
experiment_id: room-g0-controlled-corpus
claim_id: room-core-feasibility
segment: İnsan katılımcı yok; ölçüm nesnesi 20 kontrollü oda ve içine yerleştirilen cihazlar
channel_or_recruitment: Kurucunun kurduğu corpus: 20 oda düzeni, 30 bilinen kamera (Wi-Fi bağlı, BLE reklamı yapan, izole/AP modunda, tamamen kablolu/offline) ve karıştırıcı normal elektronikler (duman alarmı, saat, TV, USB adaptör, priz)
method: Her odada prototip çalıştırılır. Kameralar kurulumdan ONCE "teknik olarak görünebilir" ve "görünemez" olarak etiketlenir; etiket tarama sırasında kör tutulur. Recall yalnız görünebilir alt kümede hesaplanır; görünemez vakalar denominator'a katılmaz ve "temiz" sayılmaz, her birinde yetersiz-veri disclosure'i beklenir
target_evidence_level: E2
sample_target: 20 oda, 30 kamera (görünebilir/görünemez ayrık), her odada en az 3 karıştırıcı cihaz
metric: Görünebilir kameraların inspect-further kuyruğuna alınma oranı; yüksek-riskli false positive oranı (normal cihazı yüksek şüphe olarak işaretleme); görünemez/yetersiz vakalarda açık disclosure oranı
threshold_and_derivation: Denominator gerçek (etiketlenmiş kamera sayısı), bu yüzden eşik ölçülmüş orandır: görünebilir kameralarda >=%80 inspect-further; yüksek-riskli false positive <=%10; görünemez/yetersiz vakalarda disclosure = %100. Eşikler Quick Scan'de sonuç görülmeden kaydedildi
guardrails: Ürün hiçbir çıktıda "kamera bulundu/oda temiz" demez. Tarama local kalır; hiçbir ağ envanteri veya cihaz kimliği dışarı gönderilmez. Corpus üçüncü kişinin gerçek odasında kurulmaz
stopping_rule: Recall <%80, yüksek-riskli FP >%10 veya disclosure <%100 ise kullanıcı testine geçilmez
pass_action: Gate'i `clear` yap, claim'i E2 kaydıyla güncelle, yeniden puanla ve E1'i aç
fail_action: Detector iddiasını tamamen çıkar. Ürün saf rehberli checklist'e daralır (yeni assessment gerekir) veya `ELENDIR`
privacy_disclosure_refund: Katılımcı yok; corpus kurucuya ait. Ölçüm sonrası cihaz listesi ve ağ kayıtları silinir
owner: Kurucu (tek geliştirici)
planned_dates: Corpus kurulumu 3 gün, ölçüm 3 gün, raporlama 1 gün
```

## 5. E1 — Anlama testi (yalnız G0 geçerse)

```text
experiment_id: room-e1-comprehension
claim_id: room-wedge
segment: Son 90 günde en az iki otel/short-term rental konaklaması yapmış, mahremiyet kontrolü yapma niyeti olan 12 ABD'li iPhone kullanıcısı
channel_or_recruitment: Seyahat ve short-term rental toplulukları; kolaylık örneklemi ayrı source etiketiyle tutulur
method: Katılımcı gerçek bir konaklama odasında (veya kontrollü kurulumda) prototipi kullanır. Taramadan sonra kendi cümleleriyle üç şey açıklaması istenir: (a) sonuç ne diyor, (b) ne göremediği, (c) bir sonraki adımı ne olurdu. Yanıtlar kör kodlanır. Mevcut ikame (gözle checklist, router ekranı, flashlight, detector app'i) ile karşılaştırma sorulur
target_evidence_level: E2
sample_target: 12 kişi, iki turda (Tur 1 = 6, Tur 2 = 6 yeni tema ve karşıt örnek kontrolü)
metric: Ana metrik = "bulgu yok" sonucunu "kamera yok" diye yanlış anlamayan kişi sayısı. İkincil = sonucun karar verilebilir bulunması, mevcut ikameye kıyasla tercih, tarama süresi
threshold_and_derivation: Bu sözleşmede ilk kez kaydedilen eşikler; baseline ve MDE yok, exploratory: >=9/12 "bulgu yok = kamera yok değil" ayrımını doğru açıklar; >=8/12 sonucu karar verilebilir bulur; hiçbir katılımcı üründen yanlış güvence almaz. Anlama eşiği en yükseği çünkü yanlış güvence bu üründe doğrudan güvenlik zararıdır
guardrails: Araştırmacı sonucu katılımcı yerine yorumlamaz. Katılımcıya kesinlik vaadi verilmez. Gerçek odada tarama yapılıyorsa mekân sahibinin cihazları hakkında iddia yayılmaz, kayıt tutulmaz
stopping_rule: <9/12 doğru anlama veya herhangi bir katılımcı yanlış güvence alırsa dur. Bu bir tasarım hatası değil, ürünün etik çekirdeğinin başarısızlığıdır
pass_action: E2 preorder'ı sun
fail_action: Sonuç dilini yeniden tasarla ve bir kez daha ölç; ikinci kalışta fikri kapat
privacy_disclosure_refund: Ürünün hazır olmadığı, hiçbir tarama verisinin saklanmadığı ve ürünün kesinlik vaat etmediği yazılı açıklanır
owner: Kurucu
planned_dates: Recruitment 4 gün, oturumlar 6 gün
```

## 6. E2 — İade edilebilir preorder (yalnız E1 geçerse)

```text
experiment_id: room-e2-refundable-preorder
claim_id: room-economics
segment: E1'i tamamlayan aynı 12 kişilik kohort
channel_or_recruitment: E1 kohortu
method: İki fiyat hipotezi ayrı ayrı gösterilir: $2.99 trip pass ve $7.99-$9.99 lifetime. Ayrı ödeme sayfasında $7.99 iade edilebilir preorder alınır. Preorder prototip erişiminin şartı değildir
target_evidence_level: E3
sample_target: 12
metric: Ana metrik = gerçek para riske eden kişi sayısı. İkincil = trip pass ile lifetime arasındaki tercih, 14 günlük refund oranı
threshold_and_derivation: Bu sözleşmede ilk kez kaydedilen eşik: >=4/12 preorder ve refund <=%20. Ekonomiden türetilmemiştir; quick modda finansal model, kanal maliyeti ve komisyon sonrası brüt katkı gözlenmedi. Rakiplerin haftalık fear-subscription fiyatları ($2.99/hafta) referans değil karşı-örnektir: ürün o modeli reddediyor
guardrails: Korku pazarlaması yapılmaz; ödeme istenirken "güvende olmak için" dili kullanılmaz. Waitlist E1'dir, sayılmaz. Teslim edilmezse tam iade yazılıdır
stopping_rule: <4/12 preorder veya refund >%20 ise fiyat/paket hipotezi çürüktür; fikri park et
pass_action: room-economics'i E3 kaydıyla yeniden puanla ve build-öncesi matrisi uygula
fail_action: Trip pass tek fiyat hipotezi olarak yeni experiment_id ile test edilir
privacy_disclosure_refund: Ödeme sayfasında ürünün yayınlanmadığı, tahsilat/iade koşulları ve verinin yalnız araştırma için kullanıldığı açık yazılır
owner: Kurucu
planned_dates: E1 bitiminden sonraki 3 gün, iade penceresi 14 gün
```

## 7. Karar kuralı

- G0 kalır → gate `blocked`, karar `ELENDIR` veya saf checklist ürününe daralma
  (yeni assessment).
- G0 geçer, E1/E2 çalışmamış → gate `clear`, karar `TESTE_DEGER`, durum
  `PREBUILD_PENDING`.
- G0 + E1 + E2 geçer → build-öncesi matris. `opportunity.low = 46` ve genel kanıt `D`
  olduğu için otomatik `BUILD_SMALL` yok; `low >= 60`, genel kanıt B+ ve en riskli
  varsayımda B+ gerekir. Aksi halde `TESTE_DEVAM`.

Yayın öncesi ayrı görev (deney değil): avukat incelemesi ve `room-legal` claim'inin
durumunun raporda güncellenmesi. Gate açılması bu görevi ortadan kaldırmaz.

Eşikler sonuç görüldükten sonra değiştirilmez. Değişiklik gerekirse ilgili deney
kapatılır ve yeni `experiment_id` ile yeniden kaydedilir.
