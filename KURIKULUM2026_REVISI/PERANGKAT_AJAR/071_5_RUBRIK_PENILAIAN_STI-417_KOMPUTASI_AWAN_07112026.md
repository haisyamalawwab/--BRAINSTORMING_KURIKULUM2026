# 071_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-417 — KOMPUTASI AWAN (*Cloud Computing*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.5.RPS-STI417` · **Klaster Rubrik Master (Dok 018):** Klaster 3 (`K-3`)  
**CPL:** `CPL-07` (`P3` = 45%) & `CPL-11` (`KK3` = 55%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN ARSITEKTUR & REKAYASA KOMPUTASI AWAN (`K-3`)

Mengacu **Dokumen 018 §3 (Klaster `K-3`)**, penilaian pada `STI-417` mengukur ketepatan pemilihan model layanan/*deployment cloud*, efisiensi dan portabilitas pengemasan kontainer **Docker**, ketelitian isolasi jaringan **VPC** dan pembatasan hak akses **IAM Least Privilege**, serta ketangguhan rancangan arsitektur **High Availability, Load Balancing, & Auto-Scaling** yang bebas *Single Point of Failure* dan rasional secara biaya (*FinOps*).

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-07` [C4])
**Objek Penilaian:** Studi Kasus Strategi Layanan/Deployment Cloud (**AWS/GCP/Azure**) & Analisis **Hypervisor vs Container**.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Perbandingan Model Layanan (*IaaS/PaaS/SaaS/FaaS*) & Deployment**<br>(`Sub-CPMK-1.1`) | **55%** | Pemetaan tiap beban kerja ke *IaaS/PaaS/SaaS/FaaS* dan *Public/Hybrid* sangat tepat (termasuk kepatuhan *Data Residency* UU PDP), matriks layanan AWS/GCP/Azure & *Shared Responsibility* akurat 100%. | Pemilihan model layanan, model *deployment*, dan padanan layanan lintas vendor relevan dan terjustifikasi baik. | Mampu membedakan IaaS, PaaS, dan SaaS secara benar, namun justifikasi FaaS atau *Shared Responsibility* masih umum. | Salah kaprah menempatkan semua beban kerja di satu VM tunggal atau keliru memahami tanggung jawab keamanan pelanggan. | Tidak mampu membedakan model layanan dan *deployment cloud*. |
| **2. Analisis Virtualisasi **Hypervisor vs Container** & Ekonomi TCO**<br>(`Sub-CPMK-1.2`) | **45%** | Menganalisis tajam perbedaan teknis *Type-1/2 Hypervisor* vs *OS-Level Containers* (*namespaces/cgroups*) serta menyajikan perbandingan finansial *CapEx vs OpEx* yang realistis. | Analisis perbandingan VM vs Kontainer dan perhitungan ekonomi migrasi *cloud* disusun dengan benar. | Penjelasan perbedaan VM dan kontainer cukup benar secara konseptual dasar. | Menganggap kontainer membawa kernel OS penuh seperti VM atau salah total menghitung biaya dasar. | Bagian analisis virtualisasi dan TCO tidak dikerjakan. |

$$\text{Skor Tugas 1} = 0,55(K_1) + 0,45(K_2)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `CPMK-2` / `CPL-07` [15%] & `CPL-11` [15%] [C4])
**Objek Penilaian:** Ujian Terawasi: Konstruksi **Dockerfile & Docker Compose** serta Optimasi **Multi-Stage & Layer Caching**.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Implementasi **Dockerfile, Docker Compose,** & Registry**<br>(`Sub-CPMK-2.1` → `CPL-11`) | **50%**<br>*(15% MK)* | `Dockerfile` dan `docker-compose.yml` multi-layanan tersusun sempurna lengkap *Named Volume* persisten, jaringan internal terisolasi, *healthcheck*, dan perintah versi *Container Registry* yang tepat. | Konfigurasi `Dockerfile` dan `docker-compose.yml` valid, melayani komunikasi antar-kontainer dan persistensi volume dengan benar. | Sintaks dasar `Dockerfile` dan `Compose` benar, namun basis data masih diekspos terbuka ke host atau belum memakai `healthcheck`. | Kesalahan sintaks fatal (`CMD/RUN` tertukar) atau data basis data hilang setiap kontainer dimatikan karena tanpa volume. | Tidak mampu menulis konfigurasi `Dockerfile` maupun `Docker Compose`. |
| **2. Analisis Virtualisasi & Optimasi **Multi-Stage / Layer Caching****<br>(`Sub-CPMK-2.2` → `CPL-07`) | **50%**<br>*(15% MK)* | Mengidentifikasi seluruh cacat `Dockerfile` buruk dengan presisi dan menulis ulang **Multi-Stage Build** berurutan *cache-friendly*, `.dockerignore` ketat, serta pengguna *non-root*. | Menerapkan *multi-stage build* dan urutan penyalinan manifes dependensi yang memanfaatkan *layer caching* secara benar. | Memahami konsep dasar pengurangan ukuran *base image* (`alpine/slim`), namun urutan baris masih membatalkan *cache* dependensi. | Tidak mampu membedakan *build stage* dan *runtime stage* atau tetap menjalankan kontainer sebagai `root` dengan berkas rahasia ikut tersalin. | Gagal menjawab bagian analisis dan optimasi kontainer. |

$$\text{Skor UTS} = 0,50(K_{2.1}) + 0,50(K_{2.2})$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-3` / `CPL-11` [C3])
**Objek Penilaian:** Konfigurasi **Virtual Machine, Object Storage**, Jaringan **VPC Subnetting, Security Group,** & **IAM**.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. *Provisioning* **VM** & Konfigurasi Aman **Object Storage****<br>(`Sub-CPMK-3.1`) | **40%** | Spesifikasi VM tepat guna (*right-sized*) dengan *bootstrap script* & kunci SSH; bucket *Object Storage* mengaktifkan *Block Public Access*, enkripsi, dan *Lifecycle Policy* yang presisi. | Pembuatan VM dan konfigurasi penyimpanan objek beserta siklus hidupnya berjalan benar dan aman. | VM dan bucket penyimpanan berhasil dikonfigurasi secara fungsional dasar. | Membuka bucket *Object Storage* menjadi publik penuh (`0.0.0.0/0` baca-tulis!) atau login VM dengan kata sandi lemah. | Gagal mengonfigurasi sumber daya komputasi dan penyimpanan. |
| **2. Topologi **VPC Subnetting**, **Security Group**, & **IAM Least Privilege****<br>(`Sub-CPMK-3.2`) | **60%** | Pembagian CIDR *Public/Private Subnet* lintas AZ, *Route Table/IGW/NAT*, rantai **Security Group**, dan JSON Policy **IAM Role** (*Least Privilege*) 100% akurat tanpa celah paparan publik. | Konfigurasi subnet VPC, aturan *Security Group*, dan pembatasan hak akses IAM disusun dengan benar dan aman. | Pemisahan subnet dasar ada, namun aturan *Security Group* atau cakupan `Resource` pada IAM Policy masih agak longgar. | Menaruh basis data di *Public Subnet* dengan port `0.0.0.0/0` terbuka **ATAU** memberikan izin `Action: "*", Resource: "*"` (*AdministratorAccess* membabi buta!). | Topologi jaringan VPC tidak valid dan tanpa kontrol akses IAM. |

$$\text{Skor Tugas 2} = 0,40(K_1) + 0,60(K_2)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-07` [10%] & `CPL-11` [20%] [C5])
**Objek Penilaian:** Cetak Biru **Arsitektur Cloud High Availability, Load Balancing, Auto-Scaling, & Cost Model** + Sidang *Chaos Defense*.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Evaluasi **Load Balancing, Auto-Scaling,** & Biaya *FinOps***<br>(`Sub-CPMK-4.1` → `CPL-07`) | **33,33%**<br>*(10% MK)* | Evaluasi kapasitas, desain *stateless* di balik L7 **Load Balancer**, metrik pemicu **Auto-Scaling**, serta rincian *Cloud Pricing Calculator* (termasuk biaya trafik/NAT & strategi hemat) sangat tajam dan realistis. | Konfigurasi *Load Balancing*, kebijakan *Auto-Scaling*, dan estimasi biaya bulanan dihitung secara logis dan lengkap. | Menyertakan komponen *Load Balancer*, *Auto-Scaling* dasar, dan perkiraan harga komponen utama. | Aplikasi masih menyimpan sesi/berkas di disk lokal VM sehingga rusak saat *Auto-Scaling*, atau tanpa perhitungan biaya. | Tidak melakukan evaluasi skalabilitas maupun estimasi biaya. |
| **2. Rancangan Arsitektur **High Availability Multi-AZ**, DR, & Sidang**<br>(`Sub-CPMK-4.2` → `CPL-11`) | **66,67%**<br>*(20% MK)* | Diagram arsitektur **Multi-AZ** 100% bebas **Single Point of Failure**, perhitungan SLA komposit & strategi **RTO/RPO** presisi, dan mahasiswa sangat tangguh menjawab seluruh skenario kegagalan saat sidang *chaos defense*. | Arsitektur memenuhi kaidah *High Availability* lintas AZ di lapisan aplikasi & basis data serta anggota mampu mempertahankan rancangannya saat sidang. | Arsitektur menggandakan server aplikasi lintas AZ, namun lapisan basis data/NAT masih menyisakan satu titik rawan tunggal. | Arsitektur hanya berjalan di satu *Availability Zone* penuh SPOF dan gagal menjawab dampak kegagalan saat sidang. | Tidak menyerahkan cetak biru arsitektur atau tidak hadir sidang UAS. |

$$\text{Skor UAS} = \frac{1}{3}(K_{4.1}) + \frac{2}{3}(K_{4.2})$$

---

## BAGIAN III — RUBRIK FORMATIF AKTIVITAS STUDIO CLOUD MINGGUAN

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketepatan Latihan Studio & Disiplin Clean-Up** | Menyelesaikan latihan Docker/Cloud tepat, serta disiplin mematikan sumber daya berbayar pasca-latihan (*zero orphaned resources*). | Menyelesaikan latihan mingguan dengan benar dan tertib. | Menyelesaikan sebagian besar latihan dengan panduan. | Tidak mengikuti latihan studio atau meninggalkan sumber daya *sandbox* menyala liar. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-417` (`CPL-07` & `CPL-11` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai analisis strategis multi-cloud, mahir mengemas kontainer **Docker** berefisiensi tinggi, cermat mengamankan **VPC & IAM Least Privilege**, serta mampu merancang arsitektur **Multi-AZ High Availability & Auto-Scaling** berstandar *Well-Architected* lengkap disiplin *FinOps*. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa mampu membandingkan layanan AWS/GCP/Azure, membangun `Dockerfile` & `Docker Compose` optimal, mengonfigurasi VPC/Storage/IAM aman, serta menyusun arsitektur *cloud* tahan gagal. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi ambang ketuntasan minimal OBE ($\ge 65,0$) dalam pemahaman model *cloud*, pengemasan kontainer Docker dasar, konfigurasi VM/VPC standar, dan perancangan *Load Balancing* dasar. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih keliru membedakan model layanan *cloud*, membuat kontainer tidak portabel, membiarkan *subnet*/penyimpanan terbuka ke publik, atau merancang arsitektur penuh SPOF. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai kompetensi dasar komputasi awan atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-417` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu membandingkan model layanan (**IaaS, PaaS, SaaS, FaaS**) dan *deployment* pada **AWS / GCP / Azure**. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menganalisis perbedaan arsitektur virtualisasi *Hypervisor* dan kontainerisasi tingkat sistem operasi. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu mengemas aplikasi portabel menggunakan **Dockerfile**, **Docker Compose**, dan **Container Registry**. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu mengoptimalkan ukuran *image* kontainer dengan **multi-stage build** dan **layer caching**. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu melakukan *provisioning* **Virtual Machine** dan mengonfigurasi **Object Storage** di *cloud*. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu mengonfigurasi **VPC, Subnetting, Security Group,** dan manajemen akses **IAM** secara aman. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu mengevaluasi kebutuhan **Load Balancing**, **Auto-Scaling**, dan efisiensi biaya beban kerja *cloud*. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu merancang arsitektur *cloud* **High Availability (*Multi-AZ*)** yang bebas *Single Point of Failure*. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-417`)

```text
====================================================================================================================================
     LEMBAR REKAPITULASI PENILAIAN OBE — STI-417 KOMPUTASI AWAN (3 SKS TEORI: T=3, P=0)
====================================================================================================================================
Semester / TA  : Semester 4 (Genap) / 2026-2027      CPL Dibebankan : CPL-07 (P3: 45%) & CPL-11 (KK3: 55%) [Level: Reinforce]
Klaster Rubrik : K-3 (AI, Cloud & Cybersecurity)     Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mhs     | T1(20%) | UTS:2.1(15%)| UTS:2.2(15%)| T2(20%) | UAS:4.1(10%)| UAS:4.2(20%)| NA    | CPL-07 | CPL-11
   |           |              | [1:P3]  | [2:KK3]     | [2:P3]      | [3:KK3] | [4:P3]      | [4:KK3]     | Akhir | (45%)  | (55%)
------------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1] | 88.0    | 86.0        | 88.0        | 90.0    | 88.0        | 90.0        | 88.50 | 88.00  | 88.91
2  | 250101002 | [Nama Mhs 2] | 78.0    | 76.0        | 78.0        | 80.0    | 78.0        | 80.0        | 78.50 | 78.00  | 78.91
3  | 250101003 | [Nama Mhs 3] | 68.0    | 66.0        | 68.0        | 70.0    | 68.0        | 70.0        | 68.50 | 68.00  | 68.91
------------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS               | 78.00   | 76.00       | 78.00       | 80.00   | 78.00       | 80.00       | 78.50 | 78.00  | 78.91
====================================================================================================================================
```
