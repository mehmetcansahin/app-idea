# US Shortcuts Payload Inspector — Quick Scan

**Tarih:** 2026-07-16  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** B2B / Prosumer  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanıt kayıtları: [evidence ledger](data/evidence-ledger.md)

## Sonuç

**InputScope / Shortcuts Payload Inspector** teknik olarak en küçük ve işletmesi en hafif aday, fakat wedge'i en zayıf. Ürün bir generic Shortcuts logger değil: aynı image/URL/file Photos, Safari ve Files'tan Share Sheet ile geldiğinde host'un sunduğu `NSItemProvider` representations, UTI/MIME, filename, size ve temel decoded değeri yan yana karşılaştırır; sanitized debug report üretir.

Problem gerçek. Kullanıcılar aynı içeriğin Image, Photo Media veya URL gibi farklı tiplere dönüştüğünü ve gerçek Share Sheet event'i sırasında workflow'u izleyemediklerini anlatıyor ([input-demand-type-confusion], [input-demand-debug-share]). Fakat Apple'ın View Content Graph / Get Type aksiyonları, ücretsiz [Actions](https://apps.apple.com/us/app/actions/id1586435171), $4.99 [Logger for Shortcuts](https://apps.apple.com/us/app/logger-for-shortcuts/id1611554653), $2.99 [Shortcuts Debugger](https://apps.apple.com/us/app/shortcuts-debugger/id6761784989) ve Toolbox Pro çözüm alanını sıkıştırıyor.

Bu nedenle masa başı `TESTE_DEGER` kararı yalnız çok ucuz bir native-substitute RAT'a izin verir. Ücretsiz üç-action Shortcut aynı bilgiyi veriyorsa fikri park etmek gerekir.

## Kullanıcı, an ve JTBD

- Segment: Ayda birden fazla complex Shortcut geliştiren power user veya client automation'ı yapan consultant.
- Tetikleyici: Shortcut aynı content ile bir host'ta çalışıp diğerinde bozulduğunda.
- Mevcut iş: Get Type, View Content Graph, Quick Look, Show Result, Logger, Actions Get UTI, clipboard/temp file.
- İstenen sonuç: Host'un gerçekten ne sunduğunu tek capture'da görmek, iki capture'ı farklarıyla karşılaştırmak ve kişisel değeri sızdırmadan yardım isteyebilmek.
- Mobile-native an: Sorun gerçek Share Sheet event'inde ve host app bağlamında oluşur.

## Doğrudan gözlemler

- Bir kullanıcı aynı Live Photo'nun cihaz ve host bağlamına göre Image, Photo Media veya URL olduğunu ayrıntılı örnekliyor ([input-demand-type-confusion], [kaynak](https://www.reddit.com/r/shortcuts/comments/1bd4mis)).
- Başka bir kullanıcı gerçek Share Sheet input'u geçerken Shortcut'ı step-by-step izleyemediğini, Quick Look/Alert/temp file workaround'ları kullandığını yazıyor ([input-demand-debug-share], [kaynak](https://www.reddit.com/r/shortcuts/comments/1g87noi)).
- Mart 2026 iOS 26.4 beta konuşmasında birden fazla kullanıcı Share Sheet input'unun hiç gelmediğini bildiriyor; bu güncel debug trigger'ı olduğu kadar platform bağımlılığıdır ([input-timing-ios264], [kaynak](https://www.reddit.com/r/shortcuts/comments/1rkpcxp/share_sheet_broken/)).
- Logger $4.99 ve 26 rating/4.8 gösteriyor; bir review $5 bedelin ilk Shortcut'ta zaman tasarrufuyla çıktığını söylüyor ([input-economics-logger]).
- Actions ücretsiz, 450 rating/4.8 gösteriyor ve Get UTI / UTI conformance aksiyonları sunuyor ([input-distribution-category]).
- Apple `NSItemProvider.registeredTypeIdentifiers` ile host'un kayıt ettiği type identifier listesini erişilebilir kılıyor ([input-technical-itemprovider], [Apple dokümanı](https://developer.apple.com/documentation/foundation/nsitemprovider/registeredtypeidentifiers)).

## Çıkarım

App yalnız host'un extension'a sunduğu representations'ı görebilir; Shortcuts'ın sonradan yaptığı her coercion'ı gözleyemez. Bu sınır ürün mesajının parçası olmalıdır. Yeni Shortcuts Debugger ve mevcut Logger generic logging wedge'ini kapatır; compare-by-host işinin exact ürünü protokolde bulunmadı ([input-wedge-search]), fakat yerleşik ve ücretsiz ikameler nedeniyle bu düşük güvenli bir whitespace'tir.

2026 beta bug'ı kalıcı pazar katalizörü sayılmamalıdır. Inspector “input gelmedi” diyebilir, işletim sistemi hatasını düzeltemez.

## Rakip ve ikameler

| Ürün / ikame | Gözlenen iş | Bu fikir için anlamı |
|---|---|---|
| View Content Graph / Get Type | Apple built-in inspection | Çekirdek vaadin ücretsiz benchmark'ı |
| Actions | Get UTI ve çok sayıda free action | Güçlü ücretsiz substitute, 450 rating |
| Logger for Shortcuts | Realtime logs, filters, export | Established paid incumbent |
| Shortcuts Debugger | JSON/image/file metadata logs | Yeni ve ucuz direct-adjacent competitor |
| Toolbox Pro | 130+ actions | Bundle economics ve güçlü installed base |

## Solo MVP sınırı

**Dört core ekran:** Captures, Payload Detail, Compare, Sanitized Export.

**Üç ana özellik:**

1. Share Extension'dan registered UTI/MIME, filename, byte size, URL/image/file basics capture.
2. Aynı content'in iki veya üç host capture'ını field-by-field compare.
3. Değerleri varsayılan olarak redact eden Markdown/JSON debug report.

V1'de cloud sync, community, Shortcut marketplace, remote logging, automation execution veya “Shortcuts internal debugger” vaadi yok. SwiftUI + Share Extension + Foundation ile 3–5 haftalık solo scope makuldür. Sensitive payload için ephemeral storage ve delete-on-export testleri gerekir.

**Fiyat hipotezi:** İlk 5 capture ücretsiz; $4.99–$7.99 lifetime. $7.99 üstü mevcut $2.99/$4.99 rakipler nedeniyle zayıf hipotezdir.

## Skor

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem / talep | 2 | 3 | 3 | Somut debug vakaları; küçük segment ve workaround var |
| Monetizasyon | 2 | 3 | 3 | Logger paid proxy; free Actions güçlü karşı kanıt |
| Rekabet / wedge | 2 | 3 | 3 | Host-compare dar wedge; built-in ve iki logger sıkıştırıyor |
| Dağıtım | 3 | 3 | 4 | r/shortcuts ve App Store terms erişilebilir; hacim/CAC yok |
| Tekrar değeri | 2 | 3 | 3 | Complex builder için tekrar; sıradan kullanıcı için episodik |
| Zamanlama | 2 | 3 | 3 | Aktif platform değişimi; beta bug'ına dayanmamalı |

**Fırsat Çekiciliği:** **43 / 60 / 63 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear — user-shared local payload; third-party catalog veya scraping yok.
- Core feasibility: clear — host registered type identifiers accessible; downstream Shortcuts internals scope dışı.
- Platform: clear — iki paid Shortcuts debugging ürünü yayında.
- Safety/ethics: clear — local ephemeral capture ve default redaction scope'u; implementation audit gerekir.

## Sonraki gerçek davranış testi

Güncel ve gerçek Share Sheet problemi olan 10 power user seç. Her biri aynı content'i en az üç host'tan built-in View Content Graph/Get Type, Actions Get UTI ve InputScope prototype ile incelesin.

İlerleme eşiği:

- en az 6 vakada prototype'ın ücretsiz benchmark'ların göstermediği ve sorunu çözmeye yarayan bir fark üretmesi,
- en az 5 kullanıcının ikinci debug oturumunda geri dönmesi,
- en az 4 kullanıcının **$4.99 iade edilebilir preorder** vermesi.

Tipik vakalar ücretsiz üç-action Shortcut ile çözülüyorsa veya prototype yalnız daha güzel biçimlendiriyorsa park et. Geçiş `BUILD_SMALL` değildir; ürün-spesifik davranışla yeniden puanlama gerekir.

## Sınırlar

Segment hacmi ölçülmedi. Community örnekleri self-selected'dır. Rating revenue değildir. Beta regression kalıcı olmayabilir. Exact ürün bulunamaması yokluk kanıtı değildir. Skor başarı olasılığı değildir.
