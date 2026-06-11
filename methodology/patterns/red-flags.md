# Tehlike Isaretleri (Red Flags)

Uygulama pazar arastirmasinda basarisizligi ongoren tehlike isaretleri.
Penlo arastirma surecinden (menopoz pivotu) alinan derslerle zenginlestirilmistir.

---

## PAZAR RED FLAG'LERI

### RF-1: "Milyar Dolarlik Pazar" Yanilgisi

- **Isaretler:** Pazar raporu buyuk rakamlar soyluyor ama lider uygulamanin rating'i < 5K
- **Gercek ornek:** Menopoz pazari $4.2B tahmin ediliyordu, ama lider uygulama (Balance) sadece 890 iOS rating
- **Ders:** Pazar raporlari toplam SEKTORU olcer, mobil APP pazarini degil. $4.2B'lik pazar ilac, klinik, cihaz ve uygulamalari icerir. Mobil uygulamanin payi %0.1 bile olmayabilir.
- **Aksiyon:** Her zaman App Store rating sayisini pazar raporuyla capraz kontrol et. Lider uygulama 10K+ rating degilse, "milyar dolarlik pazar" iddiasina supheyle yaklas.
- **Formul:** Gercek pazar buyuklugu = Lider uygulamanin tahmini geliri x 5-10 (kategori carpani)

### RF-2: "Dusuk Rekabet" Tuzagi

- **Isaretler:** Kategoride az rakip var, puanlamada Competition = 1-2
- **Gercek ornek:** Menopoz kategorisinde rekabet dusuktu cunku KIMSE O UYGULAMAYI ISTEMIYORDU
- **Ders:** Dusuk rekabet iki anlama gelir: (a) Herkes kacirmis, firsat var VEYA (b) Kimse bu isi yapmak istemiyor cunku pazar yok
- **Aksiyon:** Dusuk rekabet + dusuk lider rating = pazar yok. Dusuk rekabet + yuksek lider rating = firsat. Ikisini BIRLIKTE degerlendir.
- **Kontrol sorusu:** Bu alanda neden kimse uygulama yapmamis? Cevap "firsat" mi yoksa "talep yok" mu?

### RF-3: VC/Enterprise Oyuncularin Baskisi

- **Isaretler:** Basit gorunuslu uygulama ama arkasinda buyuk fon/sirket var
- **Gercek ornek:** Stoic (YCombinator destekli) siradan bir indie rakip gibi gorunuyor ama $1M+ yatirim almis. Notion basit bir not uygulamasi gibi gorunuyordu, $10B valuasyon ile rekabet etmek imkansiz.
- **Ders:** VC destekli rakipler fiyat kirilarak, ucretsiz tier genisleterek veya agresif pazarlamayla indie dev'leri ezebilir
- **Aksiyon:** Her rakibin arkasindaki sirket/fon yapisini kontrol et. Crunchbase, LinkedIn, PitchBook kullan. 2+ VC destekli rakip varsa, cok niche'e git.

### RF-4: Apple/Google Yerlesik Cozumu

- **Isaretler:** Apple Journal, Apple Health, Google Keep, Samsung Notes gibi ucretsiz yerlesik uygulamalar var
- **Gercek ornek:** Apple Journal 244K rating aldi cunku ON-YUKLU geliyor. Google Keep gunluk 1M+ aktif kullanici. Bu uygulamalarla "temel ozellik" bazinda rekabet etmek imkansiz.
- **Ders:** Yerlesik cozumler "good enough" oldugunda, kullanicilarin %80'i baska bir sey aramaz
- **Aksiyon:** Yerlesik cozumun YAPMADIGI spesifik sey ne? O sey senin nisin. Ornek: Apple Journal analiz/istatistik vermiyor — bu bir firsat olabilir.
- **Kontrol listesi:**
  - Apple bu kategoride uygulama cikartti mi veya cikarmaya hazirlaniyormu? (WWDC duyurularini takip et)
  - Google bu alana girdi mi?
  - Samsung/Xiaomi kendi cozumunu sunuyor mu?

### RF-5: "Fiyat Zammi" Anlatisi

- **Isaretler:** "Rakip zam yapti, kullanicilar kizgin" anlatisi Reddit/Twitter'da donuyor
- **Gercek ornek:** Day One "zam" iddiasi aslinda tanitim indiriminin sona ermesiydi. Tanitim fiyati $2.92/ay'dan normal fiyat $4.17/ay'a dondugunde, Reddit'te "fiyat iki katina cikti" diye thread'ler acildi. Gercekte standart fiyat hic degismemisti.
- **Ders:** Reddit'te 2-3 sikayet = "buyuk isyan" degil. 50 upvote alan bir sikayet bile uygulamanin 100K+ kullanicisi icinde %0.05'tir.
- **Aksiyon:** Fiyat gecmisini resmi kaynaklardan kontrol et (Wayback Machine, App Store fiyat gecmisi araclari). Reddit anlatisina korkorune guvenme. Fiyat artisi GERCEK mi yoksa algi mi?

### RF-6: Android Basarisi = iOS Basarisi Degil

- **Isaretler:** Rakip Android'de cok basarili, "iOS'ta da yaparim" dusuncesi
- **Gercek ornek:** Diarium Android'de 660K+ indirme ve 4.5 yildiz, iOS'ta 0 rating (neredeyse hic kullanilmiyor). Journey Android'de guclu, iOS'ta zayif.
- **Ders:** Android ve iOS kullanici davranislari, odeme aliskanliklari ve uygulama beklentileri TAMAMEN farkli. Android'de basarili olan uygulama iOS'ta basarisiz olabilir ve tersi.
- **Aksiyon:** iOS ve Android verilerini AYRI degerlendir. Hedef platformun hangisiyse o platformun verisine bak. Cross-platform basariyi VARSAYMA.
- **Ek not:** iOS kullanicilari ortalama 2.5x daha fazla harcama yapiyor, ama beklentileri de o kadar yuksek.

### RF-7: "Aktif Goc" Hayali

- **Isaretler:** "Kullanicilar [rakip]'den goce hazir" iddialari
- **Gercek ornek:** Day One goc iddiasi dogrulanamadi — hala 4.8 yildiz, 115K rating ve buyumeye devam ediyor. "Day One'dan kaciyorum" diyen 20 kisi varken, gunluk 500+ yeni kullanici kazaniyorlar.
- **Ders:** Insanlar sikayet eder ama goc etmez. Switching cost (veri tasima, aliskanlik degisimi) cok yuksek. Ozellikle gunluk yazanlar icin 3+ yillik veri tasinmasi buyuk bariyer.
- **Aksiyon:** Reddit'te son 6 ayda "leaving [app]", "switched from [app]", "[app] alternative" aramalari yap. Gercekten goc edenler mi var, yoksa sadece sikayet edenler mi? Sikayet/goc orani genellikle 50:1'dir.

### RF-8: "Free Tier Zayif" Abartisi

- **Isaretler:** "Rakibin ucretsiz versiyonu cok kisitli, kullanicilar mutsuz" anlatisi
- **Gercek ornek:** Day One free tier "sadece 1 gunluk" iddia edildi, ama gercekte ucretsiz tier: sinirsiz yazi, 1 gunluk, temel sablonlar, cihaz basina yerel depolama iceriyordu. Cogu casual kullanici icin yeterli.
- **Ders:** Ucretsiz tier'in "zayif" olmasi subjektif. Power user icin zayif olan sey, casual kullanici icin yeterli olabilir. Casual kullanicilar pazarin %80'ini olusturur.
- **Aksiyon:** Rakibin ucretsiz versiyonunu KENDIN indir ve kullan. 1 hafta boyunca ucretsiz tier ile yas. "Zayif" iddiasi dogru mu? Hangi ozellik GERCEKTEN eksik ve bu ozellik kac kisiyi etkiliyor?
- **Kontrol:** Ucretsiz tier ile 1 hafta yasayabildiysen, cogu kullanici da yasayabilir.

### RF-9: Tek Kaynak Yanilgisi

- **Isaretler:** Tek bir forum thread'i, tek bir blog yazisi veya tek bir influencer'in gorusune dayanarak pazar karari verme
- **Gercek ornek:** Bir Reddit thread'inde "Day One'dan kaciyorum" diyen 15 kisiye bakarak 150K+ kullanici kitlesinin mutsuz oldugu sonucuna varmak. Tek bir "menopoz uygulamasi lazim" yorumunu pazar dogrulamasi olarak kullanmak.
- **Ders:** Tek kaynak = anekdot, veri degil. En az 3 BAGIMSIZ kaynak ayni seyi soyluyorsa trend olabilir.
- **Aksiyon:**
  - En az 3 farkli platform kontrol et (Reddit, Twitter/X, App Store yorumlari, forum'lar)
  - Her kaynaktaki tarih ve baglamina bak (2 yil onceki sikayet hala gecerli mi?)
  - Nicel veri ile dogrula (indirme sayilari, rating trendi, revenue tahmini)
  - "N=1" kararlarindan kacin

### RF-10: Survivorship Bias (Hayatta Kalma Yanilgisi)

- **Isaretler:** Basarili uygulamalara bakarak "bu kategoride basarili olunur" sonucuna varmak
- **Gercek ornek:** "Bear uygulama $1M+ kazaniyor, ben de not uygulamasi yapayim" dusuncesi. Bear'i goruyorsun ama ayni kategoride kapanan/basarisiz olan 500+ uygulamayi gormuyorsun.
- **Ders:** App Store'da her basarili uygulamanin arkasinda 100-500 basarisiz uygulama var. Basari orani: uygulama gelistiricilerin sadece %0.5'i $1M+ yillik gelire ulasir.
- **Aksiyon:**
  - Sadece basarililara degil, kapananlara da bak (Product Graveyard, Killed by Google)
  - "Neden basarisiz oldu?" sorusunu sor
  - Kategorideki toplam uygulama sayisina bak, sadece top 5'e degil
  - Indie dev basari hikayelerinde "sansli oldum" faktorunu hesaba kat

### RF-11: "Bana Ozel" Problemi (Kendi Kasintiyi Kasima Tuzagi)

- **Isaretler:** "Ben bu problemi yasiyorum, demek ki herkes yasiyor" dusuncesi
- **Gercek ornek:** "Ben menopoz doneminde uyku takibi istiyorum" → arastirma yapinca 50 yasin ustundeki kadinlarin sadece %3'u saglik uygulamasi kullaniyor. "Ben gunluk yaziyorum, herkes yaziyor" → arastirma yapinca yetiskinlerin sadece %8'i duzenli gunluk tutuyor.
- **Ders:** Senin yasadigin problem herkesin problemi degildir. "Scratching your own itch" guzel bir baslangic noktasi ama PAZAR DOGRULAMASI yerine gecmez.
- **Aksiyon:**
  - Google Trends'te problem aramasinin hacmini kontrol et
  - Reddit'te kac kisi bu problemden bahsediyor?
  - App Store'da bu problemi cozen uygulamalarin rating sayilarina bak
  - Potansiyel kullanicilarin %1'ine ulasmak icin ne kadar harcaman gerekir?
  - 10 potansiyel kullaiciyla konusmadan urun YAPMA

### RF-12: Saglik Uygulamasi Churn Krizi

- **Isaretler:** Saglik/wellness kategorisinde uygulama gelistirme plani
- **Gercek ornek:** Saglik uygulamalarinda %94 churn orani (kullanicilarin %94'u 90 gun icinde uygulamayi birakiyor). Menopoz, meditasyon, fitness takibi — hepsinde ayni sorun. Calm ve Headspace bile %70+ yillik churn yasiyor.
- **Ders:** Saglik uygulamalarinda kullanici kazanmak zor, tutmak DAHA ZOR. Motivasyon donemseldir: Ocak'ta "yeni yil karari" ile baslayan kullanicilar Subat'ta gider.
- **Aksiyon:**
  - Day 7 retention hedefini %15'in altinda tutarsan basarisiz olursun
  - Retention icin notification stratejisi SART (ama spam olursa uninstall)
  - Streak/gamification mekanikleri planla
  - Saglik verisini Apple Health/Google Fit ile entegre et (lock-in etkisi)
  - Churn'u azaltacak "veri biriktirme" stratejisi kur (ne kadar cok veri olursa, gitmek o kadar zor)
- **Kategori bazli churn oranlari:**
  - Fitness: %90 (90 gun)
  - Meditasyon: %85 (90 gun)
  - Beslenme: %92 (90 gun)
  - Menopoz/saglik: %94 (90 gun)
  - Karsilastirma — Finans: %65 (90 gun), Productivity: %70 (90 gun)

### RF-13: "Feature Parity" Tuzagi

- **Isaretler:** "Rakibin tum ozelliklerini yapacagim + 1 ekstra" plani
- **Gercek ornek:** Day One'in 10+ yillik ozellik birikimine yetismek icin solo dev olarak en az 2 yil gerekir. Bu surede Day One 50 yeni ozellik daha ekler.
- **Ders:** Lider uygulamanin ozellik listesini kopyalamak kaybedecegin bir yaris. Lider her zaman onde olacak cunku daha fazla kaynagi, kullanicisi ve verisi var.
- **Aksiyon:**
  - Rakibin 10 ozelligini degil, yapMADIGI 1 seyi yap
  - MVP'de MAKSIMUM 3 core ozellik
  - "Less but better" prensibi
  - Rakibin weakspot'una odaklan, strong point'ine degil

### RF-14: Pazar Zamanlama Hatasi

- **Isaretler:** Trend coktan peak yapmis veya henuz cok erken
- **Gercek ornek:** 2023'te "AI journal" uygulamasi yapmak — trend henuz basliyordu, iyi zamanlama. 2026'da yapmak — pazar doymus olabilir. 2019'da "menopoz uygulamasi" — pazar henuz hazir degil, cok erken.
- **Ders:** "Right idea, wrong time" en yaygin basarisizlik nedeni. Cok erken girersen pazar egitimi senin sirtinda. Cok gec girersen rekabet ezici.
- **Aksiyon:**
  - Google Trends ile trendin yukselis mi dusus mu oldugunu kontrol et
  - Lider uygulamanin kac yildir var olduguna bak
  - Son 12 ayda kategoriye yeni giris var mi?
  - Trend "early majority" asamasinda mi? (En iyi giris noktasi)

### RF-15: Regulasyon/Uyumluluk Mayini

- **Isaretler:** Saglik verisi, finansal veri, cocuk verisi isleme plani
- **Gercek ornek:** Saglik uygulamalarinda HIPAA (ABD), GDPR (AB), KVKK (TR) uyumlulugu gerekir. Cocuk uygulamalarinda COPPA. Finans uygulamalarinda PCI-DSS. Uyumsuzluk = App Store'dan kaldirilma + yasal sorun.
- **Ders:** Regulasyon maliyeti kucuk bir indie dev icin %30-50 ekstra maliyet demek. Hukuk danismanligi, veri guvenligi altyapisi, uyumluluk dokumantasyonu.
- **Aksiyon:**
  - Hedef pazarin regulasyon gereksinimlerini lansmandan ONCE arastir
  - GDPR/KVKK icin privacy policy ve veri isleme surecleri planla
  - Saglik verisi isliyorsan Apple HealthKit kurallarini oku
  - Gerekiyorsa hukuk danismanligi butcesi ayir ($500-2000)

### RF-16: Beyan Edilen Niyet / Iltifat Tuzagi (Mom Test)

- **Isaretler:** Talep veya gelir delili "bunu kullanirim", "harika fikir", "kesinlikle oderim" gibi beyan edilen niyete veya iltifata dayaniyor.
- **Gercek ornek:** Hipotetik satin-alma niyeti gercek davranisi sistematik olarak abartir (Chandon/Morwitz/Reinartz 2005). Insanlar nazik olmak icin yalan soyler; bir sey soylemek bedava, yapmak degil.
- **Ders (The Mom Test):** Iyi veri = spesifik GECMIS davranis ("son ay bu problem icin ne yaptin, ne odedin, hangi araci denedin"). Kotu veri = gelecek hakkinda hipotez + iltifat.
- **Aksiyon:** Beyan edilen niyet/iltifat TEK BASINA Talep veya Gelir puanini yukseltemez (override: o kriter MAX 3). Reddit/review okurken "gercekten yapmis/odemis" sinyalini "isterdim/keske" sinyalinden ayir. Gorusmede fikrini sunma, gecmis davranistan sor.

### RF-17: SISP -- Solution In Search of a Problem

- **Isaretler:** Once cozum/teknoloji secilmis, problem sonradan araniyor ("AI ile X yapalim, kime lazim acaba"). Rekabet puani "rakip yok" diye yuksek veriliyor ama rakiplerin kacirdigi spesifik icgoru adlandirilamiyor.
- **Gercek ornek:** YC (Jared Friedman): SISP cok anilan bir hata ama en yaygini DEGIL -- yani otomatik ELEN degil, UYARI. "Rakip yok = pazar yok"un keskin hali: Dropbox gibi kazananlarda rakipler VARDI + spesifik kacirilmis bir icgoru vardi; ciplak bosluk degil.
- **Ders:** Cozumden degil problemden basla. Yuksek Rekabet puani ancak ADLANDIRILMIS bir kacirilmis icgoru ile gecerli.
- **Aksiyon:** Rekabet 4-5 icin kacirilmis icgoruyu tek cumleyle adlandir (yoksa MAX 3, bkz. scoring-model.md). Seytan'in avukatinda "bu bir SISP mi?" sorusunu sor. Cozum-once geldiyse, gercek bir watering-hole'da (Sales Safari) problemi once dogrula.

---

## RED FLAG KONTROL MATRISI

Hizli degerlendirme icin bu matrisi kullan:

| Red Flag | Agirlik | Kontrol Yontemi | Karar Esigi |
|---|---|---|---|
| RF-1: Milyar $ yanilgisi | Kritik | App Store rating vs pazar raporu | Lider < 5K rating = DURMA |
| RF-2: Dusuk rekabet | Yuksek | Lider rating + kategori buyuklugu | Dusuk rekabet + dusuk lider = DURMA |
| RF-3: VC baskisi | Orta | Crunchbase arastirmasi | 2+ VC rakip = Niche'e git |
| RF-4: Yerlesik cozum | Kritik | Apple/Google uygulama kontrolu | Yerlesik var + fark yok = DURMA |
| RF-5: Fiyat zammi anlatisi | Orta | Wayback Machine kontrolu | Dogrulanmadi = Goz ardi et |
| RF-6: Platform farki | Orta | Her platformu ayri kontrol | Hedef platform verisi zayif = DURMA |
| RF-7: Goc hayali | Yuksek | Reddit/forum analizi | Goc < 100 kisi = Goz ardi et |
| RF-8: Free tier abartisi | Orta | Rakibi kendin kullan | Free tier yeterli = DURMA |
| RF-9: Tek kaynak | Yuksek | 3+ kaynak kontrolu | Tek kaynak = Karar VERME |
| RF-10: Survivorship bias | Orta | Basarisiz uygulamalari ara | Kategori olum orani > %90 = Dikkat |
| RF-11: Bana ozel problem | Yuksek | 10 potansiyel kullanici gorusmesi | < 3/10 "bunu isterim" = DURMA |
| RF-12: Saglik churn | Kritik | Kategori churn verisi | %90+ churn = Retention plani SART |
| RF-13: Feature parity | Orta | MVP scope kontrolu | > 5 core ozellik = Scope kucult |
| RF-14: Zamanlama | Yuksek | Google Trends analizi | Dusus trendinde = DURMA |
| RF-15: Regulasyon | Duruma bagli | Hukuk arastirmasi | Bilinmiyor = Arastirmadan BASLA |
| RF-16: Niyet/iltifat tuzagi | Yuksek | Gecmis davranis vs beyan ayrimi | Sadece beyan = o kriter MAX 3 |
| RF-17: SISP | Orta | Kacirilmis icgoru adlandirma | Adlandirilamiyor = Rekabet MAX 3 |

## KARAR KURALI

- **3+ Kritik red flag** = Bu fikri birak, yenisine gec
- **2 Kritik red flag** = Cok dikkatli ol, ek arastirma yap
- **1 Kritik red flag** = Risk yonetilebilir, ama plani adapte et
- **Sadece Orta/Dusuk red flag'ler** = Devam et, ama izle

## PENLO SURECINDEN ALINAN OZEL DERSLER

1. **"Pazar buyuk" demek "app pazari buyuk" demek degil.** Menopoz pazari buyuktu, ama mobil uygulama pazari kucuktu.
2. **Reddit anlatilari gercegi carpitir.** "Herkes sikayet ediyor" = 15 kisi sikayet ediyor, 100K kisi mutlu.
3. **Dusuk rekabet her zaman iyi degildir.** Bazen "dusuk rekabet" = "olmus pazar."
4. **Demografik uyumsuzluk gizli katil.** Hedef kitlen uygulama kullanan bir kitle mi? 50+ yas grubu smartphone kullaniyor ama app indirme orani dusuk.
5. **"Pivot" kelimesi kolayca soylenir, zor yapilir.** Menopozdan journaling'e pivot yapmak = tamamen yeni arastirma, tamamen yeni rakip analizi.
6. **Capraz dogrulama SART.** Pazar raporu + App Store verisi + Reddit sentimenti + Google Trends = Gercek resim. Tek kaynak = Yanlis resim.
