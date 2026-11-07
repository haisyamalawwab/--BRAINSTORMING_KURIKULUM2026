# RUBRIK PENILAIAN — STI-727 SMART CITY & PEMERINTAHAN DIGITAL

**Kode:** STI-727 | **2 SKS Teori** — 100T+120M | **Semester:** 7 | **Prasyarat:** STI-521
**CPL:** P3, KK3 | **CPMK:** 1 C4 SPBE, 2 C6 Web GIS, 3 C4 Satu Data, 4 C6 Masterplan
**Bobot:** Tugas1 20% + UTS 30% + Tugas2 20% + UAS 30% =100% | **Revisi:** 07112026

---

## A. RUBRIK TUGAS1 — Peta Dasar GIS (20% — Mg4)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **GeoJSON Valid & Struktur (30%)** | FeatureCollection valid (geojsonlint pass), 10+ features, properties lengkap (nama, kategori), koordinat WGS84 dalam rentang, file well-formed | Valid tetapi 7-9 features, properties kurang 1 field | Valid tetapi 4-6 features, koordinat swap (lat/lon tertukar) | Tidak valid (lint fail) atau 0-3 features |
| **Markers & Polygon Leaflet (30%)** | 10 markers custom icons (sekolah/hospital) dengan popup (nama+alamat), 1 polygon zonasi RT/RW dengan style fill, layer control, zoom fitBounds, responsive | 10 markers tetapi icon default, polygon ada tanpa style, layer control ada | 5-9 markers, polygon tidak ada atau error | <5 markers atau peta tidak load |
| **QGIS Layer (20%)** | Screenshot QGIS 2 layers (batas admin + fasum) dengan symbology & label jelas, legend, scale bar, attribution | Screenshot 2 layers tetapi tanpa legend/scale | Hanya 1 layer, tanpa label | Tidak ada screenshot atau layer salah |
| **Penjelasan Vektor vs Raster (20%)** | 300 kata jelas: definisi, contoh (Shapefile vs GeoTIFF), kegunaan Smart City, kapan pakai vektor/raster, WGS84 dijelaskan benar | 200 kata benar tetapi tanpa contoh Smart City | 100 kata singkat, ada kesalahan konsep | <100 kata atau konsep salah |

---

## B. RUBRIK UTS — Tertulis SPBE & GIS (30% — Mg8)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **PG 20 Soal (40%)** | 17-20 benar | 13-16 benar | 9-12 benar | 0-8 benar |
| **Esai Analisis SPBE (20%)** | Matriks 6 domain lengkap (layanan, proses bisnis, data, aplikasi, infra, keamanan) + gap + rekomendasi konkret 3 poin, sitasi Perpres pasal benar | Matriks 6 domain tetapi 1-2 domain kosong, rekomendasi 1-2 poin | Matriks 3-4 domain, tanpa rekomendasi | Matriks <3 domain atau konsep salah |
| **Esai Arsitektur Layanan Aduan Banjir (20%)** | Alur lengkap: sensor water_level → MQTT → API SPBE → GIS → notifikasi OPD → dashboard, sebut teknologi (MQTT, REST, Leaflet), SOP singkat | Alur ada tetapi missing 1 komponen (mis. notifikasi), teknologi tidak spesifik | Alur parsial (hanya sensor→GIS), tanpa SOP | Alur tidak koheren |
| **Esai Choropleth vs Heatmap (20%)** | Jelaskan perbedaan (choropleth aggregate per area vs heatmap density titik), kapan pakai (kepadatan per kecamatan vs titik sampah), kelebihan/kekurangan, contoh warna scale | Jelaskan perbedaan benar tetapi tanpa kapan pakai | Jelaskan 1 konsep benar, 1 salah | Tidak mampu jelaskan |

---

## C. RUBRIK TUGAS2 — Command Center (20% — Mg12)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **Diagram Arsitektur (40%)** | Diagram lengkap: sensor (IoT) → MQTT → Kafka → Big Data → Dashboard+GIS+Video AI → SOP → OPD, komponen (Broker, API Gateway, DB), data flow panah jelas, teknologi label (MQTT, Kafka, Grafana), estetika rapi | Diagram lengkap tetapi tanpa Kafka atau Big Data, teknologi generik | Diagram missing 2 komponen (Video AI, SOP) | Diagram tidak koheren atau tidak ada |
| **Peta GIS Live (30%)** | 3 sensor live (pm2.5, water_level, traffic) warna dinamis + update 5s, 1 video AI mock (people count dummy), popup detail, legend, auto-refresh | 2 sensor live + 1 video mock tetapi update manual (refresh) | 1 sensor live saja, tanpa video | Peta tidak live (static) |
| **KPI & SOP (15%)** | 2 KPI SMART (mis. response time <30m, resolution 80%) + SOP 1 hal (P1 emergency, P2 normal) jelas peran OPD | 2 KPI tetapi tidak SMART, SOP singkat <0.5 hal | 1 KPI saja, SOP tidak jelas | Tidak ada KPI/SOP |
| **Docs (15%)** | Laporan 2-3 hal: penjelasan arsitektur, teknologi pilihan alasan, instruksi run peta, sitasi Command Center ref | Laporan 1-2 hal tanpa alasan teknologi | Laporan <1 hal, tanpa sitasi | Tidak ada laporan |

---

## D. RUBRIK UAS — Masterplan & Demo (30% — Mg16)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **Masterplan Kedalaman (35%)** | 20 hal lengkap: visi/misi, 1-2 pilar prioritas (alasan), 3 layanan unggulan (deskripsi+manfaat+target user), roadmap 5 th (short/mid/long milestones), anggaran indikatif (CAPEX/OPEX), stakeholder (Diskominfo, OPD, vendor), KPI 4-5, risiko+mitigasi, sitasi SPBE/Satu Data | 15-19 hal, 3 layanan tetapi 1 tanpa manfaat jelas, roadmap tanpa anggaran, KPI 2-3 | 10-14 hal, 2 layanan saja, roadmap tanpa milestones, tanpa anggaran | <10 hal atau tidak ada roadmap/anggaran |
| **Purwarupa Fungsional (30%)** | HTML/JS Leaflet berfungsi: peta + form aduan (kategori+foto+latlon auto) → submit → daftar aduan (table) + detail, validasi (required), persist localStorage, responsive, no console error | Fungsional tetapi tanpa persist (reload hilang), validasi kurang | Hanya form tanpa daftar, atau daftar tanpa peta | Tidak fungsional (form tidak submit) |
| **Demo & Q&A (20%)** | Presentasi 10m jelas (visi→layanan→roadmap), demo 10m live lancar (peta+aduan E2E), Q&A jawab trade-off (kenapa pilih Mobility vs Environment, biaya Command Center) dengan angka | Presentasi jelas tetapi demo delay 1-2m (loading), Q&A ragu | Presentasi melebihi 12m, demo gagal 1 fitur tetapi workaround video | Demo gagal total (video saja) |
| **Docs & Video (15%)** | Masterplan PDF rapi (TOC, page number) + repo + video demo 3m (narasi, HD, unlisted) + Turnitin ≤20% | Masterplan PDF tetapi tanpa TOC, video 2m kualitas sedang | Masterplan PDF tanpa format, video <2m | Tidak ada video atau Turnitin >20% tanpa revisi |

**Peer eval:** Kontribusi 20-25% per org (tim 5) ideal, jika <10% → nilai individu -30%.

---

## E. Formatif & Kehadiran

| Kriteria | Lulus | Tidak Lulus |
|---|---|---|
| Kehadiran | ≥80% (13/16) | <80% → tugas pengganti atau tidak boleh UAS |
| Formatif | ≥6/10 pass | <6 → remedial 7 hari |

---

## F. Konversi NA

```
NA = 0.20×Tugas1 + 0.30×UTS + 0.20×Tugas2 + 0.30×UAS + bonus (max +3)
Bonus: aktif >80% sesi +2, video berkualitas +1
```

| NA | Huruf | Keterangan |
|---|---|---|
|85-100|A|Sangat memuaskan|
|70-84|B|Memuaskan|
|60-69|C|Cukup|
|55-59|D|Tidak lulus remedial|
|<55|E|Gagal|

Aturan: NA ≥55 (C) dengan UAS ≥50 & hadir ≥80%. NA ≥60 tetapi UAS <50 → maksimal C.

---

*Rubrik mengikat — perubahan via rapat prodi.*
