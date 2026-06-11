---
description: Quick Scan (~30 dk) — app fikri icin hizli fizibilite analizi
argument-hint: <app fikri/konu>
---

Konu: $ARGUMENTS

CLAUDE.md'deki **Quick Scan** modunu bu konu icin calistir:

1. Girdi analizi + disambiguation (konu belirsizse alt segmentleri sor)
2. Paralel: App Store lider + top 5 rakip | Google Trends (WebSearch dolayli) | Reddit hizli tarama
3. 3 katmanli puanlama — `methodology/scoring-model.md` yetkili kaynak; override kurallarini MUTLAKA uygula; early termination kurallarina dikkat (K1 fail, K3 < 0.5)
4. Rapor: `templates/report-template.md` formatinda `output/{bugun}-{konu}/REPORT.md` (Quick Scan'de atlanacak bolumler icin Mod Bazli Bolum Haritasi'na uy)
5. `output/INDEX.md`'ye satir ekle

Kalite kurallari (CLAUDE.md) zorunlu: veri etiketleri (KESIN/TAHMINI/DUSUK), ucgen kurali, menopoz testi, Mom Test. Karar GO/SARTLI GO ise Sonraki Adimlar'a Faz 5.5 onerisi ekle.
