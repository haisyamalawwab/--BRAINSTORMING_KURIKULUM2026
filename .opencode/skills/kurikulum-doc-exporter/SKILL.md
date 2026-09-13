---
name: kurikulum-doc-exporter
description: Use when exporting or converting curriculum Markdown to Excel, DOCX, HTML, PDF via _tools scripts or GENERATE bat triggers in KURIKULUM2026_REVISI.
---

# Kurikulum Doc Exporter

Eksportir dokumen kurikulum SISTEKIN dari sumber Markdown ke format diseminasi.

## When to use
- User menyebut: export Excel, buat DOCX, generate HTML, portal index.html, buat PDF, konversi tabel, `GENERATE_`, `START_LIVE_WATCHER`, `export_024_awam`.
- Setelah .md sumber berubah dan output .xlsx/.docx/.html perlu regenerate.
- ONLY untuk konversi. Jangan ubah konten akademik saat export — perbaiki di .md sumber.

## Tool map (workdir: KURIKULUM2026_REVISI)
- `python _tools/convert_md_to_html.py` — seluruh .md ke HTML + portal. Trigger: `GENERATE_HTML.bat`.
- `python _tools/export_all_to_excel.py` — multi-sheet workbook. Trigger: `GENERATE_EXCEL_011.bat`.
- `python _tools/export_024_awam.py` — Dok 024 ke XLSX 8-sheet + DOCX 9-tabel untuk awam.
- `python _tools/convert_md_to_docx.py`, `convert_html_to_pdf.py` — DOCX/PDF per dokumen.
- `python _tools/watch_and_auto_export.py` — live watcher. Trigger: `START_LIVE_WATCHER.bat`.
- Output terstruktur: `HTML/`, `PDF/`, `DOCX/`, `EXCEL/` + file root `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.*`.

## Workflow
1. Verifikasi parent dir dengan `Test-Path -LiteralPath` sebelum buat file baru.
2. Identifikasi sumber .md dan target format. Baca header tabel sumber.
3. Jalankan skrip via bash dengan workdir tepat, bukan `cd` di dalam command.
4. Cek hasil: file ada, sheet/tabel lengkap, header beku/filter (XLSX), lanskap (DOCX awam).
5. Jika gagal, laporkan traceback + file sumber:line, jangan edit output manual.

## Constraints
- Sumber kebenaran = .md. Output .xlsx/.docx/.html/.pdf adalah turunan.
- Jangan commit file biner besar tanpa diminta. Jangan ubah skrip `_tools/` tanpa persetujuan.
- Setelah selesai, ingatkan user restart/watcher jika perlu karena file baru.

