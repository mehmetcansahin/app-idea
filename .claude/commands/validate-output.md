---
description: v4.0 arastirma ciktisini render ve validate et
argument-hint: <output klasoru>
---

Cikti klasoru: $ARGUMENTS

1. `python3 scripts/evidence_tool.py render "$ARGUMENTS"`
2. `python3 scripts/evidence_tool.py validate "$ARGUMENTS"`
3. Hatalari evidence/assessment/report kaynaginda duzelt; validator gecmeden
   tamamlanmis rapor olarak sunma. Rapor kontrolleri `methodology/report-writing.md`
   §11'dedir.
4. Paylasim kopyasi gerekiyorsa `python3 scripts/evidence_tool.py pdf "$ARGUMENTS"`.
