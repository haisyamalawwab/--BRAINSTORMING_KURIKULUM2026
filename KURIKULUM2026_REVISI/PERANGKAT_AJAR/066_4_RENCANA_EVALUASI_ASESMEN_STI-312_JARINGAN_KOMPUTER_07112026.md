# 066_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-312 — JARINGAN KOMPUTER (*Computer Networks*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI312` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 3  
**Klaster Asesmen MK (Dok 018):** Klaster 3 (`K-3`) — Infrastruktur, Jaringan, Keamanan & Sistem Operasi  
**CPL Dibebankan:** `CPL-07` (`P3` = **45%**) & `CPL-11` (`KK3` = **55%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 008, 018,** dan **043**, mata kuliah berpraktikum `STI-312 Jaringan Komputer` (3 SKS `+P`) menerapkan skema bobot baku MK `+P` (`20% / 25% / 25% / 30%`) dengan korespondensi 1-ke-1 ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-07` / `P3`)** — *Case-Based Wireshark Multi-Layer Packet Encapsulation Analysis*.
* **UTS (Pekan 8 — 25%) → `CPMK-2` (`CPL-07` / `P3`)** — *Organization Multi-Division IPv4 (VLSM/CIDR) & IPv6 Addressing Design Exam*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3` (`CPL-11` / `KK3`)** — *Case-Based VLAN, 802.1Q Trunking, & Static/OSPF Routing Configuration + Live Troubleshooting*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-11` / `KK3`)** — *Project-Based Enterprise Network Services (DNS, DHCP, HTTP, NAT) & ACL Firewall Policy + Individual Practical Exam*.
* **Kepatuhan IKU 7 ($\ge 55\%$ untuk Klaster `K-3` Dok 018):** `Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75%` berbasis pemecahan kasus jaringan nyata dan proyek infrastruktur terverifikasi *(persis selaras dengan angka tabel IKU 7 Dokumen 004 untuk `STI-312` = 75%)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-07`**<br>(`P3` — 45%)<br>*Level: R* | **`CPMK-1`**<br>(C4) | `Sub-CPMK-1.1` | Mg 4 | Analisis paket individu: Pemetaan enkapsulasi PDU lintas lapisan **OSI (7 Layer)** dan **TCP/IP** | **RTM-1 (Tugas 1)** Bagian Enkapsulasi + Rubrik T1 | Sumatif | 10% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Analisis paket individu + uji filter lab 20': Bedah lalu lintas *ARP, TCP 3-Way Handshake, UDP/DNS, HTTP* di **Wireshark** | **RTM-1 (Tugas 1)** Bagian Wireshark + Uji Lab + Rubrik T1 | Sumatif | 10% | |
| **`CPL-07`**<br>(`P3` — 45%)<br>*Level: R* | **`CPMK-2`**<br>(C3) | `Sub-CPMK-2.1` | Mg 8 | Ujian tertulis studi kasus: Perancangan skema **IPv4 (*VLSM/CIDR*)** multi-divisi efisien bebas konflik | **Naskah Soal UTS** (Bagian IPv4 VLSM) + Rubrik Analitik UTS | Sumatif | 16% | **25%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Ujian tertulis studi kasus: Perancangan skema pengalamatan **IPv6** dasar multi-subnet tanpa konflik | **Naskah Soal UTS** (Bagian IPv6) + Rubrik Analitik UTS | Sumatif | 9% | |
| **`CPL-11`**<br>(`KK3` — 55%)<br>*Level: R* | **`CPMK-3`**<br>(C3) | `Sub-CPMK-3.1` | Mg 12 | Penugasan simulator + verifikasi lab: Konfigurasi **VLAN, 802.1Q Trunking,** & *Inter-VLAN Routing* | **RTM-2 (Tugas 2)** + Uji Lab + Rubrik Analitik T2 | Sumatif | 12% | **25%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Penugasan simulator + *live troubleshooting*: Konfigurasi *Static Routing* & **OSPF** hingga konektivitas *end-to-end* 100% | **RTM-2 (Tugas 2)** + *Trouble Ticket* Lab + Rubrik T2 | Sumatif | 13% | |
| **`CPL-11`**<br>(`KK3` — 55%)<br>*Level: R* | **`CPMK-4`**<br>(C4) | `Sub-CPMK-4.1` | Mg 16 | Proyek topologi organisasi + ujian praktik lab: Konfigurasi fungsional **DNS, DHCP (+ Relay), HTTP,** & **NAT/PAT** | **Topologi Proyek UAS** & Ujian Praktik Lab + Rubrik UAS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Proyek topologi organisasi + ujian praktik lab: Konfigurasi kebijakan *firewall* **Standard & Extended ACL** pengaman segmen lokal | **Matriks Uji ACL UAS** & Ujian Praktik Lab + Rubrik UAS | Sumatif | 15% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/25/25/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Analisis Enkapsulasi OSI/TCP-IP dengan Wireshark)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Uji Praktik Filter **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-07`).
* **Objek & Batasan Pengerjaan Individu:**
  1. Mahasiswa menangkap sendiri lalu lintas jaringan perangkatnya (disertai penanda permintaan berparameter NIM) dan menganalisis 1 berkas skenario studi kasus `.pcapng` yang disediakan dosen.
  2. Membedah secara detail proses enkapsulasi lintas **OSI 7-Layer** dan **TCP/IP** pada paket **ARP, DNS (UDP), ICMP, TCP (*3-Way Handshake* + urutan nomor *Sequence/Ack*),** dan **HTTP**, lalu mengikuti tes praktik 20 menit di laboratorium menjawab soal langsung dengan *Wireshark Display Filters*.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Perancangan Pengalamatan IPv4 VLSM & IPv6)
* **Format & Bobot:** Ujian Tertulis Luring Terjadwal (*Closed-Book*, **150 menit**) · Bobot **25%** (`CPMK-2` → `CPL-07`).
* **Rincian Soal:**
  1. **(65% skor UTS — `Sub-CPMK-2.1`):** Diberikan profil organisasi multi-gedung (7 segmen LAN dengan kebutuhan host bervariasi antara 8 hingga 220 host + 3 tautan antar-router WAN) dan satu blok prefix IPv4 utama; mahasiswa wajib menyusun tabel lengkap **VLSM/CIDR** (*Subnet Name, Needed Hosts, Allocated Size, Network ID, Prefix/Mask, Usable Host Range, Broadcast ID*) tanpa satu pun tumpang tindih serta menghitung *route summarization*-nya.
  2. **(35% skor UTS — `Sub-CPMK-2.2`):** Berdasarkan prefix organisasi IPv6 `/48` yang diberikan, mahasiswa merancang tabel subnetting **IPv6 `/64`** untuk seluruh divisi dan tautan router (dalam bentuk terkompresi baku), menentukan alamat *Link-Local*, serta menjelaskan mekanisme pembentukan alamat host tanpa konflik.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Konfigurasi VLAN, Trunking, & Routing OSPF)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Uji *Troubleshooting* Lab **Pekan 12** · Bobot **25%** (`CPMK-3` → `CPL-11`).
* **Objek & Batasan Pengerjaan Individu:**
  1. Mengonfigurasi topologi kampus/perusahaan multi-cabang (minimal 3 router dan 3 switch dengan parameter IP berdasarkan NIM) yang menerapkan **VLSM**, 4 **VLAN**, tautan **802.1Q Trunking**, **Inter-VLAN Routing**, **Default Route**, dan protokol dinamis **OSPF** berjalur redundan.
  2. Seluruh pasangan host lintas cabang wajib terverifikasi `ping` 100% sukses dan tetap terhubung saat salah satu jalur utama OSPF diputus. Saat pengumpulan di lab Pekan 12, mahasiswa wajib menyelesaikan tantangan perbaikan cepat 2 *trouble tickets* langsung di simulator.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Layanan Jaringan & Pengamanan Segmen ACL)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-11`), memadukan **Proyek Infrastruktur Jaringan Organisasi (50% nilai UAS)** + **Ujian Praktik Konfigurasi & Verifikasi Individu di Lab (50% nilai UAS, 150 menit)**:
  1. **Layanan Infrastruktur (`Sub-CPMK-4.1`):** Topologi menyediakan distribusi alamat otomatis **DHCP** lintas VLAN melalui `ip helper-address`, resolusi nama domain internal **DNS** menuju server **HTTP**, **PAT (*NAT Overload*)** dari seluruh LAN internal ke jaringan ISP simulasi, serta **Static NAT** untuk mempublikasikan server web DMZ.
  2. **Pengamanan Segmen dengan ACL (`Sub-CPMK-4.2`):** Menerapkan minimal 3 kebijakan **Standard & Extended ACL** yang presisi (mis. memblokir penuh akses dari segmen Tamu/Publik ke VLAN Server Basis Data & Keuangan, mengizinkan hanya port TCP `80/443` & UDP `53` ke server DMZ, serta membatasi akses SSH manajemen router hanya dari subnet Admin TI), dibuktikan melalui matriks pengujian *permit* dan *deny* saat sidang dan ujian praktik individu.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-312}}$)
$$NA_{\text{STI-312}} = 0,20\,S_{\text{Tugas 1}} + 0,25\,S_{\text{UTS}} + 0,25\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004 & 008)
1. **Ketercapaian `CPL-07` (`P3` — bobot 45% MK dari `CPMK-1` [20%] + `CPMK-2` [25%]):**
   $$\text{Score}_{\text{CPL-07, STI-312}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,25\,S_{\text{UTS}}(i)}{0,45}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,45 = 1,35\text{ SKS}$).*
2. **Ketercapaian `CPL-11` (`KK3` — bobot 55% MK dari `CPMK-3` [25%] + `CPMK-4` [30%]):**
   $$\text{Score}_{\text{CPL-11, STI-312}}(i) = \frac{0,25\,S_{\text{Tugas 2}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,55}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 3 \times 0,55 = 1,65\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**.
* **Aturan Keaslian Berkas Simulator:** Seluruh `hostname` router/switch dan parameter subnet wajib sesuai kode unik NIM mahasiswa/tim; ketidakmampuan mengonfigurasi perintah dasar CLI saat verifikasi lab menggugurkan nilai berkas kiriman. Remedial diberikan maksimal 1 kali dengan plafon nilai **70,0 (B)**.
