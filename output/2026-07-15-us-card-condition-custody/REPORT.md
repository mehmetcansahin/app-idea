# US Card Condition & Custody — Quick Scan

**Tarih:** 2026-07-15  
**Kapsam:** ABD / US App Store / iPhone  
**Arketip:** B2B/Prosumer  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

Bu fikir ilk düşündüğümüz kadar boş bir alan değil. CollX, Collectr ve LUDEX tarama/değer/portföyü; TCG Grading ise condition analysis, PDF certificate ve QR verification'ı zaten sunuyor. Bu nedenle “kartı tara ve sertifika üret” wedge'i elendi.

Kalan daha dar hipotez şudur: aktif raw-card satıcısı, listeleme anındaki köşe/kenar/yüzey durumunu ve paketleme adımlarını tek zaman çizgisinde kaydedip alıcıya açılan bir **condition + custody passport** için ödeme yapar mı? Bu passport resmi grading veya marketplace garantisi değildir.

## Kim, hangi anda kullanir?

- Segment: düzenli olarak daha yüksek değerli ungraded kart satan ABD'li iPhone kullanıcısı.
- Tetikleyici: ilanı hazırlama ve kargoyu kapatma anı.
- Capture: ön/arka, dört köşe, yüzey ışığı, sleeve/toploader, paket ve label.
- Çıktı: listing link'iyle eşlenen QR/web packet ve gönderim öncesi PDF.
- Değer iddiası: “resmi grade” değil; daha açık disclosure, daha az tekrar fotoğraf isteği ve uyuşmazlıkta düzenli kayıt.

## Dogrudan gozlemler

- [eBay Authenticity Guarantee](https://www.ebay.com/help/selling-tools/ebay-authenticity-guarantee/ebay-authenticity-guarantee?id=4644) $250+ uygun kartları authentication sürecine alıyor ve condition listing ile uyuşmazsa refund/return uygulanabileceğini belirtiyor.
- [eBay condition guidance](https://www.ebay.com/help/selling/selling-tools/seller-programs/ebay-authenticity-guarantee?id=4765) condition'ın doğru seçilmesini ve kusurların açıklanmasını istiyor.
- [TCG Grading](https://apps.apple.com/us/app/tcg-grading-card-ai-scanner/id6742651049) condition analizi yanında PDF certificate, certificate number, QR verification ve secure register sunuyor; aylık $12.99 Pro ve $24.99 Pro Plus listeliyor.
- [CollX](https://apps.apple.com/us/app/collx-sports-card-scanner/id1581164444) 44K US rating, marketplace ve seller tools ile çok güçlü komşu incumbent.
- [LUDEX](https://apps.apple.com/us/app/ludex-sports-card-scanner-tcg/id1616691213) scan/price/collection/list-on-eBay akışını kapsıyor.

## Cikarim

Kart grading doğruluğunda rekabet etmek yüksek veri ve güven maliyeti yaratır. İlk test yalnız capture checklist, immutable original hash, listing reference, packing chain ve buyer-open analytics üzerine kurulmalı. “Dispute kazanmayı garanti eder” veya “resmi grade” söylemi kullanılmamalı.

## Rakip ve ikameler

| Urun/ikame | Gozlenen kapsam | Bu fikir icin anlamı |
|---|---|---|
| CollX | Scan, price, portfolio, marketplace, seller tools | Büyük incumbent ve dağıtım duvarı |
| Collectr | Portfolio ve price tracking | Koleksiyon kaydı zaten güçlü |
| LUDEX | Scan, track, eBay listing | Seller workflow örtüşüyor |
| TCG Grading | AI condition, PDF, QR verification | Certificate wedge'ini doğrudan kapatıyor |
| Mint | AI grading ve collection sharing | Basit grading kalabalık |
| GradeX | Sports-card scanning/grading | Yeni entrant baskısı |
| Card Grading AI | AI grade | Düşük bariyerli feature alanı |
| Center Stage | Card identification | Ücretsiz/adjacent scan ikamesi |
| Sports Card Investor | Price and market data | Power-seller bütçesi için rakip |
| eBay listing photos | Fotoğraf + description + messages | Ücretsiz ve yerleşik ana ikame |

## Review sinyali ve protokol siniri

Apple'ın açık RSS akışındaki en güncel 50'şer US review incelendi:

- CollX (2026-06-22–2026-07-13): 1–2 yıldız 20, 3 yıldız 1, 4–5 yıldız 29. Keyword-coded örneklemde scan/recognition 20/50, marketplace/selling 16/50, price/paywall 13/50.
- LUDEX (2026-05-13–2026-07-13): 1–2 yıldız 22, 3 yıldız 6, 4–5 yıldız 22. Scan/recognition 23/50, price/paywall 19/50, bugs/access 5/50.

Bu kodlama yalnız incelenen, self-selected review örneklemine aittir. CollX'te yalnız bir 3-star review bulunması ve TCG Grading/Mint gibi yakın ürünlerde 15 kamuya açık review'a erişilememesi nedeniyle formal Standard stratification tamamlanmadı.

## Skor

| Boyut | Low | Base | High | Gerekce |
|---|---:|---:|---:|---|
| Problem/talep | 2 | 3 | 4 | Condition mismatch gerçek; ürün-spesifik sıklık bilinmiyor |
| Monetizasyon | 2 | 3 | 4 | Collector app fiyatları yüksek; custody için ödeme yok |
| Wedge | 1 | 2 | 3 | Certificate/QR dolu; packing chain daha dar boşluk |
| Dağıtım | 2 | 3 | 3 | Seller communities var; incumbents kanalı sahiplenmiş |
| Tekrar değeri | 2 | 3 | 4 | Aktif satıcıda ilan başına tekrar; casual collector'da zayıf |
| Zamanlama | 2 | 3 | 3 | Kamera/verification hazır; alan hızlı kalabalıklaşıyor |

**Fırsat Çekiciliği:** **37 / 57 / 73 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear, resmi grading/marketplace affiliation iddiası yapılmazsa.
- Core feasibility: clear; rakipler capture/certificate akışının yapılabilirliğini gösteriyor.
- Platform: clear; camera, local media ve sharing için bilinen yol var.
- Safety/ethics: clear; seller/buyer PII minimum tutulmalı ve kanıt sonucu garanti edilmemeli.

## Sonraki gercek davranis testi

On aktif ABD raw-card satıcısına **$19 ücretli concierge pilot** sat. En az 30 gerçek listing için condition + packing passport hazırla; buyer açılışlarını, ek fotoğraf sorularını ve return/dispute sırasında kullanımını izle.

**Stop:** 5'ten az satıcı ödeme yaparsa, iki haftada 50'den az passport oluşursa veya 10 buyer-side open/question ve 2 gerçek dispute/return kullanımı görülmezse durdur.

Bu masa başı karar build izni değildir.
