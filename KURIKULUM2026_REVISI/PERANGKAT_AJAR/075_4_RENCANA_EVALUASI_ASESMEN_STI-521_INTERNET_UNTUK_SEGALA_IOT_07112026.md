# 075_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STI-521 — Internet untuk Segala (IoT)

**Identitas:** `STI-521` Internet untuk Segala (IoT) · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-312`, `STI-310` · PL-2 · PEO-1 · IRM R · Rubrik K-3.

## 1. Rancangan empat titik asesmen

| Instrumen | Pekan | Bobot MK | Alokasi CPMK dari bobot MK | Bukti utama | Produk |
| --- | --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 20% | Node sensor dan aktuator | Diagram rangkaian, program dan rekaman uji tiga kondisi |
| UTS | 8 | 25% | CPMK-2 25% | Ujian telemetri MQTT | Kode, topik, log publish/subscribe dan jawaban individual |
| Tugas 2 | 12 | 25% | CPMK-3 25% | Alur middleware dan penyimpanan | Flow ekspor, contoh data bertimestamp dan hasil pengujian |
| UAS | 16 | 30% | CPMK-4 30% | Demo sistem IoT terpadu | Purwarupa, diagram, instruksi instalasi dan laporan uji |

**IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 2. Matriks alokasi per CPMK

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-11 (KK3) | 20% | — | — | — | 20% |
| CPMK-2 | CPL-07 (P3), CPL-11 (KK3) | — | 25% | — | — | 25% |
| CPMK-3 | CPL-11 (KK3) | — | — | 25% | — | 25% |
| CPMK-4 | CPL-11 (KK3) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

### Cara penghitungan ketercapaian

Nilai setiap instrumen (0–100) dihitung dari rubrik dokumen 5. Nilai akhir = jumlah (bobot instrumen / 100 × nilai instrumen). Bila satu instrumen mengukur lebih dari satu CPMK, penguji memberi **skor butir terpisah per CPMK**, bukan menyalin skor total. Skor instrumen = Σ(alokasi bobot MK tiap CPMK pada instrumen × skor bagian CPMK) / bobot instrumen; ini juga mencegah hitung ganda. Nilai CPMK j = Σ(alokasi bobot instrumen untuk j × skor butir j) / Σ(alokasi bobot instrumen untuk j). Nilai CPL = rata-rata tertimbang nilai CPMK yang mendukung CPL tersebut, memakai total alokasi masing-masing CPMK sebagai bobot; hasil antar-CPL tidak dijumlahkan sebagai nilai akhir. Ini rancangan lokal untuk pemantauan, bukan persentase CPL yang telah disahkan.

Contoh operasional: skor butir 80 pada alokasi 20% dan 70 pada alokasi 10% menghasilkan (20×80 + 10×70)/30 = 76,67 untuk CPMK itu. Ambang awal pemantauan 70/100 **usulan**; batas lulus, remedial, proporsi dan kebijakan resmi ditetapkan prodi.

## 3. Kisi-kisi dan rencana tugas

### Tugas 1 — Node sensor dan aktuator

- **Waktu/bobot:** pekan 4, 20% nilai MK. **Kisi-kisi CPMK:** CPMK-1 (20 poin bobot MK).
- **Masalah dan instruksi:** Bangun pembacaan sensor, tampilkan satuan dan kendalikan aktuator berdasarkan ambang.
- **Bukti wajib:** Diagram rangkaian, program dan rekaman uji tiga kondisi.
- **Indikator:** pemetaan pin, pembacaan terukur dan keselamatan tegangan rendah.
- **Pelaksanaan:** kerja berbasis kasus/proyek; penilaian individual melalui kontribusi dan tanya jawab; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### UTS — Ujian telemetri MQTT

- **Waktu/bobot:** pekan 8, 25% nilai MK. **Kisi-kisi CPMK:** CPMK-2 (25 poin bobot MK).
- **Masalah dan instruksi:** Publikasikan data sensor ke broker terisolasi dengan topik dan QoS sesuai kebutuhan; jelaskan TLS dan perlindungan kredensial.
- **Bukti wajib:** Kode, topik, log publish/subscribe dan jawaban individual.
- **Indikator:** alur data, format payload, QoS dan autentikasi.
- **Pelaksanaan:** ujian individual dengan bukti dan klarifikasi lisan; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### Tugas 2 — Alur middleware dan penyimpanan

- **Waktu/bobot:** pekan 12, 25% nilai MK. **Kisi-kisi CPMK:** CPMK-3 (25 poin bobot MK).
- **Masalah dan instruksi:** Susun flow Node-RED untuk validasi nilai, penyimpanan time-series dan notifikasi ambang.
- **Bukti wajib:** Flow ekspor, contoh data bertimestamp dan hasil pengujian.
- **Indikator:** fungsi flow, timestamp, kesalahan input dan jejak hasil.
- **Pelaksanaan:** kerja berbasis kasus/proyek; penilaian individual melalui kontribusi dan tanya jawab; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### UAS — Demo sistem IoT terpadu

- **Waktu/bobot:** pekan 16, 30% nilai MK. **Kisi-kisi CPMK:** CPMK-4 (30 poin bobot MK).
- **Masalah dan instruksi:** Integrasikan node, telemetri, middleware dan dashboard; ukur keberhasilan pengiriman dan pemulihan koneksi.
- **Bukti wajib:** Purwarupa, diagram, instruksi instalasi dan laporan uji.
- **Indikator:** uji ujung-ke-ujung, keamanan koneksi, keandalan dan pembatasan perangkat.
- **Pelaksanaan:** proyek tim dengan bukti kolaborasi, demonstrasi dan pembelaan individual; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

## 4. Integritas, umpan balik dan CQI

Nilai kelompok dikonfirmasi dengan kontribusi dan pembelaan individual. Dosen mencatat skor per butir/CPMK dan umpan balik, memberi kesempatan klarifikasi dan remediasi sesuai peraturan prodi; remediasi tidak otomatis menambah komponen nilai kelima. Pada akhir semester, rekap sebaran capaian tiap CPMK dan CPL, analisis soal/bukti dengan capaian rendah, catat penyebab, rencana perbaikan, penanggung jawab dan tindak lanjut pada siklus PPEPP. Jaga data pribadi dan arsipkan bukti sesuai kebijakan institusi.

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
