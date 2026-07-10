# BUILD_SMALL ve Lansman Playbook — v4.0

> Bu dosya yalniz `BUILD_SMALL` karari sonrasi kullanilir. `TESTE_DEGER`,
> `TEST_ONCELIKLI`, `BELIRSIZ` veya `PREBUILD_PENDING` build izni degildir.

## 1. Giris Gate'i

- fatal gate blocked/unknown yok
- opportunity low >= 60
- overall evidence B+
- en riskli varsayim B+
- en az bir urun-spesifik E3+ davranis
- assessment karari BUILD_SMALL
- activation, retention ve ekonomi esikleri onceden yazili

## 2. BUILD_SMALL Scope

- max 4 core product screen
- max 3 ana ozellik
- gerekiyorsa 1 paywall/upgrade ekrani
- tek hedef segment ve oncelikli geo
- analytics event ve kohort tanimlari build'in parcasi
- V1 disi liste zorunlu

Basit urun icin bir haftalik opsiyon:

| Gun | Cikti |
|---|---|
| Pazartesi | Segment, keyword, scope ve threshold freeze |
| Sali | Proje, auth/analytics, onboarding |
| Carsamba | Core ekranlar ve cekirdek deger |
| Persembe | Monetizasyon/paywall ve variable-cost guardrail |
| Cuma | Test, accessibility, privacy, security |
| Cumartesi | Store metadata ve submit |
| Pazar | Ilk kanal deneyi ve kohort baslangici |

## 3. Security ve Secret Hygiene

- admin endpoint auth + role kontrolu
- user content icin ownership/token kontrolu
- frontend'de admin/API secret olmamasi
- Supabase RLS/Firestore/backend authorization
- `role`, `isAdmin`, `credits`, entitlement gibi protected field'larin client
  tarafindan update edilememesi
- predictable ID riskinin azaltilmasi
- receipt/entitlement'in server veya guvenilir provider ile dogrulanmasi
- public AI share, log ve screenshot'larda secret/customer data scrub

Eksik kritik kontrol store submission'dan once kapatilir.

## 4. Olcum Plani

Her event su baglami korur:

- acquisition channel/campaign
- geo/storefront
- install/signup cohort
- app version
- pricing/paywall treatment
- arketipe ozgu activation event

Minimum metrikler:

| Alan | Metrik |
|---|---|
| Value | activation ve time-to-value |
| Retention | D1/D7/D30 veya dogal kullanim dongusu |
| Monetization | paid conversion, D30/D90 ARPPU, first renewal |
| Ekonomi | CAC, payback, brut katki |
| Quality | crash, support, refund |

Threshold'lar launch'tan once `assessment.json` stopping rule ve deney artifact'i
ile baglanir. Sonuctan sonra threshold kaydirilmaz.

## 5. Soft Launch

1. Tek geo/segmentte sinirli kohort ac.
2. Attribution ve event'leri test et.
3. Onboarding/paywall varyantini ayni anda coklu degistirme.
4. Nitel feedback'i nicel threshold yerine kullanma; ikisini evidence ledger'da
   ayri kaydet.
5. Refund, privacy, crash ve variable-cost guardrail'larini gunluk izle.

## 6. ASO ve Kanal Iterasyonu

- Custom product page veya PPO testinde variant, trafik ve confidence'i kaydet.
- Keyword/creative sonucu geo ve kanal disina genelleme.
- Community paylasiminda self-promotion kurallarina uy; organik dil ogrenimini paid
  acquisition sonucu gibi sunma.
- Paid scale yalniz gerceklesen contribution-after-CAC ve payback ile acilir.

## 7. Post-MVP Karar

### SCALE

Onceden yazilan activation, retention ve ekonomi esikleri iki ardisik kohortta
gecmis; fatal/quality guardrail temiz. Assessment `SCALE/POSTLAUNCH` olur.

### ITERATE

Value/activation gecer, yalniz bir alt metrik kalir. Bir sonraki en riskli claim
icin tek deney dongusu ac. Assessment `ITERATE/POSTLAUNCH` olur.

### STOP

Value veya retention iki ardisik kohortta kalir, ya da yeni fatal gate ortaya
cikar. Assessment `STOP/KILLED` olur.

Karar degisikliginde first-party E4 kayitlari evidence JSONL'ye eklenir, ledger
yeniden render edilir ve validator calistirilir.

## 8. Turkiye Operasyon

Tesvik, vergi, komisyon ve payout gereksinimleri yalniz guncel resmi kaynakla
kaydedilir. Tutar/limit hard-code edilmez. App Store Connect banking, agreements
ve tax formlari submit oncesi kontrol edilir.
