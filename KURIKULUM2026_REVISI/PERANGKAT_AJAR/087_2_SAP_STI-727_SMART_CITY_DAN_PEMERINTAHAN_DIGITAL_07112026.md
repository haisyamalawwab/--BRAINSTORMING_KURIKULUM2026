# SAP — STI-727 SMART CITY & PEMERINTAHAN DIGITAL

**Kode:** STI-727 | **SKS:** 2 Teori (100T+120M/minggu) | **Semester:** 7 | **Prasyarat:** STI-521 IoT
**CPL:** P3, KK3 | **CPMK:** 1 C4 SPBE, 2 C6 Web GIS, 3 C4 Satu Data, 4 C6 Masterplan | **Revisi:** 07112026

---

## A. Deskripsi SAP

SAP 16 minggu teori dengan Case Method + PjBL. **Bobot:** Tugas1 20% (Mg4 GIS) + UTS 30% (Mg8 tertulis) + Tugas2 20% (Mg12 Command Center) + UAS 30% (Mg16 Masterplan Demo) = 100%. Lulus minimal **C (55)**, hadir ≥80%.

---

## B. Rencana Mingguan Detail

### Mg1 — 6 Pilar Smart City (C2)
**Bahan:** Governance, Economy, Living, Mobility, People, Environment — tantangan urbanisasi, urban sprawl, digital divide  
**Metode:** Kuliah 100m + diskusi kasus Jakarta Smart City & Surabaya Smart City (120m mandiri: baca Anthopoulos Ch1-2)  
**Tugas:** Resume 500 kata 6 pilar + contoh kota (non-graded)  
**Sumber:** Anthopoulos, JSCLounge

### Mg2 — Kerangka SPBE Perpres 95/2018 (C4)
**Bahan:** 6 domain SPBE (layanan, proses bisnis, data, aplikasi, infrastruktur, keamanan), arsitektur SPBE nasional/daerah, Perpres 95/2018 pasal kunci  
**Metode:** Ceramah 50m + telaah regulasi kelompok (bedah Perpres pasal 8-15) 50m + Mandiri 120m (rangkum domain SPBE kota pilihan)  
**Asesmen:** Formatif — matriks 6 domain untuk kota X (pass/fail)  
**Sumber:** Perpres 95/2018, Peta SPBE KemenPAN-RB

### Mg3 — Satu Data Indonesia (C4)
**Bahan:** Perpres 39/2019, standar data, metadata (DCAT), interoperabilitas API SPBE, forum Satu Data  
**Metode:** Case Method 100m — bedah portal Satu Data Indonesia (data.go.id) + Workshop metadata 120m  
**Asesmen:** Formatif — analisis 3 dataset (metadata completeness)  
**Sumber:** Perpres 39/2019, data.go.id docs

### Mg4 — Pengantar GIS: Vektor/Raster/WGS84 (TUGAS1 — 20%)
**Bahan:** Format GeoJSON, Shapefile, KML, koordinat WGS84 vs UTM, layer (point/line/polygon), QGIS dasar, Leaflet intro  
**Metode:** Kuliah 50m + Lab GIS 50m (QGIS load Shapefile batas admin + GeoJSON fasilitas) + Mandiri 120m  
**Praktikum:** Buat peta dasar Leaflet: OSM tiles + 10 markers fasum + 1 polygon zonasi (RT/RW dummy)  
**Asesmen:** **TUGAS1 (20%)** — Submit: (a) Screenshot QGIS layer, (b) Repo Leaflet peta dasar (HTML+JS), (c) Lembar kerja GIS (jelaskan vektor vs raster). **Rubrik:** GeoJSON valid 30%, markers & polygon 30%, QGIS layer 20%, penjelasan 20%. **Deadline:** Mg4 Jumat  
**Sumber:** QGIS Manual, Leaflet quickstart

### Mg5 — Web GIS Leaflet.js (C3)
**Bahan:** Leaflet.js: `L.map`, `L.tileLayer`, `L.marker` custom icons, `L.geoJSON`, popups, layer control, event click  
**Metode:** Lab Coding 100m + Mandiri 120m (tambahkan 20 markers fasum dari CSV)  
**Asesmen:** Formatif — repo update markers CSV → GeoJSON  
**Sumber:** Leaflet docs

### Mg6 — Spatial Analysis: Choropleth & Heatmap (C4)
**Bahan:** Choropleth (kepadatan penduduk per kecamatan), heatmap (Leaflet.heat), klasifikasi (quantile), D3 color scale  
**Metode:** Lab Hands-on 100m + Mandiri 120m (visualisasi data BPS dummy)  
**Asesmen:** Formatif — peta choropleth + heatmap submit  
**Sumber:** Mapbox, D3, Leaflet.heat plugin

### Mg7 — Sensor IoT → Web GIS (C4)
**Bahan:** MQTT broker (Mosquitto), payload JSON sensor {pm2.5, water_level, traffic_count}, dashboard Web GIS real-time (polling/fetch 5s), Leaflet marker update warna (hijau/kuning/merah)  
**Metode:** Case+Lab 100m — integrasi dummy sensor API → peta + Mandiri 120m  
**Asesmen:** Formatif — dashboard sensor live (3 sensor types)  
**Sumber:** STI-521 MQTT, dummy sensor API kampus

### Mg8 — UTS Tertulis (30%)
**Materi:** Mg1-7 — analisis domain SPBE, arsitektur layanan Smart City, GIS concept, Satu Data  
**Format:** Ujian tertulis 100m: 20 soal PG + 3 esai case analysis (analisis SPBE kota Y, rancang arsitektur layanan aduan banjir)  
**Rubrik:** PG 40%, esai (kedalaman analisis SPBE 20%, arsitektur 20%, GIS 20%) — total 60% esai. Susulan H+7  
**Sumber:** Bank soal

### Mg9 — Smart Mobility & ITS (C4)
**Bahan:** ITS (Intelligent Transport System): rute optimasi angkot, real-time fleet tracking (GPS → WebSocket), GTFS, ETA prediction sederhana  
**Metode:** Case-Based Learning 100m (bedah Gojek/Grab + TransJakarta) + Mandiri 120m  
**Asesmen:** Formatif — sketsa arsitektur fleet tracking  
**Sumber:** ITS handbook, Gojek tech blog

### Mg10 — Smart Citizen Participation (C4)
**Bahan:** Portal aduan warga geotagging (Lapor! ref), kategori aduan, workflow (laporan→verifikasi→tindak lanjut), UI wireframe, anonimitas & validasi foto  
**Metode:** Case+Lab wireframe Figma 100m + Mandiri 120m  
**Asesmen:** Formatif — wireframe portal aduan (5 screen)  
**Sumber:** Lapor.go.id, FixMyStreet

### Mg11 — Smart Environment (C4)
**Bahan:** Smart energy (monitoring konsumsi lampu jalan, smart meter), smart waste (bin capacity sensor → optimasi rute truk sampah)  
**Metode:** Ceramah & diskusi 100m + Mandiri 120m (analisis trade-off biaya vs efisiensi)  
**Asesmen:** Formatif — 1 hal analisis cost-benefit smart waste  
**Sumber:** Smart environment papers

### Mg12 — Command Center (TUGAS2 — 20%)
**Bahan:** Smart City Command Center: integrasi video AI analytics (CCTV), telemetri sensor, Big Data dashboard, SOP incident, wall display, KPI (response time, resolution rate)  
**Metode:** Problem-Solving Class 100m — rancang arsitektur Command Center untuk kota 500K penduduk + Mandiri 120m  
**Asesmen:** **TUGAS2 (20%)** — Submit: (a) Diagram arsitektur Command Center (layanan, data flow, infra), (b) Peta GIS live 3 sensor types + 1 video AI mock, (c) 2 KPI & SOP 1 hal. **Rubrik:** Arsitektur 40%, peta live 30%, KPI/SOP 15%, docs 15%. **Deadline:** Mg12 Jumat  
**Sumber:** Command Center Banyuwangi, Jakarta Smart City ref

### Mg13 — Keamanan Siber Smart City (C4)
**Bahan:** Proteksi data pribadi warga (UU PDP 27/2022), infra vital (SCADA, CCTV), OWASP IoT Top10, enkripsi telemetri, anonymization  
**Metode:** Case Method 100m — bedah insiden kebocoran data kota + Mandiri 120m  
**Asesmen:** Formatif — risk matrix (likelihood×impact) 5 risiko  
**Sumber:** UU PDP, OWASP IoT

### Mg14 — Maturity Index & Audit SPBE (C5)
**Bahan:** Indeks SPBE (KemenPAN-RB: domain + aspek + indikator 47), Smart City Maturity (Connected, Integrated, Smart), audit lapangan, kuesioner  
**Metode:** Workshop evaluasi 100m — audit SPBE kota X (nilai 1-5 per indikator) + Mandiri 120m  
**Asesmen:** Formatif — score sheet audit SPBE  
**Sumber:** Pedoman Evaluasi SPBE, Gartner maturity

### Mg15 — Masterplan Smart City (C6)
**Bahan:** Dokumen masterplan 5-tahun: visi, pilar prioritas, layanan unggulan (3), roadmap (tahapan), anggaran indikatif, KPI, stakeholder (Diskominfo, OPD)  
**Metode:** PjBL Studio 100m — penyusunan masterplan kelompok 20 hal + Mandiri 120m  
**Asesmen:** Formatif — draft masterplan 10 hal (feedback dosen)  
**Sumber:** Masterplan template FSTI

### Mg16 — UAS Demo Day (30%)
**Format:** Sidang 100m per kelompok: 10m presentasi masterplan (visi→roadmap), 10m demo purwarupa portal publik (Leaflet + aduan geotagging), 5m Q&A  
**Deliverables:** Masterplan PDF 20 hal + repo purwarupa + video demo 3m  
**Rubrik:** Masterplan kedalaman 35%, purwarupa fungsional 30%, demo & Q&A 20%, docs & video 15% — minimal UAS 50 untuk lulus  
**Sumber:** Rubrik 087_5

---

## C. Tugas Terstruktur

| Tugas | Output | Bobot | Deadline |
|---|---|---|---|
| Tugas1 Mg4 | Peta dasar Leaflet + QGIS layer + lembar kerja | 20% | Mg4 Jumat |
| UTS Mg8 | Ujian tertulis SPBE & GIS | 30% | Mg8 |
| Tugas2 Mg12 | Arsitektur Command Center + peta live | 20% | Mg12 Jumat |
| UAS Mg16 | Masterplan + purwarupa + demo | 30% | Mg16 |

Keterlambatan -10%/hari, plagiarisme Turnitin >20% = revisi wajib.

---

## D. Aturan

- Hadir ≥80%, izin H+3 surat. Diskusi aktif dinilai partisipasi (bonus +2 poin NA jika aktif >80% sesi).
- Etika: data BPS/sensor dummy privacy-safe, tidak menyalahgunakan data pribadi warga simulasi.
- Kolaborasi kelompok 4-5 org, peer eval untuk UAS.

