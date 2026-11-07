# 084_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN

## STB-601 — Arsitektur Cloud & DevOps (*Cloud Architecture & DevOps*)

**Identitas:** `STB-601` Arsitektur Cloud & DevOps · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-417` · PL-2 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## Pedoman pelaksanaan

Kasus bersama: Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi. Perangkat: Terraform, container runtime, kind/minikube, Helm, GitHub Actions/GitLab CI dan Argo CD; kredensial latihan terbatas. Pembelajaran menggunakan kelompok kecil dengan bukti kontribusi individual. **TM 100 menit:** pembuka 10, demonstrasi/kasus 75, refleksi 15. **Praktik 170 menit:** briefing 15, pengerjaan 120, pengujian dan umpan balik 25, penutupan 10. **PT 120 menit, BM 120 menit** di luar kelas. Setiap praktik memakai data dan sistem berizin.

### Pertemuan 1 — Cloud native, IaC dan batas lab

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Cloud native, IaC dan batas lab.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Tentukan kebutuhan, SLO usulan dan batas biaya/akses lingkungan simulasi; identifikasi risiko kredensial. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram lingkungan dan checklist keselamatan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan availability target dan bukti uji.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 2 — Terraform: provider, resources dan plan

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Terraform: provider, resources dan plan.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Tulis konfigurasi deklaratif lokal, jalankan init/validate/plan dan interpretasikan perubahan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Kode HCL dan output plan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan state dan tujuan plan.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 3 — Modul, variabel dan konfigurasi aman

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Modul, variabel dan konfigurasi aman.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Buat modul reusable dengan input/output tervalidasi; hindari menyimpan secrets di repositori. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Modul, validasi dan instruksi penggunaan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan least privilege dan secret management.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 4 — State, drift dan Tugas 1

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait State, drift dan Tugas 1.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Jelaskan remote state/locking; demonstrasikan perubahan terkontrol dan serahkan Tugas 1. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Plan, bukti state dan Tugas 1. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan risiko state berisi data sensitif.
- **Sumatif:** Tugas 1 20% pada pekan 4, mengukur `CPMK-1`: Susun modul Terraform, variabel dan state; periksa plan dan jelaskan kontrol terhadap rahasia. Bukti: Kode HCL, plan, diagram dan instruksi. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 5 — Kubernetes control plane dan workload

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Kubernetes control plane dan workload.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Petakan control plane, node dan reconciler; deploy aplikasi latihan ke kind/minikube. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram, manifest deployment dan status pod. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan pod, deployment dan node.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 6 — Deployment dan rolling update

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Deployment dan rolling update.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Uji replicas, readiness probe, rolling update dan rollback pada klaster lab. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Manifest dan log rollout/rollback. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan keterbatasan single-node terhadap HA.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 7 — Service, ingress dan volume

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Service, ingress dan volume.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Konfigurasikan service, ingress dan PVC untuk layanan latihan; uji akses dan persistensi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Manifest, bukti konektivitas dan restart. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan service, ingress dan storage class.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 8 — UTS: orkestrasi Kubernetes

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UTS: orkestrasi Kubernetes.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Konfigurasikan workload, service dan storage; buktikan rollout dan recovery. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Manifest individual dan log uji. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Refleksi setelah umpan balik.
- **Sumatif:** UTS 25% pada pekan 8, mengukur `CPMK-2`: Deploy workload dengan service, volume, rollout dan rollback pada klaster latihan. Bukti: Manifest individual, log dan hasil uji. Ujian dikerjakan dan dipertanggungjawabkan individual.

### Pertemuan 9 — StatefulSet dan data persisten

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait StatefulSet dan data persisten.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Terapkan StatefulSet dan PVC untuk beban contoh, uji restart tanpa menghapus volume. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Manifest dan bukti persistensi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan identitas pod dan PVC.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 10 — Helm dan template

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Helm dan template.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Buat chart sederhana dengan values per lingkungan; render dan validasi hasil. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Chart dan hasil helm template. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan risiko perbedaan konfigurasi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 11 — GitOps dan deteksi drift

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait GitOps dan deteksi drift.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Konfigurasikan Argo CD untuk repo latihan; ubah konfigurasi live dan amati deteksi drift. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Manifest aplikasi Argo dan bukti sinkronisasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan desired state dan live state.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 12 — Helm dan ketahanan workload: Tugas 2

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Helm dan ketahanan workload: Tugas 2.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Verifikasi chart, service, volume dan rollback; serahkan paket Kubernetes. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Chart, manifest dan hasil pengujian Tugas 2. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan strategi rollback yang aman.
- **Sumatif:** Tugas 2 25% pada pekan 12, mengukur `CPMK-2`: Kemas workload dalam Helm, validasi rendering serta uji upgrade dan rollback. Bukti: Chart, values, manifest render dan bukti uji. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 13 — CI/CD dan kontrol keamanan

- **Keterkaitan:** `Sub-CPMK-3.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait CI/CD dan kontrol keamanan.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Jalankan lint, test, build image dan pemindaian dependensi pada pipeline contoh. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Workflow CI dan hasil run. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan perlindungan secret dan dependensi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 14 — Observability, autoscaling dan SLO

- **Keterkaitan:** `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Observability, autoscaling dan SLO.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Amati metrik resource dan uji HPA pada beban simulasi; catat kondisi pengukuran. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Konfigurasi metrik, log HPA dan temuan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan HPA, autoscaler node dan HA.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 15 — GitOps end-to-end dan recovery

- **Keterkaitan:** `Sub-CPMK-3.1`, `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait GitOps end-to-end dan recovery.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Integrasikan IaC, CI, Helm dan Argo CD; uji rollback serta deteksi drift. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Repo, diagram, hasil uji dan runbook. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Rumuskan risiko operasional dan handoff.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 16 — UAS: GitOps dan keamanan deployment

- **Keterkaitan:** `Sub-CPMK-3.1`, `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UAS: GitOps dan keamanan deployment.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Demonstrasikan deployment dan koreksi drift, lalu pertahankan keputusan secara individual. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Repo, pipeline, bukti sinkronisasi dan presentasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Catat tindak lanjut dan batas simulasi.
- **Sumatif:** UAS 30% pada pekan 16, mengukur `CPMK-3`: Integrasikan CI, image, Helm dan Argo CD; deteksi drift dan lakukan koreksi. Bukti: Repo, pipeline run, konfigurasi Argo, log drift dan demo. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

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
