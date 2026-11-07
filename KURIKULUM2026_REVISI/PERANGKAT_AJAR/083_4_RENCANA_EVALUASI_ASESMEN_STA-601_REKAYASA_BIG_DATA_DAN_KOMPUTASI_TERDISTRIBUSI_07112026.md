# 083_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STA-601 — Rekayasa Big Data dan Komputasi Terdistribusi (*Big Data Engineering and Distributed Systems*)

**Identitas:** `STA-601` Rekayasa Big Data dan Komputasi Terdistribusi · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `FST-207`, `STI-415` · PL-1 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## 1. Arsitektur asesmen dan bukti

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Diagram, analisis kegagalan dan keputusan storage |
| UTS | 8 | 25% | `CPMK-2` | Notebook individual, output dan hasil uji |
| Tugas 2 | 12 | 25% | `CPMK-3` | Kode pipeline, log, checkpoint dan hasil uji |
| UAS | 16 | 30% | `CPMK-4` | Repo, data sintetis, fitur, metrik, demo dan laporan |

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 2. Matriks CPMK dan CPL

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-06` (`P2`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-10` (`KK2`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-06` (`P2`), `CPL-10` (`KK2`) | — | — | 25% | — | 25% |
| `CPMK-4` | `CPL-10` (`KK2`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan.

### Formula dan batas interpretasi

- **Skor instrumen:** jumlah skor kriteria × bobot kriteria dalam rubrik dokumen 5, skala 0–100. **Nilai akhir MK:** 0,20 × T1 + 0,25 × UTS + 0,25 × T2 + 0,30 × UAS.
- **Skor CPMK:** jumlah (bobot instrumen terkait × skor instrumen) dibagi jumlah bobot instrumen CPMK itu; misal skor 80 pada 25% dan 70 pada 30% menghasilkan (25×80 + 30×70)/55 = 74,55.
- **Diagnostik CPL pada mata kuliah:** rata-rata berbobot CPMK yang mendukung CPL, dengan total bobot CPMK sebagai bobot. Ini sarana diagnostik lokal dan bukan pengganti formula agregasi resmi prodi.
- **CPL individu lintas MK menurut Dok 008:** Σ(SKS MK × bobot MK terhadap CPL × nilai akhir MK) / Σ(SKS MK × bobot MK terhadap CPL), pada seluruh MK pembina CPL; bobot ditetapkan prodi. Dok 008 menetapkan ambang 65 serta target 80% kohor mencapai ambang; nilai MK ini saja belum bisa menentukan capaian CPL lulusan.

## 3. Rencana Tugas Mahasiswa dan kisi-kisi ujian

### 3.1 Tugas 1 — Arsitektur penyimpanan terdistribusi

- **Waktu dan bobot:** pekan 4, 20% nilai MK; **CPMK:** `CPMK-1`; **CPL:** `CPL-06` (`P2`).
- **Tujuan:** Mahasiswa (*A*) mampu **menganalisis** arsitektur komputasi terdistribusi Master-Worker, HDFS dan object storage S3/MinIO (*B*) pada klaster data skala besar (*C*) secara tepat dan fault-tolerant (*D*).
- **Kasus & instruksi:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi. Rancang master-worker, partisi, replikasi dan pilihan HDFS/object storage pada kasus.
- **Bukti wajib:** Diagram, analisis kegagalan dan keputusan storage.
- **Indikator penilaian:** Akurasi arsitektur; asumsi replikasi; pemilihan storage; keterlacakan argumen. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.2 UTS — PySpark batch

- **Waktu dan bobot:** pekan 8, 25% nilai MK; **CPMK:** `CPMK-2`; **CPL:** `CPL-10` (`KK2`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengimplementasikan** pemrosesan data terdistribusi menggunakan Apache Spark & PySpark DataFrame API (*B*) pada dataset masif batch (*C*) dengan throughput optimal (*D*).
- **Kasus & instruksi:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi. Bersihkan dan agregasikan data menggunakan DataFrame, uji kualitas dan jelaskan execution plan.
- **Bukti wajib:** Notebook individual, output dan hasil uji.
- **Indikator penilaian:** Transformasi benar; validasi skema; pemahaman shuffle; reproduksibilitas. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** ujian praktik individual; dosen memberi dataset atau konfigurasi uji dan menilai hasil serta penjelasan. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.3 Tugas 2 — Lakehouse dan streaming

- **Waktu dan bobot:** pekan 12, 25% nilai MK; **CPMK:** `CPMK-3`; **CPL:** `CPL-06` (`P2`), `CPL-10` (`KK2`).
- **Tujuan:** Mahasiswa (*A*) mampu **menerapkan** arsitektur Data Lakehouse (Delta Lake/Parquet) dan ingesti streaming Apache Kafka (*B*) pada pipeline real-time (*C*) secara andal dan tepat waktu (*D*).
- **Kasus & instruksi:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi. Bangun alur Kafka ke lakehouse dengan checkpoint dan uji restart pada lingkungan lokal.
- **Bukti wajib:** Kode pipeline, log, checkpoint dan hasil uji.
- **Indikator penilaian:** Format dan transaksi; struktur event; pengujian pemulihan; dokumentasi batas jaminan. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.4 UAS — Pipeline analitik batch-stream

- **Waktu dan bobot:** pekan 16, 30% nilai MK; **CPMK:** `CPMK-4`; **CPL:** `CPL-10` (`KK2`).
- **Tujuan:** Mahasiswa (*A*) mampu **merancang** pipeline analitik terdistribusi end-to-end dengan Spark SQL dan Spark MLlib (*B*) untuk memasok model AI produksi (*C*) secara terdokumentasi dan reproducible (*D*).
- **Kasus & instruksi:** Aliran transaksi koperasi sintetis dikonsolidasikan dengan data batch untuk fitur permintaan tanpa memakai data pribadi. Integrasikan data batch dan streaming dengan Spark SQL serta MLlib sederhana.
- **Bukti wajib:** Repo, data sintetis, fitur, metrik, demo dan laporan.
- **Indikator penilaian:** Integrasi benar; kualitas fitur; evaluasi/baseline; replikasi dan batas skala. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

## 4. Umpan balik, remediasi dan PPEPP

Dosen menyimpan bukti per mahasiswa, hasil tiap kriteria dan nilai CPMK; menyampaikan umpan balik serta mengatur remediasi sesuai peraturan prodi tanpa menciptakan komponen nilai kelima. Pada akhir semester, hitung capaian, identifikasi indikator bermasalah, analisis penyebab, usulkan perubahan materi/asesmen dan catat penanggung jawab, tenggat serta hasil tindak lanjut pada siklus PPEPP.

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
