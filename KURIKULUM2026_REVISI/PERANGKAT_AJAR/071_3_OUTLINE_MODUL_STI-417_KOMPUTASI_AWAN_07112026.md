# 071_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-417 — KOMPUTASI AWAN (*Cloud Computing*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.5.RPS-STI417` · **Bobot:** 3 SKS (`Teori`: `T=3, P=0`) · **Semester:** 4  
**CPL:** `CPL-07` (`P3` = 45%) & `CPL-11` (`KK3` = 55%) [Level `R`] · **BoK:** `BK-IS19`, `BK-IT05`, `BK-IS03`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Arsitektur & Rekayasa Komputasi Awan Modern: Layanan Cloud Global, Kontainerisasi Docker, Jaringan VPC & IAM, hingga Desain High Availability dan FinOps* |
| **Target Tebal Naskah** | 14 Bab Materi & Studio Kasus + 2 Unit Evaluasi ($\pm 210\text{–}240\text{ halaman}$ A4) |
| **Pagar Pembatas Buku (*Guardrail*)** | Melanjutkan `STI-310` & `STI-312` pada fondasi komputasi awan, Docker, VPC/IAM, dan arsitektur *High Availability*; tidak mencakup *Terraform IaC*, *CI/CD Pipeline* penuh, maupun orkestrasi klaster *Kubernetes* (`STB-601 Arsitektur Cloud & DevOps`). |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP CPMK & SUB-CPMK

| Bagian | Bab | Judul Bab | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Paradigma Cloud & Virtualisasi** | **Bab 1** | Karakteristik **NIST Cloud**, Ekonomi **CapEx vs OpEx**, & Infrastruktur Global (*Region/AZ*) | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Spektrum Layanan (**IaaS, PaaS, SaaS, FaaS**), *Shared Responsibility*, & **AWS / GCP / Azure** | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3** | Model Deployment (*Public, Private, Hybrid, Multi-Cloud*), TCO, & **Hypervisor Type-1/2** | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | Tugas 1 (20%) |
| | **Bab 4** | Komparasi Arsitektur **Virtual Machines vs Containers** (*Linux Namespaces & cgroups*) | Mg 4 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Kontainerisasi Portabel dengan Docker** | **Bab 5** | Arsitektur **Docker Engine**, Siklus Kontainer, & Konstruksi **Dockerfile** | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 6** | Optimasi **Layer Caching**, **Multi-Stage Builds**, Keamanan Kontainer, & **Registry** | Mg 6 | `CPMK-2` | `Sub-CPMK-2.2` | UTS (30%) |
| | **Bab 7** | Persistensi *Docker Volumes*, Jaringan Internal, & Aplikasi Multi-Layanan **Docker Compose** | Mg 7 | `CPMK-2` | `Sub-CPMK-2.1` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Bank Soal Analisis Virtualisasi & Latihan Optimasi Dockerfile/Compose (UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| **Bagian III:<br>Komputasi, Storage, VPC, & IAM** | **Bab 8** | *Provisioning* **Cloud Virtual Machines**, Model Harga, & Otomasi *Bootstrapping* | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 9** | **Block, File, & Object Storage (*S3/GCS*)**, *Lifecycle Tiering*, & *Managed Database* | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 10** | Rekayasa Jaringan **VPC**: *CIDR, Public/Private Subnets, IGW, NAT,* & *Route Tables* | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (20%) |
| | **Bab 11** | Pertahanan Perimeter (**Security Group vs NACL**) & Manajemen Akses **IAM Least Privilege** | Mg 12 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>High Availability, Auto-Scaling, & FinOps** | **Bab 12** | Arsitektur *Stateless*, **Elastic Load Balancing (L4/L7)**, & **Horizontal Auto-Scaling** | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13** | Matematika SLA, Eliminasi SPOF, Arsitektur **Multi-AZ High Availability**, & **RTO/RPO** | Mg 14 | `CPMK-4` | `Sub-CPMK-4.2` | UAS (30%) |
| | **Bab 14** | Observabilitas, **Cloud FinOps & Pricing Calculator**, **Well-Architected**, & *Handoff* `STB-601` | Mg 15 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Penyusunan Cloud Well-Architected Blueprint & Sidang Chaos Defense (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB BUKU MODUL

#### BAB 1: Karakteristik NIST Cloud, Ekonomi CapEx vs OpEx, & Infrastruktur Global (Pekan 1)
* **Substansi:** Lima karakteristik NIST, enam keuntungan komputasi awan, analisis *CapEx vs OpEx*, topologi *Region, Availability Zone (AZ), Edge Location*, dan kepatuhan *Data Residency* UU PDP Indonesia.

#### BAB 2: Spektrum Layanan (IaaS, PaaS, SaaS, FaaS), Shared Responsibility, & Ekosistem Global (Pekan 2)
* **Substansi:** Komparasi teknis *IaaS, CaaS, PaaS, Serverless FaaS,* dan *SaaS*, matriks pembagian tanggung jawab keamanan *Shared Responsibility Model*, serta peta padanan layanan **AWS, Google Cloud, dan Azure**.

#### BAB 3: Model Deployment, Total Cost of Ownership (TCO), & Hypervisor Type-1/2 (Pekan 3)
* **Substansi:** Kriteria keputusan *Public, Private, Hybrid,* dan *Multi-Cloud*, perhitungan TCO migrasi, serta arsitektur *Type-1 Bare-Metal Hypervisor* (*KVM/Nitro*) vs *Type-2*.

#### BAB 4: Komparasi Arsitektur Virtual Machines vs Containers (Pekan 4)
* **Substansi:** Isolasi perangkat keras virtual vs isolasi proses kernel bersama (*Linux Namespaces & cgroups*), standar **Open Container Initiative (OCI)**, dan matriks pemilihan beban kerja VM vs Kontainer.

#### BAB 5: Arsitektur Docker Engine, Siklus Kontainer, & Konstruksi Dockerfile (Pekan 5)
* **Substansi:** Arsitektur *client-daemon*, *UnionFS*, perintah esensial CLI, dan kaidah penulisan instruksi **Dockerfile** yang bersih serta deterministik.

#### BAB 6: Optimasi Layer Caching, Multi-Stage Builds, Keamanan Kontainer, & Registry (Pekan 6)
* **Substansi:** Mekanisme invalidasi *cache layer*, pemangkasan drastis ukuran *image* dengan **Multi-Stage Builds**, eksekusi pengguna *non-root*, serta manajemen versi di **Container Registry**.

#### BAB 7: Persistensi Docker Volumes, Jaringan Internal, & Docker Compose (Pekan 7)
* **Substansi:** Penanganan data *stateful* dengan *Named Volumes*, isolasi jaringan internal antar-kontainer, dan definisi tumpukan aplikasi lengkap pada `docker-compose.yml`.

#### BAB 8: Provisioning Cloud Virtual Machines, Model Harga, & Otomasi Bootstrapping (Pekan 9)
* **Substansi:** Pemilihan keluarga *instance*, strategi penghematan *On-Demand vs Reserved vs Spot*, manajemen pasangan kunci SSH, dan inisialisasi server otomatis dengan *cloud-init / user-data*.

#### BAB 9: Block, File, & Object Storage (S3/GCS), Lifecycle Tiering, & Managed Database (Pekan 10)
* **Substansi:** Karakteristik IOPS & daya tahan *Block, File,* vs **Object Storage**, *Bucket Policy & Pre-Signed URLs*, aturan *Lifecycle Tiering*, dan keunggulan operasional *Managed RDBMS*.

#### BAB 10: Rekayasa Jaringan VPC — CIDR, Public/Private Subnets, IGW, NAT, & Route Tables (Pekan 11)
* **Substansi:** Perencanaan ruang alamat CIDR VPC multi-AZ, pemisahan ketat *Public Subnet* dan *Private Subnet*, cara kerja *Internet Gateway* vs *NAT Gateway*, serta tabel perutean.

#### BAB 11: Pertahanan Perimeter (Security Group vs NACL) & Manajemen Identitas IAM (Pekan 12)
* **Substansi:** Perbandingan firewall *stateful* (**Security Group**) vs *stateless* (**NACL**), pola *Security Group Chaining*, kebijakan JSON **IAM Least Privilege**, dan penggunaan *IAM Roles* bebas kredensial tertanam.

#### BAB 12: Arsitektur Stateless, Elastic Load Balancing (L4/L7), & Horizontal Auto-Scaling (Pekan 13)
* **Substansi:** Eksternalisasi *state* sesi/berkas, perutean cerdas *Layer-7 Application Load Balancer*, pemeriksaan kesehatan target, dan kebijakan elastisitas **Auto-Scaling Group**.

#### BAB 13: Matematika SLA, Eliminasi SPOF, Arsitektur Multi-AZ High Availability, & RTO/RPO (Pekan 14)
* **Substansi:** Perhitungan ketersediaan sistem seri-paralel, identifikasi & penghapusan **Single Point of Failure**, replikasi sinkron basis data *Multi-AZ*, serta empat pola *Disaster Recovery* berdasarkan **RTO & RPO**.

#### BAB 14: Observabilitas, Cloud FinOps & Pricing Calculator, Well-Architected, & Handoff (Pekan 15)
* **Substansi:** Telemetri *Metrics/Logs/Alarms*, estimasi biaya terperinci & jebakan biaya *egress/NAT*, audit 6 pilar **Cloud Well-Architected Framework**, serta kesiapan menuju `STB-601 Arsitektur Cloud & DevOps`.
