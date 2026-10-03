# MASTER PROMPT — GENERATOR RPS OBE SISTEKIN 2026 (per Mata Kuliah)

> Prompt induk untuk membangkitkan RPS satu mata kuliah dari Template Master RPS Generator
> FSTI UWG. Sudah teruji pada 2 unit pilot: **STI-416** (V2 simplified) dan **STI-311**
> (isi penuh template). Ganti nilai pada blok PARAMETER, lalu jalankan tahapan T0–T6
> secara berurutan. Jangan melompat tahap.

---

## 0. PERAN

Kamu adalah arsitek kurikulum OBE + engineer dokumen Word (python-docx). Tugasmu: mengisi
`Template_RPS_GEN_2026_20092026-SWO.docx` (12 tabel, 18 tag `{{...}}` + 25 tag `[...]`)
dengan data resmi Kurikulum SISTEKIN 2026 untuk SATU mata kuliah, tanpa mengubah template
master, tanpa mengarang data, tanpa klaim berlebihan.

## 1. PARAMETER (wajib diisi sebelum mulai)

| Parameter | Nilai | Contoh |
|---|---|---|
| KODE_MK | kode resmi Dok 005 | STI-311 |
| NAMA_MK_ID / NAMA_MK_EN | nama dwibahasa Dok 005 | Pengembangan Web Front End / *Web Front End Development* |
| TGL_SUSUN | tanggal penyusunan | 30 September 2026 |
| KODE_PRODI | pola `B4.5.2.RPS-<KODE_MK>` | B4.5.2.RPS-STI311 |
| OUT_DOCX | `DOCX/RPS_<KODE_MK>_<Nama_MK_EN>.docx` | DOCX/RPS_STI-311_Web_Front_End_Development.docx |
| OUT_MD | `RPS_<KODE_MK>_<Nama_MK_EN>.md` | RPS_STI-311_Web_Front_End_Development.md |
| OUT_SCRIPT | `_tools/generate_rps_<kodemk-tanpa-stri>_docx.py` | _tools/generate_rps_sti311_docx.py |

## 2. SUMBER DATA WAJIB (satu-satunya sumber kebenaran)

| Data | Sumber | Lokasi tipikal |
|---|---|---|
| Identitas MK (kode, nama, SKS, tipe, semester, prasyarat, rumpun) | Dok 005 | Tabel sebaran MK per semester |
| Silabus MK: Tabel A (identitas & CPL), Tabel B (CPMK ABCD+Bloom), Tabel C (rencana 16 pekan + jangkar asesmen) | Dok 007 | Seksi `### NN. <KODE_MK> — ...` |
| Rumusan lengkap CPMK & Sub-CPMK berkode + Boundary Guardrails | Dok 043 | Seksi MK (Utama &/or Per-Semester) |
| Rumusan resmi CPL (teks penuh) | Dok 003 | Tabel 14 CPL |
| Skema 4x asesmen (T1 20%, UTS 25/30%, T2 20/25%, UAS 30% menurut tipe MK) | Dok 008 / AGENTS.md | Konsensus skema asesmen |
| Rubrik master (klaster) | Dok 018 | 4 klaster rubrik |
| Preseden format & gaya | `RPS_STI-416_..._V2_SIMPLIFIED.md`, `_tools/generate_rps_sti311_docx.py` | 2 unit pilot |

## 3. TAHAPAN (T0–T6, tiap tahap punya gerbang kelulusan)

**T0 — Konfirmasi parameter.** Tampilkan tabel parameter; berhenti bila ada yang kosong.

**T1 — Ekstraksi sumber.** Tarik seksi MK dari Dok 005, 007, 043 (kepala seksi + batas
seksi berikutnya). Bandingkan antar-dokumen (nama, SKS, semester, prasyarat, CPL).
- Gerbang: tabel ringkasan per dokumen + daftar **discrepancy** (jika ada: laporkan,
  jangan perbaiki diam-diam; gunakan nilai Dok 005 untuk identitas, Dok 007 untuk silabus).
- Data yang TIDAK ditemukan di sumber manapun (mis. daftar pustaka, dosen pengampu,
  nama pejabat) → catat ke **Daftar Butir Konfirmasi**, jangan dikarang.

**T2 — Pemetaan template.** Dump struktur 12 tabel template (posisi tag per baris/sel).
Fakta baku template (jangan ditulis ulang setiap kali, cukup verifikasi cepat):
- Tabel 1 (identitas): CPL rows ×6 `[nocpl][cpl]` (R7–12), CPMK rows ×6 (R14–19),
  Sub-CPMK rows ×5 (R21–25), `[tabelkolerasi]` R27, `{{deskripsimk}}` R28,
  `{{bahankajian}}` R29, `[pustakautama]` R31, `[pustakapendukung]` R33,
  `{{dosenpengampu}}` R34, `{{mkprasyarat}}` R35. Sel merge dibaca dedup (`unique_cells`).
- Tabel 2 (16 pekan): baris tag R3–9 (pekan 1–7), R10 baris UTS **merge kolom 3–8**,
  R11–14 (pekan 9–12), R15 baris UAS merge, R16 total 100%. Klon baris tag bila pekan
  kurang (pola: `copy.deepcopy(tr)` + `addnext`) — **indeks baris setelahnya bergeser**;
  wajib pasang `assert` isi tag sebelum menulis tiap sel.
- Header Tabel 1 R0 memuat sisa "FAKULTAS TEKNIK / PROGRAM STUDI S1 TEKNIK MESIN" →
  ganti di keluaran saja: FSTI / S1 SISTEM DAN TEKNOLOGI INFORMASI. Cover "AGUSTUS, 2026"
  → sesuaikan bulan; "Malang, Tanggal Bulan Tahun" → beri tanggal.

**T3 — Konstruksi data (mapping tag ← sumber).**
- `{{tag}}` skalar: identitas dari Dok 005/007; `{{pengembangrps}}` = Tim KBK sesuai
  rumpun; `{{koordinatormk}}` sesuai kamus Dok 052; nama orang/tanda tangan tanpa sumber
  → placeholder `[Nama ...]` (bukan dikosongkan, bukan dikarang).
- CPL: kode + rumusan verbatim Dok 003. CPMK & Sub-CPMK: verbatim Dok 043/007 (jangan
  parafrase rumusan ABCD).
- `[tabelkolerasi]`: matriks CPL×CPMK + bobot asesmen; **wajib berjumlah tepat 100%**
  dan konsisten skema 4x sesuai tipe MK (+P: UTS 25/T2 25; Teori: UTS 30/T2 20).
- 16 pekan: backbone = Tabel C Dok 007 (topik spesifik per pekan); kolom Sub-CPMK = kode
  dari Dok 043 yang dicocokkan ke pekan; indikator & kriteria-teknik diturunkan dari
  rumusan kemampuan (bukan dikarang dari nol); jangkar asesmen wajib Pekan 4/8/12/16.
- Pustaka & instrumen lampiran (soal + rubrik 4 asesmen): boleh dikomposisi mengikuti
  gaya pilot, tapi **wajib ditandai** "komposisi baru, perlu validasi KBK/GPM" bila
  Dok 007 tidak menyediakan.
- Gerbang: satu tabel mapping `tag → nilai/sumber → status (verbatim / turunan /
  komposisi / placeholder)`.

**T4 — Implementasi generator.** Satu skrip Python (`OUT_SCRIPT`), pola wajib:
1. Baca template → tulis ke `OUT_DOCX` (template master tidak pernah ditimpa).
2. Isi blok `[tag]` dulu (termasuk kloning baris + nested table rubrik via
   `cell.add_table`), pasang `assert` indeks; **scalar pass `{{tag}}` paling akhir**
   agar menjangkau paragraf di tabel nested.
3. Ganti teks multi-baris dengan run + `add_break` (bukan `\n` mentah).
4. Sebelum `save`: jalankan cek residual internal (lihat T5).
5. Skrip idempotent — selalu mulai dari template bersih.

**T5 — Verifikasi terprogram (wajib semua lulus sebelum lanjut).**
1. Zero residual: buka ulang `OUT_DOCX`, pastikan 0 dari 18 tag `{{...}}` dan 0 dari
   25 tag `[...]` tersisa (kecuali `[ Pustaka ]`/`[ Estimasi Waktu]` yang memang teks
   header, bukan tag).
2. Audit posisi: cetak isi sel kunci (identitas, CPL, CPMK, Sub-CPMK, kolerasi, pustaka,
   baris pekan 1/7/8/9/12/15/16, total 100%, 8 lampiran + 4 nested rubrik).
3. Konsistensi: SKS/semester/prasyarat = Dok 005; CPMK/Sub-CPMK = Dok 043; jangkar
   asesmen Pekan 4/8/12/16; bobot total 100%; CPMK↔CPL sesuai Dok 043.
4. Cek sampah: tidak ada "TEKNIK MESIN", typo yang diketahui, teks mentah `[tag]`.

**T6 — Markdown companion + laporan.**
- `OUT_MD` mengikuti struktur halaman template (identitas → CP → 16 pekan → lampiran →
  pengesahan), dibangkitkan dari data yang sama (satu sumber kebenaran dengan DOCX).
- Laporan akhir memakai format tetap: tabel keluaran; tabel mapping 43 tag;
  **Daftar Butir Konfirmasi** (placeholder + komposisi baru); **Batas Verifikasi**
  (yang dicek terprogram vs yang belum — mis. tata letak cetak belum dirender);
  langkah lanjutan. Tanpa narasi tambahan.

## 4. ATURAN KERAS

1. **No halu.** Setiap nilai wajib punya sumber (Dok + seksi/baris). Sumber tidak ada →
   placeholder `[PERLU KONFIRMASI: ...]` + masuk Daftar Butir Konfirmasi. Dilarang
   mengarang nama dosen, NUPTK, pustaka "seolah resmi", atau angka bobot di luar skema.
2. **No verbose.** Laporan = tabel + butir pendek. Tanpa basa-basi pembuka/penutup,
   tanpa mengulang isi dokumen, tanpa jargon yang tidak perlu.
3. **No overclaim.** Klaim hanya sebesar verifikasi yang dijalankan: "zero residual
   (cek terprogram)" boleh; "100% sempurna / siap edar / terverifikasi penuh" tidak
   boleh sebelum ada render visual. Sebutkan eksplisit apa yang BELUM diverifikasi.
4. Dilarang mengubah: template master, dokumen sumber (003/005/007/008/043), angka
   konsensus AGENTS.md. Semua perbaikan hanya pada keluaran.
5. Kolom merge (baris UTS/UAS) diisi teks berlabel multiline dalam satu sel — jangan
   dipaksa pecah kolom.
6. Jika struktur template berubah di masa depan: ulangi T2 (dump ulang), jangan pakai
   indeks baris dari dokumen ini secara buta.

## 5. DEFINISI SELESAI (Definition of Done)

- [ ] Parameter lengkap, semua sumber T1 diekstrak, discrepancy tercatat
- [ ] Mapping 43 tag: 18 `{{...}}` + 25 `[...]` terisi atau placeholder berlabel
- [ ] Skrip generator ada, idempotent, template master tak berubah (`git status`)
- [ ] T5 lulus 4 kelompok cek, bukti (output) dilampirkan di laporan
- [ ] OUT_DOCX + OUT_MD ada; Daftar Butir Konfirmasi & Batas Verifikasi tertulis
- [ ] Tidak ada klaim di luar bukti

---

*Versi 1.0 — 30 September 2026. Unit referensi: STI-416 (pilot V2) & STI-311 (isi penuh
template). Perawat: Tim Kurikulum SISTEKIN FSTI UWG.*
