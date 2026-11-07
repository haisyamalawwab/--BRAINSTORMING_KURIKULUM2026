# 074_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STI-520 — Penambangan Data & Visualisasi Data

**Identitas:** `STI-520` Penambangan Data & Visualisasi Data · Semester 5 · 3 SKS (+P) · Prasyarat: `STI-413`, `STI-415` · PL-1 · PEO-1 · IRM R · Rubrik K-3 (adaptasi analitik data).

## 1. Identitas dan otorisasi

Prodi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tanggal dan tanda tangan: **diisi pada pengesahan**. Beban per minggu: **TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit**; PT = penugasan terstruktur, BM = belajar mandiri.

## 2. CPL yang dibebankan

| CPL | Rumusan Dok 003 | IRM |
| --- | --- | --- |
| `CPL-10` (`KK2`) | Mampu merekayasa pipeline data skala besar (*Data Engineering*), membangun model machine learning/deep learning, serta menerapkan MLOps untuk solusi analitik dan visualisasi data bisnis. | R |
| `CPL-06` (`P2`) | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital. | R |

## 3. CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD (Dok 043) | Bloom | CPL (Dok 004) |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **menerapkan** algoritma penambangan aturan asosiasi (Apriori, FP-Growth) (*B*) pada data transaksi belanja (*C*) dengan analisis Support, Confidence, dan Lift Ratio yang valid (*D*). | C3 | CPL-10 (KK2) |
| `CPMK-2` | Mahasiswa (*A*) mampu **mengimplementasikan** algoritma klastering tingkat lanjut (DBSCAN, Hierarchical Clustering) (*B*) pada data spasial/multivariat (*C*) dengan evaluasi skor Davies-Bouldin (*D*). | C4 | CPL-10 (KK2) |
| `CPMK-3` | Mahasiswa (*A*) mampu **mendeteksi** anomali dan pencilan (*Outliers*) (*B*) menggunakan algoritma Isolation Forest dan Local Outlier Factor (*C*) secara akurat (*D*). | C4 | CPL-06 (P2), CPL-10 (KK2) |
| `CPMK-4` | Mahasiswa (*A*) mampu **merancang** visualisasi data interaktif dan narasi wawasan bisnis (*Data Storytelling*) (*B*) menggunakan Python Plotly/Seaborn (*C*) secara estetik dan komunikatif (*D*). | C6 | CPL-10 (KK2) |

| Kode | Kompetensi spesifik Dok 043 | CPMK menurut Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Menerapkan alur CRISP-DM dan exploratory data analysis pada dataset nyata. | `CPMK-1` | C3 |
| `Sub-CPMK-1.2` | Mengimplementasikan visualisasi eksplorasi data menggunakan Seaborn dan Plotly. | `CPMK-1` | C3 |
| `Sub-CPMK-2.1` | Mengimplementasikan association rule mining (Apriori dan FP-Growth). | `CPMK-2` | C4 |
| `Sub-CPMK-2.2` | Menerapkan clustering lanjut (DBSCAN, Hierarchical) untuk segmentasi data. | `CPMK-2` | C4 |
| `Sub-CPMK-3.1` | Mendeteksi outlier menggunakan Isolation Forest dan LOF. | `CPMK-3` | C4 |
| `Sub-CPMK-3.2` | Menganalisis reduksi dimensi PCA dan t-SNE pada data berdimensi tinggi. | `CPMK-3` | C4 |
| `Sub-CPMK-4.1` | Membangun dashboard visualisasi data interaktif untuk eksekutif. | `CPMK-4` | C6 |
| `Sub-CPMK-4.2` | Menyusun laporan insight data berbasis visualisasi yang komunikatif. | `CPMK-4` | C6 |

## 4. Analisis pembelajaran dan korelasi penilaian

Alur belajar: pengenalan dan pemodelan → penerapan dan analisis → integrasi serta evaluasi. Penilaian bersifat kumulatif; pengalokasian nilai CPMK berikut merupakan rancangan operasional, bukan bobot resmi CPL prodi.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-10 (KK2) | 20% | — | — | — | 20% |
| CPMK-2 | CPL-10 (KK2) | — | 25% | — | — | 25% |
| CPMK-3 | CPL-06 (P2), CPL-10 (KK2) | — | — | 25% | — | 25% |
| CPMK-4 | CPL-10 (KK2) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

CPL yang didukung bersama oleh sebuah CPMK menggunakan **bukti yang sama**; nilai tidak dijumlahkan ulang sebagai persentase nilai akhir. Cara menghitung capaian masing-masing CPL dijelaskan di dokumen 4.

**IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75% nilai direncanakan melalui case method / proyek tim. Target Dok 004 65% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 5. Deskripsi dan rencana 16 pertemuan

Mata kuliah mengembangkan kompetensi sesuai CPMK melalui kasus di atas dengan Python, pandas, scikit-learn, mlxtend, Seaborn dan Plotly. Teknik penilaian dan indikator spesifik tiap instrumen ada pada dokumen 4 dan 5.

| Mg | Sub-CPMK terkait | Kemampuan / indikator | Materi | Metode | Alokasi belajar per minggu | Asesmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sub-CPMK-1.1 | Mampu menguraikan metodologi CRISP-DM dan taksonomi Data Mining (C2) | Pengantar Data Mining, Siklus Bisnis CRISP-DM, Taksonomi Pola Data | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 2 | Sub-CPMK-1.1 | Mampu melakukan penanganan data imbalanced (SMOTE) & seleksi fitur (C3) | Advanced Data Preprocessing: Resampling SMOTE, Feature Selection | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 3 | Sub-CPMK-2.1 | Mampu menguraikan konsep Market Basket Analysis dan metrik asosiasi (C2) | Aturan Asosiasi: Konsep Itemset, Support, Confidence, Lift | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 4 | Sub-CPMK-2.1 | Menghitung dan memvalidasi support, confidence dan lift atas transaksi. | Apriori dan perbandingan FP-Growth | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 (20%) |
| 5 | Sub-CPMK-2.2 | Membandingkan hasil perubahan eps dan minPts. | DBSCAN: parameter dan noise | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 6 | Sub-CPMK-2.2 | Menafsirkan linkage dan memeriksa segmentasi multivariat. | Hierarchical clustering dan dendrogram | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 7 | Sub-CPMK-2.2 | Membandingkan hasil klaster serta menyebutkan batas interpretasi noise. | Validasi Davies-Bouldin dan persiapan UTS | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 8 | Sub-CPMK-2.2 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Aturan Asosiasi (Apriori/FP-Growth) & Klastering DBSCAN | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS (25%) |
| 9 | Sub-CPMK-3.1 | Mengevaluasi skor pencilan serta memeriksa contoh secara kritis. | Deteksi anomali Isolation Forest | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 10 | Sub-CPMK-3.1 | Membandingkan pencilan lokal dan global. | Local Outlier Factor dan perbandingan | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 11 | Sub-CPMK-3.2 | Menafsirkan proyeksi dan keterbatasan visual jarak. | Reduksi dimensi PCA dan t-SNE | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 12 | Sub-CPMK-3.1, Sub-CPMK-3.2 | Memverifikasi hasil analisis dan menyerahkan Tugas 2. | Analisis anomali terintegrasi | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 (25%) |
| 13 | Sub-CPMK-1.2 | Mampu menerapkan prinsip persepsi visual Gestalt & hierarki grafik (C3) | Prinsip Visualisasi Data Ilmiah: Teori Gestalt, Pemilihan Chart | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 14 | Sub-CPMK-4.1 | Mampu merancang visualisasi interaktif via Plotly & Seaborn (C6) | Interactive Data Visualization: Plotly Dynamic Charts & Heatmaps | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 15 | Sub-CPMK-4.2 | Mampu menyusun presentasi Data Storytelling wawasan bisnis eksekutif (C6) | Data Storytelling Studio: Narasi Wawasan Bisnis & Dasbor Eksekutif | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif, tanpa bobot |
| 16 | Sub-CPMK-4.1, Sub-CPMK-4.2 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Presentasi Portofolio Data Storytelling & Ujian Komprehensif Data Mining | Case method / proyek; teori dan praktik | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS (30%) |

## 6. Ringkasan instrumen

- **Tugas 1 (20%, pekan 4): Asosiasi transaksi** — Bersihkan transaksi dan hitung support, confidence, lift; bandingkan Apriori dan FP-Growth pada data yang sama. Bukti: Notebook reproduksibel, aturan terpilih dan interpretasi bisnis. Cek: verifikasi hitungan contoh manual; dukungan dan lift; keterbatasan asosiasi.
- **UTS (25%, pekan 8): Ujian klastering** — Uji DBSCAN dan hierarchical clustering pada data multivariat; jelaskan skala, noise dan validasi Davies-Bouldin. Bukti: Notebook individual dan jawaban interpretasi klaster. Cek: pemilihan parameter, preprocessing, penanganan noise dan validasi.
- **Tugas 2 (25%, pekan 12): Analisis anomali** — Bandingkan Isolation Forest dan LOF, gunakan PCA/t-SNE sebagai visualisasi pendukung dan analisis kasus anomali. Bukti: Notebook, tabel pencilan, alasan dan keterbatasan tanpa klaim label pasti. Cek: perbandingan metode dan interpretasi, tidak menganggap skor sebagai probabilitas.
- **UAS (30%, pekan 16): Visualisasi dan data storytelling** — Rancang narasi analitik interaktif tentang pola, segmen dan anomali untuk pemangku kepentingan. Bukti: Dashboard interaktif, narasi, data dictionary, notebook dan presentasi. Cek: pemilihan grafik, transparansi sampel, ketepatan dan keterbacaan.

## Acuan, batas dan keputusan penyelarasan

**BoK (Dok 043):** `BK-IS13` *Data Analytics*, `BK-IT09` *Data Analytics & Visualization*. Klasifikasi pembina menurut Dok 004: primer BK-IS13 dan BK-IT09; BK-IS02 juga primer.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Eksplorasi Data Lanjut (EDA), Association Rule Mining (Apriori, FP-Growth), Advanced Clustering (DBSCAN), Anomaly Detection, Prinsip Visualisasi Informasi Kognitif, Storytelling with Data.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang arsitektur cluster Big Data terdistribusi (itu ranah `STA-601`); deployment streaming event-driven platform skala enterprise (itu ranah `STA-601` + `STA-701`); training neural networks computer vision.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menguasai analisis data tabular lokal; menyerahkan pemrosesan data skala besar dan pipeline terdistribusi ke `STA-601` (Big Data Engineering); menyerahkan sistem pendukung keputusan eksekutif ke `STA-501`.

**Catatan rekonsiliasi:** Dok 043 menempatkan asosiasi pada Sub-CPMK-2.1 meskipun rumusan CPMK-1 membahas asosiasi; indikator tugas mengikuti rumusan CPMK dan kode sub tetap dipertahankan. Visualisasi interaktif berorientasi temuan data, bukan pembuatan dashboard KPI statis milik STI-415. Identitas dan prasyarat mengikuti Dok 005/051; rumusan CPMK/Sub-CPMK mengikuti Dok 043, tema mingguan mengadaptasi Dok 007 sepanjang tidak melanggar batas Dok 037/043. Ketidakcocokan antardokumen dicatat untuk validasi koordinator, bukan diubah diam-diam.

**Skenario terapan:** Data transaksi anonim koperasi kampus digunakan untuk menemukan pola belanja dan mengkomunikasikan temuan tanpa mengklaim hubungan sebab-akibat.

**Sumber:**
1. Dokumen 003 dan 004: rumusan CPL, matriks IRM dan BoK.
2. Dokumen 005 dan 051: identitas, beban dan prasyarat mata kuliah.
3. Dokumen 007 dan 043: CPMK, Sub-CPMK dan rencana pembelajaran.
4. Dokumen 008 dan 018: pengukuran OBE dan klaster asesmen.
5. Dokumen 037 dan 043: boundary guardrails dan handoff.
6. Rujukan teknis: CRISP-DM 1.0; dokumentasi scikit-learn, mlxtend dan Plotly.
