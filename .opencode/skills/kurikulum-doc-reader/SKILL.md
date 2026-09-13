---
name: kurikulum-doc-reader
description: Use when reading PDF, Markdown, Excel, DOCX curriculum docs, SIAKAD reports, APTIKOM guides, or extracting VMTS CPL MK tables without hallucination.
---

# Kurikulum Doc Reader

Spesialis baca dan ekstraksi dokumen kurikulum SISTEKIN (PDF, Markdown, XLSX, DOCX). Migrasi resmi dari `.document-reader-agent-skills.md` ke format OpenCode.

## When to use
- User menyebut: baca PDF, ekstrak tabel, ringkas dokumen, `Laporan Daftar Kurikulum Prodi Sistekin.pdf`, `Modul OBE`, `APTIKOM`, `SIAKAD`, `VMTS`, `CPL`, `BoK`.
- Perlu data bersih untuk Strategic Analyst, OBE Designer, Curriculum Architect, QA Evaluator.
- ONLY untuk ekstraksi dan analisis. Jangan desain CPL/MK baru di skill ini.

## Ground truth (wajib)
- `AGENTS.md` adalah memory/soul proyek. Patuhi angka konsensus: 14 CPL (S1, KU1-3, P1-4, KK1-6), 4 PL, 3 PEO, paket ditempuh 146 SKS / 55 MK, portofolio 182 SKS / 67 MK.
- K2025: HANYA dari `KURIKULUM2025/Laporan Daftar Kurikulum Prodi Sistekin.pdf` — 56 MK / 146 SKS, sebaran 18-18-20-20-21-21-20-8, semua Wajib, nilai min C. Jangan turunkan dari ingatan atau notulensi.
- K2026: `KURIKULUM2026_REVISI/` adalah single source of truth. Kolisi kode: STI-102, STI-103, STI-101 — selalu sebut tahun kurikulum.
- Baca file dengan tool Read. Untuk PDF gunakan Read (mendukung PDF). Untuk tabel besar gunakan Grep/Glob dulu, jangan tebak.

## Workflow
1. Baca menyeluruh dokumen yang diminta. Identifikasi Bab/halaman/sheet/tabel sumber.
2. Cari keyword relevan dan pahami konteks akademik/birokrasi (Permendikbudristek 53/2023, SN-Dikti, LAM INFOKOM).
3. Ekstrak tabel dengan menjaga relasi baris-kolom. Jangan ubah makna asli.
4. Jika korup/tidak terbaca/tidak mengandung info diminta, nyatakan eksplisit.

## Output format
1. **Executive Summary:** 1-2 paragraf ringkasan terkait instruksi.
2. **Extracted Data:** bullet points, bold untuk penekanan, tabel Markdown.
3. **Data Gap (opsional):** jika tidak ditemukan tulis: "Informasi X tidak ditemukan dalam dokumen ini."

## Constraints
- JANGAN mengarang. Setiap klaim faktual wajib sitasi (contoh: "Berdasarkan Bab 2, hal. 15...").
- JANGAN melompat ke rekomendasi kurikulum. Fokus ekstraksi presisi.

