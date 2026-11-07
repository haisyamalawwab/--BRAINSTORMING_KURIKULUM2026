# 060_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-306 — ANALISIS DAN PERANCANGAN SISTEM INFORMASI (*Information Systems Analysis and Design*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI306` · **Bobot:** 3 SKS Teori · **Semester:** 3  
**Klaster Asesmen MK (Dok 018):** Klaster 4 (`K-4`) — Sintesis, Manajemen, Startup & Capstone  
**CPL Dibebankan:** `CPL-02` (`KU1` = **20%**) & `CPL-06` (`P2` = **80%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Mata kuliah `STI-306 Analisis dan Perancangan Sistem Informasi` (3 SKS Teori) menerapkan skema penilaian **Klaster 4 (`K-4`)** dengan pemetaan 1-ke-1 ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-02` / `KU1`)** — *Case-Based Stakeholder Elicitation & SRS IEEE 830*.
* **UTS (Pekan 8 — 30%) → `CPMK-2` (`CPL-06` / `P2`)** — *Case-Method Written Exam: BPMN 2.0 As-Is vs To-Be*.
* **Tugas 2 (Pekan 12 — 20%) → `CPMK-3` (`CPL-06` / `P2`)** — *Case-Based Object-Oriented UML 2.5 Modeling Suite*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-06` / `P2`)** — *Team-Based Project Software Design Document (SDD) & Individual Defense*.
* **Verifikasi Kepatuhan IKU 7 ($\ge 50\%$):** Bobot evaluasi berbasis pemecahan kasus mitra nyata & proyek tim = `Tugas 1 (20%) + Tugas 2 (20%) + UAS (30%)` = **70%** *(selaras 100% dengan target kepatuhan IKU 7 pada Dokumen 004 sebesar 70%)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-02`**<br>(`KU1` — 20%)<br>*Level: R* | **`CPMK-1`**<br>(C4) | `Sub-CPMK-1.1` | Mg 4 | Penugasan berbasis kasus nyata: Elisitasi kebutuhan pemangku kepentingan & analisis masalah PIECES + kuis verifikasi 20' | **RTM-1 (Tugas 1)** Bagian A + Kuis Verifikasi + Rubrik T1 | Sumatif | 9% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Penugasan berbasis kasus nyata: Penyusunan dokumen **SRS IEEE 830 / ISO 29148** & matriks RTM awal | **RTM-1 (Tugas 1)** Bagian B + Rubrik Analitik T1 | Sumatif | 11% | |
| **`CPL-06`**<br>(`P2` — 80%)<br>*Level: R* | **`CPMK-2`**<br>(C4) | `Sub-CPMK-2.1` | Mg 8 | Tes tertulis studi kasus terjadwal: Pemodelan alur proses bisnis organisasi dengan notasi **BPMN 2.0** | **Naskah Soal UTS** (Bagian 1 & 3) + Rubrik Analitik UTS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Tes tertulis studi kasus terjadwal: Analisis *bottleneck* & perancangan ulang proses bisnis *As-Is* ke *To-Be* | **Naskah Soal UTS** (Bagian 2 & 3) + Rubrik Analitik UTS | Sumatif | 15% | |
| **`CPL-06`**<br>(`P2` — 80%)<br>*Level: R* | **`CPMK-3`**<br>(C4) | `Sub-CPMK-3.1` | Mg 12 | Penugasan pemodelan sistem: *Use Case Diagram*, skenario *fully dressed*, & *Activity Diagram* UML 2.5 | **RTM-2 (Tugas 2)** Bagian Fungsional + Verifikasi 20' | Sumatif | 8% | **20%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Penugasan pemodelan sistem: *Class Diagram*, *Sequence Diagram*, & *State Machine Diagram* konsisten | **RTM-2 (Tugas 2)** Bagian Struktural/Dinamis + Rubrik T2 | Sumatif | 12% | |
| **`CPL-06`**<br>(`P2` — 80%)<br>*Level: R* | **`CPMK-4`**<br>(C5) | `Sub-CPMK-4.1` | Mg 16 | Proyek tim + sidang individu: Penyusunan arsitektur SDD (*Package/Deployment*, skema DB, kontrak REST API) | **Bundel SDD IEEE 1016** & Sidang UAS + Rubrik UAS | Sumatif | 16% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Proyek tim + sidang individu: *Dialog Navigation*, keselarasan NFR bisnis, & audit *end-to-end traceability* | **Bundel SDD IEEE 1016** & Tanya-Jawab Individu UAS | Sumatif | 14% | |
| — | *Seluruh CPMK* | *Seluruh Sub-CPMK* | Mg 1–3, 5–7, 9–11, 13–15 | *Role-play* wawancara, *peer-audit* SRS/UML, klinik arsitektur SDD | Ceklis umpan balik kelas | Formatif | 0% | **0%** |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (1-to-1 CPMK)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN (STANDAR KPT 2024 LAMPIRAN 23)

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Elisitasi & Dokumen SRS IEEE 830)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Bobot / Pekan** | `STI-306` Analisis dan Perancangan Sistem Informasi · **20%** · Rilis **Pekan 3**, Kumpul & Verifikasi **Pekan 4** |
| **CPMK & Sub-CPMK Diukur** | **`CPMK-1`** (`Sub-CPMK-1.1` & `Sub-CPMK-1.2` [C4]) → Mendukung **`CPL-02` (`KU1`)**. |
| **1. Tujuan Tugas** | Membuktikan kemampuan berpikir kritis dan analitis mahasiswa dalam mengelisitasi kebutuhan pemangku kepentingan nyata serta menuangkannya menjadi spesifikasi SRS berstandar IEEE 830 / ISO 29148 yang bebas ambiguitas dan dapat diuji. |
| **2. Objek Garapan** | Satu domain proses bisnis pada organisasi mitra nyata yang dipilih kelompok (setiap anggota tim bertanggung jawab penuh atas **1 sub-modul fungsional berbeda** agar akuntabilitas individu terukur jelas). |
| **3. Batasan Pengerjaan** | 1. Melampirkan bukti elisitasi nyata (pedoman pertanyaan, ringkasan transkrip wawancara/observasi, & diagnosis masalah PIECES).<br>2. Menyusun naskah **SRS IEEE 830** yang memuat minimal **12 butir *Functional Requirements* (`FR-01`..`FR-12`)** per sub-modul dan **6 butir *Non-Functional Requirements* (`NFR-01`..`NFR-06`)** dengan metrik kuantitatif tegas (waktu tanggap dalam detik, kapasitas pengguna, aturan enkripsi/akses).<br>3. Menyertakan tabel prioritas MoSCoW dan *Requirements Traceability Matrix* (RTM) awal.<br>4. Mengikuti kuis konfirmasi tertulis 20 menit di kelas pada Pekan 4. |
| **4. Luaran Tugas** | Berkas `STI306_T1_SRS_[KodeTim]_[NIM].pdf` yang diunggah ke LMS Edlink. |
| **5. Kriteria & Bobot** | (1) Ketajaman elisitasi bukti lapangan & diagnosis masalah PIECES (30%); (2) Ketepatan & keterukuran spesifikasi FR/NFR standar IEEE 830 (35%); (3) Keterlacakan RTM & konsistensi kuis verifikasi kelas (20%); (4) Tata tulis formal dokumen rekayasa (15%). |

---

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Studi Kasus BPMN 2.0)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Format & Durasi** | Ujian Tertulis Studi Kasus Luring Terjadwal (*Closed-Book*, **150 menit**) · Bobot **30%** · Mengukur **`CPMK-2`** (`CPL-06`). |
| **Struktur Kasus Uji** | Diberikan satu skenario naratif rinci (1,5 halaman) mengenai alur operasional lintas-unit dan lintas-instansi yang bermasalah (mis. *Proses Rujukan Pasien, Klaim Asuransi, & Penebusan Obat Rumah Sakit* atau *Proses Pengadaan Bahan Baku, Inspeksi Gudang, & Pembayaran Vendor*).<br>• **Soal 1 (35% — `Sub-CPMK-2.1`):** Gambarkan model **BPMN 2.0 *As-Is*** secara lengkap menggunakan *Pools, Lanes, Start/Intermediate/End Events, Tasks,* dan *Gateways* (`XOR`, `AND`, `OR`), lengkap dengan pembedaan tepat antara *Sequence Flow* dan *Message Flow*.<br>• **Soal 2 (35% — `Sub-CPMK-2.2`):** Identifikasi minimal 4 aktivitas *Non-Value-Adding* / *bottleneck* pada model *As-Is*, lalu rancang model **BPMN 2.0 *To-Be*** terintegrasi sistem informasi beserta tabel perbandingan jumlah langkah manual vs terotomasi.<br>• **Soal 3 (30% — `Sub-CPMK-2.1 & 2.2`):** Turunkan seluruh *User Task* dan *Service Task* pada BPMN *To-Be* menjadi daftar kebutuhan layanan sistem dan matriks hak akses aktornya. |

---

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Paket Pemodelan UML 2.5 Konsisten)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Bobot / Pekan** | `STI-306` Analisis dan Perancangan Sistem Informasi · **20%** · Rilis **Pekan 10**, Kumpul & Verifikasi **Pekan 12** |
| **CPMK & Sub-CPMK Diukur** | **`CPMK-3`** (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C4]) → Mendukung **`CPL-06` (`P2`)**. |
| **1. Tujuan Tugas** | Menguji ketepatan analisis dan konsistensi silang mahasiswa dalam memodelkan aspek fungsional, struktural, dan interaksi dinamis sistem informasi menggunakan standar **UML 2.5**. |
| **2. Batasan Pengerjaan** | Setiap mahasiswa pada sub-modul tanggung jawabnya wajib menghasilkan paket 5 diagram UML 2.5 yang **100% saling konsisten**:<br>1. **Use Case Diagram** sistem terpadu + minimal **3 spesifikasi skenario naratif *fully dressed*** (memuat alur normal & alternatif/eksepsi).<br>2. **Activity Diagram** ber-*swimlane* untuk 3 *Use Case* tersebut.<br>3. **Design Class Diagram** lengkap (minimal 8 kelas berstereotip/berelasi, memuat atribut bertipe data, operasi metode berparameter, *visibility* `+/-/ #`, dan *multiplicity* tepat).<br>4. **Sequence Diagram** untuk 3 *Use Case* tersebut (wajib memuat minimal 1 *combined fragment* `alt` atau `loop`, dengan nama pesan metode yang **identik** dengan operasi pada *Class Diagram*).<br>5. **State Machine Diagram** untuk minimal 1 entitas berstatus kompleks pada modulnya. |
| **3. Luaran & Verifikasi** | Berkas `STI306_T2_UML_[KodeTim]_[NIM].pdf` + berkas sumber model (`.mdj`/`.puml`/`.vpp`) di Edlink + sesi verifikasi lisan/tertulis 20 menit di kelas Pekan 12. |
| **4. Kriteria & Bobot** | (1) Ketepatan model fungsional *Use Case* & *Activity* (25%); (2) Ketepatan model struktural & dinamis *Class, Sequence, State Machine* (35%); (3) Konsistensi silang antar-diagram UML (25%); (4) Kerapian standar notasi UML 2.5 & penguasaan verifikasi (15%). |

---

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Dokumen SDD & Sidang)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Arsitektur Penilaian UAS** | Mengukur **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5] → **`CPL-06`**) sebesar **30% Nilai Akhir MK**, terdiri atas:<br>• **Komponen A — Dokumen *Software Design Document* (SDD) Berstandar IEEE 1016 (60% nilai UAS):** Memuat arsitektur paket berlapis (*Package Diagram*), topologi penempatan (*Deployment Diagram*), konsolidasi model UML 2.5 terverifikasi, pemetaan *Class-to-Relational Database Schema* (3NF + kamus data), spesifikasi kontrak antarmuka **REST API** (minimal 8 endpoint lengkap skema JSON *request/response*), *Dialog Navigation Diagram*, penyelarasan NFR bisnis, dan *End-to-End Traceability Matrix* (`SRS ↔ BPMN ↔ UML ↔ DB/API`). **Bebas dari kode program aplikasi sesuai *guardrail* MK.**<br>• **Komponen B — Sidang Presentasi & Pertahanan Individu (40% nilai UAS, 150 menit):** Penguji menilai penguasaan individual setiap anggota tim dalam menelusuri dan mempertanggungjawabkan keputusan arsitektur serta keterlacakan desainnya. |

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-306}}$)
$$\text{Score}_{\text{CPMK-1}} = S_{\text{Tugas 1}}, \quad \text{Score}_{\text{CPMK-2}} = S_{\text{UTS}}, \quad \text{Score}_{\text{CPMK-3}} = S_{\text{Tugas 2}}, \quad \text{Score}_{\text{CPMK-4}} = S_{\text{UAS}}$$
$$NA_{\text{STI-306}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004 & 008)
Karena `STI-306` mendukung dua CPL sekaligus pada level *Reinforce* (`R`), skor kontribusi mahasiswa $i$ dihitung terpisah secara presisi:
1. **Ketercapaian `CPL-02` (`KU1` — bobot 20% MK dari `CPMK-1`):**
   $$\text{Score}_{\text{CPL-02, STI-306}}(i) = S_{\text{Tugas 1}}(i) \quad (\text{bobot SKS tertimbang} = 3 \times 0,20 = 0,60\text{ SKS})$$
2. **Ketercapaian `CPL-06` (`P2` — bobot 80% MK dari `CPMK-2`, `CPMK-3`, & `CPMK-4`):**
   $$\text{Score}_{\text{CPL-06, STI-306}}(i) = \frac{0,30\,S_{\text{UTS}}(i) + 0,20\,S_{\text{Tugas 2}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,80} = 0,375\,S_{\text{UTS}}(i) + 0,250\,S_{\text{Tugas 2}}(i) + 0,375\,S_{\text{UAS}}(i)$$
   *(dengan bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,80 = 2,40\text{ SKS}$).*

### 4.3 Tabel Konversi Nilai Huruf & Protokol Remedial
* **Skala Mutu UWG & Ambang OBE:** **A** ($81,00\text{–}100$ / $4,00$); **B+** ($76,00\text{–}80,99$ / $3,50$); **B** ($70,00\text{–}75,99$ / $3,00$); **C+** ($65,00\text{–}69,99$ / $2,50$ — **Batas Minimum Tercapai OBE $\ge 65,0$**); **C** ($56,00\text{–}64,99$ / $2,00$ — *Wajib Remedial CPMK Terkait*); **D** ($45,00\text{–}55,99$); **E** ($< 45,00$).
* **Protokol Remedial & Audit Guardrail:** Mahasiswa dengan nilai CPMK $< 65,0$ wajib memperbaiki artefak spesifik yang belum tuntas (perbaikan SRS, ujian ulang kasus BPMN, revisi konsistensi UML, atau revisi SDD) dengan nilai plafon remedial maksimal **70,0 (B)**. Dokumen SDD terbaik diarsipkan sebagai artefak *handoff* resmi untuk diimplementasikan pada proyek pengujian/konstruksi di `STI-309 Rekayasa Perangkat Lunak`.
