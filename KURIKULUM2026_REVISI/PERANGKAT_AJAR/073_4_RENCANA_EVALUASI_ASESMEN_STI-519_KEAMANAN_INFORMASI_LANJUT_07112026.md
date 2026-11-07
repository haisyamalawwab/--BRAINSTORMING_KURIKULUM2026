# 073_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN

## STI-519 — Keamanan Informasi Lanjut

**Identitas:** `STI-519` Keamanan Informasi Lanjut · Semester 5 · 3 SKS (Teori) · Prasyarat: `STI-418` · PL-2 · PEO-1 · IRM M · Rubrik K-3.

## 1. Rancangan empat titik asesmen

| Instrumen | Pekan | Bobot MK | Alokasi CPMK dari bobot MK | Bukti utama | Produk |
| --- | --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 20% | Rencana dan asesmen kerentanan | Rules of engagement, inventaris aset, bukti hasil pemindaian dan rekomendasi |
| UTS | 8 | 30% | CPMK-1 30% | Ujian analisis penetrasi aplikasi | Jawaban kasus individual, matriks temuan-bukti-mitigasi |
| Tugas 2 | 12 | 20% | CPMK-2 20% | Audit kontrol dan SoA | Matriks kontrol, alasan penerapan/pengecualian, bukti dan rencana tindak lanjut |
| UAS | 16 | 30% | CPMK-3 30% | Respons insiden dan pertahanan | Incident response plan, kronologi, rekomendasi hardening dan presentasi |

**IKU 7:** Tugas 1 (20%) + Tugas 2 (20%) + UAS (30%) = 70% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 2. Matriks alokasi per CPMK

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-12 (KK4) | 20% | 30% | — | — | 50% |
| CPMK-2 | CPL-07 (P3), CPL-11 (KK3) | — | — | 20% | — | 20% |
| CPMK-3 | CPL-11 (KK3), CPL-12 (KK4) | — | — | — | 30% | 30% |
| Total | — | 20% | 30% | 20% | 30% | 100% |

### Cara penghitungan ketercapaian

Nilai setiap instrumen (0–100) dihitung dari rubrik dokumen 5. Nilai akhir = jumlah (bobot instrumen / 100 × nilai instrumen). Bila satu instrumen mengukur lebih dari satu CPMK, penguji memberi **skor butir terpisah per CPMK**, bukan menyalin skor total. Skor instrumen = Σ(alokasi bobot MK tiap CPMK pada instrumen × skor bagian CPMK) / bobot instrumen; ini juga mencegah hitung ganda. Nilai CPMK j = Σ(alokasi bobot instrumen untuk j × skor butir j) / Σ(alokasi bobot instrumen untuk j). Nilai CPL = rata-rata tertimbang nilai CPMK yang mendukung CPL tersebut, memakai total alokasi masing-masing CPMK sebagai bobot; hasil antar-CPL tidak dijumlahkan sebagai nilai akhir. Ini rancangan lokal untuk pemantauan, bukan persentase CPL yang telah disahkan.

Contoh operasional: skor butir 80 pada alokasi 20% dan 70 pada alokasi 10% menghasilkan (20×80 + 10×70)/30 = 76,67 untuk CPMK itu. Ambang awal pemantauan 70/100 **usulan**; batas lulus, remedial, proporsi dan kebijakan resmi ditetapkan prodi.

## 3. Kisi-kisi dan rencana tugas

### Tugas 1 — Rencana dan asesmen kerentanan

- **Waktu/bobot:** pekan 4, 20% nilai MK. **Kisi-kisi CPMK:** CPMK-1 (20 poin bobot MK).
- **Masalah dan instruksi:** Rumuskan ruang lingkup dan aturan keterlibatan; identifikasi risiko aplikasi latihan, klasifikasi CVE/CVSS dan langkah mitigasi.
- **Bukti wajib:** Rules of engagement, inventaris aset, bukti hasil pemindaian dan rekomendasi.
- **Indikator:** otorisasi dan batas target; ketepatan CVSS; bukti dapat ditelusuri.
- **Pelaksanaan:** kerja berbasis kasus/proyek; penilaian individual melalui kontribusi dan tanya jawab; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### UTS — Ujian analisis penetrasi aplikasi

- **Waktu/bobot:** pekan 8, 30% nilai MK. **Kisi-kisi CPMK:** CPMK-1 (30 poin bobot MK).
- **Masalah dan instruksi:** Analisis temuan OWASP pada aplikasi uji dan petakan tahapan PTES ke MITRE ATT&CK; susun validasi non-destruktif.
- **Bukti wajib:** Jawaban kasus individual, matriks temuan-bukti-mitigasi.
- **Indikator:** validitas temuan dan perbedaan indikasi dengan bukti; prioritas perbaikan.
- **Pelaksanaan:** ujian individual dengan bukti dan klarifikasi lisan; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### Tugas 2 — Audit kontrol dan SoA

- **Waktu/bobot:** pekan 12, 20% nilai MK. **Kisi-kisi CPMK:** CPMK-2 (20 poin bobot MK).
- **Masalah dan instruksi:** Dari skenario organisasi, petakan kontrol ISO/IEC 27001:2022 dan bukti, lalu susun SoA dan gap.
- **Bukti wajib:** Matriks kontrol, alasan penerapan/pengecualian, bukti dan rencana tindak lanjut.
- **Indikator:** keterlacakan klausul, keputusan SoA dan kelayakan tindakan.
- **Pelaksanaan:** kerja berbasis kasus/proyek; penilaian individual melalui kontribusi dan tanya jawab; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

### UAS — Respons insiden dan pertahanan

- **Waktu/bobot:** pekan 16, 30% nilai MK. **Kisi-kisi CPMK:** CPMK-3 (30 poin bobot MK).
- **Masalah dan instruksi:** Evaluasi skenario kebocoran, urutkan triase, containment, preservasi bukti dasar dan komunikasi insiden; kaitkan audit dan hasil uji.
- **Bukti wajib:** Incident response plan, kronologi, rekomendasi hardening dan presentasi.
- **Indikator:** prioritas dampak, preservasi bukti, batas kewenangan dan kelayakan pemulihan.
- **Pelaksanaan:** proyek tim dengan bukti kolaborasi, demonstrasi dan pembelaan individual; rubrik empat kriteria pada dokumen 5. Alokasi pada matriks harus dinilai dengan butir/bukti terpisah untuk tiap CPMK.
- **Pengumpulan:** LMS pada pekan yang ditentukan, sertakan sumber, asumsi, hasil dan keterbatasan; dosen menyediakan kasus pengganti setara jika sarana tidak tersedia.

## 4. Integritas, umpan balik dan CQI

Nilai kelompok dikonfirmasi dengan kontribusi dan pembelaan individual. Dosen mencatat skor per butir/CPMK dan umpan balik, memberi kesempatan klarifikasi dan remediasi sesuai peraturan prodi; remediasi tidak otomatis menambah komponen nilai kelima. Pada akhir semester, rekap sebaran capaian tiap CPMK dan CPL, analisis soal/bukti dengan capaian rendah, catat penyebab, rencana perbaikan, penanggung jawab dan tindak lanjut pada siklus PPEPP. Jaga data pribadi dan arsipkan bukti sesuai kebijakan institusi.

## Acuan, batas dan keputusan penyelarasan

**BoK (Dok 043):** `BK-IS06` *Information Security*, `BK-IT06` *Cybersecurity Principles*. Klasifikasi pembina menurut Dok 004: primer BK-IS06 dan BK-IT06.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Keamanan Sistem Operasi Lanjut, Zero Trust Architecture, Manajemen Kerentanan (CVE/CVSS), Security Information & Event Management (SIEM dasar), Penetrasi Web Dasar (OWASP Top 10), Defense in Depth.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang forensik memori tingkat rendah, eksploitasi zero-day kernel, penyusunan roadmap arsitektur keamanan korporasi.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menguasai hardening dan pertahanan sistem; menyerahkan manajemen risiko dan kepatuhan ke `STB-602`.

**Catatan rekonsiliasi:** Dokumen 043 mengaitkan Sub-CPMK-2.1/2.2 (OWASP/biner) dengan CPMK-2 (audit), dan Sub-CPMK-3.2 (audit) dengan CPMK-3 (insiden); bukti teknis digunakan lintas CPMK. Jadwal mengikuti kompetensi substansinya, bukan menyembunyikan ketidaksesuaian ini. Materi agresif Dok 007 dibatasi menjadi analisis etis lokal; forensik memori tingkat rendah diserahkan ke STB-501. Identitas dan prasyarat mengikuti Dok 005/051; rumusan CPMK/Sub-CPMK mengikuti Dok 043, tema mingguan mengadaptasi Dok 007 sepanjang tidak melanggar batas Dok 037/043. Ketidakcocokan antardokumen dicatat untuk validasi koordinator, bukan diubah diam-diam.

**Skenario terapan:** Aplikasi layanan kampus memiliki laporan kerentanan; hanya lingkungan uji terisolasi dengan izin tertulis yang boleh digunakan.

**Sumber:**
1. Dokumen 003 dan 004: rumusan CPL, matriks IRM dan BoK.
2. Dokumen 005 dan 051: identitas, beban dan prasyarat mata kuliah.
3. Dokumen 007 dan 043: CPMK, Sub-CPMK dan rencana pembelajaran.
4. Dokumen 008 dan 018: pengukuran OBE dan klaster asesmen.
5. Dokumen 037 dan 043: boundary guardrails dan handoff.
6. Rujukan teknis: PTES Technical Guidelines; MITRE ATT&CK; ISO/IEC 27001:2022; OWASP Top 10.
