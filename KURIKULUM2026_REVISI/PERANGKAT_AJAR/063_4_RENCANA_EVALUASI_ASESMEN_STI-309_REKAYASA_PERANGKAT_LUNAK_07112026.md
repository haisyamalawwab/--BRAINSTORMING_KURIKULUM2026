# 063_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-309 — REKAYASA PERANGKAT LUNAK (*Software Engineering*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI309` · **Bobot:** 3 SKS Teori · **Semester:** 3  
**Klaster Asesmen MK (Dok 018):** Klaster 4 (`K-4`) — Sintesis, Rekayasa Sistem & Mutu Perangkat Lunak  
**CPL Dibebankan:** `CPL-08` (`P4` = **50%**) & `CPL-13` (`KK5` = **50%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras penuh dengan **Dokumen 008, 018, 043,** dan unit perintis `RPS_STI-309_Software_Engineering.md`, mata kuliah `STI-309 Rekayasa Perangkat Lunak` (3 SKS Teori) menerapkan pemetaan 1-ke-1 ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-08` / `P4`)** — *Case-Based Software Process Selection & Justification*.
* **UTS (Pekan 8 — 30%) → `CPMK-2` (`CPL-08` / `P4`)** — *Case-Method Exam: Modular Architecture, SOLID Refactoring, & GoF Patterns*.
* **Tugas 2 (Pekan 12 — 20%) → `CPMK-3` (`CPL-13` / `KK5`)** — *Case-Based White-Box ($V(G)$, Basis Path) & Black-Box (EP, BVA) Test Suite Design*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-13` / `KK5`)** — *Team-Based Automated Testing Repository, ISO/IEC 25010 Quality Evaluation Report & Individual Defense*.
* **Kepatuhan IKU 7 ($\ge 50\%$):** Komponen pemecahan kasus (`Tugas 1` 20% + studi kasus arsitektur/pengujian) dan proyek evaluasi mutu perangkat lunak mencapai **75%** *(persis selaras dengan tabel kepatuhan IKU 7 pada Dokumen 004 untuk `STI-309` = 75%)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-08`**<br>(`P4` — 50%)<br>*Level: R* | **`CPMK-1`**<br>(C4) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus mandiri: Pemilihan model proses (*Waterfall, V-Model, Scrum, Kanban*) pada 3 konteks proyek industri + kuis verifikasi 20' | **RTM-1 (Tugas 1)** Bagian A + Kuis Verifikasi + Rubrik T1 | Sumatif | 10% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Studi kasus mandiri: Matriks komparasi multi-kriteria & rancangan mekanisme Sprint/DoD/WIP/V-Mapping | **RTM-1 (Tugas 1)** Bagian B + Rubrik Analitik T1 | Sumatif | 10% | |
| **`CPL-08`**<br>(`P4` — 50%)<br>*Level: R* | **`CPMK-2`**<br>(C3) | `Sub-CPMK-2.1` | Mg 8 | Ujian tertulis studi kasus kode: Dekomposisi arsitektur modular (*low coupling*) & *refactoring* **SOLID** | **Naskah Soal UTS** (Soal 1 & 2) + Rubrik Analitik UTS | Sumatif | 18% | **30%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Ujian tertulis studi kasus kode: Deteksi *code smells* & penerapan **GoF Design Patterns** | **Naskah Soal UTS** (Soal 2 & 3) + Rubrik Analitik UTS | Sumatif | 12% | |
| **`CPL-13`**<br>(`KK5` — 50%)<br>*Level: R* | **`CPMK-3`**<br>(C4) | `Sub-CPMK-3.1` | Mg 12 | Penugasan spesifikasi uji: *Control Flow Graph*, **Cyclomatic Complexity $V(G)$**, & *Basis Path White-Box* + kuis 20' | **RTM-2 (Tugas 2)** Bagian White-Box + Rubrik T2 | Sumatif | 10% | **20%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Penugasan spesifikasi uji: **Equivalence Partitioning**, **BVA**, & *Decision Table Black-Box* | **RTM-2 (Tugas 2)** Bagian Black-Box + Rubrik T2 | Sumatif | 10% | |
| **`CPL-13`**<br>(`KK5` — 50%)<br>*Level: R* | **`CPMK-4`**<br>(C5) | `Sub-CPMK-4.1` | Mg 16 | Proyek audit mutu + sidang/ujian individu: Evaluasi kualitas objektif berstandar **ISO/IEC 25010** | **Laporan Audit ISO/IEC 25010** & Ujian UAS + Rubrik UAS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Proyek audit mutu + sidang/ujian individu: Rangkaian *Automated Unit & Integration Tests* (*TDD, Mocking, Coverage*) | **Repositori Git Test Suite** & Demo Individu UAS | Sumatif | 15% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (1-to-1 CPMK)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Pemilihan & Justifikasi Model Proses SDLC/Agile)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Kuis Verifikasi **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-08`).
* **Objek & Batasan Pengerjaan Individu:**
  1. Diberikan 3 profil proyek industri nyata yang sangat berbeda sifat risiko, regulasi, stabilitas kebutuhan, dan ukuran timnya.
  2. Mahasiswa menyusun matriks perbandingan objektif antara **Waterfall, V-Model, Scrum,** dan **Kanban** pada minimal 6 dimensi evaluasi, memilih model terbaik untuk masing-masing proyek dengan justifikasi ilmiah tajam, serta merancang struktur siklus kerjanya (*V-Model Verification Matrix*, aturan *Sprint & Definition of Done*, atau batas *Kanban WIP*).
  3. Mengikuti kuis konfirmasi tertulis 20 menit di kelas Pekan 4.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Arsitektur Modular, SOLID, & GoF)
* **Format & Bobot:** Ujian Tertulis Studi Kasus Luring Terjadwal (*Closed-Book*, **150 menit**) · Bobot **30%** (`CPMK-2` → `CPL-08`).
* **Rincian Soal:**
  1. **(30% — `Sub-CPMK-2.1`):** Analisis cacat *high coupling / low cohesion* pada sebuah diagram modul aplikasi monolitik yang mencampur logika tampilan, aturan bisnis, dan akses basis data, lalu rancang ulang arsitektur berlapisnya (*Layered/Clean Architecture*).
  2. **(40% — `Sub-CPMK-2.1 & 2.2`):** Bedah kode sumber kelas berorientasi objek yang memiliki *Code Smells* dan melanggar prinsip **SRP, OCP,** serta **DIP**; tuliskan rancangan kelas/antarmuka dan kode hasil *refactoring*-nya.
  3. **(30% — `Sub-CPMK-2.2`):** Rancang solusi arsitektur subsistem yang membutuhkan pergantian algoritma dinamis dan notifikasi lintas-layanan menggunakan pasangan **GoF Design Patterns** (*Strategy* & *Observer* / *Factory* & *Adapter*) lengkap diagram kelas dan kerangka kodenya.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Perancangan Skenario Pengujian White-Box & Black-Box)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Kuis Verifikasi **Pekan 12** · Bobot **20%** (`CPMK-3` → `CPL-13`).
* **Objek & Batasan Pengerjaan Individu (Berparameter NIM):**
  1. **Bagian A — White-Box Testing (`Sub-CPMK-3.1`):** Diberikan 2 fungsi logika bisnis bersarang ($\pm 30\text{–}40\text{ baris}$) dengan konstanta ambang batas sesuai NIM; mahasiswa wajib menggambar **Control Flow Graph (CFG)** bernomor simpul, menghitung **Cyclomatic Complexity $V(G)$** melalui 3 rumus McCabe, mendaftar seluruh **Independent Basis Paths**, dan menyusun tabel kasus uji yang menjamin 100% *Branch Coverage*.
  2. **Bagian B — Black-Box Testing (`Sub-CPMK-3.2`):** Berdasarkan spesifikasi aturan sistem (tanpa melihat kode), mahasiswa wajib menyusun partisi **Equivalence Partitioning (EP)**, titik batas **Boundary Value Analysis (BVA)** 3-nilai, dan **Decision Table Test Cases** lengkap berformat standar (`TC-ID, Input, Precondition, Expected Output`).

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Otomasi Pengujian & Audit ISO/IEC 25010)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-13`), terdiri atas:
  1. **Komponen A — Repositori Git Proyek Mutu & Otomasi Pengujian Tim (50% nilai UAS):** Mengambil satu subsistem perangkat lunak nyata/spesifikasi SDD, me-*refactor* kodenya agar mematuhi **SOLID**, membangun rangkaian **Automated Unit & Integration Tests** (`Pytest`/`Jest`/`JUnit` dengan *Mocking* dan *Branch Coverage* $\ge 80\%$ terotomasi di *GitHub Actions*), serta menyusun **Laporan Evaluasi Kualitas Perangkat Lunak Berstandar ISO/IEC 25010**.
  2. **Komponen B — Sidang Demonstrasi Pengujian & Ujian Verifikasi Individu (50% nilai UAS, 150 menit):** Penguji memeriksa kontribusi *commit* Git masing-masing anggota, meminta eksekusi langsung *test suite* dan modifikasi 1 kasus uji di tempat, serta menguji kemampuan evaluasi objektif metrik ISO/IEC 25010 secara individu.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-309}}$)
$$NA_{\text{STI-309}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Selaras Pilot `RPS_STI-309` & Dok 004/008)
1. **Ketercapaian `CPL-08` (`P4` — total bobot 50% MK dari `CPMK-1` [20%] + `CPMK-2` [30%]):**
   $$\text{Score}_{\text{CPL-08, STI-309}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,30\,S_{\text{UTS}}(i)}{0,50} = 0,40\,S_{\text{Tugas 1}}(i) + 0,60\,S_{\text{UTS}}(i)$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,50 = 1,50\text{ SKS}$).*
2. **Ketercapaian `CPL-13` (`KK5` — total bobot 50% MK dari `CPMK-3` [20%] + `CPMK-4` [30%]):**
   $$\text{Score}_{\text{CPL-13, STI-309}}(i) = \frac{0,20\,S_{\text{Tugas 2}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,50} = 0,40\,S_{\text{Tugas 2}}(i) + 0,60\,S_{\text{UAS}}(i)$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,50 = 1,50\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**.
* **Protokol Verifikasi Git & Remedial:** Kontribusi kode & *unit test* tanpa jejak *commit* Git individu tidak diakui nilainya; mahasiswa dengan skor CPMK $< 65,0$ mengikuti 1 kali remedial terfokus pada CPMK terkait dengan nilai maksimal pasca-remedial **70,0 (B)**.
