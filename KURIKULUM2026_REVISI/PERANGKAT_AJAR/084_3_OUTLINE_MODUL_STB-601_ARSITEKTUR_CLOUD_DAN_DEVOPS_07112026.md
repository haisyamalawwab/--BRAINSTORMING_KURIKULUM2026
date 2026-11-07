# 084_3 — OUTLINE BUKU MODUL PEMBELAJARAN DAN PRAKTIKUM

## STB-601 — Arsitektur Cloud & DevOps (*Cloud Architecture & DevOps*)

**Identitas:** `STB-601` Arsitektur Cloud & DevOps · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-417` · PL-2 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## Spesifikasi buku dan peta bab

Empat belas bab untuk pekan 1–7 dan 9–15; pertemuan 8 dan 16 berupa evaluasi. Tiap bab memuat penjelasan konsep, contoh, latihan, praktik dan refleksi; kasus serta perangkat: Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi. Terraform, container runtime, kind/minikube, Helm, GitHub Actions/GitLab CI dan Argo CD; kredensial latihan terbatas. Silabus final dan batas topik mengikuti RPS. Prompt ilustrasi berikut adalah spesifikasi, bukan klaim gambar sudah dibuat.

### Bab 1. Cloud native, IaC dan batas lab — pekan 1

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Cloud native, IaC dan batas lab; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Tentukan kebutuhan, SLO usulan dan batas biaya/akses lingkungan simulasi; identifikasi risiko kredensial.
- **Bukti dan kriteria:** Diagram lingkungan dan checklist keselamatan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan availability target dan bukti uji. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Cloud native, IaC dan batas lab, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 2. Terraform: provider, resources dan plan — pekan 2

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Terraform: provider, resources dan plan; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Tulis konfigurasi deklaratif lokal, jalankan init/validate/plan dan interpretasikan perubahan.
- **Bukti dan kriteria:** Kode HCL dan output plan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan state dan tujuan plan. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Terraform: provider, resources dan plan, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 3. Modul, variabel dan konfigurasi aman — pekan 3

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Modul, variabel dan konfigurasi aman; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Buat modul reusable dengan input/output tervalidasi; hindari menyimpan secrets di repositori.
- **Bukti dan kriteria:** Modul, validasi dan instruksi penggunaan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan least privilege dan secret management. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Modul, variabel dan konfigurasi aman, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 4. State, drift dan Tugas 1 — pekan 4

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi State, drift dan Tugas 1; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Jelaskan remote state/locking; demonstrasikan perubahan terkontrol dan serahkan Tugas 1.
- **Bukti dan kriteria:** Plan, bukti state dan Tugas 1; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan risiko state berisi data sensitif. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang State, drift dan Tugas 1, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 5. Kubernetes control plane dan workload — pekan 5

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Kubernetes control plane dan workload; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Petakan control plane, node dan reconciler; deploy aplikasi latihan ke kind/minikube.
- **Bukti dan kriteria:** Diagram, manifest deployment dan status pod; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan pod, deployment dan node. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Kubernetes control plane dan workload, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 6. Deployment dan rolling update — pekan 6

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Deployment dan rolling update; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Uji replicas, readiness probe, rolling update dan rollback pada klaster lab.
- **Bukti dan kriteria:** Manifest dan log rollout/rollback; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan keterbatasan single-node terhadap HA. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Deployment dan rolling update, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 7. Service, ingress dan volume — pekan 7

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Service, ingress dan volume; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Konfigurasikan service, ingress dan PVC untuk layanan latihan; uji akses dan persistensi.
- **Bukti dan kriteria:** Manifest, bukti konektivitas dan restart; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan service, ingress dan storage class. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Service, ingress dan volume, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 8. StatefulSet dan data persisten — pekan 9

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi StatefulSet dan data persisten; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Terapkan StatefulSet dan PVC untuk beban contoh, uji restart tanpa menghapus volume.
- **Bukti dan kriteria:** Manifest dan bukti persistensi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan identitas pod dan PVC. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang StatefulSet dan data persisten, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 9. Helm dan template — pekan 10

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Helm dan template; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Buat chart sederhana dengan values per lingkungan; render dan validasi hasil.
- **Bukti dan kriteria:** Chart dan hasil helm template; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan risiko perbedaan konfigurasi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Helm dan template, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 10. GitOps dan deteksi drift — pekan 11

- **Capaian:** Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi GitOps dan deteksi drift; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Konfigurasikan Argo CD untuk repo latihan; ubah konfigurasi live dan amati deteksi drift.
- **Bukti dan kriteria:** Manifest aplikasi Argo dan bukti sinkronisasi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan desired state dan live state. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang GitOps dan deteksi drift, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 11. Helm dan ketahanan workload: Tugas 2 — pekan 12

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Helm dan ketahanan workload: Tugas 2; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Verifikasi chart, service, volume dan rollback; serahkan paket Kubernetes.
- **Bukti dan kriteria:** Chart, manifest dan hasil pengujian Tugas 2; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan strategi rollback yang aman. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Helm dan ketahanan workload: Tugas 2, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 12. CI/CD dan kontrol keamanan — pekan 13

- **Capaian:** Sub-CPMK-3.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi CI/CD dan kontrol keamanan; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Jalankan lint, test, build image dan pemindaian dependensi pada pipeline contoh.
- **Bukti dan kriteria:** Workflow CI dan hasil run; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan perlindungan secret dan dependensi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang CI/CD dan kontrol keamanan, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 13. Observability, autoscaling dan SLO — pekan 14

- **Capaian:** Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Observability, autoscaling dan SLO; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Amati metrik resource dan uji HPA pada beban simulasi; catat kondisi pengukuran.
- **Bukti dan kriteria:** Konfigurasi metrik, log HPA dan temuan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan HPA, autoscaler node dan HA. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Observability, autoscaling dan SLO, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 14. GitOps end-to-end dan recovery — pekan 15

- **Capaian:** Sub-CPMK-3.1, Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi GitOps end-to-end dan recovery; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi.
- **Aktivitas praktikum:** Integrasikan IaC, CI, Helm dan Argo CD; uji rollback serta deteksi drift.
- **Bukti dan kriteria:** Repo, diagram, hasil uji dan runbook; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Rumuskan risiko operasional dan handoff. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang GitOps end-to-end dan recovery, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

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
