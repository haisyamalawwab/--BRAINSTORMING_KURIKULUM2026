# 075_2 — SATUAN ACARA PERKULIAHAN 16 PERTEMUAN

## STI-521 — Internet untuk Segala (IoT)

**Identitas:** `STI-521` Internet untuk Segala (IoT) · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-312`, `STI-310` · PL-2 · PEO-1 · IRM R · Rubrik K-3.

## Pedoman pelaksanaan

Kasus utama: Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Perangkat: ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana. Setiap minggu mengikuti TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit. Penilaian formatif tidak menambah bobot sumatif. Metode kasus/proyek: mahasiswa menghasilkan bukti, menerima umpan balik, lalu merevisi.

### Pertemuan 1 — Pengantar IoT, Arsitektur 4-Layer (Persepsi, Jaringan, Middleware, Aplikasi)

**Target:** Mampu menguraikan arsitektur 4-lapisan IoT dan ekosistem IoT cerdas (C2) · **Keterkaitan:** Sub-CPMK-1.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Pengantar IoT, Arsitektur 4-Layer (Persepsi, Jaringan, Middleware, Aplikasi); catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 2 — Mikrokontroler ESP32: Pinout, ADC 12-bit, PWM Kontrol LED/Buzzer

**Target:** Mampu memprogram pin GPIO ESP32, ADC, DAC, PWM, dan timer interupsi (C3) · **Keterkaitan:** Sub-CPMK-1.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Mikrokontroler ESP32: Pinout, ADC 12-bit, PWM Kontrol LED/Buzzer; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 3 — Sensor Interfacing: DHT22, HC-SR04, LDR, MQ Gas Sensor

**Target:** Mampu membaca sensor suhu, kelembaban, ultrasonik, dan gas MQ (C3) · **Keterkaitan:** Sub-CPMK-1.2.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Sensor Interfacing: DHT22, HC-SR04, LDR, MQ Gas Sensor; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 4 — Aktuator: Relay AC/DC, Servo Motor, Antarmuka Bus I2C

**Target:** Mampu mengendalikan aktuator Relay, Servo Motor, dan LCD Display I2C (C3) · **Keterkaitan:** Sub-CPMK-1.2.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Aktuator: Relay AC/DC, Servo Motor, Antarmuka Bus I2C; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

**Titik sumatif:** Tugas 1 (20%); Bangun pembacaan sensor, tampilkan satuan dan kendalikan aktuator berdasarkan ambang.

### Pertemuan 5 — Protokol Komunikasi IoT: Komparasi Karakteristik & Overhead Paket

**Target:** Mampu membandingkan protokol komunikasi HTTP vs CoAP vs MQTT (C4) · **Keterkaitan:** Sub-CPMK-2.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Protokol Komunikasi IoT: Komparasi Karakteristik & Overhead Paket; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 6 — Protokol MQTT: Broker, Publisher, Subscriber, QoS 0/1/2, Retain Flag

**Target:** Mampu mengonfigurasi MQTT Broker Mosquitto, Topic Hierarchy, dan QoS (C3) · **Keterkaitan:** Sub-CPMK-2.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Protokol MQTT: Broker, Publisher, Subscriber, QoS 0/1/2, Retain Flag; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 7 — Pemrograman ESP32 MQTT Client: JSON Payload Serialization

**Target:** Mampu memprogram ESP32 mengirim data telemetri JSON via MQTT (C3) · **Keterkaitan:** Sub-CPMK-2.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Pemrograman ESP32 MQTT Client: JSON Payload Serialization; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 8 — Ujian Praktikum Terjadwal Pemrograman Sensor ESP32 & MQTT Telemetry

**Target:** EVALUASI TENGAH SEMESTER (UTS) · **Keterkaitan:** Sub-CPMK-2.1.

**Asesmen UTS (25%)**: Publikasikan data sensor ke broker terisolasi dengan topik dan QoS sesuai kebutuhan; jelaskan TLS dan perlindungan kredensial. Produk: Kode, topik, log publish/subscribe dan jawaban individual. Kriteria: alur data, format payload, QoS dan autentikasi. Dosen memverifikasi identitas, menjelaskan aturan, mengumpulkan bukti individual dan memberi umpan balik setelah penilaian.

### Pertemuan 9 — Middleware IoT: Pengenalan Node-RED Engine, Nodes, Flow Architecture

**Target:** Mampu menginstalasi dan mengonfigurasi Node-RED Middleware (C3) · **Keterkaitan:** Sub-CPMK-2.2.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Middleware IoT: Pengenalan Node-RED Engine, Nodes, Flow Architecture; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 10 — Otomasi Proses Node-RED: Function Nodes, Switch, Telegram Bot Alert

**Target:** Mampu merancang alur logika otomasi dan alert otomatis pada Node-RED (C4) · **Keterkaitan:** Sub-CPMK-2.2.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Otomasi Proses Node-RED: Function Nodes, Switch, Telegram Bot Alert; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 11 — Cloud IoT Platforms: ThingsBoard / Blynk Integration & Device Tokens

**Target:** Mampu menghubungkan data sensor ke Cloud IoT Platform ThingsBoard/Blynk (C3) · **Keterkaitan:** Sub-CPMK-3.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Cloud IoT Platforms: ThingsBoard / Blynk Integration & Device Tokens; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 12 — Node-RED, data time-series dan verifikasi integrasi

**Target:** Menguji alur, penyimpanan bertimestamp dan notifikasi ambang. · **Keterkaitan:** Sub-CPMK-3.2.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Node-RED, data time-series dan verifikasi integrasi; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

**Titik sumatif:** Tugas 2 (25%); Susun flow Node-RED untuk validasi nilai, penyimpanan time-series dan notifikasi ambang.

### Pertemuan 13 — Long Range Wireless: LoRaWAN Gateway, Node Architecture, Payload MAC

**Target:** Mampu menguraikan protokol nirkabel jarak jauh LoRa & LoRaWAN (C2) · **Keterkaitan:** Sub-CPMK-4.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Long Range Wireless: LoRaWAN Gateway, Node Architecture, Payload MAC; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 14 — Keamanan IoT: Enkripsi TLS pada MQTT & Over-The-Air (OTA) Updates

**Target:** Mampu menerapkan keamanan payload TLS/SSL dan OTA Firmware Updates (C4) · **Keterkaitan:** Sub-CPMK-4.2.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep Keamanan IoT: Enkripsi TLS pada MQTT & Over-The-Air (OTA) Updates; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 15 — PjBL IoT Hardware-Software Integration: Smart Campus / Agriculture

**Target:** Mampu mengintegrasikan purwarupa fisik produk IoT smart campus (C6) · **Keterkaitan:** Sub-CPMK-4.1.

**Skenario luring:** Tatap muka 100 menit: pendahuluan 10, telaah konsep dan kasus 75, simpulan 15. Praktik 170 menit: briefing dan keselamatan 15, kerja terarah 120, pengujian dan umpan balik 25, penutupan 10.

**Tugas terstruktur (PT):** buat artefak atau jawaban atas kasus menggunakan konsep PjBL IoT Hardware-Software Integration: Smart Campus / Agriculture; catat asumsi dan serahkan melalui LMS. **Belajar mandiri (BM):** baca rujukan terkait, periksa hasil dengan contoh berbeda dan tulis satu keterbatasan. **Bukti formatif:** hasil kerja, catatan keputusan dan umpan balik dosen.

### Pertemuan 16 — Sidang Demonstrasi Produk Fisik Sistem IoT & Pengujian Lapangan

**Target:** EVALUASI AKHIR SEMESTER (UAS) · **Keterkaitan:** Sub-CPMK-4.1, Sub-CPMK-4.2.

**Asesmen UAS (30%)**: Integrasikan node, telemetri, middleware dan dashboard; ukur keberhasilan pengiriman dan pemulihan koneksi. Produk: Purwarupa, diagram, instruksi instalasi dan laporan uji. Kriteria: uji ujung-ke-ujung, keamanan koneksi, keandalan dan pembatasan perangkat. Dosen memverifikasi identitas, menjelaskan aturan, mengumpulkan bukti individual dan memberi umpan balik setelah penilaian.

## Batas operasional dan rujukan

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
