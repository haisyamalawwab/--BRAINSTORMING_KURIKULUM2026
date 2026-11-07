# 071_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-417 — KOMPUTASI AWAN (*Cloud Computing*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.5.RPS-STI417`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Komputasi Awan / *Cloud Computing* |
| **Kode Mata Kuliah** | `STI-417` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Infrastruktur TI, Komputasi Awan & Keamanan (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS (`Teori`)** (`T = 3, P = 0`) — Tatap Muka & Studio Simulasi Cloud `3×50' = 150'`, Penugasan Terstruktur `3×60' = 180'`, Belajar Mandiri `3×60' = 180'` per pekan |
| **Semester / Tahun Akademik** | Semester 4 (Genap) — Tahap Penguatan Infrastruktur Modern (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `STI-312` Jaringan Komputer & Komunikasi Data, `STI-310` Sistem Operasi |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Bersinergi dengan `STI-416` Pengembangan Web Back End & `STI-418` Dasar Keamanan Informasi; menyerahkan otomasi IaC/Kubernetes/CI-CD ke `STB-601` Arsitektur Cloud & DevOps, *cloud backend* perangkat ke `STI-521` Internet untuk Segala (IoT), & skalabilitas layanan ke `STI-625` Rekayasa Platform Digital |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-07` (`P3` = **45%**) dan `CPL-11` (`KK3` = **55%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 3 (`K-3`)** — Kecerdasan Artifisial, Cloud & Cybersecurity (Bobot MK `Teori`: Tugas 1 `20%` · UTS `30%` · Tugas 2 `20%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Infrastruktur Jaringan, Cloud & Keamanan Siber |
| **Koordinator RMK** | Dr. Istiadi, S.T., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-07`** (`P3`) | Pengetahuan | Menguasai arsitektur komputer, sistem operasi, jaringan komputer, komputasi awan, serta prinsip keamanan informasi dan manajemen risiko siber. | **R** (*Reinforce*) | **45%** |
| **`CPL-11`** (`KK3`) | Keterampilan Khusus | Mampu merancang, mengkonfigurasi, mengamankan, dan mengelola infrastruktur jaringan, layanan komputasi awan (*cloud*), serta sistem keamanan informasi organisasi. | **R** (*Reinforce*) | **55%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **membandingkan model layanan *cloud* (*IaaS, PaaS, SaaS, FaaS*) dan model *deployment* (*Public, Private, Hybrid, Multi-Cloud*)** (*B*) pada penyedia layanan *cloud* global (*AWS / GCP / Azure*) (*C*) secara tepat (*D*). | **C4** (*Analyze*) | `CPL-07` (`P3`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **menganalisis teknologi virtualisasi dan mengimplementasikan pengemasan aplikasi menggunakan kontainer (*Docker: Dockerfile, Docker Compose, Container Registry*)** (*B*) pada lingkungan pengembangan dan target *cloud* (*C*) yang portabel dan efisien (*D*). | **C4** (*Analyze*) | `CPL-07` (`P3`) & `CPL-11` (`KK3`) | **UTS — Pekan 8 (30%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **mengonfigurasi sumber daya komputasi awan (*Virtual Machine, Object Storage*), jaringan virtual (*VPC, Subnetting, Security Group*), dan manajemen identitas (*IAM*)** (*B*) pada konsol/CLI *cloud* (*C*) secara aman (*D*). | **C3** (*Apply*) | `CPL-11` (`KK3`) | **Tugas 2 — Pekan 12 (20%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **mengevaluasi dan merancang arsitektur *cloud* yang memiliki ketersediaan tinggi (*High Availability*), *Load Balancing*, dan *Auto-Scaling*** (*B*) sesuai kebutuhan beban kerja dan anggaran organisasi (*C*) secara andal (*D*). | **C5** (*Evaluate*) | `CPL-07` (`P3`) & `CPL-11` (`KK3`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Membandingkan model layanan (**IaaS, PaaS, SaaS, FaaS**) dan model *deployment* pada **AWS / GCP / Azure** beserta keekonomian *CapEx vs OpEx*. | `CPMK-1` | **C4** | Mg 1–3 |
| **`Sub-CPMK-1.2`** | Menganalisis arsitektur virtualisasi (*Type-1 & Type-2 Hypervisor*) dibanding kontainerisasi tingkat sistem operasi. | `CPMK-1` | **C4** | Mg 3–4 |
| **`Sub-CPMK-2.1`** | Mengimplementasikan pengemasan kontainer menggunakan **Dockerfile**, **Docker Compose**, dan **Container Registry**. | `CPMK-2` | **C4** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Mengoptimalkan ukuran *image* kontainer dengan *multi-stage build*, *layer caching*, dan keamanan *non-root*. | `CPMK-2` | **C4** | Mg 6–7 |
| **`Sub-CPMK-3.1`** | Melakukan *provisioning* **Virtual Machine**, **Block/Object Storage** (*S3 / Cloud Storage*), dan basis data terkelola di *cloud*. | `CPMK-3` | **C3** | Mg 9–10 |
| **`Sub-CPMK-3.2`** | Mengonfigurasi **VPC, Public/Private Subnetting, Route Table, NAT, Security Group,** dan **IAM** (*Least Privilege*) secara aman. | `CPMK-3` | **C3** | Mg 11–12 |
| **`Sub-CPMK-4.1`** | Mengevaluasi kebutuhan **Load Balancing**, **Auto-Scaling**, pemantauan metrik, dan efisiensi biaya *cloud* (*FinOps* dasar). | `CPMK-4` | **C5** | Mg 13–14 |
| **`Sub-CPMK-4.2`** | Merancang cetak biru arsitektur *cloud* **High Availability (*Multi-AZ*)** & pemulihan bencana (*RTO/RPO*) yang tangguh. | `CPMK-4` | **C5** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Evaluasi & Perancangan Arsitektur Cloud High Availability, Load Balancing, Auto-Scaling, & FinOps (C5) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: ALB/NLB, Horizontal Auto-Scaling, CloudWatch & Cost | Sub-CPMK-4.2: Multi-AZ HA, RTO/RPO & Well-Architected)
      │
[CPMK-3: Konfigurasi Komputasi, Object Storage, Jaringan Virtual (VPC/Subnet/SG), & Identitas IAM Aman (C3) — Mg 9–12 (Tugas 2 20%)]
      ▲  (Sub-CPMK-3.1: Cloud VM, Block vs Object Storage S3/GCS, Managed DB | Sub-CPMK-3.2: VPC, Public/Private Subnet, SG, IAM)
      │
[CPMK-2: Pengemasan Aplikasi Portabel dengan Kontainer (Dockerfile, Multi-Stage, Docker Compose, Registry) (C4) — Mg 5–8 (UTS 30%)]
      ▲  (Sub-CPMK-2.1: Docker Engine, Volumes, Bridge Network, Compose | Sub-CPMK-2.2: Multi-Stage Build & Layer Cache Optimization)
      │
[CPMK-1: Analisis Model Layanan (IaaS/PaaS/SaaS/FaaS), Deployment Cloud, TCO, & Arsitektur Virtualisasi (C4) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: NIST Cloud, Shared Responsibility, CapEx/OpEx, AWS/GCP/Azure | Sub-CPMK-1.2: Hypervisor Type 1/2 vs Containers)
      ▲
[Fondasi Prasyarat: STI-310 Sistem Operasi (Kernel, Namespace, Process) + STI-312 Jaringan Komputer (CIDR Subnetting, Firewall, DNS)]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-07`** (`P3`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-07` = 45%** *(20%+15%+10%)* |
| **`CPL-07`** (`15%`) & **`CPL-11`** (`15%`) | **`CPMK-2`** | `Sub-CPMK-2.1` (`KK3`: 15%), `Sub-CPMK-2.2` (`P3`: 15%) | — | **30%** | — | — | **30%** | *(Terdisagregasi 15% `P3` + 15% `KK3`)* |
| **`CPL-11`** (`KK3`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **20%** | — | **20%** | **`CPL-11` = 55%** *(15%+20%+20%)* |
| **`CPL-07`** (`10%`) & **`CPL-11`** (`20%`) | **`CPMK-4`** | `Sub-CPMK-4.1` (`P3`: 10%), `Sub-CPMK-4.2` (`KK3`: 20%) | — | — | — | **30%** | **30%** | *(Terdisagregasi 10% `P3` + 20% `KK3`)* |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **30%** | **20%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-3` Dok 018; Target Dok 004 `65%`):** `Tugas 1 (20% — Case-Based Enterprise Cloud Migration & TCO Decision) + Tugas 2 (20% — Case-Based Cloud VPC, Storage, & Least-Privilege IAM Configuration) + UAS (30% — Project-Based Multi-AZ High Availability Cloud Architecture & Cost Blueprint)` = **70%** *(melampaui target 65% Dokumen 004)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-417 Komputasi Awan` (3 SKS `Teori`) membangun pemahaman konseptual yang kokoh sekaligus keterampilan arsitektural merancang dan mengonfigurasi infrastruktur awan modern di atas fondasi `STI-310 Sistem Operasi` dan `STI-312 Jaringan Komputer`. Mahasiswa menganalisis karakteristik NIST Cloud, keekonomian *CapEx vs OpEx*, *Shared Responsibility Model*, perbandingan **IaaS, PaaS, SaaS, & Serverless FaaS** lintas penyedia global (**AWS, Google Cloud, Microsoft Azure**), evolusi **Hypervisor Type-1/Type-2** menuju kontainer **Docker** (*Dockerfile, multi-stage layer caching, Docker Compose, Container Registry*), konfigurasi sumber daya komputasi, penyimpanan objek (*S3/GCS*), jaringan terisolasi (**VPC, Public/Private Subnet, NAT, Security Group**), dan manajemen akses (**IAM**), hingga perancangan arsitektur tahan gagal berstandar **Cloud Well-Architected Framework** (*Multi-AZ High Availability, Load Balancing, Auto-Scaling, RTO/RPO,* & estimasi biaya).

* **🟢 IN-SCOPE (Wajib Diajarkan):** Model layanan (*IaaS/PaaS/SaaS/FaaS*) & *deployment* (*Public/Private/Hybrid/Multi-Cloud*), *Shared Responsibility Model*, virtualisasi *Hypervisor* vs kontainer **Docker & Docker Compose**, *Cloud Compute & Object Storage*, **VPC Subnetting, Security Group, & IAM**, serta evaluasi & perancangan **High Availability, Load Balancing, Auto-Scaling,** dan estimasi biaya *cloud*.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. Dilarang membahas otomasi penuh *CI/CD Pipeline*, *Infrastructure as Code* (**Terraform / Ansible**), maupun administrasi klaster **Kubernetes** multi-node (ranah eksklusif peminatan **`STB-601 Arsitektur Cloud & DevOps`**).
  2. Dilarang membahas audit kepatuhan regulasi keamanan korporat ISO 27001 / COBIT mendalam (ranah **`STB-701 Tata Kelola Infrastruktur & Audit Keamanan TI`**).
* **🔄 HANDOFF ANCHOR:** Menyerahkan penguasaan kontainerisasi Docker, jaringan VPC, keamanan IAM, dan pola *High Availability* sebagai pijakan langsung menuju **`STB-601 Arsitektur Cloud & DevOps`**, **`STI-521 Internet untuk Segala (IoT)`**, dan **`STI-625 Rekayasa Platform Digital`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS19` (*IT Infrastructure & Cloud*), `BK-IT05` (*Cloud Computing*), & `BK-IS03` (*Enterprise Infrastructure*).

**Pustaka Utama:**
1. Erl, T., Puttini, R., & Mahmood, Z. (2013/2023). *Cloud Computing: Concepts, Technology & Architecture*. Pearson.
2. Wittig, M., & Wittig, A. (2023). *Amazon Web Services in Action: An In-Depth Guide to AWS* (3rd ed.). Manning Publications.
3. Poulton, N. (2023). *Docker Deep Dive* (2023 ed.). Nigel Poulton Publishing.

**Pustaka Pendukung:**
4. AWS / Google Cloud / Microsoft Azure. (2024). *Cloud Well-Architected Framework* (*Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability*).
5. NIST Special Publication 800-145 (*The NIST Definition of Cloud Computing*) & UU Pelindungan Data Pribadi (UU No. 27 Tahun 2022 — aspek *Data Residency / Sovereignty*).

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring: Tatap Muka & Studio Cloud) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Bagian I):** Menganalisis 5 karakteristik esensial **NIST Cloud**, transformasi finansial **CapEx vs OpEx**, & anatomi infrastruktur global (*Regions, Availability Zones, Edge/CDN*) [C4] | 1.1.1 Ketepatan menganalisis kapan beban kerja organisasi diuntungkan oleh elastisitas *cloud* (*OpEx*) vs infrastruktur *on-premise* (*CapEx*).<br>1.1.2 Ketepatan menjelaskan arti kedaulatan data (*Data Residency* Jakarta Region `ap-southeast-3` / `asia-southeast2`) terkait UU PDP. | **Kriteria:** Analisis ekonomi *cloud* dan topologi *Region/AZ* presisi.<br>**Teknik:** Diskusi studi kasus kegagalan kapasitas server saat pendaftaran serentak. | **Interactive Lecture & Case Discussion**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Kontrak belajar, aktivasi akun *Cloud Academy / AWS Skill Builder / GCP Sandbox* di LMS Edlink. | Evolusi *On-Premise* ke Cloud, Definisi **NIST SP 800-145**, **CapEx vs OpEx**, & Topologi Global (*Region, AZ, Edge*) `[1] Bab 1–4; [5]` | — |
| **2** | **`Sub-CPMK-1.1` (Bagian II):** Membandingkan model layanan (**IaaS, PaaS, SaaS, Serverless FaaS**) & **Shared Responsibility Model** pada **AWS, GCP, & Azure** [C4] | 1.1.3 Ketepatan memetakan batas tanggung jawab keamanan penyedia vs pelanggan pada *IaaS, PaaS,* dan *SaaS*.<br>1.1.4 Ketepatan memadankan layanan setara lintas vendor (mis. *EC2 $\leftrightarrow$ Compute Engine $\leftrightarrow$ Azure VM*; *Lambda $\leftrightarrow$ Cloud Functions*). | **Kriteria:** Pemetaan matriks layanan lintas 3 penyedia global dan tanggung jawab keamanan 100% akurat.<br>**Teknik:** Latihan komparasi arsitektur *pizza-as-a-service* & studi kasus kebocoran salah konfigurasi pelanggan. | **Comparative Analysis Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Kuis matriks **Shared Responsibility Model** di LMS Edlink. | Spektrum **IaaS, CaaS, PaaS, FaaS (*Serverless*), SaaS**, **Shared Responsibility Model**, & Peta Ekosistem **AWS / GCP / Azure** `[1] Bab 4; [2] Bab 1` | — |
| **3** | **`Sub-CPMK-1.1` (Bagian III) & `1.2` (Bagian I):** Mengevaluasi model *deployment* (**Public, Private, Hybrid, Multi-Cloud**) serta arsitektur virtualisasi **Type-1 vs Type-2 Hypervisor** (*KVM, Nitro, Xen, ESXi*) [C4] | 1.1.5 Ketepatan merekomendasikan strategi *Hybrid / Multi-Cloud* untuk perbankan/instansi pemerintah.<br>1.2.1 Ketepatan menganalisis cara *Hypervisor* membagi CPU (*vCPU*), memori, dan I/O secara terisolasi di atas perangkat keras fisik. | **Kriteria:** Pemilihan model *deployment* selaras kendala regulasi & latensi.<br>**Teknik:** Bedah arsitektur *AWS Nitro / KVM* & rilis resmi **Tugas 1 (RTM-1)**. | **Problem-Based Lecture**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Rilis resmi studi kasus migrasi enterprise **Tugas 1 (RTM-1)** di LMS Edlink. | Model Deployment (**Public, Private, Hybrid, Multi-Cloud**), Kalkulasi **TCO**, & Arsitektur **Hypervisor Type-1 vs Type-2** `[1] Bab 5; [2] Bab 3` | — |
| **4** | **`Sub-CPMK-1.2` (Bagian II):** Membandingkan **Virtual Machines vs Containers** (*Linux Namespaces & Control Groups/cgroups* dari `STI-310`) [C4]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 1.2.2 Ketepatan menganalisis kompromi waktu *booting*, jejak memori, efisiensi densitas, serta batas isolasi kernel bersama antara **VM** dan **Container**. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-3`)**.<br>**Teknik:** Pengumpulan Dokumen Analisis Strategi Cloud & Presentasi Kasus **Tugas 1 (`CPMK-1`)**. | **Architecture Debate & Uji Tugas 1**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Evolusi Virtualisasi: **VM vs OS-Level Containers**, Peran *Linux Namespaces & cgroups*, serta Standar **OCI** `[3] Bab 1–3` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1` (Bagian I):** Arsitektur **Docker Engine** (*Daemon, CLI, Image, Container*) & penyusunan **Dockerfile** portabel [C3→C4] | 2.1.1 Ketepatan membedakan instruksi `RUN` vs `CMD` vs `ENTRYPOINT`, `COPY` vs `ADD`, serta membangun *custom container image* aplikasi web yang berjalan identik di mesin mana pun. | **Kriteria:** Kontainer aplikasi berhasil dibangun dan diakses melalui *port mapping* (`-p`).<br>**Teknik:** Demonstrasi interaktif & latihan penulisan `Dockerfile` mandiri. | **Interactive Docker Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Panduan perintah esensial Docker CLI di LMS Edlink. | Arsitektur **Docker**, *Union File System*, Siklus Hidup Kontainer, & Anatomi **Dockerfile** `[3] Bab 4–7` | — |
| **6** | **`Sub-CPMK-2.2`:** Optimasi **Image Layer Caching**, **Multi-Stage Builds**, Keamanan Kontainer (*Non-Root User, Slim/Alpine Base*), & Distribusi ke **Container Registry** (*Docker Hub / GHCR / ECR*) [C4] | 2.2.1 Ketepatan memangkas ukuran *image* kontainer hingga $>70\%$ menggunakan **Multi-Stage Build** dan menyusun urutan baris `Dockerfile` agar *dependency layer cache* tidak terbangun ulang sia-sia setiap perubahan kode! | **Kriteria:** Bukti ukuran *image* sebelum vs sesudah optimasi turun drastis & kontainer berjalan tanpa hak `root`.<br>**Teknik:** Eksperimen komparasi *fat image* ($>900\text{ MB}$) vs *multi-stage slim image* ($<120\text{ MB}$). | **Optimization & Registry Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Kuis urutan instruksi *layer caching* `Dockerfile` di LMS Edlink. | Mekanisme **Copy-on-Write Layer Caching**, **Multi-Stage Builds**, `.dockerignore`, Keamanan *Container Image*, & **Container Registry** `[3] Bab 7–9` | — |
| **7** | **`Sub-CPMK-2.1` (Bagian II):** Persistensi Data Kontainer (*Volumes vs Bind Mounts*), Jaringan Internal Kontainer, & Orkestrasi Lokal Multi-Layanan **Docker Compose** + Klinik UTS [C4] | 2.1.2 Ketepatan merancang `docker-compose.yml` multi-layanan (*Reverse Proxy Nginx + App + PostgreSQL Volume + Internal Network*) di mana basis data terisolasi dari akses port luar secara langsung. | **Kriteria:** Data basis data tetap utuh saat kontainer dihapus/dibuat ulang berkat *Named Volume*.<br>**Teknik:** Bedah konfigurasi `docker-compose.yml` & klinik persiapan UTS. | **Multi-Container Studio & Klinik UTS**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Latihan soal analisis arsitektur cloud & *debugging* `Dockerfile/Compose` di LMS Edlink. | Persistensi *Stateless vs Stateful* (*Docker Volumes*), *Custom Bridge Networking*, **Docker Compose**, & *Healthcheck* `[3] Bab 10–12` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C4]** | Ketepatan menganalisis arsitektur virtualisasi/kontainer serta merancang, mendiagnosis, dan mengoptimalkan konfigurasi **Dockerfile (*Multi-Stage & Layer Caching*), Docker Compose,** dan **Container Registry** yang portabel, aman, dan efisien. | **Kriteria:** **Rubrik Analitik UTS (`K-3`)**.<br>**Teknik:** Ujian Tertulis & Praktik Konfigurasi Kontainer Terawasi (*Closed-AI*). | **Ujian Tengah Semester (Analisis Virtualisasi & Konfigurasi Docker)**<br>`[120 menit]` | Pengarsipan lembar jawaban/artefak UTS & nilai `CPMK-2` pada portal OBE. | Materi Virtualisasi, **Dockerfile**, *Multi-Stage Layer Caching*, **Docker Compose**, & Registry (Pekan 4–7) | **30%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1` (Bagian I):** *Provisioning* Komputasi Awan: **Virtual Machines** (*EC2 / Compute Engine*), keluarga tipe *instance*, pasangan kunci SSH, & *User-Data Bootstrap Script* [C3] | 3.1.1 Ketepatan memilih keluarga *instance* (*General Purpose, Compute-Optimized, Memory-Optimized, Spot vs On-Demand vs Reserved*) serta melakukan *provisioning* VM Linux aman berbasis kunci SSH. | **Kriteria:** Pemilihan ukuran VM bebas pemborosan (*right-sizing*) dan akses SSH menggunakan kunci kriptografi (tanpa kata sandi!).<br>**Teknik:** Simulasi konsol/CLI *cloud* pembuatan & *bootstrapping* server web. | **Cloud Compute Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Panduan *Cloud Sandbox* & kewaspadaan *Billing Alarm* ($0 kejutan tagihan!) di LMS Edlink. | Layanan Komputasi IaaS (*EC2 / GCE*), Model Harga (*On-Demand, Reserved, Spot*), *AMI/Machine Image*, & *Cloud-Init Bootstrap* `[2] Bab 3–4` | — |
| **10** | **`Sub-CPMK-3.1` (Bagian II):** Arsitektur Penyimpanan Awan (**Block vs File vs Object Storage — S3/GCS**) & Layanan Basis Data Terkelola (**Managed RDBMS / RDS**) [C3] | 3.1.2 Ketepatan membedakan kapan memakai *Block Storage* (EBS), *Network File Storage* (EFS), vs **Object Storage** (*S3/GCS*) lengkap *Bucket Policy, Pre-Signed URL,* & *Lifecycle Tiering* (*Standard $\rightarrow$ Infrequent $\rightarrow$ Glacier*). | **Kriteria:** Bucket penyimpanan objek tertutup dari akses publik liar (*Block Public Access*) dan kebijakan siklus hidup tepat.<br>**Teknik:** Latihan konfigurasi *Object Storage* aman & perbandingan *Self-Managed DB on VM vs Managed RDS*. | **Cloud Storage & Managed DB Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Rilis resmi spesifikasi skenario konfigurasi **Tugas 2 (RTM-2)** di LMS Edlink. | **Block, File, & Object Storage (*S3/GCS*)**, *Durability 11 Nines*, *Storage Lifecycle*, & *Managed Database Services (RDS)* `[2] Bab 8–10` | — |
| **11** | **`Sub-CPMK-3.2` (Bagian I):** Merancang dan mengonfigurasi Jaringan Virtual Terisolasi (**VPC, CIDR Subnetting, Public vs Private Subnet, Internet Gateway, NAT Gateway, & Route Tables**) [C3] | 3.2.1 Ketepatan menghitung blok CIDR **VPC** (melanjutkan `STI-312`) yang memisahkan **Public Subnet** (hanya untuk *Load Balancer / Bastion*) dan **Private Subnet** (untuk server aplikasi & basis data agar mustahil ditembak langsung dari internet!). | **Kriteria:** Tabel rute, *Internet Gateway*, dan *NAT Gateway* terpetakan benar tanpa kebocoran rute publik pada *subnet* basis data.<br>**Teknik:** Latihan perancangan diagram & konfigurasi topologi VPC 2-*tier*/3-*tier*. | **Cloud Networking Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Kuis penelusuran paket pada *Route Table* VPC di LMS Edlink. | Jaringan Definisi Perangkat Lunak di Cloud: **VPC**, Desain **Public vs Private Subnet**, **IGW vs NAT Gateway**, & *VPC Peering* Dasar `[2] Bab 6` | — |
| **12** | **`Sub-CPMK-3.2` (Bagian II):** Pertahanan Perimeter & Identitas Cloud: **Security Group (*Stateful*) vs NACL (*Stateless*)** serta **IAM (*Users, Groups, Roles, JSON Policies, MFA, Least Privilege*)** [C3]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 3.2.2 Ketepatan merancang rantai aturan *Security Group* berantai (`ALB-SG` $\rightarrow$ `App-SG` port 8000 $\rightarrow$ `DB-SG` port 5432) dan kebijakan **IAM Role** tanpa menanam *Access Key* statis di dalam kode server! | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-3`)**.<br>**Teknik:** Pengumpulan & Verifikasi Skenario Konfigurasi VPC, Storage, Security Group, & Kebijakan JSON IAM (**Tugas 2**). | **Cloud Security Studio & Uji Tugas 2**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan berkas **Tugas 2 (`CPMK-3`)** di LMS Edlink. | **Security Group vs Network ACL**, Prinsip **IAM Least Privilege**, *IAM Roles / Service Accounts* (anti-*hardcoded keys*!), & *Root Account Hardening* `[2] Bab 5–6` | **20%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.1` (Bagian I):** Mengevaluasi skalabilitas vertikal vs horizontal, arsitektur **Elastic Load Balancing** (*Layer-4 NLB vs Layer-7 ALB*), & **Auto-Scaling Groups** [C5] | 4.1.1 Ketepatan merancang kebijakan **Horizontal Auto-Scaling** (*Target Tracking CPU/Request Count, Cooldown Period, Health Check Grace Period*) serta syarat mutlak aplikasi *stateless* di balik *Load Balancer*. | **Kriteria:** Analisis membuktikan mengapa sesi lokal di disk VM hancur saat *Auto-Scaling* aktif (dan harus dipindah ke Redis/DB sesuai `STI-416`!).<br>**Teknik:** Studi kasus lonjakan trafik 20× lipat *flash sale* / KRS online. | **Scalability Case Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Spesifikasi proyek akhir perancangan arsitektur **UAS** dirilis di LMS Edlink. | *Vertical vs Horizontal Scaling*, Desain Aplikasi *Stateless*, **Layer-4 vs Layer-7 Load Balancing**, & Kebijakan **Auto-Scaling** `[1] Bab 8–10; [2] Bab 15–17` | — |
| **14** | **`Sub-CPMK-4.2`:** Merancang arsitektur **High Availability (*Multi-AZ*)**, penghitungan ketersediaan seri/paralel (*SLA 99,9% vs 99,99%*), & strategi **Disaster Recovery (*RTO & RPO*)** [C5] | 4.2.1 Ketepatan mengidentifikasi dan mengeliminasi setiap **Single Point of Failure (SPOF)** pada arsitektur *web, app, database (Multi-AZ Standby),* dan *cache*, serta memilih strategi DR (*Backup & Restore, Pilot Light, Warm Standby, Active-Active*) sesuai target **RTO/RPO**. | **Kriteria:** Diagram arsitektur *Multi-AZ* bebas SPOF dan perhitungan SLA komposit matematis benar.<br>**Teknik:** Lokakarya bedah kegagalan satu *Availability Zone* penuh (*Chaos Tabletop*). | **High Availability Design Studio**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Templat diagram arsitektur resmi (*AWS/GCP Architecture Icons*) di LMS Edlink. | Matematika Ketersediaan (*Composite SLA*), Eliminasi **Single Point of Failure (SPOF)**, Arsitektur **Multi-AZ**, & Spektrum **Disaster Recovery (RTO/RPO)** `[2] Bab 14–17; [4]` | — |
| **15** | **`Sub-CPMK-4.1` (Bagian II) & `4.2` (Sintesis):** Observabilitas Cloud (*Metrics, Logs, Billing Alerts*), **Cloud FinOps / Cost Optimization** (*AWS Pricing Calculator*), & Review Cetak Biru **Well-Architected** Pra-UAS [C5] | 4.1.2 Ketepatan menyusun estimasi biaya bulanan realistis menggunakan *Official Cloud Pricing Calculator* dan mengidentifikasi 3 strategi penghematan biaya tanpa mengorbankan ketersediaan. | **Kriteria:** Cetak biru arsitektur seimbang antara keandalan *High Availability*, keamanan VPC/IAM, dan kewajaran anggaran bulanan.<br>**Teknik:** *Architecture Peer Review* terhadap 6 pilar *Cloud Well-Architected Framework* & klinik UAS. | **FinOps & Architecture Review**<br>`[TM: 150']`<br>`[PT: 180']` · `[BM: 180']` | Pengumpulan dokumen cetak biru arsitektur, kalkulasi biaya, & prototipe/simulasi UAS di LMS Edlink. | Pemantauan *CloudWatch / Cloud Monitoring*, **Cloud FinOps & Pricing Calculator**, 6 Pilar **Well-Architected Framework**, & *Handoff* ke `STB-601` `[2]; [4]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C5]** | Kualitas evaluasi kebutuhan dan ketangguhan rancangan cetak biru **Arsitektur Cloud High Availability, Load Balancing, & Auto-Scaling** lengkap isolasi VPC/IAM, perhitungan SLA & RTO/RPO, serta rincian estimasi biaya *cloud*. | **Kriteria:** **Rubrik Analitik UAS (`K-3`)**.<br>**Teknik:** Penilaian Dokumen *Cloud Architecture Blueprint & Cost Model* (50% UAS) + Sidang *Architecture Chaos Defense* Individu (50% UAS). | **Sidang Pertahanan Arsitektur Cloud (*Chaos Failure Injection Q&A*)**<br>`[150 menit]` | Pengarsipan cetak biru arsitektur & rekap nilai `CPL-07` dan `CPL-11` pada portal OBE. | Sintesis Komprehensif Layanan Cloud, Kontainer, VPC/IAM, **High Availability**, **Load Balancing**, **Auto-Scaling**, & **FinOps** | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-07` [C4])
* **Bentuk Instrumen:** Studi Kasus **Analisis Strategi Migrasi Cloud, Pemetaan Layanan Multi-Vendor, & Komparasi Virtualisasi** pada organisasi nyata (mis. RSUD / Bank Perkreditan / Kampus / *E-Commerce* Regional): mahasiswa memetakan komponen sistem ke model **IaaS, PaaS, SaaS, atau FaaS**, memilih model *deployment* (*Public/Hybrid*) yang patuh UU PDP, membandingkan layanan setara di **AWS vs GCP vs Azure**, serta menganalisis kapan beban kerja ditaruh di **VM** vs **Container**.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan perbandingan model layanan (*IaaS/PaaS/SaaS/FaaS*), *deployment*, & *Shared Responsibility* (`Sub-CPMK-1.1`) = **55%**; (2) Ketajaman analisis virtualisasi *Hypervisor* vs kontainerisasi & kalkulasi *CapEx/OpEx* (`Sub-CPMK-1.2`) = **45%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 30% · Mengukur `CPMK-2` / `CPL-07` [15%] & `CPL-11` [15%] [C4])
* **Bentuk Instrumen:** **Ujian Tengah Semester Terawasi: Analisis Virtualisasi & Rekayasa Konfigurasi Docker** (120 menit, individu): Bagian A menguji analisis mekanisme isolasi kontainer, optimasi **layer caching**, dan perbaikan cacat keamanan/ukuran pada `Dockerfile` yang membengkak (`Sub-CPMK-2.2` → `CPL-07`); Bagian B meminta mahasiswa menyusun `Dockerfile` *multi-stage* dan `docker-compose.yml` multi-layanan lengkap *named volume*, jaringan internal terisolasi, dan alur *push/pull* **Container Registry** (`Sub-CPMK-2.1` → `CPL-11`).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan implementasi `Dockerfile`, `Docker Compose`, volume, & registry (`Sub-CPMK-2.1` → `CPL-11`) = **50%** *(15% MK)*; (2) Analisis virtualisasi & optimasi *multi-stage build / layer caching* (`Sub-CPMK-2.2` → `CPL-07`) = **50%** *(15% MK)*.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 20% · Mengukur `CPMK-3` / `CPL-11` [C3])
* **Bentuk Instrumen:** Studi Kasus Praktis **Konfigurasi Infrastruktur Cloud Terisolasi (Compute, Object Storage, VPC, Security Group, & IAM)**: mahasiswa membangun dan mendokumentasikan konfigurasi *Virtual Machine*, *Object Storage* (*S3/GCS* ber-*lifecycle* & privat), desain **VPC CIDR** dengan pemisahan ketat *Public & Private Subnet*, aturan berantai **Security Group**, serta dokumen kebijakan JSON **IAM Least Privilege** berbasis *Role*.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan *provisioning* VM & konfigurasi aman *Object Storage* (`Sub-CPMK-3.1`) = **40%**; (2) Ketepatan topologi **VPC Subnetting**, *Route/NAT*, **Security Group**, & kebijakan **IAM Least Privilege** (`Sub-CPMK-3.2`) = **60%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-07` [10%] & `CPL-11` [20%] [C5])
* **Bentuk Instrumen:** **Proyek Akhir Cetak Biru Arsitektur Cloud High Availability (*Well-Architected Blueprint & Cost Model*)** (50% nilai UAS: dokumen arsitektur teknis + prototipe/simulasi untuk sistem berskala nasional yang menuntut SLA $\ge 99,95\%$, mencakup evaluasi **Load Balancing & Auto-Scaling**, topologi **Multi-AZ** bebas SPOF, strategi *Disaster Recovery RTO/RPO*, dan rincian *Cloud Pricing Calculator*) + **Sidang *Chaos Failure Injection Defense* Individu** (50% nilai UAS, 150 menit: dosen menyimulasikan *"Bagaimana jika AZ-a mati total / trafik naik 15× / kredensial pengembang bocor?"* dan menguji ketahanan rancangan tiap mahasiswa).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketajaman evaluasi beban kerja, **Load Balancing, Auto-Scaling,** & efisiensi biaya *FinOps* (`Sub-CPMK-4.1` → `CPL-07`) = **33,33%** *(10% MK)*; (2) Ketangguhan rancangan arsitektur **High Availability Multi-AZ**, eliminasi SPOF, & penguasaan sidang *chaos defense* (`Sub-CPMK-4.2` → `CPL-11`) = **66,67%** *(20% MK)*.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Infrastruktur, Cloud & Keamanan**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Istiadi, S.T., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
