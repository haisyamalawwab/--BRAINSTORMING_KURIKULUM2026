# 075_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STI-521 — Internet untuk Segala (IoT)

**Identitas:** `STI-521` Internet untuk Segala (IoT) · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-312`, `STI-310` · PL-2 · PEO-1 · IRM R · Rubrik K-3.

## 1. Identitas dan otorisasi

Prodi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tanggal dan tanda tangan: **diisi pada pengesahan**. Beban per minggu: **TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit**; PT = penugasan terstruktur, BM = belajar mandiri.

## 2. CPL yang dibebankan

| CPL | Rumusan Dok 003 | IRM |
| --- | --- | --- |
| `CPL-11` (`KK3`) | Mampu merancang, mengintegrasikan, dan mengelola infrastruktur komputasi awan (Cloud/DevOps), sistem sensor cerdas (IoT), dan ketahanan siber (*Cybersecurity*) secara andal, terukur, dan aman. | R |
| `CPL-07` (`P3`) | Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (*cloud*), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi. | R |

## 3. CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD (Dok 043) | Bloom | CPL (Dok 004) |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **memprogram** mikrokontroler ESP32 (*B*) untuk membaca sensor analog/digital dan mengendalikan aktuator (*C*) menggunakan antarmuka GPIO/I2C/SPI (*D*). | C3 | CPL-11 (KK3) |
| `CPMK-2` | Mahasiswa (*A*) mampu **mengimplementasikan** protokol telemetri IoT berkecepatan tinggi (MQTT) (*B*) menggunakan broker Mosquitto (*C*) dengan QoS dan enkripsi payload yang andal (*D*). | C3 | CPL-07 (P3), CPL-11 (KK3) |
| `CPMK-3` | Mahasiswa (*A*) mampu **merancang** alur otomasi middleware (*B*) menggunakan Node-RED (*C*) untuk pemrosesan logika data sensor secara real-time (*D*). | C4 | CPL-11 (KK3) |
| `CPMK-4` | Mahasiswa (*A*) mampu **membangun** purwarupa produk IoT cerdas (*B*) yang terhubung ke dashboard cloud (ThingsBoard/Blynk) dan database time-series (*C*) secara terintegrasi (*D*). | C6 | CPL-11 (KK3) |

| Kode | Kompetensi spesifik Dok 043 | CPMK menurut Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Membuat program perangkat IoT menggunakan pemrograman ESP32. | `CPMK-1` | C3 |
| `Sub-CPMK-1.2` | Mengintegrasikan sensor analog/digital dan aktuator pada perangkat IoT. | `CPMK-1` | C3 |
| `Sub-CPMK-2.1` | Mengimplementasikan komunikasi MQTT (Mosquitto) antara perangkat dan broker. | `CPMK-2` | C3 |
| `Sub-CPMK-2.2` | Merancang alur data IoT menggunakan Node-RED. | `CPMK-2` | C3 |
| `Sub-CPMK-3.1` | Mengintegrasikan perangkat IoT dengan dashboard cloud (ThingsBoard/Blynk). | `CPMK-3` | C4 |
| `Sub-CPMK-3.2` | Merancang penyimpanan data time-series untuk aplikasi IoT. | `CPMK-3` | C4 |
| `Sub-CPMK-4.1` | Membangun aplikasi IoT end-to-end dari sensor hingga dashboard analitik. | `CPMK-4` | C6 |
| `Sub-CPMK-4.2` | Mengevaluasi performa dan keandalan sistem IoT yang dibangun. | `CPMK-4` | C6 |

## 4. Analisis pembelajaran dan korelasi penilaian

Alur belajar: pengenalan dan pemodelan → penerapan dan analisis → integrasi serta evaluasi. Penilaian bersifat kumulatif; pengalokasian nilai CPMK berikut merupakan rancangan operasional, bukan bobot resmi CPL prodi.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-11 (KK3) | 20% | — | — | — | 20% |
| CPMK-2 | CPL-07 (P3), CPL-11 (KK3) | — | 25% | — | — | 25% |
| CPMK-3 | CPL-11 (KK3) | — | — | 25% | — | 25% |
| CPMK-4 | CPL-11 (KK3) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

CPL yang didukung bersama oleh sebuah CPMK menggunakan **bukti yang sama**; nilai tidak dijumlahkan ulang sebagai persentase nilai akhir. Cara menghitung capaian masing-masing CPL dijelaskan di dokumen 4.

**IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 5. Deskripsi dan rencana 16 pertemuan

Mata kuliah mengembangkan kompetensi sesuai CPMK melalui kasus di atas dengan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana. Teknik penilaian dan indikator spesifik tiap instrumen ada pada dokumen 4 dan 5.

| Mg | Sub-CPMK terkait | Kemampuan / indikator | Materi | Metode | Alokasi belajar per minggu | Asesmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sub-CPMK-1.1 | Mampu menguraikan arsitektur 4-lapisan IoT dan ekosistem IoT cerdas (C2) | Pengantar IoT, Arsitektur 4-Layer (Persepsi, Jaringan, Middleware, Aplikasi) | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 2 | Sub-CPMK-1.1 | Mampu memprogram pin GPIO ESP32, ADC, DAC, PWM, dan timer interupsi (C3) | Mikrokontroler ESP32: Pinout, ADC 12-bit, PWM Kontrol LED/Buzzer | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 3 | Sub-CPMK-1.2 | Mampu membaca sensor suhu, kelembaban, ultrasonik, dan gas MQ (C3) | Sensor Interfacing: DHT22, HC-SR04, LDR, MQ Gas Sensor | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 4 | Sub-CPMK-1.2 | Mampu mengendalikan aktuator Relay, Servo Motor, dan LCD Display I2C (C3) | Aktuator: Relay AC/DC, Servo Motor, Antarmuka Bus I2C | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 (20%) |
| 5 | Sub-CPMK-2.1 | Mampu membandingkan protokol komunikasi HTTP vs CoAP vs MQTT (C4) | Protokol Komunikasi IoT: Komparasi Karakteristik & Overhead Paket | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 6 | Sub-CPMK-2.1 | Mampu mengonfigurasi MQTT Broker Mosquitto, Topic Hierarchy, dan QoS (C3) | Protokol MQTT: Broker, Publisher, Subscriber, QoS 0/1/2, Retain Flag | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 7 | Sub-CPMK-2.1 | Mampu memprogram ESP32 mengirim data telemetri JSON via MQTT (C3) | Pemrograman ESP32 MQTT Client: JSON Payload Serialization | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 8 | Sub-CPMK-2.1 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Praktikum Terjadwal Pemrograman Sensor ESP32 & MQTT Telemetry | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS (25%) |
| 9 | Sub-CPMK-2.2 | Mampu menginstalasi dan mengonfigurasi Node-RED Middleware (C3) | Middleware IoT: Pengenalan Node-RED Engine, Nodes, Flow Architecture | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 10 | Sub-CPMK-2.2 | Mampu merancang alur logika otomasi dan alert otomatis pada Node-RED (C4) | Otomasi Proses Node-RED: Function Nodes, Switch, Telegram Bot Alert | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 11 | Sub-CPMK-3.1 | Mampu menghubungkan data sensor ke Cloud IoT Platform ThingsBoard/Blynk (C3) | Cloud IoT Platforms: ThingsBoard / Blynk Integration & Device Tokens | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 12 | Sub-CPMK-3.2 | Menguji alur, penyimpanan bertimestamp dan notifikasi ambang. | Node-RED, data time-series dan verifikasi integrasi | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 (25%) |
| 13 | Sub-CPMK-4.1 | Mampu menguraikan protokol nirkabel jarak jauh LoRa & LoRaWAN (C2) | Long Range Wireless: LoRaWAN Gateway, Node Architecture, Payload MAC | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 14 | Sub-CPMK-4.2 | Mampu menerapkan keamanan payload TLS/SSL dan OTA Firmware Updates (C4) | Keamanan IoT: Enkripsi TLS pada MQTT & Over-The-Air (OTA) Updates | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 15 | Sub-CPMK-4.1 | Mampu mengintegrasikan purwarupa fisik produk IoT smart campus (C6) | PjBL IoT Hardware-Software Integration: Smart Campus / Agriculture | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 16 | Sub-CPMK-4.1, Sub-CPMK-4.2 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Fisik Sistem IoT & Pengujian Lapangan | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS (30%) |

## 6. Ringkasan instrumen

- **Tugas 1 (20%, pekan 4): Node sensor dan aktuator** — Bangun pembacaan sensor, tampilkan satuan dan kendalikan aktuator berdasarkan ambang. Bukti: Diagram rangkaian, program dan rekaman uji tiga kondisi. Cek: pemetaan pin, pembacaan terukur dan keselamatan tegangan rendah.
- **UTS (25%, pekan 8): Ujian telemetri MQTT** — Publikasikan data sensor ke broker terisolasi dengan topik dan QoS sesuai kebutuhan; jelaskan TLS dan perlindungan kredensial. Bukti: Kode, topik, log publish/subscribe dan jawaban individual. Cek: alur data, format payload, QoS dan autentikasi.
- **Tugas 2 (25%, pekan 12): Alur middleware dan penyimpanan** — Susun flow Node-RED untuk validasi nilai, penyimpanan time-series dan notifikasi ambang. Bukti: Flow ekspor, contoh data bertimestamp dan hasil pengujian. Cek: fungsi flow, timestamp, kesalahan input dan jejak hasil.
- **UAS (30%, pekan 16): Demo sistem IoT terpadu** — Integrasikan node, telemetri, middleware dan dashboard; ukur keberhasilan pengiriman dan pemulihan koneksi. Bukti: Purwarupa, diagram, instruksi instalasi dan laporan uji. Cek: uji ujung-ke-ujung, keamanan koneksi, keandalan dan pembatasan perangkat.

## Acuan, batas dan keputusan penyelarasan

**BoK (Dok 043):** `BK-IS03` *IT Infrastructure*, `BK-IT14` *IoT and Embedded Smart Systems*. Klasifikasi pembina menurut Dok 004: sekunder BK-IS03, primer BK-IT14.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur IoT (Perception, Network, Application), Mikrokontroler (ESP32/Arduino), Sensor & Aktuator, Protokol Komunikasi IoT (MQTT, CoAP, HTTP), Edge Data Acquisition, IoT Cloud Integration.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang deep learning video streaming analytics pada hardware edge, desain sirkuit PCB fabrikasi industri, audit keamanan firmware skala besar.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Membangun node sensor cerdas terhubung; menyerahkan analitik pengawasan cerdas ke `STA-703` dan platform perkotaan ke `STI-727`.

**Catatan rekonsiliasi:** Dok 043 mengaitkan alur Node-RED dengan Sub-CPMK-2.2 dan integrasi cloud dengan Sub-CPMK-3.1, sementara rumusan CPMK-3 menekankan middleware; bukti flow dipakai untuk CPMK-3 dan keterkaitan kode sub tetap dicatat. Identitas dan prasyarat mengikuti Dok 005/051; rumusan CPMK/Sub-CPMK mengikuti Dok 043, tema mingguan mengadaptasi Dok 007 sepanjang tidak melanggar batas Dok 037/043. Ketidakcocokan antardokumen dicatat untuk validasi koordinator, bukan diubah diam-diam.

**Skenario terapan:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal.

**Sumber:**
1. Dokumen 003 dan 004: rumusan CPL, matriks IRM dan BoK.
2. Dokumen 005 dan 051: identitas, beban dan prasyarat mata kuliah.
3. Dokumen 007 dan 043: CPMK, Sub-CPMK dan rencana pembelajaran.
4. Dokumen 008 dan 018: pengukuran OBE dan klaster asesmen.
5. Dokumen 037 dan 043: boundary guardrails dan handoff.
6. Rujukan teknis: OASIS MQTT Version 3.1.1; dokumentasi ESP-IDF, Node-RED dan Mosquitto.
