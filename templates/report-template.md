# App Arastirma Raporu: [KONU]

> Tarih: [TARIH]
> Mod: Quick Scan / Standard / Deep
> Metodoloji: v3.1 (10 Faz, 3 Katmanli Puanlama)

---

## Yonetici Ozeti

| Alan | Deger |
|------|-------|
| **Karar** | GO / SARTLI GO / NO-GO / ELENDIR |
| **Final Skor** | X/100 (K2) × X.XX (K3) = **XX.X** |
| **Risk Seviyesi** | DUSUK / ORTA / YUKSEK / COK YUKSEK |
| **MVP Tahmini** | X hafta |
| **Anahtar Bulgu** | [1-2 cumle] |
| **Oneri** | [1-2 cumle] |

---

## 1. Pazar Analizi

### Pazar Durumu
| Gosterge | Deger | Etiket |
|----------|-------|--------|
| Ana Keyword | [keyword] | — |
| Lider Uygulama | [app adi] | — |
| Lider Rating | [sayi] | KESIN |
| Lider Yildiz | [X/5] | KESIN |
| Pazar Sinifi | Guclu / Orta / Mikro | — |
| Google Trends | YUKARI / DUZ / ASAGI | KESIN |
| Mevsimsellik | [varsa aciklama] | TAHMINI |

### Pazar Gecerliligi (Katman 1)
| Kriter | Sonuc |
|--------|-------|
| Pazar var mi? (rating > 500) | GECTI / KALDI |
| Erisilebilir mi? (Apple/Google engeli yok) | GECTI / KALDI |
| Buyuyor mu? (trend + yeni girisler) | GECTI / KALDI |
| Regulasyon asilabilir mi? (indie icin) | GECTI / KALDI |

---

## 2. Rakip Analizi

### Top 5 Rakip
| # | Uygulama | Rating | Yildiz | Fiyat | Model | Son Guncelleme |
|---|----------|--------|--------|-------|-------|----------------|
| 1 | [app] | [sayi] | [X/5] | [fiyat] | [model] | [tarih] |
| 2 | ... | ... | ... | ... | ... | ... |

### Sikayet Temalari (1-2 Yildiz Review Mining)
| # | Tema | Siklik | Ornek |
|---|------|--------|-------|
| 1 | [tema] | ~X yorum | "[ornek]" |
| 2 | ... | ... | ... |

### Fiyat Karsilastirmasi
| Metrik | Deger |
|--------|-------|
| [Rakip 1] | $X [model] |
| [Rakip 2] | $X [model] |
| ... | ... |
| **Ortalama aylik** | $X |
| **Medyan aylik** | $X |
| **Fiyat araligi** | $X — $X |
| **Lifetime sunan** | X/Y rakip |
| **Hakim model** | Tek seferlik / Abonelik / Freemium |

---

## 3. Firsat Puanlama

### Katman 2: Firsat Kalitesi (/100)
| Kriter | Agirlik | Skor (1-5) | Puan | Veri Kaynagi |
|--------|---------|-----------|------|-------------|
| Talep Sinyali | ×5 | [X] | [XX] | [kaynak + etiket] |
| Gelir Kaniti | ×5 | [X] | [XX] | [kaynak + etiket] |
| Rekabet Boslugu | ×4 | [X] | [XX] | [kaynak + etiket] |
| Retention | ×3 | [X] | [XX] | [kaynak + etiket] |
| Zamanlama | ×3 | [X] | [XX] | [kaynak + etiket] |
| **Toplam** | | | **[XX]** | |

**Uygulanan Override:** [varsa listele]

### Katman 3: Fizibilite Carpani
| Kriter | Skor | Gerekce |
|--------|------|---------|
| Teknik Zorluk | [0.6/0.8/1.0] | [aciklama] |
| Kurucu Uyumu | [0.6/0.8/1.0] | [aciklama] |
| Regulasyon/Uyum | [0.6/0.8/1.0] | [aciklama — 1.0 ise regulasyon yok] |
| MVP Suresi | [0.6/0.8/1.0] | [aciklama] |
| **Carpan** | **[X.XX]** | |

### Final Skor
**[K2 Toplam] × [K3 Carpan] = [Final Skor]** → [Guclu (60+) / Orta (45-59) / Zayif (30-44) / Elendir (<30)]

---

## 4. Gelir Potansiyeli

### Indie Gelir Kaniti
| # | Kim | Uygulama | Gelir | Kaynak | Guvenilirlik |
|---|-----|----------|-------|--------|-------------|
| 1 | [developer] | [app] | [miktar] | [kaynak] | KESIN/TAHMINI/DUSUK |

*Bulunamadiysa: "X farkli sorgu yapildi, indie gelir kaniti BULUNAMADI"*

### Fiyat Modeli Onerisi
| Plan | Fiyat | Icerik |
|------|-------|--------|
| Ucretsiz | $0 | [icerik] |
| Premium | $X/ay | [icerik] |
| Yillik | $X/yil | [icerik] |

---

## 5. Dogrulama ⚐ STANDARD+

### 4 Dogrulama Kontrolu
| # | Kontrol | Sonuc | Guvenilirlik |
|---|---------|-------|-------------|
| 1 | Lider rating gercek mi? | [sonuc] | KESIN |
| 2 | Indie gelir kaniti | [sonuc] | [etiket] |
| 3 | Kullanici goc sinyali | [sonuc] | [etiket] |
| 4 | Menopoz Testi | GECTI / KALDI / UYGULANAMADI | [etiket] |

**Dogrulama Sonucu:** DOGRULANDI / KISMI / DOGRULANAMADI

---

## 6. Risk Degerlendirmesi

### Regulasyon Riski ⚐ (varsa)
*Bu bolum sadece regulasyon engeli olan pazarlar icin doldurulur.*

| Alan | Detay |
|------|-------|
| Gecerli yasalar | [FCRA, HIPAA, CCPA, vb.] |
| Ceza ornekleri | [varsa gercek ceza/dava ornekleri] |
| Indie etkisi | [indie developer icin ne anlama geliyor] |
| Uyum maliyeti | [tahmini maliyet] |

### Ana Riskler
| # | Risk | Olasilik | Etki | Onlem |
|---|------|----------|------|-------|
| 1 | [risk] | Dusuk/Orta/Yuksek | [etki] | [onlem] |
| 2 | ... | ... | ... | ... |

---

## 7. MVP Onerisi ⚐ STANDARD+

### Ekranlar (Max 4)
| # | Ekran | Ne Yapar |
|---|-------|----------|
| 1 | [ekran] | [aciklama] |

### 3 Ana Ozellik
1. **[ozellik]:** [aciklama]
2. **[ozellik]:** [aciklama]
3. **[ozellik]:** [aciklama]

### V1'de OLMAYACAKLAR
- [kapsam disi 1]
- [kapsam disi 2]

### Teknik Stack Onerisi
| Alan | Oneri |
|------|-------|
| Platform | [platform] |
| Framework | [framework] |
| DB | [db] |
| Odeme | [odeme] |

---

## 8. ASO Stratejisi ⚐ DEEP

| Alan | Oneri |
|------|-------|
| App Name (30 kar) | [oneri] |
| Subtitle (30 kar) | [oneri] |
| Keywords (100 kar) | [oneri] |
| Screenshot 1 | [mesaj] |
| Screenshot 2 | [mesaj] |
| Screenshot 3 | [mesaj] |

---

## 9. Sonraki Adimlar

1. [ ] [adim 1]
2. [ ] [adim 2]
3. [ ] [adim 3]

---

## 10. Cross-Report Karsilastirma ⚐ (onceki analizler varsa)

| Fikir | K2 | K3 | Final | Karar | Ana Avantaj | Ana Risk |
|-------|----|----|-------|-------|-------------|----------|
| [fikir 1] | XX | X.XX | XX.X | [karar] | [1 cumle] | [1 cumle] |
| [fikir 2] | XX | X.XX | XX.X | [karar] | [1 cumle] | [1 cumle] |

---

## Veri Kaynaklari

| # | Kaynak | Erisim Tarihi | Guvenilirlik |
|---|--------|---------------|-------------|
| 1 | [kaynak] | [tarih] | KESIN/TAHMINI/DUSUK |

---

*Bu rapor App Idea Research Agent v3.1 metodolojisi ile olusturulmustur.*

---

## Mod Bazli Bolum Haritasi

| Bolum | Quick Scan | Standard | Deep |
|-------|-----------|----------|------|
| Yonetici Ozeti | ✓ | ✓ | ✓ |
| 1. Pazar Analizi (+regulasyon K1) | ✓ | ✓ | ✓ |
| 2. Rakip Analizi | ✓ (top 5) | ✓ (top 10) | ✓ (top 10+) |
| 3. Firsat Puanlama (+regulasyon K3) | ✓ | ✓ | ✓ |
| 4. Gelir Potansiyeli | ✓ (basit) | ✓ (detayli) | ✓ (finansal model) |
| 5. Dogrulama | — | ✓ | ✓ |
| 6. Risk Degerlendirmesi (+regulasyon riski) | ✓ (top 3) | ✓ | ✓ |
| 7. MVP Onerisi | — | ✓ | ✓ |
| 8. ASO Stratejisi | — | — | ✓ |
| 9. Sonraki Adimlar | ✓ | ✓ | ✓ |
| 10. Cross-Report Karsilastirma | — | ✓ (varsa) | ✓ |
| Veri Kaynaklari | ✓ | ✓ | ✓ |
