---
description: Compare v4.0 — fikirleri ayni Quick kapsamiyla, iki eksenli ve arketip-baglamli karsilastir
argument-hint: <fikir 1>, <fikir 2>, ...
---

Fikirler: $ARGUMENTS

1. Her fikir icin ayni v4.0 metodolojisiyle `/quick-scan` adimlarini calistir. Her
   adayda kapsam aynidir: `product_type` secimi, top 5 rakip/ikame profili, top 3
   rakip icin Meta + Google ATC var/yok, stratified review yok; non-app adayda
   store/ASO gorevleri `not_applicable` kaydiyla atlanir. Bir adaya fazladan
   toplama eklenirse o aday ayri Standard analizidir, Compare satiri degildir.
2. Siralama: fatal gate -> Kanit Gucu -> firsat skor araligi -> top risk/test
   maliyeti -> operasyon kisitlari.
3. Farkli arketipleri ciplak skorla siralama; agirlik farkini tabloda goster. Urun
   turu farki agirlik farki degildir; tabloda ayri sutun olarak goster.
4. Top adaylar icin Standard test yatirimi oner.
5. Her analiz icin ayri evidence/assessment/portfolio.json uret;
   `python3 scripts/evidence_tool.py render` ve `validate` her aday klasorunde
   calissin.
6. `python3 scripts/portfolio_tool.py render` ve `validate` ile INDEX'in uretilen
   scoreboard bolgesini guncelle. Compare turu satirini `output/INDEX.md`
   "Compare Turlari" bolumune, uretilen bolgelerin disinda elle ekle; yalniz ayni
   metodoloji surumundeki yeni satirlari karsilastir.

Fikir listesi yoksa Faz 1-2 ile aday uret; problem, segment ve urun turunu
kullaniciya onaylatmadan arketip puanlama yapma.
