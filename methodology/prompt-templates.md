# App Fikri Arastirma Prompt Sablonlari — v4.0

> Bu sablonlar workflow yardimcisidir. Skor, kanit ve deney kurallari kanonik
> metodoloji dosyalarindan gelir.

## Preflight

```text
Bu app fikri icin Research Contract olustur:
- problem/JTBD ve spesifik hedef segment
- platform ve 3-5 hedef geo/storefront
- birincil arketip: consumer_utility / consumer_subscription / b2b_prosumer /
  marketplace_network
- risk modifier'lari
- karar asamasi: desk_research / prebuild_validation / post_mvp

Iki arketip makulse ve agirliklar sonucu degistirecekse kullaniciya sor.
```

## Faz 1-2: Problem, Ikame ve Kanal

```text
[ALAN] icinde kullanicinin son spesifik davranisiyla tanimlanabilen problemleri
bul. Her problem icin kim, ne zaman, status quo, harcanan zaman/para, mobil
uygunluk, app-disi ikame, keyword cluster ve watering-hole yaz. Gelecek niyeti
gecmis davranis gibi sunma.
```

## Faz 3: Hizli Tarama

```text
[FIKIR] icin ayni JTBD'yi cozen app, web urunu, hizmet ve manuel workflow'lari
tara. Store metadata'yi URL, tarih, storefront, platform ve app yasi ile kaydet.
Rating'i E2/supporting proxy olarak kullan; fatal gate yapma. Trend, geo ve
dagitim claim'leri icin bagimsiz ve karsit kaynak ara. Her bulguyu evidence JSONL
sozlesmesine gore kaydet.
```

## Faz 4: Rakip ve Review

```text
Top 10 rakip/ikame matrisi olustur. Top 5 app icin son 12 aydan storefront ve
version bilgili stratified review sample topla: 1-2, 3 ve 4-5 yildizdan min 5'er,
hedef 30. Tema frekansini yalniz sample denominator'u icinde raporla. Community
verisini JTBD Push/Pull/Anxiety/Habit ile analiz et. Fiyat, odeme davranisi,
ad/channel (`ad_library` kayitlari) ve visual intelligence'i claim/evidence
ID'lerine bagla.
```

## Faz 5: Iki Eksenli Degerlendirme

```text
`methodology/scoring-model.md` kullan:
1. Fatal gate'leri evidence ID'leriyle clear/blocked/unknown yap.
2. Arketipin agirligi sifir olmayan her boyutuna 1-5 low/base/high ver; veri yoksa
   null kullan.
3. Opportunity low/base/high hesapla.
4. RAT ile en riskli varsayimlari sirala.
5. `evidence-model.md` ile claim ve overall A-D hesapla.
6. Asamaya uygun karar matrisini uygula. Desk research build/scale karari vermez.
7. Sonucu `data/assessment.json` sozlesmesine yaz.
```

## Faz 5.5: Deney Sozlesmesi

```text
En riskli claim icin landing'i otomatik varsayma. Risk turune gore interview,
deposit/preorder/LOI, competitor prototype, technical spike, concierge retention,
channel veya liquidity testi sec. Segment, orneklem, baseline/MDE, metric,
threshold derivation, guardrail, stopping rule, pass/fail aksiyonu ve
privacy/refund kosullarini onceden yaz. Waitlist max E1'dir; yuzde guven uretme.
```

## Faz 7: Evidence Audit

```text
Kritik claim'leri audit et: observation vs inference, source root independence,
freshness, geo/storefront, behavior vs stated intent, missingness, sample
denominator, contradicting evidence. Iki URL ayni primary raporu aktariyorsa tek
root say. Audit sonucunu `05-validation.md` icine yaz.
```

## Faz 8: Compare

```text
Yalniz ayni methodology version raporlarini karsilastir. Sirayi fatal gate,
overall evidence grade, opportunity interval, top-risk test cost ve operasyon
kisitlarina gore kur. Farkli arketiplerin agirliklarini acikla; ciplak skoru tek
gerekce yapma.
```

## Faz 9: Brief ve Ekonomi

```text
Faz 5.5 tamamlanmadiysa brief'i PREBUILD_PENDING kosullu taslak yap. BUILD_SMALL
varsa max 4 core ekran, 3 ozellik ve gerekirse 1 paywall sinirla. Pre-launch
ekonomiyi benchmark senaryosu olarak etiketle; D30/D90 realized ARPPU, payback,
brut katki ve retention kohortlarini first-party veri plani olarak yaz. AI
variable cost ve geo sensitivity gerekiyorsa ekle.
```

## Faz 10: Seytanin Avukati

```text
Value, usability, feasibility, viability, retention, distribution, regulation ve
marketplace ise liquidity varsayimlarina guclu karsit kanit ara. Yeni fatal gate,
unresolved contradiction veya evidence downgrade varsa assessment ve karari
yeniden hesapla.
```

## Final Rapor

```text
`templates/report-template.md` kullan. Her kritik claim'i evidence ID ve tam URL
ile bagla. REPORT, assessment.json ve evidence ledger ayni arketip, skor, grade,
karar ve durumu gostersin. Son adimda evidence_tool render + validate calistir.
```
