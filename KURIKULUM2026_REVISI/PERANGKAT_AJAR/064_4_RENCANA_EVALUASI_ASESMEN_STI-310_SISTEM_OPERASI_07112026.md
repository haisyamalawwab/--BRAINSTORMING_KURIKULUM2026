# 064_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-310 — SISTEM OPERASI (*Operating Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI310` · **Bobot:** 3 SKS Teori · **Semester:** 3  
**Klaster Asesmen MK (Dok 018):** Klaster 3 (`K-3`) — Infrastruktur, Jaringan, Keamanan & Sistem Operasi  
**CPL Dibebankan:** `CPL-07` (`P3` = **50%**) & `CPL-11` (`KK3` = **50%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Sesuai **Dokumen 008, 018,** dan **043**, mata kuliah `STI-310 Sistem Operasi` (3 SKS Teori) menerapkan skema bobot baku MK Teori (`20% / 30% / 20% / 30%`) yang memetakan ketiga CPMK dan keenam Sub-CPMK secara seimbang ke `CPL-07` (50%) dan `CPL-11` (50%):
* **Tugas 1 (Pekan 4 — 20%)** mengukur `CPMK-1` (`Sub-CPMK-1.1` → `CPL-07`).
* **UTS (Pekan 8 — 30%)** mengukur `CPMK-1` (`Sub-CPMK-1.2`: **15%** → `CPL-07`) dan `CPMK-3` (`Sub-CPMK-3.1`: **15%** → `CPL-07`).
* **Tugas 2 (Pekan 12 — 20%)** mengukur `CPMK-2` (`Sub-CPMK-2.1` → `CPL-11`).
* **UAS (Pekan 16 — 30%)** mengukur `CPMK-2` (`Sub-CPMK-2.2`: **15%** → `CPL-11`) dan `CPMK-3` (`Sub-CPMK-3.1 & 3.2`: **15%** → `CPL-11`).
* **Kepatuhan IKU 7 ($\ge 55\%$ untuk Klaster `K-3` Dok 018):** `Tugas 1 (20% — Case-Based CPU Scheduling Evaluation) + Tugas 2 (20% — Case-Based Linux Server Configuration) + UAS (30% — Project-Based Containerized Server & Quantitative OS Workload Evaluation)` = **70%** *(persis selaras dengan angka kepatuhan IKU 7 Dokumen 004 untuk `STI-310` = 70%)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-07`**<br>(`P3` — 50%)<br>*Level: R* | **`CPMK-1`**<br>(C4) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus berparameter NIM: Analisis & simulasi penjadwalan CPU (*FCFS, SJF/SRTF, Priority, RR*) + kuis 20' | **RTM-1 (Tugas 1)** + Kuis Verifikasi + Rubrik Analitik T1 | Sumatif | 20% | **35%** |
| | | `Sub-CPMK-1.2` | Mg 8 | Ujian tertulis analitis: Perbaikan *race condition* (*Mutex/Semaphore*) & **Banker's Algorithm** *deadlock* | **Naskah UTS Bagian A** + Rubrik Analitik UTS | Sumatif | 15% | |
| **`CPL-07`**<br>(`P3` — 50%)<br>*Level: R* | **`CPMK-3`**<br>(C5 — *Bagian I*) | `Sub-CPMK-3.1` | Mg 8 | Ujian tertulis kuantitatif: Translasi **Paging/Segmentation**, EAT dengan TLB, & **FIFO/OPT/LRU** | **Naskah UTS Bagian B** + Rubrik Analitik UTS | Sumatif | 15% | **30%** *(15% UTS + 15% UAS)* |
| **`CPL-11`**<br>(`KK3` — 50%)<br>*Level: R* | **`CPMK-2`**<br>(C3) | `Sub-CPMK-2.1` | Mg 12 | Penugasan praktis mandiri VM Linux: Skrip **Bash CLI**, matriks **Permission POSIX**, & unit **`systemd`** + verifikasi 20' | **RTM-2 (Tugas 2)** + Verifikasi Terminal + Rubrik T2 | Sumatif | 20% | **35%** |
| | | `Sub-CPMK-2.2` | Mg 16 | Proyek & sidang terminal: Konfigurasi kontainerisasi dasar **Docker** (`Dockerfile` non-root, `cgroups`, *volumes*) | **Bundel Proyek UAS Bagian A** & Demo Terminal + Rubrik UAS | Sumatif | 15% | |
| **`CPL-11`**<br>(`KK3` — 50%)<br>*Level: R* | **`CPMK-3`**<br>(C5 — *Bagian II*) | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | Mg 16 | Proyek & sidang terminal: Evaluasi kuantitatif beban kerja **Memori Virtual** & **Sistem Berkas** nyata (`vmstat, iostat, fio`) | **Laporan Benchmark UAS Bagian B** & Ujian Individu + Rubrik UAS | Sumatif | 15% | *(tergabung pada 30% `CPMK-3`)* |
| **TOTAL** | **3 CPMK** | **6 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/30/20/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Analisis Algoritma Penjadwalan Prosesor)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Kuis Verifikasi **Pekan 4** · Bobot **20%** (`CPMK-1` / `Sub-CPMK-1.1` → `CPL-07`).
* **Objek & Batasan Pengerjaan Individu:**
  1. Diberikan tabel antrean 7 proses pada sistem *multi-tasking* dengan waktu kedatangan (*arrival time*), *CPU burst*, dan prioritas yang dimodifikasi oleh 2 digit terakhir NIM.
  2. Mahasiswa menyusun *Gantt Chart* presisi dan menghitung *Waiting Time*, *Turnaround Time*, *Response Time*, serta *Context Switch count* untuk **FCFS, SJF, SRTF, Priority (+ Aging),** dan **Round Robin** ($q = 2\text{ ms}$ vs $q = 6\text{ ms}$), dapat divalidasi dengan skrip simulator pendek buatan sendiri, lalu merumuskan analisis rekomendasi kebijakan penjadwalan terbaik.
  3. Mengikuti kuis verifikasi 20 menit tanpa alat bantu di kelas Pekan 4.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Sinkronisasi, Deadlock, & Memori Virtual)
* **Format & Bobot:** Ujian Tertulis Analitis-Kuantitatif Luring Terjadwal (*Closed-Book*, **150 menit**) · Bobot **30%** (`CPL-07`).
* **Rincian Soal:**
  1. **Bagian A (`CPMK-1` / `Sub-CPMK-1.2` — 50% skor UTS = 15% MK):** (a) Mendiagnosis cacat *race condition / deadlock* pada potongan pseudokode multi-thread dan memperbaikinya menggunakan **Mutex / Semaphore**; (b) Mengeksekusi **Banker's Algorithm** atas sistem 5 proses × 4 tipe sumber daya untuk membuktikan status aman/tidak aman dan mengevaluasi permintaan sumber daya baru.
  2. **Bagian B (`CPMK-3` / `Sub-CPMK-3.1` — 50% skor UTS = 15% MK):** (a) Menghitung ukuran *Page Table*, menerjemahkan alamat logis ke fisik pada skema **Paging & Segmentation**, dan menghitung **Effective Access Time (EAT)** dengan TLB serta *Page Fault Rate*; (b) Mengevaluasi untai referensi 18 halaman dengan 3 & 4 bingkai menggunakan **FIFO, Optimal,** dan **LRU** serta menganalisis kondisi **Thrashing**.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Konfigurasi Lingkungan Linux Server)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Verifikasi **Pekan 12** · Bobot **20%** (`CPMK-2` / `Sub-CPMK-2.1` → `CPL-11`).
* **Objek & Batasan Pengerjaan Individu:**
  1. Mengonfigurasi lingkungan Ubuntu Server untuk skenario server perusahaan 3 divisi: struktur akun/grup, direktori bersama berizin **POSIX** ketat (`chmod` oktal, `SGID`, *Sticky Bit*, `umask`, dan ACL), serta pengamanan akses SSH dasar.
  2. Menulis skrip **Bash CLI** otomatis yang mengumpulkan ringkasan proses rakus memori/CPU, pemakaian disk, dan galat log ke berkas laporan harian.
  3. Membangun dan mengaktifkan layanan daemon aplikasi sederhana menggunakan berkas unit **`systemd`** kustom (`User=` non-root, `Restart=on-failure`) lengkap bukti tangkapan `systemctl status` dan `journalctl` beridentitas `hostname` NIM mahasiswa.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Kontainerisasi Docker & Evaluasi Kuantitatif Beban Kerja)
* **Format & Bobot:** Bobot **30%** (`CPL-11`), memadukan **Proyek & Laporan Eksperimen (50% nilai UAS)** + **Sidang Demonstrasi Terminal & Ujian Individu (50% nilai UAS, 150 menit)**:
  1. **Poros `CPMK-2` (`Sub-CPMK-2.2` — 50% skor UAS = 15% MK):** Mengemas layanan server aplikasi ke dalam kontainer **Docker** fungsional melalui `Dockerfile` berpraktik terbaik (eksekusi *non-root*, *layer* efisien), persistensi **Docker Volume**, dan pembatasan kuota memori/CPU `cgroups`.
  2. **Poros `CPMK-3` (`Sub-CPMK-3.1 & 3.2` — 50% skor UAS = 15% MK):** Melakukan pengujian beban nyata (*workload benchmarking* menggunakan `stress-ng` / `fio` / beban HTTP) dan mengevaluasi secara kuantitatif perilaku **Memori Virtual** (*RSS, minor/major page faults, swap activity* saat mendekati batas RAM `cgroups`) serta kinerja **Sistem Berkas** (*IOPS, sequential/random throughput, latency* antara direktori host `ext4`/`XFS`, *Docker Volume*, dan *container writable layer*).

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-310}}$)
$$NA_{\text{STI-310}} = 0,20\,S_{\text{Tugas 1}} + 0,15\,S_{\text{UTS-A}} + 0,15\,S_{\text{UTS-B}} + 0,20\,S_{\text{Tugas 2}} + 0,15\,S_{\text{UAS-A}} + 0,15\,S_{\text{UAS-B}}$$

### 4.2 Rumus Skor per CPMK & Disaggregasi Multi-CPL (Dokumen 004 & 008)
* $\text{Skor}_{\text{CPMK-1}} = \dfrac{0,20\,S_{\text{Tugas 1}} + 0,15\,S_{\text{UTS-A}}}{0,35}$ · $\text{Skor}_{\text{CPMK-2}} = \dfrac{0,20\,S_{\text{Tugas 2}} + 0,15\,S_{\text{UAS-A}}}{0,35}$ · $\text{Skor}_{\text{CPMK-3}} = \dfrac{0,15\,S_{\text{UTS-B}} + 0,15\,S_{\text{UAS-B}}}{0,30}$
* **Ketercapaian `CPL-07` (`P3` — bobot 50% MK dari `Tugas 1` [20%] + `UTS` [30%]):**
  $$\text{Score}_{\text{CPL-07, STI-310}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,30\,S_{\text{UTS}}(i)}{0,50} = 0,40\,S_{\text{Tugas 1}}(i) + 0,60\,S_{\text{UTS}}(i)$$
* **Ketercapaian `CPL-11` (`KK3` — bobot 50% MK dari `Tugas 2` [20%] + `UAS` [30%]):**
  $$\text{Score}_{\text{CPL-11, STI-310}}(i) = \frac{0,20\,S_{\text{Tugas 2}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,50} = 0,40\,S_{\text{Tugas 2}}(i) + 0,60\,S_{\text{UAS}}(i)$$

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**. Mahasiswa dengan skor CPMK $< 65,0$ mengikuti maksimal 1 kali remedial terfokus pada bagian CPMK yang belum tuntas dengan plafon nilai maksimal **70,0 (B)**.
