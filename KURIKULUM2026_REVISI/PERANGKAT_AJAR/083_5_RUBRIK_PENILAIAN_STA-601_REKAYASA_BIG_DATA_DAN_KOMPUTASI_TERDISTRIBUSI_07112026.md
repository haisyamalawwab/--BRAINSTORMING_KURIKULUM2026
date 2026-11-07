# 083_5 — RUBRIK PENILAIAN PEMBELAJARAN

## STA-601 — Rekayasa Big Data dan Komputasi Terdistribusi (*Big Data Engineering and Distributed Systems*)

**Identitas:** `STA-601` Rekayasa Big Data dan Komputasi Terdistribusi · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `FST-207`, `STI-415` · PL-1 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## 1. Prinsip dan skala

Rubrik adaptasi K-3 Dok 018. Untuk setiap kriteria berikan skor 0–100 dengan acuan **Sangat Baik 81–100**, **Baik 66–80**, **Cukup 56–65**, **Kurang 0–55**; kalikan skor dengan bobot kriteria. Hasil penjumlahan adalah nilai instrumen. Rentang ini merupakan adaptasi operasional dari Dok 018, bukan klaim salinan batas kategori dokumen sumber.

### Tugas 1 — Arsitektur penyimpanan terdistribusi (pekan 4, 20% MK)

**CPMK:** `CPMK-1`. **Tugas:** Rancang master-worker, partisi, replikasi dan pilihan HDFS/object storage pada kasus. **Bukti:** Diagram, analisis kegagalan dan keputusan storage.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Akurasi arsitektur | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| asumsi replikasi | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| pemilihan storage | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| keterlacakan argumen | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UTS — PySpark batch (pekan 8, 25% MK)

**CPMK:** `CPMK-2`. **Tugas:** Bersihkan dan agregasikan data menggunakan DataFrame, uji kualitas dan jelaskan execution plan. **Bukti:** Notebook individual, output dan hasil uji.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Transformasi benar | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| validasi skema | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| pemahaman shuffle | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| reproduksibilitas | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### Tugas 2 — Lakehouse dan streaming (pekan 12, 25% MK)

**CPMK:** `CPMK-3`. **Tugas:** Bangun alur Kafka ke lakehouse dengan checkpoint dan uji restart pada lingkungan lokal. **Bukti:** Kode pipeline, log, checkpoint dan hasil uji.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Format dan transaksi | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| struktur event | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| pengujian pemulihan | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| dokumentasi batas jaminan | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UAS — Pipeline analitik batch-stream (pekan 16, 30% MK)

**CPMK:** `CPMK-4`. **Tugas:** Integrasikan data batch dan streaming dengan Spark SQL serta MLlib sederhana. **Bukti:** Repo, data sintetis, fitur, metrik, demo dan laporan.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Integrasi benar | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| kualitas fitur | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| evaluasi/baseline | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| replikasi dan batas skala | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

## 2. Rubrik formatif dan refleksi

Setiap praktik diberi status **tercapai / perlu perbaikan / belum ditunjukkan** untuk ketepatan proses, kualitas bukti dan penjelasan batas; tidak menambah bobot nilai sumatif. Refleksi persepsi 1–5 (1 sangat tidak setuju sampai 5 sangat setuju): saya dapat menjelaskan konsep; saya dapat menguji hasil; saya memahami batas dan risiko; saya berkontribusi dalam tim. Refleksi bukan pengganti penilaian capaian.

## 3. Lembar penilaian

| Mahasiswa | Instrumen | Kriteria 1–4 (0–100) | Skor berbobot | CPMK | Umpan balik dan tindak lanjut |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

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
