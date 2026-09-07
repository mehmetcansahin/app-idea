# US Voice Memo Archive — Quick Scan

**Tarih:** 2026-07-16  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** B2B / Prosumer  
**Metodoloji:** v4.0  
**Karar:** **BELIRSIZ**  
**Durum:** **DESK_RESEARCH_COMPLETE**

Kanıt kayıtları: [evidence ledger](data/evidence-ledger.md)

## Sonuç

Bu fikir **tam ürün geliştirmeye hazır değil**, fakat 1–2 günlük teknik RAT'a değer. Önerilen ürün yeni bir ses kayıt veya transkripsiyon uygulaması değil: Apple Voice Memos'tan kullanıcı tarafından seçilen kayıtları alıp orijinal sesi, bulunan başlık/tarihi, CSV/JSON manifest'i ve checksum içeren taşınabilir bir arşiv üretir; bulunmayan metadata'yı asla uydurmaz.

Problem sinyali güncel ve somut. Kullanıcılar 200, 3.000+ ve gigabaytlarca memo için dosya tarihinin kaybolduğunu veya isimlerin karıştığını bildiriyor ([memo-demand-files-metadata], [memo-demand-200], [memo-demand-3000]). Dar Voice Memos araçlarına ödeme sinyali de var: [Merge Voice Memos](https://apps.apple.com/us/app/merge-voice-memos/id6476123178) $4.99 ve 514 rating; [Combine Voice Memos](https://apps.apple.com/us/app/combine-voice-memos/id6759183190) $1.99 ve 30 rating gösteriyor ([memo-economics-merge], [memo-economics-combine]). Bunlar gelir veya bu ürünün fiyat doğrulaması değildir.

Belirsizliğin sebebi çekirdek teknik vaattir. Apple, media `creationDate` alanının `nil` olabileceğini söylüyor; Share Extension'ların bellek limiti düşük ve sistem tarafından sonlandırılabileceğini de açıkça belgeliyor ([memo-technical-metadata], [memo-technical-extension-limits]). Yüzlerce kayıt ve 2 GB batch güvenilir biçimde kuyruklanmadan “tarihleri koruyan toplu arşiv” satılamaz. Bu yüzden core-feasibility gate `unknown` ve masa başı karar zorunlu olarak `BELIRSIZ`.

## Kullanıcı, an ve JTBD

- Segment: Gazeteci, müzisyen, araştırmacı, içerik üreticisi veya arşiv meraklısı; Apple Voice Memos içinde en az 100 kaydı olan ABD'li iPhone kullanıcısı.
- Tetikleyici: Yeni telefona/bilgisayara geçiş, Windows'a yedekleme, proje teslimi veya “bu kayıtları uygulama dışında sahiplenmek istiyorum” anı.
- Mevcut iş: AirDrop, Files, iCloud sync, manuel yeniden adlandırma, iMazing veya Mac aracı.
- İstenen sonuç: Orijinallere dokunmadan, hangi alanların gerçekten korunduğu görülebilen, tekrar açılabilir ve denetlenebilir bir klasör/ZIP.
- Mobile-native an: Kaynak kayıtlar iPhone'daki Apple Voice Memos içindedir; çoklu seçim ve Share Sheet doğrudan giriş sağlar.

## Doğrudan gözlemler

- Apple, bir veya birden fazla Voice Memo'nun Rendered veya Editable biçimde paylaşılabildiğini belgeliyor ([memo-technical-multi-share], [Apple kılavuzu](https://support.apple.com/en-ie/guide/iphone/iph3d6dc359/ios)).
- Mayıs 2026'da bir kullanıcı iPhone'dan Windows'a metadata koruyan bir yöntem bilmediğini ve gigabaytlarca memo'su olduğunu yazıyor ([memo-demand-files-metadata], [kaynak](https://www.reddit.com/r/iphone/comments/1tg52vy/metadata_is_no_longer_preserved_when_saving_to/)).
- Mart 2026'da başka bir kullanıcı 200'den fazla memo'yu yedeklemek istediğini, AirDrop sonrası created/modified değerlerinin transfer zamanına döndüğünü bildiriyor ([memo-demand-200], [kaynak](https://www.reddit.com/r/applehelp/comments/1rrctu7/how_do_i_backup_voice_memos_to_macbook_while/)).
- Bir başka güncel konuşmada 3.000+ dosyalık library için bulk import ve isim koruma sorunu tarif ediliyor ([memo-demand-3000], [kaynak](https://www.reddit.com/r/ios/comments/1tq4s1j/voice_memos_labeling_issue_any_alternative_apps/)).
- [Aurloom](https://apps.apple.com/us/app/aurloom-audio-archive/id6762100529) güncel bir local-first ses arşivi; import, katalog ve iCloud sync sunuyor. $2.99/ay veya $19.99/yıl ve 5 rating gösteriyor ([memo-wedge-aurloom]).
- [Voice Memo Exporter](https://www.voicememoexporter.com/) Mac'te bulk export, tarih/başlık “where available”, CSV/JSON ve local archive için $49 erken erişim fiyatı listeliyor ([memo-economics-mac-price]).
- [iMazing](https://imazing.com/guides/how-to-save-and-export-iphone-voice-memos-to-your-computer) iPhone/iPad içindeki Voice Memos'u Mac/Windows'a toplu aktarabiliyor ([memo-wedge-imazing]).

## Çıkarım

Sorun var; fakat pazar boş değil. Savunulabilir wedge “audio archive” değil, **Apple Voice Memos için iPhone üzerinde açık eksik-metadata durumu + deterministik manifest + checksum receipt** kombinasyonudur. Exact kombinasyon arama protokolünde bulunmadı ([memo-wedge-search]); bu bir yokluk kanıtı değildir.

Kullanıcının ana ihtiyacı tarihse ve gerçek dosyaların büyük bölümünde tarih yoksa ürün değeri çöker. Teknik test pazarlama görüşmesinden önce gelmelidir. Ayrıca Apple export davranışını düzeltirse wedge daralır.

## Rakip ve ikameler

| Ürün / ikame | Gözlenen iş | Bu fikir için anlamı |
|---|---|---|
| Aurloom | Local-first audio archive, import, catalog, iCloud | En yakın iPhone archive rakibi; whitespace'i küçültüyor |
| Voice Memo Exporter | Mac bulk archive, dates where available, CSV/JSON | Ürün vaadinin doğrudan Mac ikamesi |
| iMazing | iPhone'dan Mac/Windows'a bulk export | Bilgisayar kullanmayı kabul eden segment için güçlü ikame |
| Merge / Combine Voice Memos | Share Extension üzerinden dar paid utility | Ödeme ve yayın proxy'si; farklı JTBD |
| AirDrop / Files / iCloud | Ücretsiz yerleşik yollar | En güçlü ücretsiz ikame; tarih davranışı tutarsız bildiriliyor |

## Solo MVP sınırı

**Dört core ekran:** Import Queue, Metadata Review, Filename Template, Export Receipt.

**Üç ana özellik:**

1. Share Sheet'ten küçük ve devam ettirilebilir batch'i App Group kuyruğuna kopyalama.
2. Embedded title/date/duration çıkarma; eksik ve şüpheli alanları açıkça işaretleme.
3. Orijinal audio + date-aware filename + `metadata.csv/json` + checksum manifest ZIP'i.

V1'de kayıt, transkripsiyon, özetleme, AI, cloud upload, iCloud sync, audio editing veya orijinal dosya silme yok. Teknik RAT geçerse SwiftUI + Share Extension + AVFoundation ile 6–8 haftalık scope makuldür. Büyük batch güvenilirliği geçmeden bu süre tahmini güvenilir değildir.

**Fiyat hipotezi:** $7.99–$12.99 lifetime. Bu, gerçekleşmiş ödeme değildir; adjacent araçların $1.99–$4.99 fiyatları üst fiyatı özellikle riskli kılar.

## Skor

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem / talep | 3 | 4 | 4 | Üç bağımsız büyük-library ve tarih/isim kaybı vakası |
| Monetizasyon | 2 | 3 | 3 | Paid adjacent araçlar var; archive ödemesi yok |
| Rekabet / wedge | 3 | 3 | 4 | Dar receipt wedge'i; Aurloom, iMazing ve Mac exporter güçlü karşı kanıt |
| Dağıtım | 3 | 4 | 4 | Voice Memo utility ASO self-report'u var; doğrulanmış CAC yok |
| Tekrar değeri | 2 | 2 | 3 | Büyük ilk job; sonrası episodik export |
| Zamanlama | 3 | 4 | 4 | 2026 tarih kaybı şikâyetleri; Apple fix riski |

**Fırsat Çekiciliği:** **52 / 66 / 72 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear — yalnız kullanıcının seçtiği dosyalar; third-party catalog veya scraping yok.
- Core feasibility: **unknown** — çoklu paylaşım ve nullable metadata API'si var, fakat gerçek Voice Memos UI tarihi kapsaması ve 2 GB extension batch'i test edilmedi.
- Platform: clear — iki güncel paid Voice Memos extension'ı yayın precedenti sağlıyor.
- Safety/ethics: clear — copy-only, local ve explicit missing-state scope'u; implementation security testi yine gerekir.

## İlk gerçek test

UI tasarlamadan önce küçük bir Swift komut/prototype hedefi:

1. iOS 17/18/26 kaynaklı 50 gerçek memo: yeniden adlandırılmış, edited, layered, Apple Watch ve eski kayıtlar.
2. Voice Memos UI'daki başlık/tarih ile extracted metadata'yı timezone normalize ederek karşılaştır.
3. En eski desteklenen cihazda 25 dosya ve toplam 2 GB batch'i App Group'a sırayla kopyala; zorla termination sonrası devamı doğrula.

Geçiş: **en az %95 doğru tarih kapsaması, sıfır yanlış tarih, eksik/şüpheli alanların %100 işaretlenmesi, 2 GB job'da kayıpsız resume**. Bunlardan biri kalırsa fikri `ELENDIR`; “dosyanın transfer tarihini original tarih gibi” sunma. Teknik gate geçerse 100+ memo'su olan 12 kullanıcıya çalışan demo ve **$9.99 iade edilebilir preorder** sun; en az 5 ödeme yoksa park et. Bu geçiş de tek başına `BUILD_SMALL` değildir; yeniden puanlama gerekir.

Teknik gate sözleşmesi: [phases/06-prebuild-plan.md](phases/06-prebuild-plan.md). Belge masa başında kapanan üç alt soruyu, kapanamayan iki ölçümü (gerçek tarih kapsaması ve 2 GB batch resume) ve G0 spike'ının ön-kayıtlı eşiklerini ayırır. Kullanıcı ve ödeme deneyleri gate `clear` olmadan açılmaz.

## Sınırlar

Community vakaları self-selected'dır. App Store rating'i revenue değildir. Seller fiyatı satış değildir. Exact ürün bulunamaması yokluk kanıtı değildir. Masa başı skor başarı olasılığı değildir. Bu rapor “tutacak app” garantisi vermez; en ucuz öldürücü testi belirler.
