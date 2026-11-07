# 113_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## FST-714 — SKRIPSI / TUGAS AKHIR (*Undergraduate Thesis / Final Project*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.6.RPS-FST714` · **Klaster Rubrik Master (Dok 018):** Klaster 4 (`K-4`) — Tugas Akhir, Proyek Inovasi & Publikasi  
**CPL:** `CPL-01`–`CPL-14` (14 CPL, Level `M`) · **Jalur:** 4 Opsi Setara (Dok 009) · **Bobot Asesmen:** Tugas 1 (20%) · UTS-Monev (25%) · Tugas 2 (25%) · UAS-Sidang (30%)  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN TUGAS AKHIR SISTEKIN (`K-4`)

Mengacu **Dokumen 018 §5 (Klaster `K-4`)**, penilaian `FST-714` mengedepankan **kebaruan riset (novelty), rigor metodologis, keandalan bukti empiris (fair benchmarking + signifikansi statistik), integritas penulisan ilmiah (Bab 1–5 + artikel IMRAD + Turnitin <20%), kepatuhan etika data (UU PDP, HKI), dan profesionalisme pertahanan sidang (presentasi, demo, QA).** Penilaian bersifat **holistik-komprehensif**: 4 titik asesmen membangun akumulasi bukti ketercapaian 14 CPL pada level *Mastery*.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-05`–`CPL-08` & `CPL-09`–`CPL-14` [C6])

**Objek Penilaian:** Laporan Kemajuan Riset 25% — Dataset Etis + Repo Baseline/Novelty + Log Eksperimen Batch-1 + Draf Bab 4 §1.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Kelengkapan & Etika Dataset**<br>(`Sub-CPMK-1.1` → `CPL-01`) | **25%** | Dataset card lengkap (sumber, distribusi, bias, lisensi), data bersih tanpa missing/error, bukti izin etik/mitra lengkap, anonimisasi UU PDP sempurna. | Dataset card lengkap, data bersih, izin etik ada. | Dataset tersedia namun dokumentasi bias/lisensi kurang. | Dataset tidak bersih (banyak missing/error) atau tanpa izin etik. | Dataset tidak tersedia atau plagiasi data. |
| **2. Keberfungsian & Reproduksibilitas Baseline**<br>(`Sub-CPMK-1.2` → `CPL-09`–`CPL-14`) | **30%** | Repo baseline berjalan reproduksibel (`git clone + install + train → hasil identik`), README lengkap, diagram arsitektur jelas, modular & terdokumentasi. | Repo berjalan & dapat direproduksi dengan sedikit penyesuaian. | Repo berjalan namun dokumentasi kurang (README minim). | Repo tidak berjalan (error env/dependensi) atau tidak ada diagram. | Tidak ada repo atau plagiasi kode. |
| **3. Implementasi Kebaruan & Kualitas Kode**<br>(`Sub-CPMK-1.3` → `CPL-05`–`CPL-08`, `CPL-09`–`CPL-14`) | **30%** | Novelty jelas (pseudocode + kode), bukan ganti nama, kualitas kode tinggi (unit test, komentar, efisien), tuning hyperparam terstruktur. | Novelty terimplementasi dengan baik, kode rapi. | Novelty ada namun penjelasan kurang tajam, kode cukup rapi. | Novelty tidak jelas (klaim kosong) atau kode berantakan. | Tidak ada implementasi novelty. |
| **4. Kelengkapan Log Eksperimen & Kejujuran**<br>(`Sub-CPMK-1.3` → `CPL-02`) | **15%** | Log MLflow/W&B lengkap (≥10 run, param/metric/seed/waktu), tidak cherry-picking, draf Bab 4 §1 informatif. | Log lengkap (≥5 run), jujur, draf Bab 4 ada. | Log tersedia namun kurang lengkap (param/metric tidak konsisten). | Log tidak lengkap atau cherry-picking terbukti. | Tidak ada log eksperimen. |

$$S_{Tugas1} = 0,25(K_1) + 0,30(K_2) + 0,30(K_3) + 0,15(K_4)$$

---

### 2.2 Rubrik Analitik UTS-Monev Kemajuan 50% (Pekan 8 — Bobot 25% MK · Mengukur `CPMK-2` / `CPL-02` & `CPL-09`–`CPL-14` [C5])

**Objek Penilaian:** Monev 50% — Presentasi 10' + QA 15' — Tabel SOTA + Notebook Statistik + Draf Bab 4 ≥50% + Logbook.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Fairness & Kelengkapan Benchmarking SOTA**<br>(`Sub-CPMK-2.1`) | **30%** | ≥2 baseline SOTA mutakhir (3 th terakhir), fair (same split/metric/hardware/seed), bukan strawman, laporan cost (FLOPs/latensi) lengkap. | ≥2 baseline SOTA, fair, cost tercatat. | 1–2 baseline namun pemilihan kurang mutakhir atau fairness kurang. | Hanya 1 baseline usang (strawman) atau fairness dilanggar. | Tidak ada benchmarking. |
| **2. Ketepatan Uji Statistik & Kualitas Visualisasi**<br>(`Sub-CPMK-2.2`) | **30%** | Uji-t/Wilcoxon/McNemar tepat + p <0,05 + IK 95%, visualisasi informatif (label jelas, tidak menyesatkan, color-blind friendly). | Uji statistik tepat, visual informatif, p-value dilaporkan. | Uji statistik ada namun pemilihan kurang tepat atau visual kurang informatif. | Klaim unggul tanpa uji statistik (hanya rerata) atau visual menyesatkan. | Tidak ada analisis statistik/visual. |
| **3. Kedalaman Draf Bab 4 & Koherensi**<br>(`Sub-CPMK-2.3`) | **25%** | Bab 4 ≥50% mengalir logis (setup→hasil→pembahasan kausal→limitasi), koheren dengan Bab 2–3, analisis error case mendalam. | Bab 4 ≥50% mengalir baik, ada pembahasan kausal. | Bab 4 ≥50% namun pembahasan dangkal (hanya lapor angka). | Bab 4 <50% atau tidak koheren dengan Bab 2–3. | Tidak ada draf Bab 4. |
| **4. Kemajuan Jadwal & Disiplin Bimbingan**<br>(`CPL-04` KU3) | **15%** | Kemajuan 50% tercapai tepat waktu, logbook harian lengkap, kartu bimbingan 4x, proaktif. | Kemajuan 50% tercapai, logbook & kartu lengkap. | Kemajuan 40–49%, logbook kurang lengkap. | Kemajuan <40% atau sering mangkir bimbingan. | Tidak hadir monev atau tanpa logbook. |

$$S_{UTSMonev} = 0,30(K_1) + 0,30(K_2) + 0,25(K_3) + 0,15(K_4)$$

**Keputusan Monev:** Skor ≥ 65 (B-) = **Lulus Monev** (lanjut Pekan 9). Skor 50–64 = **Peringatan + Perpanjangan 2 minggu** (remedial, plafon 70). Skor <50 = **Tidak Lulus Monev** (wajib perbaikan menyeluruh, monev ulang).

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 25% MK · Mengukur `CPMK-3` / `CPL-01` & `CPL-03` [C6])

**Objek Penilaian:** Naskah Lengkap Bab 1–5 + Artikel IMRAD + Bukti HKI + Lembar Turnitin <20% + Repo Final.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Kelengkapan & Sintesis Bab 5**<br>(`Sub-CPMK-3.1` → `CPL-03`) | **20%** | Bab 5 menjawab tiap rumusan masalah eksplisit, sintesis 3–5 temuan utama, implikasi teoretis/praktis jelas, saran spesifik & orisinal, matriks keterlacakan lengkap. | Bab 5 menjawab rumusan masalah, sintesis jelas, saran relevan. | Bab 5 menjawab sebagian rumusan masalah, saran kurang spesifik. | Bab 5 tidak menjawab rumusan masalah atau saran klise ("perlu penelitian lebih lanjut" tanpa isi). | Tidak ada Bab 5. |
| **2. Kualitas Artikel IMRAD**<br>(`Sub-CPMK-3.2` → `CPL-03`) | **30%** | Artikel 6–10 hal format IEEE/ACM sempurna, Title spesifik, Abstract 250 kata BG-M-R-C, kontribusi 3 poin jelas, References ≥15 (70% 5th), siap submit (untuk J4: accepted). | Artikel format IMRAD baik, kontribusi jelas, References memadai. | Artikel ada namun format kurang (abstract kurang struktur, sitasi kurang). | Artikel tidak IMRAD atau kontribusi tidak jelas. | Tidak ada artikel. |
| **3. Kelengkapan Berkas HKI**<br>(`Sub-CPMK-3.3` → `CPL-01`) | **15%** | Berkas e-HKCI lengkap (pernyataan, KTP, manual 5–10 hal, cuplikan kode 10–20 hal), judul ciptaan tepat, bukti EC/permohonan terunggah, pembagian hak sesuai kontribusi. | Berkas HKI lengkap, bukti EC ada. | Berkas HKI ada namun manual kurang atau judul kurang tepat. | Berkas HKI tidak lengkap atau salah jenis ciptaan. | Tidak ada HKI. |
| **4. Skor Turnitin & Integritas**<br>(`Sub-CPMK-3.4` → `CPL-01`) | **35%** | Similarity <15% + AI detection <10% + surat orisinalitas + deklarasi AI jujur. Naskah Bab 1–5 80–120 hal, format Panduan Skripsi sempurna (margin 4-3-3-3, TNR 12, spasi 1.5, sitasi IEEE). | Similarity <20% + AI <15%, format baik, surat orisinalitas ada. | Similarity 20–25% (perlu perbaikan minor) atau format kurang. | Similarity 25–30% atau tidak ada surat orisinalitas. | Similarity >30% atau plagiasi terbukti (nilai E). |

$$S_{Tugas2} = 0,20(K_1) + 0,30(K_2) + 0,15(K_3) + 0,35(K_4)$$

---

### 2.4 Rubrik Analitik UAS — Sidang Pendadaran Sarjana (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-01`, `CPL-03`, `CPL-04` [C5])

**Objek Penilaian:** Sidang 150 menit — Presentasi & Live Demo 20' (50% UAS) + Tanya Jawab 40' (50% UAS) oleh 3 penguji.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Kualitas Presentasi & Live Demo**<br>(`Sub-CPMK-4.2` — 50% UAS) | **25%** | Slide 15–20 hal padat visual (6×6), alur IMRAD mengalir, manajemen waktu presisi 20' (bel 15'/19'), demo live lancar (happy path + edge case), video backup siap. | Slide jelas, waktu tepat, demo live berjalan baik. | Slide cukup jelas namun teks padat, waktu 18–22', demo ada lag minor. | Slide penuh teks, waktu <15' atau >25', demo gagal (hanya screenshot). | Tidak presentasi/demo. |
| **2. Penguasaan Metodologi & Kebaruan**<br>(`Sub-CPMK-4.1` — 25% UAS) | **25%** | Menguasai metodologi & novelty mendalam (bisa jelaskan why & how, alternatif desain, trade-off), menjawab "mengapa tidak pakai X?" dengan argumen ilmiah. | Menguasai metodologi & novelty dengan baik. | Menguasai sebagian metodologi, jawaban kurang mendalam. | Tidak menguasai metodologi (bingung jelaskan kodenya sendiri). | Plagiasi metodologi (tidak paham karyanya). |
| **3. Kemampuan Mempertahankan Argumen (QA 40')**<br>(`Sub-CPMK-4.2` — 30% UAS) | **30%** | Menjawab kritis 40' dengan percaya diri, mengakui limitasi jujur + tawarkan solusi, tidak berbohong, argumen koheren, bisa replikasi/generaliasi. | Menjawab kritis dengan baik, mengakui limitasi. | Menjawab cukup, namun argumen kurang tajam atau defensif. | Gagal jawab pertanyaan dasar (apa kontribusi? apa metrik?) atau berbohong. | Tidak bisa jawab QA atau melanggar etika sidang. |
| **4. Sikap Profesional & Kesiapan Yudisium**<br>(`CPL-01` S1, `CPL-04` KU3 — 20% UAS) | **20%** | Sikap profesional (formal, tepat waktu 30' awal, sapa penguji, tidak memotong), etika akademik utuh, berkas yudisium lengkap, revisi siap 2 minggu. | Sikap profesional, berkas lengkap. | Sikap cukup profesional, berkas hampir lengkap. | Terlambat >15' atau pakaian tidak formal atau berkas kurang. | Tidak hadir sidang atau pelanggaran etika berat. |

$$S_{UAS} = 0,25(Presentasi\&Demo) + 0,25(Penguasaan) + 0,30(QA) + 0,20(Sikap)$$

> **Varian Jalur pada Rubrik UAS:**
> - **J1 Riset Eksperimental:** Dimensi 2 diberi penekanan +5% (diambil dari Dimensi 4) — penguasaan eksperimen & statistik menjadi kunci.
> - **J2 Proyek Industri:** Dimensi 1 = 30% (diambil 5% dari Dimensi 2) — bukti TRL≥6 + surat mitra + demo di lingkungan mitra.
> - **J3 Startup:** Dimensi 1 = 30% — bukti traksi (pengguna/MoU/pendapatan) + Lean Canvas + pitch deck.
> - **J4 Publikasi:** Jika artikel sudah *accepted* SINTA 1/2 atau Scopus Q1–Q4 (bukti letter of acceptance), **Dimensi 2 & 3 otomatis ≥ 85** (konversi publikasi, Dok 009 §2.4), mahasiswa hanya verifikasi kontribusi first-author 10 menit.

---

## BAGIAN III — RUBRIK FORMATIF BIMBINGAN MINGGUAN (LOG BOOK 480')

| Kriteria Formatif Bimbingan | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (<65) |
|---|---|---|---|---|
| **Kedisiplinan & Proaktifitas** | Logbook harian lengkap (tanggal/jam/aktivitas/kendala), bimbingan ≥8x, balas pesan pembimbing <24 jam. | Logbook lengkap, bimbingan 8x, respons <48 jam. | Logbook 75% lengkap, bimbingan 6–7x. | Sering mangkir bimbingan atau logbook kosong. |
| **Kualitas Artefak Mingguan** | Artefak (dataset card, repo, log, draf) lengkap & bermutu, siap review. | Artefak lengkap & bermutu. | Artefak 75% lengkap. | Datang bimbingan tanpa artefak. |
| **Etika & Kejujuran Riset** | Jujur lapor kegagalan, tidak fabrikasi data, sitasi benar, deklarasi AI. | Jujur, sitasi benar. | Cukup jujur, ada sitasi kurang. | Fabrikasi data/plagiasi terbukti → sanksi. |

---

## BAGIAN IV — RUBRIK HOLISTIK TUGAS AKHIR (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `FST-714` (14 CPL — Level *Mastery*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa merekayasa solusi TUGAS AKHIR bernilai kebaruan tinggi (novelty jelas), evaluasi empiris rigor (fair SOTA + signifikansi p<0,05 + visual informatif), naskah Bab 1–5 koheren 80–120 hal + artikel IMRAD siap submit (atau accepted SINTA/Scopus), HKI terdaftar, Turnitin <15%, dan mempertahankan sidang dengan percaya diri + demo live meyakinkan. Layak nominasi skripsi terbaik / publikasi Q1. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa menyelesaikan siklus riset penuh (data etis → baseline → novelty → benchmark → Bab 4/5 → artikel → HKI → Turnitin <20%) dengan metodologi kuat, membuktikan keunggulan via SOTA + statistik, dan mempertahankan sidang dengan baik. Layak yudisium cumlaude. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE Mastery*)** | Mahasiswa memenuhi ambang ketuntasan minimal OBE (≥65,0) dalam rekayasa solusi, evaluasi SOTA, penulisan Bab 1–5 + artikel + HKI, Turnitin <20%, dan lulus sidang dengan revisi minor. Layak yudisium. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih membuat solusi tanpa kebaruan jelas, benchmarking tidak fair (strawman) atau tanpa uji statistik, naskah Bab 1–5 tidak koheren, atau Turnitin 20–30%, atau gagal demo/sidang. Perlu remedial 2 minggu–1 bulan. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menyelesaikan siklus riset (data tidak ada / baseline tidak jalan), plagiasi >30% atau fabrikasi data terbukti, atau gagal sidang 2x. Tidak layak yudisium — mengulang MK. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `FST-714` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu mengumpulkan & membersihkan dataset secara etis (UU PDP, informed consent). | `1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu membangun baseline architecture yang reproduksibel (Git, README, env). | `1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu mengimplementasikan algoritma usulan bernilai kebaruan & tuning hyperparam. | `1.3` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu melakukan benchmarking fair vs SOTA (same split/metric/hardware). | `2.1` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu menganalisis hasil secara statistik (uji-t, p-value, IK 95%) & visual. | `2.2` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu menulis Bab 4 (Hasil & Pembahasan Kritis) yang mendalam & koheren. | `2.3` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu menulis Bab 5 (Kesimpulan & Saran) yang menjawab rumusan masalah. | `3.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu menyusun artikel IMRAD IEEE/ACM siap submit (SINTA/Scopus). | `3.2` | 1 – 2 – 3 – 4 – 5 |
| 9 | Saya mampu mendaftarkan HKI Hak Cipta Program Komputer (e-HKI DJKI). | `3.3` | 1 – 2 – 3 – 4 – 5 |
| 10 | Saya mampu lolos Turnitin <20% & menjaga integritas akademik. | `3.4` | 1 – 2 – 3 – 4 – 5 |
| 11 | Saya mampu memperoleh persetujuan sidang (administrasi yudisium lengkap). | `4.1` | 1 – 2 – 3 – 4 – 5 |
| 12 | Saya mampu mempresentasikan & mendemonstrasikan karya secara meyakinkan di sidang. | `4.2` | 1 – 2 – 3 – 4 – 5 |
| 13 | Saya mampu mempertahankan argumen & menjawab sanggahan penguji secara kritis. | `4.2` | 1 – 2 – 3 – 4 – 5 |
| 14 | Saya merefleksikan diri sebagai lulusan SISTEKIN yang siap kerja/riset/wirausaha (PEO-1/2/3). | `CPL-01`–`CPL-14` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `FST-714`)

```text
================================================================================================================================================================
     LEMBAR REKAPITULASI PENILAIAN OBE — FST-714 SKRIPSI / TUGAS AKHIR (6 SKS Mandiri — 14 CPL Mastery)
================================================================================================================================================================
Semester / TA  : Semester 8 (Genap) / 2026-2027      CPL Dibebankan : CPL-01–CPL-14 (14 CPL, Level M) [6 SKS per CPL]
Klaster Rubrik : K-4 (Tugas Akhir & Publikasi)        Ambang OBE     : >= 65.0 (Cumlaude >= 85 & IPK >=3.51)
Jalur TA       : [ ] J1 Riset  [ ] J2 Industri-TRL6  [ ] J3 Startup-MVP  [ ] J4 Publikasi-SINTA/Scopus
----------------------------------------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (25%)   | T2 (25%)    | UAS (30%)   | NA    | Predikat        | Yudisium
   |           |                  | [CPMK-1:C6] | [CPMK-2:C5] | [CPMK-3:C6] | [CPMK-4:C5] | Akhir | Holistik (1-5)  |
----------------------------------------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 90.0        | 92.0        | 90.0        | 90.10 | 5 (Outstanding) | Lulus Cumlaude
2  | 250101002 | [Nama Mhs 2]     | 78.0        | 80.0        | 82.0        | 80.0        | 80.10 | 4 (Excellent)   | Lulus
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 70.0        | 72.0        | 70.0        | 70.10 | 3 (Proficient)  | Lulus (Revisi Minor)
4  | 250101004 | [Nama Mhs 4]     | 58.0        | 60.0        | 62.0        | 60.0        | 60.10 | 2 (Developing)  | Remedial 2 mg
----------------------------------------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 73.00       | 75.00       | 77.00       | 75.00       | 75.10 | 3.50            | 75% Lulus
================================================================================================================================================================
RUMUS: NA = 0.20*T1 + 0.25*UTS + 0.25*T2 + 0.30*UAS | 14 CPL = rerata tertimbang 6 SKS per CPL (FST-714 dominan)
CATATAN JALUR: J1=Riset (penekanan statistik) | J2=Industri TRL6+Surat Mitra | J3=Startup MVP+Traksi | J4=Publikasi Accepted→konversi 85+
================================================================================================================================================================
```

