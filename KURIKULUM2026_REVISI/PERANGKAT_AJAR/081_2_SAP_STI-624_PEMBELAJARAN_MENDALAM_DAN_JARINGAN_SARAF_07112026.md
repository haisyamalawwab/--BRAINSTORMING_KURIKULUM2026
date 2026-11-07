# 081_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN

## STI-624 — Pembelajaran Mendalam & Jaringan Saraf (*Deep Learning & Neural Networks*)

**Identitas:** `STI-624` Pembelajaran Mendalam & Jaringan Saraf · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-413` · PL-1 · PEO-1, PEO-3 · IRM **R** · Klaster K-3.

## Pedoman pelaksanaan

Kasus bersama: Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan. Perangkat: Python, PyTorch, notebook dan dataset citra/sekuens berlisensi; GPU opsional dengan fallback CPU. Pembelajaran menggunakan kelompok kecil dengan bukti kontribusi individual. **TM 100 menit:** pembuka 10, demonstrasi/kasus 75, refleksi 15. **Praktik 170 menit:** briefing 15, pengerjaan 120, pengujian dan umpan balik 25, penutupan 10. **PT 120 menit, BM 120 menit** di luar kelas. Setiap praktik memakai data dan sistem berizin.

### Pertemuan 1 — Tensor, autograd dan pembagian data

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Tensor, autograd dan pembagian data.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Pisahkan data pelatihan, validasi dan uji sebelum transformasi; hitung gradien tensor sederhana secara manual dan dengan autograd. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Notebook split dan pemeriksaan gradien. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bandingkan seed dan dampak data leakage.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 2 — MLP, aktivasi dan loss

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait MLP, aktivasi dan loss.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Rancang jaringan kecil dengan dimensi tensor jelas; bandingkan ReLU dan satu alternatif menggunakan data pelatihan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram dimensi dan notebook forward pass. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan pemilihan loss untuk klasifikasi dan regresi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 3 — Backpropagation dan optimizer

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Backpropagation dan optimizer.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Hitung gradien satu lapisan lalu latih MLP dengan SGD atau Adam; simpan kurva loss train/validasi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Turunan ringkas, kode training loop dan log. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan zero_grad, backward dan step.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 4 — Regularisasi dan evaluasi MLP

- **Keterkaitan:** `Sub-CPMK-1.2`, `Sub-CPMK-4.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Regularisasi dan evaluasi MLP.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bandingkan model dasar dan dropout pada split tetap; serahkan Tugas 1 dan interpretasikan overfitting. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Notebook reproduksibel, kurva dan Tugas 1. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan batch normalization saat train dan eval.
- **Sumatif:** Tugas 1 20% pada pekan 4, mengukur `CPMK-1`: Bangun MLP dan training loop pada data berizin; jelaskan gradien, fungsi loss dan regularisasi. Bukti: Notebook, skema model, split dan kurva loss. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 5 — Konvolusi, pooling dan dimensi keluaran

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Konvolusi, pooling dan dimensi keluaran.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Hitung ukuran keluaran kernel, stride dan padding; bangun CNN kecil untuk klasifikasi citra. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Perhitungan dimensi dan CNN berjalan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Uji perbedaan augmentasi pada data train saja.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 6 — CNN ResNet dan transfer learning

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait CNN ResNet dan transfer learning.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Gunakan bobot pretrained berlisensi dan bandingkan feature extraction dengan fine-tuning terbatas. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Konfigurasi model dan matriks kebingungan validasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan kapan membekukan lapisan.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 7 — Validasi model visual dan klinik UTS

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Validasi model visual dan klinik UTS.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Evaluasi transfer learning pada set validasi, analisis kelas minoritas serta contoh salah klasifikasi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Metrik per kelas dan analisis kesalahan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan akurasi, precision, recall dan F1.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 8 — UTS: CNN dan transfer learning

- **Keterkaitan:** `Sub-CPMK-2.1`, `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UTS: CNN dan transfer learning.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Kerjakan klasifikasi citra individual menggunakan split yang disediakan; jelaskan hasil dan batasnya. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Notebook ujian dan jawaban analisis. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Refleksikan kesalahan setelah umpan balik.
- **Sumatif:** UTS 25% pada pekan 8, mengukur `CPMK-2`: Latih atau fine-tune CNN pada split yang disediakan, evaluasi per kelas dan jelaskan kesalahan. Bukti: Notebook individual, konfigurasi, confusion matrix dan analisis. Ujian dikerjakan dan dipertanggungjawabkan individual.

### Pertemuan 9 — RNN dan representasi sekuens

- **Keterkaitan:** `Sub-CPMK-3.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait RNN dan representasi sekuens.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Siapkan window sekuens dengan urutan waktu dan bandingkan prediksi baseline naif serta RNN sederhana. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Dataset window dan baseline sekuens. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Identifikasi kebocoran masa depan.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 10 — LSTM dan GRU

- **Keterkaitan:** `Sub-CPMK-3.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait LSTM dan GRU.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Latih LSTM atau GRU pada sekuens; catat ukuran batch, horizon dan kurva loss. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Notebook pelatihan serta metrik validasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan peran gate dan gradien terpotong.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 11 — Self-attention dan masking

- **Keterkaitan:** `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Self-attention dan masking.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Hitung matriks attention kecil dan implementasikan masking untuk menghindari informasi masa depan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Perhitungan attention dan uji mask. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan dimensi Q, K, V serta scaling.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 12 — Evaluasi sekuens dan Tugas 2

- **Keterkaitan:** `Sub-CPMK-3.1`, `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Evaluasi sekuens dan Tugas 2.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bandingkan LSTM/GRU dengan baseline dan uji attention sederhana; serahkan Tugas 2. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Kode, metrik dan analisis kesalahan sekuens. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan ketidakpastian prediksi di luar distribusi.
- **Sumatif:** Tugas 2 25% pada pekan 12, mengukur `CPMK-3`: Latih LSTM/GRU, bandingkan dengan baseline dan demonstrasikan attention dengan masking. Bukti: Notebook, window temporal, metrik dan perhitungan attention. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 13 — Object detection dan keterbatasan

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Object detection dan keterbatasan.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Gunakan model deteksi pretrained pada citra uji berizin; tafsirkan bounding box dan threshold. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Contoh deteksi, metrik dan catatan false positive. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan klasifikasi dan deteksi; jelaskan IoU.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 14 — Optimasi, reproducibility dan etika AI

- **Keterkaitan:** `Sub-CPMK-4.1`, `Sub-CPMK-4.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Optimasi, reproducibility dan etika AI.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Catat seed, versi, waktu dan konfigurasi; bandingkan regularisasi tanpa memilih model pada test set. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Model card, log eksperimen dan catatan penggunaan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Periksa lisensi, privasi dan representativitas data.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 15 — Integrasi aplikasi inferensi lokal

- **Keterkaitan:** `Sub-CPMK-4.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Integrasi aplikasi inferensi lokal.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Hubungkan model terpilih ke antarmuka lokal dan uji data baru tanpa deployment produksi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Demo lokal dan uji kasus gagal. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Tentukan keterbatasan dan handoff ke MLOps.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 16 — UAS: demonstrasi proyek deep learning

- **Keterkaitan:** `Sub-CPMK-4.1`, `Sub-CPMK-4.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UAS: demonstrasi proyek deep learning.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Demonstrasikan model, data split, evaluasi dan alasan pemilihan model dalam pembelaan individual. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Repo, model card, laporan dan demo. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Catat umpan balik dan rencana perbaikan.
- **Sumatif:** UAS 30% pada pekan 16, mengukur `CPMK-4`: Buat demo inferensi lokal menggunakan model yang dipilih dengan validasi; uji final sekali pada test terpisah. Profilkan waktu inferensi/latih dan pemakaian memori; bila GPU tersedia bandingkan dengan CPU dengan batch dan prosedur sama, jika tidak dokumentasikan fallback CPU serta rencana eksperimen GPU tanpa mengklaim hasil. Bukti: Kode, model card, log eksperimen, laporan uji dan demonstrasi tim. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

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
