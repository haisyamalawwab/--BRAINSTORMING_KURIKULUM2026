# SEMESTER 8 — Paket Perangkat Ajar Skripsi / Tugas Akhir

Semester 8 dalam Kurikulum OBE SISTEKIN 2026 terdiri dari **1 MK Mandiri 6 SKS**:

| No | Kode | Nama MK | SKS | Tipe | Prasyarat |
|---|---|---|---|---|---|
| 1 | `FST-714` | Skripsi / Tugas Akhir (*Undergraduate Thesis / Final Project*) | 6 | Mandiri | Lulus `FST-613` Pra-Skripsi, ≥120 SKS |

## Lokasi Berkas Baku (Flat Naming per `PERANGKAT_AJAR/README.md`)

Berkas perangkat ajar disimpan dengan penomoran baku **113** (cadangan 101+ untuk MK FSTI):

- `113_1_RPS_FST-714_SKRIPSI_TUGAS_AKHIR_07112026.md` — RPS lengkap 16 pekan, 14 CPL Mastery, 4 CPMK, 12 Sub-CPMK, matriks korelasi & guardrails
- `113_2_SAP_FST-714_SKRIPSI_TUGAS_AKHIR_07112026.md` — SAP mikro 16 pekan (bimbingan 480' + riset mandiri)
- `113_3_OUTLINE_MODUL_FST-714_SKRIPSI_TUGAS_AKHIR_07112026.md` — Outline buku panduan 13 bab + 8 lampiran template (dataset card → sidang)
- `113_4_RENCANA_EVALUASI_ASESMEN_FST-714_SKRIPSI_TUGAS_AKHIR_07112026.md` — Arsitektur 4 titik baku (20/25/25/30), formula NA & disaggregasi CPL, remedial
- `113_5_RUBRIK_PENILAIAN_FST-714_SKRIPSI_TUGAS_AKHIR_07112026.md` — Rubrik analitik K-4 untuk T1, UTS-Monev, T2, UAS-Sidang + holistik & persepsi

> **Akses cepat:** Berkas berada di `KURIKULUM2026_REVISI/PERANGKAT_AJAR/113_*`. Folder `SEMESTER_8/` ini adalah penanda navigasi; jangan duplikasi berkas.

## 4 Jalur Setara (Dok 009)

1. **J1 Riset Eksperimental** — Naskah Bab 1–5 + kode + statistik
2. **J2 Proyek Industri** — TRL≥6 + surat mitra + HKI
3. **J3 Startup** — MVP + traksi + Lean Canvas
4. **J4 Publikasi** — Artikel SINTA 1/2 atau Scopus Q1–Q4 accepted

Semua jalur dinilai dengan rubrik yang sama (bobot diferensiasi 5% pada UAS).

## Verifikasi

```bash
python3 -B _tools/check_all_md_alignment_with_005.py
python3 -B _tools/verify_zero_discrepancy.py
python3 -B _tools/verify_all_mk_aligned_with_005.py
```
Hasil: **100% Selaras dengan Dok 005** (176/176 berkas).

