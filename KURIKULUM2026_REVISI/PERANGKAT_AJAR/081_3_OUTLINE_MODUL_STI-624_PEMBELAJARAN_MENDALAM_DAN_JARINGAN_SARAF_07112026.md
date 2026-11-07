# 081_3 — OUTLINE BUKU MODUL PEMBELAJARAN DAN PRAKTIKUM

## STI-624 — Pembelajaran Mendalam & Jaringan Saraf (*Deep Learning & Neural Networks*)

**Identitas:** `STI-624` Pembelajaran Mendalam & Jaringan Saraf · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-413` · PL-1 · PEO-1, PEO-3 · IRM **R** · Klaster K-3.

## Spesifikasi buku dan peta bab

Empat belas bab untuk pekan 1–7 dan 9–15; pertemuan 8 dan 16 berupa evaluasi. Tiap bab memuat penjelasan konsep, contoh, latihan, praktik dan refleksi; kasus serta perangkat: Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan. Python, PyTorch, notebook dan dataset citra/sekuens berlisensi; GPU opsional dengan fallback CPU. Silabus final dan batas topik mengikuti RPS. Prompt ilustrasi berikut adalah spesifikasi, bukan klaim gambar sudah dibuat.

### Bab 1. Tensor, autograd dan pembagian data — pekan 1

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Tensor, autograd dan pembagian data; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Pisahkan data pelatihan, validasi dan uji sebelum transformasi; hitung gradien tensor sederhana secara manual dan dengan autograd.
- **Bukti dan kriteria:** Notebook split dan pemeriksaan gradien; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bandingkan seed dan dampak data leakage. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Tensor, autograd dan pembagian data, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 2. MLP, aktivasi dan loss — pekan 2

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi MLP, aktivasi dan loss; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Rancang jaringan kecil dengan dimensi tensor jelas; bandingkan ReLU dan satu alternatif menggunakan data pelatihan.
- **Bukti dan kriteria:** Diagram dimensi dan notebook forward pass; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan pemilihan loss untuk klasifikasi dan regresi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang MLP, aktivasi dan loss, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 3. Backpropagation dan optimizer — pekan 3

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Backpropagation dan optimizer; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Hitung gradien satu lapisan lalu latih MLP dengan SGD atau Adam; simpan kurva loss train/validasi.
- **Bukti dan kriteria:** Turunan ringkas, kode training loop dan log; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan zero_grad, backward dan step. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Backpropagation dan optimizer, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 4. Regularisasi dan evaluasi MLP — pekan 4

- **Capaian:** Sub-CPMK-1.2, Sub-CPMK-4.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Regularisasi dan evaluasi MLP; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Bandingkan model dasar dan dropout pada split tetap; serahkan Tugas 1 dan interpretasikan overfitting.
- **Bukti dan kriteria:** Notebook reproduksibel, kurva dan Tugas 1; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan batch normalization saat train dan eval. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Regularisasi dan evaluasi MLP, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 5. Konvolusi, pooling dan dimensi keluaran — pekan 5

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Konvolusi, pooling dan dimensi keluaran; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Hitung ukuran keluaran kernel, stride dan padding; bangun CNN kecil untuk klasifikasi citra.
- **Bukti dan kriteria:** Perhitungan dimensi dan CNN berjalan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Uji perbedaan augmentasi pada data train saja. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Konvolusi, pooling dan dimensi keluaran, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 6. CNN ResNet dan transfer learning — pekan 6

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi CNN ResNet dan transfer learning; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Gunakan bobot pretrained berlisensi dan bandingkan feature extraction dengan fine-tuning terbatas.
- **Bukti dan kriteria:** Konfigurasi model dan matriks kebingungan validasi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan kapan membekukan lapisan. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang CNN ResNet dan transfer learning, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 7. Validasi model visual dan klinik UTS — pekan 7

- **Capaian:** Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Validasi model visual dan klinik UTS; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Evaluasi transfer learning pada set validasi, analisis kelas minoritas serta contoh salah klasifikasi.
- **Bukti dan kriteria:** Metrik per kelas dan analisis kesalahan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan akurasi, precision, recall dan F1. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Validasi model visual dan klinik UTS, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 8. RNN dan representasi sekuens — pekan 9

- **Capaian:** Sub-CPMK-3.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi RNN dan representasi sekuens; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Siapkan window sekuens dengan urutan waktu dan bandingkan prediksi baseline naif serta RNN sederhana.
- **Bukti dan kriteria:** Dataset window dan baseline sekuens; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Identifikasi kebocoran masa depan. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang RNN dan representasi sekuens, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 9. LSTM dan GRU — pekan 10

- **Capaian:** Sub-CPMK-3.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi LSTM dan GRU; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Latih LSTM atau GRU pada sekuens; catat ukuran batch, horizon dan kurva loss.
- **Bukti dan kriteria:** Notebook pelatihan serta metrik validasi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan peran gate dan gradien terpotong. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang LSTM dan GRU, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 10. Self-attention dan masking — pekan 11

- **Capaian:** Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Self-attention dan masking; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Hitung matriks attention kecil dan implementasikan masking untuk menghindari informasi masa depan.
- **Bukti dan kriteria:** Perhitungan attention dan uji mask; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan dimensi Q, K, V serta scaling. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Self-attention dan masking, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 11. Evaluasi sekuens dan Tugas 2 — pekan 12

- **Capaian:** Sub-CPMK-3.1, Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Evaluasi sekuens dan Tugas 2; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Bandingkan LSTM/GRU dengan baseline dan uji attention sederhana; serahkan Tugas 2.
- **Bukti dan kriteria:** Kode, metrik dan analisis kesalahan sekuens; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan ketidakpastian prediksi di luar distribusi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Evaluasi sekuens dan Tugas 2, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 12. Object detection dan keterbatasan — pekan 13

- **Capaian:** Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Object detection dan keterbatasan; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Gunakan model deteksi pretrained pada citra uji berizin; tafsirkan bounding box dan threshold.
- **Bukti dan kriteria:** Contoh deteksi, metrik dan catatan false positive; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan klasifikasi dan deteksi; jelaskan IoU. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Object detection dan keterbatasan, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 13. Optimasi, reproducibility dan etika AI — pekan 14

- **Capaian:** Sub-CPMK-4.1, Sub-CPMK-4.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Optimasi, reproducibility dan etika AI; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Catat seed, versi, waktu dan konfigurasi; bandingkan regularisasi tanpa memilih model pada test set.
- **Bukti dan kriteria:** Model card, log eksperimen dan catatan penggunaan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Periksa lisensi, privasi dan representativitas data. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Optimasi, reproducibility dan etika AI, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 14. Integrasi aplikasi inferensi lokal — pekan 15

- **Capaian:** Sub-CPMK-4.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Integrasi aplikasi inferensi lokal; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan.
- **Aktivitas praktikum:** Hubungkan model terpilih ke antarmuka lokal dan uji data baru tanpa deployment produksi.
- **Bukti dan kriteria:** Demo lokal dan uji kasus gagal; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Tentukan keterbatasan dan handoff ke MLOps. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Integrasi aplikasi inferensi lokal, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

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
