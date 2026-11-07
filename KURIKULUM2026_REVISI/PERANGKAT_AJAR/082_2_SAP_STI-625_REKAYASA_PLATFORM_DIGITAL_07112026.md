# 082_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN

## STI-625 — Rekayasa Platform Digital (*Digital Platform Engineering*)

**Identitas:** `STI-625` Rekayasa Platform Digital · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-416` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-2.

## Pedoman pelaksanaan

Kasus bersama: Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi. Perangkat: Docker Compose, Git, layanan REST/gRPC sederhana, Kafka atau RabbitMQ lokal, OpenTelemetry dan GitHub Actions. Pembelajaran menggunakan kelompok kecil dengan bukti kontribusi individual. **TM 100 menit:** pembuka 10, demonstrasi/kasus 75, refleksi 15. **Praktik 170 menit:** briefing 15, pengerjaan 120, pengujian dan umpan balik 25, penutupan 10. **PT 120 menit, BM 120 menit** di luar kelas. Setiap praktik memakai data dan sistem berizin.

### Pertemuan 1 — Monolit, microservices dan konteks bisnis

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Monolit, microservices dan konteks bisnis.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bandingkan arsitektur monolit dan layanan dari skenario, termasuk trade-off latensi dan transaksi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram konteks dan alasan batas layanan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan kapan monolit lebih tepat.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 2 — DDD dan bounded context

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait DDD dan bounded context.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Petakan domain, aggregate, batas kepemilikan data dan kontrak antar dua layanan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Context map dan kontrak layanan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan aggregate dari bounded context.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 3 — Kontrak API dan komunikasi sinkron

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Kontrak API dan komunikasi sinkron.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Rancang kontrak REST atau gRPC dan uji timeout pada layanan contoh. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Spesifikasi API dan hasil uji. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bandingkan coupling sinkron dan asinkron.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 4 — Arsitektur layanan dan Tugas 1

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Arsitektur layanan dan Tugas 1.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Tinjau batas layanan, diagram konteks dan alur data; serahkan rancangan arsitektur kasus. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram, kontrak dan justifikasi Tugas 1. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Tulis risiko transaksi lintas layanan.
- **Sumatif:** Tugas 1 20% pada pekan 4, mengukur `CPMK-1`: Susun konteks domain, batas minimal dua layanan dan kontrak untuk kasus peminjaman. Bukti: Context map, kontrak dan analisis trade-off. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 5 — Event-driven dan broker

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Event-driven dan broker.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Definisikan event, producer dan consumer pada broker lokal dengan skema pesan berversi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Skema event dan demo publish/subscribe. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan event dan command.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 6 — Delivery guarantees dan idempotensi

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Delivery guarantees dan idempotensi.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Simulasikan pesan duplikat; implementasikan idempotency key dan catat offset/ack. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Log pengujian duplikat dan kode consumer. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan at-least-once dan risiko exactly-once.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 7 — Kafka/RabbitMQ dan penanganan gagal

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Kafka/RabbitMQ dan penanganan gagal.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Uji redelivery dan dead-letter pada broker lokal; dokumentasikan pemulihan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Konfigurasi broker dan bukti uji gagal. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan ordering dan partisi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 8 — UTS: komunikasi asinkron

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UTS: komunikasi asinkron.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Implementasikan producer-consumer dan jelaskan penanganan duplikasi serta kegagalan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Kode individual dan log pengujian. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Refleksi setelah umpan balik.
- **Sumatif:** UTS 25% pada pekan 8, mengukur `CPMK-2`: Implementasikan pertukaran event pada broker lokal, tangani duplikasi dan demonstrasikan redelivery. Bukti: Kode individual, skema event, log dan hasil uji. Ujian dikerjakan dan dipertanggungjawabkan individual.

### Pertemuan 9 — API gateway dan identitas

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait API gateway dan identitas.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Konfigurasi routing, validasi permintaan dan rate limit pada gateway lokal. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Konfigurasi gateway dan hasil uji. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan authentication dengan authorization.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 10 — Saga dan kompensasi

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Saga dan kompensasi.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Modelkan saga peminjaman; injeksikan kegagalan dan periksa aksi kompensasi. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram saga, trace dan catatan inkonsistensi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan choreography dan orchestration.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 11 — Circuit breaker, retry dan batas waktu

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Circuit breaker, retry dan batas waktu.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Simulasikan layanan gagal dan uji timeout, retry berbatas dan circuit breaker. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Log closed/open/half-open dan hasil uji. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan retry storm dan exponential backoff.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 12 — Integrasi ketahanan dan Tugas 2

- **Keterkaitan:** `Sub-CPMK-2.1`, `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Integrasi ketahanan dan Tugas 2.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Verifikasi gateway dan saga terhadap tiga skenario gagal; serahkan milestone Tugas 2. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Konfigurasi, diagram dan hasil fault injection. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan kapan kompensasi memerlukan intervensi.
- **Sumatif:** Tugas 2 25% pada pekan 12, mengukur `CPMK-3`: Konfigurasi gateway dan simulasikan saga beserta kompensasi serta circuit breaker. Bukti: Konfigurasi gateway, diagram saga dan laporan fault injection. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 13 — Tracing, log dan metrik

- **Keterkaitan:** `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Tracing, log dan metrik.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Instrumentasi trace lintas dua layanan dan korelasikan event dengan request ID. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Trace contoh dan log terkorelasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan trace, metrics dan logs.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 14 — CI/CD, kontainer dan pemeriksaan keamanan

- **Keterkaitan:** `Sub-CPMK-3.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait CI/CD, kontainer dan pemeriksaan keamanan.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bangun pipeline test, build dan pemindaian image pada repositori; gunakan rahasia dummy. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Workflow, image dan hasil pemeriksaan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan prinsip least privilege.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 15 — Integrasi dan uji ketahanan platform

- **Keterkaitan:** `Sub-CPMK-4.1`, `Sub-CPMK-4.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Integrasi dan uji ketahanan platform.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Gabungkan gateway, broker, observability dan pipeline; ukur hasil uji kegagalan pada lingkungan lokal. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Repo, diagram, rencana uji dan rekaman demo. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan hasil uji lokal dari klaim HA produksi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 16 — UAS: demonstrasi platform

- **Keterkaitan:** `Sub-CPMK-4.1`, `Sub-CPMK-4.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UAS: demonstrasi platform.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Tunjukkan sistem terintegrasi, CI/CD, trace dan jawaban individual. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Demo, bukti pipeline, trace dan laporan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Rangkum keterbatasan dan handoff.
- **Sumatif:** UAS 30% pada pekan 16, mengukur `CPMK-4`: Integrasikan build/test/deploy lokal dan distributed tracing pada dua layanan. Bukti: Repo, workflow CI/CD, trace, hasil pengujian dan demo. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

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
