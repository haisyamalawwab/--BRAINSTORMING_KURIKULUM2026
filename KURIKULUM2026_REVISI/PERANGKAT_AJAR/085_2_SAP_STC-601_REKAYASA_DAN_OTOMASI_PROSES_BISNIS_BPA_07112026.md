# 085_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN

## STC-601 — Rekayasa & Otomasi Proses Bisnis (BPA) (*Business Process Engineering & Automation (BPA)*)

**Identitas:** `STC-601` Rekayasa & Otomasi Proses Bisnis (BPA) · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-306` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-4 (adaptasi BPA).

## Pedoman pelaksanaan

Kasus bersama: Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual. Perangkat: Camunda 8 atau engine BPMN/DMN setara, PM4Py, UiPath/Python RPA dan OCR menggunakan dokumen sintetis. Pembelajaran menggunakan kelompok kecil dengan bukti kontribusi individual. **TM 100 menit:** pembuka 10, demonstrasi/kasus 75, refleksi 15. **Praktik 170 menit:** briefing 15, pengerjaan 120, pengujian dan umpan balik 25, penutupan 10. **PT 120 menit, BM 120 menit** di luar kelas. Setiap praktik memakai data dan sistem berizin.

### Pertemuan 1 — BPM lifecycle dan baseline proses

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait BPM lifecycle dan baseline proses.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Gambarkan proses as-is, pemangku kepentingan dan titik persetujuan pada kasus kampus. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** BPMN as-is dan daftar aktivitas. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Definisikan cycle time dan throughput.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 2 — BPMN, log peristiwa dan kualitas data

- **Keterkaitan:** `Sub-CPMK-1.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait BPMN, log peristiwa dan kualitas data.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Buat event log case ID, aktivitas dan timestamp; periksa data hilang dan urutan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** CSV sintetis dan laporan kualitas log. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan perbedaan activity time dan waiting time.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 3 — Process discovery dan bottleneck

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Process discovery dan bottleneck.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Temukan model proses dari log menggunakan process mining, hitung waktu tunggu dan throughput. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Model hasil discovery dan tabel KPI. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan batas simpulan dari log kecil.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 4 — Conformance checking dan Tugas 1

- **Keterkaitan:** `Sub-CPMK-1.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Conformance checking dan Tugas 1.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bandingkan model as-is dengan jejak aktual, identifikasi deviasi dan rekomendasi perbaikan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Laporan kesenjangan, bukti log dan Tugas 1. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan fitness dan precision proses.
- **Sumatif:** Tugas 1 20% pada pekan 4, mengukur `CPMK-1`: Gunakan log sintetis untuk discovery, pengukuran cycle time dan analisis deviasi terhadap model. Bukti: Event log, model, perhitungan KPI dan rekomendasi. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 5 — Workflow engine dan BPMN eksekutabel

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Workflow engine dan BPMN eksekutabel.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Ubah model to-be menjadi BPMN yang dapat dijalankan; atur user/service task. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** BPMN dan bukti instans workflow. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan peran token dan gateway.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 6 — DMN dan aturan keputusan

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait DMN dan aturan keputusan.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Rancang tabel keputusan dengan hit policy, batas nilai dan test case konflik. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Tabel DMN dan hasil uji aturan. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Bedakan hit policy Unique dan First.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 7 — Service task dan penanganan error

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Service task dan penanganan error.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Integrasikan workflow ke API mock; uji timeout, kesalahan dan jalur manual. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Konfigurasi workflow, payload dan log. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan mekanisme retry dan eskalasi.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 8 — UTS: workflow dan DMN

- **Keterkaitan:** `Sub-CPMK-2.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UTS: workflow dan DMN.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bangun dan jalankan workflow berikut aturan keputusan; uji kasus normal dan gagal. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** BPMN, DMN dan bukti uji individual. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Refleksi setelah umpan balik.
- **Sumatif:** UTS 25% pada pekan 8, mengukur `CPMK-2`: Implementasikan workflow dan tabel keputusan dengan service task mock dan jalur exception. Bukti: BPMN, DMN, bukti eksekusi dan jawaban individual. Ujian dikerjakan dan dipertanggungjawabkan individual.

### Pertemuan 9 — RPA attended dan unattended

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait RPA attended dan unattended.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Pilih aktivitas cocok untuk bot, tetapkan batas otomasi dan izin akun latihan. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Matriks kelayakan RPA dan peta exception. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan risiko otomasi antarmuka rapuh.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 10 — Bot input formulir

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Bot input formulir.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Otomatiskan input pada formulir latihan lokal dengan verifikasi hasil dan timeout. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Script/bot, log dan hasil uji dummy. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan cara menangani elemen berubah.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 11 — OCR dan kualitas ekstraksi

- **Keterkaitan:** `Sub-CPMK-2.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait OCR dan kualitas ekstraksi.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Ekstrak field dokumen sintetis dengan OCR; bandingkan hasil dengan kebenaran dasar. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Dokumen contoh, hasil OCR dan error report. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan kapan human-in-the-loop diperlukan.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 12 — Bot RPA dan Tugas 2

- **Keterkaitan:** `Sub-CPMK-2.1`, `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Bot RPA dan Tugas 2.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Gabungkan OCR dengan bot dan mekanisme penanganan kesalahan; serahkan milestone. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Bot, laporan uji dan rekaman Tugas 2. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan perlindungan data input/output.
- **Sumatif:** Tugas 2 25% pada pekan 12, mengukur `CPMK-3`: Bangun bot untuk input formulir latihan dan ekstraksi dokumen sintetis dengan fallback manual. Bukti: Bot, data dummy, hasil OCR dan log pengujian. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

### Pertemuan 13 — Integrasi workflow, bot dan API

- **Keterkaitan:** `Sub-CPMK-3.1`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Integrasi workflow, bot dan API.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Hubungkan service task pada mock ke bot; korelasikan case ID dengan log. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Diagram integrasi dan hasil uji jalur gagal. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan idempotensi dan audit trail.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 14 — Pengukuran efisiensi dan akses

- **Keterkaitan:** `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Pengukuran efisiensi dan akses.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Bandingkan baseline dan proses baru menggunakan data simulasi; cek akses berdasarkan peran. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Tabel KPI, asumsi dan pemeriksaan akses. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Jelaskan mengapa simulasi bukan dampak riil.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 15 — Uji end-to-end dan dokumentasi

- **Keterkaitan:** `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait Uji end-to-end dan dokumentasi.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Uji kasus normal, exception dan pemulihan; siapkan runbook dan demo. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Test matrix, runbook dan catatan batas. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Susun handoff ke pengembangan platform.
- **Formatif:** umpan balik praktik, tidak menambah bobot nilai akhir.

### Pertemuan 16 — UAS: solusi BPA terpadu

- **Keterkaitan:** `Sub-CPMK-2.2`, `Sub-CPMK-3.2`.
- **Pembuka (10 menit):** tinjau prasyarat dan jelaskan tujuan serta keamanan kerja terkait UAS: solusi BPA terpadu.
- **Inti TM (75 menit):** dosen membahas konsep dan keputusan pada kasus; mahasiswa mengajukan alasan, asumsi, serta langkah kerja.
- **Penutup TM (15 menit):** periksa pemahaman dan rumuskan hipotesis/hasil yang akan diuji pada praktik.
- **Praktik (170 menit):** briefing 15 menit; 120 menit implementasi: Demonstrasikan workflow, keputusan dan bot, lalu pertahankan hasil secara individual. Pengujian dan umpan balik 25 menit; simpulan, pencadangan serta penutupan 10 menit.
- **Indikator dan bukti:** Model, bot, log, laporan dan presentasi. Dosen memeriksa hasil terhadap asumsi, keterulangan dan batas kasus.
- **PT (120 menit):** rapikan bukti, tambahkan skenario uji atau jawaban beralasan, dan serahkan melalui LMS. **BM (120 menit):** Rangkum umpan balik dan perbaikan.
- **Sumatif:** UAS 30% pada pekan 16, mengukur `CPMK-3`: Integrasikan workflow BPMN/DMN dengan bot; ukur KPI simulasi dan uji jalur exception. Bukti: Diagram, workflow, bot, KPI, bukti uji dan demo tim. Tugas/proyek berbasis kerja tim dengan verifikasi kontribusi individual.

## Acuan, guardrails dan rekonsiliasi

**BoK Dok 043:** `BK-IS09` *Business Process Management*, `BK-IS07` *Systems Analysis and Design*. **Pembina Dok 004:** BK-IS09 primer dan BK-IS07 sekunder; Dok 037 juga menyebut BK-IT11.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Rekayasa Proses Bisnis Enterprise, Simulasi Alur Kerja Bisnis (BPMN), Robotic Process Automation (RPA dasar: UiPath / Camunda), Integrasi Alur Kerja Antar-Departemen, Pengukuran Efisiensi Proses.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang koding antarmuka visual grafis aplikasi dari nol, audit pembukuan keuangan korporat, perancangan firewall jaringan.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Mengotomatisasi proses bisnis organisasi; menyerahkan integrasi platform vertikal ke `STC-602`.

Batas tambahan Dok 037: tidak mengembangkan full-stack aplikasi dari nol atau audit COBIT.

**Catatan sumber:** Dok 037 memberi empat CPMK serta P2/KK4/KK5; Dok 043 memberi tiga CPMK dan P2/P4/KK5, selaras pembebanan Dok 004. Dok 043 menempatkan RPA pada Sub-CPMK-2.1 dan integrasi pada Sub-CPMK-3.1 meski rumusan CPMK-3 berfokus RPA; bukti dinilai menurut rumusan CPMK. OCR menggunakan data sintetis, bukan identitas nyata. Dok 043 merumuskan tiga CPMK, sehingga empat instrumen tidak dipaksakan menjadi empat CPMK: Tugas 2 dan UAS sama-sama mengukur CPMK-3. Penyesuaian rencana mingguan di bawah mengutamakan kompetensi dan asesmen sebelum pekan pengumpulan; detail teknologi dari Dok 007 digunakan sejauh tidak melanggar guardrails. Prasyarat dan kode resmi mengikuti Dok 005/051. Perbedaan antar sumber ini perlu dikonfirmasi koordinator.

**Skenario:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.

**Rujukan kurikulum:** Dok 003/004 (CPL, IRM dan BoK); 005/051 (identitas dan prasyarat); 007/043 (materi, CPMK/Sub-CPMK); 008/018 (asesmen); 037/043 (boundary); 053 dan README perangkat ajar (format).

**Pustaka teknis:** Dumas et al., *Fundamentals of Business Process Management*, 2nd ed. (2018); OMG BPMN 2.0.2 dan DMN; dokumentasi Camunda dan PM4Py.
