---
name: kurikulum-doc-verifier
description: Use when verifying SKS, MK codes, CPL, semester alignment, zero discrepancy, SIAKAD ground truth, or running verify_ scripts in KURIKULUM2026_REVISI.
---

# Kurikulum Doc Verifier

Verifikator keselarasan dokumen kurikulum SISTEKIN vs Dok 005 dan ground truth SIAKAD.

## When to use
- User menyebut: verifikasi, cek selaras, audit, zero discrepancy, sinkronisasi, SKS tidak cocok, kode MK, prasyarat, CPL vs MK, ekivalensi K2025.
- Setelah edit struktur, restrukturisasi kode, atau sebelum finalisasi Buku Kurikulum.
- ONLY untuk verifikasi. Jangan ubah isi akademik saat verifikasi gagal — laporkan dan usulkan perbaikan.

## Ground truth numbers (tolak jika beda tanpa persetujuan)
- 14 CPL, 4 PL, 3 PEO. Paket ditempuh 146 SKS / 55 MK. Portofolio 182 SKS / 67 MK.
- K2025: 56 MK / 146 SKS. Sem 1 max 20 SKS (aktual 19), Sem 2 tepat 20.
- 3 peminatan @ 18 SKS (STA/STB/STC-501, 601-602, 701-703). Skema asesmen 4x titik = 100%.
- Kolisi: STI-102, STI-103, STI-101 beda arti K2025 vs K2026.

## Workflow
1. Tentukan target: Dok `005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md` sebagai acuan SKS/semester/tipe/kode/prasyarat.
2. Jalankan verifikator via bash dari workdir `KURIKULUM2026_REVISI`:
   - `python _tools/verify_k2025_ground_truth.py` — 11 kelompok uji / 17 butir vs PDF SIAKAD.
   - `python _tools/verify_all_mk_aligned_with_005.py` — 67 MK: SKS, semester, tipe, kode, prasyarat.
   - `python _tools/verify_zero_discrepancy.py` — sinkronisasi antar file.
3. Untuk klaim ekivalensi Dok 024, cek kategori E1-E5 dan neraca 146 SKS. Simulasi P1/P2=120, P3=117 SKS.
4. Laporkan: PASS/FAIL per butir, file:line penyebab, dan aksi perbaikan minimal.

## Output format
- Tabel hasil: Check | Expected | Actual | Status.
- Daftar diskrepansi dengan path `file_path:line_number`.
- Kesimpulan: lulus/gagal + langkah repair konkret. Jangan klaim lulus jika satu butir gagal.

## Constraints
- Selalu baca file aktual dengan Read/Grep. Jangan verifikasi dari ingatan.
- Jangan edit file .xlsx/.docx manual — perbaiki sumber .md lalu regenerate.

