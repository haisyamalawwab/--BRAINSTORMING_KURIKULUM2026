# 066_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-312 — JARINGAN KOMPUTER (*Computer Networks*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI312` · **Bobot:** 3 SKS `+P` (`TM 100'`, `Prak 170'`, `PT 120'`, `BM 120'`) · **Semester:** 3  
**Prasyarat:** `STI-103` Organisasi dan Arsitektur Komputer · **CPL:** `CPL-07` (`P3` = 45%) & `CPL-11` (`KK3` = 55%) [Level `R`]  
**Klaster Rubrik:** `K-3` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu & Asisten Laboratorium `STI-312` |
|---|---|
| **Struktur Waktu per Sesi** | **Sesi Teori (`100'`):** Pendahuluan `15'` · Inti & Bedah Protokol `70'` · Penutup `15'`<br>**Sesi Praktikum Lab (`170'`):** *Briefing* Topologi `15'` · Konfigurasi CLI & Inspeksi Paket Terbimbing `135'` · Verifikasi Konektivitas `20'`, diikuti `PT 120'` & `BM 120'`. |
| **Fokus Keilmuan (*In-Scope*)** | Analisis enkapsulasi **OSI 7-Layer & TCP/IP** dengan **Wireshark**, perancangan **IPv4 CIDR/VLSM** & **IPv6**, konfigurasi **VLAN/Trunking**, **Static/OSPF Routing**, layanan **DNS/DHCP/HTTP/NAT**, serta pengamanan segmen lokal dengan **ACL**. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** melebar ke *penetration testing*, kriptografi lanjut, & IDS/IPS enterprise (**`STI-418 Dasar Keamanan Informasi`** / **`STB-501 Keamanan Jaringan dan Forensik Digital`**), dilarang membahas *Cloud VPC* AWS/GCP (**`STI-417 Komputasi Awan`**), dan dilarang membahas fisika sinyal RF mendalam. |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Teori (`100'`) & Modul Praktikum (`170'`) | Waktu Total | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Teori: Metrik Kinerja, **OSI 7-Layer**, & **TCP/IP** · Lab 1: Utilitas Jaringan & Pengantar Simulator | 270' | Formatif Lab |
| **2** | `Sub-CPMK-1.1` | Teori: **Enkapsulasi PDU**, Ethernet `802.3`, & **ARP** · Lab 2: Pelacakan PDU & Tabel MAC/ARP | 270' | Formatif Lab |
| **3** | `Sub-CPMK-1.2` | Teori: *Transport Layer* (**TCP vs UDP**) · Lab 3: Bedah **TCP 3-Way Handshake** di **Wireshark** | 270' | Formatif Lab |
| **4** | `Sub-CPMK-1.2` | Teori: Kronologi Lintas Lapisan & **ICMP** · Lab 4: Forensik Paket **Wireshark** & Uji **Tugas 1** | 270' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Teori: Struktur **IPv4**, RFC 1918, & **CIDR** · Lab 5: Perhitungan & Implementasi Subnet CIDR | 270' | Formatif Lab |
| **6** | `Sub-CPMK-2.1` | Teori: Teknik **VLSM** Multi-Divisi & *Summarization* · Lab 6: Topologi Organisasi Berbasis **VLSM** | 270' | Formatif Lab |
| **7** | `Sub-CPMK-2.2` | Teori: Pengalamatan **IPv6** (*GUA, LLA, SLAAC*) · Lab 7: Topologi *Dual-Stack* IPv4/IPv6 & Klinik UTS | 270' | Formatif Lab |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** Perancangan Skema Pengalamatan **IPv4 VLSM/CIDR** & **IPv6** | 150' | **UTS (25%)** |
| **9** | `Sub-CPMK-3.1` | Teori: Segmentasi **VLAN**, **802.1Q Trunking**, & STP · Lab 8: Konfigurasi CLI VLAN & Trunk | 270' | Formatif Lab |
| **10** | `Sub-CPMK-3.1, 3.2` | Teori: **Inter-VLAN Routing** & **Static Routing** · Lab 9: *Router-on-a-Stick*, SVI, & Rute Statis | 270' | Formatif Lab |
| **11** | `Sub-CPMK-3.2` | Teori: *Link-State Routing* **OSPF** (*SPF, Area 0, Cost*) · Lab 10: Konfigurasi & *Failover* **OSPF** | 270' | Formatif Lab |
| **12** | `Sub-CPMK-3.1, 3.2` | Teori: Metodologi *Troubleshooting* L2/L3 · Lab 11: Verifikasi Konektivitas **Tugas 2** | 270' | **Tugas 2 (25%)** |
| **13** | `Sub-CPMK-4.1` | Teori: Layanan **DHCP (+ Relay)**, **DNS**, & **HTTP** · Lab 12: Server Layanan Terpusat Lintas VLAN | 270' | Formatif Lab |
| **14** | `Sub-CPMK-4.1, 4.2` | Teori: **Static NAT, PAT Overload**, & **Standard ACL** · Lab 13: Koneksi Internet NAT & Filter Dasar | 270' | Formatif Lab |
| **15** | `Sub-CPMK-4.2` | Teori: Kebijakan Keamanan **Extended ACL** Multi-Zona · Lab 14: Pengamanan Segmen & Klinik UAS | 270' | Formatif Lab |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang Topologi Layanan/ACL & Ujian Praktik Individu di Lab | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN (TEORI + PRAKTIKUM)

### PERTEMUAN 1 — Arsitektur Internet, Metrik Kinerja, & Model **OSI 7-Layer vs TCP/IP**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C2→C4] · **Alat:** *Cisco Packet Tracer*, *Wireshark*, CLI Host (`ip`, `ping`, `tracert/traceroute`).
* **Sesi Teori (`100'`):** Menghubungkan prasyarat `STI-103` menuju komunikasi antar-sistem: topologi fisik vs logis, perbedaan tajam *Bandwidth* (kapasitas pipa) vs *Throughput* (aliran aktual), 4 sumber latensi paket, serta perbandingan peran setiap lapis pada **OSI 7-Layer** dan **TCP/IP**.
* **Sesi Praktikum Lab 1 (`170'`):** Membangun LAN pertama di simulator, menguji `ping` dan `traceroute`, serta memverifikasi instalasi penangkap paket *Wireshark*.
* **PT (`120'`) & BM (`120'`):** Menghitung soal latihan *transmission delay* vs *propagation delay*.

### PERTEMUAN 2 — **Enkapsulasi PDU**, Standar Ethernet `802.3`, & Protokol **ARP**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C4] · **Alat:** *Packet Tracer Simulation Mode*, *Wireshark*.
* **Sesi Teori (`100'`):** Menelusuri pembungkusan **PDU** (*Data → Segment → Packet → Frame → Bits*), aturan emas komunikasi jaringan (**alamat IP sumber/tujuan tetap utuh dari ujung ke ujung kecuali ada NAT, sedangkan alamat MAC sumber/tujuan selalu berganti di setiap lompatan router!**), cara switch membangun *MAC Address Table*, serta mekanisme *broadcast request / unicast reply* pada **Address Resolution Protocol (ARP)**.
* **Sesi Praktikum Lab 2 (`170'`):** Mengamati tabel `arp -a` dan `show mac address-table` serta membedah *Ethernet II Frame* dan paket ARP di mode simulasi & Wireshark.
* **PT (`120'`) & BM (`120'`):** Menyusun diagram jejak perubahan *header* L2 dan L3 pada perjalanan paket melintasi 2 router.

### PERTEMUAN 3 — *Transport Layer* (**TCP vs UDP**) & Inspeksi **Wireshark**
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] · **Alat:** *Wireshark Packet Analyzer*.
* **Sesi Teori (`100'`):** Membedah fungsi penomoran *Port* (`Well-Known 0–1023`, `Registered`, `Ephemeral`), perbandingan **UDP** (*connectionless, low overhead* untuk DNS/VoIP/streaming) dengan **TCP** (*connection-oriented*, **Three-Way Handshake [`SYN → SYN,ACK → ACK`]**, *Sequence & Acknowledgment Numbers*, *Window Size*, dan penutupan koneksi `FIN/ACK`). Merilis resmi **Tugas 1 (RTM-1)**.
* **Sesi Praktikum Lab 3 (`170'`):** Menangkap lalu lintas nyata di **Wireshark**, menggunakan fitur *Follow TCP Stream* dan *Display Filters* (`tcp.port == 80`, `tcp.flags.syn == 1`, `udp.port == 53`), serta menghitung kenaikan *Sequence Number* sesuai panjang *payload*.
* **PT (`120'`) & BM (`120'`):** Menganalisis berkas tangkapan sesi TCP & UDP pada **Tugas 1**.

### PERTEMUAN 4 — Analisis Komunikasi Lintas Lapisan di **Wireshark** & Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.2` [C4] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Alat:** *Wireshark*.
* **Sesi Teori (`100'`):** Merangkai gambaran utuh komunikasi jaringan dari awal hingga akhir ketika pengguna mengetik sebuah alamat web (*DHCP → ARP Gateway → DNS Query UDP → TCP 3-Way Handshake → HTTP GET/200 OK*), serta penggunaan pesan kontrol **ICMP** (*Echo Request/Reply, Time Exceeded, Destination Unreachable*) untuk diagnostik.
* **Sesi Praktikum Lab 4 (`170'`):** Pengumpulan laporan **Tugas 1 (`CPMK-1`)** disertai ujian singkat 20 menit menyaring dan menjawab 5 pertanyaan langsung dari berkas `.pcapng` baru di layar lab menggunakan **Wireshark**.
* **PT (`120'`) & BM (`120'`):** Melatih kembali konversi cepat biner 8-bit (`128, 64, 32, 16, 8, 4, 2, 1`) untuk pekan pengalamatan IP.

### PERTEMUAN 5 — Pengalamatan **IPv4**, Ruang Privat RFC 1918, & **CIDR Subnetting**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Alat:** Lembar Kerja Biner IPv4 & *Packet Tracer*.
* **Sesi Teori (`100'`):** Menguraikan keterbatasan *Classful Addressing* kuno dan transisi ke **CIDR (*Classless Inter-Domain Routing*)**, blok alamat privat (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), operasi `AND` biner *Subnet Mask*, serta teknik cepat menentukan *Block Size / Magic Number*, alamat jaringan, rentang host valid, dan alamat *broadcast*.
* **Sesi Praktikum Lab 5 (`170'`):** Memecah satu jaringan `/24` menjadi beberapa subnet sama besar, memasangkannya ke antarmuka router & PC di Packet Tracer, dan membuktikan mengapa salah *subnet mask* menggagalkan komunikasi.
* **PT (`120'`) & BM (`120'`):** Menyelesaikan 15 soal latihan cepat *CIDR Subnetting* berbagai panjang prefix (`/19` s.d. `/30`).

### PERTEMUAN 6 — Perancangan Efisien **VLSM (*Variable Length Subnet Mask*)** Multi-Divisi
* **Sub-CPMK:** `Sub-CPMK-2.1` [C3] · **Alat:** Peta Blok Alamat VLSM & Simulator Jaringan.
* **Sesi Teori (`100'`):** Mengajarkan mengapa FLSM memboroskan ratusan alamat IP saat diterapkan pada tautan antar-router yang hanya butuh 2 alamat! Melatih metodologi sistematis **VLSM**: mengurutkan segmen dari kebutuhan host terbesar ke terkecil (ditambah cadangan pertumbuhan), mengalokasikan blok berurutan tanpa celah tumpang tindih (**zero overlap**), memakai `/30` untuk tautan titik-ke-titik WAN, serta merangkum rute (*route summarization*).
* **Sesi Praktikum Lab 6 (`170'`):** Merancang dan mengimplementasikan topologi perusahaan 5 divisi (200, 90, 45, 20, dan 10 host + 3 tautan router `/30`) dari satu blok `172.16.10.0/23`.
* **PT (`120'`) & BM (`120'`):** Mengerjakan studi kasus perancangan VLSM multi-gedung kampus.

### PERTEMUAN 7 — Pengalamatan **IPv6** Dasar & Klinik Persiapan UTS
* **Sub-CPMK:** `Sub-CPMK-2.2` [C3] · **Alat:** *Packet Tracer Dual-Stack Lab*.
* **Sesi Teori (`100'`):** Menguraikan arsitektur 128-bit heksadesimal **IPv6**: dua aturan emas penyingkatan (menghapus nol di depan hekstet & satu kali `::`), ketiadaan *broadcast* di IPv6 (digantikan *Multicast*), jenis alamat (**Global Unicast `2000::/3`, Unique Local `fc00::/7`, Link-Local `fe80::/10`**), pembagian subnet bersih pada hekstet ke-4 (`/48` organisasi $\rightarrow$ `/64` per LAN), serta konfigurasi otomatis **SLAAC** berbasis *Router Advertisement* ICMPv6, ditutup klinik pra-UTS.
* **Sesi Praktikum Lab 7 (`170'`):** Mengonfigurasi topologi *Dual-Stack* (IPv4 VLSM + IPv6 `/64` per divisi dengan `ipv6 unicast-routing`) dan memverifikasi `ping` IPv4 maupun IPv6 tanpa konflik.
* **PT (`120'`) & BM (`120'`):** Persiapan mandiri menghadapi UTS Pekan 8.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C3]) · **Bobot:** **25%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Ujian tertulis perancangan pengalamatan jaringan luring terjadwal (*closed-book*): merancang tabel skema **IPv4 VLSM/CIDR** multi-divisi dan multi-cabang yang efisien serta skema pengalamatan **IPv6** pendampingnya secara akurat dan bebas konflik alamat.

### PERTEMUAN 9 — Segmentasi Switching: **VLAN**, **IEEE 802.1Q Trunking**, & Dasar **STP**
* **Sub-CPMK:** `Sub-CPMK-3.1` [C3] · **Alat:** *Cisco Packet Tracer / GNS3* CLI Switch.
* **Sesi Teori (`100'`):** Membahas hasil UTS lalu menguraikan mengapa jaringan datar besar lumpuh oleh badai *broadcast*: konsep pemecahan *broadcast domain* secara logis menggunakan **VLAN**, penandaan *header* 4-byte **IEEE 802.1Q** pada tautan **Trunk** antar-switch, praktik aman memindahkan *Native VLAN* dari VLAN 1 dan mematikan port menganggur, serta fungsi **Spanning Tree Protocol (STP)** mencegah *Layer-2 Broadcast Storm*.
* **Sesi Praktikum Lab 8 (`170'`):** Mengonfigurasi 3 switch bertingkat dengan 4 VLAN (Akademik, Keuangan, Lab, Manajemen), *Access Ports*, dan *802.1Q Trunk Ports*, serta memverifikasi `show vlan brief` dan `show interfaces trunk`.
* **PT (`120'`) & BM (`120'`):** Melatih perintah CLI pembuatan VLAN dan pembatasan `switchport trunk allowed vlan`.

### PERTEMUAN 10 — **Inter-VLAN Routing** & **Static / Default Routing**
* **Sub-CPMK:** `Sub-CPMK-3.1` & `3.2` [C3] · **Alat:** CLI Router & *Layer-3 Multilayer Switch*.
* **Sesi Teori (`100'`):** Mengajarkan dua arsitektur menghubungkan komunikasi antar-VLAN yang berbeda subnet: **Router-on-a-Stick** (sub-antarmuka `g0/0.10`, `encapsulation dot1Q 10`) dan **Layer-3 Switch SVI** (`interface vlan 10` + `ip routing`), dilanjutkan pengambilan keputusan *routing* (*Longest Prefix Match* & *Administrative Distance*) serta konfigurasi **Static Route**, *Floating Static Route*, dan **Default Route** (`0.0.0.0 0.0.0.0`). Merilis resmi **Tugas 2 (RTM-2)**.
* **Sesi Praktikum Lab 9 (`170'`):** Menghubungkan 4 VLAN melalui *Inter-VLAN Routing* dan merutekan lalu lintas antar 3 kantor cabang menggunakan *Static & Default Routing*.
* **PT (`120'`) & BM (`120'`):** Membangun fondasi VLAN dan pengalamatan VLSM untuk proyek **Tugas 2**.

### PERTEMUAN 11 — Protokol *Dynamic Routing* **OSPF** (*Single/Multi-Area Dasar*)
* **Sub-CPMK:** `Sub-CPMK-3.2` [C3] · **Alat:** Simulator Topologi Mesh 4 Router.
* **Sesi Teori (`100'`):** Mengapa *Static Routing* sulit dipelihara saat jaringan tumbuh memiliki puluhan router dan jalur cadangan? Membedah cara kerja protokol *Link-State* standar terbuka **OSPFv2**: paket *Hello*, syarat terbentuknya *Neighbor Adjacency (`FULL`)*, pertukaran *Link-State Advertisement* (LSA) membentuk LSDB identik, pohon jalur terpendek Dijkstra, rumus $Cost = \text{Reference BW} / \text{Interface BW}$, pemilihan *DR/BDR* pada segmen multi-akses, serta pengamanan **`passive-interface`** ke arah LAN pengguna.
* **Sesi Praktikum Lab 10 (`170'`):** Mengonfigurasi **OSPF Area 0** pada topologi cincin 4 router, mengatur `auto-cost reference-bandwidth`, lalu memutus salah satu kabel utama dan menyaksikan OSPF mengalihkan rute secara otomatis!
* **PT (`120'`) & BM (`120'`):** Menyelesaikan keseluruhan konfigurasi **VLAN + Trunking + Inter-VLAN + OSPF** pada **Tugas 2**.

### PERTEMUAN 12 — *Troubleshooting* Konektivitas Lapisan 2/3 & Evaluasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.1` & `3.2` [C3] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 25%)** · **Alat:** Simulator Lab.
* **Sesi Teori (`100'`):** Mengajarkan daftar periksa sistematis pelacakan kegagalan jaringan: *VLAN belum dibuat di switch perantara, VLAN terpotong di allowed trunk, salah encapsulation dot1Q, default-gateway PC keliru, ketidakcocokan Hello/Dead timer atau subnet mask pada tetangga OSPF*.
* **Sesi Praktikum Lab 11 (`170'`):** Verifikasi proyek **Tugas 2 (`CPMK-3`)** di laboratorium — selain memeriksa berkas topologi mahasiswa, asisten/dosen menyuntikkan 2 kesalahan tersembunyi (*trouble tickets*) yang wajib ditemukan dan diperbaiki langsung oleh mahasiswa dalam waktu 15 menit!
* **PT (`120'`) & BM (`120'`):** Mempelajari layanan jaringan otomatis DHCP dan DNS untuk pekan berikutnya.

### PERTEMUAN 13 — Konfigurasi Layanan Jaringan Dasar: **DHCP (+ Relay)**, **DNS**, & **HTTP**
* **Sub-CPMK:** `Sub-CPMK-4.1` [C4] · **Alat:** Topologi Server Farm + Multi-VLAN.
* **Sesi Teori (`100'`):** Menguraikan empat tahap pertukaran **DHCP** (*Discover, Offer, Request, Acknowledge — DORA*) dan mengapa paket *broadcast* DHCP Discover terhenti di router sehingga wajib diteruskan sebagai *unicast* menggunakan **`ip helper-address` (DHCP Relay)**, dilanjutkan cara kerja resolusi rekursif/iteratif **DNS** (*A, AAAA, CNAME, MX, NS*) menuju server aplikasi **HTTP**.
* **Sesi Praktikum Lab 12 (`170'`):** Membangun segmen *Server Farm* terpusat yang melayani distribusi IP otomatis ke 4 VLAN berbeda via *DHCP Relay* serta resolusi domain internal `portal.sistekin.local` ke server **HTTP**.
* **PT (`120'`) & BM (`120'`):** Mengintegrasikan layanan DHCP, DNS, dan HTTP ke rancangan topologi akhir UAS.

### PERTEMUAN 14 — Konfigurasi **NAT (*Static NAT, Dynamic NAT, PAT*)** & Dasar **Standard ACL**
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C4] · **Alat:** Topologi Router Tepi (*Edge Router*) + Simulasi ISP.
* **Sesi Teori (`100'`):** Mengajarkan bagaimana ratusan perangkat ber-IP privat RFC 1918 dapat mengakses internet publik hanya dengan 1 alamat IP publik melalui **PAT (*Port Address Translation / NAT Overload*)**, cara mengekspos server web lokal di zona DMZ menggunakan **Static NAT / Port Forwarding**, serta pengantar penyaringan paket menggunakan **Standard Access Control List** (aturan pemrosesan *top-down*, perhitungan *Wildcard Mask*, dan jebakan mematikan **`implicit deny any`** di baris paling bawah).
* **Sesi Praktikum Lab 13 (`170'`):** Mengonfigurasi `ip nat inside` / `ip nat outside`, **PAT Overload** untuk seluruh VLAN internal, **Static NAT** untuk server HTTP DMZ, serta **Standard ACL** pembatas akses administrasi SSH/VTY router.
* **PT (`120'`) & BM (`120'`):** Merancang matriks kebijakan akses keamanan antar-segmen untuk proyek akhir UAS.

### PERTEMUAN 15 — Pengamanan Segmen Jaringan Lokal dengan **Extended ACL** & Klinik Pra-UAS
* **Sub-CPMK:** `Sub-CPMK-4.2` [C4] · **Alat:** Topologi Multi-Zona (*Internal LAN, Guest Wi-Fi, Server DMZ, ISP*).
* **Sesi Teori (`100'`):** Mengajarkan perancangan dan penempatan presisi **Extended Named ACL** yang menyaring berdasarkan 5-tupel (*protokol `tcp/udp/icmp`, IP sumber, IP tujuan, dan nomor port `eq 80/443/53/22`*): aturan emas menempatkan **Extended ACL sedekat mungkin ke sumber lalu lintas** agar paket terlarang langsung dibuang tanpa memboroskan *bandwidth* tulang punggung, serta metode verifikasi menggunakan `show access-lists` (melihat kenaikan pencacah `matches`!).
* **Sesi Praktikum Lab 14 (`170'`):** Menerapkan kebijakan keamanan lengkap pada topologi multi-zona (mis. mengisolasi *VLAN Guest* dari *VLAN Keuangan/HRD* sambil tetap mengizinkannya mengakses DNS & Web publik via NAT) dan melakukan klinik pemeriksaan kesiapan proyek UAS.
* **PT (`120'`) & BM (`120'`):** Finalisasi berkas simulasi dan laporan matriks pengujian layanan + keamanan **ACL** untuk UAS Pekan 16.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C4]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Proyek Topologi Organisasi Terintegrasi Layanan (DNS, DHCP, HTTP, NAT) & Pengamanan Segmen ACL (50% nilai UAS)** dengan **Ujian Praktik Konfigurasi & Verifikasi Langsung Individu di Laboratorium (50% nilai UAS)** di mana setiap mahasiswa diuji mengonfigurasi NAT/Extended ACL atas kebijakan baru dan membuktikan penghitung `matches` paket yang diizinkan maupun diblokir secara langsung.
