# Mobil App Finansal Model Sablonu — v4.0

> Pre-launch model bir senaryodur, kanit degildir. Benchmark girdileri en fazla C
> evidence uretir. First-party kohort verisi geldikce model gerceklesen ekonomiyle
> degistirilir.

## 1. Model Baglami

| Alan | Deger |
|---|---|
| Arketip | consumer_utility / consumer_subscription / b2b_prosumer / marketplace_network |
| Hedef segment | [segment] |
| Hedef geo/kohort | [ulke + kanal] |
| Monetizasyon | paid / subscription / hybrid / usage / marketplace fee |
| Risk modifier | ai_variable_cost vb. |
| Veri asamasi | benchmark scenario / prebuild transaction / first-party cohort |

Her girdi evidence ID ve grade tasir.

## 2. Bottom-Up Funnel

| Adim | Formul | Low | Base | High | Evidence |
|---|---|---:|---:|---:|---|
| Qualified reach | kanal hacmi | | | | |
| Store/page visit | reach × CTR | | | | |
| Install/signup | visit × conversion | | | | |
| Activated user | signup × activation | | | | |
| Paid user | activated × paid conversion | | | | |
| Retained payer | paid × renewal/retention | | | | |

Paid ve organik kanallari ayri kohortta tut. Geo'lari tek ortalamada birlestirme.

## 3. Gelir ve Brut Katki

```text
gross_revenue = paid_users * realized_or_scenario_ARPPU
store_and_tax = gross_revenue * effective_store_tax_rate
variable_cost = usage_cost + support_cost + payment_cost
gross_contribution = gross_revenue - store_and_tax - variable_cost
contribution_after_CAC = gross_contribution - acquisition_spend
```

`ai_variable_cost` varsa request/token/media generation maliyeti kullanim dagilimina
gore low/base/high modellenir; ortalama power-user maliyetini gizlememeli.

## 4. Kohort Metrikleri

First-party veri geldikce ana tablo:

| Kohort | Kanal | Geo | n | D0 Paid | D30 ARPPU | D90 ARPPU | First Renewal | D30/D90 Retention | CAC | Payback | Brut Katki |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| [tarih] | [kanal] | [geo] | [n] | | | | | | | | |

- Realized ARPPU, erken tahmini lifetime degerinden once gelir.
- Payback, kümülatif brut katkının CAC'i karsiladigi tarihtir.
- Subscription arketipinde first renewal ve retention olmadan ekonomi gecmis
  sayilmaz.
- Marketplace'te iki tarafin acquisition maliyeti ve take-rate ayri izlenir.

## 5. Pre-Launch Senaryolari

Uc senaryo zorunlu:

| Girdi | Konservatif | Base | Iyimser | Kaynak/Grade |
|---|---:|---:|---:|---|
| Qualified reach | | | | |
| Install/signup conversion | | | | |
| Activation | | | | |
| Paid conversion | | | | |
| First renewal/retention | | | | |
| ARPPU | | | | |
| CAC | | | | |
| Variable cost | | | | |

Iyimser senaryo karar icin tek basina kullanilmaz. Benchmark farkli kategori,
platform veya geo'dansa limitation yaz.

## 6. Threshold Turetimi

Faz 5.5 quantitative threshold'u su girdilere baglanir:

- hedef payback suresi
- kabul edilen CAC tavani
- ilgili geo/kanal CPC veya outreach maliyeti
- D30/D90 brut katki senaryosu
- refund/churn guardrail

Girdiler credible degilse test `exploratory`dir. Universal CTR, email veya paid
conversion esigi kullanma.

## 7. Sensitivity

En az su degiskenleri stresle:

- paid conversion yarisi
- retention/renewal yarisi
- CAC iki kati
- store/tax degisimi
- AI/variable cost iki kati
- yuksek-LTV geo erisilemez

Sonuc yalniz iyimser senaryoda pozitifse viability claim'i C'yi gecemez ve Faz
5.5'te odeme/ekonomi testi onceliklenir.

## 8. Post-MVP Karari

Build oncesi yazilan activation, retention ve ekonomi threshold'larini kohort
tablosuyla karsilastir:

- iki ardisik kohort tum esikleri gecer -> SCALE adayi
- value/activation gecer, tek alt metrik kalir -> ITERATE
- value veya retention iki kohort kalir -> STOP

Karari `data/assessment.json` icinde guncelle ve first-party kayitlari E4 olarak
evidence ledger'a ekle.
