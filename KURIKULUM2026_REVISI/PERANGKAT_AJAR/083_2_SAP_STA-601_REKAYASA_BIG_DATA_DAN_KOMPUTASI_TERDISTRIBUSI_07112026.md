# 083_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN

## STA-601 — Rekayasa Big Data dan Komputasi Terdistribusi (*Big Data Engineering and Distributed Systems*)

**Identitas:** `STA-601` Rekayasa Big Data dan Komputasi Terdistribusi · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `FST-207`, `STI-415` · PL-1 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## Pedoman pelaksanaan

Kasus bersama: Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi. Perangkat: Docker Compose, MinIO, PySpark, Kafka, Parquet/Delta Lake, document store dan wide-column store (mis. MongoDB dan Cassandra); mode lokal atau lingkungan lab terkelola untuk kelas. Pembelajaran menggunakan kelompok kecil dengan bukti kontribusi individual. **TM 100 menit:** pembuka 10, demonstrasi/kasus 75, refleksi 15. **Praktik 170 menit:** briefing 15, pengerjaan 120, pengujian dan umpan balik 25, penutupan 10. **PT 120 menit, BM 120 menit** di luar kelas. Setiap praktik memakai data dan sistem berizin.

### Pertemuan 1 — Master-worker, batch dan streaming

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Master-worker, batch dan streaming.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Petakan driver, worker, storage dan jalur batch/stream untuk kasus koperasi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram komponen dan aliran data. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan paralelisme dan trade-off latensi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 2 — HDFS dan object storage

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait HDFS dan object storage.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bandingkan HDFS dengan MinIO/S3 pada kasus; buat bucket lokal dan uji akses. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Tabel perbandingan, objek contoh dan log. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan perbedaan konsistensi dan semantik rename.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 3 — Partisi, replikasi dan toleransi gagal

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Partisi, replikasi dan toleransi gagal.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Hitung penempatan partisi dan replikasi hipotetis; jelaskan kegagalan satu node. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Rancangan replikasi dan analisis risiko. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan replikasi dari backup.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 4 — NoSQL dan Tugas 1 arsitektur

- **Keterkaitan:** `Sub-CPMK-1.2`, `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait NoSQL dan Tugas 1 arsitektur.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Terapkan operasi tambah, baca dan kueri pada document store dan wide-column store dalam lingkungan latihan; bandingkan model keduanya, lalu serahkan rancangan storage terdistribusi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Skema dokumen, kueri dan hasil document/wide-column, tabel keputusan dan Tugas 1. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan dasar pemilihan partition key.
- **Sumatif:** Tugas 1 20% pada pekan 4, mengukur `CPMK-1`: Rancang master-worker, partisi, replikasi dan pilihan HDFS/object storage pada kasus. Bukti: Diagram, analisis kegagalan dan keputusan storage. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 5 — PySpark DataFrame dan transformasi

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait PySpark DataFrame dan transformasi.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Baca dataset contoh, validasi skema, filter dan agregasi menggunakan DataFrame API. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Notebook PySpark dan output transformasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan transformasi dan action.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 6 — Partisi, join dan Catalyst

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Partisi, join dan Catalyst.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Periksa explain plan, bandingkan join dan partisi pada dataset sama, catat waktu eksekusi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Explain plan dan catatan benchmark lokal. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan shuffle dan skew tanpa klaim kinerja umum.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 7 — Batch pipeline dan kualitas data

- **Keterkaitan:** `Sub-CPMK-2.1`, `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Batch pipeline dan kualitas data.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Tangani rekaman duplikat dan nilai hilang; tulis output ke Parquet dengan partisi yang jelas. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Notebook, data uji dan quality checks. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan idempotensi rerun batch.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 8 — UTS: PySpark batch

- **Keterkaitan:** `Sub-CPMK-2.1`, `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UTS: PySpark batch.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Implementasikan pipeline batch dan jawab pertanyaan tentang skema dan execution plan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Notebook individual dan hasil uji. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Refleksi setelah umpan balik.
- **Sumatif:** UTS 25% pada pekan 8, mengukur `CPMK-2`: Bersihkan dan agregasikan data menggunakan DataFrame, uji kualitas dan jelaskan execution plan. Bukti: Notebook individual, output dan hasil uji. Ujian dikerjakan dan dipertanggungjawabkan individual.

### Pertemuan 9 — Lakehouse dan transaksi ACID

- **Keterkaitan:** `Sub-CPMK-3.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Lakehouse dan transaksi ACID.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Tuliskan tabel Delta atau contoh transaksi yang dapat dijalankan secara lokal; bandingkan dengan Parquet. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Tabel lakehouse dan catatan versi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan format data dengan protokol transaksi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 10 — Kafka: topik, key dan partisi

- **Keterkaitan:** `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Kafka: topik, key dan partisi.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Publikasikan event sintetis dengan key dan konsumer; inspeksi offset dan urutan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Konfigurasi topik, payload dan log. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan ordering dalam partisi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 11 — Structured Streaming dan checkpoint

- **Keterkaitan:** `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Structured Streaming dan checkpoint.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Baca stream Kafka dan simpan output dengan checkpoint lokal; uji restart. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Kode stream, checkpoint dan log recovery. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan keterbatasan jaminan pemrosesan.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 12 — Lakehouse + streaming dan Tugas 2

- **Keterkaitan:** `Sub-CPMK-3.1`, `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Lakehouse + streaming dan Tugas 2.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Gabungkan event dengan penyimpanan lakehouse, uji duplikat dan serahkan milestone. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Pipeline streaming, bukti restart dan Tugas 2. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan late data dan watermark.
- **Sumatif:** Tugas 2 25% pada pekan 12, mengukur `CPMK-3`: Bangun alur Kafka ke lakehouse dengan checkpoint dan uji restart pada lingkungan lokal. Bukti: Kode pipeline, log, checkpoint dan hasil uji. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 13 — Spark SQL dan kualitas fitur

- **Keterkaitan:** `Sub-CPMK-4.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Spark SQL dan kualitas fitur.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Gabungkan batch dan stream melalui kueri analitik, dokumentasikan grain dan validasi fitur. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** SQL, skema fitur dan hasil uji. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan risiko data leakage fitur.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 14 — Spark MLlib dan evaluasi

- **Keterkaitan:** `Sub-CPMK-4.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Spark MLlib dan evaluasi.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Latih model sederhana dengan split benar dan baseline; catat metrik tanpa neural network. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Pipeline MLlib, metrik dan baseline. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan keterbatasan data simulasi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 15 — Integrasi, throughput dan reproducibility

- **Keterkaitan:** `Sub-CPMK-4.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Integrasi, throughput dan reproducibility.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Integrasikan batch, stream dan analitik; ukur throughput/latensi lokal beserta konfigurasi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram, pengukuran dan instruksi replikasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Tentukan batas inferensi dari benchmark lokal.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 16 — UAS: pipeline data terpadu

- **Keterkaitan:** `Sub-CPMK-4.1`, `Sub-CPMK-4.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UAS: pipeline data terpadu.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Demonstrasikan jalur batch dan stream, recovery, analitik dan pembelaan individual. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Repo, demo, pengujian dan laporan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Identifikasi handoff ke MLOps.
- **Sumatif:** UAS 30% pada pekan 16, mengukur `CPMK-4`: Integrasikan data batch dan streaming dengan Spark SQL serta MLlib sederhana. Bukti: Repo, data sintetis, fitur, metrik, demo dan laporan. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

## Acuan, guardrails dan rekonsiliasi

**BoK Dok 043:** `BK-IS02` *Data and Information Management*, `BK-IS18` *Machine Learning and Data Science* (sekunder: Spark MLlib). **Pembina Dok 004:** BK-IS02 primer dan BK-IS18 sekunder; BK-IT07 tercantum di Dok 037.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur terdistribusi Master-Worker, HDFS/S3/MinIO, PySpark DataFrame API, NoSQL document & wide-column, Data Lakehouse Delta Lake/Parquet, Kafka + Structured Streaming, Spark SQL & Spark MLlib, orkestrasi pipeline terdistribusi.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang metode numerik klasik (Bisection, Newton-Raphson, Spline, Romberg, RK4); dilarang training CNN/RNN deep learning penuh (itu ranah `STI-624`); dilarang dashboard BI relasional semata (itu ranah `STI-415`).
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menguasai pipeline data masif batch+streaming; menyerahkan deployment model produksi ke `STA-701` MLOps and AI Pipeline.

Batas tambahan: training CNN/RNN penuh adalah ranah `STI-624`, bukan mata kuliah ini; model MLlib hanya demonstrasi analitik.

**Catatan sumber:** Dok 037/043 menyebut kode lama STI-726 untuk Deep Learning; kode resmi setelah Dok 051 adalah STI-624. Gunakan cluster lokal sebagai simulasi: jangan mengklaim skala produksi atau fault tolerance multi-node tanpa pengujian yang sesuai. Spark MLlib digunakan untuk demonstrasi analitik, sedangkan deployment dan monitoring model produksi diserahkan ke STA-701. Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan. Penyesuaian rencana mingguan di bawah mengutamakan kompetensi dan asesmen sebelum pekan pengumpulan; detail teknologi dari Dok 007 digunakan sejauh tidak melanggar guardrails. Prasyarat dan kode resmi mengikuti Dok 005/051. Perbedaan antar sumber ini perlu dikonfirmasi koordinator.

**Skenario:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.

**Rujukan kurikulum:** Dok 003/004 (CPL, IRM dan BoK); 005/051 (identitas dan prasyarat); 007/043 (materi, CPMK/Sub-CPMK); 008/018 (asesmen); 037/043 (boundary); 053 dan README perangkat ajar (format).

**Pustaka teknis:** Kleppmann, *Designing Data-Intensive Applications* (2017); dokumentasi Apache Spark, Kafka dan Delta Lake.
