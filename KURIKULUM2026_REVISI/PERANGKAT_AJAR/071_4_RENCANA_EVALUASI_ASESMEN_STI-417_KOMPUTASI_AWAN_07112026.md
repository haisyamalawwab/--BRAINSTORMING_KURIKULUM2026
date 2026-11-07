# 071_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-417 — KOMPUTASI AWAN (*Cloud Computing*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.5.RPS-STI417` · **Bobot:** 3 SKS (`Teori`: `T=3, P=0`) · **Semester:** 4  
**Klaster Asesmen MK (Dok 018):** Klaster 3 (`K-3`) — Kecerdasan Artifisial, Cloud & Cybersecurity  
**CPL Dibebankan:** `CPL-07` (`P3` = **45%**) & `CPL-11` (`KK3` = **55%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 005, 008, 018,** dan **043**, mata kuliah `STI-417 Komputasi Awan` (3 SKS `Teori`) menerapkan skema bobot baku mata kuliah `Teori` (`20% / 30% / 20% / 30%`) dengan pemetaan presisi ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-07` / `P3`)** — *Case-Based Cloud Service/Deployment Strategy & Hypervisor vs Container Analysis*.
* **UTS (Pekan 8 — 30%) → `CPMK-2` (`CPL-07` [15%] & `CPL-11` [15%])** — *Supervised Exam: Container Virtualization Optimization & Dockerfile/Docker Compose Engineering*.
* **Tugas 2 (Pekan 12 — 20%) → `CPMK-3` (`CPL-11` / `KK3`)** — *Case-Based Cloud Compute, Object Storage, Multi-Subnet VPC, Security Group, & IAM Configuration*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-07` [10%] & `CPL-11` [20%])** — *Project-Based Multi-AZ High Availability Cloud Architecture Blueprint, Cost Model, & Chaos Defense*.
* **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-3` Dok 018; Target Dok 004 `65%`):** `Tugas 1 (20%) + Tugas 2 (20%) + UAS (30%) = 70%` berbasis studi kasus keputusan infrastruktur dan proyek perancangan arsitektur *cloud* tahan gagal.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-07`**<br>(`P3` — 45%)<br>*Level: R* | **`CPMK-1`**<br>(C4) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus migrasi cloud: Perbandingan *IaaS/PaaS/SaaS/FaaS* & *deployment* di AWS/GCP/Azure | **RTM-1 (Tugas 1)** Bagian Strategi Layanan + Rubrik Analitik T1 | Sumatif | 11% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Studi kasus arsitektur: Analisis virtualisasi *Hypervisor Type-1/2* vs kontainerisasi & TCO | **RTM-1 (Tugas 1)** Bagian Virtualisasi & TCO + Rubrik Analitik T1 | Sumatif | 9% | |
| **`CPL-07` (15%)**<br>& **`CPL-11` (15%)**<br>*Level: R* | **`CPMK-2`**<br>(C4) | `Sub-CPMK-2.1`<br>*(`CPL-11`)* | Mg 8 | Ujian terawasi 120': Pengemasan aplikasi portabel dengan **Dockerfile, Docker Compose,** & Registry | **Lembar Soal UTS** (Bagian Konstruksi Kontainer) + Rubrik UTS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-2.2`<br>*(`CPL-07`)* | Mg 8 | Ujian terawasi 120': Analisis & optimasi ukuran *image* (*multi-stage build* & *layer caching*) | **Lembar Soal UTS** (Bagian Audit & Optimasi Layer) + Rubrik UTS | Sumatif | 15% | |
| **`CPL-11`**<br>(`KK3` — 55%)<br>*Level: R* | **`CPMK-3`**<br>(C3) | `Sub-CPMK-3.1` | Mg 12 | Studi kasus konfigurasi cloud: *Provisioning* **Virtual Machine** & **Object Storage** aman | **RTM-2 (Tugas 2)** Artefak Compute/Storage + Rubrik Analitik T2 | Sumatif | 8% | **20%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Studi kasus jaringan & akses: Konfigurasi **VPC, Subnetting, Security Group,** & kebijakan **IAM** | **RTM-2 (Tugas 2)** Topologi VPC & JSON Policy IAM + Rubrik T2 | Sumatif | 12% | |
| **`CPL-07` (10%)**<br>& **`CPL-11` (20%)**<br>*Level: R* | **`CPMK-4`**<br>(C5) | `Sub-CPMK-4.1`<br>*(`CPL-07`)* | Mg 16 | Proyek cetak biru arsitektur + sidang: Evaluasi **Load Balancing, Auto-Scaling,** & biaya *FinOps* | **Dokumen Blueprint & Cloud Cost Calculator** + Rubrik Analitik UAS | Sumatif | 10% | **30%** |
| | | `Sub-CPMK-4.2`<br>*(`CPL-11`)* | Mg 16 | Proyek cetak biru arsitektur + sidang: Rancangan **High Availability Multi-AZ** & *Chaos Defense* | **Diagram Arsitektur HA, Strategi DR, & Sidang UAS** + Rubrik UAS | Sumatif | 20% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/30/20/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Analisis Strategi Migrasi Cloud & Virtualisasi)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Diskusi Kasus **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-07`).
* **Spesifikasi Pengerjaan Individu:**
  1. Diberikan profil organisasi dengan 5 beban kerja beragam (portal publik, ERP legasi, pemroses kuitansi periodik, penyimpanan rekam dokumen sensitif UU PDP, dan kolaborasi kantor); mahasiswa memetakan tiap beban kerja secara tepat ke **IaaS, PaaS, SaaS, atau Serverless FaaS** beserta model *deployment*-nya (*Public/Hybrid*).
  2. Menyusun matriks perbandingan layanan setara pada **AWS, GCP, dan Azure**, memetakan *Shared Responsibility*, serta menganalisis beban kerja mana yang tepat dijalankan pada **VM Hypervisor** vs **Container**.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Analisis & Optimasi Kontainerisasi Docker)
* **Format & Bobot:** Ujian Terawasi (**120 menit**, individu) · Bobot **30%** (`CPMK-2` → `CPL-07` [15%] & `CPL-11` [15%]).
* **Spesifikasi Soal:**
  1. **Bagian Audit & Optimasi (`Sub-CPMK-2.2` — 50% UTS):** Diberikan sebuah `Dockerfile` buruk berukuran $1,1\text{ GB}$ yang memiliki 6 kelemahan (*urutan layer membatalkan cache, menjalankan proses sebagai `root`, menyalin `.env`/`.git`, memakai base image penuh kompilator*); mahasiswa mendiagnosis keenam masalah dan menulis ulang menjadi **Multi-Stage Dockerfile** yang optimal dan aman.
  2. **Bagian Orkestrasi & Registry (`Sub-CPMK-2.1` — 50% UTS):** Menyusun `docker-compose.yml` lengkap untuk arsitektur 3-lapis (*Nginx Reverse Proxy + API Service + PostgreSQL Stateful Volume*) dengan jaringan internal terisolasi, *healthcheck*, dan perintah publikasi ke **Container Registry**.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Konfigurasi Komputasi, Storage, VPC, & IAM Aman)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Verifikasi **Pekan 12** · Bobot **20%** (`CPMK-3` → `CPL-11`).
* **Spesifikasi Teknis Individu:**
  1. Mengonfigurasi (pada *Cloud Sandbox* / simulator CLI terverifikasi) *Virtual Machine* ber-*bootstrap script* dan bucket **Object Storage** (*S3/GCS*) privat dengan aturan *Lifecycle Policy* otomatis.
  2. Merancang dan mengonfigurasi blok CIDR **VPC** dengan pemisahan ketat *Public Subnets* & *Private Subnets* lintas 2 AZ, tabel rute (*IGW & NAT*), rantai **Security Group** minimal-port, serta dokumen kebijakan JSON **IAM Least Privilege** berbasis *Role* (tanpa *hardcoded access keys*).

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Cetak Biru Arsitektur Cloud High Availability)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-07` [10%] & `CPL-11` [20%]), memadukan **Proyek Tim *Cloud Well-Architected Blueprint* (50% nilai UAS)** + **Sidang *Chaos Failure Injection Defense* Individu (50% nilai UAS, 150 menit)**:
  1. Tim (maks. 3 orang) menyusun cetak biru arsitektur *cloud* kelas produksi untuk sistem bertrafik puncak 50.000 pengguna serentak (SLA target $\ge 99,95\%$), mencakup diagram arsitektur standar resmi, desain **Application Load Balancer & Auto-Scaling**, redundansi basis data **Multi-AZ** bebas *Single Point of Failure*, strategi **Disaster Recovery (RTO & RPO)**, serta lembar rincian biaya bulanan dari *Official Cloud Pricing Calculator*.
  2. Pada sidang individu, penguji menyuntikkan skenario bencana (*kegagalan satu AZ penuh, lonjakan DDoS/flash-sale, atau penghapusan tak-sengaja objek S3*) untuk menguji ketahanan rancangan mahasiswa.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-417}}$)
$$NA_{\text{STI-417}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004 & 008)
1. **Ketercapaian `CPL-07` (`P3` — bobot 45% MK dari `CPMK-1` [20%] + `Sub-CPMK-2.2` pada UTS [15%] + `Sub-CPMK-4.1` pada UAS [10%]):**
   $$\text{Score}_{\text{CPL-07, STI-417}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,15\,S_{\text{UTS, Sub-2.2}}(i) + 0,10\,S_{\text{UAS, Sub-4.1}}(i)}{0,45}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,45 = 1,35\text{ SKS}$).*
2. **Ketercapaian `CPL-11` (`KK3` — bobot 55% MK dari `Sub-CPMK-2.1` pada UTS [15%] + `CPMK-3` [20%] + `Sub-CPMK-4.2` pada UAS [20%]):**
   $$\text{Score}_{\text{CPL-11, STI-417}}(i) = \frac{0,15\,S_{\text{UTS, Sub-2.1}}(i) + 0,20\,S_{\text{Tugas 2}}(i) + 0,20\,S_{\text{UAS, Sub-4.2}}(i)}{0,55}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,55 = 1,65\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**; remedial diberikan maksimal 1 kali bagi mahasiswa dengan skor CPMK $< 65,0$ dengan nilai plafon pasca-remedial **70,0 (B)**.
