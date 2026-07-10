# App Arastirma Raporu: [KONU]

> Tarih: [YYYY-MM-DD]
> Mod: Quick / Standard / Deep
> Metodoloji: v4.0
> Kanit defteri: [data/evidence-ledger.md](data/evidence-ledger.md)

## Yonetici Ozeti

| Alan | Deger |
|---|---|
| Karar | ELENDIR / BELIRSIZ / TESTE_DEGER / TEST_ONCELIKLI / KILL / PIVOT / BUILD_SMALL / TESTE_DEVAM / SCALE / ITERATE / STOP |
| Asama | desk_research / prebuild_validation / post_mvp |
| Durum | DESK_RESEARCH_COMPLETE / PREBUILD_PENDING / PREBUILD_PASSED / BUILDING / POSTLAUNCH / KILLED |
| Arketip | consumer_utility / consumer_subscription / b2b_prosumer / marketplace_network |
| Risk modifier'lari | [liste veya yok] |
| Firsat Cekiciligi | Low [X] / Base [X] / High [X] — weak / borderline / attractive / insufficient_data |
| Kanit Gucu | A / B / C / D |
| Hedef Segment | [spesifik segment] |
| Hedef Geo/Storefront | [3-5 oncelik] |
| Fatal Gate | clear / blocked / unknown ozeti |
| En Riskli Varsayim | [claim_id + tek cumle] |
| Bir Sonraki Test | [test veya yok] |
| Anahtar Bulgu | [1-2 cumle] |

Masa basi raporunda build/scale dili kullanma. Sonuc `TESTE_DEGER` veya
`TEST_ONCELIKLI` ise oneriyi deney yatirimi olarak yaz.

## 0. Research Contract

| Alan | Karar |
|---|---|
| Problem/JTBD | [kim, hangi durumda, hangi sonucu istiyor] |
| Platform | [iOS/Android/cross-platform] |
| Birincil Arketip | [arketip + gerekce] |
| Alternatif Arketip | [varsa; neden secilmedi] |
| Modifier'lar | [liste + etkisi] |
| Hedef Geo | [ulke/storefront] |
| Veri Penceresi | [tarih araligi] |

## 1. Pazar ve Ikameler

| Gosterge | Gozlem | Evidence | Kalite / Relevance |
|---|---|---|---|
| Ana keyword/JTBD | [deger] | [EVIDENCE_ID] | [direct/supporting] |
| Lider app veya ikame | [deger] | [EVIDENCE_ID] | [direct/supporting] |
| Rating | [sayi + storefront + tarih + app yasi] | [EVIDENCE_ID] | E2/supporting |
| Trend/yasam dongusu | [yon] | [EVIDENCE_ID] | [seviye/relevance] |
| Mevcut workaround | [Excel/WhatsApp/manual/service] | [EVIDENCE_ID] | [seviye/relevance] |
| Problem maliyeti | [zaman/para/adim] | [EVIDENCE_ID] | [seviye/relevance] |

Rating fatal gate degildir. App rakibi bulunamazsa app-disi ikameleri burada
goster. Pazar raporu/dijital davranis uyumsuzlugunu uyari olarak yaz.

### Dagitim Erisimi

| Kanal/Keyword | Segment/Geo | Gozlenen Sinyal | Maliyet veya Difficulty | Evidence | Sinir |
|---|---|---|---|---|---|
| [kanal] | [baglam] | [sonuc] | [deger] | [ID] | [limit] |

## 2. Rakip, Review ve Wedge

### Rakip ve Ikame Matrisi

| # | Rakip/Ikame | Tur | Storefront/Geo | Fiyat | Son Guncelleme | Evidence |
|---|---|---|---|---|---|---|
| 1 | [isim] | app/manual/service | [baglam] | [fiyat] | [tarih] | [ID] |

### Stratified Review Mining ⚐ STANDARD+

| Rakip | 1-2★ n | 3★ n | 4-5★ n | Veri Penceresi | Storefront | Tema | Orneklem Ici Oran | Evidence |
|---|---:|---:|---:|---|---|---|---:|---|
| [app] | [n] | [n] | [n] | [son 12 ay] | [US] | [tema] | [x/n] | [ID] |

Random sample yoksa orani pazar prevalansi diye sunma.

### Adlandirilmis Wedge

[Rakiplerin neden cozmedigi/cozemedigi spesifik insight. Yalniz "daha iyi UX"
ise prototiple test edilmesi gerektigini yaz.] Evidence: [CLAIM/EVIDENCE_ID]

### JTBD Forces ⚐ STANDARD+

| Push | Pull | Anxiety | Habit | Goc Sonucu | Evidence |
|---|---|---|---|---|---|
| [aci] | [vaat] | [risk] | [aliskanlik] | gercek/belirsiz/fantezi | [ID] |

### Visual Intelligence ⚐ STANDARD+

| Rakip | URL/Tool | Tarih | Storefront | Akis | Mesaj/Pattern | Bos Aci | Evidence/Artifact |
|---|---|---|---|---|---|---|---|
| [app] | [link] | [tarih] | [geo] | onboarding/paywall | [pattern] | [wedge] | [ID/path] |

## 3. Fatal Gate Audit

| Gate | Durum | Gerekce | Evidence |
|---|---|---|---|
| LEGAL_BLOCKED | clear/blocked/unknown | [not] | [ID'ler] |
| CORE_FEASIBILITY_BLOCKED | clear/blocked/unknown | [not] | [ID'ler] |
| PLATFORM_BLOCKED | clear/blocked/unknown | [not] | [ID'ler] |
| SAFETY_ETHICS_BLOCKED | clear/blocked/unknown | [not] | [ID'ler] |

## 4. Iki Eksenli Degerlendirme

### Firsat Cekiciligi

| Boyut | Agirlik | Low | Base | High | Claim ID | Gerekce |
|---|---:|---:|---:|---:|---|---|
| Problem / Talep | [x] | [1-5] | [1-5] | [1-5] | [claim] | [not] |
| Monetizasyon / Ekonomi | [x] | [1-5] | [1-5] | [1-5] | [claim] | [not] |
| Rekabet / Wedge | [x] | [1-5] | [1-5] | [1-5] | [claim] | [not] |
| Dagitim Erisimi | [x] | [1-5] | [1-5] | [1-5] | [claim] | [not] |
| Tekrarlanan Deger / Retention | [x] | [1-5] | [1-5] | [1-5] | [claim] | [not] |
| Zamanlama | [x] | [1-5] | [1-5] | [1-5] | [claim] | [not] |
| Likidite / Cold Start | [x/0] | [1-5/null] | [1-5/null] | [1-5/null] | [claim] | [not] |
| **Toplam** | **100** | **[x/null]** | **[x/null]** | **[x/null]** | | |

Skor basari olasiligi degildir. Gerekli boyut null ise toplam yoktur.

### RAT ve Kanit Gucu

| Sira | Claim | Kategori | Impact | Uncertainty | Risk | Claim Grade | Product-Specific Davranis |
|---|---|---|---:|---:|---:|---|---|
| 1 | [claim] | [kategori] | [1-3] | [1-3] | [carpim] | A-D | evet/hayir |
| 2 | ... | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... | ... |

**Genel Kanit Gucu:** [top 3 minimumu]

**Karar matrisi sonucu:** [DECISION] — [kurala tek cumle referans]

## 5. Kanit Denetimi ⚐ STANDARD+

| Kontrol | Sonuc | Not |
|---|---|---|
| Primary/public gozlem dogru baglamda mi? | pass/fail/unknown | [not] |
| Kaynak kokleri bagimsiz mi? | pass/fail | [not] |
| Gelir kaniti davranis mi iddia mi? | [sonuc] | [not] |
| Goc davranisla destekli mi? | [sonuc] | [not] |
| Karsit kanit arandi mi? | [sonuc] | [not] |
| Gozlemden cikarima sicrama var mi? | [sonuc] | [not] |

## 6. Faz 5.5 Deney Sozlesmesi ⚐ TEST ADAYI STANDARD+

| Alan | Deger |
|---|---|
| experiment_id | [id] |
| claim_id | [en riskli claim] |
| Segment | [kitle] |
| Kanal/Recruitment | [kanal] |
| Yontem | interview/deposit/prototype/spike/concierge/channel/liquidity |
| Hedef Evidence | E1-E4 |
| Orneklem | [hedef + hesap] |
| Metrik | [ana metrik] |
| Esik ve Turetimi | [baseline/MDE/ekonomi baglantisi] |
| Guardrail | [etik/ekonomi/kalite] |
| Stopping Rule | [kural] |
| Pass Aksiyonu | [karar] |
| Fail Aksiyonu | [karar] |
| Gizlilik/Iade | [aciklama] |

Universal CTR/email/yuzde guven esigi kullanma. Exploratory test BUILD_SMALL
uretemez.

## 7. Monetizasyon ve Kohort Ekonomisi

| Metrik | Pre-Launch Senaryo | First-Party Sonuc | Evidence/Grade |
|---|---|---|---|
| Fiyat/plan | [deger] | [varsa] | [ID/grade] |
| D30 ARPPU | [benchmark senaryo] | [varsa] | [ID/grade] |
| D90 ARPPU | [benchmark senaryo] | [varsa] | [ID/grade] |
| Payback | [senaryo] | [varsa] | [ID/grade] |
| CAC sonrasi brut katki | [senaryo] | [varsa] | [ID/grade] |
| First renewal/retention | [subscription ise] | [varsa] | [ID/grade] |
| AI kullanim maliyeti | [modifier varsa] | [varsa] | [ID/grade] |

Pre-launch LTV:CAC yalniz senaryodur; karar kaniti gibi sunma.

## 8. Risk, Security ve Operasyon

| Risk | Olasilik | Etki | Kanit | Test/Onlem |
|---|---|---|---|---|
| [risk] | [seviye] | [seviye] | [ID] | [aksiyon] |

### Security Preflight ⚐ STANDARD+

Admin auth/role, user ownership, frontend secret, RLS/backend rules, protected
field update, predictable ID ve public AI share secret scrub kontrollerini yaz.

### Turkiye Operasyon ⚐ GEREKIYORSA

Yalniz guncel resmi kaynakla tesvik/payout bilgisi yaz; kaynak yoksa BELIRSIZ.

## 9. BUILD_SMALL / Brief ⚐ STANDARD+

Faz 5.5 tamamlanmadiysa bu bolumu `PREBUILD_PENDING — kosullu taslak` olarak
isaretle. BUILD_SMALL yoksa gelistirme talimati verme.

- Max 4 core ekran
- Max 3 ana ozellik
- Gerekiyorsa 1 paywall/upgrade ekrani
- V1 disi liste
- Onceden yazilmis activation, retention ve ekonomi esikleri
- Default stack veya gerekceli alternatif

## 10. ASO ve Visual Hipotez ⚐ DEEP

| Alan | Hipotez | Evidence | Test |
|---|---|---|---|
| Name/subtitle/keyword | [deger] | [ID] | [test] |
| Screenshot mesaji | [deger] | [ID] | PPO/qualitative |
| Paywall/onboarding | [pattern] | [ID] | experiment |

## 11. Sonraki Adim

1. [Karar matrisinin zorunlu kildigi tek sonraki test/aksiyon]
2. [Kaniti kaydetme ve stopping rule]
3. [Karar tekrar hesaplama]

## 12. Cross-Report Karsilastirma ⚐ VARSA

Yalniz v4.0 raporlarini karsilastir.

| Fikir | Arketip | Fatal | Kanit | Firsat Low/Base/High | Top Risk | Test Maliyeti | Karar |
|---|---|---|---|---|---|---|---|
| [fikir] | [arketip] | [durum] | [A-D] | [x/x/x] | [claim] | [deger] | [karar] |

## Kaynak Ozeti

| Claim/Evidence | Kaynak | Erisim | Geo/Storefront | Seviye | Relevance |
|---|---|---|---|---|---|
| [ID] | [tiklanabilir URL] | [tarih] | [baglam] | E0-E4 | direct/supporting/weak |

Tam kanit: [data/evidence-ledger.md](data/evidence-ledger.md)

---

*Bu rapor App Idea Research Agent v4.0 ile olusturulmustur.*
