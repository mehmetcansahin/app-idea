# Pipeline Tanimlari — 10 Faz

> Bu dosya her fazin KISA tanimini, girdisini, ciktisini ve gate kriterini icerir.
> Detayli prompt sablonlari icin: `prompt-templates.md`
> Detayli veri toplama adımlari icin: `data-collection-protocol.md`

---

## Faz 1: Problem Havuzu

**Amac:** 20-30 somut, tekrarlayan, mobilde cozulebilir problem belirle
**Girdi:** Kullanicinin belirttigi alan veya genel arama
**Cikti:** Problem listesi (her biri: kim, ne sorunu, mobilde mantikli mi, sik mi, para verir mi)
**Araclar:** Reddit, App Store 1-2 yildiz reviewlar, Google Trends, IndieHackers
**Sure:** ~2-3 saat

**Gate:** Min 15 problem, 3+ farkli kategori
**Basarisizlik:** Reddit "I wish there was an app for..." aramalari, App Store kotu yorum taramasi, farkli kategorilere genisle

---

## Faz 2: Keyword Cluster

**Amac:** Her problem icin 10-20 aranabilir keyword kumesi olustur
**Girdi:** Faz 1 problem listesi
**Cikti:** Keyword tablosu (5 tip: ana, kitle, sonuc, alternatif, uzun kuyruk)
**Araclar:** App Store Search Suggest, Google Trends, rakip title/subtitle
**Sure:** ~2-3 saat

**Gate:** Her problem icin min 10 keyword
**Basarisizlik:** Autocomplete, rakip title'lari, Reddit basliklarindan tamamla

---

## Faz 3: Hizli Pazar Tarama

**Amac:** Keyword cluster'larin gercek App Store verileriyle dogrulamasi
**Girdi:** Faz 2 keyword cluster listesi
**Cikti:** Her cluster icin lider app, rating, yildiz, fiyat, trend, pazar durumu
**Araclar:** WebSearch (site:apps.apple.com), WebFetch (App Store sayfalari), Google Trends
**Sure:** ~5 dk/cluster

**Pazar siniflandirmasi:**
- Rating > 10K = Guclu pazar
- 2K-10K = Orta pazar
- 500-2K = Mikro pazar (DIKKAT)
- < 500 = Pazar yok (ELEN)

**Gate:** Min 8 cluster gecmeli
**Basarisizlik:** Faz 1'e don, farkli kategorilerle genislet

---

## Faz 4: Rakip Analizi

**Amac:** Her cluster icin derinlemesine rakip incelemesi
**Girdi:** Faz 3'ten gecen cluster'lar
**Cikti:** Rakip matrisi, sikayet analizi, fiyat/ozellik karsilastirmasi, Reddit sentiment
**Araclar:** App Store (WebFetch), Reddit (WebSearch), Google Play (cross-check), Ad library (FB/Google ATC — browser otomasyonu; WebFetch calismaz)
**Sure:** ~30 dk/cluster

**8 Adim:**
1. Tam rakip listesi (min 5, ideal 10)
2. Her rakip icin tam metadata (App Store WebFetch)
3. Kotu yorum analizi (1-2 yildiz, min 10-20 yorum/rakip)
4. Reddit sentiment (min 3 farkli sorgu)
5. Fiyat karsilastirma matrisi
6. Ozellik karsilastirma matrisi
7. Google Play cross-check
8. Reklam istihbarati (FB Ad Library keyword + top rakip advertiser, Google ATC; browser yoksa WebSearch fallback)

**Gate:** Her cluster icin min 5 rakip analiz edilmis
**Basarisizlik:** Analizi tamamla, eksik veriyle puanlama yapma

---

## Faz 5: Firsat Puanlama (3 Katmanli)

**Amac:** Sistematik degerlendirme
**Girdi:** Faz 3-4 verileri
**Cikti:** Final skor tablosu
**Detay:** `scoring-model.md`
**Sure:** ~15 dk/cluster

**3 Katman:**
- K1: Pass/Fail (pazar var mi, erisilebilir mi, buyuyor mu, regulasyon asilabilir mi)
- K2: Agirlikli skor /100 (talep %25, gelir %25, rekabet %20, retention %15, zamanlama %15)
- K3: Fizibilite carpani (teknik x kurucu x regulasyon x MVP, her biri 0.6/0.8/1.0; regulasyon engeli yoksa 1.0 alir)
- Final = K2 × K3

**Esikler:** 60+ Guclu | 45-59 Orta | 30-44 Zayif | <30 Elen

**Gate:** Min 3 cluster 45+
**Basarisizlik:** Override kurallarini kontrol et, gerekirse Faz 1'e don

---

## Faz 5.5: Build-Oncesi Talep Dogrulama (Opsiyonel-Onerilen)

**Amac:** Kod yazmadan once talebi DAVRANISLA test et (landing page/fake-door + Mom-Test gorusmeleri)
**Girdi:** Faz 5'ten GO/SARTLI-GO cikan aday(lar)
**Cikti:** Davranis-bazli go/no-go + guven %; puanlama duzeltmeleri
**Detay:** `pre-build-validation.md`
**Sure:** ~20 saat (INSAN-aksiyonu; Claude landing kopyasi/gorusme kilavuzu yazar)

**Walling 2/20/200:** 2sa eleme (Faz 1-5) -> 20sa talep testi (bu faz) -> 200sa MVP (Faz 9)

**Gate:** GO icin guven >=%70 + en az 1 gercek davranis sinyali (sadece "kullanirim/begendim" YETMEZ -> RF-16)
**Basarisizlik:** Sadece beyan -> Talep/Gelir override (MAX 3); problem hic dogrulanamadi -> SISP (RF-17), Faz 8'e/1'e don
**Not:** Quick Scan'de opsiyonel; Standard/Deep'te GO adayi icin ZORUNLU. En gec Faz 9 oncesi tamamlanmali.

---

## Faz 6: En Iyi 5 Secim

**Amac:** 4 pratik filtre ile final secim
**Girdi:** Faz 5'ten 45+ cluster'lar
**Cikti:** En iyi 5 fikir (tanim, MVP suresi, fark, ucretli model)

**4 Filtre:** Anlatilabilirlik | MVP 2-4 hafta | Fark netligi | Ucretli model baglantisi

**Gate:** Min 3 fikir gecmeli
**Basarisizlik:** Faz 1'e don veya sinir degerlerini (40-44) yeniden incele

---

## Faz 7: Pazar Dogrulama

**Amac:** Gercek veriyle zorunlu dogrulama
**Girdi:** Faz 6'dan gecen finalistler
**Cikti:** Her finalist icin 4 dogrulama raporu
**Sure:** ~45 dk/finalist

**4 Dogrulama:**
1. Gercek rating kontrolu (App Store'dan teyit)
2. Indie gelir kaniti (min 4 farkli sorgu)
3. Kullanici goc sinyali (min 4 farkli sorgu)
4. Pazar raporu cross-check + Menopoz Testi

**Gate:** Min 2/5 GECTI
**Basarisizlik:** Veri kaynagi yetersizse derinlestir, fikirler zayifsa Faz 1'e don

---

## Faz 8: Capraz Karsilastirma

**Amac:** Finalistler arasi net siralama
**Girdi:** Faz 7'den gecen fikirler
**Cikti:** Karsilastirma tablosu + #1 secimi

**Oncelik sirasi:**
1. Kanitlanmis Talep (lider rating)
2. Indie Gelir Kaniti
3. Final Skor
4. MVP Kolayligi

**Gate:** Net #1 veya max 2 finalist
**Basarisizlik:** Detaylandir veya ek dogrulama topla

---

## Faz 9: Proje Brief + MVP + Moat

**Amac:** Kazanan icin eksiksiz proje dokumani
**Girdi:** Faz 8'den secilen finalist + tum onceki faz verileri
**Cikti:** Proje brief, MVP scope (max 4 ekran, 3 ozellik), Moat analizi, monetizasyon, ASO taslagi

**Moat turleri (0-3 puan):** Veri avantaji | Gecis maliyeti | Network etkisi | Hiz avantaji | Ekosistem kilit
- <5: Zayif moat | 5-10: Orta moat | 10+: Guclu moat

**Gate:** Tum alanlar dolu, Moat dahil
**Basarisizlik:** Tamamla, eksik bolum birakma

---

## Faz 10: Seytanin Avukati

**Amac:** Varsayimlari kirma, kor noktalari bulma, Go/No-Go
**Girdi:** Faz 9 proje brief + tum veriler
**Cikti:** Varsayim tablosu, Menopoz Testi, en kotu senaryolar, Go/No-Go kontrol listesi

**5 Varsayim Testi:**
1. Pazar buyuk ve buyuyor mu? (karsit kanit ara)
2. Kullanicilar oder mu? (ucretsiz alternatif yeterli mi?)
3. Farklilasma yeterli mi? (baskasi zaten yapti mi?)
4. Teknik olarak yapabilir miyiz? (API sinirlamalari?)
5. Zamanlama dogru mu? (buyuk rakip giriyor mu?)

**Go/No-Go kontrol listesi:**
- [ ] Olumcul kusur yok
- [ ] Min 3 varsayim GUCLU kanita sahip
- [ ] Indie gelir kaniti min 1
- [ ] Menopoz testi 3/5+ Evet
- [ ] En kotu senaryolarin hepsi icin Plan B var

**Gate:** Olumcul kusur yok
**Basarisizlik:** Pivot (ayni pazar farkli aci) veya Kill (Faz 1'e don)
