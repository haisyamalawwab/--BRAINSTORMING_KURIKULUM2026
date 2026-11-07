# 075_3 — OUTLINE BUKU MODUL DAN PEMBELAJARAN

## STI-521 — Internet untuk Segala (IoT)

**Identitas:** `STI-521` Internet untuk Segala (IoT) · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-312`, `STI-310` · PL-2 · PEO-1 · IRM R · Rubrik K-3.

## Spesifikasi dan peta bab

Empat belas bab untuk pekan 1–7 dan 9–15; pekan 8 dan 16 untuk evaluasi. Sasaran: pengembangan kompetensi STI-521 melalui kasus, latihan dan refleksi. Perangkat: ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana. Peta bab mengikuti kode Sub-CPMK yang ada di RPS; rincian penilaian di dokumen 4–5.

### Bab 1 — Pengantar IoT, Arsitektur 4-Layer (Persepsi, Jaringan, Middleware, Aplikasi) (pekan 1)

- **Tujuan:** Mampu menguraikan arsitektur 4-lapisan IoT dan ekosistem IoT cerdas (C2) (Sub-CPMK-1.1).
- **Pokok bahasan:** definisi dan asumsi Pengantar IoT, Arsitektur 4-Layer (Persepsi, Jaringan, Middleware, Aplikasi); langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Pengantar IoT, Arsitektur 4-Layer (Persepsi, Jaringan, Middleware, Aplikasi) membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Pengantar IoT, Arsitektur 4-Layer (Persepsi, Jaringan, Middleware, Aplikasi), hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 2 — Mikrokontroler ESP32: Pinout, ADC 12-bit, PWM Kontrol LED/Buzzer (pekan 2)

- **Tujuan:** Mampu memprogram pin GPIO ESP32, ADC, DAC, PWM, dan timer interupsi (C3) (Sub-CPMK-1.1).
- **Pokok bahasan:** definisi dan asumsi Mikrokontroler ESP32: Pinout, ADC 12-bit, PWM Kontrol LED/Buzzer; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Mikrokontroler ESP32: Pinout, ADC 12-bit, PWM Kontrol LED/Buzzer membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Mikrokontroler ESP32: Pinout, ADC 12-bit, PWM Kontrol LED/Buzzer, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 3 — Sensor Interfacing: DHT22, HC-SR04, LDR, MQ Gas Sensor (pekan 3)

- **Tujuan:** Mampu membaca sensor suhu, kelembaban, ultrasonik, dan gas MQ (C3) (Sub-CPMK-1.2).
- **Pokok bahasan:** definisi dan asumsi Sensor Interfacing: DHT22, HC-SR04, LDR, MQ Gas Sensor; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Sensor Interfacing: DHT22, HC-SR04, LDR, MQ Gas Sensor membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Sensor Interfacing: DHT22, HC-SR04, LDR, MQ Gas Sensor, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 4 — Aktuator: Relay AC/DC, Servo Motor, Antarmuka Bus I2C (pekan 4)

- **Tujuan:** Mampu mengendalikan aktuator Relay, Servo Motor, dan LCD Display I2C (C3) (Sub-CPMK-1.2).
- **Pokok bahasan:** definisi dan asumsi Aktuator: Relay AC/DC, Servo Motor, Antarmuka Bus I2C; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Aktuator: Relay AC/DC, Servo Motor, Antarmuka Bus I2C membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Aktuator: Relay AC/DC, Servo Motor, Antarmuka Bus I2C, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 5 — Protokol Komunikasi IoT: Komparasi Karakteristik & Overhead Paket (pekan 5)

- **Tujuan:** Mampu membandingkan protokol komunikasi HTTP vs CoAP vs MQTT (C4) (Sub-CPMK-2.1).
- **Pokok bahasan:** definisi dan asumsi Protokol Komunikasi IoT: Komparasi Karakteristik & Overhead Paket; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Protokol Komunikasi IoT: Komparasi Karakteristik & Overhead Paket membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Protokol Komunikasi IoT: Komparasi Karakteristik & Overhead Paket, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 6 — Protokol MQTT: Broker, Publisher, Subscriber, QoS 0/1/2, Retain Flag (pekan 6)

- **Tujuan:** Mampu mengonfigurasi MQTT Broker Mosquitto, Topic Hierarchy, dan QoS (C3) (Sub-CPMK-2.1).
- **Pokok bahasan:** definisi dan asumsi Protokol MQTT: Broker, Publisher, Subscriber, QoS 0/1/2, Retain Flag; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Protokol MQTT: Broker, Publisher, Subscriber, QoS 0/1/2, Retain Flag membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Protokol MQTT: Broker, Publisher, Subscriber, QoS 0/1/2, Retain Flag, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 7 — Pemrograman ESP32 MQTT Client: JSON Payload Serialization (pekan 7)

- **Tujuan:** Mampu memprogram ESP32 mengirim data telemetri JSON via MQTT (C3) (Sub-CPMK-2.1).
- **Pokok bahasan:** definisi dan asumsi Pemrograman ESP32 MQTT Client: JSON Payload Serialization; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Pemrograman ESP32 MQTT Client: JSON Payload Serialization membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Pemrograman ESP32 MQTT Client: JSON Payload Serialization, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 8 — Middleware IoT: Pengenalan Node-RED Engine, Nodes, Flow Architecture (pekan 9)

- **Tujuan:** Mampu menginstalasi dan mengonfigurasi Node-RED Middleware (C3) (Sub-CPMK-2.2).
- **Pokok bahasan:** definisi dan asumsi Middleware IoT: Pengenalan Node-RED Engine, Nodes, Flow Architecture; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Middleware IoT: Pengenalan Node-RED Engine, Nodes, Flow Architecture membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Middleware IoT: Pengenalan Node-RED Engine, Nodes, Flow Architecture, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 9 — Otomasi Proses Node-RED: Function Nodes, Switch, Telegram Bot Alert (pekan 10)

- **Tujuan:** Mampu merancang alur logika otomasi dan alert otomatis pada Node-RED (C4) (Sub-CPMK-2.2).
- **Pokok bahasan:** definisi dan asumsi Otomasi Proses Node-RED: Function Nodes, Switch, Telegram Bot Alert; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Otomasi Proses Node-RED: Function Nodes, Switch, Telegram Bot Alert membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Otomasi Proses Node-RED: Function Nodes, Switch, Telegram Bot Alert, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 10 — Cloud IoT Platforms: ThingsBoard / Blynk Integration & Device Tokens (pekan 11)

- **Tujuan:** Mampu menghubungkan data sensor ke Cloud IoT Platform ThingsBoard/Blynk (C3) (Sub-CPMK-3.1).
- **Pokok bahasan:** definisi dan asumsi Cloud IoT Platforms: ThingsBoard / Blynk Integration & Device Tokens; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Cloud IoT Platforms: ThingsBoard / Blynk Integration & Device Tokens membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Cloud IoT Platforms: ThingsBoard / Blynk Integration & Device Tokens, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 11 — Node-RED, data time-series dan verifikasi integrasi (pekan 12)

- **Tujuan:** Menguji alur, penyimpanan bertimestamp dan notifikasi ambang. (Sub-CPMK-3.2).
- **Pokok bahasan:** definisi dan asumsi Node-RED, data time-series dan verifikasi integrasi; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Node-RED, data time-series dan verifikasi integrasi membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Node-RED, data time-series dan verifikasi integrasi, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 12 — Long Range Wireless: LoRaWAN Gateway, Node Architecture, Payload MAC (pekan 13)

- **Tujuan:** Mampu menguraikan protokol nirkabel jarak jauh LoRa & LoRaWAN (C2) (Sub-CPMK-4.1).
- **Pokok bahasan:** definisi dan asumsi Long Range Wireless: LoRaWAN Gateway, Node Architecture, Payload MAC; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Long Range Wireless: LoRaWAN Gateway, Node Architecture, Payload MAC membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Long Range Wireless: LoRaWAN Gateway, Node Architecture, Payload MAC, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 13 — Keamanan IoT: Enkripsi TLS pada MQTT & Over-The-Air (OTA) Updates (pekan 14)

- **Tujuan:** Mampu menerapkan keamanan payload TLS/SSL dan OTA Firmware Updates (C4) (Sub-CPMK-4.2).
- **Pokok bahasan:** definisi dan asumsi Keamanan IoT: Enkripsi TLS pada MQTT & Over-The-Air (OTA) Updates; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana Keamanan IoT: Enkripsi TLS pada MQTT & Over-The-Air (OTA) Updates membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses Keamanan IoT: Enkripsi TLS pada MQTT & Over-The-Air (OTA) Updates, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

### Bab 14 — PjBL IoT Hardware-Software Integration: Smart Campus / Agriculture (pekan 15)

- **Tujuan:** Mampu mengintegrasikan purwarupa fisik produk IoT smart campus (C6) (Sub-CPMK-4.1).
- **Pokok bahasan:** definisi dan asumsi PjBL IoT Hardware-Software Integration: Smart Campus / Agriculture; langkah penerapan pada kasus; interpretasi hasil, risiko dan keterbatasan.
- **Studi kasus:** Prototipe pemantauan suhu ruang belajar mengirim data dari sensor ke dashboard melalui broker lokal. Jelaskan bagaimana PjBL IoT Hardware-Software Integration: Smart Campus / Agriculture membantu menjawab masalah dan bukti apa yang diperlukan.
- **Latihan:** (1) identifikasi masukan, keluaran dan asumsi; (2) terapkan metode pada contoh kecil; (3) uji hasil terhadap kondisi berbeda dan simpulkan keterbatasannya.
- **Praktikum:** gunakan ESP32 atau simulator, sensor/aktuator tegangan rendah, Mosquitto, Node-RED, InfluxDB dan Grafana; dokumentasikan prosedur, hasil dan minimal satu alternatif solusi. Gunakan hanya bahan dan lingkungan yang diizinkan.
- **Prompt ilustrasi:** diagram edukatif berlabel bahasa Indonesia yang memperlihatkan masukan, proses PjBL IoT Hardware-Software Integration: Smart Campus / Agriculture, hasil dan titik validasi; tanpa data pribadi atau merek yang menyesatkan. Simpan aset bila dibuat di `../assets/ilustrasi_modul/`.

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
