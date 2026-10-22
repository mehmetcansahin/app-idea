# Okur İncelemesi

<!--
Standard ve Deep raporlarda zorunlu: data/reader-review.md olarak kaydedilir.
Kurallar: methodology/report-writing.md §13. Bu yorum bloğunu kopyalama.
- İnceleyen, raporu yazan değildir (ayrı alt ajan veya kişi).
- Rapor önce yalnız REPORT.md okunarak değerlendirilir; data/ ve phases/ yalnız iddia kontrolü için açılır.
- İncelenen revizyon, incelemenin hangi rapora ait olduğunu kanıtlar. İnceleyen, güncel REPORT.md'yi baştan sona okuyup iddiaları kontrol ettikten SONRA `python3 scripts/evidence_tool.py revision <çıktı-klasörü>` çalıştırır ve çıkan 64 karakterlik özeti tek satır olarak yazar: `- İncelenen revizyon: <özet>`. Özet; REPORT.md'nin yazılan metnini (üretilen "## Özet" bölümü hariç) ve data/evidence.jsonl kayıtlarını kapsar.
- Raporun yazılan metni veya bir kanıt kaydı değişirse revizyon eskir ve validate hata verir; inceleyen değişen raporu yeniden okuyup iddiaları yeniden kontrol etmeden yeni özeti yazamaz. `render` yalnız "## Özet" bölümünü ve ilk "## Ek" başlığından önceki boşluğu (tek boş satır) yeniden yazar; revizyon bu boşluğu aynı biçimde normalleştirdiği için ilk `render` de sonrakiler de revizyonu değiştirmez. Başka yerdeki boşluk değişiklikleri yazılan metin değişikliği sayılır. Bu dosyaya hiçbir komut kendiliğinden revizyon yazmaz.
- Ölçüt sonucu yalnız GEÇTİ veya KALDI olur. KALDI kalan veya Durumu "Açık" olan sorun varsa validate hata verir.
- Sorun düzeltildiğinde Durum "Düzeltildi" yapılır; düzeltilmeyecekse "Kabul edilmedi" yazılır ve Çözüm sütununa gerekçe girilir.
- İddia kontrolünde en az 10 FARKLI iddia gerekir. Bir iddiayı "İddia" metni ile "Yer" birlikte tanımlar; büyük/küçük harf, boşluk ve Markdown biçimi (kalın, eğik, `kod`, bağlantı) farkı yeni iddia sayılmaz. Aynı iddiayı aynı yerde tekrar yazmak hatadır ve sayıma girmez. Aynı kanıt kaydı farklı iddiaları destekleyebilir.
- "Kanıt kaydı" sütununa yalnız data/evidence.jsonl'deki evidence_id değerleri yazılır (birden fazlaysa virgül veya noktalı virgülle ayrılır; ters tırnak kullanılabilir). Açıklama "Uyuyor mu?" sütununa girer. Kaydı olmayan veya bilinmeyen kimlik yazılan satır hatadır.
-->

- İnceleyen: [bağımsız okur; raporu yazan ajan/kişi değil]
- Tarih: [YYYY-MM-DD]
- Yöntem: [Rapor yalnız REPORT.md okunarak değerlendirildi; iddia kontrolü için data/evidence.jsonl açıldı.]
- İncelenen revizyon: [okuma ve iddia kontrolü bittikten sonra `python3 scripts/evidence_tool.py revision <çıktı-klasörü>` çıktısı]

## Ölçütler

| Ölçüt | Sonuç | Not |
|---|---|---|
| **Kapsam** — Başlık, kapsam ve sonuç aynı ürünü tarif ediyor; kapsam dışı ihtiyaçlar sonuca genellenmiyor. | [GEÇTİ / KALDI] | [satır referansı] |
| **Akış** — Rapor sorundan karara ilerliyor; her numaralı bölüm sorusuyla açılıp üç etiketli sonuç kutusuyla kapanıyor. | | |
| **Bulgular** — Her bulgu ne gözlemlendiğini, ürün açısından anlamını ve neye varılamadığını söylüyor. | | |
| **Örnekler** — Kurgusal senaryolar ve gerçek kullanıcı deneyimleri ayrı etiketli ve kapsam içinde. | | |
| **Dil** — Cümleler tam; tablo hücreleri okurun tahmin etmesini gerektirmiyor; yazım tutarlı. | | |
| **Terim ve sayılar** — Terimler ilk geçtiği yerde açıklanmış; puan ölçeği, formül ve harf notları anlatılmış; ekonomik ifadeler kesin. | | |
| **Karar** — Ne önerildiği, hangi bulgulara dayandığı, neyin belirsiz olduğu ve hangi bilginin kararı değiştireceği açık. | | |
| **Kaynaklar** — Kararı etkileyen iddiaların yanında bağlantı var; kaynak türü (gözlem, şirket beyanı, bağımsız kaynak, varsayım, yorum) anlaşılıyor. | | |
| **Rakipler** — Rakiplerin ne yaptığı, ne kadar iyi yaptığı, neyi çözemediği, platformları, ne zamandır bu işte oldukları ve büyüklükleri anlatılmış. | | |
| **Pazar ve kanallar** — Pazar büyüklüğü, oyuncuların konumu, pazarlama ve organik kanallar, kanal hâkimiyeti, anahtar kelime ve reklam analizi var. | | |
| **Başarı ölçütü** — Okur her bölüm sonunda "ne öğrendim, neden önemli, karar nasıl etkileniyor, proje mantıklı mı?" sorularını yazara sormadan cevaplayabiliyor. | | |

## Bulunan sorunlar

| # | Yer | Sorun | Durum | Çözüm |
|---|---|---|---|---|
| 1 | [Bölüm / satır] | [sorun ve alıntı] | [Açık / Düzeltildi / Kabul edilmedi] | [yapılan düzeltme veya gerekçe] |

## İddia kontrolü

Raporun farklı bölümlerinden en az 10 farklı iddia (iddia metni + yer) seçilir ve kanıt kayıtlarıyla karşılaştırılır.

| İddia | Yer | Kanıt kaydı | Uyuyor mu? |
|---|---|---|---|
| [rakam veya cümle] | [Bölüm / satır] | [evidence_id; birden fazlaysa virgülle] | [Evet / Düzeltildi / Hayır] |
