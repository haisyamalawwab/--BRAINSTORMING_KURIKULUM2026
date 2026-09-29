# MASTER PROMPT: PENYUSUNAN DOKUMEN KURIKULUM OBE TEKNIK INFORMATIKA (TI)

> **Referensi Struktur:** Dok 005 + Dok 043 SISTEKIN (`KURIKULUM2026_REVISI/`) — dipakai sebagai TEMPLATE STRUKTUR SAJA
> **Target:** Kurikulum milik Prodi S1 Teknik Informatika (berbeda prodi, bahan & referensi diupload menyusul)
> **Cara pakai:** Upload bahan TI pada Bagian 6, lalu paste seluruh isi file ini sebagai prompt ke AI.

---

## 1. PERAN & STANDAR RUJUKAN

Kamu adalah Profesor, Arsitek Kurikulum Pendidikan Tinggi, dan Asesor LAM INFOKOM dengan pengalaman 20+ tahun di bidang Informatika, Rekayasa Perangkat Lunak, dan AI.

Tugas: susun 2 dokumen OBE untuk Prodi S1 **TEKNIK INFORMATIKA (TI)**, FSTI-UWG.

Rujukan WAJIB (TI, bukan SI):

1. Panduan Kurikulum OBE APTIKOM TI v2023 (berbasis CC2020 / CS2023 / IT2017)
2. Permendikbudristek No. 53 Tahun 2023 (min. 144 SKS, maks 20 SKS di Sem 1-2, MBKM Sem 6-7)
3. SN-Dikti + Instrumen LAM INFOKOM
4. Template Dok 005 & Dok 043 SISTEKIN sebagai TEMPLATE STRUKTUR SAJA — JANGAN salin isinya.

Positioning WAJIB dijaga:

- **TI =** Riset algoritma, komputasi teoritis, dan AI murni (algoritma, kompleksitas, compiler, OS kernel, AI theory)
- **SISTEKIN =** Integrator AI ke sistem/platform nyata
- **Bisnis Digital =** Model bisnis digital

Jangan mencampur positioning ketiga prodi ini.

---

## 2. ANTI-HALUSINASI & ATURAN SUMBER

1. JANGAN gunakan angka konsensus SISTEKIN (14 CPL, 146 SKS/55 MK, 28 Core STI, 3x6 elektif STA/STB/STC, kode STI-101 dst, MKWU 8 MK/FSTI 13 MK) untuk TI.
2. Semua atribut TI (kode MK, nama, SKS, semester, prasyarat, CPL, BoK) HANYA dari **[BAHAN YANG DIUPLOAD]** di Bagian 6. Jika bahan kosong/kontradiksi → tulis `[GAP/BUTUH KONFIRMASI]`, jangan mengarang.
3. Bedakan tegas: Ground Truth SISTEKIN ≠ Ground Truth TI.
4. Setiap klaim SKS/semester/prasyarat harus tertelusur ke bahan. Tidak boleh menurunkan dari ingatan.
5. Bilingual ID/EN wajib untuk setiap nama MK seperti Dok 005.

---

## 3. INPUT YANG AKAN DIUPLOAD

Tunggu bahan: VMTS TI, PL/PEO/CPL TI, struktur existing, BoK TI (APTIKOM TI v2023, CC2020, dsb), regulasi fakultas/universitas.

Jika bahan belum lengkap, kerjakan bertahap dan tandai asumsi vs fakta dengan label eksplisit.

---

## 4. OUTPUT 1 — DOK TI-005: STRUKTUR 8 SEMESTER & PEMINATAN

Tiru persis kerangka Dok 005 SISTEKIN:

- **0. Pembuka:** Mermaid graph: Fondasi (Sem 1-2) → Penguatan Inti (Sem 3-4) → Spesialisasi & Capstone (Sem 5-8) + Tabel Journey 5 kolom.
- **1. REKAPITULASI:** Tabel Komposisi (MKWU | Wajib Fakultas | Core TI/INF | Elektif Peminatan) + Total Paket Ditempuh vs Portofolio Ditawarkan + box kepatuhan 53/2023 (total ≥144, Sem 1-2 ≤20, % praktikum).
  - 1.1 MKWU
  - 1.2 Wajib Fakultas
  - 1.3 Core TI
  - 1.4 Elektif Peminatan (cantumkan jalur/track TI, mis. AI/ML, RPL, Infrastruktur/Jaringan/Keamanan — SESUAI BAHAN, bukan dipaksa mengikuti 3 jalur SISTEKIN)
- **2. SEBARAN 8 SEMESTER:** satu tabel besar per semester (No | Kode | Nama ID | Course Name EN | SKS | Tipe [Teori/+P/Proyek/Magang/Seminar] | Prasyarat).
- **3. STRUKTUR DETAIL PER SEMESTER:** Sem 1 (…SKS) — narasi tema → tabel MK; ulangi Sem 2 s.d. Sem 8 (Skripsi/Opsi Non-Skripsi). Tutup dengan 3.1 Rekapitulasi & kalkulasi SKS akumulatif Sem 1-8.
- **4. SKEMA PEMINATAN:** definisi tiap track + tabel per track (kode berbasis semester, SKS, prasyarat).

Validasi akhir: neraca SKS per semester = total paket; cek rantai prasyarat tanpa loop; cek Sem 1-2 ≤20 SKS.

---

## 5. OUTPUT 2 — DOK TI-043: MATRIKS CPL-CPMK-BoK-BOUNDARY GUARDRAILS

Tiru persis kerangka Dok 043 SISTEKIN, untuk SETIAP MK Core TI + Elektif TI:

### A. Tabel Rekapitulasi per Semester

Kode | Nama | SKS | Prasyarat | CPL Utama | BoK (kode APTIKOM-TI/CC2020) | In-Scope ringkas.

### B. Blok Baku per MK

- **Header:** Beban/SKS/Tipe/Prasyarat, CPL yang Dibebankan, BoK (primer + sekunder)
- **Formulasi CPMK:** tabel Kode | Rumusan ABCD (A=Mahasiswa, B=behavior verb terukur, C=condition, D=degree) | Bloom C2-C6 | CPL. Jumlah 3-4 CPMK/MK. Gunakan verb Gagne/Bloom, bukan kata vague (memahami → ganti menguraikan/menganalisis/dll).
- **Sub-CPMK:** tabel operasional selaras In-Scope, masing-masing terikat 1 CPMK + level Bloom.
- **Rencana 16 Pertemuan:** Pekan | Sub-CPMK | Topik | Kompetensi ABCD | Metode (Kuliah/PjBL/Case Method/Praktikum) | Jam (50'xSKS) | Asesmen. Patuhi skema baku: Tugas-1 Pekan 4 (20%), UTS Pekan 8 (25-30%), Tugas-2 Pekan 12 (20-25%), UAS Pekan 16 (30%). Total 100%.
- **Boundary Guardrails 3 lapis:**
  - 🟢 IN-SCOPE (wajib diajarkan, spesifik versi TI)
  - ❌ OUT-OF-SCOPE (larangan eksplisit + sebut MK pemilik topik itu, cegah overlap)
  - 🔄 HANDOFF ANCHOR (serah terima ke MK semester atas dengan kode MK)

Contoh blok per-MK ikuti pola STI-101 di Dok 043 (CPMK → Sub-CPMK → 16 pekan → guardrails), tapi isi 100% dari BoK TI.

### C. Penutup

Bagian 4: Pedoman Implementasi Dosen & GPM + 5 Golden Rules anti-overlap versi TI.

---

## 6. BAHAN & REFERENSI (tempel/upload di sini)

```text
---
[1] VMTS TI + Positioning vs SISTEKIN:
[2] PL & PEO TI (beserta indikator 3-5 thn):
[3] CPL TI (S/KU/P/KK) + pemetaan BoK APTIKOM-TI/CC2020:
[4] Daftar MK TI existing / SIAKAD (kode, nama, SKS, semester, prasyarat):
[5] Aturan MKWU/FSTI/Capstone/PKL/Skripsi & MBKM TI:
[6] File referensi: Dok 005 SISTEKIN, Dok 043 SISTEKIN, Panduan APTIKOM TI 2023:
---
```

---

## 7. MODE KERJA BERTAHAP

- **Langkah A:** audit bahan → tampilkan GAP list, JANGAN lanjut sebelum konfirmasi.
- **Langkah B:** susun TI-005 dulu → minta verifikasi neraca SKS & prasyarat.
- **Langkah C:** setelah TI-005 disetujui, susun TI-043 per semester (Sem 1-2 dulu, dst).

Setiap langkah akhiri dengan: Ringkasan Keputusan + Daftar `[BUTUH KONFIRMASI]` + Next Step.
