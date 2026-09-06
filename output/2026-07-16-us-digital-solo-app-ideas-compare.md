# Tamamen Dijital, Tek Geliştiricilik iOS Fikirleri — Karşılaştırma

**Tarih:** 2026-07-16  
**Geo / platform:** ABD / US App Store / iPhone-first  
**Metodoloji:** v4.0 Quick Scan karşılaştırması  
**Kurucu sınırı:** Tek geliştirici; fiziksel operasyon, ekip, inventory, hizmet teslimi veya marketplace yok

## Kısa cevap

Bugün tam uygulama geliştirmeye başlamazdım. İlk yapacağım iş **Voice Memo Archive için 1–2 günlük metadata + 2 GB batch teknik RAT'ı** olurdu. Geçerse en iyi solo ürün hipotezi o olur; kalırsa doğrudan elenir ve **Vertical Video Preflight** kullanıcı testine geçilir.

Teknik gate'i bugün açık olan en güçlü ürün adayı **Vertical Video Preflight**. Fakat generic safe-zone app değil; cihaz içinde final-export lint olmalıdır. **Shortcuts Payload Inspector** en küçük build'dir ama native/free substitutes nedeniyle üçüncü sırada ve park edilmeye en yakın adaydır.

Önceki Quilt/Resin/Laser shortlist'i fiziksel workflow'a bağlıydı. Araştırma dosyaları tarihsel olarak korunuyor, fakat kullanıcının yeni “işletmesi de tamamen dijital” sınırı için artık uygun shortlist değildir.

## Research Contract

- Segment: ABD'li iPhone power user veya bireysel profesyonel.
- İş modeli: App Store üzerinden one-time purchase veya düşük fiyatlı IAP; first-party tekrar kanıtı olmadan subscription yok.
- Operasyon: On-device/local-first; zorunlu backend, content moderation, customer marketplace, scraping veya insan hizmeti yok.
- Solo MVP: En fazla 4 core ekran, 3 ana özellik, 6–8 hafta.
- Erken eleme: Regulated/medical/fintech, high-liability accuracy, UGC/community, canlı içerik treadmill'i, pahalı generative AI ve fiziksel entegrasyon.

## Sonuç tablosu

| Sıra | Fikir | Fatal gate | Low / Base / High | Kanıt | Desk kararı | Solo operasyon | Net aksiyon |
|---:|---|---|---:|---|---|---|---|
| 1 | Vertical Video Preflight | Tümü clear | 52 / 63 / 72 | C | TESTE_DEGER | Orta: preset + false-positive desteği | Gate-cleared ilk aday; 12 editor testi |
| 2 | Shortcuts Payload Inspector | Tümü clear | 43 / 60 / 63 | C | TESTE_DEGER | Düşük | Yalnız native benchmark'ı aşarsa |
| 3 | Voice Memo Archive | Core feasibility unknown | 52 / 66 / 72 | C | BELIRSIZ | Geçerse düşük | En ucuz ilk öğrenme: teknik RAT |

Üçü de aynı B2B/Prosumer ağırlıklarıyla puanlandı. Yine de ham skor tek başına sıra değildir: fatal gate önce gelir. Voice Memo'nun base skoru yüksek olsa da nullable metadata ve Share Extension batch güvenilirliği kapanmadan ürün adayı sayılamaz.

## 1. Vertical Video Preflight

**Ürün:** Share Sheet'ten final MP4/MOV alır; TikTok/Reels/Shorts için media specs, black/freeze/silence ve OCR safe-zone risklerini cihazda tarar.

**Neden rekabet edilebilir:** Previewly/CaptionSafe safe-zone'u, CodecAudit metadata'yı çözüyor; dar hipotez bunları tek local “publish gate”te birleştirmek. [Güncel creator vakası](https://www.reddit.com/r/NewTubers/comments/1tei9ym/what_do_yall_use_to_make_sure_your_shorts/) gerçek desktop-to-mobile mismatch gösteriyor. [Previewly](https://apps.apple.com/us/app/previewly-video-safe-zone/id6748048131) ve [CodecAudit](https://apps.apple.com/us/app/codecaudit-media-metadata/id6759266682) ise generic konumların dolu olduğunu gösteriyor.

**Killer risk:** False positives ve incumbent feature expansion. Kullanıcı “intentional black frame”i sürekli dismiss ederse ürün güveni kaybolur.

**Test:** 12 editor, 60 video; kontrollü sorun recall >= %90, clean videoda yanlış critical <= %10, 6 gerçek düzeltme, 6 ikinci kullanım, 4 adet $9.99 refundable preorder. Ayrıntı: [Quick Scan](2026-07-16-us-vertical-video-preflight/REPORT.md).

## 2. Shortcuts Payload Inspector

**Ürün:** Aynı item'ın Photos/Safari/Files tarafından verilen UTI/MIME/file representations'ını capture eder, karşılaştırır ve sanitized report üretir.

**Neden ancak koşullu:** Problem ayrıntılı kullanıcı örnekleriyle gerçek; fakat Apple built-in Get Type/View Content Graph, ücretsiz [Actions](https://apps.apple.com/us/app/actions/id1586435171), [Logger](https://apps.apple.com/us/app/logger-for-shortcuts/id1611554653) ve [Shortcuts Debugger](https://apps.apple.com/us/app/shortcuts-debugger/id6761784989) işin büyük bölümünü yapıyor.

**Killer risk:** Ürün yeni bilgi değil, yalnız daha güzel format üretir. Ayrıca host representation'ı görebilir; Shortcuts'ın sonraki tüm coercion'larını göremez.

**Test:** 10 power user; en az 6 vakada native/free araçların göstermediği çözümleyici fark, 5 ikinci debug session, 4 adet $4.99 refundable preorder. Ayrıntı: [Quick Scan](2026-07-16-us-shortcuts-payload-inspector/REPORT.md).

## 3. Voice Memo Archive

**Ürün:** Apple Voice Memos seçimini original audio + date-aware filename + CSV/JSON + checksum receipt olarak arşivler; missing metadata'yı uydurmaz.

**Neden hâlâ ilginç:** 200, 3.000+ ve gigabaytlarca memo için tarih/isim koruma problemleri 2026'da raporlanıyor. Dar Voice Memos araçlarına ödeme proxy'si var. [Merge Voice Memos](https://apps.apple.com/us/app/merge-voice-memos/id6476123178) $4.99 ve 514 US rating gösteriyor. [Voice Memo Exporter](https://www.voicememoexporter.com/) Mac'te çok benzer arşiv işini $49'a listeliyor.

**Neden bugün `BELIRSIZ`:** Apple `creationDate` değerinin nil olabileceğini söylüyor ve Share Extension'ların düşük memory limitleri var. Yakın rakip [Aurloom](https://apps.apple.com/us/app/aurloom-audio-archive/id6762100529) da artık audio archive/import/iCloud alanında. iMazing güçlü desktop ikamesi.

**Test:** Önce 50 memo'da >= %95 doğru tarih kapsaması, 0 yanlış tarih, %100 missing flag ve 2 GB job'da termination sonrası resume. Teknik test kalırsa elenir; geçerse 12 kullanıcıdan 5 adet $9.99 refundable preorder. Ayrıntı: [Quick Scan](2026-07-16-us-voice-memo-archive/REPORT.md).

## Bilerek elenen mobil fikir alanları

- Generic screenshot/PII redaction, image diff, PDF compare: çok sayıda exact utility ve düşük wedge.
- Generic App Store screenshot/localization, link preview, UTM checker: free web araç ve bundle rekabeti.
- Return-window tracker: 2026'da çok sayıda yeni giriş; Gmail/receipt erişimi ve privacy yükü.
- Voice memo transcription/summarization: crowded, AI variable cost ve Apple native expansion riski.
- Generic safe-zone preview: Previewly, CaptionSafe, VEED ve ücretsiz template'ler.
- Generic Shortcuts logger/debugger: Logger, Shortcuts Debugger, Toolbox Pro ve Actions.
- Screen-recording privacy scrub: false-negative liability ve mevcut blur/video redaction araçları.
- Subtitle QC: editörlerin ve Captionista benzeri araçların içine gömülü.
- Marketplace, community, creator network, physical service workflow ve inventory/hardware fikirleri: yeni kurucu sınırına uymuyor.

## Önerilen araştırma sırası

1. **Voice Memo teknik RAT — 1–2 gün.** Kod yazma maliyeti düşük; gate'i net şekilde açar veya fikri öldürür.
2. Geçerse Voice Memo çalışan demo + payment davranışı; kalırsa **Vertical Video Preflight** video corpus RAT + 12 editor testi.
3. InputScope yalnız mevcut Shortcuts power-user erişimi varsa ve 10 kullanıcıyı hızlı bulabiliyorsan çalıştır; aksi halde park et.
4. Hiçbirinde refundable payment + tekrar davranışı olmadan 6–8 haftalık MVP'ye girme.

## Kanıt sınırları

App Store fiyat/rating revenue veya retention değildir. Community kaynakları self-selected'dır. Vendor ürün sayfaları satış kanıtı değildir. `not_found_after_protocol` market absence değildir. Low/base/high skorlar başarı olasılığı değildir. Masa başı `TESTE_DEGER` build izni vermez; `BELIRSIZ` ise teknik gate kapanmadan kullanıcı testi bile ana kararı çözmez.

Hesaplama denetimi: [scoring notebook](2026-07-16-us-digital-solo-app-ideas-report/analysis/scoring.ipynb).
