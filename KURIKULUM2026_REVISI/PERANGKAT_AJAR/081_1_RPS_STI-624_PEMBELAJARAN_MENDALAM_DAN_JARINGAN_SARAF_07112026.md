# 081_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE

## STI-624 — Pembelajaran Mendalam & Jaringan Saraf (*Deep Learning & Neural Networks*)

**Identitas:** `STI-624` Pembelajaran Mendalam & Jaringan Saraf · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-413` · PL-1 · PEO-1, PEO-3 · IRM **R** · Klaster K-3.

## 1. Identitas, pembelajaran dan otorisasi

Program Studi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tahun akademik, tanggal dan tanda tangan **diisi pada pengesahan**. Beban mingguan: **TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit**; PT adalah tugas terstruktur, BM belajar mandiri. Waktu ujian dan praktik dapat diatur sesuai kalender akademik tanpa mengubah beban semester.

## 2. CPL yang dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| `CPL-09` (`KK1`) | Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas terintegrasi kecerdasan artifisial (AI/ML, NLP, Computer Vision, Smart Sys, DSS) guna memecahkan masalah kompleks organisasi dan industri. | R |
| `CPL-10` (`KK2`) | Mampu merekayasa pipeline data skala besar (*Data Engineering*), membangun model machine learning/deep learning, serta menerapkan MLOps untuk solusi analitik dan visualisasi data bisnis. | R |

## 3. Rumusan CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD menurut Dok 043 | Bloom | CPL terkait |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **mengonstruksi** arsitektur Multi-Layer Perceptron (MLP) dan mengimplementasikan algoritma Backpropagation (*B*) menggunakan framework PyTorch (*C*) secara matematis dan modular (*D*). | C3 | `CPL-09` (`KK1`) |
| `CPMK-2` | Mahasiswa (*A*) mampu **merancang, melatih, dan mengevaluasi** model Convolutional Neural Networks (CNN) dan arsitektur transfer learning (ResNet, VGG) (*B*) untuk klasifikasi citra medis/industri (*C*) dengan akurasi terukur (*D*). | C5 | `CPL-09` (`KK1`), `CPL-10` (`KK2`) |
| `CPMK-3` | Mahasiswa (*A*) mampu **mengonstruksi** model sekuensial (LSTM, GRU, Transformer Self-Attention) (*B*) untuk pemrosesan bahasa alami atau prediksi runtun waktu (*C*) dengan konvergensi loss yang stabil (*D*). | C5 | `CPL-09` (`KK1`) |
| `CPMK-4` | Mahasiswa (*A*) mampu **membangun** aplikasi deep learning terpadu (*B*) dengan teknik regularisasi (Dropout, Batch Normalization) dan optimasi akselerasi GPU (*C*) secara andal (*D*). | C6 | `CPL-09` (`KK1`) |

| Sub-CPMK Dok 043 | Kompetensi spesifik | CPMK di Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Menerapkan prinsip MLP dan backpropagation pada neural network. | `CPMK-1` | C3 |
| `Sub-CPMK-1.2` | Mengimplementasikan training jaringan saraf tiruan menggunakan PyTorch/TensorFlow. | `CPMK-1` | C3 |
| `Sub-CPMK-2.1` | Mengonstruksi model CNN (ResNet, VGG) untuk klasifikasi citra. | `CPMK-2` | C5 |
| `Sub-CPMK-2.2` | Menerapkan transfer learning dan object detection (YOLO) pada data visual. | `CPMK-2` | C5 |
| `Sub-CPMK-3.1` | Mengonstruksi model RNN/LSTM/GRU untuk data sekuensial. | `CPMK-3` | C5 |
| `Sub-CPMK-3.2` | Menerapkan mekanisme Transformer self-attention pada pemrosesan sekuens. | `CPMK-3` | C5 |
| `Sub-CPMK-4.1` | Menerapkan regularisasi (dropout, batch norm) dan teknik optimasi pada pelatihan model. | `CPMK-4` | C6 |
| `Sub-CPMK-4.2` | Mengevaluasi dan menyempurnakan performa model deep learning pada dataset nyata. | `CPMK-4` | C6 |

## 4. Analisis pembelajaran dan matriks korelasi

Alur: fondasi dan analisis → implementasi terarah → integrasi, pengujian dan refleksi. Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-09` (`KK1`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-09` (`KK1`), `CPL-10` (`KK2`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-09` (`KK1`) | — | — | 25% | — | 25% |
| `CPMK-4` | `CPL-09` (`KK1`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Bobot dalam tabel adalah alokasi terhadap nilai mata kuliah; satu CPMK dapat mendukung beberapa CPL dan tidak boleh dihitung sebagai nilai MK berulang. Lihat dokumen 4 untuk agregasi resmi CPL dan skor diagnostik.

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 5. Deskripsi dan rencana pembelajaran 16 pekan

Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan. Perangkat: Python, PyTorch, notebook dan dataset citra/sekuens berlisensi; GPU opsional dengan fallback CPU. Kegiatan, indikator dan bukti tiap pekan dijabarkan di SAP dan outline modul; asesmen formatif tidak menjadi komponen nilai tambahan.

| Pekan | Sub-CPMK terkait | Topik | Aktivitas / indikator yang dapat diamati | Bukti | Metode | Estimasi belajar | Asesmen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Sub-CPMK-1.1` | Tensor, autograd dan pembagian data | Pisahkan data pelatihan, validasi dan uji sebelum transformasi; hitung gradien tensor sederhana secara manual dan dengan autograd. | Notebook split dan pemeriksaan gradien | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 2 | `Sub-CPMK-1.1` | MLP, aktivasi dan loss | Rancang jaringan kecil dengan dimensi tensor jelas; bandingkan ReLU dan satu alternatif menggunakan data pelatihan. | Diagram dimensi dan notebook forward pass | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 3 | `Sub-CPMK-1.2` | Backpropagation dan optimizer | Hitung gradien satu lapisan lalu latih MLP dengan SGD atau Adam; simpan kurva loss train/validasi. | Turunan ringkas, kode training loop dan log | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 4 | `Sub-CPMK-1.2`, `Sub-CPMK-4.1` | Regularisasi dan evaluasi MLP | Bandingkan model dasar dan dropout pada split tetap; serahkan Tugas 1 dan interpretasikan overfitting. | Notebook reproduksibel, kurva dan Tugas 1 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 1 (20%) |
| 5 | `Sub-CPMK-2.1` | Konvolusi, pooling dan dimensi keluaran | Hitung ukuran keluaran kernel, stride dan padding; bangun CNN kecil untuk klasifikasi citra. | Perhitungan dimensi dan CNN berjalan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 6 | `Sub-CPMK-2.1` | CNN ResNet dan transfer learning | Gunakan bobot pretrained berlisensi dan bandingkan feature extraction dengan fine-tuning terbatas. | Konfigurasi model dan matriks kebingungan validasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 7 | `Sub-CPMK-2.2` | Validasi model visual dan klinik UTS | Evaluasi transfer learning pada set validasi, analisis kelas minoritas serta contoh salah klasifikasi. | Metrik per kelas dan analisis kesalahan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 8 | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | UTS: CNN dan transfer learning | Kerjakan klasifikasi citra individual menggunakan split yang disediakan; jelaskan hasil dan batasnya. | Notebook ujian dan jawaban analisis | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UTS (25%) |
| 9 | `Sub-CPMK-3.1` | RNN dan representasi sekuens | Siapkan window sekuens dengan urutan waktu dan bandingkan prediksi baseline naif serta RNN sederhana. | Dataset window dan baseline sekuens | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 10 | `Sub-CPMK-3.1` | LSTM dan GRU | Latih LSTM atau GRU pada sekuens; catat ukuran batch, horizon dan kurva loss. | Notebook pelatihan serta metrik validasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 11 | `Sub-CPMK-3.2` | Self-attention dan masking | Hitung matriks attention kecil dan implementasikan masking untuk menghindari informasi masa depan. | Perhitungan attention dan uji mask | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 12 | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | Evaluasi sekuens dan Tugas 2 | Bandingkan LSTM/GRU dengan baseline dan uji attention sederhana; serahkan Tugas 2. | Kode, metrik dan analisis kesalahan sekuens | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 2 (25%) |
| 13 | `Sub-CPMK-2.2` | Object detection dan keterbatasan | Gunakan model deteksi pretrained pada citra uji berizin; tafsirkan bounding box dan threshold. | Contoh deteksi, metrik dan catatan false positive | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 14 | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | Optimasi, reproducibility dan etika AI | Catat seed, versi, waktu dan konfigurasi; bandingkan regularisasi tanpa memilih model pada test set. | Model card, log eksperimen dan catatan penggunaan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 15 | `Sub-CPMK-4.2` | Integrasi aplikasi inferensi lokal | Hubungkan model terpilih ke antarmuka lokal dan uji data baru tanpa deployment produksi. | Demo lokal dan uji kasus gagal | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 16 | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | UAS: demonstrasi proyek deep learning | Demonstrasikan model, data split, evaluasi dan alasan pemilihan model dalam pembelaan individual. | Repo, model card, laporan dan demo | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UAS (30%) |

## 6. Ringkasan empat instrumen

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Notebook, skema model, split dan kurva loss |
| UTS | 8 | 25% | `CPMK-2` | Notebook individual, konfigurasi, confusion matrix dan analisis |
| Tugas 2 | 12 | 25% | `CPMK-3` | Notebook, window temporal, metrik dan perhitungan attention |
| UAS | 16 | 30% | `CPMK-4` | Kode, model card, log eksperimen, laporan uji dan demonstrasi tim |

## Acuan, guardrails dan rekonsiliasi

**BoK Dok 043:** `BK-IS18` *Machine Learning*, `BK-IT02` *Applied AI*. **Pembina Dok 004:** BK-IS18 dan BK-IT02 pembina primer menurut tabel Dok 004 (entri Deep Learning berkode lama).

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Multi-Layer Perceptron, Backpropagation, Framework PyTorch, Convolutional Neural Networks (CNN: ResNet, YOLO), Recurrent Networks (LSTM), Self-Attention & Vision Transformer, Transfer Learning.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang mengulang regresi linier biasa, deployment kluster Kubernetes, monitoring model drift operasional.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menghasilkan model deep learning terlatih berperforma tinggi; menyerahkan otomatisasi pipeline dan serving ke `STA-701`.

Handoff: model terlatih dan laporan evaluasi menuju layanan cerdas dan MLOps; tidak membangun deployment Kubernetes atau monitoring drift produksi.

**Catatan sumber:** Dok 043 dan baris IRM/IKU Dok 004 masih menyebut kode lama STI-726 untuk mata kuliah Deep Learning. Berdasarkan identitas serta prasyaratnya, materi tersebut dicocokkan ke STI-624 menurut Dok 005 dan 051; STI-726 kini Integrasi Layanan Cerdas Berbasis AI, bukan Deep Learning. Level Bloom dan Sub-CPMK dipertahankan sesuai sumber. Penggunaan data medis nyata hanya dengan izin dan etika yang relevan; dataset pengajaran anonim lebih aman. Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan. Penyesuaian rencana mingguan di bawah mengutamakan kompetensi dan asesmen sebelum pekan pengumpulan; detail teknologi dari Dok 007 digunakan sejauh tidak melanggar guardrails. Prasyarat dan kode resmi mengikuti Dok 005/051. Perbedaan antar sumber ini perlu dikonfirmasi koordinator.

**Skenario:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.

**Rujukan kurikulum:** Dok 003/004 (CPL, IRM dan BoK); 005/051 (identitas dan prasyarat); 007/043 (materi, CPMK/Sub-CPMK); 008/018 (asesmen); 037/043 (boundary); 053 dan README perangkat ajar (format).

**Pustaka teknis:** Goodfellow, Bengio & Courville, *Deep Learning* (2016); dokumentasi PyTorch dan torchvision; dokumentasi scikit-learn tentang pemisahan data dan metrik.
