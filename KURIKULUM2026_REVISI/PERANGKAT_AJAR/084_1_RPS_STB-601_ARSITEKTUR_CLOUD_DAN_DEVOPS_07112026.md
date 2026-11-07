# 084_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE

## STB-601 — Arsitektur Cloud & DevOps (*Cloud Architecture & DevOps*)

**Identitas:** `STB-601` Arsitektur Cloud & DevOps · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-417` · PL-2 · PEO-1, PEO-3 · IRM **M** · Klaster K-3.

## 1. Identitas, pembelajaran dan otorisasi

Program Studi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tahun akademik, tanggal dan tanda tangan **diisi pada pengesahan**. Beban mingguan: **TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit**; PT adalah tugas terstruktur, BM belajar mandiri. Waktu ujian dan praktik dapat diatur sesuai kalender akademik tanpa mengubah beban semester.

## 2. CPL yang dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| `CPL-07` (`P3`) | Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (*cloud*), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi. | M |
| `CPL-08` (`P4`) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | M |
| `CPL-11` (`KK3`) | Mampu merancang, mengintegrasikan, dan mengelola infrastruktur komputasi awan (Cloud/DevOps), sistem sensor cerdas (IoT), dan ketahanan siber (*Cybersecurity*) secara andal, terukur, dan aman. | M |

## 3. Rumusan CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD menurut Dok 043 | Bloom | CPL terkait |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **memprovisi** infrastruktur cloud otomatis (*B*) menggunakan Infrastructure as Code (Terraform) (*C*) dengan modul deklaratif terstandar (*D*). | C4 | `CPL-07` (`P3`), `CPL-08` (`P4`) |
| `CPMK-2` | Mahasiswa (*A*) mampu **mengorkestrasikan** aplikasi multi-kontainer (*B*) pada klaster Kubernetes (Deployments, StatefulSets, Ingress, PersistentVolumes) (*C*) dengan konfigurasi *high availability* (*D*). | C4 | `CPL-11` (`KK3`) |
| `CPMK-3` | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Delivery berbasis GitOps (*B*) menggunakan ArgoCD dan Helm Charts (*C*) secara otomatis dan bebas *configuration drift* (*D*). | C6 | `CPL-08` (`P4`), `CPL-11` (`KK3`) |

| Sub-CPMK Dok 043 | Kompetensi spesifik | CPMK di Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Mengelola infrastruktur cloud sebagai kode menggunakan Terraform (IaC). | `CPMK-1` | C4 |
| `Sub-CPMK-1.2` | Menganalisis konsep orkestrasi Kubernetes (Deployments, StatefulSets, Ingress, PV). | `CPMK-1` | C4 |
| `Sub-CPMK-2.1` | Mengelola paket aplikasi dan rilis menggunakan Helm. | `CPMK-2` | C4 |
| `Sub-CPMK-2.2` | Menerapkan GitOps (ArgoCD) untuk deployment berkelanjutan. | `CPMK-2` | C4 |
| `Sub-CPMK-3.1` | Menyusun pipeline CI/CD kontainer untuk otomasi rilis aplikasi. | `CPMK-3` | C6 |
| `Sub-CPMK-3.2` | Mengevaluasi keandalan dan keamanan jalur deployment DevOps. | `CPMK-3` | C6 |

## 4. Analisis pembelajaran dan matriks korelasi

Alur: fondasi dan analisis → implementasi terarah → integrasi, pengujian dan refleksi. Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UTS sama-sama mengukur CPMK-2.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-07` (`P3`), `CPL-08` (`P4`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-11` (`KK3`) | — | 25% | 25% | — | 50% |
| `CPMK-3` | `CPL-08` (`P4`), `CPL-11` (`KK3`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Bobot dalam tabel adalah alokasi terhadap nilai mata kuliah; satu CPMK dapat mendukung beberapa CPL dan tidak boleh dihitung sebagai nilai MK berulang. Lihat dokumen 4 untuk agregasi resmi CPL dan skor diagnostik.

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **70%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 5. Deskripsi dan rencana pembelajaran 16 pekan

Infrastruktur layanan kampus simulasi di-deploy dari konfigurasi berversi pada klaster lab lokal, tanpa akun produksi. Perangkat: Terraform, container runtime, kind/minikube, Helm, GitHub Actions/GitLab CI dan Argo CD; kredensial latihan terbatas. Kegiatan, indikator dan bukti tiap pekan dijabarkan di SAP dan outline modul; asesmen formatif tidak menjadi komponen nilai tambahan.

| Pekan | Sub-CPMK terkait | Topik | Aktivitas / indikator yang dapat diamati | Bukti | Metode | Estimasi belajar | Asesmen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Sub-CPMK-1.1` | Cloud native, IaC dan batas lab | Tentukan kebutuhan, SLO usulan dan batas biaya/akses lingkungan simulasi; identifikasi risiko kredensial. | Diagram lingkungan dan checklist keselamatan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 2 | `Sub-CPMK-1.1` | Terraform: provider, resources dan plan | Tulis konfigurasi deklaratif lokal, jalankan init/validate/plan dan interpretasikan perubahan. | Kode HCL dan output plan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 3 | `Sub-CPMK-1.1` | Modul, variabel dan konfigurasi aman | Buat modul reusable dengan input/output tervalidasi; hindari menyimpan secrets di repositori. | Modul, validasi dan instruksi penggunaan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 4 | `Sub-CPMK-1.1` | State, drift dan Tugas 1 | Jelaskan remote state/locking; demonstrasikan perubahan terkontrol dan serahkan Tugas 1. | Plan, bukti state dan Tugas 1 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 1 (20%) |
| 5 | `Sub-CPMK-1.2` | Kubernetes control plane dan workload | Petakan control plane, node dan reconciler; deploy aplikasi latihan ke kind/minikube. | Diagram, manifest deployment dan status pod | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 6 | `Sub-CPMK-1.2` | Deployment dan rolling update | Uji replicas, readiness probe, rolling update dan rollback pada klaster lab. | Manifest dan log rollout/rollback | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 7 | `Sub-CPMK-1.2` | Service, ingress dan volume | Konfigurasikan service, ingress dan PVC untuk layanan latihan; uji akses dan persistensi. | Manifest, bukti konektivitas dan restart | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 8 | `Sub-CPMK-1.2` | UTS: orkestrasi Kubernetes | Konfigurasikan workload, service dan storage; buktikan rollout dan recovery. | Manifest individual dan log uji | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UTS (25%) |
| 9 | `Sub-CPMK-1.2` | StatefulSet dan data persisten | Terapkan StatefulSet dan PVC untuk beban contoh, uji restart tanpa menghapus volume. | Manifest dan bukti persistensi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 10 | `Sub-CPMK-2.1` | Helm dan template | Buat chart sederhana dengan values per lingkungan; render dan validasi hasil. | Chart dan hasil helm template | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 11 | `Sub-CPMK-2.2` | GitOps dan deteksi drift | Konfigurasikan Argo CD untuk repo latihan; ubah konfigurasi live dan amati deteksi drift. | Manifest aplikasi Argo dan bukti sinkronisasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 12 | `Sub-CPMK-2.1` | Helm dan ketahanan workload: Tugas 2 | Verifikasi chart, service, volume dan rollback; serahkan paket Kubernetes. | Chart, manifest dan hasil pengujian Tugas 2 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 2 (25%) |
| 13 | `Sub-CPMK-3.1` | CI/CD dan kontrol keamanan | Jalankan lint, test, build image dan pemindaian dependensi pada pipeline contoh. | Workflow CI dan hasil run | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 14 | `Sub-CPMK-3.2` | Observability, autoscaling dan SLO | Amati metrik resource dan uji HPA pada beban simulasi; catat kondisi pengukuran. | Konfigurasi metrik, log HPA dan temuan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 15 | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | GitOps end-to-end dan recovery | Integrasikan IaC, CI, Helm dan Argo CD; uji rollback serta deteksi drift. | Repo, diagram, hasil uji dan runbook | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 16 | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | UAS: GitOps dan keamanan deployment | Demonstrasikan deployment dan koreksi drift, lalu pertahankan keputusan secara individual. | Repo, pipeline, bukti sinkronisasi dan presentasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UAS (30%) |

## 6. Ringkasan empat instrumen

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Kode HCL, plan, diagram dan instruksi |
| UTS | 8 | 25% | `CPMK-2` | Manifest individual, log dan hasil uji |
| Tugas 2 | 12 | 25% | `CPMK-2` | Chart, values, manifest render dan bukti uji |
| UAS | 16 | 30% | `CPMK-3` | Repo, pipeline run, konfigurasi Argo, log drift dan demo |

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
