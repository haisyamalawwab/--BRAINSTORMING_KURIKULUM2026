# 082_5 — RUBRIK PENILAIAN PEMBELAJARAN

## STI-625 — Rekayasa Platform Digital (*Digital Platform Engineering*)

**Identitas:** `STI-625` Rekayasa Platform Digital · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-416` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-2.

## 1. Prinsip dan skala

Rubrik adaptasi K-2 Dok 018. Untuk setiap kriteria berikan skor 0–100 dengan acuan **Sangat Baik 81–100**, **Baik 66–80**, **Cukup 56–65**, **Kurang 0–55**; kalikan skor dengan bobot kriteria. Hasil penjumlahan adalah nilai instrumen. Rentang ini merupakan adaptasi operasional dari Dok 018, bukan klaim salinan batas kategori dokumen sumber.

### Tugas 1 — Rancangan bounded context (pekan 4, 20% MK)

**CPMK:** `CPMK-1`. **Tugas:** Susun konteks domain, batas minimal dua layanan dan kontrak untuk kasus peminjaman. **Bukti:** Context map, kontrak dan analisis trade-off.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Koherensi batas domain | 40% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| kepemilikan data | 30% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| kontrak layanan | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| argumentasi | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UTS — Komunikasi event (pekan 8, 25% MK)

**CPMK:** `CPMK-2`. **Tugas:** Implementasikan pertukaran event pada broker lokal, tangani duplikasi dan demonstrasikan redelivery. **Bukti:** Kode individual, skema event, log dan hasil uji.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Publish/consume | 40% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| idempotensi | 30% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| handling gagal | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| penjelasan jaminan delivery | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### Tugas 2 — Gateway dan saga tangguh (pekan 12, 25% MK)

**CPMK:** `CPMK-3`. **Tugas:** Konfigurasi gateway dan simulasikan saga beserta kompensasi serta circuit breaker. **Bukti:** Konfigurasi gateway, diagram saga dan laporan fault injection.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Routing | 40% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| ketepatan kompensasi | 30% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| timeout dan retry | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| bukti pengujian | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

### UAS — Pipeline platform terintegrasi (pekan 16, 30% MK)

**CPMK:** `CPMK-4`. **Tugas:** Integrasikan build/test/deploy lokal dan distributed tracing pada dua layanan. **Bukti:** Repo, workflow CI/CD, trace, hasil pengujian dan demo.

| Kriteria khusus instrumen | Bobot | Sangat Baik 81–100 | Baik 66–80 | Cukup 56–65 | Kurang 0–55 |
| --- | --- | --- | --- | --- | --- |
| Otomasi pipeline | 40% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| korelasi trace | 30% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| uji integrasi | 20% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |
| dokumentasi serta rahasia aman | 10% | Seluruh aspek kriteria terbukti tepat, lengkap, dapat diverifikasi dan sesuai konteks tugas. | Aspek utama terbukti benar; terdapat kekurangan minor yang tidak mengubah hasil. | Sebagian terbukti, tetapi ada langkah/asumsi penting yang belum tepat atau bukti terbatas. | Aspek utama tidak benar, gagal, atau tidak ada bukti yang dapat diverifikasi. |

## 2. Rubrik formatif dan refleksi

Setiap praktik diberi status **tercapai / perlu perbaikan / belum ditunjukkan** untuk ketepatan proses, kualitas bukti dan penjelasan batas; tidak menambah bobot nilai sumatif. Refleksi persepsi 1–5 (1 sangat tidak setuju sampai 5 sangat setuju): saya dapat menjelaskan konsep; saya dapat menguji hasil; saya memahami batas dan risiko; saya berkontribusi dalam tim. Refleksi bukan pengganti penilaian capaian.

## 3. Lembar penilaian

| Mahasiswa | Instrumen | Kriteria 1–4 (0–100) | Skor berbobot | CPMK | Umpan balik dan tindak lanjut |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

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
