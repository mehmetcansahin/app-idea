# Tehlike Isaretleri — v4.0

Bu liste skor formulu degil, claim/risk audit yardimcisidir.

## Evidence ve Cikarim

- **RF-1 Construct validity:** Dogru rating gozleminden dogrudan pazar sonucu cikarmak.
- **RF-2 Source echo:** Ayni primary raporu aktaran URL'leri bagimsiz saymak.
- **RF-3 Missingness:** Public kanit bulunmamasini yokluk kabul etmek.
- **RF-4 Synthetic replacement:** AI persona'yi gercek kullanici kaniti saymak.
- **RF-5 False precision:** Kalibrasyonsuz yuzde veya tek nokta tahmini kullanmak.
- **RF-6 Stale context:** Geo, storefront, version veya veri donemini kaybetmek.
- **RF-7 Sample generalization:** Review/Reddit orneklemini pazar prevalansi yapmak.

## Pazar ve Urun

- **RF-8 Solution-first:** Problem davranisi yerine ozellik listesiyle baslamak.
- **RF-9 App-only competition:** Spreadsheet, manual workflow, service ve web ikamesini atlamak.
- **RF-10 Implementation-only promise:** UX/hiz iddiasini kullaniciya deneyimletmeden landing ile test etmek.
- **RF-11 Built-in dominance:** Platform cozumu varken switch nedeni/kanal olmamasi.
- **RF-12 Moat mismatch:** Boslugun veri, network, lisans veya partnership gerektirmesi.
- **RF-13 Fantasy migration:** Push+Pull, Anxiety+Habit'i asmiyor.
- **RF-14 Peaked timing:** Yuksek hacmi buyume sanmak.

## Ekonomi ve Dagitim

- **RF-15 Waitlist theater:** Email'i odeme/retention kaniti gibi sunmak.
- **RF-16 Average economics:** Geo/kanal/power-user farklarini ortalamayla gizlemek.
- **RF-17 Projected LTV certainty:** Pre-launch LTV:CAC'i gerceklesen ekonomi sanmak.
- **RF-18 Single-channel dependency:** Tek paid/organic kanal olmadan dagitim plani olmamasi.
- **RF-19 Variable-cost blindness:** AI/API/support maliyetinin kullanimla buyumesini atlamak.
- **RF-20 Retention proxy:** Gunluk problem sikligini urun retention'i sanmak.

## Fatal Risk

- **RF-21 Legal block:** Lisans/hak/mevzuat indie olcekte asilamiyor.
- **RF-22 Core dependency block:** Cekirdek API/veri/teknoloji erisilemiyor.
- **RF-23 Platform block:** Store policy yayinlamaya izin vermiyor.
- **RF-24 Safety/ethics block:** Kabul edilemez zarar, privacy veya guvenlik riski.

Fatal risk `scoring-model.md` gate'ine gider. Diger red flag'ler ilgili boyutun
low/base/high araligini genisletir, evidence grade'i dusurur veya Faz 5.5 testini
belirler; otomatik fatal eleme yapmaz.
