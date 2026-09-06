# Faz 3 — Review Mining

## Protokol

- Storefront/platform: US / iOS App Store
- Kaynak: Apple Customer Reviews RSS, `sortby=mostrecent`
- Pencere: 2025-07-18–2026-07-18
- Top five app için hedef: 1–2★ ≥10, 3★ ≥5, 4–5★ ≥10
- Sayfalar: app başına 1–10; nominal 50 kayıt/sayfa, page 11 JSON dönmedi
- Review ID ile dedupe
- Star-only ratings review örneklemine eklenmedi

RSS non-random ve platform-cap'li olduğu için tema yüzdesi veya pazar prevalansı üretilmedi.

## Coverage

| App | All-time erişilebilir | Son 12 ay | 1–2★ hedef/erişim | 3★ hedef/erişim | 4–5★ hedef/erişim | Sonuç |
|---|---:|---:|---:|---:|---:|---|
| Photo Compare | 68 | 3 | 10 / 3 | 5 / 0 | 10 / 0 | Eksik |
| Instant Watermark | 83 | 1 | 10 / 1 | 5 / 0 | 10 / 0 | Eksik |
| Before and after compare | 54 | 7 | 10 / 7 | 5 / 0 | 10 / 0 | Eksik |
| Before After Effect | 117 | 0 | 10 / 0 | 5 / 0 | 10 / 0 | Eksik |
| Photo compare before and after | 0 | 0 | 10 / 0 | 5 / 0 | 10 / 0 | RSS sıfır kayıt |
| **Toplam** | **322** | **11** | **50 / 11** | **25 / 0** | **50 / 0** | **Protokol minimumu karşılanmadı** |

`1584081351` ürün sayfası bir review render etmesine rağmen RSS sayfa 1–10 sıfır verdi; kaynak protokolü korunarak bu review örnekleme alınmadı.

## Erişilen son 12 ay örneklemi

| App | Tarih/yıldız | Paraphrase | Kod |
|---|---|---|---|
| Photo Compare | 2026-06-23 / 1★ | Haftalık ücret reddediliyor | monetization |
| Photo Compare | 2026-05-28 / 1★ | Aylık yaklaşık $20 çok pahalı | monetization |
| Photo Compare | 2025-10-12 / 1★ | Full frame yerine fotoğrafın parçası çıkıyor | controls, export |
| Instant Watermark | 2025-10-02 / 2★ | Zoom/alignment yok, yaklaşık 0.4 MP export | controls, export |
| Before and after compare | 2026-05-09 / 1★ | Ücretli; Albums görünmüyor | monetization, source access |
| Before and after compare | 2026-05-06 / 1★ | Çok basic/seçenek az | controls |
| Before and after compare | 2026-01-21 / 1★ | Edit sırasında crash | stability |
| Before and after compare | 2025-09-13 / 2★ | Zor kullanım, sınırlı trial | monetization, UX |
| Before and after compare | 2025-09-08 / 1★ | Karmaşık UX, support/cancel bozuk | monetization, UX, support |
| Before and after compare | 2025-08-23 / 2★ | Crash ve free path yok | stability, monetization |
| Before and after compare | 2025-08-14 / 1★ | İptal sonrası ücret, yanlış support linki | monetization, support |

Tam kayıt: [review-sample.json](../data/review-sample.json).

## Tema sayıları — yalnız n=11

| Tema | Kodlanan review |
|---|---:|
| Monetization friction | 7 |
| Eksik kontrol/source erişimi | 4 |
| Export/framing/resolution | 2 |
| Crash/stability | 2 |
| UX complexity | 2 |
| Support/cancellation | 2 |

Bir review birden fazla temaya kodlanabildiği için toplam 11'i aşar.

## Gains

Son 12 ayda 3–5★ written review erişilemedi. Gains `not_found_after_protocol` olarak tutuldu. Bu, kullanıcıların olumlu sonuç yaşamadığı anlamına gelmez.

## Karara etkisi

Desteklenen kalite hipotezleri:

- Manual alignment/zoom fallback.
- Tam-kadraj ve yüksek çözünürlüklü export.
- Basit import flow ve crash-free render.
- Paywall'ı render sonunda sürpriz yapmayan şeffaf one-time teklif.

Desteklenmeyen iddialar:

- Kullanıcıların auto-align'ı en sevdiği gain olduğu.
- Bu feature için $9.99 ödeyeceği.
- Temaların category prevalence'i.

Review mining, wedge'i tanımlamaya yardımcı olur; ürün tercihini doğrulamaz.

