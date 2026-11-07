# RPS — STI-727 SMART CITY & PEMERINTAHAN DIGITAL

**Program Studi:** S1 SISTEKIN | **Semester:** 7 | **Kode:** STI-727 | **Nama EN:** Smart City & Digital Governance
**SKS/Tipe:** 2 SKS / Teori (100m Kuliah + 120m Mandiri/minggu) | **Rumpun:** Sistem Informasi & Tata Kelola — Core STI
**Prasyarat:** STI-521 Internet of Things (IoT) | **Dosen:** Tim Tata Kelola TI | **Revisi:** 07112026
**CPL:** P3 (Infrastruktur Kota Cerdas & SPBE), KK3 (Integrasi GIS & Telemetri Perkotaan) — IS2020 BK-GOV01, BK-IS19

---

## 1. Identitas & Pemetaan

| Atribut | Spesifikasi |
|---|---|
| **Kode & Nama** | STI-727 Smart City & Pemerintahan Digital |
| **Semester/Rumpun** | 7 / Tata Kelola — Core STI (79 SKS Core total) |
| **Prasyarat** | STI-521 IoT — wajib menguasai sensor, MQTT, GIS dasar |
| **CPL** | P3 Infrastruktur & Tata Kelola TI; KK3 Infrastruktur Cloud/IoT & Ketahanan Siber (spesifik: GIS & Telemetri Kota) |
| **PL** | PL-2 Smart Systems Integrator & PL-4 IT Project Manager |
| **PEO** | PEO-1 Professional Practice |
| **BoK** | IS2020 BK-GOV01 (IT Governance), BK-IS19 (Smart City), IT2017 KK2/KK3 |

MK ini membekali analisis SPBE (Perpres 95/2018), Satu Data Indonesia, Web GIS (Leaflet/Mapbox), sensor perkotaan, Command Center, hingga masterplan 5-tahunan.

---

## 2. Deskripsi MK

Mahasiswa mempelajari **6 pilar Smart City** (Governance, Economy, Living, Mobility, People, Environment) dan **kerangka SPBE nasional** (6 domain: layanan, proses bisnis, data, aplikasi, infrastruktur, keamanan). Melalui **Case Method & PjBL**, mahasiswa membangun **peta digital interaktif** (Web GIS Leaflet + telemetri sensor IoT), merancang **interoperabilitas Satu Data** (RESTful API SPBE, metadata, keamanan), dan menyusun **masterplan + purwarupa portal layanan publik cerdas** (smart mobility, aduan warga geotagging, command center) yang dipresentasikan sebagai **masterplan kota** pada Demo Day.

Relevansi: Smart City Consultant, Digital Governance Analyst, GIS Developer, SPBE Auditor.

---

## 3. CPL Dibebankan

| CPL | Deskripsi | Indikator MK |
|---|---|---|
| **P3** | Menguasai infrastruktur TI, jaringan, cloud, keamanan, tata kelola & manajemen proyek | Mampu memetakan 6 domain SPBE & menganalisis maturitas SPBE daerah |
| **KK3** | Merancang & mengelola infrastruktur cloud/IoT & ketahanan siber andal terukur aman | Mampu membangun Web GIS + integrasi telemetri sensor & merancang Command Center |

---

## 4. CPMK (ABCD & Bloom)

| Kode | Rumusan CPMK | Bloom | CPL |
|---|---|---|---|
| **CPMK-1** | Mahasiswa (A) mampu **menganalisis** arsitektur SPBE (B) berdasar Perpres 95/2018 (C) dengan 6 domain (D) | C4 | P3 |
| **CPMK-2** | Mahasiswa (A) mampu **membangun** peta digital interaktif (B) via Web GIS Leaflet/Mapbox + telemetri sensor (C) visual fungsional (D) | C6 | KK3 |
| **CPMK-3** | Mahasiswa (A) mampu **merancang** skema interoperabilitas Satu Data (B) berdasar prinsip Satu Data & API SPBE (C) aman terstandar (D) | C4 | P3,KK3 |
| **CPMK-4** | Mahasiswa mampu **menyusun** masterplan & purwarupa layanan publik cerdas (B) pada salah satu pilar Smart City (C) komprehensif (D) | C6 | P3,KK3 |

---

## 5. Matriks 16 Minggu

| Mg | Sub-CPMK & Bahan Kajian | Metode (100T+120M) | Asesmen & Bobot | Sumber |
|---|---|---|---|---|
| 1 | 6 pilar Smart City & tantangan urbanisasi (C2) — Governance/Economy/Living/Mobility/People/Environment | Kuliah interaktif 100m + diskusi kasus Jakarta/Surabaya Smart City 120m | Formatif quiz | [A1] Smart City Framework, [A2] Case Jakarta |
| 2 | Kerangka SPBE Perpres 95/2018 — 6 domain (layanan, proses bisnis, data, aplikasi, infra, keamanan) (C4) | Ceramah & telaah regulasi 100m + studi kasus SPBE nasional | Formatif analisis domain | [B1] Perpres 95/2018, [B2] Peta SPBE KemenPAN |
| 3 | Satu Data Indonesia: standar data, metadata, interoperabilitas API (C4) | Case Method 100m + workshop metadata | Formatif | [B3] Perpres Satu Data 39/2019, [B4] API SPBE docs |
| **4** | **Pengantar GIS: vektor/raster, WGS84, GeoJSON/Shapefile (C2)** | Kuliah+Lab GIS (QGIS/Leaflet intro) | **TUGAS1 20%** — Lembar kerja GIS + peta dasar | [C1] QGIS, [C2] Leaflet |
| 5 | Web GIS Leaflet.js: markers, layers, OSM tiles (C3) | Lab Coding Leaflet 220m | Formatif — web peta markers | [C2] Leaflet docs |
| 6 | Spatial Analysis: choropleth & heatmap kepadatan (C4) | Lab Hands-on 220m | Formatif — heatmap submit | [C3] Mapbox, D3 choropleth |
| 7 | Sensor IoT → Web GIS: kualitas udara, banjir, CCTV traffic (C4) | Case+Lab integrasi MQTT→GIS dashboard | Formatif — sensor dashboard | [D1] STI-521 IoT, MQTT |
| **8** | **UTS — Analisis Domain SPBE & Arsitektur Layanan Smart City** | Ujian tertulis case analysis 100m | **UTS 30%** | Bank soal Mg1-7 |
| 9 | Smart Mobility & ITS: rute angkot, fleet tracking real-time (C4) | Case-Based Learning 220m | Formatif — analisis rute | [A3] ITS, Smart Mobility |
| 10 | Smart Citizen Participation: aduan warga geotagging + portal partisipasi (C4) | Case+Lab wireframe portal aduan | Formatif — wireframe | [E1] Lapor!, FixMyStreet |
| 11 | Smart Environment: monitoring energi publik & smart waste bin (C4) | Ceramah & diskusi 220m | Formatif | [A4] Smart Env |
| **12** | **Command Center perkotaan terpadu: video AI, telemetri, Big Data (C5)** | Problem-Solving Class 220m | **TUGAS2 20%** — Arsitektur Command Center + peta GIS sensor live | [F1] Command Center ref |
| 13 | Keamanan siber Smart City: proteksi data pribadi & infra vital (C4) | Case Method 220m | Formatif — risk matrix | [G1] OWASP IoT, PDP Law |
| 14 | Maturity Index Smart City & Indeks SPBE (C5) | Workshop evaluasi 220m — audit SPBE kota X | Formatif — audit score | [B5] Evaluasi SPBE, [A5] Maturity Model |
| 15 | PjBL Masterplan Smart City: roadmap 5-tahun (C6) | Studio PjBL 220m — dokumen masterplan 20 hal | Formatif — draft masterplan | [A6] Masterplan template |
| **16** | **UAS — Sidang Masterplan & Demonstrasi Purwarupa Portal Publik** | Demo Day & Defense 100m (10m presentasi + 10m demo + 5m Q&A) | **UAS 30%** | Rubrik 087_5 |

**Bobot:** Tugas1 20% (Mg4) + UTS 30% (Mg8) + Tugas2 20% (Mg12) + UAS 30% (Mg16) = 100% (penyesuaian 2 SKS Teori).

---

## 6. Pengalaman Belajar

- Case Method 40%: bedah SPBE Kemendagri, Smart City Banyuwangi, Jakarta Smart City (JSCLounge)
- PjBL 40%: masterplan kelompok 4-5 org (pilih 1 pilar: Mobility/Environment/Governance), peta GIS + portal aduan
- Field Study: kunjungan virtual Command Center / wawancara Diskominfo (opsional)
- Guest: Praktisi SPBE KemenPAN-RB & GIS Engineer

---

## 7. Asesmen Ringkas

| Komponen | Bentuk | CPMK | Bobot |
|---|---|---|---|
| Tugas1 Mg4 | Lembar kerja GIS + peta dasar (Leaflet) | CPMK-1,2 | 20% |
| UTS Mg8 | Ujian tertulis analisis SPBE & arsitektur layanan | CPMK-1,2,3 | 30% |
| Tugas2 Mg12 | Arsitektur Command Center + peta GIS sensor live | CPMK-2,3 | 20% |
| UAS Mg16 | Masterplan 20hal + purwarupa portal + demo | CPMK-1-4 | 30% |

Minimal C (55), UAS ≥50, hadir ≥80%.

---

## 8. Sumber Belajar

1. Perpres 95/2018 SPBE, Perpres 39/2019 Satu Data, PermenPAN SPBE
2. Anthopoulos — *Understanding Smart Cities* (2017)
3. Leaflet.js docs, Mapbox GL JS, QGIS Training Manual
4. Jakarta Smart City & Bandung Smart City case studies
5. OWASP IoT Top10, UU PDP No.27/2022
6. Indeks SPBE & Maturity Model KemenPAN
7. FSTI Masterplan Template

---

## 9. Fasilitas

- Lab GIS (QGIS, Leaflet, Mapbox token edukasi, OSM)
- Dataset: Shapefile batas admin, data kepadatan BPS, dummy sensor (kualitas udara, banjir)
- LMS + GitHub untuk peta repo

---

*Disahkan Kaprodi SISTEKIN — perubahan bobot via rapat kurikulum.*
