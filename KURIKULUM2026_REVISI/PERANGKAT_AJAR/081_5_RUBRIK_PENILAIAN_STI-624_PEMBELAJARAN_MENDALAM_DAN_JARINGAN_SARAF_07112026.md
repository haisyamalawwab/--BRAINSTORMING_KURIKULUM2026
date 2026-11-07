# 081_5 — RUBRIK PENILAIAN PEMBELAJARAN

## STI-624 — Pembelajaran Mendalam & Jaringan Saraf (*Deep Learning & Neural Networks*)

**Identitas:** `STI-624` Pembelajaran Mendalam & Jaringan Saraf · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-413` · PL-1 · PEO-1, PEO-3 · IRM **R** · Klaster K-3.

## 1. Prinsip dan skala

Rubrik adaptasi K-3 Dok 018. Untuk setiap kriteria berikan skor 0–100 dengan acuan **Sangat Baik 81–100**, **Baik 66–80**, **Cukup 56–65**, **Kurang 0–55**; kalikan skor dengan bobot kriteria. Hasil penjumlahan adalah nilai instrumen. Rentang ini merupakan adaptasi operasional dari Dok 018, bukan klaim salinan batas kategori dokumen sumber.

### Tugas 1 — MLP dan backpropagation (pekan 4, 20% MK)

**CPMK:** `CPMK-1`. **Tugas:** Bangun MLP dan training loop pada data berizin; jelaskan gradien, fungsi loss dan regularisasi. **Bukti:** Notebook, skema model, split dan kurva loss.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Kebenaran gradien dan konfigurasi training | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| validitas split | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| interpretasi loss | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| reproduksibilitas | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UTS — CNN dan transfer learning (pekan 8, 25% MK)

**CPMK:** `CPMK-2`. **Tugas:** Latih atau fine-tune CNN pada split yang disediakan, evaluasi per kelas dan jelaskan kesalahan. **Bukti:** Notebook individual, konfigurasi, confusion matrix dan analisis.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| CNN berjalan | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| evaluasi tidak bocor | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| metrik per kelas | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| penjelasan kesalahan | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### Tugas 2 — Model sekuens dan attention (pekan 12, 25% MK)

**CPMK:** `CPMK-3`. **Tugas:** Latih LSTM/GRU, bandingkan dengan baseline dan demonstrasikan attention dengan masking. **Bukti:** Notebook, window temporal, metrik dan perhitungan attention.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Ketepatan urutan dan masking | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| baseline dan metrik | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| analisis error | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| replikasi | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UAS — Purwarupa deep learning terpadu (pekan 16, 30% MK)

**CPMK:** `CPMK-4`. **Tugas:** Buat demo inferensi lokal menggunakan model yang dipilih dengan validasi; uji final sekali pada test terpisah. Profilkan waktu inferensi/latih dan pemakaian memori; bila GPU tersedia bandingkan dengan CPU dengan batch dan prosedur sama, jika tidak dokumentasikan fallback CPU serta rencana eksperimen GPU tanpa mengklaim hasil. **Bukti:** Kode, model card, log eksperimen, laporan uji dan demonstrasi tim.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Kinerja terukur | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| validitas pengujian | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| mitigasi overfitting | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| batas etika dan replikasi | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

## 2. Rubrik formatif dan refleksi

Setiap praktik diberi status **tercapai / perlu perbaikan / belum ditunjukkan** untuk ketepatan proses, kualitas bukti dan penjelasan batas; tidak menambah bobot nilai sumatif. Refleksi persepsi 1–5 (1 sangat tidak setuju sampai 5 sangat setuju): saya dapat menjelaskan konsep; saya dapat menguji hasil; saya memahami batas dan risiko; saya berkontribusi dalam tim. Refleksi bukan pengganti penilaian capaian.

## 3. Lembar penilaian

| Mahasiswa | Instrumen | Kriteria 1–4 (0–100) | Skor berbobot | CPMK | Umpan balik dan tindak lanjut |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

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
