# 082_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE

## STI-625 — Rekayasa Platform Digital (*Digital Platform Engineering*)

**Identitas:** `STI-625` Rekayasa Platform Digital · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-416` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-2.

## 1. Identitas, pembelajaran dan otorisasi

Program Studi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tahun akademik, tanggal dan tanda tangan **diisi pada pengesahan**. Beban mingguan: **TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit**; PT adalah tugas terstruktur, BM belajar mandiri. Waktu ujian dan praktik dapat diatur sesuai kalender akademik tanpa mengubah beban semester.

## 2. CPL yang dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| `CPL-08` (`P4`) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | M |
| `CPL-13` (`KK5`) | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | M |

## 3. Rumusan CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD menurut Dok 043 | Bloom | CPL terkait |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **merancang** arsitektur sistem berbasis layanan mikro (*Microservices Architecture*) (*B*) menggunakan prinsip Domain-Driven Design (DDD) (*C*) dengan batas layanan (*Bounded Context*) yang tepat (*D*). | C4 | `CPL-08` (`P4`) |
| `CPMK-2` | Mahasiswa (*A*) mampu **mengimplementasikan** komunikasi antar-layanan asinkron (*B*) menggunakan message streaming Apache Kafka / RabbitMQ (*C*) dengan penanganan jaminan pengiriman pesan (*D*). | C3 | `CPL-13` (`KK5`) |
| `CPMK-3` | Mahasiswa (*A*) mampu **mengonfigurasi** API Gateway, Service Discovery, dan pola ketahanan sistem (Circuit Breaker, Saga Pattern) (*B*) pada klaster platform (*C*) untuk skalabilitas tinggi (*D*). | C4 | `CPL-08` (`P4`), `CPL-13` (`KK5`) |
| `CPMK-4` | Mahasiswa (*A*) mampu **membangun** pipeline Continuous Integration / Continuous Deployment (CI/CD) otomatis (*B*) menggunakan GitHub Actions dan observability distributed tracing (*C*) secara terintegrasi (*D*). | C6 | `CPL-13` (`KK5`) |

| Sub-CPMK Dok 043 | Kompetensi spesifik | CPMK di Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Merancang arsitektur microservices berbasis Domain-Driven Design (DDD). | `CPMK-1` | C4 |
| `Sub-CPMK-1.2` | Menerapkan pola event-driven dan message broker (Kafka/RabbitMQ). | `CPMK-1` | C4 |
| `Sub-CPMK-2.1` | Mengimplementasikan API Gateway dan circuit breaker pada layanan platform. | `CPMK-2` | C3 |
| `Sub-CPMK-2.2` | Menerapkan pola Saga untuk transaksi terdistribusi antar microservices. | `CPMK-2` | C3 |
| `Sub-CPMK-3.1` | Mengontainerisasi layanan dan menyusun pipeline CI/CD. | `CPMK-3` | C4 |
| `Sub-CPMK-3.2` | Mengonfigurasi observability (logging, tracing, metrik) pada platform. | `CPMK-3` | C4 |
| `Sub-CPMK-4.1` | Membangun platform digital terintegrasi berbasis arsitektur layanan modern. | `CPMK-4` | C6 |
| `Sub-CPMK-4.2` | Mengevaluasi keandalan dan skalabilitas platform digital yang dibangun. | `CPMK-4` | C6 |

## 4. Analisis pembelajaran dan matriks korelasi

Alur: fondasi dan analisis → implementasi terarah → integrasi, pengujian dan refleksi. Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-08` (`P4`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-13` (`KK5`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | — | 25% | — | 25% |
| `CPMK-4` | `CPL-13` (`KK5`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Bobot dalam tabel adalah alokasi terhadap nilai mata kuliah; satu CPMK dapat mendukung beberapa CPL dan tidak boleh dihitung sebagai nilai MK berulang. Lihat dokumen 4 untuk agregasi resmi CPL dan skor diagnostik.

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **75%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 5. Deskripsi dan rencana pembelajaran 16 pekan

Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi. Perangkat: Docker Compose, Git, layanan REST/gRPC sederhana, Kafka atau RabbitMQ lokal, OpenTelemetry dan GitHub Actions. Kegiatan, indikator dan bukti tiap pekan dijabarkan di SAP dan outline modul; asesmen formatif tidak menjadi komponen nilai tambahan.

| Pekan | Sub-CPMK terkait | Topik | Aktivitas / indikator yang dapat diamati | Bukti | Metode | Estimasi belajar | Asesmen |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Sub-CPMK-1.1` | Monolit, microservices dan konteks bisnis | Bandingkan arsitektur monolit dan layanan dari skenario, termasuk trade-off latensi dan transaksi. | Diagram konteks dan alasan batas layanan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 2 | `Sub-CPMK-1.1` | DDD dan bounded context | Petakan domain, aggregate, batas kepemilikan data dan kontrak antar dua layanan. | Context map dan kontrak layanan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 3 | `Sub-CPMK-1.1` | Kontrak API dan komunikasi sinkron | Rancang kontrak REST atau gRPC dan uji timeout pada layanan contoh. | Spesifikasi API dan hasil uji | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 4 | `Sub-CPMK-1.1` | Arsitektur layanan dan Tugas 1 | Tinjau batas layanan, diagram konteks dan alur data; serahkan rancangan arsitektur kasus. | Diagram, kontrak dan justifikasi Tugas 1 | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 1 (20%) |
| 5 | `Sub-CPMK-1.2` | Event-driven dan broker | Definisikan event, producer dan consumer pada broker lokal dengan skema pesan berversi. | Skema event dan demo publish/subscribe | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 6 | `Sub-CPMK-1.2` | Delivery guarantees dan idempotensi | Simulasikan pesan duplikat; implementasikan idempotency key dan catat offset/ack. | Log pengujian duplikat dan kode consumer | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 7 | `Sub-CPMK-1.2` | Kafka/RabbitMQ dan penanganan gagal | Uji redelivery dan dead-letter pada broker lokal; dokumentasikan pemulihan. | Konfigurasi broker dan bukti uji gagal | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 8 | `Sub-CPMK-1.2` | UTS: komunikasi asinkron | Implementasikan producer-consumer dan jelaskan penanganan duplikasi serta kegagalan. | Kode individual dan log pengujian | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UTS (25%) |
| 9 | `Sub-CPMK-2.1` | API gateway dan identitas | Konfigurasi routing, validasi permintaan dan rate limit pada gateway lokal. | Konfigurasi gateway dan hasil uji | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 10 | `Sub-CPMK-2.2` | Saga dan kompensasi | Modelkan saga peminjaman; injeksikan kegagalan dan periksa aksi kompensasi. | Diagram saga, trace dan catatan inkonsistensi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 11 | `Sub-CPMK-2.1` | Circuit breaker, retry dan batas waktu | Simulasikan layanan gagal dan uji timeout, retry berbatas dan circuit breaker. | Log closed/open/half-open dan hasil uji | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 12 | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | Integrasi ketahanan dan Tugas 2 | Verifikasi gateway dan saga terhadap tiga skenario gagal; serahkan milestone Tugas 2. | Konfigurasi, diagram dan hasil fault injection | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Tugas 2 (25%) |
| 13 | `Sub-CPMK-3.2` | Tracing, log dan metrik | Instrumentasi trace lintas dua layanan dan korelasikan event dengan request ID. | Trace contoh dan log terkorelasi | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 14 | `Sub-CPMK-3.1` | CI/CD, kontainer dan pemeriksaan keamanan | Bangun pipeline test, build dan pemindaian image pada repositori; gunakan rahasia dummy. | Workflow, image dan hasil pemeriksaan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 15 | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | Integrasi dan uji ketahanan platform | Gabungkan gateway, broker, observability dan pipeline; ukur hasil uji kegagalan pada lingkungan lokal. | Repo, diagram, rencana uji dan rekaman demo | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | Formatif (0%) |
| 16 | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | UAS: demonstrasi platform | Tunjukkan sistem terintegrasi, CI/CD, trace dan jawaban individual. | Demo, bukti pipeline, trace dan laporan | Kuliah kasus + praktik terarah | TM 100 menit, praktik 170 menit, PT 120 menit, BM 120 menit | UAS (30%) |

## 6. Ringkasan empat instrumen

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Context map, kontrak dan analisis trade-off |
| UTS | 8 | 25% | `CPMK-2` | Kode individual, skema event, log dan hasil uji |
| Tugas 2 | 12 | 25% | `CPMK-3` | Konfigurasi gateway, diagram saga dan laporan fault injection |
| UAS | 16 | 30% | `CPMK-4` | Repo, workflow CI/CD, trace, hasil pengujian dan demo |

## Acuan, guardrails dan rekonsiliasi

**BoK Dok 043:** `BK-IS12` *Web and Mobile App Development*, `BK-IT07` *System Integration and Architecture*. **Pembina Dok 004:** BK-IS12 dan BK-IT07 tercantum sebagai pembina primer untuk kode lama STI-727 di Dok 004; penyandingan dengan STI-625 mengikuti Dok 051 dan perlu dikonfirmasi.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Platform Digital, Event-Driven Architecture, Message Broker (Apache Kafka / RabbitMQ), API Gateway Pattern, Microservices Communication (gRPC & Async REST), Database Sharding & Read-Replicas.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang perancangan kabel data server fisik, riset algoritma AI murni, penulisan prototipe UI wireframe Figma.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Membangun platform digital terdistribusi tangguh; menyerahkan integrasi model bisnis dan monetisasi startup ke `STI-728`.

Batas tambahan: jangan mengulang pembangunan backend CRUD dasar dari awal; fokus pada integrasi layanan, ketahanan dan observability.

**Catatan sumber:** Dok 043 dan 004 menggunakan kode lama STI-727 pada judul Digital Platform Engineering; pemetaan isi berdasarkan judul dan prasyarat diselaraskan menjadi STI-625 menurut Dok 005/051. Pada Dok 043, beberapa nomor Sub-CPMK mengelompokkan event broker di CPMK-1 dan gateway/Saga di CPMK-2, sedangkan rumusan CPMK-2 dan CPMK-3 mengelompokkan sebaliknya; nomor sub asli dipertahankan, penilaian mengikuti rumusan CPMK. Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan. Penyesuaian rencana mingguan di bawah mengutamakan kompetensi dan asesmen sebelum pekan pengumpulan; detail teknologi dari Dok 007 digunakan sejauh tidak melanggar guardrails. Prasyarat dan kode resmi mengikuti Dok 005/051. Perbedaan antar sumber ini perlu dikonfirmasi koordinator.

**Skenario:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.

**Rujukan kurikulum:** Dok 003/004 (CPL, IRM dan BoK); 005/051 (identitas dan prasyarat); 007/043 (materi, CPMK/Sub-CPMK); 008/018 (asesmen); 037/043 (boundary); 053 dan README perangkat ajar (format).

**Pustaka teknis:** Newman, *Building Microservices*, 2nd ed. (2021); dokumentasi Apache Kafka, OpenTelemetry dan GitHub Actions.
