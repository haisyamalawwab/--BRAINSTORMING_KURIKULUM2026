# 071_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-417 — KOMPUTASI AWAN (*Cloud Computing*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.5.RPS-STI417` · **Bobot:** 3 SKS `Teori` (`TM 150'`, `PT 180'`, `BM 180'`) · **Semester:** 4  
**Prasyarat:** `STI-312` Jaringan Komputer & Komunikasi Data, `STI-310` Sistem Operasi  
**CPL:** `CPL-07` (`P3` = 45%) & `CPL-11` (`KK3` = 55%) [Level `R`] · **Klaster Rubrik:** `K-3`  
**Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu `STI-417` |
|---|---|
| **Struktur Waktu Tatap Muka (`150'`)** | **Pendahuluan Insiden/Kasus Cloud (`15'`)** · **Eksposisi Arsitektur & Demonstrasi Konsol/CLI (`85'`)** · **Studio Desain / Latihan Terbimbing (`35'`)** · **Refleksi & Penugasan (`15'`)**, diikuti `PT 180'` & `BM 180'`. |
| **Fokus Keilmuan (*In-Scope*)** | Model layanan & *deployment cloud* (AWS/GCP/Azure), virtualisasi vs kontainer **Docker & Docker Compose**, komputasi & penyimpanan awan, **VPC Subnetting, Security Group, & IAM**, serta arsitektur **High Availability, Load Balancing, Auto-Scaling, & FinOps**. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** mengajarkan otomasi *CI/CD Pipeline* penuh, *Infrastructure as Code* Terraform/Ansible, maupun administrasi klaster Kubernetes (ranah **`STB-601 Arsitektur Cloud & DevOps`**), serta audit tata kelola ISO 27001/COBIT mendalam (`STB-701`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti & Aktivitas Studio Cloud (`150'`) | Waktu | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Karakteristik **NIST Cloud**, **CapEx vs OpEx**, & Topologi Global (*Region, AZ, Edge*) | 150' | Formatif |
| **2** | `Sub-CPMK-1.1` | Spektrum **IaaS, PaaS, SaaS, FaaS**, *Shared Responsibility*, & Peta **AWS / GCP / Azure** | 150' | Formatif |
| **3** | `Sub-CPMK-1.1, 1.2` | Model Deployment (*Public/Private/Hybrid/Multi-Cloud*) & **Hypervisor Type-1 vs Type-2** | 150' | Formatif |
| **4** | `Sub-CPMK-1.2` | Komparasi **Virtual Machines vs Containers** (*Namespaces/cgroups*) & Evaluasi **Tugas 1** | 150' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Arsitektur **Docker Engine**, Siklus Kontainer, & Konstruksi **Dockerfile** | 150' | Formatif |
| **6** | `Sub-CPMK-2.2` | Optimasi **Layer Caching**, **Multi-Stage Builds**, Keamanan *Image*, & **Container Registry** | 150' | Formatif |
| **7** | `Sub-CPMK-2.1` | Persistensi *Docker Volumes*, Jaringan Internal, **Docker Compose**, & Klinik UTS | 150' | Formatif |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** Analisis Virtualisasi & Rekayasa Konfigurasi Docker | 120' | **UTS (30%)** |
| **9** | `Sub-CPMK-3.1` | *Provisioning* **Cloud VM** (*EC2/GCE*), Model Harga (*Spot/Reserved*), & *Bootstrap Script* | 150' | Formatif |
| **10** | `Sub-CPMK-3.1` | **Block vs File vs Object Storage (*S3/GCS*)**, *Lifecycle Policy*, & *Managed Database* | 150' | Formatif |
| **11** | `Sub-CPMK-3.2` | Jaringan Virtual **VPC**, **Public vs Private Subnetting**, *IGW, NAT,* & *Route Tables* | 150' | Formatif |
| **12** | `Sub-CPMK-3.2` | **Security Group vs NACL**, **IAM Least Privilege**, & Verifikasi **Tugas 2** | 150' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-4.1` | Desain *Stateless*, **Layer-4 vs Layer-7 Load Balancing**, & **Horizontal Auto-Scaling** | 150' | Formatif |
| **14** | `Sub-CPMK-4.2` | Matematika SLA, Arsitektur **Multi-AZ High Availability**, Eliminasi SPOF, & **RTO/RPO** | 150' | Formatif |
| **15** | `Sub-CPMK-4.1, 4.2` | Observabilitas, **Cloud FinOps / Pricing Calculator**, & Review **Well-Architected** Pra-UAS | 150' | Formatif |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang Cetak Biru Arsitektur Cloud HA & *Chaos Q&A* | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN

### PERTEMUAN 1 — Definisi **NIST Cloud**, Ekonomi **CapEx vs OpEx**, & Infrastruktur Global
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Aktivitas (`150'`):** Menganalisis mengapa pembelian server fisik kapasitas puncak menyebabkan pemborosan 85% di hari biasa (*over-provisioning*) atau tumbang saat lonjakan (*under-provisioning*); membedah 5 karakteristik NIST, struktur *Region $\rightarrow$ Availability Zone (AZ) terpisah puluhan km dengan serat optik latensi rendah $\rightarrow$ Point of Presence/CDN*, serta aturan penempatan data di Region Indonesia sesuai UU PDP.
* **PT (`180'`) & BM (`180'`):** Menghitung perbandingan arus kas 3 tahun *On-Premise CapEx* vs *Cloud OpEx*.

### PERTEMUAN 2 — **IaaS, PaaS, SaaS, FaaS**, *Shared Responsibility Model*, & Peta **AWS / GCP / Azure**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Aktivitas (`150'`):** Membandingkan tingkat kendali vs beban operasional dari *Bare Metal $\rightarrow$ IaaS $\rightarrow$ CaaS $\rightarrow$ PaaS $\rightarrow$ FaaS (Serverless Event-Driven) $\rightarrow$ SaaS*; membedah **Shared Responsibility Model** (*Security OF the Cloud* milik vendor vs *Security IN the Cloud* milik pelanggan) dan memetakan katalog layanan inti lintas **AWS, Google Cloud, dan Microsoft Azure**.
* **PT (`180'`) & BM (`180'`):** Menyusun tabel padanan 10 layanan utama di AWS, GCP, dan Azure.

### PERTEMUAN 3 — Model Deployment (*Public, Private, Hybrid, Multi-Cloud*) & **Hypervisor Type-1 vs Type-2**
* **Sub-CPMK:** `Sub-CPMK-1.1` & `1.2` [C4] · **Aktivitas (`150'`):** Mengevaluasi skenario kapan rumah sakit/bank wajib memakai arsitektur **Hybrid Cloud** atau menghindari *vendor lock-in* lewat **Multi-Cloud**; dilanjutkan bedah mesin di balik layar *cloud*: bagaimana **Type-1 Bare-Metal Hypervisor** (*KVM, AWS Nitro, VMware ESXi*) memvirtualisasikan CPU/RAM dengan *hardware-assisted virtualization* dibanding *Type-2 Hosted Hypervisor*. Merilis resmi **Tugas 1 (RTM-1)**.
* **PT (`180'`) & BM (`180'`):** Mengerjakan analisis migrasi *cloud* enterprise pada **Tugas 1**.

### PERTEMUAN 4 — **Virtual Machines vs Containers** (*Linux Namespaces & cgroups*) + Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Aktivitas (`150'`):** Menghubungkan materi kernel `STI-310 Sistem Operasi`: mengapa VM membawa *Guest OS* gigabita dan butuh puluhan detik untuk menyala, sedangkan **Container** berbagi kernel *Host OS* menggunakan isolasi pandangan **Linux Namespaces** (`pid, net, mnt, user`) dan pembatasan kuota **cgroups** sehingga menyala dalam milidetik; dilanjutkan presentasi dan diskusi kritis **Tugas 1 (`CPMK-1`)**.
* **PT (`180'`) & BM (`180'`):** Memasang Docker Engine/Desktop untuk studio kontainerisasi pekan ke-5.

### PERTEMUAN 5 — Arsitektur **Docker Engine** & Konstruksi **Dockerfile** Portabel
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3→C4] · **Aktivitas (`150'`):** Membedah komponen *Docker Client, Docker Daemon (`containerd`), Image Layers,* dan *Running Container*; mendemonstrasikan serta melatih penyusunan **Dockerfile** bersih (`FROM, WORKDIR, COPY, RUN, ENV, EXPOSE, USER, CMD/ENTRYPOINT`) yang membungkus aplikasi web sehingga kutukan *"di laptop saya jalan kok!"* tamat selamanya.
* **PT (`180'`) & BM (`180'`):** Mengemas satu aplikasi API sederhana ke dalam `Dockerfile` dan menguji pemetaan port serta variabel lingkungan.

### PERTEMUAN 6 — Optimasi **Layer Caching**, **Multi-Stage Builds**, & **Container Registry**
* **Sub-CPMK:** `Sub-CPMK-2.2` [C4] · **Aktivitas (`150'`):** Membongkar kesalahan klasik pemula yang menaruh `COPY . .` sebelum `RUN npm ci / pip install` sehingga setiap ganti 1 huruf kode memaksa unduh ulang seluruh pustaka! Melatih teknik **Multi-Stage Build** (memisahkan *builder stage* berisi kompilator berat dari *runtime stage* ramping `alpine/slim/distroless`), akun *non-root*, `.dockerignore`, serta mengunggah *image* ber-tag versi semantik ke **Container Registry** (*GHCR / Docker Hub / Cloud Artifact Registry*).
* **PT (`180'`) & BM (`180'`):** Mengoptimalkan *image* aplikasi dari $>800\text{ MB}$ menjadi $<120\text{ MB}$.

### PERTEMUAN 7 — Persistensi *Volumes*, Jaringan Kontainer, & **Docker Compose** + Klinik UTS
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Aktivitas (`150'`):** Mengapa seluruh data di dalam kontainer lenyap saat `docker rm` dijalankan? Membedah *Ephemeral Writable Layer* vs **Named Volumes** & *Bind Mounts*, resolusi DNS otomatis antar-nama layanan pada *User-Defined Bridge Network*, dan orkestrasi tumpukan utuh (`nginx + backend + postgres + redis`) dalam `docker-compose.yml` lengkap `depends_on: condition: service_healthy`; diakhiri klinik simulasi **UTS Pekan 8**.
* **PT (`180'`) & BM (`180'`):** Persiapan mandiri menghadapi UTS konfigurasi dan optimasi kontainer.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]) · **Bobot:** **30%** · **Durasi:** `120 menit`.
* **Pelaksanaan:** Menguji ketajaman analisis virtualisasi vs kontainer, audit & penyusutan ukuran `Dockerfile` melalui *layer caching* & *multi-stage build*, serta perancangan `docker-compose.yml` multi-layanan dan alur *Container Registry*.

### PERTEMUAN 9 — *Provisioning* **Cloud Virtual Machines**, Model Harga, & *Bootstrap Automation*
* **Sub-CPMK:** `Sub-CPMK-3.1` [C3] · **Aktivitas (`150'`):** Evaluasi UTS lalu masuk ke infrastruktur awan publik: memilih spesifikasi vCPU/RAM (*Compute/Memory Optimized*), perbedaan drastis biaya *On-Demand* vs *Reserved/Savings Plan* (hemat s.d. 72%) vs *Spot/Preemptible Instances* (hemat s.d. 90% untuk beban kerja *fault-tolerant*), autentikasi kunci SSH asimetris, dan otomasi inisialisasi server saat penyalaan pertama menggunakan *User-Data / Startup Script* + pemasangan **Billing Budget Alert** wajib!
* **PT (`180'`) & BM (`180'`):** Menulis skrip `cloud-init` pembangun server web otomatis tanpa login SSH manual.

### PERTEMUAN 10 — **Block vs File vs Object Storage (*S3/GCS*)** & Basis Data Terkelola (*Managed RDS*)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C3] · **Aktivitas (`150'`):** Membedah tiga pilar penyimpanan awan: *Block Storage* (EBS untuk disk sistem/DB satu VM), *Shared File Storage* (EFS/Filestore NFS lintas VM), dan primadona awan **Object Storage** (*Amazon S3 / Google Cloud Storage* berdaya tahan `99,999999999%` [11 *nines*]), konfigurasi *Block Public Access*, *Pre-Signed URL* untuk unggah/unduh berkas aman, *Lifecycle Policy* pengarsipan otomatis, serta perbandingan mengelola PostgreSQL sendiri di VM vs **Managed RDS / Cloud SQL**. Merilis resmi **Tugas 2 (RTM-2)**.
* **PT (`180'`) & BM (`180'`):** Merancang kebijakan penyimpanan dan siklus hidup objek pada **Tugas 2**.

### PERTEMUAN 11 — Jaringan Virtual **VPC**, **Public vs Private Subnetting**, *IGW, NAT,* & *Route Tables*
* **Sub-CPMK:** `Sub-CPMK-3.2` [C3] · **Aktivitas (`150'`):** Mengaplikasikan langsung keterampilan CIDR `STI-312` ke arsitektur **Virtual Private Cloud (VPC)**: membagi blok `10.20.0.0/16` menjadi *Public Subnets* dan *Private Subnets* lintas 2 *Availability Zones*, membedah mengapa basis data **harus selalu berada di Private Subnet** tanpa IP publik, bagaimana server di *Private Subnet* mengunduh pembaruan keamanan keluar via **NAT Gateway** tanpa bisa dimasuki dari luar, serta penelusuran **Route Tables**.
* **PT (`180'`) & BM (`180'`):** Menyusun tabel pengalamatan CIDR 4 *subnet* lintas 2 AZ untuk **Tugas 2**.

### PERTEMUAN 12 — Pertahanan Berlapis **Security Group vs NACL** & **IAM Least Privilege** + Evaluasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.2` [C3] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 20%)** · **Aktivitas (`150'`):** Membandingkan *Virtual Firewall* tingkat *instance* **Security Group** (*stateful, allow-only, security-group chaining*) vs tingkat *subnet* **Network ACL** (*stateless, allow & deny*); dilanjutkan prinsip nomor satu keamanan *cloud*: **Identity and Access Management (IAM)** — penguncian *Root Account* dengan MFA, larangan mutlak menaruh `AWS_ACCESS_KEY_ID` di GitHub (gunakan *IAM Instance Profile / Workload Identity Role*!), pembacaan dokumen JSON Policy (`Effect, Action, Resource, Condition`), serta verifikasi pengumpulan **Tugas 2 (`CPMK-3`)**.
* **PT (`180'`) & BM (`180'`):** Membentuk tim (maks. 3 orang) untuk proyek akhir perancangan arsitektur **UAS**.

### PERTEMUAN 13 — Arsitektur *Stateless*, **Elastic Load Balancing**, & **Horizontal Auto-Scaling**
* **Sub-CPMK:** `Sub-CPMK-4.1` [C5] · **Aktivitas (`150'`):** Mengevaluasi batas *Vertical Scaling* (*scale-up* mentok ukuran mesin & butuh *downtime*) vs *Horizontal Scaling* (*scale-out* menambah/mengurangi jumlah mesin otomatis); membedakan *Layer-4 Network Load Balancer* vs *Layer-7 Application Load Balancer* (*path/host routing, TLS termination, health check*), aturan wajib aplikasi *stateless* (penyimpanan berkas di S3 & sesi di Redis), serta perancangan kebijakan **Auto-Scaling Group** (*Target Tracking, Step Scaling, Scheduled Scaling* menjelang jadwal KRS/lebaran).
* **PT (`180'`) & BM (`180'`):** Merancang kebijakan *Load Balancing* dan *Auto-Scaling* proyek akhir UAS.

### PERTEMUAN 14 — Matematika Ketersediaan, **Multi-AZ High Availability**, & **Disaster Recovery (RTO/RPO)**
* **Sub-CPMK:** `Sub-CPMK-4.2` [C5] · **Aktivitas (`150'`):** Menghitung ketersediaan sistem seri ($A_{\text{total}} = A_1 \times A_2$) vs paralel redundan ($A_{\text{total}} = 1 - (1-A_1)(1-A_2)$) dan arti nyata waktu henti tahunan antara **SLA 99% (3,65 hari/tahun)** vs **99,99% (52,6 menit/tahun)**; membedah cara meniadakan seluruh **Single Point of Failure (SPOF)** menggunakan *Multi-AZ Load Balancer, Multi-AZ Auto-Scaling App Tier,* dan *Multi-AZ Synchronous Standby Database + Read Replicas*, serta spektrum pemulihan bencana berdasarkan target **Recovery Time Objective (RTO)** & **Recovery Point Objective (RPO)**.
* **PT (`180'`) & BM (`180'`):** Menggambar diagram arsitektur lengkap *Multi-AZ High Availability* proyek UAS.

### PERTEMUAN 15 — Observabilitas Cloud, **Cloud FinOps (*Pricing Calculator*)**, & Klinik **Well-Architected** Pra-UAS
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C5] · **Aktivitas (`150'`):** Mengajarkan pemantauan kesehatan infrastruktur (*CloudWatch / Cloud Operations: CPU, Latency, 5xx Error Rate, Billing Alarms*) dan disiplin rekayasa biaya **Cloud FinOps** menggunakan *AWS / GCP Pricing Calculator* (menghitung biaya tersembunyi *NAT Gateway & Data Egress* yang sering mengejutkan perusahaan!); melaksanakan *peer review* cetak biru proyek UAS terhadap 6 pilar **Cloud Well-Architected Framework**, serta menjelaskan *handoff* menuju `STB-601 Arsitektur Cloud & DevOps` (di mana seluruh arsitektur ini akan diotomasi dengan *Terraform & Kubernetes*).
* **PT (`180'`) & BM (`180'`):** Finalisasi dokumen cetak biru arsitektur *cloud*, lembar rincian biaya bulanan, dan kesiapan sidang *chaos defense* UAS.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Dokumen *Cloud High-Availability Architecture Blueprint & Cost Model* (50% nilai UAS)** dengan **Sidang *Chaos Failure Injection Defense* Individu (50% nilai UAS)** di mana dosen menyuntikkan skenario kegagalan komponen/lonjakan beban secara spontan untuk menguji ketangguhan rancangan.
