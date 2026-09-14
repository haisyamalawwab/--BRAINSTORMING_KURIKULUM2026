# 048 — KEPUTUSAN PENGGANTIAN STA-601: COMPUTATIONAL METHODS & NUMERICS → REKAYASA BIG DATA DAN KOMPUTASI TERDISTRIBUSI
## Program Studi Sistem dan Teknologi Informasi (S1) — FSTI Universitas Widyagama Malang

### Informasi Dokumen
* **Nomor:** 048/KUR-SISTEKIN/2026
* **Status:** Definitif — menggantikan status Dok 030 (diarsipkan), mengeksekusi Rekomendasi 1 Dok 047
* **Rujukan bukti:** Dok 005:147,283,341,352; Dok 004:147,217,225; Dok 007:2108-2147; Dok 043:1212-1214,1880-1933; Dok 009D (KK2 PySpark); Dok 024:127,392,404,428,513; Dok 025:66,68; Dok 030 (arsip); Dok 047:170,289-317

### 1. Keputusan
1. `STA-601` (3 SKS +P, Sem 6, P1) diganti dari **Computational Methods and Numerics** menjadi **Rekayasa Big Data dan Komputasi Terdistribusi** (*Big Data Engineering & Distributed Systems*).
2. Atribut baku baru: prasyarat `FST-207` + `STI-415`; CPL `P2` + `KK2`; BoK `BK-IS02` (+ `BK-IS18` sekunder Spark MLlib); stack Spark/PySpark, Kafka, Delta Lake/Parquet, S3/MinIO, Spark SQL/MLlib; proporsi 70% engineering + 30% analytical integration (Dok 047:265-274).
3. SKS/semester/tipe tidak berubah: tetap 3 SKS +P Sem 6. Neraca paket 146 SKS / 55 MK dan portofolio 182 SKS / 67 MK tidak berubah.
4. Dok 030 diarsipkan (superseded). Materi numerik klasik tidak diwajibkan di Core (Dok 047:60-61, sah APTIKOM SI v2.0 & TI 2023).
5. Riset Operasi tidak dibuang; masuk pool usulan 2027 sebagai `STA-603` (Dok 047 Rekomendasi 3; Dok 025 direvisi).

### 2. Konsekuensi ekivalensi (Dok 024)
* `STI-317` (2 SKS) E2 → **E5** (tanpa padanan, kredit bebas). Alasan: overlap <10%, tidak memenuhi ambang E2 60-85%.
* Neraca K2025: E1 34 / E2 10 / E3 8 / E4 1 / E5 3 = 56 MK / 146 SKS (tetap Zero Orphan).
* Portofolio: 48 direkognisi (126 SKS) + 19 baru (56 SKS) = 67 MK / 182 SKS.
* Simulasi lulusan penuh: **P2 = 120 SKS; P1/P3 = 117 SKS** (P1 turun 3 SKS karena `STA-601` menjadi wajib tempuh).

### 3. Penyelarasan dieksekusi
* 004 (CPL P2/KK2, BK-IS02 +6 MK, BK-IS10 4 MK, KK1 30/KK2 21 SKS), 005 (nama+prasyarat+BoK), 007 + BUKU_FINAL §49 (4 CPMK ABCD C3-C6 + 16 pertemuan 4x asesmen 20/25/25/30), 043 utama + varian Per-Semester (CPMK/Sub-CPMK/guardrails + handoff `STI-520` → `STA-601`), 037 (baris STA + baseline), 011 (P2+KK2), 012 (tree+prasyarat), 025 (`STA-601` eksis + `STA-603` OR), 042, 044, 045 (nama+edge `STI-415`→`STA-601`), 024 (di atas), 030 (arsip).
* Berkas `*-BACKUP.md` tidak diubah (arsip).

### 4. Verifikasi
* Wajib lolos: `python _tools/verify_all_mk_aligned_with_005.py` dan `verify_zero_discrepancy.py`; `verify_k2025_ground_truth.py` perlu penyesuaian ekspektasi E2/E5 bila skrip mengunci angka lama — bila gagal, laporkan sebagai perbedaan keputusan (bukan galat SIAKAD).
* Klaim di atas hanya sejauh baris yang diubah; tidak mengklaim lulus verifikasi sebelum skrip dijalankan.
