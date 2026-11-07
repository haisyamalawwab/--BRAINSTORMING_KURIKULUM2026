# 064_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-310 — SISTEM OPERASI (*Operating Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI310` · **Bobot:** 3 SKS Teori · **Semester:** 3  
**CPL:** `CPL-07` (`P3` = 50%) & `CPL-11` (`KK3` = 50%) [Level `R`] · **BoK:** `BK-IS03`, `BK-IT01`, `BK-IT05`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Sistem Operasi Modern: Penjadwalan Prosesor, Konkurensi, Memori Virtual, Sistem Berkas, Administrasi Linux Server, & Kontainerisasi Docker* |
| **Target Tebal Naskah** | 14 Bab Materi Inti + 2 Unit Evaluasi ($\pm 200\text{–}230\text{ halaman}$ A4 dilengkapi diagram kernel, tabel perhitungan *Gantt/Banker/Paging*, skrip Bash/`systemd`/`Dockerfile`, dan panduan *benchmark* kinerja OS) |
| **Pagar Pembatas Buku (*Guardrail*)** | Tidak mengulang gerbang logika & register mikroprosesor (`STI-103`), tidak membahas *routing* IP/VLAN (`STI-312`), dan tidak melebar ke *Cloud VPC* (`STI-417`) maupun orkestrasi klaster *Kubernetes* (`STB-601`). |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Proses, Thread, & Penjadwalan CPU** | **Bab 1** | Arsitektur Sistem Operasi, *User vs Kernel Mode*, & Mekanisme *System Calls* | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Abstraksi Proses (*PCB, Context Switch, IPC*) & Konkurensi *Multithreading* | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3** | Analisis Kuantitatif Algoritma Penjadwalan CPU (*FCFS, SJF, SRTF, Priority, RR*) | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Sinkronisasi, Deadlock, & Memori Virtual** | **Bab 4** | Masalah *Race Condition*, *Critical Section*, **Mutex**, & **Semaphore** | Mg 4 | `CPMK-1` | `Sub-CPMK-1.2` | UTS (15%) |
| | **Bab 5** | Masalah Sinkronisasi Klasik & Penanganan **Deadlock** (*Banker's Algorithm*) | Mg 5 | `CPMK-1` | `Sub-CPMK-1.2` | UTS (15%) |
| | **Bab 6** | Manajemen Memori Fisik, Skema **Paging**, Akselerasi **TLB**, & **Segmentation** | Mg 6 | `CPMK-3` | `Sub-CPMK-3.1` | UTS (15%) |
| | **Bab 7** | **Virtual Memory**: *Demand Paging*, **FIFO / Optimal / LRU**, & Diagnosis *Thrashing* | Mg 7 | `CPMK-3` | `Sub-CPMK-3.1` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Bank Soal Analitis-Kuantitatif Sinkronisasi, Deadlock, & Memori Virtual (UTS)* | *Mg 8* | *`CPMK-1, 3`* | *`1.2, 3.1`* | *UTS (30%)* |
| **Bagian III:<br>Sistem Berkas & Administrasi Linux Server** | **Bab 8** | Arsitektur **Sistem Berkas** (*Inode, Journaling ext4/XFS*), Penjadwalan I/O, & **RAID** | Mg 9 | `CPMK-3` | `Sub-CPMK-3.2` | UAS (15%) |
| | **Bab 9** | Standar Hierarki Berkas Linux, **Bash CLI**, *Pipes*, & Skrip Otomasi Administrasi | Mg 10 | `CPMK-2` | `Sub-CPMK-2.1` | Tugas 2 (20%) |
| | **Bab 10** | Manajemen Identitas, **Permission POSIX** (`chmod, umask, ACL`), & Daemon **`systemd`** | Mg 11 | `CPMK-2` | `Sub-CPMK-2.1` | **Tugas 2 (Mg 12)** |
| | **Bab 11** | Penguatan Keamanan Tingkat Sistem Operasi (*SSH Hardening, PAM, ulimit, Audit*) | Mg 12 | `CPMK-2` | `Sub-CPMK-2.1` | UAS (Pendukung) |
| **Bagian IV:<br>Kontainerisasi Docker & Evaluasi Beban Kerja** | **Bab 12** | *Hypervisor* vs Kontainer Berbasis Kernel (**Linux Namespaces & cgroups**) & **Docker** | Mg 13 | `CPMK-2` | `Sub-CPMK-2.2` | UAS (15%) |
| | **Bab 13** | Rekayasa **`Dockerfile`** Aman, *OverlayFS Image Layers*, & Persistensi *Volumes* | Mg 14 | `CPMK-2` | `Sub-CPMK-2.2` | UAS (15%) |
| | **Bab 14** | Evaluasi Kuantitatif Kinerja Memori Virtual & Sistem Berkas pada Beban Kerja Nyata | Mg 15 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Server Kontainer & Sidang Evaluasi Kinerja Sistem Operasi (UAS)* | *Mg 16* | *`CPMK-2, 3`* | *`2.2, 3.1, 3.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB

#### BAB 1: Arsitektur Sistem Operasi, *User vs Kernel Mode*, & Mekanisme *System Calls* (Pekan 1)
* **Sub-Pokok Bahasan:** Abstraksi sumber daya perangkat keras, *Dual-Mode Operation* & *Trap Interrupt*, klasifikasi *System Calls* POSIX, perbandingan *Monolithic Modular Kernel*, *Microkernel*, dan *Hybrid Kernel*, serta observasi `strace`.

#### BAB 2: Abstraksi Proses (*PCB, Context Switch, IPC*) & Konkurensi *Multithreading* (Pekan 2)
* **Sub-Pokok Bahasan:** Tata letak memori proses, **Process Control Block (PCB)**, diagram 5 status proses, anatomi **Context Switch**, *Shared Memory* vs *Message Passing*, serta model pemetaan *User-to-Kernel Threads*.

#### BAB 3: Analisis Kuantitatif Algoritma Penjadwalan CPU (*FCFS, SJF, SRTF, Priority, RR*) (Pekan 3)
* **Sub-Pokok Bahasan:** Metrik evaluasi penjadwalan (AWT, ATAT, *Response Time*, *Throughput*, utilisasi CPU), penyusunan *Gantt Chart* dan pembuktian karakteristik **FCFS**, **SJF**, **SRTF**, **Priority + Aging**, **Round Robin**, dan **MLFQ**.

#### BAB 4: Masalah *Race Condition*, *Critical Section*, Mutex, & Semaphore (Pekan 4)
* **Sub-Pokok Bahasan:** Bukti ketidakatomikan operasi konkuren, 3 syarat solusi *Critical Section*, dukungan perangkat keras atomik, penguncian **Mutex** (*spinlock vs sleeping lock*), serta **Semaphore** Dijkstra pada kasus *Producer–Consumer*.

#### BAB 5: Masalah Sinkronisasi Klasik & Penanganan Deadlock (*Banker's Algorithm*) (Pekan 5)
* **Sub-Pokok Bahasan:** *Readers–Writers* & *Dining Philosophers*, 4 kondisi Coffman, deteksi siklus **Resource-Allocation Graph**, strategi pencegahan *deadlock*, serta langkah lengkap **Banker's Algorithm**.

#### BAB 6: Manajemen Memori Fisik, Skema Paging, Akselerasi TLB, & Segmentation (Pekan 6)
* **Sub-Pokok Bahasan:** *Logical vs Physical Address Space*, *First/Best/Worst-Fit* & fragmentasi, pembagian *Frames & Pages*, translasi alamat biner/heksadesimal, *Multi-level Page Table*, perhitungan **Effective Access Time (EAT)** dengan **TLB**, dan **Segmentation**.

#### BAB 7: Virtual Memory: *Demand Paging*, FIFO / Optimal / LRU, & Diagnosis *Thrashing* (Pekan 7)
* **Sub-Pokok Bahasan:** *Lazy Swapper & Page Fault Trap*, evaluasi kuantitatif **FIFO** (*Belady's Anomaly*), **Optimal**, dan **LRU** (*Stack/Counter & Clock Second-Chance*), *Allocation of Frames*, serta pencegahan **Thrashing** berbasis *Working-Set Model*.

#### BAB 8: Arsitektur Sistem Berkas (*Inode, Journaling ext4/XFS*), Penjadwalan I/O, & RAID (Pekan 9)
* **Sub-Pokok Bahasan:** Struktur direktori & **Unix Inode**, alokasi *Contiguous / Linked / Indexed*, mekanisme pemulihan *crash* **Journaling** (`ext4`, `XFS`) & *Copy-on-Write*, algoritma penjadwalan antrean disk (*FCFS, SSTF, SCAN, C-SCAN*) vs NVMe, serta level **RAID**.

#### BAB 9: Standar Hierarki Berkas Linux, Bash CLI, *Pipes*, & Skrip Otomasi Administrasi (Pekan 10)
* **Sub-Pokok Bahasan:** Navigasi FHS Linux, *Standard Streams* & *Pipelines*, utilitas pemrosesan teks sistem (`grep, awk, sed, find`), serta penulisan skrip otomasi **Bash** tangguh dan terjadwal.

#### BAB 10: Manajemen Identitas, Permission POSIX (`chmod, umask, ACL`), & Daemon `systemd` (Pekan 11)
* **Sub-Pokok Bahasan:** Pengelolaan `/etc/passwd`, `/etc/shadow`, `/etc/group`, matriks izin **POSIX** (`rwx`, `SUID`, `SGID`, *Sticky Bit*, `umask`, POSIX ACL), serta perancangan berkas unit layanan **`systemd`** dan analisis `journalctl`.

#### BAB 11: Penguatan Keamanan Tingkat Sistem Operasi (*SSH Hardening, PAM, ulimit, Audit*) (Pekan 12)
* **Sub-Pokok Bahasan:** Prinsip *Least Privilege*, tata kelola `sudoers`, pengamanan otentikasi kunci publik SSH, pembatasan kuota proses `ulimit`, *host firewall* dasar, dan inspeksi log keamanan OS.

#### BAB 12: *Hypervisor* vs Kontainer Berbasis Kernel (Linux Namespaces & cgroups) & Docker (Pekan 13)
* **Sub-Pokok Bahasan:** Perbandingan arsitektur *Type-1/Type-2 Hypervisor* dengan isolasi tingkat kernel (**Namespaces** + **`cgroups` v2**), arsitektur *Docker Daemon / containerd*, dan manajemen siklus hidup kontainer dengan pembatasan sumber daya.

#### BAB 13: Rekayasa `Dockerfile` Aman, *OverlayFS Image Layers*, & Persistensi *Volumes* (Pekan 14)
* **Sub-Pokok Bahasan:** Cara kerja *Union / OverlayFS*, penyusunan **`Dockerfile`** ringan dan aman (*multi-stage*, eksekusi `USER` non-root), pengelolaan **Docker Volumes**, serta jaringan lokal kontainer server aplikasi.

#### BAB 14: Evaluasi Kuantitatif Kinerja Memori Virtual & Sistem Berkas pada Beban Kerja Nyata (Pekan 15)
* **Sub-Pokok Bahasan:** Metodologi *benchmarking* sistem operasi menggunakan `/proc`, `vmstat`, `iostat`, `pidstat`, `stress-ng`, dan `fio`; analisis komparatif metrik *page faults, swap, RSS, IOPS,* dan latensi berkas; serta *handoff* kompetensi menuju `STI-417 Komputasi Awan`, `STI-521 Internet untuk Segala (IoT)`, dan `STB-601 Arsitektur Cloud & DevOps`.
