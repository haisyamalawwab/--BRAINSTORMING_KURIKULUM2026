# 084_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STB-601 — Arsitektur Cloud & DevOps (*Cloud Architecture & DevOps*)

**Identitas:** `STB-601` Arsitektur Cloud & DevOps · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-417` · PL-2 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## 1. Arsitektur asesmen dan bukti

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Kode HCL, plan, diagram dan instruksi |
| UTS | 8 | 25% | `CPMK-2` | Manifest individual, log dan hasil uji |
| Tugas 2 | 12 | 25% | `CPMK-2` | Chart, values, manifest render dan bukti uji |
| UAS | 16 | 30% | `CPMK-3` | Repo, pipeline run, konfigurasi Argo, log drift dan demo |

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 2. Matriks CPMK dan CPL

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-07` (`P3`), `CPL-08` (`P4`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-11` (`KK3`) | — | 25% | 25% | — | 50% |
| `CPMK-3` | `CPL-08` (`P4`), `CPL-11` (`KK3`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UTS sama-sama mengukur CPMK-2.

### Formula dan batas interpretasi

- **Skor instrumen:** jumlah skor kriteria × bobot kriteria dalam rubrik dokumen 5, skala 0–100. **Nilai akhir MK:** 0,20 × T1 + 0,25 × UTS + 0,25 × T2 + 0,30 × UAS.
- **Skor CPMK:** jumlah (bobot instrumen terkait × skor instrumen) dibagi jumlah bobot instrumen CPMK itu; misal skor 80 pada 25% dan 70 pada 30% menghasilkan (25×80 + 30×70)/55 = 74,55.
- **Diagnostik CPL pada mata kuliah:** rata-rata berbobot CPMK yang mendukung CPL, dengan total bobot CPMK sebagai bobot. Ini sarana diagnostik lokal dan bukan pengganti formula agregasi resmi prodi.
- **CPL individu lintas MK menurut Dok 008:** Σ(SKS MK × bobot MK terhadap CPL × nilai akhir MK) / Σ(SKS MK × bobot MK terhadap CPL), pada seluruh MK pembina CPL; bobot ditetapkan prodi. Dok 008 menetapkan ambang 65 serta target 80% kohor mencapai ambang; nilai MK ini saja belum bisa menentukan capaian CPL lulusan.

## 3. Rencana Tugas Mahasiswa dan kisi-kisi ujian

### 3.1 Tugas 1 — Infrastruktur sebagai kode

- **Waktu dan bobot:** pekan 4, 20% nilai MK; **CPMK:** `CPMK-1`; **CPL:** `CPL-07` (`P3`), `CPL-08` (`P4`).
- **Tujuan:** Mahasiswa (*A*) mampu **memprovisi** infrastruktur cloud otomatis (*B*) menggunakan Infrastructure as Code (Terraform) (*C*) dengan modul deklaratif terstandar (*D*).
- **Kasus & instruksi:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi. Susun modul Terraform, variabel dan state; periksa plan dan jelaskan kontrol terhadap rahasia.
- **Bukti wajib:** Kode HCL, plan, diagram dan instruksi.
- **Indikator penilaian:** Kebenaran deklarasi; struktur modul; keamanan state; replikasi. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.2 UTS — Orkestrasi Kubernetes

- **Waktu dan bobot:** pekan 8, 25% nilai MK; **CPMK:** `CPMK-2`; **CPL:** `CPL-11` (`KK3`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengorkestrasikan** aplikasi multi-kontainer (*B*) pada klaster Kubernetes (Deployments, StatefulSets, Ingress, PersistentVolumes) (*C*) dengan konfigurasi *high availability* (*D*).
- **Kasus & instruksi:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi. Deploy workload dengan service, volume, rollout dan rollback pada klaster latihan.
- **Bukti wajib:** Manifest individual, log dan hasil uji.
- **Indikator penilaian:** Workload dan networking; storage; recovery; penjelasan batas HA. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** ujian praktik individual; dosen memberi dataset atau konfigurasi uji dan menilai hasil serta penjelasan. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.3 Tugas 2 — Paket dan ketahanan Kubernetes

- **Waktu dan bobot:** pekan 12, 25% nilai MK; **CPMK:** `CPMK-2`; **CPL:** `CPL-11` (`KK3`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengorkestrasikan** aplikasi multi-kontainer (*B*) pada klaster Kubernetes (Deployments, StatefulSets, Ingress, PersistentVolumes) (*C*) dengan konfigurasi *high availability* (*D*).
- **Kasus & instruksi:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi. Kemas workload dalam Helm, validasi rendering serta uji upgrade dan rollback.
- **Bukti wajib:** Chart, values, manifest render dan bukti uji.
- **Indikator penilaian:** Kebenaran template; parameter; hasil uji; rollback. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.4 UAS — GitOps dan CI/CD

- **Waktu dan bobot:** pekan 16, 30% nilai MK; **CPMK:** `CPMK-3`; **CPL:** `CPL-08` (`P4`), `CPL-11` (`KK3`).
- **Tujuan:** Mahasiswa (*A*) mampu **membangun** pipeline Continuous Delivery berbasis GitOps (*B*) menggunakan ArgoCD dan Helm Charts (*C*) secara otomatis dan bebas *configuration drift* (*D*).
- **Kasus & instruksi:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi. Integrasikan CI, image, Helm dan Argo CD; deteksi drift dan lakukan koreksi.
- **Bukti wajib:** Repo, pipeline run, konfigurasi Argo, log drift dan demo.
- **Indikator penilaian:** Pipeline; sinkronisasi GitOps; uji keamanan/recovery; dokumentasi. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

## 4. Umpan balik, remediasi dan PPEPP

Dosen menyimpan bukti per mahasiswa, hasil tiap kriteria dan nilai CPMK; menyampaikan umpan balik serta mengatur remediasi sesuai peraturan prodi tanpa menciptakan komponen nilai kelima. Pada akhir semester, hitung capaian, identifikasi indikator bermasalah, analisis penyebab, usulkan perubahan materi/asesmen dan catat penanggung jawab, tenggat serta hasil tindak lanjut pada siklus PPEPP.

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
