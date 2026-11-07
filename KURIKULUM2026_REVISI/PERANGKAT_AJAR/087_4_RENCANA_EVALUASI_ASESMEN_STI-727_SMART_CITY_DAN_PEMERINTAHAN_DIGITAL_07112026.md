# RENCANA EVALUASI & ASESMEN — STI-727 SMART CITY & PEMERINTAHAN DIGITAL

**Kode:** STI-727 | **2 SKS Teori** — 100T+120M | **Semester:** 7 | **Prasyarat:** STI-521 IoT
**CPL:** P3, KK3 | **CPMK:** 1 C4 SPBE, 2 C6 Web GIS, 3 C4 Satu Data, 4 C6 Masterplan | **Revisi:** 07112026

---

## 1. Prinsip OBE (008)

- **Authentic:** Masterplan kota nyata + purwarupa portal geotagging, bukan hafalan regulasi
- **Proportional:** Tugas1 20% + UTS 30% + Tugas2 20% + UAS 30% =100% (2 SKS Teori: penilaian tertulis & proyek berbobot seimbang)
- **Transparan:** Rubrik 087_5 terpublikasi Mg1, Turnitin untuk masterplan
- **Formative+Summative:** 10 formatif (non-graded) scaffolding, 4 summative yudisium

---

## 2. Pemetaan CPMK→Asesmen

| CPMK | Bloom | Asesmen Utama | Bobot Efektif | Teknik |
|---|---|---|---|---|
| CPMK-1 SPBE 6 domain | C4 | UTS 60% + Tugas2 20% + UAS 20% | 30% | Matriks domain, audit SPBE |
| CPMK-2 Web GIS | C6 | Tugas1 40% + Tugas2 40% + UAS 20% | 30% | Repo Leaflet, peta sensor live |
| CPMK-3 Satu Data API | C4 | UTS 50% + Tugas2 30% + UAS 20% | 20% | Analisis metadata, rancang API |
| CPMK-4 Masterplan | C6 | UAS 60% + Tugas2 25% + UTS 15% | 20% | Masterplan 20hal + demo |

---

## 3. Rincian Summative

### A. TUGAS1 — Peta Dasar GIS (20% — Mg4)

**Deliverables:** (a) Screenshot QGIS layer batas admin + fasum, (b) Repo HTML/JS Leaflet peta dasar (OSM + 10 markers + 1 polygon zonasi), (c) Lembar kerja 1 hal (vektor vs raster, WGS84)  
**Rubrik (087_5 §A):** GeoJSON valid 30%, markers+polygon 30%, QGIS layer 20%, penjelasan 20%. Minimal 55, remedial 7 hari.  
**Deadline:** Mg4 Jumat 23:59 GitHub Classroom.

### B. UTS — Ujian Tertulis SPBE & Arsitektur Layanan (30% — Mg8)

**Format:** 100m — 20 PG + 3 esai case analysis  
**Kisi:** 6 pilar, 6 domain SPBE (Perpres 95), Satu Data (Perpres 39), GIS konsep, Leaflet dasar  
**Contoh esai:** (1) Analisis SPBE Kota Y (isi matriks 6 domain + gap), (2) Rancang arsitektur layanan aduan banjir (sensor→API→GIS→OPD), (3) Jelaskan choropleth vs heatmap kapan dipakai  
**Rubrik:** PG 40%, esai 60% (kedalaman analisis 20% + arsitektur 20% + GIS 20%). Open ringkasan Perpres 2 hal (disediakan). Susulan H+7.

### C. TUGAS2 — Arsitektur Command Center (20% — Mg12)

**Deliverables:** (a) Diagram arsitektur Command Center (draw.io/PDF) — sensor→MQTT→Kafka→Dashboard+GIS+Video AI→SOP→OPD, (b) Peta GIS live 3 sensor types (udara/banjir/traffic) + 1 video AI mock, (c) 2 KPI (response time, resolution) & SOP 1 hal  
**Rubrik:** Arsitektur 40%, peta live 30%, KPI/SOP 15%, docs 15%. Minimal 55.  
**Deadline:** Mg12 Jumat 23:59.

### D. UAS — Masterplan & Demo Purwarupa (30% — Mg16)

**Format:** Kelompok 4-5 org, Demo Day 100m sesi (5-6 kelompok/hari) — 10m presentasi masterplan, 10m demo purwarupa portal publik (Leaflet + form aduan geotagging), 5m Q&A panel dosen+industri  
**Deliverables:** (a) Masterplan PDF 20 hal (visi, 1-2 pilar prioritas, 3 layanan unggulan, roadmap 5 th, anggaran indikatif, KPI, stakeholder), (b) Repo purwarupa HTML/JS (peta + form aduan → daftar aduan), (c) Video demo 3m unlisted  
**Rubrik (087_5 §D):** Masterplan kedalaman 35%, purwarupa fungsional 30%, demo & Q&A 20%, docs/video 15%. Minimal UAS 50, demo live wajib (tidak boleh video saja). Jika demo gagal total → maksimal C.  
**Sumber:** Rubrik 087_5

---

## 4. Formatif (10 sesi — Non-Graded, Gate UAS)

| Mg | Aktivitas | Output | Jika Gagal |
|---|---|---|---|
|1|Resume 6 pilar 500 kata|Pass ≥60%|Revisi 3 hari|
|2|Matriks 6 domain SPBE|Pass|Bimbingan|
|3|Analisis metadata 3 dataset|Pass|Perbaikan|
|5|Repo Leaflet markers CSV|Pass|Rebuild|
|6|Choropleth+heatmap|Pass|Revisi style|
|7|Dashboard sensor live|≥2 sensor|Perbaikan polling|
|9|Arsitektur fleet tracking|Sketsa|Bimbingan|
|10|Wireframe Figma 5 screen|Pass|Revisi UI|
|13|Risk matrix 5 risiko|Pass|Perbaikan|
|14|Score sheet audit SPBE|Pass|Revisi skor|
|15|Draft masterplan 10 hal|Feedback|Revisi → final 20 hal|

**Aturan:** Tidak kumpul ≥6 formatif → tidak boleh UAS (remedial formatif 7 hari). Kehadiran ≥80%.

---

## 5. Formula Nilai Akhir & Yudisium

```
NA = 0.20×Tugas1 + 0.30×UTS + 0.20×Tugas2 + 0.30×UAS + bonus (max +3)
Bonus: partisipasi aktif >80% sesi +2, video demo berkualitas +1
```

| NA | Huruf | Keterangan |
|---|---|---|
|85-100|A|Lulus sangat baik|
|70-84|B|Lulus baik|
|60-69|C|Lulus bersyarat|
|55-59|D|Tidak lulus remedial|
|<55|E|Gagal|

**Aturan:** NA ≥55 (C) dengan UAS ≥50 & hadir ≥80%. Jika NA ≥60 tetapi UAS <50 → maksimal C. Remedial Tugas1/2 7 hari (nilai maks B), UAS remedial 14 hari (maks B).

---

## 6. Integritas

- Masterplan Turnitin ≤20% (kecuali template & regulasi sitasi). Wajib lampirkan log Turnitin.
- Code Leaflet original, MOSS >30% antar kelompok → investigasi → 0 jika copy-paste.
- AI-assistance (Copilot) disclosure di README, tanpa disclosure & terdeteksi → -20%.

---

## 7. Jadwal Ilustratif Ganjil 2026/2027

| Milestone | Tanggal | Tempat |
|---|---|---|
|Tugas1|Mg4 Jumat|GitHub Classroom|
|UTS|Mg8 Kamis 08:00-10:00|Kelas (tertulis)|
|Tugas2|Mg12 Jumat|Classroom|
|UAS Demo Day|Mg16 Senin-Selasa 08:00-17:00|Aula FSTI|

---

*Rubrik detail 087_5 terlampir.*

