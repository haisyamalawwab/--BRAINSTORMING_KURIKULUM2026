# 083_3 — OUTLINE BUKU MODUL PEMBELAJARAN DAN PRAKTIKUM

## STA-601 — Rekayasa Big Data dan Komputasi Terdistribusi (*Big Data Engineering and Distributed Systems*)

**Identitas:** `STA-601` Rekayasa Big Data dan Komputasi Terdistribusi · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `FST-207`, `STI-415` · PL-1 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## Spesifikasi buku dan peta bab

Empat belas bab untuk pekan 1–7 dan 9–15; pertemuan 8 dan 16 berupa evaluasi. Tiap bab memuat penjelasan konsep, contoh, latihan, praktik dan refleksi; kasus serta perangkat: Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi. Docker Compose, MinIO, PySpark, Kafka, Parquet/Delta Lake, document store dan wide-column store (mis. MongoDB dan Cassandra); mode lokal atau lingkungan lab terkelola untuk kelas. Silabus final dan batas topik mengikuti RPS. Prompt ilustrasi berikut adalah spesifikasi, bukan klaim gambar sudah dibuat.

### Bab 1. Master-worker, batch dan streaming — pekan 1

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Master-worker, batch dan streaming; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Petakan driver, worker, storage dan jalur batch/stream untuk kasus koperasi.
- **Bukti dan kriteria:** Diagram komponen dan aliran data; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan paralelisme dan trade-off latensi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Master-worker, batch dan streaming, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 2. HDFS dan object storage — pekan 2

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi HDFS dan object storage; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Bandingkan HDFS dengan MinIO/S3 pada kasus; buat bucket lokal dan uji akses.
- **Bukti dan kriteria:** Tabel perbandingan, objek contoh dan log; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan perbedaan konsistensi dan semantik rename. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang HDFS dan object storage, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 3. Partisi, replikasi dan toleransi gagal — pekan 3

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Partisi, replikasi dan toleransi gagal; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Hitung penempatan partisi dan replikasi hipotetis; jelaskan kegagalan satu node.
- **Bukti dan kriteria:** Rancangan replikasi dan analisis risiko; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan replikasi dari backup. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Partisi, replikasi dan toleransi gagal, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 4. NoSQL dan Tugas 1 arsitektur — pekan 4

- **Capaian:** Sub-CPMK-1.2, Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi NoSQL dan Tugas 1 arsitektur; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Terapkan operasi tambah, baca dan kueri pada document store dan wide-column store dalam lingkungan latihan; bandingkan model keduanya, lalu serahkan rancangan storage terdistribusi.
- **Bukti dan kriteria:** Skema dokumen, kueri dan hasil document/wide-column, tabel keputusan dan Tugas 1; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan dasar pemilihan partition key. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang NoSQL dan Tugas 1 arsitektur, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 5. PySpark DataFrame dan transformasi — pekan 5

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi PySpark DataFrame dan transformasi; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Baca dataset contoh, validasi skema, filter dan agregasi menggunakan DataFrame API.
- **Bukti dan kriteria:** Notebook PySpark dan output transformasi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan transformasi dan action. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang PySpark DataFrame dan transformasi, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 6. Partisi, join dan Catalyst — pekan 6

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Partisi, join dan Catalyst; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Periksa explain plan, bandingkan join dan partisi pada dataset sama, catat waktu eksekusi.
- **Bukti dan kriteria:** Explain plan dan catatan benchmark lokal; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan shuffle dan skew tanpa klaim kinerja umum. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Partisi, join dan Catalyst, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 7. Batch pipeline dan kualitas data — pekan 7

- **Capaian:** Sub-CPMK-2.1, Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Batch pipeline dan kualitas data; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Tangani rekaman duplikat dan nilai hilang; tulis output ke Parquet dengan partisi yang jelas.
- **Bukti dan kriteria:** Notebook, data uji dan quality checks; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan idempotensi rerun batch. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Batch pipeline dan kualitas data, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 8. Lakehouse dan transaksi ACID — pekan 9

- **Capaian:** Sub-CPMK-3.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Lakehouse dan transaksi ACID; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Tuliskan tabel Delta atau contoh transaksi yang dapat dijalankan secara lokal; bandingkan dengan Parquet.
- **Bukti dan kriteria:** Tabel lakehouse dan catatan versi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan format data dengan protokol transaksi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Lakehouse dan transaksi ACID, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 9. Kafka: topik, key dan partisi — pekan 10

- **Capaian:** Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Kafka: topik, key dan partisi; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Publikasikan event sintetis dengan key dan konsumer; inspeksi offset dan urutan.
- **Bukti dan kriteria:** Konfigurasi topik, payload dan log; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan ordering dalam partisi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Kafka: topik, key dan partisi, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 10. Structured Streaming dan checkpoint — pekan 11

- **Capaian:** Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Structured Streaming dan checkpoint; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Baca stream Kafka dan simpan output dengan checkpoint lokal; uji restart.
- **Bukti dan kriteria:** Kode stream, checkpoint dan log recovery; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan keterbatasan jaminan pemrosesan. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Structured Streaming dan checkpoint, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 11. Lakehouse + streaming dan Tugas 2 — pekan 12

- **Capaian:** Sub-CPMK-3.1, Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Lakehouse + streaming dan Tugas 2; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Gabungkan event dengan penyimpanan lakehouse, uji duplikat dan serahkan milestone.
- **Bukti dan kriteria:** Pipeline streaming, bukti restart dan Tugas 2; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan late data dan watermark. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Lakehouse + streaming dan Tugas 2, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 12. Spark SQL dan kualitas fitur — pekan 13

- **Capaian:** Sub-CPMK-4.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Spark SQL dan kualitas fitur; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Gabungkan batch dan stream melalui kueri analitik, dokumentasikan grain dan validasi fitur.
- **Bukti dan kriteria:** SQL, skema fitur dan hasil uji; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan risiko data leakage fitur. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Spark SQL dan kualitas fitur, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 13. Spark MLlib dan evaluasi — pekan 14

- **Capaian:** Sub-CPMK-4.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Spark MLlib dan evaluasi; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Latih model sederhana dengan split benar dan baseline; catat metrik tanpa neural network.
- **Bukti dan kriteria:** Pipeline MLlib, metrik dan baseline; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan keterbatasan data simulasi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Spark MLlib dan evaluasi, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 14. Integrasi, throughput dan reproducibility — pekan 15

- **Capaian:** Sub-CPMK-4.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Integrasi, throughput dan reproducibility; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi.
- **Aktivitas praktikum:** Integrasikan batch, stream dan analitik; ukur throughput/latensi lokal beserta konfigurasi.
- **Bukti dan kriteria:** Diagram, pengukuran dan instruksi replikasi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Tentukan batas inferensi dari benchmark lokal. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Integrasi, throughput dan reproducibility, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

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
