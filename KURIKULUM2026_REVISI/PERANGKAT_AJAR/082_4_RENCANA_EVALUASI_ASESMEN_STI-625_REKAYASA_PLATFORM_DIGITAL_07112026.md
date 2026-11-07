# 082_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STI-625 — Rekayasa Platform Digital (*Digital Platform Engineering*)

**Identitas:** `STI-625` Rekayasa Platform Digital · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-416` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-2.

## 1. Arsitektur asesmen dan bukti

| Asesmen | Pekan | Bobot | CPMK | Produk / bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | `CPMK-1` | Context map, kontrak dan analisis trade-off |
| UTS | 8 | 25% | `CPMK-2` | Kode individual, skema event, log dan hasil uji |
| Tugas 2 | 12 | 25% | `CPMK-3` | Konfigurasi gateway, diagram saga dan laporan fault injection |
| UAS | 16 | 30% | `CPMK-4` | Repo, workflow CI/CD, trace, hasil pengujian dan demo |

**Rencana IKU 7:** Tugas 1 (20% studi kasus kolaboratif) + Tugas 2 (25% milestone proyek tim) + UAS (30% proyek dan pembelaan individual) = **75% bobot** berbasis kasus/proyek. Target Dok 004 untuk mata kuliah ini adalah **75%**; untuk peminatan digunakan baris umum peminatan semester 6. Angka 75% adalah rancangan penilaian, bukan klaim realisasi pembelajaran. Simpan bukti diskusi, kontribusi dan produk tim. Persentase komposisi metode dapat berbeda dari proporsi indikatif Dok 004 dan perlu validasi prodi.

## 2. Matriks CPMK dan CPL

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| `CPMK-1` | `CPL-08` (`P4`) | 20% | — | — | — | 20% |
| `CPMK-2` | `CPL-13` (`KK5`) | — | 25% | — | — | 25% |
| `CPMK-3` | `CPL-08` (`P4`), `CPL-13` (`KK5`) | — | — | 25% | — | 25% |
| `CPMK-4` | `CPL-13` (`KK5`) | — | — | — | 30% | 30% |
| Jumlah | — | 20% | 25% | 25% | 30% | 100% |

Keempat instrumen memetakan CPMK-1 hingga CPMK-4 secara berurutan.

### Formula dan batas interpretasi

- **Skor instrumen:** jumlah skor kriteria × bobot kriteria dalam rubrik dokumen 5, skala 0–100. **Nilai akhir MK:** 0,20 × T1 + 0,25 × UTS + 0,25 × T2 + 0,30 × UAS.
- **Skor CPMK:** jumlah (bobot instrumen terkait × skor instrumen) dibagi jumlah bobot instrumen CPMK itu; misal skor 80 pada 25% dan 70 pada 30% menghasilkan (25×80 + 30×70)/55 = 74,55.
- **Diagnostik CPL pada mata kuliah:** rata-rata berbobot CPMK yang mendukung CPL, dengan total bobot CPMK sebagai bobot. Ini sarana diagnostik lokal dan bukan pengganti formula agregasi resmi prodi.
- **CPL individu lintas MK menurut Dok 008:** Σ(SKS MK × bobot MK terhadap CPL × nilai akhir MK) / Σ(SKS MK × bobot MK terhadap CPL), pada seluruh MK pembina CPL; bobot ditetapkan prodi. Dok 008 menetapkan ambang 65 serta target 80% kohor mencapai ambang; nilai MK ini saja belum bisa menentukan capaian CPL lulusan.

## 3. Rencana Tugas Mahasiswa dan kisi-kisi ujian

### 3.1 Tugas 1 — Rancangan bounded context

- **Waktu dan bobot:** pekan 4, 20% nilai MK; **CPMK:** `CPMK-1`; **CPL:** `CPL-08` (`P4`).
- **Tujuan:** Mahasiswa (*A*) mampu **merancang** arsitektur sistem berbasis layanan mikro (*Microservices Architecture*) (*B*) menggunakan prinsip Domain-Driven Design (DDD) (*C*) dengan batas layanan (*Bounded Context*) yang tepat (*D*).
- **Kasus & instruksi:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi. Susun konteks domain, batas minimal dua layanan dan kontrak untuk kasus peminjaman.
- **Bukti wajib:** Context map, kontrak dan analisis trade-off.
- **Indikator penilaian:** Koherensi batas domain; kepemilikan data; kontrak layanan; argumentasi. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.2 UTS — Komunikasi event

- **Waktu dan bobot:** pekan 8, 25% nilai MK; **CPMK:** `CPMK-2`; **CPL:** `CPL-13` (`KK5`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengimplementasikan** komunikasi antar-layanan asinkron (*B*) menggunakan message streaming Apache Kafka / RabbitMQ (*C*) dengan penanganan jaminan pengiriman pesan (*D*).
- **Kasus & instruksi:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi. Implementasikan pertukaran event pada broker lokal, tangani duplikasi dan demonstrasikan redelivery.
- **Bukti wajib:** Kode individual, skema event, log dan hasil uji.
- **Indikator penilaian:** Publish/consume; idempotensi; handling gagal; penjelasan jaminan delivery. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** ujian praktik individual; dosen memberi dataset atau konfigurasi uji dan menilai hasil serta penjelasan. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.3 Tugas 2 — Gateway dan saga tangguh

- **Waktu dan bobot:** pekan 12, 25% nilai MK; **CPMK:** `CPMK-3`; **CPL:** `CPL-08` (`P4`), `CPL-13` (`KK5`).
- **Tujuan:** Mahasiswa (*A*) mampu **mengonfigurasi** API Gateway, Service Discovery, dan pola ketahanan sistem (Circuit Breaker, Saga Pattern) (*B*) pada klaster platform (*C*) untuk skalabilitas tinggi (*D*).
- **Kasus & instruksi:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi. Konfigurasi gateway dan simulasikan saga beserta kompensasi serta circuit breaker.
- **Bukti wajib:** Konfigurasi gateway, diagram saga dan laporan fault injection.
- **Indikator penilaian:** Routing; ketepatan kompensasi; timeout dan retry; bukti pengujian. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

### 3.4 UAS — Pipeline platform terintegrasi

- **Waktu dan bobot:** pekan 16, 30% nilai MK; **CPMK:** `CPMK-4`; **CPL:** `CPL-13` (`KK5`).
- **Tujuan:** Mahasiswa (*A*) mampu **membangun** pipeline Continuous Integration / Continuous Deployment (CI/CD) otomatis (*B*) menggunakan GitHub Actions dan observability distributed tracing (*C*) secara terintegrasi (*D*).
- **Kasus & instruksi:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi. Integrasikan build/test/deploy lokal dan distributed tracing pada dua layanan.
- **Bukti wajib:** Repo, workflow CI/CD, trace, hasil pengujian dan demo.
- **Indikator penilaian:** Otomasi pipeline; korelasi trace; uji integrasi; dokumentasi serta rahasia aman. Rubrik terperinci dan pembobotan kriteria di dokumen 5.
- **Mekanisme:** produk kasus/proyek tim, dengan catatan kontribusi dan pembelaan individual. Kumpulkan melalui LMS dalam format yang dapat diperiksa, tanpa kredensial rahasia atau data pribadi.
- **Kisi-kisi periksa:** (1) konsep dan asumsi; (2) implementasi sesuai instruksi; (3) minimal satu pengujian dan interpretasi; (4) dokumentasi dan batas hasil. Rincian contoh/varian soal diberikan dosen sebelum penilaian.

## 4. Umpan balik, remediasi dan PPEPP

Dosen menyimpan bukti per mahasiswa, hasil tiap kriteria dan nilai CPMK; menyampaikan umpan balik serta mengatur remediasi sesuai peraturan prodi tanpa menciptakan komponen nilai kelima. Pada akhir semester, hitung capaian, identifikasi indikator bermasalah, analisis penyebab, usulkan perubahan materi/asesmen dan catat penanggung jawab, tenggat serta hasil tindak lanjut pada siklus PPEPP.

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
