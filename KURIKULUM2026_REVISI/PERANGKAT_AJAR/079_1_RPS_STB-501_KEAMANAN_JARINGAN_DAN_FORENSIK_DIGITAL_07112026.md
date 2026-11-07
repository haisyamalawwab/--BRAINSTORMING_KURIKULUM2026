# 079_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STB-501 — Keamanan Jaringan dan Forensik Digital

**Identitas:** `STB-501` Keamanan Jaringan dan Forensik Digital · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-312`, `STI-418` · PL-2 · PEO-1, PEO-3 · IRM R · Rubrik K-3.

## 1. Identitas dan otorisasi

Prodi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tanggal dan tanda tangan: **diisi pada pengesahan**. Beban per minggu: **TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit**; PT = penugasan terstruktur, BM = belajar mandiri.

## 2. CPL yang dibebankan

| CPL | Rumusan Dok 003 | IRM |
| --- | --- | --- |
| `CPL-07` (`P3`) | Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (*cloud*), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi. | R |
| `CPL-11` (`KK3`) | Mampu merancang, mengintegrasikan, dan mengelola infrastruktur komputasi awan (Cloud/DevOps), sistem sensor cerdas (IoT), dan ketahanan siber (*Cybersecurity*) secara andal, terukur, dan aman. | R |
| `CPL-12` (`KK4`) | Mampu merancang tata kelola TI (*IT Governance*), melakukan audit sistem informasi, serta memastikan kepatuhan terhadap standar industri dan manajemen risiko (COBIT, ITIL, ISO 27001). | R |

## 3. CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD (Dok 043) | Bloom | CPL (Dok 004) |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **mengonfigurasi dan menyusun aturan** (*Rules*) Intrusion Detection / Prevention Systems (Snort / Suricata) (*B*) untuk mendeteksi serangan port scan, DoS, dan eksploitasi jaringan (*C*) secara akurat (*D*). | C4 | CPL-07 (P3), CPL-11 (KK3) |
| `CPMK-2` | Mahasiswa (*A*) mampu **menganalisis** bukti transfer data mencurigakan dan jejak eksfiltrasi (*B*) melalui analisis lalu lintas paket jaringan (PCAP) menggunakan Wireshark/Zeek (*C*) secara kritis (*D*). | C4 | CPL-12 (KK4) |
| `CPMK-3` | Mahasiswa (*A*) mampu **melakukan** akuisisi bukti digital (*Bit-Stream Image*) dan analisis forensik memori/disk (*B*) menggunakan Autopsy dan Volatility (*C*) sesuai prinsip Chain of Custody (*D*). | C5 | CPL-12 (KK4) |

| Kode | Kompetensi spesifik Dok 043 | CPMK menurut Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Mengonfigurasi Intrusion Detection/Prevention System (Snort/Suricata). | `CPMK-1` | C4 |
| `Sub-CPMK-1.2` | Menganalisis lalu lintas PCAP menggunakan Wireshark dan Zeek. | `CPMK-1` | C4 |
| `Sub-CPMK-2.1` | Melakukan akuisisi bukti digital (bit-stream image) sesuai standar forensik. | `CPMK-2` | C4 |
| `Sub-CPMK-2.2` | Menganalisis forensik memori/disk menggunakan Autopsy dan Volatility. | `CPMK-2` | C4 |
| `Sub-CPMK-3.1` | Menyusun chain of custody dan laporan investigasi digital forensik. | `CPMK-3` | C5 |
| `Sub-CPMK-3.2` | Mengevaluasi temuan forensik untuk rekomendasi peningkatan keamanan jaringan. | `CPMK-3` | C5 |

## 4. Analisis pembelajaran dan korelasi penilaian

Alur belajar: pengenalan dan pemodelan → penerapan dan analisis → integrasi serta evaluasi. Penilaian bersifat kumulatif; pengalokasian nilai CPMK berikut merupakan rancangan operasional, bukan bobot resmi CPL prodi.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-07 (P3), CPL-11 (KK3) | 20% | 12.5% | — | — | 32.5% |
| CPMK-2 | CPL-12 (KK4) | — | 12.5% | — | — | 12.5% |
| CPMK-3 | CPL-12 (KK4) | — | — | 25% | 30% | 55% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

CPL yang didukung bersama oleh sebuah CPMK menggunakan **bukti yang sama**; nilai tidak dijumlahkan ulang sebagai persentase nilai akhir. Cara menghitung capaian masing-masing CPL dijelaskan di dokumen 4.

**IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 5. Deskripsi dan rencana 16 pertemuan

Mata kuliah mengembangkan kompetensi sesuai CPMK melalui kasus di atas dengan Wireshark, Zeek, Snort/Suricata, Autopsy dan Volatility pada citra latihan. Teknik penilaian dan indikator spesifik tiap instrumen ada pada dokumen 4 dan 5.

| Mg | Sub-CPMK terkait | Kemampuan / indikator | Materi | Metode | Alokasi belajar per minggu | Asesmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sub-CPMK-1.2 | Mampu menguraikan prinsip Defense-in-Depth dan model ancaman jaringan (C2) | Pengantar Network Security Architecture, Vektor Serangan Jaringan, CIA Triad | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 2 | Sub-CPMK-1.2 | Mampu membedah header paket protokol TCP/IP, DNS, ICMP secara mendalam (C4) | Deep Packet Inspection: Analisis Header TCP/IP, Bendera TCP, DNS Query | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 3 | Sub-CPMK-1.1 | Mampu mengonfigurasi Next-Generation Firewall (pfSense/iptables) (C3) | Firewall Architecture: Stateful Packet Filter, DMZ Setup, pfSense Config | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 4 | Sub-CPMK-1.1 | Mampu menguraikan arsitektur NIDS/NIPS (Snort / Suricata) (C2) | Intrusion Detection Systems: Signature-Based vs Anomaly-Based NIDS | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 (20%) |
| 5 | Sub-CPMK-1.1 | Mampu menulis Rule Snort kustom untuk mendeteksi scanning dan exploit (C4) | Snort Rule Writing: Header, Rule Options, Payload Detection, Thresholding | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 6 | Sub-CPMK-1.2 | Mampu menganalisis serangan DoS/DDoS dan menerapkan mitigasi rate limiting (C4) | Denial of Service (DoS/DDoS) Analysis & Mitigasi SYN Flood / UDP Flood | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 7 | Sub-CPMK-1.1 | Mampu mengonfigurasi VPN aman menggunakan protokol WireGuard / IPsec (C3) | Virtual Private Networks: IPsec Site-to-Site & WireGuard Tunneling Setup | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 8 | Sub-CPMK-1.1, Sub-CPMK-1.2 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Praktikum Terjadwal Penulisan Snort Rules & Analisis Paket Wireshark | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS (25%) |
| 9 | Sub-CPMK-2.1 | Mampu menguraikan prinsip forensik digital dan rantai bukti (Chain of Custody) (C2) | Pengantar Forensik Digital: Standar ISO/IEC 27037 & Legalitas Bukti Digital | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 10 | Sub-CPMK-2.1 | Mampu melakukan akuisisi bit-stream image hard disk via FTK Imager / dd (C3) | Akuisisi Bukti Digital: Forensic Imaging, Hashing (MD5/SHA256), Write Blocker | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 11 | Sub-CPMK-2.2 | Mampu merecover berkas terhapus dan menganalisis sistem berkas via Autopsy (C4) | Disk Forensics: Analisis NTFS/ext4, File Carving, Timeline Analysis via Autopsy | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 12 | Sub-CPMK-2.2, Sub-CPMK-3.1 | Mampu melakukan dump RAM volatil dan ekstraksi proses via Volatility (C4) | Memory Forensics: Dump RAM, Analisis Profil Volatility, Injected DLLs | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 (25%) |
| 13 | Sub-CPMK-3.2 | Mampu merekonstruksi linimasa serangan melalui analisis log server ELK (C4) | Log Analysis & SIEM: Sentralisasi Log Syslog, Korelasi Event Serangan | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 14 | Sub-CPMK-1.2, Sub-CPMK-3.2 | Mampu mengekstraksi berkas transfer malware dari berkas pcap Wireshark (C4) | Network Forensics: Ekstraksi Payload Malware & Jejak Eksfiltrasi Data | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 15 | Sub-CPMK-3.1, Sub-CPMK-3.2 | Mampu menyusun Laporan Investigasi Forensik Digital standar BAP Pengadilan (C5) | PjBL Forensik: Penyusunan Dokumen Laporan Ahli Forensik Digital & BAP | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 16 | Sub-CPMK-3.1, Sub-CPMK-3.2 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Ujian Kasus Investigasi Insiden Keamanan & Forensik Siber Terpadu | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS (30%) |

## 6. Ringkasan instrumen

- **Tugas 1 (20%, pekan 4): Pertahanan jaringan** — Analisis trafik latihan dan susun aturan IDS untuk mendeteksi satu pola ancaman, beserta pengujian negatif. Bukti: Aturan IDS, PCAP latihan, hasil alarm dan catatan false positive. Cek: lingkup berizin, kualitas signature dan pengujian.
- **UTS (25%, pekan 8): Ujian IDS dan PCAP** — Tafsirkan paket dan log untuk membedakan aktivitas normal, pemindaian dan dugaan eksfiltrasi; uji aturan deteksi. Bukti: Jawaban individual, filter, potongan log dan alasan. Cek: ketepatan interpretasi paket dan alarm, batas inferensi.
- **Tugas 2 (25%, pekan 12): Akuisisi dan analisis bukti** — Verifikasi hash citra latihan, dokumentasikan chain of custody dan analisis disk/memori tanpa mengubah bukti asli. Bukti: Formulir chain of custody, hash, timeline dan hasil analisis. Cek: integritas bukti, dokumentasi langkah dan validitas temuan.
- **UAS (30%, pekan 16): Laporan investigasi terpadu** — Korelasikan PCAP, log dan artefak forensik; susun kronologi, keterbatasan dan rekomendasi perbaikan. Bukti: Laporan investigasi, tabel bukti, timeline dan presentasi. Cek: keterlacakan sumber, interpretasi kritis, batas kewenangan dan rekomendasi.

## Acuan, batas dan keputusan penyelarasan

**BoK (Dok 043):** `BK-IS06` *Information Security*, `BK-IT06` *Cybersecurity Principles*. Klasifikasi pembina menurut Dok 004: primer BK-IS06 dan BK-IT06; BK-IS03 sekunder.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Keamanan Jaringan Lanjut, Analisis Lalu Lintas Siber (Wireshark/Zeek), Deteksi Intrusi (Snort/Suricata), Metodologi Forensik Digital, Akuisisi Bukti Digital, Analisis Log & Disk Forensics.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang eksploitasi zero-day binary kernel, reverse engineering firmware perangkat keras, audit tata kelola korporat tingkat komisaris.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menguasai pertahanan perimeter dan investigasi insiden; menyerahkan tata kelola risiko ke `STB-602`.

**Catatan rekonsiliasi:** Dok 043 menempatkan analisis PCAP pada Sub-CPMK-1.2 tetapi CPMK-2, dan akuisisi pada Sub-CPMK-2.1 tetapi CPMK-3. Penilaian mengikuti rumusan CPMK dan mencatat kode sub sumber. Contoh malware menggunakan artefak inert, bukan eksekusi malware. Identitas dan prasyarat mengikuti Dok 005/051; rumusan CPMK/Sub-CPMK mengikuti Dok 043, tema mingguan mengadaptasi Dok 007 sepanjang tidak melanggar batas Dok 037/043. Ketidakcocokan antardokumen dicatat untuk validasi koordinator, bukan diubah diam-diam.

**Skenario terapan:** PCAP dan citra disk simulasi insiden laboratorium diberikan bersama mandat investigasi dan catatan akuisisi.

**Sumber:**
1. Dokumen 003 dan 004: rumusan CPL, matriks IRM dan BoK.
2. Dokumen 005 dan 051: identitas, beban dan prasyarat mata kuliah.
3. Dokumen 007 dan 043: CPMK, Sub-CPMK dan rencana pembelajaran.
4. Dokumen 008 dan 018: pengukuran OBE dan klaster asesmen.
5. Dokumen 037 dan 043: boundary guardrails dan handoff.
6. Rujukan teknis: ISO/IEC 27037:2012; dokumentasi Wireshark, Suricata, Autopsy dan Volatility.
