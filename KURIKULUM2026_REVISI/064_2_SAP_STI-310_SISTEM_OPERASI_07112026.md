# 064_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-310 — SISTEM OPERASI (*Operating Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI310` · **Bobot:** 3 SKS Teori (`TM 150'`, `PT 180'`, `BM 180'`) · **Semester:** 3  
**Prasyarat:** `STI-103` Organisasi dan Arsitektur Komputer · **CPL:** `CPL-07` (`P3` = 50%) & `CPL-11` (`KK3` = 50%) [Level `R`]  
**Klaster Rubrik:** `K-3` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu `STI-310` |
|---|---|
| **Struktur Waktu per Sesi** | **Pendahuluan `20'` · Kegiatan Inti `110'` · Penutup & Refleksi `20'`** (Total Tatap Muka = `150 menit`), diikuti `PT 180'` dan `BM 180'`. |
| **Fokus Keilmuan (*In-Scope*)** | Tiga pilar klasik OSTEP (*Virtualization of CPU & Memory, Concurrency & Deadlock, File System Persistence*) dipadukan langsung dengan keterampilan administrasi **Linux Server** (*Bash CLI, POSIX Permissions, systemd*) dan kontainerisasi dasar **Docker** beserta *benchmarking* kuantitatif. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** mengulang gerbang logika & siklus instruksi mikroprosesor (`STI-103`), dilarang membahas *routing* IP/VLAN (`STI-312`), dan dilarang melebar ke penyediaan *Cloud VPC* (`STI-417`) ataupun klaster **Kubernetes** multi-node (`STB-601`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Perkuliahan | Metode Utama | Waktu TM | Evaluasi |
|:---:|:---:|---|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Peran OS, *Kernel vs User Mode*, Interupsi, & *System Calls* | Kuliah Interaktif & Demo `strace` | 150' | Formatif |
| **2** | `Sub-CPMK-1.1` | Manajemen Proses (*PCB, Context Switch, IPC*) & *Multithreading* | Ceramah & Analisis Kasus | 150' | Formatif |
| **3** | `Sub-CPMK-1.1` | Algoritma Penjadwalan CPU (*FCFS, SJF/SRTF, Priority, Round Robin*) | *Case-Based Problem Solving* | 150' | Formatif |
| **4** | `Sub-CPMK-1.2` | *Race Condition*, *Critical Section*, **Mutex**, & **Semaphore** + Verifikasi T1 | *Problem-Solving* + T1 | 150' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-1.2` | Masalah Sinkronisasi Klasik, 4 Kondisi **Deadlock**, & **Banker's Algorithm** | *Problem-Solving Class* | 150' | Formatif |
| **6** | `Sub-CPMK-3.1` | Alokasi Memori Fisik, **Paging**, *Page Table / TLB*, & **Segmentation** | Ceramah & Latihan Kuantitatif | 150' | Formatif |
| **7** | `Sub-CPMK-3.1` | **Virtual Memory**: *Page Fault*, **FIFO / Optimal / LRU**, *Thrashing*, & Klinik UTS | *Problem-Solving* & Klinik | 150' | Formatif |
| **8** | `CPMK-1 & 3` | **Ujian Tengah Semester (UTS):** Sinkronisasi/*Deadlock* & Memori Virtual | Ujian Tertulis Kuantitatif | 150' | **UTS (30%)** |
| **9** | `Sub-CPMK-3.2` | Arsitektur **Sistem Berkas** (*Inode, Journaling ext4/XFS*), Penjadwalan Disk, & RAID | *Case-Based Learning* | 150' | Formatif |
| **10** | `Sub-CPMK-2.1` | Administrasi **Linux**: FHS, **Bash CLI**, *Pipes*, `grep/awk/sed`, & *Shell Scripting* | *Hands-on Lecture* | 150' | Formatif |
| **11** | `Sub-CPMK-2.1` | Manajemen Akun, **Permission POSIX** (`chmod/umask/ACL`), & Layanan **`systemd`** | *Problem-Based Configuration* | 150' | Formatif |
| **12** | `Sub-CPMK-2.1` | Keamanan Tingkat OS (*SSH Hardening, PAM, ulimit, Audit Log*) + Verifikasi T2 | Kuliah *Hardening* + T2 | 150' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-2.2` | *Virtualization* vs *Containerization* (*Linux Namespaces & cgroups*) & **Docker** Dasar | Kuliah & Demo Kontainer | 150' | Formatif |
| **14** | `Sub-CPMK-2.2` | Penyusunan **`Dockerfile`** Aman (*Non-Root*), *OverlayFS*, & **Docker Volumes** | *Case-Based Configuration* | 150' | Formatif |
| **15** | `Sub-CPMK-3.1, 3.2` | Evaluasi Kuantitatif Beban Kerja Memori Virtual & Sistem Berkas (`vmstat, iostat, fio`) | Presentasi & Klinik Pra-UAS | 150' | Formatif |
| **16** | `CPMK-2 & 3` | **Evaluasi Akhir Semester (UAS):** Demo Linux/Docker & Evaluasi Kinerja OS | Sidang Terminal & Evaluasi | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN

### PERTEMUAN 1 — Peran Sistem Operasi, *Kernel vs User Space*, & *System Calls*
* **Sub-CPMK:** `Sub-CPMK-1.1` (Pengantar, C2→C4) · **Media:** Salindia Bab 1, Terminal Linux Ubuntu (`uname -a`, `strace`), LMS Edlink.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menyambungkan kembali konsep *Interrupt* dan *Privilege Ring* dari mata kuliah prasyarat `STI-103 Organisasi dan Arsitektur Komputer` menuju fungsi sistem operasi sebagai pengelola sumber daya (*resource allocator*) dan lapisan abstraksi perangkat keras.
  - **Kegiatan Inti (110'):** Menguraikan pemisahan **User Mode vs Kernel Mode**, alur eksekusi *Trap / System Call* (`open, read, write, fork, execve`), serta perbandingan arsitektur *Monolithic Modular Kernel* (Linux) vs *Microkernel* vs *Hybrid Kernel*. Mendemonstrasikan perintah `strace ls` secara langsung agar mahasiswa melihat ratusan *system call* nyata yang bekerja di balik satu perintah sederhana.
  - **Penutup (20'):** Menugaskan instalasi VM Ubuntu Server 24.04 LTS / WSL2 di perangkat masing-masing untuk latihan mandiri semester.
* **PT (`180'`) & BM (`180'`):** Menyiapkan lingkungan Ubuntu Linux dan mengamati keluaran `lscpu`, `free -h`, serta `/proc/cpuinfo`.

### PERTEMUAN 2 — Manajemen Proses (*PCB, Context Switch, IPC*) & *Multithreading*
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Media:** Diagram Siklus Hidup 5-Status Proses, Terminal Linux (`ps`, `pstree`, `top`).
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Bagaimana laptop dengan 4 inti CPU sanggup menjalankan 250 proses secara tampak bersamaan?
  - **Kegiatan Inti (110'):** Membedah anatomi proses di memori (*Text, Data, Heap, Stack*), struktur **Process Control Block (PCB)**, transisi 5 status proses, biaya murni (*pure overhead*) saat **Context Switch**, mekanisme **Inter-Process Communication (IPC: *Shared Memory vs Message Passing*)**, serta perbedaan mendasar antara penciptaan proses terpisah (`fork`) dan **Threads** dalam satu proses yang berbagi ruang alamat.
  - **Penutup (20'):** Kuis cepat membedakan proses *Zombie* vs *Orphan* pada Linux.
* **PT (`180'`) & BM (`180'`):** Menganalisis model konkurensi *multi-process* vs *multi-threaded* vs *event-loop* pada layanan server modern.

### PERTEMUAN 3 — Algoritma Penjadwalan Prosesor (*FCFS, SJF/SRTF, Priority, Round Robin*)
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Media:** Papan Tulis *Gantt Chart*, Lembar Kasus Penjadwalan.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Membedakan pola siklus *CPU Burst* dan *I/O Burst* serta menjelaskan mengapa pemilihan algoritma penjadwalan menentukan responsivitas server.
  - **Kegiatan Inti (110'):** Melatih analisis kuantitatif 5 algoritma penjadwalan CPU: **First-Come First-Served (FCFS)** dan jebakan *Convoy Effect*, **Shortest-Job-First (SJF)** non-preemptif dan **Shortest-Remaining-Time-First (SRTF)** preemptif, **Priority Scheduling** (masalah *Starvation* dan solusi **Aging**), **Round Robin (RR)** (aturan emas pemilihan *Time Quantum* $q$ dibanding waktu *Context Switch*), serta pengenalan *Multilevel Feedback Queue* (MLFQ) dan *Linux CFS*. Merilis resmi **Tugas 1 (RTM-1)**.
  - **Penutup (20'):** Memeriksa hasil perhitungan AWT dan ATAT latihan kelas.
* **PT (`180'`) & BM (`180'`):** Menyelesaikan studi kasus perbandingan kuantitatif algoritma penjadwalan CPU berparameter NIM (**Tugas 1**).

### PERTEMUAN 4 — Sinkronisasi Proses (*Race Condition, Mutex, Semaphore*) + Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Media:** Contoh Kode Konkuren Python/C, LMS Edlink.
* **Skenario (`25' / 105' / 20'`):**
  - **Pendahuluan (25'):** Melaksanakan kuis verifikasi tertulis 20 menit atas pengumpulan **Tugas 1 (`Sub-CPMK-1.1`)**.
  - **Kegiatan Inti (105'):** Mendemonstrasikan dua *thread* yang menambah variabel saldo `counter++` sebanyak 1.000.000 kali tetapi hasilnya selalu meleset acak (**Race Condition** akibat instruksi mesin tidak atomik!). Menguraikan 3 syarat mutlak solusi **Critical Section** (*Mutual Exclusion, Progress, Bounded Waiting*), instruksi perangkat keras atomik (`compare_and_swap`), kunci **Mutex**, serta operasi atomik `wait(S)` / `signal(S)` pada **Counting & Binary Semaphore** lengkap penerapannya pada kasus *Bounded-Buffer (Producer–Consumer)*.
  - **Penutup (20'):** Menekankan bahaya pembalikan urutan `wait()` yang memicu penguncian abadi pekan depan.
* **PT (`180'`) & BM (`180'`):** Menelusuri jejak eksekusi *semaphore* pada skenario *Producer–Consumer*.

### PERTEMUAN 5 — Masalah Sinkronisasi Klasik & Penanganan **Deadlock** (*Banker's Algorithm*)
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] · **Media:** Diagram *Resource-Allocation Graph*, Tabel Matriks Dijkstra.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Mengilustrasikan kebuntuan lalu lintas perempatan 4 arah dan masalah klasik *Dining Philosophers*.
  - **Kegiatan Inti (110'):** Menguraikan 4 kondisi perlu & cukup terjadinya **Deadlock** (Coffman: *Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait*), deteksi siklus pada **Resource-Allocation Graph (RAG)**, strategi pencegahan (pengurutan penomoran kunci), serta pelatihan tuntas **Banker's Algorithm** (*Safety Algorithm* & *Resource-Request Algorithm* menggunakan matriks `Allocation`, `Max`, `Need`, dan vektor `Available`).
  - **Penutup (20'):** Mengulas mengapa sistem operasi umum kerap memadukan pencegahan tingkat aplikasi dengan deteksi-pemulihan.
* **PT (`180'`) & BM (`180'`):** Mengerjakan 3 soal lengkap *Banker's Algorithm* dan *Resource-Allocation Graph*.

### PERTEMUAN 6 — Manajemen Memori Utama, **Paging**, *TLB*, & **Segmentation**
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4→C5] · **Media:** Bagan Translasi Alamat MMU, Kalkulator Heksadesimal.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Mengapa proses tidak boleh diizinkan menulis langsung ke alamat fisik RAM sesuka hatinya?
  - **Kegiatan Inti (110'):** Membandingkan alokasi bersebelahan (*First-Fit, Best-Fit, Worst-Fit* beserta masalah *External vs Internal Fragmentation*), membedah arsitektur **Paging** (*Page Number $p$ + Page Offset $d$* $\rightarrow$ *Frame Number $f$ + Offset $d$*), struktur *Hierarchical / Hashed Page Table*, akselerasi perangkat keras **Translation Lookaside Buffer (TLB)** beserta rumus perhitungan **Effective Access Time (EAT)**, serta konsep **Segmentation**.
  - **Penutup (20'):** Latihan kilat menghitung EAT saat *TLB hit ratio* berubah dari 80% menjadi 98%.
* **PT (`180'`) & BM (`180'`):** Menyelesaikan lembar latihan translasi alamat logis-ke-fisik dan ukuran tabel halaman.

### PERTEMUAN 7 — **Virtual Memory**: *Demand Paging*, **FIFO / Optimal / LRU**, *Thrashing*, & Klinik UTS
* **Sub-CPMK:** `Sub-CPMK-3.1` [C5] · **Media:** Tabel Simulasi Bingkai Halaman, LMS Edlink.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Bagaimana sebuah permainan atau basis data berukuran 24 GB dapat tetap berjalan di mesin dengan RAM fisik 16 GB?
  - **Kegiatan Inti (110'):** Menguraikan mekanisme **Demand Paging** dan biaya mahal penanganan **Page Fault** ke penyimpanan sekunder, melatih evaluasi kuantitatif algoritma penggantian halaman **FIFO** (beserta pembuktian *Belady's Anomaly*), **Optimal (OPT)** sebagai tolok ukur teoretis, dan **Least Recently Used (LRU)**, serta mendiagnosis fenomena **Thrashing** menggunakan *Working-Set Model*, ditutup klinik persiapan UTS.
  - **Penutup (20'):** Menyampaikan kisi-kisi resmi **UTS Pekan 8 (`CPMK-1` 15% + `CPMK-3` 15% = 30%)**.
* **PT (`180'`) & BM (`180'`):** Persiapan mandiri menghadapi UTS atas materi Pekan 4–7.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-1`** (`Sub-CPMK-1.2`: 15% MK) & **`CPMK-3`** (`Sub-CPMK-3.1`: 15% MK) · **Total Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Ujian tertulis analitis-kuantitatif luring terjadwal (*closed-book*) menguji analisis sinkronisasi *mutex/semaphore*, *Resource-Allocation Graph*, & **Banker's Algorithm**, serta evaluasi kuantitatif skema **Paging/TLB**, EAT, dan algoritma penggantian halaman **FIFO/OPT/LRU**.

### PERTEMUAN 9 — Arsitektur **Sistem Berkas**, Penjadwalan I/O Disk, & **RAID**
* **Sub-CPMK:** `Sub-CPMK-3.2` [C5] · **Media:** Diagram Struktur *Inode* `ext4`, Perbandingan `ext4` vs `XFS` vs `ZFS`.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Membahas umpan balik hasil UTS dan membuka pilar ketiga OSTEP (*Persistence*): apa yang terjadi di dalam sistem berkas ketika listrik server mati mendadak tepat saat menulis transaksi?
  - **Kegiatan Inti (110'):** Mengevaluasi metode alokasi blok berkas (*Contiguous, Linked, Indexed / Unix Inode* dengan *direct, single/double/triple indirect blocks*), mekanisme ketahanan *crash* melalui **Journaling (`ext4`, `XFS`)** dan *Copy-on-Write*, algoritma penjadwalan antrean I/O (*FCFS, SSTF, SCAN, C-SCAN*) vs antrean paralel **NVMe SSD**, serta evaluasi kuantitatif redundansi/kecepatan **RAID 0, 1, 5, 6, & 10**.
  - **Penutup (20'):** Studi kasus singkat memilih kombinasi sistem berkas + level RAID untuk server basis data produksi.
* **PT (`180'`) & BM (`180'`):** Mengeksplorasi `df -Th`, `lsblk`, dan nomor *inode* (`ls -li`, `stat`) pada VM Ubuntu Linux masing-masing.

### PERTEMUAN 10 — Administrasi **Linux Server**: FHS, **Bash CLI**, *Pipes*, & *Shell Scripting*
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Media:** Terminal Ubuntu Server LTS, Proyektor.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Mengapa lebih dari 90% server aplikasi dunia berjalan di atas Linux tanpa antarmuka grafis (*headless CLI*)?
  - **Kegiatan Inti (110'):** Mempraktikkan secara terarah *Filesystem Hierarchy Standard* (`/etc`, `/var/log`, `/proc`, `/sys`, `/srv`), pengalihan arus standar (`stdin, stdout, stderr`, `|`, `>`, `>>`, `2>&1`), penyaringan log menggunakan `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`, serta penulisan skrip otomasi **Bash** (`#!/usr/bin/env bash`, `set -euo pipefail`, argumen, kondisional `[ ]`, perulangan, dan penjadwalan `cron` / *systemd timer*). Merilis resmi **Tugas 2 (RTM-2)**.
  - **Penutup (20'):** Memeriksa eksekusi skrip pemantau pemakaian disk karya mahasiswa.
* **PT (`180'`) & BM (`180'`):** Menyusun skrip otomasi audit kesehatan & pencadangan server Linux untuk **Tugas 2**.

### PERTEMUAN 11 — Manajemen Pengguna, **Permission POSIX**, & Layanan Daemon **`systemd`**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Media:** Terminal Ubuntu Server LTS, Templat Unit `systemd`.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menampilkan dosa fatal pemula server: menjalankan perintah `chmod -R 777 /var/www` dan menjalankan aplikasi web sebagai `root`!
  - **Kegiatan Inti (110'):** Melatih manajemen akun & grup (`useradd`, `usermod`, `/etc/passwd`, `/etc/group`), perhitungan presisi **Permission POSIX** oktal & simbolik (`chmod`, `chown`, `chgrp`, `umask`), bit khusus (`SUID`, `SGID` untuk pewarisan grup direktori bersama, dan *Sticky Bit* `+t`), `setfacl`/`getfacl`, serta pembuatan layanan latar belakang kustom menggunakan **`systemd`** (`User=`, `WorkingDirectory=`, `ExecStart=`, `Restart=on-failure`, `systemctl enable --now`, dan pelacakan log `journalctl -u`).
  - **Penutup (20'):** Menguji ketahanan unit `systemd` dengan mematikan paksa PID proses (`kill -9`) dan membuktikan `systemd` menghidupkannya kembali dalam hitungan detik.
* **PT (`180'`) & BM (`180'`):** Menyelesaikan seluruh spesifikasi konfigurasi Linux Server pada **Tugas 2**.

### PERTEMUAN 12 — Keamanan Dasar Tingkat Sistem Operasi (*OS Hardening*) + Verifikasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] + **Evaluasi Sumatif Tugas 2 (`CPMK-2`, 20%)** · **Media:** Terminal Ubuntu Server, LMS Edlink.
* **Skenario (`25' / 105' / 20'`):**
  - **Pendahuluan (25'):** Melaksanakan kuis/verifikasi perintah langsung 20 menit atas pengumpulan **Tugas 2 (`Sub-CPMK-2.1`)**.
  - **Kegiatan Inti (105'):** Mengajarkan praktik penguatan keamanan tingkat sistem operasi (*OS-Level Hardening* selaras `BK-IT01`): pembatasan hak `sudo`, pengamanan akses SSH berbasis kunci asimetris (`PermitRootLogin no`, `PasswordAuthentication no`), pembatasan sumber daya proses (`ulimit` / `/etc/security/limits.conf` mencegah *fork bomb*), penyaringan port host dasar (`ufw`), serta pembacaan jejak serangan *brute-force* pada `/var/log/auth.log`.
  - **Penutup (20'):** Memperkenalkan proyek akhir UAS kepada tim mahasiswa.
* **PT (`180'`) & BM (`180'`):** Memasang *Docker Engine* resmi pada VM Ubuntu Server yang telah diamankan.

### PERTEMUAN 13 — *Virtualization* vs *Containerization* (*Namespaces & cgroups*) & **Docker** Dasar
* **Sub-CPMK:** `Sub-CPMK-2.2` [C3] · **Media:** Terminal Linux + Docker Engine, Bagan Arsitektur Kernel.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Mengapa kontainer Docker bisa menyala dalam 0,3 detik dan hanya memakan belasan MB RAM, sedangkan Mesin Virtual penuh membutuhkan puluhan detik dan ratusan MB?
  - **Kegiatan Inti (110'):** Membongkar fakta penting sistem operasi: *"Container is just an isolated Linux process!"* — membedah 2 fitur inti kernel Linux pembentuk kontainer, yaitu **Namespaces** (`pid, net, mnt, uts, ipc, user` — membatasi apa yang bisa *dilihat* proses) dan **Control Groups (`cgroups` v2)** (membatasi berapa banyak CPU, RAM, & I/O yang boleh *dipakai* proses), lalu mempraktikkan manajemen siklus hidup kontainer **Docker** (`pull, run, exec, logs, inspect, stats`) lengkap pembatasan `--memory` dan `--cpus`.
  - **Penutup (20'):** Membuktikan bahwa proses di dalam kontainer yang melihat dirinya ber-PID `1` sesungguhnya tampak sebagai PID biasa di terminal host Linux.
* **PT (`180'`) & BM (`180'`):** Bereksperimen menjalankan kontainer server web/aplikasi dengan variasi kuota memori `cgroups`.

### PERTEMUAN 14 — Penyusunan **`Dockerfile`**, *OverlayFS*, & **Docker Volumes** untuk Server Aplikasi
* **Sub-CPMK:** `Sub-CPMK-2.2` [C3] · **Media:** Terminal Docker, Contoh Aplikasi Layanan Ringan.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Apa yang terjadi pada berkas basis data di dalam kontainer apabila kontainer dihapus dan dibuat ulang tanpa konfigurasi *Volume*?
  - **Kegiatan Inti (110'):** Mengajarkan arsitektur lapisan berkas *Copy-on-Write* (**OverlayFS**) pada citra kontainer, praktik terbaik menulis **`Dockerfile`** produksi (*minimal base image* seperti `alpine`/`slim`, optimalisasi urutan *layer cache*, berkas `.dockerignore`, serta wajib menambahkan instruksi `USER nonroot`!), pengelolaan persistensi sistem berkas melalui **Docker Named Volumes & Bind Mounts**, serta pemetaan port jaringan *bridge* lokal *(menjaga guardrail: orkestrasi multi-host Kubernetes diserahkan ke `STB-601`)*.
  - **Penutup (20'):** Meninjau `Dockerfile` rancangan dua tim mahasiswa.
* **PT (`180'`) & BM (`180'`):** Menyelesaikan kontainerisasi layanan aplikasi proyek UAS di atas server Linux.

### PERTEMUAN 15 — Evaluasi Kuantitatif Kinerja Memori Virtual & Sistem Berkas pada Beban Nyata
* **Sub-CPMK:** `Sub-CPMK-3.1` & `3.2` [C5] · **Media:** Utilitas `vmstat`, `iostat`, `pidstat`, `free`, `stress-ng`, `fio`, `docker stats`.
* **Skenario (`20' / 110' / 20'`):**
  - **Pendahuluan (20'):** Menyatukan teori kuantitatif paruh pertama semester dengan infrastruktur Linux/Docker paruh kedua: bagaimana mengukur *page fault*, *thrashing*, dan *bottleneck* I/O berkas secara nyata?
  - **Kegiatan Inti (110'):** Mendemonstrasikan metode *benchmarking* dan evaluasi kuantitatif kinerja sistem operasi menggunakan kakas standar industri (`vmstat 1` untuk kolom `si/so` *swap* & `cs` *context switch*, `/proc/<pid>/status` untuk *minor/major page faults* & RSS, `iostat -xz 1` dan `fio` untuk IOPS, *throughput* MB/s, & `await` latensi disk), dilanjutkan klinik peninjauan draf laporan eksperimen kelompok pra-UAS.
  - **Penutup (20'):** Menjelaskan tata tertib sidang demonstrasi langsung dan ujian evaluasi **UAS Pekan 16 (`CPMK-2` 15% + `CPMK-3` 15% = 30%)**.
* **PT (`180'`) & BM (`180'`):** Finalisasi skrip konfigurasi Linux/Docker dan laporan evaluasi kuantitatif kinerja memori & sistem berkas.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.2`: 15% MK) & **`CPMK-3`** (`Sub-CPMK-3.1 & 3.2`: 15% MK) · **Total Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Bundel Konfigurasi Server Linux/Docker & Laporan Evaluasi Kuantitatif Beban Kerja Memori/Berkas (50% nilai UAS)** dengan **Sidang Demonstrasi Langsung di Terminal & Ujian Evaluasi Individu (50% nilai UAS)** di mana setiap mahasiswa diuji kemampuannya mengoperasikan CLI/POSIX/`systemd`/Docker dan menafsirkan metrik kinerja memori virtual serta sistem berkas secara langsung.
