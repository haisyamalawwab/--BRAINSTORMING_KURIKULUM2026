# OUTLINE MODUL — STI-727 SMART CITY & PEMERINTAHAN DIGITAL

**Kode:** STI-727 | **2 SKS Teori** — 100m Kuliah + 120m Mandiri/minggu | **Semester:** 7
**Prasyarat:** STI-521 IoT | **CPL:** P3, KK3 | **Revisi:** 07112026

---

## 1. Peta Modul & Progres PjBL

```
Mg1 6 Pilar ─► Mg2 SPBE 6 Domain ─► Mg3 Satu Data ─► [Mg4 GIS DASAR TUGAS1 20%]
                                                      │
Mg5 Leaflet ─► Mg6 Choropleth/Heatmap ─► Mg7 Sensor IoT→GIS ─► [Mg8 UTS TERTULIS 30%]
                                                                  │
Mg9 Smart Mobility ─► Mg10 Aduan Warga ─► Mg11 Smart Env ─► [Mg12 COMMAND CENTER TUGAS2 20%]
                                                                  │
Mg13 Keamanan Siber ─► Mg14 Maturity & Audit SPBE ─► Mg15 Masterplan ─► [Mg16 SIDANG MASTERPLAN UAS 30%]
```

Produk: Peta dasar → peta sensor live → arsitektur Command Center → Masterplan 5-tahun + purwarupa portal.

---

## 2. Tujuan per Modul

| Modul | Nama | CPMK | Tujuan Akhir | Beban |
|---|---|---|---|---|
| **M1** | 6 Pilar Smart City | CPMK-1 | Menguraikan 6 pilar & tantangan urbanisasi (contoh 2 kota) | 3.7 jam |
| **M2** | SPBE 6 Domain | CPMK-1 | Menganalisis SPBE berdasar Perpres 95/2018 (matriks 6 domain) | 3.7 jam |
| **M3** | Satu Data | CPMK-3 | Menganalisis interoperabilitas Satu Data & metadata (3 dataset) | 3.7 jam |
| **M4** | GIS Fundamentals | CPMK-1,2 | Membangun peta dasar Leaflet + QGIS (markers+polygon) — **TUGAS1** | 3.7 jam |
| **M5** | Web GIS Leaflet | CPMK-2 | Membangun peta Leaflet dengan custom markers & layers | 3.7 jam |
| **M6** | Choropleth & Heatmap | CPMK-2 | Visualisasi choropleth & heatmap kepadatan | 3.7 jam |
| **M7** | Sensor→GIS | CPMK-2 | Integrasi 3 sensor IoT dummy ke peta real-time | 3.7 jam |
| **M8** | UTS | CPMK-1,2,3 | Ujian tertulis SPBE & GIS | 1.7 jam |
| **M9** | Smart Mobility | CPMK-4 | Menganalisis ITS & fleet tracking | 3.7 jam |
| **M10** | Aduan Warga | CPMK-4 | Merancang wireframe portal aduan geotagging | 3.7 jam |
| **M11** | Smart Environment | CPMK-4 | Menganalisis smart energy & waste | 3.7 jam |
| **M12** | Command Center | CPMK-2,3 | Merancang arsitektur Command Center + peta live — **TUGAS2** | 3.7 jam |
| **M13** | Keamanan Siber | CPMK-2 | Menganalisis proteksi data warga & infra vital | 3.7 jam |
| **M14** | Maturity & Audit | CPMK-1 | Mengevaluasi indeks SPBE & maturity | 3.7 jam |
| **M15** | Masterplan | CPMK-4 | Menyusun masterplan 5-tahun 20 hal | 3.7 jam |
| **M16** | Sidang Masterplan | CPMK-1-4 | Presentasi masterplan + demo purwarupa — **UAS** | 1.7 jam |

---

## 3. Rincian Materi per Modul

### M1 — 6 Pilar Smart City (Mg1)
**Topik:** Smart Governance (e-government, transparansi), Economy (UMKM digital), Living (kesehatan/pendidikan), Mobility (transport), People (literasi), Environment (udara/sampah) — challenges: urbanisasi, kesenjangan digital, funding  
**Case:** Jakarta Smart City (JSC) 6 pilar, Banyuwangi smart village — bedah KPI  
**Aktivitas:** Diskusi kelas 100m + Mandiri 120m (baca Anthopoulos Ch1, resume 500 kata)  
**Sumber:** Anthopoulos, JSC

### M2 — SPBE 6 Domain (Mg2)
**Topik:** Perpres 95/2018: layanan, proses bisnis, data & informasi, aplikasi, infrastruktur, keamanan — arsitektur SPBE nasional vs daerah, 47 indikator  
**Workshop:** Kelompok bedah Perpres pasal 8-15, isi matriks 6 domain untuk kota pilihan  
**Sumber:** Perpres 95/2018, Peta SPBE KemenPAN

### M3 — Satu Data Indonesia (Mg3)
**Topik:** Perpres 39/2019: standar data, metadata DCAT, wali data, interoperabilitas RESTful API SPBE, portal data.go.id, forum Satu Data  
**Workshop:** Analisis 3 dataset di data.go.id (kelengkapan metadata, format, API)  
**Sumber:** Perpres 39/2019, data.go.id

### M4 — GIS Fundamentals (Mg4 — TUGAS1)
**Topik:** Vektor (point/line/polygon) vs raster, WGS84 (lat/lon) vs UTM, GeoJSON (FeatureCollection), Shapefile (.shp/.shx/.dbf), KML, QGIS (load, style, label)  
**Lab:** QGIS load Shapefile batas kecamatan + GeoJSON fasum 10 titik → style + label → export map; Leaflet: `L.map('map').setView([-8,112],13)`, `L.tileLayer OSM`, `L.marker`+`L.polygon`  
**Output Tugas1:** QGIS screenshot + Leaflet HTML + lembar kerja vektor vs raster  
**Sumber:** QGIS Manual, Leaflet quickstart

### M5 — Web GIS Leaflet.js (Mg5)
**Topik:** `L.marker` custom icons ( fasum: sekolah/hospital), `L.geoJSON` dengan `onEachFeature` popup, layer control (`L.control.layers`), events (click → latlon)  
**Hands-on:** Load 20 fasum dari CSV→GeoJSON (via script Python), cluster markers  
**Sumber:** Leaflet docs, leaflet.markercluster

### M6 — Choropleth & Heatmap (Mg6)
**Topik:** Choropleth: quantile vs equal interval, D3 scaleThreshold, warna (YlGnBu), heatmap: Leaflet.heat (radius 25, blur 15) untuk kepadatan penduduk  
**Hands-on:** Visualisasi BPS dummy per kecamatan (choropleth) + titik penduduk (heatmap)  
**Sumber:** Mapbox, Leaflet.heat, D3

### M7 — Sensor IoT→GIS (Mg7)
**Topik:** MQTT Mosquitto, JSON payload `{id, lat, lon, pm2.5, water_level, traffic}`, polling 5s `fetch('/api/sensors')`, warna marker dinamis (hijau <50, kuning 50-100, merah >100 pm2.5)  
**Hands-on:** Dummy sensor API kampus (Node.js) → update marker real-time  
**Sumber:** STI-521 MQTT, dummy API

### M8 — UTS Tertulis (Mg8)
**Kisi:** 6 pilar, 6 domain SPBE, Satu Data, GIS vektor/raster, Leaflet dasar — PG 20 + esai 3 (analisis SPBE, arsitektur aduan banjir)  
**Durasi:** 100m, tanpa HP, open Perpres ringkasan 2 hal (disediakan)

### M9 — Smart Mobility & ITS (Mg9)
**Topik:** ITS: GTFS, optimasi rute angkot (Dijkstra), real-time fleet tracking (GPS→WebSocket), ETA prediction, contoh: TransJakarta, GoTransit  
**Case:** Bedah Gojek routing + TransJakarta tracking — sketsa arsitektur  
**Sumber:** ITS Handbook, Gojek tech

### M10 — Smart Citizen Participation (Mg10)
**Topik:** Portal aduan geotagging: form (kategori: jalan/ sampah/ banjir), foto + latlon auto, workflow: laporan→verifikasi OPD→tindak lanjut→notifikasi, anonimitas  
**Hands-on:** Wireframe Figma 5 screens (home/map, form aduan, daftar aduan, detail, dashboard OPD)  
**Sumber:** Lapor.go.id, FixMyStreet UX

### M11 — Smart Environment (Mg11)
**Topik:** Smart energy: monitoring lampu jalan (kWh per zone), smart meter; smart waste: bin capacity sensor (ultrasonic) → optimasi rute truk (TSP), cost-benefit  
**Diskusi:** Trade-off investasi sensor vs penghematan operasional  
**Sumber:** Smart env papers

### M12 — Command Center (Mg12 — TUGAS2)
**Topik:** Command Center: wall display, integrasi CCTV AI analytics (people counting), telemetri (udara/banjir/traffic), Big Data pipeline, SOP incident (P1/P2/P3), KPI (response time <30m, resolution 80%)  
**Arsitektur:** Sensor → MQTT → Kafka → Dashboard (Grafana) + GIS + Video AI → SOP → OPD  
**Output Tugas2:** Diagram arsitektur (draw.io) + peta GIS live 3 sensors + 1 video AI mock + 2 KPI & SOP 1 hal  
**Sumber:** Command Center refs

### M13 — Keamanan Siber Smart City (Mg13)
**Topik:** UU PDP 27/2022 (hak subjek data), enkripsi telemetri (TLS), anonymization (k-anonymity), OWASP IoT Top10 (weak password, insecure network), proteksi SCADA  
**Case:** Insiden kebocoran data pemerintah kota — risk matrix likelihood×impact  
**Sumber:** UU PDP, OWASP IoT

### M14 — Maturity & Audit SPBE (Mg14)
**Topik:** Evaluasi SPBE (domain, aspek, indikator 47, nilai 1-5), Smart City Maturity: Ad-hoc → Connected → Integrated → Smart, kuesioner audit, evidence  
**Workshop:** Audit SPBE kota X (beri nilai per indikator + bukti), hitung indeks  
**Sumber:** Pedoman Evaluasi SPBE

### M15 — Masterplan Smart City (Mg15)
**Topik:** Dokumen 20 hal: visi, misi, pilar prioritas (pilih 1-2), layanan unggulan 3, roadmap 5 tahun (short/mid/long), anggaran indikatif, stakeholder (Diskominfo, OPD, vendor), KPI, risiko  
**Studio:** Kelompok 4-5 org — pilih pilar (Mobility/Environment/Governance), draft 20 hal (feedback dosen Mg15)  
**Sumber:** Masterplan template FSTI, contoh Banyuwangi masterplan

### M16 — Sidang Masterplan (Mg16 — UAS)
**Agenda:** 10m presentasi masterplan (visi→roadmap), 10m demo purwarupa portal (Leaflet + aduan geotagging), 5m Q&A panel  
**Output UAS:** Masterplan PDF 20 hal + repo purwarupa (HTML/JS) + video demo 3m (unlisted)  
**Kriteria lulus:** Demo live berfungsi (peta + form aduan), masterplan lengkap (visi, layanan 3, roadmap)

---

## 4. Bahan Ajar

| Jenis | Judul | Akses |
|---|---|---|
| Regulasi | Perpres 95/2018 SPBE, 39/2019 Satu Data, UU 27/2022 PDP | jdih.go.id |
| Buku | Anthopoulos *Understanding Smart Cities* (2017) | Perpus |
| Docs | Leaflet.js, Mapbox GL, QGIS Manual, GTFS spec | Online |
| Case | Jakarta Smart City, Banyuwangi Smart Village, Lapor.go.id | Web |
| Standar | Evaluasi SPBE KemenPAN, Smart City Maturity Gartner | PDF |
| Dataset | Shapefile batas admin Malang, BPS kepadatan dummy, sensor dummy API | Lab |

---

## 5. Alat & Lingkungan

- Lab GIS: QGIS 3.34, Leaflet 1.9, Mapbox token edu, OSM tiles, Figma, draw.io
- MQTT broker kampus + dummy sensor API (Node.js)
- LMS + GitHub (peta repo), LMS quiz, Turnitin (laporan masterplan ≤20%)

---

## 6. Skill Ladder

```
Level 1 (Mg1-3): Pahami 6 pilar & SPBE 6 domain & Satu Data (analisis)
Level 2 (Mg4-7): Bangun peta GIS → Leaflet markers → choropleth/heatmap → sensor live
Level 3 (Mg9-11): Rancang layanan Mobility/Partisipasi/Environment (wireframe)
Level 4 (Mg12-14): Arsitektur Command Center → keamanan → audit SPBE
Level 5 (Mg15-16): Masterplan 5-tahun + purwarupa → Demo Day
```

