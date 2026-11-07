---
name: perangkat-ajar-generator
description: Use when generating, enriching, or auditing OBE teaching materials (RPS, SAP, Outline Modul, Modul Ajar, Rencana Evaluasi/Asesmen, Rubrik Penilaian, Jobsheet, Slide, Bank Soal) in KURIKULUM2026_REVISI/PERANGKAT_AJAR/.
---

# Perangkat Ajar & Bahan Ajar Generator

Spesialis pembangkitan dan pengayaan paket perangkat ajar OBE Program Studi S1 SISTEKIN FSTI UWG (Kurikulum 2026).

## When to use
- User menyebut: perangkat ajar, bahan ajar, RPS, SAP, outline modul, modul ajar, rencana evaluasi, asesmen, rubrik penilaian, jobsheet praktikum, bank soal, slide kuliah, atau nomor urut `055`–`100`.
- Melanjutkan pembangkitan semester berikutnya (`073_*` dst.) atau memperkaya/mengekspansi berkas yang sudah ada (`055_*`–`072_*`).

## Target Directory Wajib (JANGAN LANGGAR)
- **Satu-satunya folder kerja & output perangkat ajar:** `KURIKULUM2026_REVISI/PERANGKAT_AJAR/`
- **DILARANG** membuat atau menyimpan berkas `055_*` s.d. `100_*` (maupun perangkat ajar/bahan ajar baru lainnya) di root `KURIKULUM2026_REVISI/`.
- Selalu baca `KURIKULUM2026_REVISI/PERANGKAT_AJAR/README.md` terlebih dahulu untuk:
  1. Manifest penomoran baku `<NNN>` (`055` s.d. `100` untuk 46 MK Core STI + Peminatan; `101+` bila memperluas ke FSTI/MKWU).
  2. Status berkas yang sudah tersedia (`055`–`072` = 90 berkas Sem 1–4 sudah berada di `PERANGKAT_AJAR/`).
  3. Konvensi 5 berkas per MK (`_1_RPS`, `_2_SAP`, `_3_OUTLINE_MODUL`, `_4_RENCANA_EVALUASI_ASESMEN`, `_5_RUBRIK_PENILAIAN`) dan ekstensi bahan ajar lanjutan (`_6_MODUL_AJAR`, `_7_JOBSHEET_PRAKTIKUM`, `_8_BANK_SOAL`).

## Ground truth & aturan kepatuhan wajib
1. **Identitas MK (Kode, Nama ID/EN, SKS, Tipe, Semester, Prasyarat):** wajib 100% merujuk `KURIKULUM2026_REVISI/005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md` (termasuk hasil restrukturisasi Sem 6–7 pada Dok 050 & 051: `STI-519` Keamanan Informasi Lanjut di Sem 5 [3 SKS Teori], `STI-624` Pembelajaran Mendalam & Jaringan Saraf di Sem 6 [3 SKS +P], `STI-625` Rekayasa Platform Digital di Sem 6 [3 SKS +P], `STI-726` Integrasi Layanan Cerdas Berbasis AI di Sem 7 [3 SKS +P], `STI-727` Smart City & Pemerintahan Digital di Sem 7 [2 SKS Teori]).
2. **Kode Baku CPL:** gunakan `CPL-01` s.d. `CPL-14` sesuai `003` & `004` Bagian 0.
3. **Silabus, CPMK ABCD, Sub-CPMK & Boundary Guardrails:** rujuk `007`, `037`, dan `043` (*In-Scope, Out-of-Scope, Handoff*).
4. **Estimasi Waktu & Skema 4x Asesmen (= 100%):**
   - Teori (2 SKS: `TM 100', PT 120', BM 120'`; 3 SKS: `TM 150', PT 180', BM 180'`) → **20% / 30% / 20% / 30%** (Tugas 1 / UTS / Tugas 2 / UAS).
   - Praktikum `+P` (2 SKS: `TM 50', Prak 170', PT 60', BM 60'`; 3 SKS: `TM 100', Prak 170', PT 120', BM 120'`) → **20% / 25% / 25% / 30%**.
5. **Path Aset Gambar dari dalam `PERANGKAT_AJAR/`:** gunakan path relatif `../assets/ilustrasi_modul/<nama_file>.png`.

## Verification gate (wajib lulus sebelum selesai)
Jalankan dari folder `KURIKULUM2026_REVISI/`:
- `python3 -B _tools/verify_all_mk_aligned_with_005.py`
- `python3 -B _tools/verify_zero_discrepancy.py`
- `python3 -B _tools/check_all_md_alignment_with_005.py`
