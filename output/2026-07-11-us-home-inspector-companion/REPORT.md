# US Home Inspector Companion — Quick Scan v4.0

## Karar

**TESTE_DEGER · PREBUILD_PENDING**

ABD'de iPhone kullanan bağımsız home inspector için tam raporlama platformu değil;
mevcut Spectora, HomeGauge veya benzeri sisteme bağlanan **offline fotoğraf/ses yakalama,
kaynak izleme ve zorunlu insan onaylı export companion** test edilmeye değer. Build izni yoktur.

## Araştırma kontratı

- Geo/storefront/platform: ABD / US App Store / iOS
- Segment: bağımsız veya çok küçük ekipli home inspector
- Arketip: `b2b_prosumer`
- Risk modifier'ları: `regulated`, `sensitive_data`, `ai_variable_cost`, `platform_dependency`
- Kullanım anı: sahada fotoğraf ve sesli not yakalama → incumbent şablonuna taslak aktarım
- İkame: incumbent rapor yazılımları, kamera + dikte + manuel kopyalama, akşam masaüstü raporu

## Gözlenen sinyaller

- BLS'nin geniş inspector kategorisinde 2024'te 147.600 iş ve %5 self-employed payı var;
  aynı kaynak home inspectorların gündüz sahada çalışıp raporu akşam yazabildiğini belirtiyor.
- HomeGauge ve Inspector Toolbelt App Store yorumları mobil raporlamanın saat kazandırabildiğini,
  fakat kamera ve günlük saha güvenilirliğinin sorun olabildiğini gösteriyor. Bunlar küçük,
  self-selected örneklemlerdir.
- Ücretli workflow var: rakiplerin resmi liste fiyatları $50–$109/ay veya $7,50/iş bandında.
  Bu, bu companion'a ayrıca ödeme yapılacağını kanıtlamaz.

## Top 5 rakip/ikame

| Ürün | Resmi liste fiyatı | Yorum |
|---|---:|---|
| [Spectora](https://www.spectora.com/) | $109/ay veya $1.090/yıl | Full suite; güçlü incumbent |
| [HomeGauge](https://www.homegauge.com/one/pricing/) | $89/ay | Desktop + iOS companion |
| [Inspector Toolbelt](https://inspectortoolbelt.com/pricing/) | $79/ay | Mobil rapor ve back office |
| [Palmtech](https://www.palmtech.com/) | $50/ay veya $500/yıl | Mobil/web raporlama |
| [Tap Inspect](https://www.tapinspect.com/) | $7,50/iş veya $90/ay | iPhone/iPad saha raporu |

Spectora'nın HomeGauge'i 2026'da satın alması nedeniyle bu iki marka bağımsız talep
kökü sayılmamıştır.

## v4.0 değerlendirme

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem/talep | 3 | 4 | 4 | Akşam raporu ve mobil güvenilirlik için birden fazla sinyal |
| Monetizasyon/ekonomi | 2 | 2 | 3 | Yalnız rakip fiyatı ve vendor/public proxy |
| Rekabet/wedge | 2 | 3 | 3 | Full suite değil, incumbent'a kaynaklı capture/export |
| Dağıtım erişimi | 3 | 3 | 3 | InterNACHI/ASHI ve yerel referral ağları erişilebilir |
| Tekrarlanan değer | 3 | 3 | 3 | Her inspeksiyonda doğal döngü; ürün retention'ı yok |
| Zamanlama | 2 | 3 | 3 | AI ilgisi var, fakat meslek görünümü güçlü büyüme göstermiyor |

**Fırsat Çekiciliği: 51 / 60 / 65 · borderline · Kanıt Gücü: C.**

## Fatal gate ve sınırlar

Dört gate de bu dar kapsam için `clear`. Ürün defect teşhisi yapmamalı, inspector onayı
olmadan nihai rapor yayımlamamalı ve foto/ses kaynağı ile değişiklik geçmişini korumalıdır.
Incumbent export yapılamaması ticari olarak öldürücü olabilir, fakat masa başında teknik
imkânsızlık kanıtı yoktur.

## Sonraki gerçek davranış testi

8 ABD'li inspector ile, kişisel verisi silinmiş ikişer gerçek inspeksiyonda concierge
import-ready taslak üret. Katılım için sonraki beş rapora yönelik **$49 peşin/depozito** iste.
İlerleme şartı: sıfır uydurulmuş defect, notların en az %90'ının doğru bölüme düşmesi,
medyan en az 30 dakika doğrulanmış tasarruf, en az 6 ikinci kullanım ve en az 4 ödeme.
Herhangi bir kritik yanlış teşhiste veya dört ödemeden azında durdur.

## Kanıt ve sınırlamalar

Exact ABD bağımsız home-inspector sayısı yapısal olarak gözlenemiyor; BLS kategorisi daha
geniştir. App Store yorumları prevalans değildir. Ödeme sinyali web SaaS içindir, Apple IAP
harcaması değildir. Ayrıntılı kayıt: [kanıt defteri](data/evidence-ledger.md).

