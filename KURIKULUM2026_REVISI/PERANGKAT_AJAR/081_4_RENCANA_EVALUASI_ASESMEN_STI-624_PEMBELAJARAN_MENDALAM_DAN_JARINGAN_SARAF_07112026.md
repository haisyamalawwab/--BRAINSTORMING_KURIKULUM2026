# 081_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STI-624 — Pembelajaran Mendalam & Jaringan Saraf (*Deep Learning & Neural Networks*)

**Identitas:** `STI-624` Pembelajaran Mendalam & Jaringan Saraf · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-413` · PL-1 · PEO-1, PEO-3 · IRM **R** · Klaster K-3.

## 1. Arsitektur asesmen dan bukti

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Notebook, skema model, split dan kurva loss |
| UTS | 8 | 25% | `CPMK-2` | Notebook individual, konfigurasi, confusion matrix dan analisis |
| Tugas 2 | 12 | 25% | `CPMK-3` | Notebook, window temporal, metrik dan perhitungan attention |
| UAS | 16 | 30% | `CPMK-4` | Kode, model card, log eksperimen, laporan uji dan demonstrasi tim |

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 2. Matriks CPMK dan CPL

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-09` (`KK1`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-09` (`KK1`), `CPL-10` (`KK2`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-09` (`KK1`) | — | — | 25% | — | 25% |
| `CPMK-4` | `CPL-09` (`KK1`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan.

### Formula dan batas interpretasi

- **Skor instrumen:** jumlah skor kriteria × bobot kriteria dalam rubrik dokumen 5, skala 0–100. **Nilai akhir MK:** 0,20 × T1 + 0,25 × UTS + 0,25 × T2 + 0,30 × UAS.
- **Skor CPMK:** jumlah (bobot instrumen terkait × skor instrumen) dibagi jumlah bobot instrumen CPMK itu; misal skor 80 pada 25% dan 70 pada 30% menghasilkan (25×80 + 30×70)/55 = 74,55.
- **Diagnostik CPL pada mata kuliah:** rata-rata berbobot CPMK yang mendukung CPL, dengan total bobot CPMK sebagai bobot. Ini sarana diagnostik lokal dan bukan pengganti formula agregasi resmi prodi.
- **CPL individu lintas MK menurut Dok 008:** Σ(SKS MK × bobot MK terhadap CPL × nilai akhir MK) / Σ(SKS MK × bobot MK terhadap CPL), pada seluruh MK pembina CPL; bobot ditetapkan prodi. Dok 008 menetapkan ambang 65 serta target 80% kohor mencapai ambang; nilai MK ini saja belum bisa menentukan capaian CPL lulusan.

## 3. Rencana Tugas Mahasiswa dan kisi-kisi ujian

### 3.1 Tugas 1 — MLP dan backpropagation

- **Waktu dan bobot:** pekan 4, 20% nilai MK; **CPMK:** `CPMK-1`; **CPL:** `CPL-09` (`KK1`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengonstruksi** arsitektur Multi-Layer Perceptron (MLP) dan mengimplementasikan algoritma Backpropagation (*B*) menggunakan framework PyTorch (*C*) secara matematis dan modular (*D*).
- **Kasus & instruksi:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan. Bangun MLP dan training loop pada data berizin; jelaskan gradien, fungsi loss dan regularisasi.
- **Bukti wajib:** Notebook, skema model, split dan kurva loss.
- **Indikator penilaian:** Kebenaran gradien dan konfigurasi training; validitas split; interpretasi loss; reproduksibilitas. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.2 UTS — CNN dan transfer learning

- **Waktu dan bobot:** pekan 8, 25% nilai MK; **CPMK:** `CPMK-2`; **CPL:** `CPL-09` (`KK1`), `CPL-10` (`KK2`).
- **Tujuan:** Mahasiswa (*A*) mampu **merancang, melatih, dan mengevaluasi** model Convolutional Neural Networks (CNN) dan arsitektur transfer learning (ResNet, VGG) (*B*) untuk klasifikasi citra medis/industri (*C*) dengan akurasi terukur (*D*).
- **Kasus & instruksi:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan. Latih atau fine-tune CNN pada split yang disediakan, evaluasi per kelas dan jelaskan kesalahan.
- **Bukti wajib:** Notebook individual, konfigurasi, confusion matrix dan analisis.
- **Indikator penilaian:** CNN berjalan; evaluasi tidak bocor; metrik per kelas; penjelasan kesalahan. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** ujian praktik individual; dosen memberi dataset atau konfigurasi uji dan menilai hasil serta penjelasan. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.3 Tugas 2 — Model sekuens dan attention

- **Waktu dan bobot:** pekan 12, 25% nilai MK; **CPMK:** `CPMK-3`; **CPL:** `CPL-09` (`KK1`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengonstruksi** model sekuensial (LSTM, GRU, Transformer Self-Attention) (*B*) untuk pemrosesan bahasa alami atau prediksi runtun waktu (*C*) dengan konvergensi loss yang stabil (*D*).
- **Kasus & instruksi:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan. Latih LSTM/GRU, bandingkan dengan baseline dan demonstrasikan attention dengan masking.
- **Bukti wajib:** Notebook, window temporal, metrik dan perhitungan attention.
- **Indikator penilaian:** Ketepatan urutan dan masking; baseline dan metrik; analisis error; replikasi. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.4 UAS — Purwarupa deep learning terpadu

- **Waktu dan bobot:** pekan 16, 30% nilai MK; **CPMK:** `CPMK-4`; **CPL:** `CPL-09` (`KK1`).
- **Tujuan:** Mahasiswa (*A*) mampu **membangun** aplikasi deep learning terpadu (*B*) dengan teknik regularisasi (Dropout, Batch Normalization) dan optimasi akselerasi GPU (*C*) secara andal (*D*).
- **Kasus & instruksi:** Klasifikasi citra produk sintetis/berlisensi dan prediksi sekuens sensor laboratorium; kelompok mendokumentasikan kualitas data dan batas penggunaan. Buat demo inferensi lokal menggunakan model yang dipilih dengan validasi; uji final sekali pada test terpisah. Profilkan waktu inferensi/latih dan pemakaian memori; bila GPU tersedia bandingkan dengan CPU dengan batch dan prosedur sama, jika tidak dokumentasikan fallback CPU serta rencana eksperimen GPU tanpa mengklaim hasil.
- **Bukti wajib:** Kode, model card, log eksperimen, laporan uji dan demonstrasi tim.
- **Indikator penilaian:** Kinerja terukur; validitas pengujian; mitigasi overfitting; batas etika dan replikasi. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

## 4. Umpan balik, remediasi dan PPEPP

Dosen menyimpan bukti per mahasiswa, hasil tiap kriteria dan nilai CPMK; menyampaikan umpan balik serta mengatur remediasi sesuai peraturan prodi tanpa menciptakan komponen nilai kelima. Pada akhir semester, hitung capaian, identifikasi indikator bermasalah, analisis penyebab, usulkan perubahan materi/asesmen dan catat penanggung jawab, tenggat serta hasil tindak lanjut pada siklus PPEPP.

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
