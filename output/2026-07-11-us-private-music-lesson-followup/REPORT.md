# US Private Music Lesson Follow-up — Quick Scan v4.0

## Karar

**TESTE_DEGER · PREBUILD_PENDING · düşük öncelik**

Problem haftalık ve gerçek; fakat fikir neredeyse birebir rakiplerle dolu. Yalnız
**30 saniyelik öğretmen notu → öğretmen onaylı practice checklist + veli özeti** olarak,
çocuk hesabı ve yeni parent app'i olmadan ucuz test yapılmalı. Build izni yoktur.

## Araştırma kontratı

- Geo/storefront/platform: ABD / US App Store / iOS-first
- Segment: haftada en az 15 öğrencisi olan bağımsız private music teacher
- Arketip: `b2b_prosumer`
- Risk modifier'ları: `children`, `sensitive_data`, `ai_variable_cost`, `platform_dependency`
- Kullanım anı: dersler arasındaki 1–2 dakika → haftalık çalışma → sonraki ders öncesi
- İkame: LessonRelay, My Music Staff, Fons, Duet, Practice Space, e-mail/SMS

## Gözlenen sinyaller

- [MTNA](https://www.mtna.org/Membership.html) 17.000 üye bildiriyor;
  [demografisinde](https://www.mtna.org/Demographics.html) üyelerin %73'ü independent teacher.
  Türetilmiş yaklaşık 12.410 kişi yalnız association proxy'sidir.
- [MTNA practice rehberi](https://www.mtna.org/Practice.html) haftalık assignment, practice
  minutes, parent signature ve progress check öneriyor. Bu doğal tekrar döngüsüdür; ürün
  retention'ı değildir.
- [Studio-policy örneği](https://www.mtna.org/downloads/MembersOnly/22161_StudioPolicies.pdf)
  25 haftada 24 haftalık ders öngörüyor.

## Top 5 rakip

| Ürün | Resmi liste fiyatı | Çakışma |
|---|---:|---|
| [LessonRelay](https://lessonrelay.com/) | $9/ay | Ders yakalama, practice plan, parent update, next-lesson brief |
| [My Music Staff](https://www.mymusicstaff.com/pricing/) | $16,95/ay | Notes, assignments, portal, scheduling ve ödeme |
| [Fons](https://fons.com/pricing) | $19,95/ay | Scheduling, payment ve communication |
| [Duet](https://app.duetpartner.com/signup) | $14/ay veya $140/yıl | Student/repertoire/billing/admin |
| [Practice Space](https://www.practicespaceapp.com/) | $15,99/aydan | Assignment, media ve practice tracking |

LessonRelay önerilen akışı neredeyse birebir sunduğu için “AI recap” tek başına wedge değildir.
MTNA'nın [üye indirimlerinde](https://www.mtna.org/Membership_Discounts.html) My Music Staff,
Fons ve Duet zaten yer alıyor; bu hem erişilebilir kanal hem incumbent dağıtım gücüdür.

## Dar ürün hipotezi

1. Tam ders kaydı yerine öğretmenin 30 saniyelik voice memo'su.
2. Öğretmen review'ünden sonra practice checklist ve parent-safe digest.
3. Çocuk hesabı/yeni veli uygulaması olmadan e-mail, SMS veya incumbent'a export.
4. Sonraki ders öncesi tek ekran: son assignment + parent acknowledgement.
5. İlk üründe payment, scheduling ve otomatik pedagojik değerlendirme yok.

## v4.0 değerlendirme

| Boyut | Low | Base | High | Gerekçe |
|---|---:|---:|---:|---|
| Problem/talep | 3 | 3 | 4 | Haftalık döngü açık; ödeme ve ürün-spesifik kullanım yok |
| Monetizasyon/ekonomi | 1 | 2 | 3 | Yalnız rakip fiyatı ve vendor metriği |
| Rekabet/wedge | 1 | 1 | 2 | LessonRelay birebir; export-only mikro-wedge test edilmedi |
| Dağıtım erişimi | 2 | 3 | 3 | MTNA doğrudan kanal; incumbent'lar kanalda yerleşik |
| Tekrarlanan değer | 2 | 3 | 3 | Haftalık ders doğal döngü; ürün retention'ı yok |
| Zamanlama | 2 | 2 | 3 | Yapısal ürün göçü veya zaman penceresi bulunmadı |

**Fırsat Çekiciliği: 37 / 48 / 62 · borderline · Kanıt Gücü: C.**

## Gate ve guardrail'ler

Parent-owned, teacher-only ve çocuk hesabı olmayan MVP'de dört gate `clear` kabul edildi.
13 yaş altından ad, fotoğraf, video veya ses toplanırsa [FTC COPPA](https://www.ftc.gov/business-guidance/resources/childrens-online-privacy-protection-rule-six-step-compliance-plan-your-business)
yükümlülükleri doğar. Ürün öğretmen onayı olmadan öğrenci skoru, pedagojik öneri veya veliye
otomatik değerlendirme göndermemeli; ses ve sheet-music haklarını korumalıdır.
[Apple kuralları](https://developer.apple.com/app-store/review/guidelines/) ayrıca uygulanır.

## Sonraki gerçek davranış testi

Haftada 15+ öğrencisi olan 12 ABD'li iPhone öğretmeninde iki gerçek ders için concierge
follow-up üret. İlk örnekten sonra dört haftalık pilot için **$19 peşin** iste. İlerleme şartı:
4 ödeme, en az 3 öğretmenin üç haftada 6+ gerçek derste kullanması ve en az 2 yenileme.
Geçmezse broad companion ve payment modülünü ele.

## Kanıt ve sınırlamalar

MTNA üyeliği tüm ABD öğretmenleri değildir. Public kaynaklar ücretli iOS alt kümesini,
ürün retention'ını veya veli engagement denominator'unu vermiyor. Liste fiyatı bu yeni
ürüne ödeme değildir. Ayrıntılar: [kanıt defteri](data/evidence-ledger.md).
