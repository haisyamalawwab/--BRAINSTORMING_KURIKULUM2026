# 085_3 — OUTLINE BUKU MODUL PEMBELAJARAN DAN PRAKTIKUM

## STC-601 — Rekayasa & Otomasi Proses Bisnis (BPA) (*Business Process Engineering & Automation (BPA)*)

**Identitas:** `STC-601` Rekayasa & Otomasi Proses Bisnis (BPA) · Semester 6 · 3 SKS (+P: 2T + 1P) · Prasyarat `STI-306` · PL-3 · PEO-1, PEO-2 · IRM **M** · Klaster K-4 (adaptasi BPA).

## Spesifikasi buku dan peta bab

Empat belas bab untuk pekan 1–7 dan 9–15; pertemuan 8 dan 16 berupa evaluasi. Tiap bab memuat penjelasan konsep, contoh, latihan, praktik dan refleksi; kasus serta perangkat: Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual. Camunda 8 atau engine BPMN/DMN setara, PM4Py, UiPath/Python RPA dan OCR menggunakan dokumen sintetis. Silabus final dan batas topik mengikuti RPS. Prompt ilustrasi berikut adalah spesifikasi, bukan klaim gambar sudah dibuat.

### Bab 1. BPM lifecycle dan baseline proses — pekan 1

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi BPM lifecycle dan baseline proses; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Gambarkan proses as-is, pemangku kepentingan dan titik persetujuan pada kasus kampus.
- **Bukti dan kriteria:** BPMN as-is dan daftar aktivitas; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Definisikan cycle time dan throughput. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang BPM lifecycle dan baseline proses, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 2. BPMN, log peristiwa dan kualitas data — pekan 2

- **Capaian:** Sub-CPMK-1.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi BPMN, log peristiwa dan kualitas data; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Buat event log case ID, aktivitas dan timestamp; periksa data hilang dan urutan.
- **Bukti dan kriteria:** CSV sintetis dan laporan kualitas log; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan perbedaan activity time dan waiting time. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang BPMN, log peristiwa dan kualitas data, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 3. Process discovery dan bottleneck — pekan 3

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Process discovery dan bottleneck; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Temukan model proses dari log menggunakan process mining, hitung waktu tunggu dan throughput.
- **Bukti dan kriteria:** Model hasil discovery dan tabel KPI; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan batas simpulan dari log kecil. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Process discovery dan bottleneck, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 4. Conformance checking dan Tugas 1 — pekan 4

- **Capaian:** Sub-CPMK-1.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Conformance checking dan Tugas 1; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Bandingkan model as-is dengan jejak aktual, identifikasi deviasi dan rekomendasi perbaikan.
- **Bukti dan kriteria:** Laporan kesenjangan, bukti log dan Tugas 1; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan fitness dan precision proses. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Conformance checking dan Tugas 1, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 5. Workflow engine dan BPMN eksekutabel — pekan 5

- **Capaian:** Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Workflow engine dan BPMN eksekutabel; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Ubah model to-be menjadi BPMN yang dapat dijalankan; atur user/service task.
- **Bukti dan kriteria:** BPMN dan bukti instans workflow; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan peran token dan gateway. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Workflow engine dan BPMN eksekutabel, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 6. DMN dan aturan keputusan — pekan 6

- **Capaian:** Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi DMN dan aturan keputusan; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Rancang tabel keputusan dengan hit policy, batas nilai dan test case konflik.
- **Bukti dan kriteria:** Tabel DMN dan hasil uji aturan; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Bedakan hit policy Unique dan First. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang DMN dan aturan keputusan, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 7. Service task dan penanganan error — pekan 7

- **Capaian:** Sub-CPMK-2.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Service task dan penanganan error; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Integrasikan workflow ke API mock; uji timeout, kesalahan dan jalur manual.
- **Bukti dan kriteria:** Konfigurasi workflow, payload dan log; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan mekanisme retry dan eskalasi. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Service task dan penanganan error, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 8. RPA attended dan unattended — pekan 9

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi RPA attended dan unattended; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Pilih aktivitas cocok untuk bot, tetapkan batas otomasi dan izin akun latihan.
- **Bukti dan kriteria:** Matriks kelayakan RPA dan peta exception; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan risiko otomasi antarmuka rapuh. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang RPA attended dan unattended, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 9. Bot input formulir — pekan 10

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Bot input formulir; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Otomatiskan input pada formulir latihan lokal dengan verifikasi hasil dan timeout.
- **Bukti dan kriteria:** Script/bot, log dan hasil uji dummy; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan cara menangani elemen berubah. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Bot input formulir, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 10. OCR dan kualitas ekstraksi — pekan 11

- **Capaian:** Sub-CPMK-2.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi OCR dan kualitas ekstraksi; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Ekstrak field dokumen sintetis dengan OCR; bandingkan hasil dengan kebenaran dasar.
- **Bukti dan kriteria:** Dokumen contoh, hasil OCR dan error report; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan kapan human-in-the-loop diperlukan. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang OCR dan kualitas ekstraksi, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 11. Bot RPA dan Tugas 2 — pekan 12

- **Capaian:** Sub-CPMK-2.1, Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Bot RPA dan Tugas 2; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Gabungkan OCR dengan bot dan mekanisme penanganan kesalahan; serahkan milestone.
- **Bukti dan kriteria:** Bot, laporan uji dan rekaman Tugas 2; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan perlindungan data input/output. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Bot RPA dan Tugas 2, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 12. Integrasi workflow, bot dan API — pekan 13

- **Capaian:** Sub-CPMK-3.1; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Integrasi workflow, bot dan API; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Hubungkan service task pada mock ke bot; korelasikan case ID dengan log.
- **Bukti dan kriteria:** Diagram integrasi dan hasil uji jalur gagal; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan idempotensi dan audit trail. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Integrasi workflow, bot dan API, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 13. Pengukuran efisiensi dan akses — pekan 14

- **Capaian:** Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Pengukuran efisiensi dan akses; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Bandingkan baseline dan proses baru menggunakan data simulasi; cek akses berdasarkan peran.
- **Bukti dan kriteria:** Tabel KPI, asumsi dan pemeriksaan akses; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Jelaskan mengapa simulasi bukan dampak riil. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Pengukuran efisiensi dan akses, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

### Bab 14. Uji end-to-end dan dokumentasi — pekan 15

- **Capaian:** Sub-CPMK-3.2; mahasiswa dapat menjelaskan keputusan dan menunjukkan bukti yang bisa diperiksa.
- **Subtopik:** (1) konsep dan asumsi Uji end-to-end dan dokumentasi; (2) penerapan pada kasus; (3) verifikasi, kesalahan umum dan batas klaim.
- **Studi kasus:** Proses pengajuan fasilitas kampus dianalisis dari event log sintetis, diotomasi melalui workflow dan bot dengan pengecualian manual.
- **Aktivitas praktikum:** Uji kasus normal, exception dan pemulihan; siapkan runbook dan demo.
- **Bukti dan kriteria:** Test matrix, runbook dan catatan batas; periksa masukan, proses, hasil dan minimal satu kondisi gagal/revisi sesuai konteks.
- **Latihan dan refleksi:** Susun handoff ke pengembangan platform. Catat apa yang berubah ketika satu asumsi atau input kasus diubah dan jelaskan alasannya.
- **Prompt ilustrasi:** Buat diagram edukatif berlabel Indonesia tentang Uji end-to-end dan dokumentasi, menampilkan input, tahapan, output dan titik verifikasi, tanpa data pribadi. Aset yang benar-benar dibuat disimpan di `../assets/ilustrasi_modul/`.

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
