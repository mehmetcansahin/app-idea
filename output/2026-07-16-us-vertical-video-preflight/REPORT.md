# US Vertical Video Preflight — Quick Scan

**Tarih:** 2026-07-16  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** B2B / Prosumer  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanıt kayıtları: [evidence ledger](data/evidence-ledger.md)

## Sonuç

Teknik gate'i açık olan en güçlü aday **ClipLint / Vertical Video Preflight**. Ancak ürün “safe-zone app” olmamalı; o alan zaten [Previewly](https://apps.apple.com/us/app/previewly-video-safe-zone/id6748048131), [CaptionSafe](https://apps.apple.com/us/app/captionsafe/id6758465708) ve VEED tarafından dolduruluyor. Dar wedge: masaüstünde export edilen son MP4/MOV dosyasını iPhone'da, buluta göndermeden, TikTok/Reels/Shorts için **media spec + black/freeze/silence + OCR safe-zone** risklerinden geçirmek.

Bu fikir fiziksel operasyon, kullanıcı içeriği moderasyonu, marketplace veya sunucu gerektirmez. Buna karşılık platform preset güncellemesi ve false-positive desteği kalıcı dijital operasyon yüküdür. Masa başı araştırması build izni değil, gerçek video üzerinde ürün-spesifik teste izin verir.

## Kullanıcı, an ve JTBD

- Segment: Haftada en az üç kısa video yayınlayan ABD'li freelance editor, social media manager veya creator-business operator.
- Tetikleyici: DaVinci, Premiere, CapCut veya Canva'dan final 9:16 dosya çıktıktan hemen sonra, telefondan upload etmeden önce.
- Mevcut iş: Platforma private/draft upload, safe-zone PNG, ücretsiz web checker, MediaInfo/CodecAudit veya gözle tüm videoyu izleme.
- İstenen sonuç: Yayın sonrası fark edilen kapalı caption, yanlış codec veya istemsiz black/freeze/silence riskini son teslimde yakalamak.
- Mobile-native an: Final publish telefondan yapılır; checker share sheet'te son kapı olur.

## Doğrudan gözlemler

- Güncel bir TikTok kullanıcısı UI öğelerinin subtitle ve B-roll'u kapattığını, preview yolu aradığını yazıyor ([clip-demand-ui-cover], [kaynak](https://www.reddit.com/r/SocialMediaMarketing/comments/1tctz6v/how_do_you_edit_tiktok_videos_more_professionally/)).
- Başka bir editor, desktop'ta hazırladığı Shorts caption'ını telefonda like button altında gördüğünü ve iki web checker denediğini söylüyor ([clip-demand-shorts-caption], [kaynak](https://www.reddit.com/r/NewTubers/comments/1tei9ym/what_do_yall_use_to_make_sure_your_shorts/)).
- Güncel bir DaVinci kullanıcısı 9:16 H.264 MP4'ün Shorts olarak tanınmadığını, phone re-encode sonrası sonucun değiştiğini bildiriyor; root cause doğrulanmış değildir ([clip-demand-reencode], [kaynak](https://www.reddit.com/r/davinciresolve/comments/1uusd14/why_are_916_videos_exported_in_davinci/)).
- Previewly UI overlay/safe-zone ve $2.99/ay, $24.99/yıl teklif ediyor; US storefront'ta yalnız 1 rating gösteriyor ([clip-economics-previewly]).
- [CodecAudit](https://apps.apple.com/us/app/codecaudit-media-metadata/id6759266682) codec, resolution, FPS, audio ve subtitle metadata inspection'ı ve $4.99 Pro sunuyor; black/freeze/silence veya UI-zone OCR advertise etmiyor ([clip-wedge-codecaudit]).
- Apple Vision, OCR sonuçlarıyla bounding box döndürüyor ve işlemi cihazda yapabiliyor ([clip-technical-vision], [Apple dokümanı](https://developer.apple.com/documentation/vision/recognizing-text-in-images)).

## Çıkarım

Problem vardır, ancak generic safe-zone çözümü commoditized'dır. Wedge yalnız üç ayrı final-check işini tek local pass'te ve editör olmayan creator'ın anlayacağı severity ile birleştirirse yaşar. Exact iPhone kombinasyonu protokolde bulunmadı ([clip-wedge-search]); yakın web QC ürünleri ve mevcut iOS araçları nedeniyle bu, pazar boşluğu kanıtı değildir.

Black frame, freeze veya silence her zaman hata değildir. Ürün “platform kabul garantisi” veya “bu frame hatalı” dememeli; conservative **risk warning** vermeli ve kullanıcıya dismiss/confirm imkânı tanımalıdır.

## Rakip ve ikameler

| Ürün / ikame | Gözlenen iş | Bu fikir için anlamı |
|---|---|---|
| Previewly | UI overlay, safe zones, trim/export | Generic safe-zone wedge'ini kapatıyor |
| CaptionSafe | Safe zones, on-device processing, batch export | Local/privacy tek başına wedge değil |
| VEED iOS | Editör içinde platform safe zones | Existing workflow avantajı |
| CodecAudit | Media metadata inspection/report | Spec lint tarafının yakın iOS rakibi |
| AutoQC / FrameSense | Web tabanlı automated QC | Combined QC yenilik değil; mobile gate ve privacy test edilmeli |
| Private/draft upload + gözle izleme | Ücretsiz gerçek platform preview | En güçlü mevcut workflow |

## Solo MVP sınırı

**Dört core ekran:** Import, Platform Target, Findings, Report.

**Üç ana özellik:**

1. MP4/MOV codec, resolution, aspect, duration ve audio spec lint.
2. Sampled-frame/audio ile conservative black/freeze/silence riskleri.
3. Apple Vision OCR bounding box'larını versioned TikTok/Reels/Shorts UI bölgeleriyle karşılaştırma.

V1 yalnız 9:16, en fazla 3 dakika ve MP4/MOV destekler. Video editing, transkripsiyon, grammar AI, copyright/logo tespiti, cloud upload ve platform hesabına yayın yok. SwiftUI + AVFoundation + Vision ile 6–8 haftalık solo scope makuldür; accuracy/performance RAT sonucu süreyi değiştirebilir.

**Fiyat hipotezi:** $9.99 lifetime; ilk scan ücretsiz. Subscription yalnız first-party tekrar kullanım görülürse yeniden değerlendirilir.

## Skor

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem / talep | 3 | 3 | 4 | Üç güncel publish-mismatch vakası; prevalence yok |
| Monetizasyon | 2 | 3 | 3 | Adjacent IAP/subscription fiyatları; satış kanıtı yok |
| Rekabet / wedge | 2 | 3 | 3 | Safe zone ve specs ayrı ayrı dolu; combined local pass test edilmedi |
| Dağıtım | 3 | 3 | 4 | Kullanıcılar problem terimleriyle araç arıyor; CAC/ASO hacmi yok |
| Tekrar değeri | 3 | 4 | 4 | Aktif creator için her final export doğal döngü |
| Zamanlama | 3 | 3 | 4 | Sorun güncel, fakat hızlı yeni giriş ve incumbent expansion var |

**Fırsat Çekiciliği:** **52 / 63 / 72 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear — user-selected media ve versioned generic risk zones; brand asset kullanımı ayrıca incelenmeli.
- Core feasibility: clear — current iPhone apps media metadata okuyor; Apple on-device OCR ve bounding box sağlıyor. Accuracy henüz kanıtlanmış değildir.
- Platform: clear — safe-zone ve codec-inspection ürünleri US App Store'da yayında.
- Safety/ethics: clear — conservative preflight, içerik moderasyonu veya acceptance guarantee yok.

## Sonraki gerçek davranış testi

12 aktif editor'dan kişi başı son üç export'u al. Clean, gerçek problemli ve kontrollü hata eklenmiş en az 60 video üzerinde prototype çalıştır. Her finding'i insanla doğrula; 14 gün içinde yeni bir export geldiğinde ürünü yeniden kullanıp kullanmadığını izle. Sonunda ürünün hazır olmadığı açıkça belirtilerek **$9.99 iade edilebilir preorder** sun.

İlerleme eşiği:

- kontrollü sorunların en az %90'ını yakalama,
- clean videolarda en fazla %10 yanlış `critical`,
- uyarıların en az %85'inin editor tarafından doğru ve faydalı bulunması,
- en az 6 kullanıcının gerçek bir düzeltme yapması,
- en az 6 kullanıcının ikinci export'ta kendiliğinden dönmesi,
- en az 4 preorder.

Eşiklerden biri ciddi biçimde kalırsa durdur. Yalnız safe-zone veya yalnız metadata uygulamasına pivot etme; o alanlar zaten kalabalık. Geçiş `BUILD_SMALL` değildir; evidence B+ ve product-specific E3+ davranışla yeniden puanlama gerekir.

Deney sözleşmesi: [phases/06-prebuild-plan.md](phases/06-prebuild-plan.md). Sözleşme dört deneyi kapı sırasına dizer: ölçülebilir denominator'lı doğruluk corpus'u (G0), 12 editörlük gerçek export kohortu (E1), hatırlatmasız ikinci-export dönüşü (E2) ve iade edilebilir preorder (E3). `claim-demand` zaten B olduğu için ayrı deney açılmaz; frekans E1 içinde ölçülür.

## Sınırlar

Community örnekleri self-selected'dır. App Store fiyat ve rating'i revenue değildir. Platform safe zones ve upload kuralları değişir. Exact birleşik ürün bulunamaması yokluk kanıtı değildir. Skor başarı olasılığı değildir.
