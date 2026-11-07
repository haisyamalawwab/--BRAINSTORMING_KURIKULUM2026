# 083_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE

## STA-601 — Rekayasa Big Data dan Komputasi Terdistribusi (*Big Data Engineering and Distributed Systems*)

**Identitas:** `STA-601` Rekayasa Big Data dan Komputasi Terdistribusi · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `FST-207`, `STI-415` · PL-1 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## 1. Identitas, pembelajaran dan otorisasi

Program Studi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tahun akademik, tanggal dan tanda tangan **diisi pada pengesahan**. Beban mingguan: **TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit**; PT adalah tugas terstruktur, BM belajar mandiri. Waktu ujian dan praktik dapat diatur sesuai kalender akademik tanpa mengubah beban semester.

## 2. CPL yang dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| `CPL-06` (`P2`) | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital. | M |
| `CPL-10` (`KK2`) | Mampu merekayasa pipeline data skala besar (*Data Engineering*), membangun model machine learning/deep learning, serta menerapkan MLOps untuk solusi analitik dan visualisasi data bisnis. | M |

## 3. Rumusan CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD menurut Dok 043 | Bloom | CPL terkait |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **menganalisis** arsitektur komputasi terdistribusi Master-Worker, HDFS dan object storage S3/MinIO (*B*) pada klaster data skala besar (*C*) secara tepat dan fault-tolerant (*D*). | C4 | `CPL-06` (`P2`) |
| `CPMK-2` | Mahasiswa (*A*) mampu **mengimplementasikan** pemrosesan data terdistribusi menggunakan Apache Spark & PySpark DataFrame API (*B*) pada dataset masif batch (*C*) dengan throughput optimal (*D*). | C3 | `CPL-10` (`KK2`) |
| `CPMK-3` | Mahasiswa (*A*) mampu **menerapkan** arsitektur Data Lakehouse (Delta Lake/Parquet) dan ingesti streaming Apache Kafka (*B*) pada pipeline real-time (*C*) secara andal dan tepat waktu (*D*). | C4 | `CPL-06` (`P2`), `CPL-10` (`KK2`) |
| `CPMK-4` | Mahasiswa (*A*) mampu **merancang** pipeline analitik terdistribusi end-to-end dengan Spark SQL dan Spark MLlib (*B*) untuk memasok model AI produksi (*C*) secara terdokumentasi dan reproducible (*D*). | C6 | `CPL-10` (`KK2`) |

| Sub-CPMK Dok 043 | Kompetensi spesifik | CPMK di Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Menganalisis arsitektur Master-Worker, HDFS dan object storage S3/MinIO. | `CPMK-1` | C4 |
| `Sub-CPMK-1.2` | Mengevaluasi partisi, replikasi dan fault tolerance klaster terdistribusi. | `CPMK-1` | C4 |
| `Sub-CPMK-2.1` | Mengimplementasikan PySpark DataFrame API dan Catalyst Optimizer. | `CPMK-2` | C3 |
| `Sub-CPMK-2.2` | Menerapkan NoSQL document & wide-column stores untuk data semi-terstruktur. | `CPMK-2` | C3 |
| `Sub-CPMK-3.1` | Menerapkan Data Lakehouse Delta Lake/Parquet dan transaksi ACID. | `CPMK-3` | C4 |
| `Sub-CPMK-3.2` | Menerapkan ingesti streaming Apache Kafka dan Spark Structured Streaming. | `CPMK-3` | C4 |
| `Sub-CPMK-4.1` | Menjalankan analitik Spark SQL masif dan ML terdistribusi Spark MLlib. | `CPMK-4` | C6 |
| `Sub-CPMK-4.2` | Membangun pipeline Big Data end-to-end batch+streaming untuk suplai model AI. | `CPMK-4` | C6 |

## 4. Analisis pembelajaran dan matriks korelasi

Alur: fondasi dan analisis → implementasi terarah → integrasi, pengujian dan refleksi. Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-06` (`P2`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-10` (`KK2`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-06` (`P2`), `CPL-10` (`KK2`) | — | — | 25% | — | 25% |
| `CPMK-4` | `CPL-10` (`KK2`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Bobot dalam tabel adalah alokasi terhadap nilai mata kuliah; satu CPMK dapat mendukung beberapa CPL dan tidak boleh dihitung sebagai nilai MK berulang. Lihat dokumen 4 untuk agregasi resmi CPL dan skor diagnostik.

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 5. Deskripsi dan rencana pembelajaran 16 pekan

Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi. Perangkat: Docker Compose, MinIO, PySpark, Kafka, Parquet/Delta Lake, document store dan wide-column store (mis. MongoDB dan Cassandra); mode lokal atau lingkungan lab terkelola untuk kelas. Kegiatan, indikator dan bukti tiap pekan dijabarkan di SAP dan outline modul; asesmen formatif tidak menjadi komponen nilai tambahan.

| Pekan | Sub-CPMK terkait | Topik | Aktivitas / indikator yang dapat diamati | Bukti | Metode | Estimasi belajar | Asesmen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Sub-CPMK-1.1` | Master-worker, batch dan streaming | Petakan driver, worker, storage dan jalur batch/stream untuk kasus koperasi. | Diagram komponen dan aliran data | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 2 | `Sub-CPMK-1.1` | HDFS dan object storage | Bandingkan HDFS dengan MinIO/S3 pada kasus; buat bucket lokal dan uji akses. | Tabel perbandingan, objek contoh dan log | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 3 | `Sub-CPMK-1.2` | Partisi, replikasi dan toleransi gagal | Hitung penempatan partisi dan replikasi hipotetis; jelaskan kegagalan satu node. | Rancangan replikasi dan analisis risiko | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 4 | `Sub-CPMK-1.2`, `Sub-CPMK-2.2` | NoSQL dan Tugas 1 arsitektur | Terapkan operasi tambah, baca dan kueri pada document store dan wide-column store dalam lingkungan latihan; bandingkan model keduanya, lalu serahkan rancangan storage terdistribusi. | Skema dokumen, kueri dan hasil document/wide-column, tabel keputusan dan Tugas 1 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 1 (20%) |
| 5 | `Sub-CPMK-2.1` | PySpark DataFrame dan transformasi | Baca dataset contoh, validasi skema, filter dan agregasi menggunakan DataFrame API. | Notebook PySpark dan output transformasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 6 | `Sub-CPMK-2.1` | Partisi, join dan Catalyst | Periksa explain plan, bandingkan join dan partisi pada dataset sama, catat waktu eksekusi. | Explain plan dan catatan benchmark lokal | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 7 | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | Batch pipeline dan kualitas data | Tangani rekaman duplikat dan nilai hilang; tulis output ke Parquet dengan partisi yang jelas. | Notebook, data uji dan quality checks | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 8 | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | UTS: PySpark batch | Implementasikan pipeline batch dan jawab pertanyaan tentang skema dan execution plan. | Notebook individual dan hasil uji | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UTS (25%) |
| 9 | `Sub-CPMK-3.1` | Lakehouse dan transaksi ACID | Tuliskan tabel Delta atau contoh transaksi yang dapat dijalankan secara lokal; bandingkan dengan Parquet. | Tabel lakehouse dan catatan versi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 10 | `Sub-CPMK-3.2` | Kafka: topik, key dan partisi | Publikasikan event sintetis dengan key dan konsumer; inspeksi offset dan urutan. | Konfigurasi topik, payload dan log | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 11 | `Sub-CPMK-3.2` | Structured Streaming dan checkpoint | Baca stream Kafka dan simpan output dengan checkpoint lokal; uji restart. | Kode stream, checkpoint dan log recovery | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 12 | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | Lakehouse + streaming dan Tugas 2 | Gabungkan event dengan penyimpanan lakehouse, uji duplikat dan serahkan milestone. | Pipeline streaming, bukti restart dan Tugas 2 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 2 (25%) |
| 13 | `Sub-CPMK-4.1` | Spark SQL dan kualitas fitur | Gabungkan batch dan stream melalui kueri analitik, dokumentasikan grain dan validasi fitur. | SQL, skema fitur dan hasil uji | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 14 | `Sub-CPMK-4.1` | Spark MLlib dan evaluasi | Latih model sederhana dengan split benar dan baseline; catat metrik tanpa neural network. | Pipeline MLlib, metrik dan baseline | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 15 | `Sub-CPMK-4.2` | Integrasi, throughput dan reproducibility | Integrasikan batch, stream dan analitik; ukur throughput/latensi lokal beserta konfigurasi. | Diagram, pengukuran dan instruksi replikasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 16 | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | UAS: pipeline data terpadu | Demonstrasikan jalur batch dan stream, recovery, analitik dan pembelaan individual. | Repo, demo, pengujian dan laporan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UAS (30%) |

## 6. Ringkasan empat instrumen

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Diagram, analisis kegagalan dan keputusan storage |
| UTS | 8 | 25% | `CPMK-2` | Notebook individual, output dan hasil uji |
| Tugas 2 | 12 | 25% | `CPMK-3` | Kode pipeline, log, checkpoint dan hasil uji |
| UAS | 16 | 30% | `CPMK-4` | Repo, data sintetis, fitur, metrik, demo dan laporan |

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
