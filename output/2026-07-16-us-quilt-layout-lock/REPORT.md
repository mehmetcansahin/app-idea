# US Quilt Layout Lock — Quick Scan

**Tarih:** 2026-07-16  
**Kapsam:** ABD / US App Store / iPhone-first  
**Arketip:** Consumer Utility  
**Metodoloji:** v4.0  
**Karar:** **TESTE_DEGER**  
**Durum:** **PREBUILD_PENDING**

Kanit kayitlari: [evidence ledger](data/evidence-ledger.md)

## Sonuc

Bu taramadaki ilk test tercihi **Quilt Layout Lock**. Ürün quilt tasarlamaz; fiziksel olarak design wall veya zemine dizilmiş blokların, toplanırken ve satırlar dikilirken yönünün ya da sırasının bozulmasını engeller.

Neden ilk sırada: sorun iPhone kamerasının bulunduğu anda yaşanıyor, ilk sürüm AI veya bilgisayarlı görü gerektirmiyor, dört ekran ve üç özellikle kurulabiliyor ve hedef kullanıcıya quilt guild, mağaza eğitmeni ve quilting topluluklarından ulaşılabiliyor. En güçlü karşı kanıt ise aynı derecede nettir: telefon fotoğrafı, maskeleme bandı ve Post-it ücretsiz ve alışılmış ikamelerdir.

Bu nedenle masa başı araştırması build izni vermiyor. Önce gerçek bir quilt assembly seansında ürünün mevcut fotoğraf yönteminden daha fazla hata önleyip önlemediği ve kullanıcının bunun için ödeme yapıp yapmadığı görülmeli.

## Kullanici, an ve JTBD

- Segment: En az bir patchwork quilt'i blok/satır halinde birleştirmiş, design wall veya zemin kullanan ABD'li iPhone sahibi quilter.
- Tetikleyici: Bloklar doğru dizildikten hemen önce tasarımın toplanması veya ilk satırların dikilmesi.
- Mevcut iş: Referans fotoğrafı çekmek; sıra/sütun etiketi, iğne, maskeleme bandı veya Post-it kullanmak.
- İstenen sonuç: Yanlış yönlü veya yanlış sıradaki bloğu seam ripper kullanmadan önce fark etmek.
- Mobile-native an: Referans çekimi, yarı saydam kamera overlay'i ve satır checklist'i aynı fiziksel çalışma alanında kullanılır.

## Dogrudan gozlemler

- Quilter'lar blok sırasını korumak için telefon fotoğrafı, satır/sütun etiketleri, maskeleme bandı ve iğne gibi birden fazla manuel yöntem tarif ediyor ([quilt-demand-methods], [kaynak](https://www.reddit.com/r/quilting/comments/1342d91)).
- Bir kullanıcı yön hatasını quilting bittikten sonra fark ettiğini, yorumlardaki kullanıcılar ise referans fotoğrafı çekmeyi önerdiklerini gösteriyor ([quilt-demand-late-error], [kaynak](https://www.reddit.com/r/quilting/comments/196bawg)).
- Başka bir kullanıcı doğru blokların bir kısmını baş aşağı diktiğini bildiriyor ([quilt-demand-orientation], [kaynak](https://www.reddit.com/r/quilting/comments/1menlku)).
- [Quiltography](https://apps.apple.com/us/app/quiltography-quilt-design-made-simple/id585991997) ve [Quiltler](https://apps.apple.com/us/app/quiltler-quilt-designer/id1120958195) ücretli quilt tasarım ürünlerinin US App Store'da bulunduğunu gösteriyor; liste fiyatı ve rating ödeme/retention kanıtı değildir ([quilt-economics-quiltography], [quilt-economics-quiltler]).
- [Quiltler 3](https://apps.apple.com/us/app/quiltler-3-quilt-design/id6755831082) gibi yeni girişler dijital tasarım tarafının aktif kaldığını, aynı zamanda genel “quilt design app” konumunun kalabalıklaştığını gösteriyor ([quilt-timing-quiltler3]).

## Cikarim

Topluluk örnekleri problemin var olduğunu ve kullanıcıların davranışsal workaround geliştirdiğini destekliyor. Ancak örnekler self-selected'dır; hatanın segmentteki sıklığını veya uygulamaya ödeme isteğini ölçmez. App Store ürünleri quilt yazılımına ödeme yapılabildiği yönünde proxy'dir; bu dar fiziksel assembly ürününe talep kanıtı değildir.

## Rakip ve ikameler

| Urun / ikame | Gozlenen is | Bu fikir icin anlamı |
|---|---|---|
| Quiltography | Fotoğraftan/dijital quilt tasarımı | Ödeme proxy'si; assembly doğrulaması değil |
| Quiltler / Quiltler 3 | Blok tasarımı, layout ve renk | Genel design alanı kalabalık |
| Quilters DesignWall / QuiltFit / Quilt-a-lator | Dijital düzen veya matematik | Aynı kullanıcı bütçesine komşu |
| Telefon fotoğrafı | Ücretsiz referans | En güçlü ikame |
| Post-it, maskeleme bandı, pin | Fiziksel sıra/yön işareti | Sıfır onboarding ve sıfır fiyat |

### Arama protokolu

US App Store ve web için `quilt design wall app block order row orientation camera`, `quilt camera overlay block orientation design wall` ve exact-product sorguları çalıştırıldı. Fiziksel blok montajını referans overlay + satır doğrulama döngüsüyle çözen güncel bir exact ürün bulunamadı ([quilt-wedge-search]). Bu **yokluk kanıtı değildir**; yalnızca wedge hipotezini test etmeye değer kılar.

## Solo MVP siniri

**Dört core ekran:** Projects, Reference Capture, Row Mode, Compare.

**Üç ana özellik:**

1. Referans fotoğrafına satır/sütun ve yön işareti ekleme.
2. Canlı kamera üzerinde ayarlanabilir yarı saydam referans overlay'i.
3. Satır bazlı toplama/dikme checklist'i.

İlk sürümde otomatik blok tanıma, perspektif düzeltme vaadi, sosyal ağ, pattern marketplace veya AI hata skoru yoktur. SwiftUI + yerel fotoğraf saklama ile 6–8 haftalık solo build sınırına uygundur; bu süre yalnız teknik scope tahminidir.

**Fiyat hipotezi:** $7.99–$12.99 lifetime. Bu fiyat araştırma girdisidir, gerçekleşmiş ödeme değildir.

## Skor

| Boyut | Low | Base | High | Gerekce |
|---|---:|---:|---:|---|
| Problem / talep | 3 | 4 | 4 | Üç bağımsız davranış örneği ve manuel workaround |
| Monetizasyon | 2 | 3 | 3 | Yalnız komşu ürün liste fiyatı/rating proxy'leri |
| Rekabet / wedge | 3 | 3 | 3 | Dar fiziksel assembly işi var; prototip tercihi henüz yok |
| Dağıtım | 3 | 3 | 3 | Birden fazla adlandırılmış kanal var; traction/CAC yok |
| Tekrar değeri | 2 | 3 | 3 | Quilt proje döngülerinde episodik tekrar |
| Zamanlama | 2 | 3 | 3 | Kategori aktif; özel bir yapısal pencere yok |

**Fırsat Çekiciliği:** **54 / 65 / 65 — borderline**  
**Kanıt Gücü:** **C**

## Fatal gate

- Legal: clear — kullanıcı kendi fotoğrafını ve işaretlerini tutar; lisanslı pattern kataloğu kopyalanmaz.
- Core feasibility: clear — referans çekimi, manuel işaret ve overlay standart iOS yetenekleridir; otomatik tanıma scope dışıdır.
- Platform: clear — fotoğraf tabanlı quilt uygulamalarının US App Store'da bulunması yayın yolunu destekler.
- Safety/ethics: clear — ürün görsel organizasyon aracıdır; fiziksel/sağlık tavsiyesi vermez.

## Sonraki gercek davranis testi

İki turda dörder aktif quilter ile gerçek assembly seansında tıklanabilir veya concierge overlay prototipi kullan. Her kullanıcı mevcut fotoğraf/etiket yöntemiyle ve prototiple aynı işi yapsın. Görevden sonra ürünün hazır olmadığı açıkça belirtilerek **$9.99 iade edilebilir depozito** teklif et.

Bu test exploratory'dir; baseline ve population MDE bilinmediği için eşikler nüfus genellemesi üretmez. İlerlemek için sekiz kullanıcının en az dördü depozito bırakmalı ve en az üç kullanıcı prototipin gerçek bir yön/sıra hatasını dikmeden önce yakaladığını veya önlediğini göstermeli. Eşiklerden biri kalırsa fikri park et; geçerse ikinci doğal quilt döngüsünde tekrar kullanım testi ve yeniden puanlama yap. Tek test doğrudan build izni vermez.

## Kanit sinirlari

Community gönderileri seçilmiş örneklerdir. App Store rating ve fiyatları satış, gelir veya retention değildir. Exact rakip bulunamaması pazar boşluğunu kanıtlamaz. Segment büyüklüğü, kanal CAC'i ve ürün-spesifik ödeme davranışı masa başında gözlenemedi.
