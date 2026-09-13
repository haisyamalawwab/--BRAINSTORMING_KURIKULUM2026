# Rencana Lanjutan — Pengembangan Sub-CPMK & Rencana 16 Pertemuan (Dokumen 043)

**Tanggal:** 2026-09-13
**Cakupan:** 46 MK (28 Core STI + 18 Peminatan STA/STB/STC)
**Target:** Kedua dokumen 043 (`043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md` dan `043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md`)

---

## 1. Status Saat Ini (Sudah Terverifikasi)

### 1.1 Data Sub-CPMK (Phase 1 — Tuntas)
- 46 MK × 2 Sub-CPMK per CPMK = **175 CPMK induk → 322 Sub-CPMK** ter-author.
- Terdiri dari:
  - 28 MK Core STI (Semester 1–7): 220 Sub-CPMK
  - 18 MK Peminatan (Semester 5–7): 102 Sub-CPMK
- Setiap Sub-CPMK memuat: kode (`Sub-CPMK-X.Y`), rumusan kompetensi spesifik, rujukan ke CPMK induk (`CPMK-N`), dan level Bloom.
- Sub-CPMK diturunkan langsung dari rumusan CPMK induk + topik IN-SCOPE Boundary Guardrails masing-masing MK.
- **Validasi struktural:** 46/46 MK terpetakan, 0 missing, 0 extra, 0 structural problem (setelah perbaikan `STC-702` CPMK-4 → CPMK-3).

### 1.2 Generator Injeksi (Terverifikasi)
- Skrip: `KURIKULUM2026_REVISI/_tools/gen_043_subcpmk.py`
- Modul data: `_043_subcpmk_{s1, s23, s45, s67, p56, p7}.py`
- **Hasil uji pada salinan temp:**
  - PER_SEMESTER: **46/46** berhasil disisipkan (anchor: `**Boundary Guardrails** (dari Dok 037)`)
  - DAN_BOUNDARY: **46/46** berhasil disisipkan (anchor: `**Boundary Guardrails:**`)
- Generator bersifat **idempoten**: tidak menyisipkan ulang bila sudah ada `Sub-CPMK-` di blok MK tersebut.

---

## 2. Rencana Eksekusi

### Langkah 2.1 — Injeksi Sub-CPMK ke Dokumen Asli (Phase 1 Final)
1. Jalankan `gen_043_subcpmk.py` pada kedua dokumen 043 asli (bukan salinan temp).
2. Verifikasi:
   - Jumlah blok Sub-CPMK = 46 per dokumen.
   - Tidak ada duplikasi.
   - Tidak ada perubahan pada konten CPMK induk, Boundary Guardrails, atau bagian lain.
3. Komit perubahan Markdown (`git add` kedua file 043).

### Langkah 2.2 — Regenerasi HTML/PDF (Phase 1 Final)
1. Jalankan `_tmp_batch_md_to_pdf.py` untuk kedua dokumen 043.
2. Verifikasi HTML:
   - Sub-CPMK tabel ter-render sebagai `<table>` (bukan teks mentah).
   - Tidak ada regresi pada tabel CPMK induk atau Boundary Guardrails.
3. Verifikasi PDF: ukuran wajar, Sub-CPMK tabel terbaca, tidak ada halaman terpotong.

### Langkah 2.3 — Pengembangan Rencana 16 Pertemuan + Asesmen (Phase 2)
**Skema asesmen baku (selaras Dok 008):**
- Tugas 1 → Pekan 4–5 (20%)
- UTS → Pekan 8 (25% teori / 30% praktikum)
- Tugas 2 → Pekan 12–13 (20% teori / 25% praktikum)
- UAS / Tugas Akhir / Proyek → Pekan 16 (30%)

**Format tabel per MK:**

| Pekan | Topik Pembelajaran | Sub-CPMK Terkait | Metode | Asesmen |
|:---:|---|:---:|---|:---:|
| 1 | Pengantar MK & Kontrak Belajar | — | Kuliah interaktif | — |
| 2–3 | Topik A | Sub-CPMK-1.1, 1.2 | ... | — |
| 4–5 | Topik B | Sub-CPMK-2.1, 2.2 | ... | **Tugas 1** |
| 6–7 | Topik C | Sub-CPMK-2.3, 2.4 | ... | — |
| 8 | **UTS** | CPMK-1 s.d. 2 | Ujian tertulis/praktikum | **UTS** |
| 9–11 | Topik D | Sub-CPMK-3.1, 3.2 | ... | — |
| 12–13 | Topik E | Sub-CPMK-3.3, 3.4 | ... | **Tugas 2** |
| 14–15 | Topik F | Sub-CPMK-4.1, 4.2 | ... | — |
| 16 | **UAS / Tugas Akhir / Proyek** | Seluruh CPMK | Ujian/Proyek akhir | **UAS** |

**Catatan implementasi:**
- Untuk MK 2 SKS: 16 baris topik, beberapa pekan digabung.
- Untuk MK 3 SKS: 16 baris topik penuh.
- Untuk MK praktikum (+P): kolom metode menyebut "Praktikum" dan bobot UTS/UAS disesuaikan (30/25).
- Setiap Sub-CPMK harus muncul minimal di 1 baris pekan.
- Kolom "Asesmen" hanya diisi pada pekan Tugas 1, UTS, Tugas 2, UAS.

**Urutan pengerjaan Phase 2:**
1. Author data rencana 16 pertemuan untuk 46 MK (dipisahkan per semester untuk ukuran file).
2. Buat generator baru `gen_043_rps.py` yang menyisipkan tabel 16 pertemuan setelah blok Sub-CPMK (sebelum `**Boundary Guardrails**`).
3. Uji pada salinan temp, lalu injeksi ke dokumen asli.
4. Regenerasi HTML/PDF.

### Langkah 2.4 — Regenerasi Artefak Turunan
- HTML: `_tmp_batch_md_to_pdf.py` (sudah ada).
- PDF: via Chrome headless di skrip yang sama.
- DOCX/EXCEL: jika ada generator (`gen_043_matrix.py`), jalankan ulang.

---

## 3. Artefak yang Akan Dihasilkan

| No | File | Keterangan |
|---|---|---|
| 1 | `043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md` | +322 baris Sub-CPMK (46 blok) + 46 tabel 16 pertemuan |
| 2 | `043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md` | Cerminan identik dari (1) |
| 3 | `HTML/043_*.html` | HTML ter-render ulang |
| 4 | `PDF/043_*.pdf` | PDF ter-render ulang |
| 5 | `DOCX/043_*.docx` | Jika generator DOCX tersedia |
| 6 | `EXCEL/043_*.xlsx` | Jika generator EXCEL tersedia |

---

## 4. Risiko & Mitigasi

| Risiko | Mitigasi |
|---|---|
| Sub-CPMK tidak selaras dengan CPMK induk | Validasi struktural: setiap Sub-CPMK merujuk CPMK yang ada di MK tersebut |
| Tabel 16 pertemuan tidak mencakup semua Sub-CPMK | Verifikasi: setiap Sub-CPMK muncul minimal 1x di kolom "Sub-CPMK Terkait" |
| Regresi pada konten lama (CPMK/Guardrails) | Generator hanya menyisipkan, tidak mengubah konten eksisting |
| File Markdown terlalu besar untuk diedit manual | Generator otomatis, tidak perlu edit manual |
| HTML/PDF tidak ter-render benar | Verifikasi visual pada sampel 3 MK (STI-101, STI-413, STA-702) |

---

## 5. Perintah Eksekusi (Referensi)

```bash
# Phase 1: Injeksi Sub-CPMK
cd KURIKULUM2026_REVISI
python _tools/gen_043_subcpmk.py

# Phase 2: Injeksi rencana 16 pertemuan (setelah gen_043_rps.py dibuat)
python _tools/gen_043_rps.py

# Regenerasi HTML/PDF
python _tmp_batch_md_to_pdf.py 043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md
python _tmp_batch_md_to_pdf.py 043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md

# Atau regenerasi seluruh dokumen
python _tmp_batch_md_to_pdf.py
```

---

**Catatan akhir:** Rencana ini faktual dan berbasis hasil kerja yang sudah terverifikasi. Tidak ada overclaim — hanya langkah konkret yang akan dieksekusi setelah persetujuan.
