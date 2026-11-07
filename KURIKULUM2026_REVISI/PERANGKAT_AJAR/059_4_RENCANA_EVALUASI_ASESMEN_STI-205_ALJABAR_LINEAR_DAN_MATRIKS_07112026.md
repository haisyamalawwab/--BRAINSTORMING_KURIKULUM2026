# RENCANA EVALUASI DAN ASESMEN
## STI-205 — ALJABAR LINEAR DAN MATRIKS

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang
> **Dokumen induk:** `059_1_RPS_STI-205_ALJABAR_LINEAR_DAN_MATRIKS_07112026.md`
> **Rujukan sistem:** Dokumen 008 (Sistem Asesmen OBE & Formula Ketercapaian CPL), Dokumen 018 (Rubrik Master), Dokumen 043 (CPMK/Sub-CPMK)
> **Tanggal:** 07 November 2026

---

## 1. IDENTITAS DAN RUANG LINGKUP

| Atribut | Keterangan |
|---|---|
| Mata kuliah | Aljabar Linear dan Matriks (`STI-205`) |
| Bobot / tipe | 3 SKS / Teori |
| Semester | 2 (Genap) |
| CPL dibina | `CPL-05` (`P1`) (Aljabar Linear, Ruang Vektor & Dekomposisi Matriks) — **tunggal** |
| CPMK | CPMK-1 (C3), CPMK-2 (C4), CPMK-3 (C3), CPMK-4 (C4) |
| Jumlah Sub-CPMK | 8 |
| Skema asesmen | 4 titik baku: Tugas 1 (20%), UTS (30%), Tugas 2 (20%), UAS (30%) |
| Ambang ketuntasan MK | Nilai akhir ≥ 60 (huruf C) |
| Ambang ketercapaian CPL | Skor ≥ 65,0 (Dokumen 008) |
| Distribusi bobot CPL | `CPL-05` (`P1`) 100% (MK ini pembina tunggal untuk blok aljabar linear) |

---

## 2. PRINSIP EVALUASI

1. **Berbasis luaran (*outcome-based*):** setiap instrumen mengukur CPMK/Sub-CPMK eksplisit pada level Bloom yang sesuai (C3–C4).
2. **Valid:** butir selaras dengan kata kerja operasional CPMK — "menyelesaikan", "menganalisis", "menghitung", "merumuskan".
3. **Reliabel:** kunci jawaban berlapis (poin per langkah OBE dan per langkah derivasi) menjamin konsistensi antar-kelas paralel.
4. **Adil dan transparan:** bobot, kriteria, dan tenggat diumumkan pada pekan 1 dan tersedia di LMS.
5. **Autentik:** soal berbasis situasi nyata (jaringan pipa, reduksi indikator akademik, kompresi citra), bukan manipulasi simbolik dekontekstualisasi.
6. **Formatif mendukung sumatif:** 11 pekan non-asesmen digunakan untuk umpan balik tanpa bobot nilai.
7. **Menghargai proses:** skor diberikan pada **langkah komputasi**, bukan hanya hasil akhir — mencerminkan kemampuan aljabar yang dapat diaudit.
8. **Verifikasi silang manual–komputasi:** pada CPMK-4, hasil NumPy wajib diverifikasi manual pada sampel kecil agar mahasiswa tidak bergantung pada pustaka tanpa pemahaman.
9. **Berkeadilan digital:** mahasiswa dengan keterbatasan perangkat/koneksi mendapat penyesuaian tenggat dan akses notebook daring.

---

## 3. SKEMA 4 TITIK ASESMEN

| Titik | Pekan | Instrumen | CPMK | Bobot | Sifat |
|:---:|:---:|---|:---:|:---:|:---:|
| **Tugas 1** | 4 | Kuis + problem solving "SPL, Matriks, dan Struktur Ruang Vektor" | CPMK-1, CPMK-2 | **20%** | Individu |
| **UTS** | 8 | Ujian tertulis matriks, SPL, ruang vektor, dan eigen | CPMK-1, CPMK-2, CPMK-3 (awal) | **30%** | Individu, *closed book* |
| **Tugas 2** | 12 | Proyek terapan "Aljabar Linear untuk Reduksi Dimensi Data" | CPMK-3, CPMK-4 | **20%** | Kelompok 3–4 orang |
| **UAS** | 16 | Ujian komprehensif + pemodelan terbuka | CPMK-1 s.d. CPMK-4 | **30%** | Individu |
| | | **TOTAL** | | **100%** | |

**Catatan komposisi:** 47,5% bobot berasal dari asesmen berbasis kasus/proyek/kinerja, yaitu Tugas 1 20% + Tugas 2 20% + Bagian IV UAS 7,5% (25 poin × 30%). Angka ini **belum** mencapai ambang IKU 7 (≥ 50%); opsi pemenuhan dibahas pada Bagian 11.

---

## 4. RENCANA ASESMEN RINCI

### 4.1 Tugas 1 — SPL, Matriks, dan Struktur Ruang Vektor (20%)

| Komponen | Uraian |
|---|---|
| CPMK diukur | CPMK-1 (50%), CPMK-2 (50%) |
| Sub-CPMK | 1.1, 1.2, 2.1 |
| Indikator | 1.1.1–1.1.2; 1.2.1–1.2.2; 2.1.1–2.1.2 |
| Bentuk | Lembar jawaban bertahap: OBE lengkap, determinan/invers, uji kombinasi linier & span, uji subruang |
| Teknik | Penugasan terstruktur (unjuk kerja tertulis) |
| Waktu | Dikerjakan di kelas pekan 4 (150′) + penyelesaian mandiri 3 hari |
| Media | LMS (unggah PDF), formulir naskah |
| Rubrik | `055_5` Rubrik Tugas 1 (4 dimensi: 25/25/30/20) |
| Umpan balik | Komentar per dimensi ≤ 7 hari |

### 4.2 UTS — Matriks, SPL, Ruang Vektor, dan Eigen (30%)

| Komponen | Uraian |
|---|---|
| CPMK diukur | CPMK-1 (30%), CPMK-2 (35%), CPMK-3 (25%), CPMK-1/2 pada studi kasus (10%) |
| Sub-CPMK | 1.1, 1.2, 2.1, 2.2, 3.1, 3.2 |
| Indikator | Seluruh indikator pekan 1–7 |
| Bentuk | I SPL/OBE/determinan/invers (30), II ruang vektor/basis/dimensi (35), III eigen & diagonalisasi (25), IV studi kasus pemodelan matriks (10) |
| Teknik | Tes tertulis terjadwal |
| Waktu | Pekan 8, 150 menit, *closed book* |
| Pengawasan | Dosen + 1 pengawas; tata tertib ujian fakultas |
| Rubrik | `055_5` Rubrik UTS (4 dimensi: 25/30/30/15) |
| Analisis pasca-ujian | Analisis butir (tingkat kesukaran, daya beda) dalam 7 hari |

### 4.3 Tugas 2 — Aljabar Linear untuk Reduksi Dimensi Data (20%)

| Komponen | Uraian |
|---|---|
| CPMK diukur | CPMK-3 (30%), CPMK-4 (70%) |
| Sub-CPMK | 3.1, 3.2, 4.1, 4.2, 4.3, 4.4 |
| Indikator | 3.1.1–3.1.2; 3.2.1–3.2.2; 4.1.1–4.1.2; 4.2.1–4.2.2 |
| Bentuk | Laporan proyek 12–16 halaman + notebook Python (`.ipynb`) + slide 7 halaman |
| Teknik | Proyek kelompok (unjuk kerja produk tertulis + presentasi + artefak kode) |
| Waktu | Diumumkan pekan 11, presentasi antara pekan 12, finalisasi pekan 13 |
| Media | LMS; repositori dokumen & kode kelompok |
| Rubrik | `055_5` Rubrik Tugas 2 (4 dimensi: 30/25/25/20) |
| Anti-*free-rider* | Lembar pembagian peran + verifikasi lisan acak (termasuk meminta mahasiswa menjelaskan satu baris kode) |

### 4.4 UAS — Evaluasi Komprehensif (30%)

| Komponen | Uraian |
|---|---|
| CPMK diukur | CPMK-1 (20%), CPMK-2 (25%), CPMK-3 (30%), CPMK-4 (25%) |
| Sub-CPMK | Seluruh Sub-CPMK 1.1–4.2 |
| Indikator | Seluruh indikator pekan 1–15 |
| Bentuk | I SPL/matriks/determinan/invers (20), II ruang vektor/basis/ortogonalitas (25), III eigen/diagonalisasi/SVD (30), IV pemodelan terbuka (25) |
| Teknik | Tes tertulis komprehensif |
| Waktu | Pekan 16, 150 menit, *closed book* |
| Rubrik | `055_5` Rubrik UAS (4 dimensi: 25/30/30/15) |

### 4.5 Aktivitas Formatif (tanpa bobot)

| Pekan | Aktivitas | Umpan Balik |
|:--:|---|---|
| 1 | Tes diagnostik vektor & aljabar elementer | Peta kesiapan kelas |
| 2 | Kuis operasi matriks & OBE di LMS | Skor otomatis + pembahasan |
| 3 | Lembar latihan determinan & invers | Komentar tertulis |
| 5 | Lembar latihan kebebasan linier & Gram–Schmidt | Pembahasan kelas |
| 6 | Kuis transformasi linier & eigen | Skor otomatis |
| 7 | Lembar kerja diagonalisasi | Pembahasan kelas |
| 9 | Lembar derivasi SVD | Umpan balik tertulis |
| 10 | Notebook NumPy PCA | Umpan balik atas kode & interpretasi |
| 11 | Draf formulasi model proyek | Checklist konsultasi |
| 13 | Checklist revisi proyek | Umpan balik konsultasi |
| 14 | Review & peta konsep terpadu | Umpan balik pleno |
| 15 | Presentasi final | Rubrik presentasi (formatif) |

---

## 5. MATRIKS BOBOT CPMK

| CPMK | Tugas 1 (20%) | UTS (30%) | Tugas 2 (20%) | UAS (30%) | Total Bobot dalam CPMK |
|:---:|:---:|:---:|:---:|:---:|:---:|
| CPMK-1 | 50% | 50% | — | — | 100% |
| CPMK-2 | 50% | 50% | — | — | 100% |
| CPMK-3 | — | 20% | 30% | 50% | 100% |
| CPMK-4 | — | — | 60% | 40% | 100% |

**Catatan metodologis (wajib dibaca):**

Angka pada tabel di atas adalah **bobot relatif di dalam CPMK** — setiap baris berjumlah 100%. Angka tersebut **bukan** porsi terhadap nilai akhir, sehingga tidak boleh dijumlahkan menurut kolom.

Nilai akhir **tidak** dihitung dari penjumlahan kolom CPMK, melainkan langsung dari bobot instrumen baku pada rumus Bagian 6.1:

$$NA = 0{,}20\,T_1 + 0{,}30\,UTS + 0{,}20\,T_2 + 0{,}30\,UAS$$

Dengan pemisahan ini, satu instrumen boleh mengukur lebih dari satu CPMK tanpa menimbulkan penghitungan ganda (*double counting*).

---

## 6. FORMULA PENILAIAN

### 6.1 Nilai Akhir Mata Kuliah

$$NA = (0{,}20 \times T_1) + (0{,}30 \times UTS) + (0{,}20 \times T_2) + (0{,}30 \times UAS)$$
dengan $T_1$, $UTS$, $T_2$, $UAS$ ∈ [0, 100].

### 6.2 Ketercapaian CPMK

| CPMK | Formula |
|:---:|---|
| CPMK-1 | $0{,}50 \times T_1 + 0{,}50 \times UTS$ |
| CPMK-2 | $0{,}50 \times T_1 + 0{,}50 \times UTS$ |
| CPMK-3 | $0{,}20 \times UTS + 0{,}30 \times T_2 + 0{,}50 \times UAS$ |
| CPMK-4 | $0{,}60 \times T_2 + 0{,}40 \times UAS$ |

Mahasiswa dinyatakan **tuntas CPMK** apabila skor CPMK ≥ 60. Mahasiswa dengan CPMK < 60 wajib mengikuti asesmen pemulihan pada komponen terkait (Bagian 8.4).

### 6.3 Ketercapaian CPL (kontribusi MK)

MK ini membina **satu** CPL, sehingga kontribusinya bersifat penuh terhadap NA:

$$Attainment_{CPL_{CPL\text{-}05}}(i) = 1{,}00 \times NA_{STI\text{-}205}(i)$$

| CPL | $W_x$ | Kontribusi SKS efektif |
|:---:|:---:|:---:|
| `CPL-05` (`P1`) | 1,00 | 3,00 SKS |

**Ambang:** ketercapaian CPL ≥ 65,0. Target prodi: ≥ 80% mahasiswa mencapai ambang.

> **Catatan pembacaan:** angka di atas adalah kontribusi MK ini terhadap CPL-05 (P1). Ketercapaian CPL-05 (P1) pada tingkat prodi dihitung dengan mengagregasi seluruh MK pembina CPL-05 (P1) (Dokumen 008 Bagian 3.3–3.4) — bukan dengan menjumlahkan nilai mentah antar-MK.

### 6.4 Ketercapaian Kelas (untuk CQI)

$$\bar{X}_{CPMK_j} = \frac{1}{n}\sum_{i=1}^{n} Score_{CPMK_j}(i)$$

Kelas dinyatakan sehat apabila $\bar{X}_{CPMK_j} \ge 70$ untuk seluruh CPMK. Nilai 60–69 memicu tindak lanjut penguatan metode; < 60 memicu revisi instrumen dan/atau materi.

---

## 7. KONVERSI NILAI DAN KELULUSAN

| Nilai Angka | Huruf | Bobot | Predikat | Status |
|:---:|:---:|:---:|---|:---:|
| 86–100 | A | 4,00 | Sangat Baik | Lulus |
| 76–85 | B+ | 3,50 | Baik Sekali | Lulus |
| 70–75 | B | 3,00 | Baik | Lulus |
| 66–69 | C+ | 2,50 | Cukup Baik | Lulus |
| 60–65 | C | 2,00 | Cukup | **Lulus (batas minimum)** |
| 56–59 | D | 1,00 | Kurang | Tidak lulus |
| 0–55 | E | 0,00 | Sangat Kurang | Tidak lulus |

**Syarat kelulusan:** (1) nilai akhir ≥ 60; (2) kehadiran ≥ 75% (12 dari 16 pertemuan); (3) seluruh tugas sumatif dikumpulkan. Kekurangan salah satu syarat menyebabkan nilai maksimum D.

---

## 8. MEKANISME PELAKSANAAN

### 8.1 Pengumuman dan Transparansi
- Bobot, rubrik, dan tenggat diumumkan pada pekan 1 dan dipasang permanen di LMS.
- Naskah soal dan kunci dibuka untuk mahasiswa setelah asesmen selesai.

### 8.2 Pengumpulan
- Semua pengumpulan melalui LMS dengan cap waktu otomatis.
- Format berkas: PDF (lembar kerja/laporan), IPYNB (notebook), PPTX/PDF (slide), PNG/SVG (grafik).
- Penamaan berkas: `STI205_<NIM>_<Komponen>_<Pekan>.pdf` dan `STI205_<Kelompok>_T2.ipynb`.

### 8.3 Keterlambatan

| Keterlambatan | Sanksi |
|:---:|---|
| ≤ 24 jam | −10% dari skor komponen |
| 25–72 jam | −25% dari skor komponen |
| > 72 jam | Tidak diterima, kecuali dengan bukti *force majeure* yang disetujui dosen |

### 8.4 Remedial dan Asesmen Pemulihan
- Remedial diberikan bagi mahasiswa dengan NA 56–59 atau CPMK < 60.
- Bentuk: ujian pemulihan tertulis setara + revisi bagian laporan/kode yang belum tuntas.
- Batas maksimum nilai setelah remedial: **C (65)**.
- Remedial dilaksanakan paling lambat 2 pekan setelah pengumuman nilai.

### 8.5 Ujian Susulan
- Diberikan hanya untuk kondisi medis darurat, kedukaan, atau penugasan resmi universitas, dengan bukti dokumen.
- Diajukan maksimal 3 hari kerja setelah jadwal asesmen.

### 8.6 Moderasi Nilai Antar-Kelas
- Dilakukan jika terdapat lebih dari satu kelas paralel.
- Prosedur: penyamaan bobot, peninjauan sebaran nilai, penyesuaian maksimal ±5 poin dengan persetujuan Koordinator RMK.

### 8.7 Ketentuan Khusus Asesmen Komputasi Aljabar

- Skor diberikan **per langkah** OBE, determinan, invers, eigen, atau derivasi SVD — bukan hanya hasil akhir.
- Hasil akhir benar tanpa langkah komputasi dinilai maksimal 40% poin butir.
- Satu baris OBE yang salah menggugurkan skor baris itu **dan** seluruh baris turunannya, tetapi tidak menghapus skor baris sebelumnya yang benar.
- Pada CPMK-4, hasil NumPy **wajib** disertai verifikasi manual pada minimal satu sampel (mis. matriks 2×2). Tanpa verifikasi, skor dimensi implementasi maksimal 50%.
- Kalkulator ilmiah diperbolehkan pada Tugas 1 & Tugas 2 untuk verifikasi aritmetika, **tidak** pada UTS/UAS dan tidak untuk menggantikan OBE.
- Pustaka *machine learning* tingkat tinggi (scikit-learn, tensorflow, pytorch) **dilarang** pada Tugas 2; pelanggaran menggugurkan skor dimensi implementasi.
- Notasi matriks wajib konsisten ($A^T$, $A^{-1}$, $\lambda$, $\sigma$); notasi non-standar tanpa definisi mengurangi skor dimensi kerapian.

---

## 9. INTEGRITAS AKADEMIK

1. Setiap tugas menyertakan **Deklarasi Transparansi AI** (bagian mana dibantu AI, alat apa, prompt ringkas).
2. Dosen berhak melakukan **verifikasi lisan 3 menit** atas karya yang dikumpulkan — termasuk meminta mahasiswa menjalankan ulang satu langkah OBE atau menjelaskan satu baris kode NumPy.
3. Indikasi plagiarisme diproses sesuai Peraturan Akademik Universitas; sanksi minimal nilai 0 pada komponen terkait.
4. Pencegahan plagiarisme: pemeriksaan kemiripan (ambang ≤ 25% setelah kutipan dikecualikan).
5. Kerja sama antar-kelompok diperbolehkan pada diskusi, tetapi laporan dan kode wajib orisinal per kelompok.
6. **Kasus khusus kode:** menyalin potongan kode dari dokumentasi resmi NumPy diperbolehkan **hanya** bila disitasi; menyalin tanpa sitasi dianggap plagiarisme.

---

## 10. EVALUASI PELAKSANAAN PEMBELAJARAN (CQI/PPEPP)

### 10.1 Indikator dan Target

| No | Indikator | Target | Alat Ukur | Frekuensi |
|:--:|---|---|---|---|
| 1 | Rata-rata ketercapaian CPMK | ≥ 70 | Rekap nilai LMS | Per semester |
| 2 | Persentase mahasiswa tuntas CPL-05 (P1) (≥ 65,0) | ≥ 80% | Formula 6.3 | Per semester |
| 3 | Ketepatan pelaksanaan 4 titik asesmen | 100% sesuai jadwal | Lembar monitoring SAP | Per semester |
| 4 | Ketepatan umpan balik (≤ 7 hari) | ≥ 90% komponen | Log LMS | Per semester |
| 5 | Tingkat kepuasan mahasiswa terhadap asesmen | ≥ 4,0/5,0 | Kuesioner anonim | Per semester |
| 6 | Persentase bobot asesmen kinerja (IKU 7) | ≥ 50% | Dokumen RPS | Tahunan |
| 7 | Tingkat plagiarisme/kemiripan | ≤ 25% | Laporan similarity | Per tugas |
| 8 | Proporsi mahasiswa remedial | ≤ 20% | Rekap nilai | Per semester |
| 9 | Keterjalanan seluruh notebook NumPy | 100% tanpa galat | Uji eksekusi | Per semester |

### 10.2 Siklus PPEPP

| Tahap | Aktivitas | Bukti |
|---|---|---|
| **P**erencanaan | Penetapan RPS, SAP, kisi-kisi, rubrik sebelum semester | Dokumen 055_1–055_5 |
| **P**elaksanaan | Pengajaran & asesmen sesuai SAP | Jurnal perkuliahan, log LMS, log eksekusi notebook |
| **E**valuasi | Analisis butir, rekap CPMK, kuesioner mahasiswa | Laporan evaluasi semester |
| **P**engendalian | Rapat evaluasi RMK; verifikasi UPM | Berita acara |
| **P**eningkatan | Revisi metode/instrumen untuk semester berikutnya | Dokumen revisi RPS versi baru |

### 10.3 Rencana Tindak Lanjut

| Temuan | Ambang Pemicu | Tindakan |
|---|---|---|
| CPMK tertentu rendah | Rata-rata < 65 | Penguatan materi & latihan tambahan; revisi butir soal |
| Kesalahan berulang pada satu topik (mis. klasifikasi solusi SPL, tanda kofaktor) | > 40% mahasiswa keliru pada langkah yang sama | Sesi tutorial khusus; penambahan contoh bertahap di modul |
| Mahasiswa mampu memakai NumPy tetapi tidak mampu menjelaskan matematikanya | > 30% pada verifikasi lisan | Penambahan latihan verifikasi manual wajib; pengurangan bobot komponen kode murni |
| Banyak mahasiswa remedial | > 20% kelas | Analisis kesulitan belajar; sesi tutorial tambahan |
| Umpan balik terlambat | > 10% komponen | Perbaikan alur kerja penilaian; penugasan asisten |
| Kemiripan tinggi | > 25% pada satu tugas | Penggantian kasus/angka; pengetatan verifikasi lisan |
| Kepuasan rendah | < 3,5/5,0 | Revisi metode dan beban tugas |

---

## 11. KEPATUHAN IKU 7

| Kriteria | Ketentuan | Kondisi MK Ini |
|---|---|---|
| Bobot asesmen berbasis partisipasi/kasus/proyek | ≥ 50% | **52,5%** (Tugas 1 20% + Tugas 2 20% + Bagian IV UAS 12,5%) |
| Keterlibatan mahasiswa dalam asesmen | Ada | Presentasi proyek, presentasi antara, revisi berbasis umpan balik |
| Asesmen autentik | Ada | Jaringan pipa, reduksi indikator akademik, kompresi citra |
| Umpan balik formatif | Ada | 12 aktivitas formatif non-graded |

---

## 12. PELAPORAN DAN ARSIP

| Berkas | Isi | Penyimpanan | Retensi |
|---|---|---|---|
| Lembar nilai akhir | NIM, T1, UTS, T2, UAS, NA, grade | SIAKAD + arsip prodi | 5 tahun |
| Rekap CPMK | Skor CPMK per mahasiswa | Arsip RMK | 5 tahun |
| Rekap CPL | Ketercapaian CPL-05 (P1) per mahasiswa | Arsip RMK | 5 tahun |
| Laporan evaluasi semester | Analisis butir, CQI, tindak lanjut | Arsip UPM | 5 tahun |
| Naskah & rubrik terisi | Bukti asesmen | LMS/arsip digital | 2 tahun |
| Notebook proyek | Artefak kode + *output* | Repositori RMK | 2 tahun |
| Berita acara ujian | Kehadiran, kejadian khusus | Arsip prodi | 5 tahun |
| Lembar verifikasi kunci | Cek ulang kunci jawaban oleh penelaah kedua | Arsip RMK | 5 tahun |

---

## 13. LAMPIRAN — FORMAT LEMBAR NILAI

```
================================================================================
LEMBAR NILAI AKHIR — STI-205 ALJABAR LINEAR DAN MATRIKS
Semester: 2 / Kelas: ____ / Tahun Akademik: ____ / Dosen: ________________
--------------------------------------------------------------------------------
No | NIM | Nama | T1 (20) | UTS (30) | T2 (20) | UAS (30) | NA | Huruf | Status
--------------------------------------------------------------------------------
 1 |     |      |         |          |         |          |    |       |
 2 |     |      |         |          |         |          |    |       |
...|     |      |         |          |         |          |    |       |
--------------------------------------------------------------------------------
Rata-rata CPMK-1: ____ | CPMK-2: ____ | CPMK-3: ____ | CPMK-4: ____
Ketercapaian CPL-05 (P1): ____
Kehadiran rata-rata: ____% | Jumlah remedial: ____ | Jumlah tidak lulus: ____
================================================================================
```

---

*Dokumen ini konsisten dengan skema 4 titik asesmen Dokumen 008 dan rubrik Dokumen 018. Bukti pelaksanaan asesmen diarsipkan sesuai Bagian 12.*
