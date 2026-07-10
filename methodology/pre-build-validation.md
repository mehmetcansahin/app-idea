# Build-Oncesi Dogrulama — Faz 5.5, v4.0

> Faz 5.5 bir landing-page ritueli degil, en riskli varsayima uygun deney
> merdivenidir. Insan tarafindan yurutulur; agent deney sozlesmesini ve analizini
> hazirlar. Yuzde guven uretilmez.

## 1. Giris Kosulu

Faz 5 masa basi karari `TESTE_DEGER` veya `TEST_ONCELIKLI` olmali. `ELENDIR` veya
fatal gate `blocked` ise plan uretilmez. `BELIRSIZ` ise once eksik masa basi kaniti
toplanir; yalniz masa basinda kapatilamayacak belirsizlikler deney konusu olur.

## 2. Riskiest Assumption Test (RAT)

Varsayimlari su risk siniflarinda listele:

- value/problem demand
- usability
- technical feasibility
- business viability/monetization
- retention/repeat value
- distribution
- regulation/safety
- marketplace ise liquidity/cold start

Her varsayim `impact` ve `uncertainty` icin 1-3 alir. `impact * uncertainty` en
yuksek olan once test edilir. Esitlikte fatal olma potansiyeli, sonra test maliyeti
en dusuk olan onceliklidir.

## 3. Deney Yontemi Esleme

| En riskli varsayim | Varsayilan deney |
|---|---|
| Problem/talep | Gecmis davranis gorusmesi + mevcut workaround gozlemi |
| Odeme/ekonomi | Gercek, acik ve iade edilebilir depozito/on-siparis veya B2B LOI |
| UX/hiz/kalite wedge'i | Rakiple karsilastirmali gorev prototipi |
| Teknik fizibilite | 1-2 gunluk teknik spike, API/veri erisim testi |
| Retention | Concierge/Wizard-of-Oz, en az iki dogal kullanim dongusu |
| Dagitim | Kanal-spesifik acquisition testi; UTM + maliyet + donusum |
| Regulasyon | Resmi kaynak taramasi + gerekli ise uzman/avukat gorusmesi |
| Likidite | Dar geo/segmentte arz tohumlama + gercek eslesme deneyi |

Urunun vaadi "daha hizli/daha guzel/daha kullanisli" ise landing page ana test
olamaz; kullanici farki deneyimlemelidir.

## 4. Evidence Merdiveni

- Waitlist, email, scroll veya ucuz tiklama: en fazla `E1`.
- Dogrulanmis gorusme randevusu veya gecmis ucretli workaround: `E2`.
- Iade edilebilir depozito, gercek on-siparis, imzali LOI: `E3`.
- Ucretli urun kullanimi, tekrarli kullanim veya retention: `E4`.

Landing page mesaj/kanal ogrenmek icin faydalidir; tek basina `BUILD_SMALL`
uretemez. Kullanici kandirilmaz: urunun hazir olmadigi, tahsilatin/iadenin kosullari
ve verinin nasil kullanilacagi aciklanir.

## 5. Gorusme Duzeni

Oncelikli segment basina iki tur planla:

1. Tur 1: 4-8 kisiyle problem ve gecmis davranis kesfi.
2. Tur 2: 4-8 kisiyle yeni yuksek-etkili tema cikmadigini ve karsit ornekleri
   kontrol et.

Segmentler tek orneklemde karistirilmaz. Gorusmeler nicel oran veya yuzde guven
uretmez. Iyi sorular son spesifik olayi, mevcut cozumleri, harcanan zaman/parayi ve
gecis engellerini arar. "Kullanir miydin/oder miydin?" karar kaniti degildir.

## 6. Quantitative Test Kurali

Her quantitative test su girdileri yazar:

- baseline veya neden bilinmedigi
- minimum detectable effect
- orneklem hedefi ve hesaplama yontemi
- trafik kaynagi ve attribution
- ana metrik, guardrail ve stopping rule

Baseline/MDE/orneklem hesabi yoksa sonuc `directional`dir ve claim C'yi gecemez.
Evrensel ziyaretci, CTR, email veya donusum esigi kullanilmaz.

Ekonomi esigi kanal maliyeti, hedef payback ve finansal modeldeki brut katkidan
turetilir. Bu girdiler credible degilse deney `exploratory`dir ve `BUILD_SMALL`
karari uretemez.

## 7. Deney Sozlesmesi

`phases/06-prebuild-plan.md` her deney icin su sablonu kullanir:

```text
experiment_id:
claim_id:
segment:
channel_or_recruitment:
method:
target_evidence_level:
sample_target:
metric:
threshold_and_derivation:
guardrails:
stopping_rule:
pass_action:
fail_action:
privacy_disclosure_refund:
owner:
planned_dates:
```

Esik sonuctan sonra degistirilmez. Degisiklik gerekirse eski deney kapatilir ve yeni
`experiment_id` ile tekrar kaydedilir.

## 8. Karar

`methodology/scoring-model.md` karar matrisini uygula:

- problem/talep E3+ ile curutuldu -> `KILL`
- problem B+, wedge/cozum E3+ ile curutuldu -> `PIVOT`
- firsat `low >= 60`, genel kanit B+, en riskli varsayim B+ ve urun-spesifik E3+
  davranis -> `BUILD_SMALL`
- aksi -> `TESTE_DEVAM`

Faz 5.5 sonucu `data/evidence.jsonl` ve `data/assessment.json` icine islenmeden
durum degistirilmez.

## 9. BUILD_SMALL Siniri

`BUILD_SMALL` tam urun veya scale izni degildir. Varsayilan sinir:

- max 4 core product screen
- max 3 ana ozellik
- gerekiyorsa 1 paywall/upgrade ekrani
- activation, retention ve ekonomi esikleri build oncesi yazilmis

Sonraki karar gercek MVP kohortlarindan `SCALE`, `ITERATE` veya `STOP` olur.
