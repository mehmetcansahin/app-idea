---
description: v4.0 arastirma ciktisini render ve validate et, portfoy INDEX'ini uret
argument-hint: <output klasoru>
---

Cikti klasoru: $ARGUMENTS

1. `python3 scripts/evidence_tool.py render "$ARGUMENTS"` (ledger ve raporun
   `## Özet` bolumu; ozet elle duzenlenmez)
2. `python3 scripts/evidence_tool.py validate "$ARGUMENTS"`
3. Hatalari evidence/assessment/report kaynaginda duzelt; validator gecmeden
   tamamlanmis rapor olarak sunma. Rapor kontrolleri `methodology/report-writing.md`
   §11'dedir.
4. Standard/Deep'te mevcut bir `data/reader-review.md` `analysis_date`'ten bagimsiz
   denetlenir (revizyon, benzersiz iddialar, evidence ID'leri, sorunlar, olcutler);
   incelemenin hic olmamasi yalniz 2026-10-20 ve sonrasi raporlarda hatadir. Quick
   incelemesi istege baglidir ve denetlenmez. Inceleme bayat veya revizyon eksikse
   bu komut onu onaylamaz ve revizyon satirini yazmaz: bagimsiz okur guncel raporu
   okuyup kontrol ettikten sonra
   `python3 scripts/evidence_tool.py revision "$ARGUMENTS"` ciktisini kendisi yazar
   (`prompt-templates.md` "Okur Dogrulama Turu").
5. `data/portfolio.json` eksikse once yaz (`prompt-templates.md` "Portfoy Kaydi");
   sonra `python3 scripts/portfolio_tool.py render` ve
   `python3 scripts/portfolio_tool.py validate` (varsayilan `output`). Hatalari
   portfolio.json'da duzelt; INDEX'in uretilen bolgelerini elle duzenleme.
6. Paylasim kopyasi gerekiyorsa `python3 scripts/evidence_tool.py pdf "$ARGUMENTS"`.
