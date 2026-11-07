# 084_5 — RUBRIK PENILAIAN PEMBELAJARAN

## STB-601 — Arsitektur Cloud & DevOps (*Cloud Architecture & DevOps*)

**Identitas:** `STB-601` Arsitektur Cloud & DevOps · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-417` · PL-2 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## 1. Prinsip dan skala

Rubrik adaptasi K-3 Dok 018. Untuk setiap kriteria berikan skor 0–100 dengan acuan **Sangat Baik 81–100**, **Baik 66–80**, **Cukup 56–65**, **Kurang 0–55**; kalikan skor dengan bobot kriteria. Hasil penjumlahan adalah nilai instrumen. Rentang ini merupakan adaptasi operasional dari Dok 018, bukan klaim salinan batas kategori dokumen sumber.

### Tugas 1 — Infrastruktur sebagai kode (pekan 4, 20% MK)

**CPMK:** `CPMK-1`. **Tugas:** Susun modul Terraform, variabel dan state; periksa plan dan jelaskan kontrol terhadap rahasia. **Bukti:** Kode HCL, plan, diagram dan instruksi.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Kebenaran deklarasi | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| struktur modul | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| keamanan state | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| replikasi | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UTS — Orkestrasi Kubernetes (pekan 8, 25% MK)

**CPMK:** `CPMK-2`. **Tugas:** Deploy workload dengan service, volume, rollout dan rollback pada klaster latihan. **Bukti:** Manifest individual, log dan hasil uji.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Workload dan networking | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| storage | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| recovery | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| penjelasan batas HA | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### Tugas 2 — Paket dan ketahanan Kubernetes (pekan 12, 25% MK)

**CPMK:** `CPMK-2`. **Tugas:** Kemas workload dalam Helm, validasi rendering serta uji upgrade dan rollback. **Bukti:** Chart, values, manifest render dan bukti uji.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Kebenaran template | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| parameter | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| hasil uji | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| rollback | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UAS — GitOps dan CI/CD (pekan 16, 30% MK)

**CPMK:** `CPMK-3`. **Tugas:** Integrasikan CI, image, Helm dan Argo CD; deteksi drift dan lakukan koreksi. **Bukti:** Repo, pipeline run, konfigurasi Argo, log drift dan demo.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Pipeline | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| sinkronisasi GitOps | 35% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| uji keamanan/recovery | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| dokumentasi | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

## 2. Rubrik formatif dan refleksi

Setiap praktik diberi status **tercapai / perlu perbaikan / belum ditunjukkan** untuk ketepatan proses, kualitas bukti dan penjelasan batas; tidak menambah bobot nilai sumatif. Refleksi persepsi 1–5 (1 sangat tidak setuju sampai 5 sangat setuju): saya dapat menjelaskan konsep; saya dapat menguji hasil; saya memahami batas dan risiko; saya berkontribusi dalam tim. Refleksi bukan pengganti penilaian capaian.

## 3. Lembar penilaian

| Mahasiswa | Instrumen | Kriteria 1–4 (0–100) | Skor berbobot | CPMK | Umpan balik dan tindak lanjut |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

## Acuan, guardrails dan rekonsiliasi

**BoK Dok 043:** `BK-IS19` *Cloud Architecture*, `BK-IT05` *Cloud Computing*. **Pembina Dok 004:** BK-IS19 dan BK-IT05 primer; BK-IS03 sekunder.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Cloud Tingkat Lanjut, Infrastructure as Code (Terraform), Orkestrasi Container (Kubernetes), Pipeline CI/CD Terintegrasi (GitLab CI/GitHub Actions), DevSecOps & Otomasi Keamanan.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding logika aplikasi bisnis tingkat atas, instalasi kabel rak data center on-premise, pembuatan desain grafis prototipe.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menyediakan platform infrastruktur awan yang terotomasi, skalabel, dan aman untuk aplikasi enterprise.

Batas tambahan Dok 037: tidak mengulang provisi VM manual sebagai materi utama; fokus otomasi dan orkestrasi.

**Catatan sumber:** Dok 037 merumuskan empat CPMK dan P3/KK3; Dok 043 menggunakan tiga CPMK dan menambahkan P4 sesuai matriks Dok 004. Kode Sub-CPMK pada Dok 043 menempatkan Kubernetes di CPMK-1 dan Helm/GitOps di CPMK-2, sementara rumusan CPMK-2/3 berbeda; bukti dinilai menurut rumusan CPMK. High availability nyata tidak diklaim dari klaster single-node. Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UTS sama-sama mengukur CPMK-2. Penyesuaian rencana mingguan di bawah mengutamakan kompetensi dan asesmen sebelum pekan pengumpulan; detail teknologi dari Dok 007 digunakan sejauh tidak melanggar guardrails. Prasyarat dan kode resmi mengikuti Dok 005/051. Perbedaan antar sumber ini perlu dikonfirmasi koordinator.

**Skenario:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.

**Rujukan kurikulum:** Dok 003/004 (CPL, IRM dan BoK); 005/051 (identitas dan prasyarat); 007/043 (materi, CPMK/Sub-CPMK); 008/018 (asesmen); 037/043 (boundary); 053 dan README perangkat ajar (format).

**Pustaka teknis:** HashiCorp Terraform documentation; Kubernetes documentation; dokumentasi Helm dan Argo CD.
