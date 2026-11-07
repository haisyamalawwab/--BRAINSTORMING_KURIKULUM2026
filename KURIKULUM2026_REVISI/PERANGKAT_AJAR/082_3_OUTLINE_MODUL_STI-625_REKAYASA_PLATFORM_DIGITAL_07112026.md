# 082_3 — OUTLINE BUKU MODUL PEMBELAJARAN DAN PRAKTIKUM

## STI-625 — Rekayasa Platform Digital (*Digital Platform Engineering*)

**Identitas:** `STI-625` Rekayasa Platform Digital · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-416` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-2.

## Spesifikasi buku dan peta bab

Empat belas bab untuk pekan 1–7 dan 9–15; pertemuan 8 dan 16 berupa evaluasi. Tiap bab memuat penjelasan konsep, contoh, latihan, praktik dan refleksi; kasus serta perangkat: Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi. Docker Compose, Git, layanan REST/gRPC sederhana, Kafka atau RabbitMQ lokal, OpenTelemetry dan GitHub Actions. Silabus final dan batas topik mengikuti RPS. Prompt ilustrasi berikut adalah spesifikasi, bukan klaim gambar sudah dibuat.

### Bab 1. Monolit, microservices dan konteks bisnis — pekan 1

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Monolit, microservices dan konteks bisnis; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Bandingkan arsitektur monolit dan layanan dari skenario, termasuk trade-off latensi dan transaksi.
- **Bukti dan kriteria:** Diagram konteks dan alasan batas layanan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan kapan monolit lebih tepat. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Monolit, microservices dan konteks bisnis, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 2. DDD dan bounded context — pekan 2

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi DDD dan bounded context; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Petakan domain, aggregate, batas kepemilikan data dan kontrak antar dua layanan.
- **Bukti dan kriteria:** Context map dan kontrak layanan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan aggregate dari bounded context. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang DDD dan bounded context, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 3. Kontrak API dan komunikasi sinkron — pekan 3

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Kontrak API dan komunikasi sinkron; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Rancang kontrak REST atau gRPC dan uji timeout pada layanan contoh.
- **Bukti dan kriteria:** Spesifikasi API dan hasil uji; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bandingkan coupling sinkron dan asinkron. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Kontrak API dan komunikasi sinkron, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 4. Arsitektur layanan dan Tugas 1 — pekan 4

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Arsitektur layanan dan Tugas 1; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Tinjau batas layanan, diagram konteks dan alur data; serahkan rancangan arsitektur kasus.
- **Bukti dan kriteria:** Diagram, kontrak dan justifikasi Tugas 1; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Tulis risiko transaksi lintas layanan. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Arsitektur layanan dan Tugas 1, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 5. Event-driven dan broker — pekan 5

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Event-driven dan broker; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Definisikan event, producer dan consumer pada broker lokal dengan skema pesan berversi.
- **Bukti dan kriteria:** Skema event dan demo publish/subscribe; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan event dan command. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Event-driven dan broker, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 6. Delivery guarantees dan idempotensi — pekan 6

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Delivery guarantees dan idempotensi; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Simulasikan pesan duplikat; implementasikan idempotency key dan catat offset/ack.
- **Bukti dan kriteria:** Log pengujian duplikat dan kode consumer; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan at-least-once dan risiko exactly-once. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Delivery guarantees dan idempotensi, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 7. Kafka/RabbitMQ dan penanganan gagal — pekan 7

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Kafka/RabbitMQ dan penanganan gagal; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Uji redelivery dan dead-letter pada broker lokal; dokumentasikan pemulihan.
- **Bukti dan kriteria:** Konfigurasi broker dan bukti uji gagal; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan ordering dan partisi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Kafka/RabbitMQ dan penanganan gagal, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 8. API gateway dan identitas — pekan 9

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi API gateway dan identitas; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Konfigurasi routing, validasi permintaan dan rate limit pada gateway lokal.
- **Bukti dan kriteria:** Konfigurasi gateway dan hasil uji; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan authentication dengan authorization. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang API gateway dan identitas, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 9. Saga dan kompensasi — pekan 10

- **Capaian:** Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Saga dan kompensasi; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Modelkan saga peminjaman; injeksikan kegagalan dan periksa aksi kompensasi.
- **Bukti dan kriteria:** Diagram saga, trace dan catatan inkonsistensi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan choreography dan orchestration. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Saga dan kompensasi, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 10. Circuit breaker, retry dan batas waktu — pekan 11

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Circuit breaker, retry dan batas waktu; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Simulasikan layanan gagal dan uji timeout, retry berbatas dan circuit breaker.
- **Bukti dan kriteria:** Log closed/open/half-open dan hasil uji; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan retry storm dan exponential backoff. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Circuit breaker, retry dan batas waktu, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 11. Integrasi ketahanan dan Tugas 2 — pekan 12

- **Capaian:** Sub-CPMK-2.1, Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Integrasi ketahanan dan Tugas 2; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Verifikasi gateway dan saga terhadap tiga skenario gagal; serahkan milestone Tugas 2.
- **Bukti dan kriteria:** Konfigurasi, diagram dan hasil fault injection; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan kapan kompensasi memerlukan intervensi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Integrasi ketahanan dan Tugas 2, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 12. Tracing, log dan metrik — pekan 13

- **Capaian:** Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Tracing, log dan metrik; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Instrumentasi trace lintas dua layanan dan korelasikan event dengan request ID.
- **Bukti dan kriteria:** Trace contoh dan log terkorelasi; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan trace, metrics dan logs. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Tracing, log dan metrik, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 13. CI/CD, kontainer dan pemeriksaan keamanan — pekan 14

- **Capaian:** Sub-CPMK-3.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi CI/CD, kontainer dan pemeriksaan keamanan; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Bangun pipeline test, build dan pemindaian image pada repositori; gunakan rahasia dummy.
- **Bukti dan kriteria:** Workflow, image dan hasil pemeriksaan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan prinsip least privilege. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang CI/CD, kontainer dan pemeriksaan keamanan, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 14. Integrasi dan uji ketahanan platform — pekan 15

- **Capaian:** Sub-CPMK-4.1, Sub-CPMK-4.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Integrasi dan uji ketahanan platform; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Platform layanan peminjaman kampus memisahkan layanan inventaris dan peminjaman dengan event dan jejak transaksi.
- **Aktivitas praktikum:** Gabungkan gateway, broker, observability dan pipeline; ukur hasil uji kegagalan pada lingkungan lokal.
- **Bukti dan kriteria:** Repo, diagram, rencana uji dan rekaman demo; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan hasil uji lokal dari klaim HA produksi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Integrasi dan uji ketahanan platform, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

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
