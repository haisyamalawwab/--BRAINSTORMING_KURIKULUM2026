# 066_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-312 — JARINGAN KOMPUTER (*Computer Networks*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI312` · **Klaster Rubrik Master (Dok 018):** Klaster 3 (`K-3`)  
**CPL:** `CPL-07` (`P3` = 45%) & `CPL-11` (`KK3` = 55%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN REKAYASA JARINGAN KOMPUTER (`K-3`)

Selaras **Dokumen 018 §3**, penilaian Klaster 3 (`K-3`) pada `STI-312 Jaringan Komputer` menuntut presisi absolut pada 4 pilar jaringan: (1) ketajaman pembacaan *header* enkapsulasi paket nyata di **Wireshark**, (2) nol toleransi terhadap tumpang tindih (*address conflict*) pada perancangan **IPv4 VLSM/CIDR** & **IPv6**, (3) konektivitas *end-to-end* penuh dan ketahanan *failover* pada **VLAN/Trunking & OSPF**, serta (4) keakuratan layanan (**DNS, DHCP, HTTP, NAT**) dan penyaringan keamanan **ACL** tanpa memutus lalu lintas sah.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-07` [C4])
**Objek Penilaian:** Laporan Analisis Enkapsulasi **OSI 7-Layer & TCP/IP** Menggunakan **Wireshark** + Uji Praktik Filter Lab.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Analisis Enkapsulasi PDU Lintas **OSI 7-Layer & TCP/IP****<br>(`Sub-CPMK-1.1`) | **35%** | Memetakan secara akurat perubahan PDU (*Frame, Packet, Segment, Payload*) beserta alasan perubahan MAC per-hop vs tetapnya IP sumber/tujuan tanpa kekeliruan. | Pemetaan *header* ke lapisan OSI dan TCP/IP tepat dan konsisten pada seluruh jenis paket yang dianalisis. | Mampu memetakan lapisan utama L2, L3, L4, dan L7 dengan benar, namun penjelasan proses dekapsulasi di router kurang rinci. | Tertukar antara alamat fisik MAC (L2) dan alamat logis IP (L3) atau tertukar antara port TCP dan alamat IP. | Gagal menjelaskan proses enkapsulasi lintas lapisan. |
| **2. Ketepatan Bedah Paket di **Wireshark** (*ARP, TCP, UDP, HTTP*)**<br>(`Sub-CPMK-1.2`) | **40%** | Menelusuri *ARP Request/Reply*, *DNS Query/Response*, *TCP 3-Way Handshake* (perhitungan kenaikan `Seq/Ack` eksak), dan *HTTP* dengan bukti tangkapan paket asli yang tajam. | Pembacaan nilai *field header* ARP, TCP, UDP, dan HTTP dari rekaman Wireshark akurat dengan analisis yang jelas. | Mampu menunjukkan paket *SYN, SYN-ACK, ACK* dan permintaan HTTP, namun perhitungan nomor urut `Seq/Ack` relatif/absolut kurang lengkap. | Hanya melampirkan tangkapan layar daftar paket Wireshark tanpa membedah isi panel *Packet Details*. | Tangkapan paket tidak sesuai skenario atau menyalin milik rekan. |
| **3. Kecakapan Praktik *Wireshark Display Filters* di Lab** | **15%** | Menyelesaikan seluruh 5 pertanyaan pencarian paket langsung di lab menggunakan *display filter* presisi dalam waktu singkat. | Menjawab 4 dari 5 soal praktik filter Wireshark dengan benar dan mandiri. | Menjawab 3 dari 5 soal praktik menggunakan filter dasar atau pencarian manual. | Bingung membedakan *Capture Filter* dan *Display Filter* sehingga gagal menyaring paket yang diminta. | Tidak mampu mengoperasikan dasar *Wireshark* di lab. |
| **4. Kerapian Dokumentasi Teknis** | **10%** | Laporan terstruktur sistematis, setiap tangkapan layar diberi anotasi penunjuk *field* yang relevan. | Laporan rapi, jelas terbaca, dan mencantumkan identitas tangkapan paket sendiri. | Laporan cukup rapi walau beberapa gambar tangkapan layar terlalu kecil. | Dokumentasi berantakan dan tanpa keterangan gambar. | Tidak mengumpulkan berkas `.pcapng` asli. |

$$\text{Skor Tugas 1} = 0,35(K_1) + 0,40(K_2) + 0,15(K_3) + 0,10(K_4)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 25% MK · Mengukur `CPMK-2` / `CPL-07` [C3])
**Objek Penilaian:** Jawaban Ujian Tertulis 150 Menit: Perancangan Skema Pengalamatan **IPv4 (*VLSM/CIDR*)** & **IPv6** Multi-Divisi.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Ketepatan Perhitungan Tabel **IPv4 VLSM/CIDR****<br>(`Sub-CPMK-2.1`) | **45%** | Pengurutan divisi terbesar-ke-terkecil tepat, pemilihan prefix (`/24` s.d. `/30`), *Subnet Mask*, *Network ID*, rentang *Usable Host*, *Broadcast ID*, dan *Route Summary* 100% akurat. | Prosedur VLSM benar seluruhnya; hanya terdapat 1 salah hitung aritmetika kecil pada oktet terakhir satu segmen kecil. | Mampu menghitung sebagian besar subnet VLSM dengan benar, namun kurang tepat pada penentuan subnet tautan WAN `/30` atau *route summary*. | Menggunakan ukuran subnet seragam (FLSM) yang memboroskan/menghabiskan blok alamat sebelum semua divisi kebagian. | Tidak mampu menghitung *Network ID* dan *Broadcast ID* dasar. |
| **2. Efisiensi Ruang Alamat & Bebas Konflik (*Zero Overlap*)**<br>(`Sub-CPMK-2.1`) | **25%** | **0 konflik/tumpang tindih alamat** antar-seluruh segmen organisasi dan menyisakan ruang alamat cadangan secara rapi dan terencana. | Seluruh segmen bebas tumpang tindih (*zero overlap*) dan memenuhi kebutuhan jumlah host tiap divisi. | Bebas tumpang tindih pada segmen utama, namun terdapat 1 batas blok yang melompat kurang efisien. | Terjadi **tumpang tindih ruang alamat (*address overlap*)** antara dua divisi yang akan memicu konflik fatal di router. | Mayoritas rentang alamat saling bertabrakan atau keluar dari prefix induk. |
| **3. Perancangan Skema Pengalamatan **IPv6****<br>(`Sub-CPMK-2.2`) | **30%** | Pembagian *Subnet ID* pada prefix `/48 → /64` konsisten, aturan penyingkatan heksadesimal (`::` tunggal & hapus nol depan) 100% baku, serta penentuan *Link-Local* dan penjelasan *SLAAC* akurat. | Alokasi subnet IPv6 `/64` per divisi bebas konflik dan aturan penyingkatan penulisan alamat benar. | Mampu membagi subnet IPv6 dasar, namun terdapat 1 kekeliruan penyingkatan (mis. memakai `::` dua kali dalam satu alamat). | Mencampur pola pikir *broadcast* IPv4 ke IPv6 atau salah panjang prefix LAN standar `/64`. | Bagian perancangan IPv6 tidak dikerjakan atau salah total. |

$$\text{Skor UTS} = 0,45(K_1) + 0,25(K_2) + 0,30(K_3)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 25% MK · Mengukur `CPMK-3` / `CPL-11` [C3])
**Objek Penilaian:** Konfigurasi Simulator **VLAN, 802.1Q Trunking, Inter-VLAN,** & **Static/OSPF Routing** + *Live Troubleshooting* di Lab.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Konfigurasi **VLAN, 802.1Q Trunking,** & *Inter-VLAN***<br>(`Sub-CPMK-3.1`) | **40%** | Seluruh VLAN, port akses, *802.1Q Trunk* (lengkap *Native VLAN* non-default & *allowed VLAN*), serta sub-antarmuka/SVI *Inter-VLAN* terkonfigurasi bersih dan rapi. | Konfigurasi VLAN, Trunking, dan *Inter-VLAN Routing* berfungsi penuh menghubungkan seluruh segmen lokal. | VLAN dan *Inter-VLAN* berjalan untuk komunikasi dasar, namun konfigurasi keamanan dasar *trunk/native VLAN* belum diterapkan. | Salah menandai VLAN pada tautan *trunk* sehingga sebagian departemen terisolasi tidak bisa mencapai *gateway*. | Gagal mengonfigurasi VLAN dan *Trunking* dasar. |
| **2. Konfigurasi **Static Routing & Dynamic OSPF****<br>(`Sub-CPMK-3.2`) | **40%** | Seluruh tetangga **OSPF** mencapai `FULL`, *Router-ID* eksplisit, *wildcard mask* presisi, `passive-interface` aktif di sisi LAN, rute *default* terpropagasi, dan *failover* otomatis berhasil mulus saat kabel utama diputus. | Konfigurasi rute statis/default dan OSPF berjalan baik menghasilkan tabel rute lengkap dan konektivitas lintas cabang penuh. | Tetangga OSPF terbentuk dan paket sampai ke tujuan, namun lupa memasang `passive-interface` atau *failover* jalur kedua belum dioptimasi biaya *cost*-nya. | Tabel rute tidak lengkap akibat salah jaringan/area OSPF sehingga komunikasi antar-cabang terputus sebagian. | Protokol OSPF tidak berjalan (*0 neighbor*) dan konektivitas lintas router gagal. |
| **3. Konektivitas *End-to-End* & *Live Troubleshooting* Lab** | **20%** | Konektivitas *end-to-end* 100% dan mahasiswa berhasil menuntaskan kedua *trouble tickets* suntikan penguji secara cepat dan metodis dengan perintah `show`. | Konektivitas penuh terverifikasi dan mahasiswa berhasil memperbaiki minimal 1,5 dari 2 masalah *troubleshooting* di lab. | Konektivitas proyek utama berjalan dan mahasiswa menemukan letak 1 masalah dengan petunjuk ringan. | Tidak mampu menggunakan `show ip route` / `show interfaces trunk` untuk mendiagnosis kerusakan sederhana. | Tidak hadir verifikasi lab atau berkas bukan hasil konfigurasi mandiri. |

$$\text{Skor Tugas 2} = 0,40(K_1) + 0,40(K_2) + 0,20(K_3)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-11` [C4])
**Objek Penilaian:** Proyek Jaringan Organisasi Terintegrasi Layanan (**DNS, DHCP, HTTP, NAT**) & Keamanan **ACL** + Ujian Praktik Individu di Lab.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Konfigurasi Layanan **DNS, DHCP (+ Relay), HTTP, & NAT/PAT****<br>(`Sub-CPMK-4.1`) | **35%** | Klien multi-VLAN otomatis mendapat IP via *DHCP Relay*, membuka server **HTTP** lewat nama domain **DNS**, akses keluar **PAT Overload** dan akses masuk **Static NAT** DMZ terbukti aktif sempurna di `show ip nat translations`. | Keempat layanan (**DHCP, DNS, HTTP, NAT/PAT**) berfungsi dengan benar memenuhi skenario jaringan organisasi. | DHCP, DNS, dan HTTP berjalan di jaringan internal serta PAT keluar berhasil, namun *Static Port Forwarding* DMZ masih perlu perbaikan kecil. | Hanya sebagian kecil layanan yang berjalan (mis. IP klien masih diisi statis manual karena *DHCP Relay* gagal atau NAT terbalik `inside/outside`). | Layanan jaringan dasar gagal berfungsi seluruhnya. |
| **2. Ketepatan Kebijakan Keamanan **Standard & Extended ACL****<br>(`Sub-CPMK-4.2`) | **35%** | Urutan aturan spesifik-ke-umum tepat, tidak terjebak *implicit deny* yang mematikan OSPF/DHCP/DNS sah, ditempatkan pada antarmuka & arah (`in`/`out`) optimal, serta **100% lulus matriks uji positif & negatif**. | Kebijakan *Standard & Extended ACL* memblokir lalu lintas terlarang dan tetap mengizinkan layanan sah sesuai spesifikasi soal. | ACL berhasil memblokir segmen terlarang, namun diletakkan pada lokasi kurang optimal atau tidak sengaja memutus `ping` balasan di satu segmen. | Salah urutan baris (`permit ip any any` ditaruh paling atas!) sehingga aturan blokir di bawahnya tidak pernah tersentuh sama sekali, atau memblokir total seluruh jaringan. | Tidak mengonfigurasi kebijakan keamanan ACL. |
| **3. Dokumentasi Topologi, Tabel IP/Port, & Matriks Uji** | **15%** | Peta topologi berlabel lengkap, tabel pengalamatan & kebijakan port rapi, serta bukti pencacah `matches` pada `show access-lists` terdokumentasi utuh. | Dokumentasi konfigurasi dan tabel hasil pengujian layanan serta ACL lengkap dan jelas. | Dokumentasi mencantumkan topologi dan tangkapan layar uji dasar dengan cukup rapi. | Dokumentasi tidak sinkron dengan isi konfigurasi `running-config` aktual pada berkas simulator. | Tidak menyertakan laporan dokumentasi dan matriks uji. |
| **4. Ujian Praktik Konfigurasi & Sidang Individu di Lab** | **15%** | Mahasiswa sangat sigap menulis dan memasang aturan **Extended ACL** & **NAT** baru langsung di CLI dalam waktu singkat tanpa ragu. | Mahasiswa mampu mengonfigurasi aturan yang diminta pada ujian praktik individu dan menjelaskan logikanya dengan benar. | Mahasiswa berhasil menyelesaikan tugas praktik dasar dengan 1 kali koreksi arah antarmuka (`in/out`). | Tidak mampu menulis sintaks dasar ACL maupun NAT secara mandiri di laboratorium. | Tidak hadir ujian/sidang UAS atau melanggar integritas akademik. |

$$\text{Skor UAS} = 0,35(K_1) + 0,35(K_2) + 0,15(K_3) + 0,15(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF PRAKTIKUM LABORATORIUM MINGGUAN (LAB 1–14)

| Kriteria Formatif Lab | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Akurasi Konfigurasi CLI & Penyimpanan (`wr` / `copy run start`)** | Topologi lab tuntas 100%, konfigurasi tersimpan rapi di NVRAM, dan seluruh uji konektivitas hijau. | Modul praktikum selesai tepat waktu sesuai target indikator mingguan. | Modul selesai minimal 75% di sesi lab dan dituntaskan mandiri. | Gagal menyelesaikan konfigurasi dasar praktikum mingguan. |
| **Kemandirian Diagnostik (`show`, `ping`, `Wireshark`)** | Mampu melacak sendiri letak putusnya paket dari L1 hingga L7 secara sistematis. | Terampil memakai perintah verifikasi untuk memperbaiki salah ketik IP/VLAN. | Masih sering bertanya sebelum memeriksa status antarmuka `show ip interface brief`. | Pasif menyalin skrip perintah tanpa memahami topologi. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-312` (`CPL-07` & `CPL-11` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa mampu membedah paket lintas lapisan dengan **Wireshark** secara tajam, merancang pengalamatan **IPv4 VLSM & IPv6** bebas konflik, mengonfigurasi & memulihkan jaringan **VLAN/Trunking/OSPF**, serta mengamankan infrastruktur layanan (**DNS, DHCP, HTTP, NAT**) dengan **ACL** presisi tinggi. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa menguasai analisis enkapsulasi protokol, perancangan subnetting VLSM/IPv6 efisien, konfigurasi *switching* dan *routing* OSPF, serta implementasi layanan dasar dan *firewall* ACL secara fungsional. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) dalam pembacaan paket dasar, perhitungan subnetting bebas konflik, konfigurasi konektivitas VLAN/routing dasar, serta pemasangan layanan dan ACL sederhana. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih menghasilkan konflik alamat subnet, gagal membangun ketetanggaan routing, atau salah menyusun urutan aturan ACL sehingga mengorbankan konektivitas/keamanan. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai konsep dasar maupun keterampilan konfigurasi jaringan komputer atau melanggar kejujuran akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-312` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menganalisis proses enkapsulasi data lintas lapisan protokol **OSI (7 Layer)** dan **TCP/IP**. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu membedah lalu lintas komunikasi paket (*ARP, TCP, UDP, HTTP*) menggunakan **Wireshark**. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu merancang skema pengalamatan **IPv4 (*VLSM/CIDR*)** multi-divisi secara efisien tanpa konflik alamat. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu merancang dan mengonfigurasi skema pengalamatan **IPv6** dasar tanpa konflik alamat. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu mengonfigurasi *switching* (**VLAN, 802.1Q Trunking,** & *Inter-VLAN*) pada simulator/perangkat jaringan. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu mengonfigurasi *routing* statis dan dinamis (**OSPF**) hingga konektivitas *end-to-end* terverifikasi. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu mengonfigurasi layanan jaringan dasar (**DNS, DHCP, HTTP, NAT/PAT**) secara fungsional. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu mengonfigurasi kebijakan *firewall* sederhana (**Standard & Extended ACL**) untuk mengamankan segmen lokal. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-312`)

```text
==============================================================================================================================
             LEMBAR REKAPITULASI PENILAIAN OBE — STI-312 JARINGAN KOMPUTER (3 SKS: T=2, P=1)
==============================================================================================================================
Semester / TA  : Semester 3 (Ganjil) / 2026-2027     CPL Dibebankan : CPL-07 (P3: 45%) & CPL-11 (KK3: 55%) [Level: Reinforce]
Klaster Rubrik : K-3 (Infrastruktur & Jaringan)      Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (25%)   | T2 (25%)    | UAS (30%)   | NA    | CPL-07 | CPL-11 | Huruf
   |           |                  | [CPMK-1:C4] | [CPMK-2:C3] | [CPMK-3:C3] | [CPMK-4:C4] | Akhir | (45%)  | (55%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 86.0        | 88.0        | 88.0        | 87.50 | 86.89  | 88.00  | A
2  | 250101002 | [Nama Mhs 2]     | 78.0        | 74.0        | 78.0        | 76.0        | 76.40 | 75.78  | 76.91  | B+
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0        | 68.00 | 66.89  | 68.91  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 78.00       | 75.33       | 78.67       | 77.33       | 77.30 | 76.52  | 77.94  | >=65:100%
==============================================================================================================================
```
