# App Arastirma Metodolojisi v3.3

> 10 fazli, veri odakli, sistematik app fikri degerlendirme metodolojisi.
> Menopoz tracker hatasından (890 rating'li "milyar dolarlik pazar") ve 20+ uygulama
> arastirmasindan elde edilen derslerle gelistirildi.

## Surum Gecmisi

| Surum | Tarih | Degisiklik |
|-------|-------|------------|
| v1 | 2026-03-05 | Ilk versiyon: subjektif puanlama |
| v2 | 2026-03-11 | Objektif ankorlar + GATE sistemi + karar agaclari |
| v3 | 2026-03-11 | 3 katmanli puanlama + Moat analizi + basarisizlik agaclari |
| v3.1 | 2026-03-12 | Gercek veri dogrulamasi + Triangle Rule + veri kalite etiketleri |
| v3.1.1 | 2026-06-01 | Regulasyon faktoru phases.md + prompt-templates.md'ye senkronize edildi (K1'e 4. kriter, K3'e 4. faktor); Faz 5 override listesi tum dosyalarda esitlendi; scoring-model.md tek yetkili kaynak ilan edildi |
| v3.2 | 2026-06-01 | Differential dis-kaynak arastirmasindan 7 ekleme: Dagitim Fizibilitesi/keyword difficulty (#1), Faz 5.5 build-oncesi dogrulama [Walling 2/20/200 + Mom Test + fake-door] (#5), Mom Test kalite kurali/RF-16 (#2), adlandirilmis-icgoru + SISP/RF-17 (#3), Sales Safari watering-hole kesfi/Kural 7 (#4), Zamanlama yasam-dongusu etiketi (#6), Apple first-party talep sinyali (#7) |
| v3.2.1 | 2026-06-11 | Senkronizasyon + yapi: CLAUDE.md'ye Faz 5.5 pipeline adimi + 06-prebuild-plan.md cikti dosyasi eklendi; report-template v3.2'ye yukseltildi (Durum/Guven, 1.3 Dagitim Fizibilitesi, 5.2 Faz 5.5 plani, yasam-dongusu, adlandirilmis icgoru); Deep cikti dosyalari 07-11 olarak yeniden numaralandi; financial-model (Deep adim 9 sablonu) ve launch-playbook (GO sonrasi) pipeline'a baglandi; "15 tehlike isareti" → 17 duzeltildi; output/INDEX.md scoreboard + Durum takibi; .claude/commands/ kisayollari; git versiyon kontrolu baslatildi |
| v3.3 | 2026-06-26 | Akran-grubu karsilastirmasindan eklemeler. KAVRAMLAR: Lean Canvas + Quantified Value Prop (Faz 9), Riskiest Assumption Test/RAT (Faz 5.5 Adim 0), JTBD Forces of Progress (Faz 4/7 goc analizi), Sean Ellis %40 PMF testi (launch post), 2x2 stratejik konumlandirma (Faz 4 Adim 6.5). ARACLAR (referans + pipeline): Glimpse/Exploding Topics (Trends kor noktasi), SearchAds.com/AppTweak (keyword difficulty, Apple popularity - Eki 2025 bozulmasi gecerli), F5Bot/Syften (Reddit otomasyonu), Acquire.com/Flippa/Starter Story (gelir kaniti), AppFigures/AppMagic (indie app intel), IdeaBrowser/ValidatorAI (capraz-kontrol), AnswerThePublic, Meta audience size. DAVRANIS: B5 satin-alma komparasyonu ima edilen MRR'a cevrilince "Gelir MAX 2" override'ini kaldirabilir; A2 pre-build artik en riskli varsayimi once test eder. DUZELTME: data.ai 2024'te Sensor Tower'a katildi; GummySearch (Kas 2025 kapandi) kullanilmaz. Append-only: faz dosya adlari + kalite kurali numaralari degismedi |

## Temel Ilkeler

1. **Veri > Gorus**: Her karar somut veriye dayanir, "bence" yasak
2. **Gate Sistemi**: Fazlar arasi gecis kontrolleri, gecemeyen durur
3. **Ucgen Kurali**: Kritik iddia tek kaynaga dayanamaz (min 2 kaynak)
4. **Menopoz Testi**: Pazar raporu tahminleri vs gercek App Store verisi cross-check
5. **Override Kurallari**: Objektif esikler (lider <500 → elen, indie gelir yok → max 2)
6. **Bulunamadi da Veridir**: Aranan verinin bulunamamasi da puani sinirlar
7. **Mom Test (Davranis > Beyan)**: Beyan edilen niyet/iltifat veri degil; sadece gecmis davranis sayilir

## 10 Faz Ozeti

| Faz | Isim | Amac | Gate |
|-----|------|------|------|
| 1 | Problem Havuzu | 20-30 somut problem belirle | Min 15 problem, 3+ kategori |
| 2 | Keyword Cluster | Her problem icin 10+ keyword | Min 10 keyword/cluster |
| 3 | Hizli Pazar Tarama | Olu pazarlari erken ele | Min 8 cluster gecmeli |
| 4 | Rakip Analizi | Derin inceleme + sikayet analizi | Min 5 rakip/cluster |
| 5 | Firsat Puanlama | 3 katmanli: Pass/Fail → Skor → Carpan | Min 3 cluster 45+ |
| 5.5 | Build-Oncesi Dogrulama | Landing/fake-door + Mom-Test ile davranis testi | Guven >=%70 + 1 davranis sinyali |
| 6 | En Iyi 5 | 4 filtre (anlatim, MVP, fark, odeme) | Min 3 fikir gecmeli |
| 7 | Pazar Dogrulama | Gercek veriyle zorunlu dogrulama | Min 2/5 dogrulanmali |
| 8 | Capraz Karsilastirma | Kategoriler arasi kiyaslama | Net #1 veya max 2 finalist |
| 9 | Brief + MVP + Moat | Detayli plan + savunulabilirlik | Tum alanlar dolu |
| 10 | Seytanin Avukati | Varsayim kirma + Go/No-Go | Olumcul kusur yok |

## Dosya Haritasi

| Dosya | Icerik | Ne Zaman Kullanilir |
|-------|--------|---------------------|
| `phases.md` | 10 faz detaylari, gate'ler, cikti formatlari | Pipeline calistirirken |
| `scoring-model.md` | 3 katmanli puanlama: ankorlar, formuller, override | Faz 5 ve dogrulama |
| `data-collection-protocol.md` | Faz bazli sorgu sablonlari | Veri toplama sirasinda |
| `pre-build-validation.md` | Build-oncesi talep testi (2/20/200, Mom Test, fake-door) | Faz 5.5 (GO adayi cikinca) |
| `prompt-templates.md` | Her faz icin hazir prompt'lar | Faz calistirirken |
| `tools-and-data-sources.md` | Arac guvenilirlik matrisi | Kaynak secerken |
| `financial-model-template.md` | Bottom-up gelir modeli | Faz 9 (deep mode) |
| `launch-playbook.md` | Lansman stratejisi | Post-arastirma |
| `patterns/red-flags.md` | 17 tehlike isareti (RF-1 … RF-17) | Tum fazlarda kontrol |
| `patterns/green-flags.md` | 15 basari isareti | Tum fazlarda kontrol |

## Ogrenilen Dersler (Gercek Arastirmadan)

### Hatalar
- Menopoz tracker: $4.2B pazar raporu + 890 rating = hayali pazar
- OxbowSoft $30K/mo iddiasi: 6 sorgu sonrasi DOGRULANAMADI (Adapty "supposedly" dedi)
- Medisafe firsat penceresi: Acik ama MyTherapy/Pillo zaten dolduruyor

### Basarilar
- Debt Payoff: En dusuk risk, en kolay MVP, guclu topluluk kanallari
- Review mining: 8 sikayet temasi tespit edildi → somut farklilasmma firsatlari
- Google Trends: 3 finalist de UP trend — mevsimsellik kaliplari tespit edildi
