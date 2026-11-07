# 064_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-310 — SISTEM OPERASI (*Operating Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI310`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Sistem Operasi / *Operating Systems* |
| **Kode Mata Kuliah** | `STI-310` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Infrastruktur TI, Jaringan & Keamanan Siber (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS Teori** (`T = 3, P = 0`) — Tatap Muka `3×50' = 150'`, Penugasan Terstruktur `3×60' = 180'`, Belajar Mandiri `3×60' = 180'` per pekan |
| **Semester / Tahun Akademik** | Semester 3 (Ganjil) — Tahap Penguatan Fondasi Infrastruktur Komputasi (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `STI-103` Organisasi dan Arsitektur Komputer |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Bersinergi dengan `STI-312` Jaringan Komputer; menjadi fondasi bagi `STI-417` Komputasi Awan, `STI-519` Keamanan Informasi Lanjut, `STI-521` Internet untuk Segala (IoT), & `STB-601` Arsitektur Cloud & DevOps |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-07` (`P3` = **50%**) dan `CPL-11` (`KK3` = **50%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 3 (`K-3`)** — Infrastruktur, Jaringan, Keamanan & Sistem Operasi (Bobot MK Teori: Tugas 1 `20%` · UTS `30%` · Tugas 2 `20%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Infrastruktur TI, Cloud & Keamanan Siber |
| **Koordinator RMK** | Ir. Bambang Suprapto, M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-07`** (`P3`) | Pengetahuan | Menguasai arsitektur komputer, sistem operasi, jaringan komputer modern, komputasi awan (*Cloud*), prinsip keamanan siber, serta integrasi sistem berbasis sensor/IoT. | **R** (*Reinforce*) | **50%** |
| **`CPL-11`** (`KK3`) | Keterampilan Khusus | Mampu merancang, mengkonfigurasi, mengamankan, dan mengelola infrastruktur jaringan, layanan komputasi awan (*Cloud/DevOps*), sistem tertanam/IoT, serta pertahanan siber proaktif. | **R** (*Reinforce*) | **50%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **menganalisis** algoritma penjadwalan prosesor (*FCFS, SJF, Round Robin, Priority*) dan mekanisme penanganan *deadlock* (*semaphore, mutex*) (*B*) pada studi kasus sistem operasi *multi-tasking* (*C*) secara akurat (*D*). | **C4** (*Analyze*) | `CPL-07` (`P3`) | **Tugas 1 (20%) + ½ UTS (15%) = 35%** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **mengonfigurasi** lingkungan sistem operasi Linux (*Bash CLI, manajemen permission POSIX, systemd service*) dan kontainerisasi dasar (**Docker**) (*B*) untuk kebutuhan server aplikasi (*C*) secara fungsional (*D*). | **C3** (*Apply*) | `CPL-11` (`KK3`) | **Tugas 2 (20%) + ½ UAS (15%) = 35%** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **mengevaluasi** kinerja manajemen memori virtual (*paging, segmentation*) dan sistem berkas (*B*) pada skenario beban kerja komputasi nyata (*C*) secara kuantitatif (*D*). | **C5** (*Evaluate*) | `CPL-07` (`P3`) & `CPL-11` (`KK3`) | **½ UTS (15%) + ½ UAS (15%) = 30%** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Menganalisis algoritma penjadwalan prosesor (*FCFS, SJF, RR, Priority*) pada *multi-tasking*. | `CPMK-1` | **C4** | Mg 1–4 |
| **`Sub-CPMK-1.2`** | Menganalisis mekanisme sinkronisasi dan penanganan *deadlock* (*semaphore, mutex*). | `CPMK-1` | **C4** | Mg 5–6 |
| **`Sub-CPMK-2.1`** | Mengonfigurasi lingkungan Linux (*Bash CLI, permission POSIX, systemd*) untuk server. | `CPMK-2` | **C3** | Mg 10–12 |
| **`Sub-CPMK-2.2`** | Mengonfigurasi kontainerisasi dasar (**Docker**) untuk kebutuhan server aplikasi. | `CPMK-2` | **C3** | Mg 13–14 |
| **`Sub-CPMK-3.1`** | Mengevaluasi kinerja manajemen memori virtual (*paging, segmentation*) secara kuantitatif. | `CPMK-3` | **C5** | Mg 7 & 15 |
| **`Sub-CPMK-3.2`** | Mengevaluasi kinerja sistem berkas pada skenario beban kerja komputasi nyata. | `CPMK-3` | **C5** | Mg 9 & 15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-2 & CPMK-3 (Sintesis Akhir): Kontainerisasi Dasar Docker & Evaluasi Beban Kerja Memori/Berkas Nyata (C3 & C5) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-2.2: Namespaces/cgroups, Dockerfile, Volumes | Sub-CPMK-3.1 & 3.2: Benchmark Memori Virtual & I/O Berkas Server)
      │
[CPMK-2 (Tahap I) & CPMK-3 (Sistem Berkas): Sistem Berkas I/O & Konfigurasi Linux Server (C5 & C3) — Mg 9–12 (Tugas 2 20%)]
      ▲  (Sub-CPMK-3.2: Inode, Journaling ext4/XFS, Disk Scheduling | Sub-CPMK-2.1: Bash CLI, POSIX Permission, systemd Service)
      │
[CPMK-1 (Tahap II) & CPMK-3 (Memori Virtual): Sinkronisasi, Deadlock, & Memori Virtual (C4 & C5) — Mg 5–8 (UTS 30%)]
      ▲  (Sub-CPMK-1.2: Race Condition, Mutex, Semaphore, Banker's Algorithm | Sub-CPMK-3.1: Paging, Segmentation, FIFO/OPT/LRU)
      │
[CPMK-1 (Tahap I): Arsitektur Kernel, Manajemen Proses/Thread, & Algoritma Penjadwalan CPU (C4) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: System Calls, PCB, Context Switch, FCFS, SJF/SRTF, Priority, Round Robin)
      ▲
[Fondasi Prasyarat: STI-103 Organisasi dan Arsitektur Komputer (CPU, Register, Hierarki Cache/RAM, Interrupts)]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-07`** (`P3`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | **15%** | — | — | **35%** | **`CPL-07` = 50%** |
| **`CPL-07`** (`P3`) | **`CPMK-3`** *(Memori Virtual)* | `Sub-CPMK-3.1` | — | **15%** | — | — | **15%** | *(20% + 15% + 15%)* |
| **`CPL-11`** (`KK3`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | — | **20%** | **15%** | **35%** | **`CPL-11` = 50%** |
| **`CPL-11`** (`KK3`) | **`CPMK-3`** *(Benchmark Memori & Berkas)* | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | — | **15%** | **15%** | *(20% + 15% + 15%)* |
| **Total** | **3 CPMK** | **6 Sub-CPMK** | **20%** | **30%** | **20%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 55\%$ untuk Klaster `K-3` Dok 018):** `Tugas 1 (20% — Case-Based Multi-Tasking CPU Scheduling Simulation & Analysis) + Tugas 2 (20% — Case-Based Linux Server Administration: Bash, POSIX, systemd) + UAS (30% — Project-Based Dockerized Application Server & Quantitative Virtual Memory/Filesystem Workload Evaluation)` = **70%** *(persis selaras dengan angka tabel IKU 7 Dokumen 004 untuk `STI-310` = 70%)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-310 Sistem Operasi` (3 SKS Teori) menjembatani perangkat keras komputer (`STI-103`) dengan perangkat lunak layanan aplikasi modern. Mahasiswa mengkaji arsitektur kernel (*monolithic, microkernel, hybrid*), *system calls*, manajemen siklus hidup proses dan *thread*, analisis kuantitatif algoritma penjadwalan CPU (*FCFS, SJF/SRTF, Priority, Round Robin*), sinkronisasi konkurensi (*mutex, semaphore, monitor*) dan penanganan *deadlock* (*Banker's Algorithm*), manajemen memori utama dan **memori virtual** (*paging, segmentation, TLB, page replacement FIFO/Optimal/LRU, thrashing*), arsitektur sistem berkas (*inode, journaling ext4/XFS*) dan penjadwalan I/O disk, serta keterampilan esensial administrasi **Linux Server** (*Bash CLI scripting, manajemen permission POSIX & ACL, pengelolaan daemon `systemd`*), keamanan dasar tingkat OS, dan kontainerisasi dasar **Docker** beserta evaluasi kuantitatif beban kerja server nyata.

* **🟢 IN-SCOPE (Wajib Diajarkan):** Kernel & *system call*, proses/*thread*, penjadwalan CPU (*FCFS, SJF, RR, Priority*), sinkronisasi (*mutex, semaphore*) & *deadlock*, memori virtual (*paging, segmentation, page replacement*), sistem berkas & I/O disk, administrasi **Linux** (*Bash CLI, POSIX permission, systemd*), konsep *virtualization vs containerization* (*Linux namespaces & cgroups*), kontainerisasi dasar **Docker** satu layanan, dan evaluasi metrik kinerja memori/berkas.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. Dilarang mengulang gerbang logika digital, representasi biner komplemen-2, maupun siklus *fetch-decode-execute* register mikroprosesor (sudah tuntas di **`STI-103 Organisasi dan Arsitektur Komputer`**).
  2. Dilarang membahas pengalamatan subnetting VLSM maupun konfigurasi *routing* OSPF/VLAN antar-switch (ranah ko-semester **`STI-312 Jaringan Komputer`**).
  3. Dilarang melebar ke penyediaan infrastruktur *Public Cloud* AWS/GCP IAM/VPC (ranah **`STI-417 Komputasi Awan`**) maupun orkestrasi klaster **Kubernetes** *multi-node* dan *enterprise CI/CD* (ranah **`STB-601 Arsitektur Cloud & DevOps`**).
* **🔄 HANDOFF ANCHOR:** Mengambil fondasi arsitektur CPU & memori dari `STI-103`, bersinergi dengan `STI-312 Jaringan Komputer`, dan menyerahkan kesiapan administrasi Linux & kontainer dasar ke **`STI-417 Komputasi Awan`**, **`STI-519 Keamanan Informasi Lanjut`**, **`STI-521 Internet untuk Segala (IoT)`**, serta **`STB-601 Arsitektur Cloud & DevOps`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS03` (*IT Infrastructure*), `BK-IT01` (*Cybersecurity Principles*), & `BK-IT05` (*System Administration and Maintenance*).

**Pustaka Utama:**
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley. *(Osc / Dinosaur Book)*
2. Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). *Operating Systems: Three Easy Pieces (OSTEP)*. Arpaci-Dusseau Books. *(Virtualization, Concurrency, Persistence)*
3. Tanenbaum, A. S., & Bos, H. (2022). *Modern Operating Systems* (5th ed.). Pearson.

**Pustaka Pendukung:**
4. Nemeth, E., Snyder, G., Hein, T. R., Whaley, B., & Mackin, D. (2017). *UNIX and Linux System Administration Handbook* (5th ed.). Addison-Wesley.
5. Shotts, W. (2019). *The Linux Command Line: A Complete Introduction* (2nd ed.). No Starch Press; serta Dokumentasi Resmi *Docker Engine* & *Linux Kernel Documentation*.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Pengantar):** Menguraikan peran sistem operasi, mode *Kernel vs User Space*, interupsi, dan *System Calls* [C2→C4] | 1.1.1 Ketepatan menjelaskan transisi *User Mode ↔ Kernel Mode* saat pemanggilan *System Call* (`fork, exec, read, write`).<br>1.1.2 Ketepatan membandingkan arsitektur *Monolithic Kernel* (Linux), *Microkernel*, dan *Hybrid Kernel*. | **Kriteria:** Kuis diagnostik formatif.<br>**Teknik:** Tanya-jawab penelusuran *system call* dengan `strace` sederhana di layar kelas. | **Kuliah Interaktif & Demo `strace` Kernel**<br>`[TM: 3×50' = 150']`<br>Instalasi lingkungan Ubuntu Server VM / WSL2 pada laptop mahasiswa:<br>`[PT: 180']` · `[BM: 180']` | Kontrak belajar, unduh panduan VM/WSL2 Ubuntu LTS di LMS Edlink. | Peran Sistem Operasi, *Dual-Mode Operation*, *System Calls*, & Struktur Kernel Modern `[1] Bab 1–2; [2] Pengantar` | — |
| **2** | **`Sub-CPMK-1.1`:** Menganalisis konsep **Proses**, *Process Control Block* (PCB), *Context Switch*, Komunikasi Antar-Proses (IPC), dan **Multithreading** [C4] | 1.1.3 Ketepatan menganalisis diagram 5-status proses (*New, Ready, Running, Waiting, Terminated*) dan biaya *overhead Context Switch*.<br>1.1.4 Ketepatan membandingkan proses berat (*heavyweight process*) vs *Thread* berbagi ruang alamat (*shared memory vs message passing*). | **Kriteria:** Ketepatan analisis status proses & memori *thread*.<br>**Teknik:** Latihan pelacakan pohon proses `pstree` & status proses. | **Ceramah Interaktif & Analisis Kasus Proses**<br>`[TM: 3×50' = 150']`<br>Analisis perbandingan *multi-process* vs *multi-thread* web server:<br>`[PT: 180']` · `[BM: 180']` | Kuis pemahaman *PCB, Context Switch,* & *Threads* di LMS Edlink. | Manajemen Proses (*Process State, PCB, Context Switching, IPC*) & Konsep *Threads / Concurrency* `[1] Bab 3–4; [2] Bagian I` | — |
| **3** | **`Sub-CPMK-1.1`:** Menganalisis dan membandingkan algoritma **Penjadwalan CPU** (*FCFS, SJF, SRTF, Priority, Round Robin, Multilevel Feedback Queue*) [C4] | 1.1.5 Ketepatan menyusun *Gantt Chart* eksekusi CPU dan menghitung secara presisi **Average Waiting Time (AWT)**, **Average Turnaround Time (ATAT)**, **Response Time**, dan **Throughput**.<br>1.1.6 Ketepatan menganalisis fenomena *Convoy Effect*, *Starvation* (+ solusi *Aging*), dan pengaruh ukuran *Time Quantum* $q$ pada *Round Robin*. | **Kriteria:** Akurasi 100% *Gantt Chart* & metrik waktu.<br>**Teknik:** *Problem-solving* perhitungan 5 algoritma atas antrean proses *burst-time* bervariasi. | **Case-Based Problem-Solving Penjadwalan CPU**<br>`[TM: 3×50' = 150']`<br>Pengerjaan studi kasus analisis & simulasi penjadwalan CPU untuk **Tugas 1**:<br>`[PT: 180']` · `[BM: 180']` | Rilis resmi instruksi **Tugas 1 (RTM-1)** berparameter NIM di LMS Edlink. | Kriteria & Algoritma Penjadwalan Prosesor: *FCFS*, *SJF / SRTF*, *Priority Scheduling + Aging*, *Round Robin*, & *MLFQ* `[1] Bab 5; [2] Bab 7–8` | — |
| **4** | **`Sub-CPMK-1.2` (Bagian I):** Menganalisis masalah *Race Condition*, *Critical Section*, dan mekanisme sinkronisasi (**Mutex Locks & Semaphores**) [C4]<br>*(+ Evaluasi Tugas 1 atas `Sub-CPMK-1.1`)* | 1.2.1 Ketepatan membuktikan terjadinya *Race Condition* pada variabel bersama.<br>1.2.2 Ketepatan memverifikasi 3 syarat solusi *Critical Section* (*Mutual Exclusion, Progress, Bounded Waiting*) menggunakan **Mutex** dan **Counting/Binary Semaphore**. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-3`)**.<br>**Teknik:** Pengumpulan Studi Kasus Penjadwalan CPU + Kuis Verifikasi Kelas 20'. | **Problem-Solving Sinkronisasi & Verifikasi Tugas 1**<br>`[TM: 3×50' = 150']`<br>Analisis solusi bebas *race condition* pada masalah *Bounded-Buffer (Producer–Consumer)*:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Masalah *Race Condition*, *Critical Section*, *Hardware Atomic Instructions*, **Mutex**, & **Semaphore** `[1] Bab 6–7; [2] Bab 26–31` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-1.2` (Bagian II):** Menganalisis masalah sinkronisasi klasik dan mekanisme penanganan **Deadlock** (*Resource-Allocation Graph* & **Banker's Algorithm**) [C4] | 1.2.3 Ketepatan menganalisis masalah klasik *Readers–Writers* & *Dining Philosophers*.<br>1.2.4 Ketepatan mengidentifikasi 4 syarat mutlak Coffman (*Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait*), mendeteksi siklus pada *Resource-Allocation Graph*, dan menentukan *Safe Sequence* menggunakan **Banker's Algorithm**. | **Kriteria:** Ketepatan matriks `Need = Max - Allocation` & barisan aman *Banker's Algorithm*.<br>**Teknik:** Latihan langkah demi langkah *Banker's Algorithm* di kelas. | **Problem-Solving Class *Deadlock & Banker's Algorithm***<br>`[TM: 3×50' = 150']`<br>Latihan deteksi dan penghindaran *deadlock* multi-instans sumber daya:<br>`[PT: 180']` · `[BM: 180']` | Kuis perhitungan matriks `Available/Allocation/Need` di LMS Edlink. | Masalah Sinkronisasi Klasik, 4 Kondisi Coffman, Pencegahan/Penghindaran/Deteksi **Deadlock**, & **Banker's Algorithm** `[1] Bab 8; [2] Bab 32` | — |
| **6** | **`Sub-CPMK-3.1` (Bagian I):** Mengevaluasi alokasi memori utama (*Contiguous Allocation, Fragmentation*), **Paging**, *Page Table / TLB*, dan **Segmentation** [C4→C5] | 3.1.1 Ketepatan membandingkan *Internal vs External Fragmentation* pada *First-Fit, Best-Fit, Worst-Fit*.<br>3.1.2 Ketepatan menerjemahkan alamat logis `(p, d)` ke alamat fisik `(f, d)` pada skema **Paging** serta menghitung **Effective Access Time (EAT)** dengan rasio *hit Translation Lookaside Buffer* (TLB). | **Kriteria:** Akurasi translasi alamat biner/heksadesimal & rumus EAT.<br>**Teknik:** Pemecahan soal perhitungan tabel halaman dan EAT dengan TLB. | **Ceramah Analitis & Latihan Kuantitatif Memori**<br>`[TM: 3×50' = 150']`<br>Latihan perhitungan *Page Table Size*, translasi alamat, & EAT:<br>`[PT: 180']` · `[BM: 180']` | Lembar kerja latihan *Paging, TLB,* & *Segmentation* di LMS Edlink. | Manajemen Memori Fisik, *Fragmentation*, Skema **Paging**, *Translation Lookaside Buffer* (TLB), & **Segmentation** `[1] Bab 9; [2] Bab 15–20` | — |
| **7** | **`Sub-CPMK-3.1` (Bagian II):** Mengevaluasi kinerja **Virtual Memory**: *Demand Paging*, *Page Fault*, algoritma *Page Replacement* (**FIFO, Optimal, LRU**), & *Thrashing* [C5] | 3.1.3 Ketepatan menghitung jumlah *Page Fault* dan *Hit Ratio* untuk untai acuan halaman menggunakan **FIFO** (termasuk anomali Belady), **Optimal**, dan **Least Recently Used (LRU)**.<br>3.1.4 Ketepatan mengevaluasi dampak *Page Fault Rate* terhadap penurunan drastis EAT dan fenomena **Thrashing** (*Working-Set Model*). | **Kriteria:** Akurasi tabel bingkai halaman & ketajaman evaluasi kuantitatif EAT.<br>**Teknik:** Simulasi perbandingan *FIFO vs OPT vs LRU* & klinik persiapan UTS. | **Problem-Solving *Virtual Memory* & Klinik Pra-UTS**<br>`[TM: 3×50' = 150']`<br>Persiapan komprehensif menghadapi UTS Pekan 8:<br>`[PT: 180']` · `[BM: 180']` | Simulasi soal UTS (*Deadlock + Virtual Memory*) di LMS Edlink. | **Virtual Memory**: *Demand Paging*, Penanganan *Page Fault*, Algoritma **FIFO, Optimal, & LRU**, serta *Thrashing* `[1] Bab 10; [2] Bab 21–22` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-1` (`Sub-CPMK-1.2`: 15%) & `CPMK-3` (`Sub-CPMK-3.1`: 15%) [C4/C5]** | Ketepatan menganalisis sinkronisasi *semaphore/mutex* dan **Banker's Algorithm** penanganan *deadlock* (`CPMK-1`), serta mengevaluasi secara kuantitatif translasi **Paging/TLB**, *Effective Access Time*, dan algoritma *Page Replacement* **FIFO/OPT/LRU** (`CPMK-3`). | **Kriteria:** **Rubrik Analitik UTS (`K-3`)**.<br>**Teknik:** Ujian tertulis analitis-kuantitatif luring terjadwal (*Closed-Book*). | **Ujian Tertulis Luring Terjadwal**<br>`[150 menit]` | Pengarsipan nilai UTS terpilah per `CPMK-1` dan `CPMK-3` pada portal OBE. | Materi Sinkronisasi, *Deadlock*, **Paging/Segmentation**, & **Virtual Memory** (Pekan 4–7) | **30%**<br>*(UTS: 15% `CPMK-1` + 15% `CPMK-3`)* |
| **9** | **`Sub-CPMK-3.2`:** Mengevaluasi arsitektur **Sistem Berkas** (*Inode, Allocation Methods, Journaling ext4/XFS*) & algoritma penjadwalan I/O penyimpanan (*FCFS, SSTF, SCAN, C-SCAN*, & RAID) [C5] | 3.2.1 Ketepatan membandingkan metode alokasi blok (*Contiguous, Linked, Indexed/Inode*) serta mekanisme ketahanan *crash* pada *Journaling File System* (`ext4`, `XFS`).<br>3.2.2 Ketepatan menghitung total pergerakan kepala disk (*FCFS, SSTF, SCAN, C-SCAN*), karakteristik IOPS SSD NVMe, dan *trade-off* redundansi/kecepatan **RAID 0, 1, 5, 10**. | **Kriteria:** Ketepatan perhitungan I/O & evaluasi pemilihan sistem berkas/RAID.<br>**Teknik:** Studi kasus pemilihan arsitektur penyimpanan server basis data vs server arsip. | **Case-Based Learning Sistem Berkas & Penyimpanan**<br>`[TM: 3×50' = 150']`<br>Analisis perbandingan *throughput*/ketahanan `ext4` vs `XFS` dan level RAID:<br>`[PT: 180']` · `[BM: 180']` | Kuis perhitungan penjadwalan I/O & pemilihan level RAID di LMS Edlink. | Arsitektur Sistem Berkas (*Directory, Inode, Journaling*), Penjadwalan Penyimpanan Sekunder, NVMe SSD, & **RAID** `[1] Bab 11–14; [2] Bagian III` | — |
| **10** | **`Sub-CPMK-2.1` (Bagian I):** Mengonfigurasi lingkungan **Linux Server** menggunakan **Bash CLI**, *Pipes/Redirection*, pemrosesan teks (`grep, awk, sed`), & skrip otomasi administrasi [C3] | 2.1.1 Ketepatan menavigasi *Filesystem Hierarchy Standard* (`/etc, /var/log, /proc, /opt, /srv`) dan merangkai *pipeline* perintah Unix.<br>2.1.2 Ketepatan menulis skrip **Bash** fungsional (variabel, percabangan, *loop*, kode keluar, `cron`/penjadwalan) untuk pencadangan dan pemantauan kesehatan server. | **Kriteria:** Skrip Bash berjalan bersih tanpa galat di Ubuntu Server.<br>**Teknik:** Demo langsung & latihan penulisan skrip otomasi CLI di kelas. | **Hands-on Lecture *Linux Bash CLI & Scripting***<br>`[TM: 3×50' = 150']`<br>Penulisan skrip otomasi administrasi sistem untuk **Tugas 2**:<br>`[PT: 180']` · `[BM: 180']` | Rilis resmi instruksi **Tugas 2 (RTM-2)** di LMS Edlink. | Standar Hierarki Berkas Linux (FHS), *Streams & Pipes*, Pemrosesan Log (`grep, sed, awk`), & **Bash Shell Scripting** `[4]; [5]` | — |
| **11** | **`Sub-CPMK-2.1` (Bagian II):** Mengonfigurasi manajemen pengguna, grup, **Permission POSIX** (`rwx` oktal/simbolik, `SUID/SGID/Sticky Bit`, `umask`, ACL), & layanan daemon **`systemd`** [C3] | 2.1.3 Ketepatan menerapkan prinsip *Least Privilege* melalui manajemen *user/group*, matriks izin **POSIX** (`chmod, chown, umask`, *Sticky Bit* pada direktori kolaborasi), dan `sudoers`.<br>2.1.4 Ketepatan menulis berkas unit kustom `/etc/systemd/system/*.service` (lengkap fitur `Restart=on-failure`, pembatasan user non-root, & inspeksi `journalctl`). | **Kriteria:** Layanan `systemd` aktif otomatis & izin berkas ketat sesuai spesifikasi.<br>**Teknik:** Simulasi audit keamanan izin direktori & pembuatan unit `systemd`. | **Problem-Based Configuration *POSIX & systemd***<br>`[TM: 3×50' = 150']`<br>Finalisasi bundel konfigurasi Linux Server untuk **Tugas 2**:<br>`[PT: 180']` · `[BM: 180']` | Templat berkas unit `systemd` aman & daftar periksa izin POSIX di LMS Edlink. | Manajemen Identitas Linux, **POSIX Permissions**, *Special Bits*, *Access Control Lists* (ACL), & Manajemen Layanan **`systemd` / `journalctl`** `[4] Bab 4–7` | — |
| **12** | **`Sub-CPMK-2.1` (Penguatan Keamanan OS):** Mengonfigurasi penguatan dasar keamanan sistem operasi (*SSH Key-Only Hardening, UFW Host Firewall, Resource Limits `ulimit`, & Log Auditing*) [C3]<br>*(+ Evaluasi Tugas 2 atas `Sub-CPMK-2.1`)* | 2.1.5 Ketepatan mengamankan akses administrasi jarak jauh (*disable root password SSH*), membatasi port lokal host, dan memeriksa log otentikasi `/var/log/auth.log`. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-3`)**.<br>**Teknik:** Pengumpulan Dokumentasi & Skrip Konfigurasi Linux Server + Verifikasi Langsung/Kuis 20'. | **Kuliah *OS Hardening* & Verifikasi Tugas 2**<br>`[TM: 3×50' = 150']`<br>Persiapan lingkungan host Linux untuk kontainerisasi Docker:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 2 (`CPMK-2`)** di LMS Edlink. | Prinsip Keamanan Tingkat Sistem Operasi (*Principle of Least Privilege, PAM, SSH Key Auth, Host Firewall Dasar, & System Auditing*) `[1] Bab 16; [4]` | **20%**<br>*(Tugas 2 — `CPMK-2`)* |
| **13** | **`Sub-CPMK-2.2` (Bagian I):** Menganalisis perbedaan *Hypervisor Virtualization* vs *OS-Level Containerization* (*Linux Namespaces & cgroups*) dan mengonfigurasi **Docker** dasar [C3] | 2.2.1 Ketepatan membedakan arsitektur *Hypervisor Type-1/Type-2* dengan kontainer berbagi kernel host berbasis **Linux Namespaces** (isolasi PID, mount, net) & **Control Groups (`cgroups`)** (batas RAM/CPU).<br>2.2.2 Ketepatan menjalankan siklus hidup kontainer **Docker** dan membatasi kuota memori/CPU (`--memory`, `--cpus`). | **Kriteria:** Kontainer berjalan terisolasi dengan batas *cgroups* terverifikasi.<br>**Teknik:** Demonstrasi inspeksi `docker stats` & ruang nama proses di host Linux. | **Interactive Lecture & Demo *Containers & Docker***<br>`[TM: 3×50' = 150']`<br>Eksperimen menjalankan dan membatasi sumber daya kontainer Docker:<br>`[PT: 180']` · `[BM: 180']` | Panduan instalasi *Docker Engine* pada Ubuntu VM di LMS Edlink. | *Virtual Machines* vs *Containers*, Mekanisme Kernel **Namespaces & cgroups**, & Dasar **Docker Engine** `[1] Bab 18; [5]` | — |
| **14** | **`Sub-CPMK-2.2` (Bagian II):** Merancang **`Dockerfile`** yang efisien (*layer caching, non-root user*), mengelola *Volumes* persistensi sistem berkas, & kontainer server aplikasi fungsional [C3] | 2.2.3 Ketepatan menulis `Dockerfile` bersih (*minimal base image, non-root execution*), memetakan *named volume / bind mount* untuk persistensi data, dan menjalankan server aplikasi secara fungsional *(tanpa melebar ke Kubernetes ranah `STB-601`)*. | **Kriteria:** Citra Docker terbangun ringan, berjalan sebagai *non-root*, dan data persisten saat kontainer dimulai ulang.<br>**Teknik:** Peninjauan `Dockerfile` proyek kelompok di kelas. | **Case-Based Configuration *Dockerfile & Volumes***<br>`[TM: 3×50' = 150']`<br>Kontainerisasi aplikasi uji proyek UAS di atas server Linux:<br>`[PT: 180']` · `[BM: 180']` | Contoh praktik terbaik `Dockerfile` aman di LMS Edlink. | Penyusunan **`Dockerfile`**, Arsitektur *UnionFS / OverlayFS Image Layers*, **Docker Volumes**, & Kontainer Server Aplikasi `[4]; [5]` | — |
| **15** | **`Sub-CPMK-3.1` & `3.2` (Sintesis Kuantitatif):** Mengevaluasi kinerja memori virtual (*RSS, page faults, swap*) dan I/O sistem berkas secara kuantitatif pada beban kerja server nyata (`vmstat, iostat, pidstat, fio/stress-ng`) [C5] | 3.1.5 & 3.2.3 Ketepatan mengukur, memvisualisasikan, dan mengevaluasi metrik penggunaan memori virtual (*minor/major page faults, swap in/out, cache hit*) serta IOPS/latensi sistem berkas antara eksekusi *native systemd* vs *Docker container* berkuota `cgroups`. | **Kriteria:** Kelengkapan data kuantitatif eksperimen & ketajaman analisis gejala *bottleneck/thrashing*.<br>**Teknik:** Presentasi draf hasil *benchmark* beban kerja & klinik pra-UAS. | **Presentasi Analisis Kuantitatif Kinerja OS & Klinik UAS**<br>`[TM: 3×50' = 150']`<br>Finalisasi bundel konfigurasi Linux/Docker & Laporan Evaluasi Kuantitatif Kinerja Memori/Berkas:<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan draf laporan proyek *OS Configuration & Workload Evaluation* di LMS Edlink. | Observabilitas & Evaluasi Kuantitatif Kinerja Sistem Operasi (`procfs`, `vmstat`, `iostat`, `free`, `docker stats`) pada Beban Kerja Nyata `[2]; [4]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-2` (`Sub-CPMK-2.2`: 15%) & `CPMK-3` (`Sub-CPMK-3.1 & 3.2`: 15%) [C3 & C5]** | Fungsionalitas konfigurasi lingkungan Linux & kontainerisasi dasar **Docker** (`CPMK-2` = 15% MK) serta ketajaman evaluasi kuantitatif kinerja manajemen memori virtual dan sistem berkas pada beban kerja komputasi nyata (`CPMK-3` = 15% MK). | **Kriteria:** **Rubrik Analitik UAS (`K-3`)**.<br>**Teknik:** Penilaian Bundel Konfigurasi Server Linux/Docker & Laporan Evaluasi Kuantitatif Beban Kerja (50% UAS) + Sidang Demo Langsung/Ujian Individu (50% UAS). | **Sidang Demonstrasi Server Kontainer & Evaluasi Kinerja OS**<br>`[150 menit]` | Pengarsipan artefak konfigurasi, laporan *benchmark*, & rekap nilai `CPL-07` dan `CPL-11` pada portal OBE. | Integrasi Konfigurasi Linux (`Bash, POSIX, systemd`), **Docker**, & Evaluasi Kuantitatif Kinerja Memori Virtual dan Sistem Berkas | **30%**<br>*(UAS: 15% `CPMK-2` + 15% `CPMK-3`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `Sub-CPMK-1.1` → `CPL-07` [C4])
* **Bentuk Instrumen:** Studi Kasus Analitis & Simulasi Penjadwalan Prosesor *Multi-Tasking* Berparameter NIM + Kuis Verifikasi Kelas 20 Menit: mahasiswa membandingkan kinerja **FCFS, SJF Non-Preemptive, SRTF (Preemptive SJF), Priority Scheduling (+ Aging),** dan **Round Robin** (pada 2 variasi nilai *Time Quantum* $q$) atas beban campuran proses *CPU-bound* dan *I/O-bound*, lengkap *Gantt Chart*, tabel **Waiting Time, Turnaround Time, Response Time**, serta rekomendasi kebijakan penjadwalan terbaik.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Akurasi *Gantt Chart* & penanganan *preemption/arrival time* = **35%**; (2) Presisi perhitungan AWT, ATAT, *Response Time*, & *Context Switch overhead* = **35%**; (3) Ketajaman analisis fenomena *Convoy Effect / Starvation / Quantum* & rekomendasi = **20%**; (4) Kerapian laporan & konsistensi kuis verifikasi = **10%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 30% · Mengukur `CPMK-1` [15%] & `CPMK-3` [15%] → `CPL-07` [C4/C5])
* **Bentuk Instrumen:** Ujian Tertulis Analitis-Kuantitatif Luring Terjadwal (*Closed-Book*, 150 menit):
  1. **Bagian A (`CPMK-1` / `Sub-CPMK-1.2` — 50% skor UTS = 15% MK):** Analisis *race condition* & perbaikan sinkronisasi kode konkuren menggunakan **Mutex/Semaphore**, ditambah pengujian **Banker's Algorithm** (*Safe/Unsafe State* & penentuan persetujuan permintaan sumber daya baru).
  2. **Bagian B (`CPMK-3` / `Sub-CPMK-3.1` — 50% skor UTS = 15% MK):** Evaluasi kuantitatif translasi alamat **Paging/Segmentation**, perhitungan **Effective Access Time (EAT)** bertingkat TLB + *Page Fault*, serta perbandingan jumlah *Page Fault* algoritma **FIFO, Optimal,** dan **LRU** beserta diagnosis gejala *Thrashing*.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 20% · Mengukur `CPMK-2` / `Sub-CPMK-2.1` → `CPL-11` [C3])
* **Bentuk Instrumen:** Penugasan Praktis Konfigurasi **Linux Server** Mandiri (di atas VM Ubuntu Server + verifikasi langsung/kuis 20 menit): (1) Menata struktur grup, akun non-root, dan **Permission POSIX** (`chmod`, `chown`, `umask`, *SGID/Sticky Bit*) untuk direktori kolaborasi multi-divisi; (2) Menulis skrip **Bash CLI** otomatis untuk rotasi/audit log dan pemantauan ambang memori/disk; (3) Mengonfigurasi layanan aplikasi latar belakang menggunakan berkas unit **`systemd`** kustom yang pulih otomatis saat *crash* (`Restart=on-failure`) dan terverifikasi lewat `systemctl status` & `journalctl`.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan & keamanan konfigurasi *user/group* serta **Permission POSIX** = **35%**; (2) Fungsionalitas & kebersihan skrip otomasi **Bash CLI** = **35%**; (3) Keandalan konfigurasi unit **`systemd`** & pengujian pemulihan layanan = **20%**; (4) Dokumentasi reproduksibel & verifikasi perintah di kelas = **10%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-2` [15%] & `CPMK-3` [15%] → `CPL-11` [C3 & C5])
* **Bentuk Instrumen:** **Proyek Kontainerisasi Aplikasi & Evaluasi Kuantitatif Beban Kerja Sistem Operasi** (50% nilai UAS: repositori konfigurasi Linux + `Dockerfile` non-root + *Docker Volume* + **Laporan Evaluasi Kuantitatif Kinerja Memori Virtual & Sistem Berkas** menggunakan data uji beban `stress-ng`/`fio`/`vmstat`/`iostat`) + **Sidang Demonstrasi Terminal Langsung & Ujian Individu** (50% nilai UAS, 150 menit).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Fungsionalitas & keamanan konfigurasi kontainer **Docker** (`Dockerfile`, `cgroups` limit, *volume* persisten — `Sub-CPMK-2.2`) = **40%**; (2) Ketajaman evaluasi kuantitatif kinerja **Memori Virtual** (*page faults, RSS, swap*) & **Sistem Berkas** (*IOPS, throughput, latency* — `Sub-CPMK-3.1 & 3.2`) = **40%**; (3) Penguasaan perintah langsung di terminal Linux/Docker saat sidang individu = **20%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Infrastruktur TI, Cloud & Keamanan Siber**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Ir. Bambang Suprapto, M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
