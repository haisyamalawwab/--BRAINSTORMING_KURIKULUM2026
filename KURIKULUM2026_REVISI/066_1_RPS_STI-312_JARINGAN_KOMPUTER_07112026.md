# 066_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-312 — JARINGAN KOMPUTER (*Computer Networks*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017 · Standar IEEE 802 / IETF RFC)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI312`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Jaringan Komputer / *Computer Networks* |
| **Kode Mata Kuliah** | `STI-312` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Infrastruktur TI, Jaringan & Keamanan Siber (*Core STI*) |
| **Bobot SKS & Tipe** | **3 SKS (`+P`)** (`T = 2, P = 1`) — Tatap Muka `2×50' = 100'`, Praktikum Terbimbing `1×170' = 170'`, Penugasan Terstruktur `2×60' = 120'`, Belajar Mandiri `2×60' = 120'` per pekan |
| **Semester / Tahun Akademik** | Semester 3 (Ganjil) — Tahap Penguatan Infrastruktur Komunikasi Data (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `STI-103` Organisasi dan Arsitektur Komputer |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Bersinergi dengan `STI-310` Sistem Operasi; menjadi fondasi mutlak bagi `STI-417` Komputasi Awan, `STI-418` Dasar Keamanan Informasi, `STI-521` Internet untuk Segala (IoT), & `STB-501` Keamanan Jaringan dan Forensik Digital |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-07` (`P3` = **45%**) dan `CPL-11` (`KK3` = **55%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 3 (`K-3`)** — Infrastruktur, Jaringan, Keamanan & Sistem Operasi (Bobot MK `+P`: Tugas 1 `20%` · UTS `25%` · Tugas 2 `25%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Infrastruktur TI, Cloud & Keamanan Siber |
| **Koordinator RMK** | Ir. Bambang Suprapto, M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-07`** (`P3`) | Pengetahuan | Menguasai arsitektur komputer, sistem operasi, jaringan komputer modern, komputasi awan (*Cloud*), prinsip keamanan siber, serta integrasi sistem berbasis sensor/IoT. | **R** (*Reinforce*) | **45%** |
| **`CPL-11`** (`KK3`) | Keterampilan Khusus | Mampu merancang, mengkonfigurasi, mengamankan, dan mengelola infrastruktur jaringan, layanan komputasi awan (*Cloud/DevOps*), sistem tertanam/IoT, serta pertahanan siber proaktif. | **R** (*Reinforce*) | **55%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **menganalisis** proses enkapsulasi dan komunikasi data lintas lapisan protokol **OSI (7 Layer)** dan **TCP/IP** (*B*) menggunakan *packet analyzer* (**Wireshark**) (*C*) secara akurat (*D*). | **C4** (*Analyze*) | `CPL-07` (`P3`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **merancang** skema pengalamatan jaringan **IPv4 (*VLSM/CIDR*)** dan **IPv6** (*B*) untuk memenuhi kebutuhan organisasi multi-divisi (*C*) secara efisien tanpa konflik alamat (*D*). | **C3** (*Apply*) | `CPL-07` (`P3`) | **UTS — Pekan 8 (25%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **mengonfigurasi** *switching* (**VLAN, Trunking**) dan *routing* statis/dinamis (**OSPF**) (*B*) pada simulator/perangkat jaringan (*C*) hingga konektivitas *end-to-end* terverifikasi (*D*). | **C3** (*Apply*) | `CPL-11` (`KK3`) | **Tugas 2 — Pekan 12 (25%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **mengonfigurasi** layanan jaringan dasar (**DNS, DHCP, HTTP, NAT**) dan kebijakan *firewall* sederhana (**ACL**) (*B*) untuk mengamankan segmen jaringan lokal (*C*) secara fungsional (*D*). | **C4** (*Analyze*) | `CPL-11` (`KK3`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Menganalisis proses enkapsulasi data lintas lapisan protokol **OSI (7 Layer)** dan **TCP/IP**. | `CPMK-1` | **C4** | Mg 1–2 |
| **`Sub-CPMK-1.2`** | Menganalisis lalu lintas komunikasi paket data menggunakan *packet analyzer* (**Wireshark**). | `CPMK-1` | **C4** | Mg 3–4 |
| **`Sub-CPMK-2.1`** | Merancang skema pengalamatan **IPv4 (*VLSM/CIDR*)** untuk organisasi multi-divisi. | `CPMK-2` | **C3** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Merancang skema pengalamatan **IPv6** dasar tanpa konflik alamat. | `CPMK-2` | **C3** | Mg 7 |
| **`Sub-CPMK-3.1`** | Mengonfigurasi *switching* (**VLAN, Trunking**) pada simulator atau perangkat jaringan. | `CPMK-3` | **C3** | Mg 9–10 |
| **`Sub-CPMK-3.2`** | Mengonfigurasi *routing* statis dan dinamis (**OSPF**) hingga konektivitas terverifikasi. | `CPMK-3` | **C3** | Mg 11–12 |
| **`Sub-CPMK-4.1`** | Mengonfigurasi layanan jaringan dasar (**DNS, DHCP, HTTP, NAT**) secara fungsional. | `CPMK-4` | **C4** | Mg 13–14 |
| **`Sub-CPMK-4.2`** | Mengonfigurasi kebijakan *firewall* sederhana (**ACL**) untuk pengamanan segmen jaringan lokal. | `CPMK-4` | **C4** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Layanan Jaringan (DNS, DHCP, HTTP, NAT) & Kebijakan Keamanan ACL Segmen Lokal (C4) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: DHCP Relay, DNS Hierarchy, HTTP, Static/Dynamic NAT & PAT | Sub-CPMK-4.2: Standard & Extended ACL)
      │
[CPMK-3: Konfigurasi Switching (VLAN, 802.1Q Trunking) & Routing Statis/Dinamis OSPF (C3) — Mg 9–12 (Tugas 2 25%)]
      ▲  (Sub-CPMK-3.1: VLAN Segmentation, 802.1Q Trunk, Inter-VLAN Routing | Sub-CPMK-3.2: Static/Default Route & OSPF)
      │
[CPMK-2: Perancangan Pengalamatan Efisien IPv4 (CIDR/VLSM) & IPv6 Multi-Divisi (C3) — Mg 5–8 (UTS 25%)]
      ▲  (Sub-CPMK-2.1: Subnetting FLSM, CIDR, Hierarki VLSM Bebas Overlap | Sub-CPMK-2.2: IPv6 Global Unicast, Link-Local, SLAAC)
      │
[CPMK-1: Analisis Enkapsulasi OSI 7-Layer, TCP/IP, & Inspeksi Paket Wireshark (C4) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: Topologi, PDU Enkapsulasi OSI & TCP/IP | Sub-CPMK-1.2: Bedah ARP, ICMP, TCP 3-Way Handshake, UDP di Wireshark)
      ▲
[Fondasi Prasyarat: STI-103 Organisasi dan Arsitektur Komputer (Biner/Heksadesimal, Antarmuka I/O) + Sinergi STI-310]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-07`** (`P3`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-07` = 45%** |
| **`CPL-07`** (`P3`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **25%** | — | — | **25%** | *(20% + 25%)* |
| **`CPL-11`** (`KK3`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **25%** | — | **25%** | **`CPL-11` = 55%** |
| **`CPL-11`** (`KK3`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | *(25% + 30%)* |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **25%** | **25%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 55\%$ untuk Klaster `K-3` Dok 018):** `Tugas 1 (20% — Case-Based Wireshark Protocol Forensics) + Tugas 2 (25% — Case-Based Campus/Branch VLAN & OSPF Topology Configuration) + UAS (30% — Project-Based Enterprise Network Architecture: Services, NAT, & ACL Security Defense)` = **75%** *(persis selaras dengan angka tabel IKU 7 Dokumen 004 untuk `STI-312` = 75%)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-312 Jaringan Komputer` (3 SKS `+P`) membekali mahasiswa dengan penguasaan konsep komunikasi data berlapis dan keterampilan rekayasa jaringan tingkat organisasi. Mahasiswa mempelajari model referensi **OSI 7-Layer** dan **TCP/IP**, proses enkapsulasi/dekapsulasi *Protocol Data Unit* (PDU), inspeksi paket nyata menggunakan **Wireshark** (*Ethernet, ARP, ICMP, IP, TCP 3-Way Handshake, UDP*), perancangan ruang alamat efisien **IPv4 (*CIDR & VLSM*)** serta **IPv6** (*Dual-Stack / SLAAC*), konfigurasi *switching* lapis-2 (**VLAN, IEEE 802.1Q Trunking, Inter-VLAN Routing**), *routing* lapis-3 (**Static Routing & Dynamic OSPF**), penyediaan layanan jaringan dasar (**DHCP, DNS, HTTP, NAT/PAT**), hingga penyaringan lalu lintas menggunakan **Access Control Lists (Standard & Extended ACL)** pada simulator (*Cisco Packet Tracer / GNS3*) dan perangkat laboratorium.

* **🟢 IN-SCOPE (Wajib Diajarkan):** OSI 7-Layer & TCP/IP, enkapsulasi PDU, analisis paket **Wireshark**, dasar Ethernet (`802.3`) & pengenalan WLAN (`802.11`), perhitungan **IPv4 CIDR/VLSM** & **IPv6**, **VLAN & 802.1Q Trunking**, *Inter-VLAN Routing*, **Static Routing & OSPF**, layanan **DNS, DHCP, HTTP, NAT/PAT**, serta kebijakan keamanan segmen **ACL**.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. Dilarang membahas kriptografi asimetris mendalam, pengujian penetrasi (*pentesting*), *Intrusion Detection/Prevention System* (IDS/IPS Snort/Suricata), maupun forensik insiden siber (ranah eksklusif **`STI-418 Dasar Keamanan Informasi`**, **`STI-519 Keamanan Informasi Lanjut`**, & **`STB-501 Keamanan Jaringan dan Forensik Digital`**).
  2. Dilarang membahas penyediaan *Virtual Private Cloud* (VPC) AWS/GCP, *Cloud Load Balancer*, dan *Infrastructure as Code* (ranah **`STI-417 Komputasi Awan`** & **`STB-601 Arsitektur Cloud & DevOps`**).
  3. Dilarang mendalami teori fisika modulasi sinyal elektromagnetik RF tingkat teknik telekomunikasi murni.
* **🔄 HANDOFF ANCHOR:** Mengambil fondasi representasi biner/antarmuka dari `STI-103`, bersinergi dengan administrasi host Linux `STI-310`, lalu menyerahkan penguasaan TCP/IP, subnetting, routing, dan ACL ke **`STI-417 Komputasi Awan`** (*Cloud VPC Networking*), **`STI-418 Dasar Keamanan Informasi`**, **`STI-521 Internet untuk Segala (IoT)`** (komunikasi MQTT/CoAP), dan **`STB-501 Keamanan Jaringan dan Forensik Digital`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS03` (*IT Infrastructure*), `BK-IT03` (*Networking*), & `BK-IT14` (*Network Infrastructure*).

**Pustaka Utama:**
1. Kurose, J. F., & Ross, K. W. (2021). *Computer Networking: A Top-Down Approach* (8th ed.). Pearson.
2. Tanenbaum, A. S., Feamster, N., & Wetherall, D. J. (2021). *Computer Networks* (6th ed.). Pearson.
3. Lammle, T. (2020) / Odom, W. (2024). *CCNA 200-301 Official Cert Guide, Volume 1 & Volume 2* (2nd ed.). Cisco Press.

**Pustaka Pendukung:**
4. Sanders, C. (2017). *Practical Packet Analysis: Using Wireshark to Solve Real-World Network Problems* (3rd ed.). No Starch Press.
5. Dokumentasi Teknis *Wireshark User's Guide*, *Cisco IOS Command Reference*, & *GNS3 / MikroTik RouterOS Documentation*.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring: Teori + Praktikum) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Bagian I):** Menganalisis komponen jaringan, topologi, metrik kinerja (*bandwidth, throughput, latency, jitter, packet loss*), & arsitektur **OSI 7-Layer vs TCP/IP** [C2→C4] | 1.1.1 Ketepatan memetakan fungsi setiap lapisan pada model **OSI (7 Layer)** dan **TCP/IP**. <br>1.1.2 Ketepatan menghitung empat komponen *delay* paket (*processing, queuing, transmission, propagation delay*). | **Kriteria:** Kuis diagnostik formatif.<br>**Teknik:** Eksplorasi awal topologi dasar di *Cisco Packet Tracer* & instalasi *Wireshark*. | **Kuliah Interaktif** `[TM: 100']`<br>**Praktikum Lab 1:** Penyiapan *Packet Tracer & Wireshark*, utilitas dasar `ip/ifconfig, ping, traceroute` `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kontrak belajar, unduh installer *Packet Tracer / Wireshark* di LMS Edlink. | Arsitektur Internet, Metrik Kinerja Transmisi, Model **OSI 7-Layer**, & **TCP/IP Protocol Suite** `[1] Bab 1; [2] Bab 1` | — |
| **2** | **`Sub-CPMK-1.1` (Bagian II):** Menganalisis proses **Enkapsulasi & Dekapsulasi PDU**, media transmisi fisik (UTP, serat optik, nirkabel `802.11`), & protokol *Data Link* (**Ethernet `802.3` & ARP**) [C4] | 1.1.3 Ketepatan menelusuri perubahan *header/trailer* PDU (*Data → Segment → Packet → Frame → Bits*) saat melintasi host dan switch.<br>1.1.4 Ketepatan menganalisis struktur *Ethernet Frame*, pengalamatan MAC 48-bit, tabel *MAC Learning* switch, dan mekanisme resolusi **ARP**. | **Kriteria:** Ketepatan pelacakan alamat MAC vs IP saat paket melewati switch & router.<br>**Teknik:** Praktikum mode simulasi *PDU Inspector* di Packet Tracer. | **Ceramah & Analisis PDU** `[TM: 100']`<br>**Praktikum Lab 2:** Simulasi Enkapsulasi PDU, Tabel MAC Switch, & Pertukaran **ARP** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis pelacakan perubahan MAC sumber/tujuan vs IP sumber/tujuan di LMS Edlink. | Proses **Enkapsulasi PDU**, Media Fisik, Standar **Ethernet (`802.3`)**, Pengenalan WLAN (`802.11`), & **ARP** `[1] Bab 6; [3] Vol 1` | — |
| **3** | **`Sub-CPMK-1.2` (Bagian I):** Menganalisis protokol *Transport Layer* (**TCP vs UDP**: *3-Way Handshake, Flow Control, Port Numbers*) menggunakan **Wireshark** [C4] | 1.2.1 Ketepatan membedakan mekanisme keandalan **TCP** (*SYN, SYN-ACK, ACK, Sequence/Ack Number, FIN/RST*) dengan komunikasi ringan tanpa koneksi **UDP**.<br>1.2.2 Ketepatan menggunakan *display filter* **Wireshark** untuk membedah *header* segmen TCP dan datagram UDP. | **Kriteria:** Ketepatan pembacaan nomor urut *Sequence/Ack* dari berkas `.pcapng`.<br>**Teknik:** Praktikum penangkapan langsung sesi TCP & UDP dengan **Wireshark**. | **Interactive Lecture TCP/UDP** `[TM: 100']`<br>**Praktikum Lab 3:** Tangkapan & Bedah Paket **TCP 3-Way Handshake** dan **UDP** dengan **Wireshark** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi instruksi & berkas `.pcapng` **Tugas 1 (RTM-1)** di LMS Edlink. | *Transport Layer*: *Multiplexing/Demultiplexing Ports*, **UDP**, **TCP** (*3-Way Handshake, Reliable Transfer*), & Inspeksi **Wireshark** `[1] Bab 3; [4]` | — |
| **4** | **`Sub-CPMK-1.2` (Bagian II):** Menganalisis komunikasi *end-to-end* lintas lapisan (*ARP + DNS + TCP + HTTP + ICMP*) menggunakan **Wireshark** [C4]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 1.2.3 Ketepatan merekonstruksi kronologi paket lengkap ketika peramban membuka sebuah situs web dari *cold cache* hingga halaman tampil.<br>1.2.4 Ketepatan mendiagnosis anomali jaringan dasar (*TCP Retransmission, Destination Unreachable ICMP*) dari rekaman Wireshark. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-3`)**.<br>**Teknik:** Pengumpulan Laporan Forensik Paket **Wireshark** + Uji Praktik Singkat *Filter Wireshark* di Lab. | **Case-Based Packet Analysis** `[TM: 100']`<br>**Praktikum Lab 4:** Bedah *Full Protocol Stack Trace* di **Wireshark** & Verifikasi **Tugas 1** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan laporan & berkas tangkapan **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Analisis Lintas Lapisan (**OSI/TCP-IP**) dengan **Wireshark**: Kronologi *ARP–DNS–TCP–HTTP* & Diagnostik **ICMP** `[1]; [4]` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1` (Bagian I):** Merancang pengalamatan **IPv4**, *Subnet Mask*, **CIDR** (*Classless Inter-Domain Routing*), & *Fixed-Length Subnet Masking* (FLSM) [C3] | 2.1.1 Ketepatan menganalisis struktur *IPv4 Header* (TTL, Protocol, Source/Dest IP), ruang alamat privat RFC 1918, dan konversi biner-desimal oktet.<br>2.1.2 Ketepatan menghitung *Network Address, Broadcast Address, First/Last Usable Host,* dan jumlah host valid $2^h - 2$ pada notasi **CIDR** (`/8` s.d. `/30`). | **Kriteria:** Akurasi 100% perhitungan subnet tanpa tumpang tindih.<br>**Teknik:** Latihan cepat perhitungan CIDR & konfigurasi IP antarmuka di lab. | **Problem-Solving IPv4 & CIDR** `[TM: 100']`<br>**Praktikum Lab 5:** Perhitungan Subnetting **CIDR** & Pengujian Konektivitas Subnet di Packet Tracer `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Kuis hitung cepat CIDR tanpa kalkulator di LMS Edlink. | Struktur Paket **IPv4**, Alamat Publik vs Privat (RFC 1918), Notasi Prefix **CIDR**, & *Subnetting* Dasar `[1] Bab 4; [3] Vol 1` | — |
| **6** | **`Sub-CPMK-2.1` (Bagian II):** Merancang skema pengalamatan **VLSM (*Variable Length Subnet Mask*)** & *Route Summarization* untuk organisasi multi-divisi dan tautan titik-ke-titik (`/30`) [C3] | 2.1.3 Ketepatan mengurutkan kebutuhan host divisi dari terbesar ke terkecil dan mengalokasikan blok **VLSM** secara rapat, hemat ruang alamat, dan **100% bebas konflik (*zero address overlap*)**. | **Kriteria:** Tabel alokasi VLSM multi-gedung/multi-divisi efisien & terverifikasi di simulator.<br>**Teknik:** Praktikum perancangan & implementasi VLSM 5 divisi + 3 tautan WAN `/30`. | **Case-Based VLSM Design** `[TM: 100']`<br>**Praktikum Lab 6:** Perancangan & Konfigurasi Topologi Multi-Divisi Berbasis **VLSM** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Lembar studi kasus perancangan VLSM kampus di LMS Edlink. | Teknik **Variable Length Subnet Mask (VLSM)** Efisien, Tautan WAN `/30`–`/31`, & *Supernetting / Route Aggregation* `[3] Vol 1` | — |
| **7** | **`Sub-CPMK-2.2`:** Merancang skema pengalamatan **IPv6** (*128-bit Hexadecimal Compression, Global Unicast, Unique Local, Link-Local, ICMPv6 NDP, & SLAAC*) serta Klinik Pra-UTS [C3] | 2.2.1 Ketepatan menyederhanakan penulisan alamat **IPv6**, membagi *Subnet ID* 16-bit pada prefix `/48 → /64`, serta mengonfigurasi jaringan *Dual-Stack* IPv4/IPv6 tanpa konflik alamat. | **Kriteria:** Konektivitas `ping` IPv6 lintas router berjalan sukses.<br>**Teknik:** Praktikum pengalamatan IPv6 statis & *SLAAC* di Packet Tracer + simulasi UTS. | **Interactive Lecture IPv6 & Klinik UTS** `[TM: 100']`<br>**Praktikum Lab 7:** Konfigurasi Skema **IPv6** & *Dual-Stack* Multi-Divisi `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Simulasi soal perancangan VLSM & IPv6 UTS di LMS Edlink. | Arsitektur **IPv6**: Aturan Penyingkatan, Jenis Alamat (*GUA, ULA, LLA*), *Subnetting* `/64`, **ICMPv6 NDP**, & **SLAAC** `[1] Bab 4; [3] Vol 1` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C3]** | Ketepatan dan efisiensi perancangan skema pengalamatan **IPv4 (*VLSM/CIDR*)** dan **IPv6** untuk studi kasus organisasi multi-divisi dan multi-cabang secara utuh tanpa satu pun konflik/tumpang tindih alamat. | **Kriteria:** **Rubrik Analitik UTS (`K-3`)**.<br>**Teknik:** Ujian Tertulis & Verifikasi Tabel Pengalamatan Terjadwal (*Closed-Book*). | **Ujian Tertulis Perancangan Pengalamatan Luring**<br>`[150 menit]` | Pengarsipan nilai `CPMK-2` pada portal OBE. | Materi Pengalamatan **IPv4 CIDR**, **VLSM Multi-Divisi**, & **IPv6** (Pekan 5–7) | **25%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1` (Bagian I):** Mengonfigurasi segmentasi *Layer-2 Switching* menggunakan **VLAN**, **IEEE 802.1Q Trunking**, *Native VLAN*, & konsep pencegahan *loop* (**STP**) [C3] | 3.1.1 Ketepatan memisahkan *broadcast domain* antar-departemen menggunakan **VLAN** pada beberapa switch yang terhubung melalui tautan **802.1Q Trunk**.<br>3.1.2 Ketepatan menjelaskan mekanisme *VLAN Tagging* dan peran dasar *Spanning Tree Protocol* (STP / RSTP). | **Kriteria:** Host satu VLAN lintas switch terhubung, sedangkan antar-VLAN terisolasi.<br>**Teknik:** Praktikum konfigurasi CLI Switch (*Access Port, Trunk Port, Allowed VLAN*). | **Interactive Lecture Switching** `[TM: 100']`<br>**Praktikum Lab 8:** Konfigurasi **VLAN**, **802.1Q Trunking**, & Pengamatan STP `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Panduan perintah dasar Cisco IOS / RouterOS Switching di LMS Edlink. | Segmentasi *Broadcast Domain*, **VLAN**, Penandaan Frame **IEEE 802.1Q Trunking**, Keamanan *Native VLAN*, & Dasar **STP** `[3] Vol 1` | — |
| **10** | **`Sub-CPMK-3.1` & `3.2` (Awal):** Mengonfigurasi **Inter-VLAN Routing** (*Router-on-a-Stick* sub-interface & *Layer-3 Switch SVI*) serta **Static & Default Routing** [C3] | 3.1.3 Ketepatan menghubungkan komunikasi antar-VLAN melalui sub-antarmuka `encapsulation dot1Q` maupun *Switched Virtual Interface* (SVI).<br>3.2.1 Ketepatan menyusun tabel *routing* menggunakan **Static Route**, *Floating Backup Static Route*, dan **Default Route** (`0.0.0.0/0`). | **Kriteria:** Konektivitas *end-to-end* lintas VLAN & lintas router statis terverifikasi 100%.<br>**Teknik:** Praktikum konfigurasi *Router-on-a-Stick* + *Static Routing* 3 router. | **Problem-Based Configuration** `[TM: 100']`<br>**Praktikum Lab 9:** **Inter-VLAN Routing** + **Static & Default Routing** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi spesifikasi topologi **Tugas 2 (RTM-2)** di LMS Edlink. | **Inter-VLAN Routing** (*ROAS & L3 Switch SVI*), Prinsip *Longest Prefix Match*, *Administrative Distance*, & **Static Routing** `[3] Vol 1` | — |
| **11** | **`Sub-CPMK-3.2`:** Mengonfigurasi protokol *Link-State Dynamic Routing* **OSPFv2** (*Router ID, Wildcard Mask, Neighbor Adjacency, Cost Metric, Passive Interface*) [C3] | 3.2.2 Ketepatan memahami algoritma *Dijkstra Shortest Path First*, pertukaran LSA, pembentukan tetangga `FULL`, dan perhitungan metrik biaya $Cost = \text{Ref BW} / \text{Interface BW}$.<br>3.2.3 Ketepatan mengonfigurasi **OSPF** multi-router, *passive-interface* ke arah LAN, dan memverifikasi konvergensi jalur cadangan otomatis saat satu tautan diputus. | **Kriteria:** Seluruh tetangga OSPF berstatus `FULL` & *failover* otomatis berhasil saat jalur utama diputus.<br>**Teknik:** Praktikum konfigurasi & uji pemutusan tautan **OSPF** di simulator. | **Case-Based OSPF Configuration** `[TM: 100']`<br>**Praktikum Lab 10:** Konfigurasi & Uji *Failover* **Dynamic Routing OSPF** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Daftar perintah verifikasi `show ip ospf neighbor / show ip route` di LMS Edlink. | *Dynamic Routing* (*Distance-Vector vs Link-State*), Protokol **OSPF** (*Area 0, Router-ID, Cost, DR/BDR, Passive Interface*) `[1] Bab 5; [3] Vol 1` | — |
| **12** | **`Sub-CPMK-3.1` & `3.2` (Evaluasi Switching & Routing):** Diagnostik & verifikasi konektivitas terpadu **VLAN + Trunking + Inter-VLAN + OSPF** [C3]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 3.2.4 Ketepatan membangun dan memperbaiki masalah (*troubleshooting*) topologi kampus/cabang lengkap **VLSM + VLAN + Trunk + OSPF** hingga *ping/traceroute end-to-end* sukses 100%. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-3`)**.<br>**Teknik:** Pengumpulan Berkas Topologi & Uji Verifikasi Langsung/Troubleshooting di Laboratorium. | **Troubleshooting Clinic & Uji Tugas 2** `[TM: 100']`<br>**Praktikum Lab 11:** Uji Konektivitas & *Live Troubleshooting* **Tugas 2 (`CPMK-3`)** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas `.pkt`/GNS3 & dokumentasi **Tugas 2 (`CPMK-3`)** di LMS Edlink. | Metodologi *Troubleshooting* Lapisan 2 & 3 serta Evaluasi Topologi Terpadu **VLAN + Trunk + Static/OSPF** `[3] Vol 1` | **25%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.1` (Bagian I):** Mengonfigurasi layanan jaringan dasar **DHCP** (*DORA Process, DHCP Pool, Excluded Address, `ip helper-address` DHCP Relay*), **DNS**, & **HTTP** [C4] | 4.1.1 Ketepatan mengonfigurasi server **DHCP** terpusat lintas VLAN menggunakan *DHCP Relay Agent* sehingga seluruh klien memperoleh IP, *gateway*, dan DNS secara otomatis.<br>4.1.2 Ketepatan mengonfigurasi resolusi nama hierarkis **DNS** (*A, AAAA, CNAME Record*) menuju server **HTTP**. | **Kriteria:** Klien lintas VLAN otomatis mendapat IP dan mampu membuka situs lokal menggunakan nama domain.<br>**Teknik:** Praktikum konfigurasi *DHCP Relay + DNS + HTTP Server*. | **Interactive Lecture Network Services** `[TM: 100']`<br>**Praktikum Lab 12:** Konfigurasi Terpusat **DHCP (+ Relay)**, **DNS**, & **HTTP** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Panduan pelacakan paket DORA DHCP & DNS Query di LMS Edlink. | Protokol Lapisan Aplikasi & Layanan Infrastruktur: **DHCP** (*DORA & Relay*), Hierarki **DNS**, & **HTTP/HTTPS Dasar** `[1] Bab 2; [3] Vol 2` | — |
| **14** | **`Sub-CPMK-4.1` (Bagian II) & `4.2` (Awal):** Mengonfigurasi **NAT** (*Static NAT, Dynamic NAT, PAT / NAT Overload*) menuju jaringan eksternal & dasar **Standard ACL** [C4] | 4.1.3 Ketepatan mengonfigurasi **PAT (*Port Address Translation / NAT Overload*)** untuk akses internet klien internal serta **Static NAT / Port Forwarding** untuk mempublikasikan server web DMZ.<br>4.2.1 Ketepatan memahami cara kerja pemrosesan berurutan (*top-down*), *wildcard mask*, dan aturan tak terlihat **`deny any` (*implicit deny*)** pada **Standard ACL**. | **Kriteria:** Tabel `show ip nat translations` aktif benar & akses manajemen VTY/segmen tersaring sesuai kebijakan.<br>**Teknik:** Praktikum konfigurasi *PAT + Static Port Forwarding + Standard ACL*. | **Case-Based NAT & ACL Lecture** `[TM: 100']`<br>**Praktikum Lab 13:** Konfigurasi **Static NAT, PAT Overload**, & **Standard ACL** `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Spesifikasi proyek jaringan akhir UAS dirilis di LMS Edlink. | *Network Address Translation* (**Static NAT, Dynamic NAT, PAT**) & Prinsip Dasar **Access Control Lists (Standard ACL)** `[3] Vol 2` | — |
| **15** | **`Sub-CPMK-4.2`:** Merancang dan mengonfigurasi kebijakan keamanan segmen lokal menggunakan **Extended ACL** (berbasis protokol TCP/UDP, IP sumber/tujuan, & nomor port) serta klinik pra-UAS [C4] | 4.2.2 Ketepatan menempatkan **Extended ACL** sedekat mungkin ke sumber dan **Standard ACL** sedekat mungkin ke tujuan.<br>4.2.3 Ketepatan mengimplementasikan matriks kebijakan keamanan antar-zona (mis. *VLAN Tamu hanya boleh HTTP/HTTPS & DNS ke DMZ/Internet, dilarang keras mengakses/ping VLAN Keuangan & SSH Router!*). | **Kriteria:** Matriks uji positif (yang diizinkan tembus) & uji negatif (yang dilarang terblokir) 100% sesuai spesifikasi.<br>**Teknik:** Praktikum pengamanan jaringan multi-zona dengan **Extended ACL** & klinik pra-UAS. | **Security Policy Workshop & Klinik UAS** `[TM: 100']`<br>**Praktikum Lab 14:** Implementasi Kebijakan **Extended ACL** Multi-Segmen & Uji Penetrasi Koneksi Dasar `[Prak: 170']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan draf topologi & matriks uji kebijakan jaringan UAS di LMS Edlink. | Kebijakan Penyaringan Paket **Extended ACL** (*Source/Dest IP, Protocol ICMP/TCP/UDP, Port `eq 80/443/53/22`*), Aturan Penempatan ACL, & Dokumentasi Jaringan `[3] Vol 2` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C4]** | Keberhasilan fungsional konfigurasi layanan jaringan dasar (**DNS, DHCP, HTTP, NAT**) dan ketepatan kebijakan penyaringan keamanan **ACL** dalam mengamankan segmen jaringan lokal pada proyek topologi organisasi dan ujian praktik individu. | **Kriteria:** **Rubrik Analitik UAS (`K-3`)**.<br>**Teknik:** Penilaian Proyek Topologi Jaringan Organisasi Lengkap & Matriks Uji (50% UAS) + Sidang Praktik Konfigurasi/*Troubleshooting* Langsung Individu (50% UAS). | **Sidang Demonstrasi Topologi & Ujian Praktik Konfigurasi ACL/NAT di Lab**<br>`[150 menit]` | Pengarsipan berkas simulasi, dokumentasi jaringan, & rekap nilai `CPL-07` dan `CPL-11` pada portal OBE. | Integrasi Komprehensif **VLSM/IPv6 + VLAN/OSPF + Layanan DNS/DHCP/HTTP/NAT + Pengamanan Segmen ACL** | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-07` [C4])
* **Bentuk Instrumen:** Laporan Analisis Forensik Lalu Lintas Paket **Wireshark** Individu + Verifikasi Praktik Filter Singkat di Lab: mahasiswa menangkap langsung dan membedah berkas `.pcapng` berisi rangkaian sesi **ARP, DNS, ICMP, TCP (*3-Way Handshake*, transfer data, *teardown*),** dan **HTTP**, memetakan secara presisi setiap *header* ke lapisan **OSI (7 Layer)** dan **TCP/IP** (alamat MAC, alamat IP, nomor port ephemerals/layanan, *Sequence/Ack number*, dan ukuran *payload*).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan analisis enkapsulasi PDU lintas lapisan **OSI 7-Layer & TCP/IP** = **35%**; (2) Akurasi pembedahan *header* & kronologi paket di **Wireshark** (*ARP, TCP Handshake, UDP/DNS, HTTP*) = **40%**; (3) Ketepatan penggunaan *Wireshark Display Filters* saat verifikasi lab = **15%**; (4) Kerapian laporan bukti tangkapan paket asli = **10%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 25% · Mengukur `CPMK-2` / `CPL-07` [C3])
* **Bentuk Instrumen:** Ujian Tertulis Perancangan Pengalamatan Jaringan Luring Terjadwal (*Closed-Book*, 150 menit): diberikan studi kasus organisasi dengan kantor pusat dan 2 kantor cabang (total 7 segmen divisi dengan jumlah host berbeda-beda + 3 tautan antar-router WAN), mahasiswa merancang tabel alokasi lengkap **IPv4 VLSM/CIDR** yang paling hemat tanpa konflik alamat, menghitung ringkasan rute (*route summarization*), serta merancang skema pengalamatan pendamping **IPv6** (`/48` ke subnet `/64` per segmen + alamat *Link-Local*).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan urutan & perhitungan blok **IPv4 VLSM/CIDR** (*Network, Prefix, First/Last Host, Broadcast*) = **45%**; (2) Efisiensi ruang alamat & jaminan **0 konflik/overlap alamat** = **25%**; (3) Ketepatan perancangan skema subnetting & penulisan **IPv6** = **30%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 25% · Mengukur `CPMK-3` / `CPL-11` [C3])
* **Bentuk Instrumen:** Proyek Konfigurasi Jaringan Kampus/Cabang Individu pada Simulator (*Cisco Packet Tracer / GNS3*) + Uji Verifikasi/Troubleshooting di Lab: mengimplementasikan topologi multi-switch dan multi-router dengan minimal 4 **VLAN**, tautan **802.1Q Trunking**, **Inter-VLAN Routing**, **Static/Default Route**, dan protokol dinamis **OSPF** berjalur redundan hingga *end-to-end connectivity* dan *failover* otomatis terverifikasi 100%.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Kebenaran konfigurasi **VLAN, 802.1Q Trunking,** & **Inter-VLAN Routing** (`Sub-CPMK-3.1`) = **40%**; (2) Kebenaran konfigurasi **Static Routing & Dynamic OSPF** beserta uji *failover* (`Sub-CPMK-3.2`) = **40%**; (3) Verifikasi konektivitas *end-to-end* & kecakapan *live troubleshooting* di lab = **20%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-11` [C4])
* **Bentuk Instrumen:** **Proyek Infrastruktur Jaringan Lokal Aman Terintegrasi** (50% nilai UAS: topologi organisasi utuh yang menjalankan layanan terpusat **DHCP Relay, DNS, HTTP Server, Static NAT + PAT Overload**, dan matriks kebijakan keamanan multi-segmen menggunakan **Standard & Extended ACL** lengkap laporan pengujian positif/negatif) + **Ujian Praktik Konfigurasi & Sidang Verifikasi Individu di Lab** (50% nilai UAS, 150 menit).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Fungsionalitas penuh layanan jaringan (**DNS, DHCP, HTTP, & NAT/PAT** — `Sub-CPMK-4.1`) = **35%**; (2) Ketepatan aturan, urutan baris, & lokasi pemasangan **Standard/Extended ACL** mengamankan segmen lokal tanpa memutus layanan sah (`Sub-CPMK-4.2`) = **35%**; (3) Kelengkapan dokumentasi topologi & matriks verifikasi uji = **15%**; (4) Keberhasilan ujian praktik/modifikasi aturan ACL langsung saat sidang individu = **15%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Infrastruktur TI, Cloud & Keamanan Siber**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Ir. Bambang Suprapto, M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
