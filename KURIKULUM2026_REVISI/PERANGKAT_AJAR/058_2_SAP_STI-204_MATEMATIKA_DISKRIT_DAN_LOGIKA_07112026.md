# SATUAN ACARA PERKULIAHAN (SAP)

## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA
### *Discrete Mathematics and Logic*

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang
> **Semester:** 2 (Genap) | **Bobot:** 3 SKS Teori | **Pertemuan:** 16 pekan
> **Dokumen induk:** `058_1_RPS_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md`
> **Tanggal:** 07 November 2026

---

## 1. IDENTITAS DAN KEDUDUKAN DOKUMEN

| Atribut | Keterangan |
|---|---|
| Nama MK / Kode | Matematika Diskrit dan Logika / `STI-204` |
| Rumpun MK | Matematika & Sains Komputasi (Core STI) |
| Prasyarat | `STI-103` Arsitektur dan Organisasi Sistem Teknologi Informasi |
| Dosen Pengampu | Tim Pengampu Rumpun Matematika & Sains Komputasi |
| Hari / Jam | Sesuai jadwal akademik fakultas |
| Ruang | Kelas teori (kapasitas ≥ 40 mahasiswa) |
| Media utama | LCD proyektor, papan tulis, LMS (Edlink/Moodle), simulator otomata (JFLAP), perangkat visualisasi graf |
| Alokasi waktu | TM 150′/pekan; PT 180′/pekan; BM 180′/pekan |
| Fungsi dokumen | Menjabarkan RPS menjadi rencana operasional tiap pertemuan (kegiatan, media, waktu, penilaian) |

**Kedudukan dalam rantai dokumen:** RPS (055_1) → **SAP (055_2)** → Buku Modul (055_3) → Rencana Evaluasi (055_4) → Rubrik (055_5). SAP tidak boleh menyimpang dari RPS; seluruh Sub-CPMK, materi, dan titik asesmen mengikuti RPS dan Dokumen 043.

**Catatan prasyarat:** `STI-103` dibutuhkan bukan untuk materi aritmetika, melainkan untuk konteks **representasi data dan siklus eksekusi mesin** — khususnya pada pekan 10 ketika model otomata dikaitkan dengan transisi status sistem komputasi.

---

## 2. CAPAIAN DAN INDIKATOR RINGKAS

| Kode | Rumusan | Bloom | Pekan Pencapaian | Instrumen Ukur |
|:---:|---|:---:|:---:|---|
| CPMK-1 | Membuktikan validitas argumen logika proposisi/predikat dan kebenaran algoritma | C3 | 2–3, 8 | Tugas 1, UTS |
| CPMK-2 | Menerapkan relasi ekuivalensi, Poset, aljabar Boolean, dan kombinatorika | C3 | 4–5, 8 | Tugas 1, UTS |
| CPMK-3 | Menganalisis graf dan pohon dengan matriks representasi dan penelusuran lintasan | C4 | 6–7, 8, 12, 16 | UTS, Tugas 2, UAS |
| CPMK-4 | Mengonstruksi model otomata berhingga (DFA dan NFA) | C4 | 9–11, 12, 16 | Tugas 2, UAS |

**Indikator kinerja kunci (IKK):**

1. ≥ 80% mahasiswa mampu menyusun tabel kebenaran dan membuktikan ekuivalensi logis tanpa kekeliruan hukum aljabar logika.
2. ≥ 75% mahasiswa mampu menyelesaikan pembuktian induksi dengan basis, hipotesis, dan langkah yang lengkap.
3. ≥ 75% mahasiswa mampu menguji sifat relasi dan menyusun diagram Hasse yang benar.
4. ≥ 70% mahasiswa mampu menerapkan algoritma Kruskal/Prim dan Dijkstra pada graf berbobot.
5. ≥ 70% mahasiswa mampu mengonstruksi DFA dan mengonversi NFA→DFA dengan *subset construction*.
6. Rata-rata ketercapaian CPL-05 (P1) dari MK ini ≥ 65,0 (ambang Dokumen 008).

---

## 3. MATRIKS JADWAL PERKULIAHAN

| Pekan | Sub-CPMK | Pokok Bahasan | Metode | Asesmen |
|:--:|---|---|---|---|
| 1 | Orientasi | Ruang lingkup, kontrak belajar, peta CPL–CPMK | Kuliah interaktif | Formatif |
| 2 | 1.1 | Logika proposisi, tabel kebenaran, hukum aljabar logika | Kuliah + latihan terbimbing | Formatif (kuis LMS) |
| 3 | 1.2 | Logika predikat, aturan inferensi, induksi matematika | Ceramah + latihan pembuktian | Formatif |
| 4 | 2.1 | Himpunan, relasi biner, relasi ekuivalensi, Poset, diagram Hasse | Case-based learning | **Tugas 1 (20%)** |
| 5 | 2.2 | Aljabar Boolean, kombinatorika, relasi rekurensi | Kuliah + latihan bertingkat | Formatif |
| 6 | 3.1 | Graf, adjacency matrix/list, BFS/DFS | Ceramah + visualisasi | Formatif (kuis) |
| 7 | 3.2 | Pohon, MST Kruskal–Prim, Dijkstra, Floyd–Warshall | Case method | Formatif (studi kasus) |
| 8 | — | **UTS** (CPMK-1, 2, 3) | Ujian tertulis | **UTS (30%)** |
| 9 | 4.1 | DFA: definisi formal, tabel transisi, diagram status | Ceramah + konstruksi bersama | Formatif |
| 10 | 4.2 | NFA, ε-transisi, subset construction, ekspresi reguler | Ceramah + latihan | Formatif |
| 11 | 4.3 | Studi kasus pemodelan graf & otomata | PjBL / case method | Formatif (konsultasi) |
| 12 | 4.4 | Proyek terapan lanjut & presentasi antara | PjBL / presentasi | **Tugas 2 (20%)** |
| 13 | Semua | Penyempurnaan proyek | PjBL / konsultasi | Formatif (checklist) |
| 14 | Semua | Review & konsolidasi | Diskusi / konsultasi | Formatif |
| 15 | Semua | Presentasi final | Presentasi | Formatif (rubrik presentasi) |
| 16 | — | **UAS** (komprehensif) | Ujian tertulis | **UAS (30%)** |

---

## 4. RINCIAN KEGIATAN PER PERTEMUAN

### Pertemuan 1 — Orientasi dan Kontrak Belajar

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Orientasi (fondasi CPMK-1) |
| Indikator | Mahasiswa mampu menjelaskan ruang lingkup MK, capaian pembelajaran, dan skema asesmen |
| Materi | Ruang lingkup matematika diskrit untuk komputasi; peta CPL-05 (P1)/KU1 → CPMK-1..4 → Sub-CPMK; skema 4 titik asesmen; aturan akademik & etika AI; pengantar mengapa logika formal menjadi dasar *debugging* dan verifikasi program |
| Metode | Kuliah interaktif, tanya-jawab, diagnostik awal |
| Media | Slide pengantar, kontrak belajar, LMS |
| **Kegiatan (150′)** | **Pendahuluan (15′):** salam, presensi, apersepsi "mengapa program bisa dibuktikan benar?". **Inti (120′):** (1) pemaparan ruang lingkup & capaian 30′; (2) pemaparan skema asesmen & bobot 25′; (3) kontrak belajar & etika akademik 25′; (4) tes diagnostik kemampuan logika dasar 40′. **Penutup (15′):** rangkuman, penugasan membaca Bab 1 [1], pengarahan unduh materi LMS |
| Penilaian | Formatif — tes diagnostik (non-graded), kehadiran & partisipasi |
| Referensi | [1] Bab 1 |

### Pertemuan 2 — Logika Proposisi dan Ekuivalensi Logis

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-1.1** |
| Indikator | 1.1.1 Ketepatan tabel kebenaran; 1.1.2 Ketepatan penerapan hukum aljabar logika |
| Materi | Proposisi dan nilai kebenaran; konektif NOT, AND, OR, XOR, implikasi, bikondisional; tabel kebenaran; tautologi, kontradiksi, kontingensi; hukum identitas, dominasi, idempoten, negasi ganda, komutatif, asosiatif, distributif, De Morgan; ekuivalensi logis dan pembuktiannya tanpa tabel |
| Metode | Kuliah & latihan terbimbing |
| Media | Slide, papan tulis, lembar latihan bertingkat |
| **Kegiatan (150′)** | **Pendahuluan (15′):** review tugas baca, pertanyaan pemantik "apakah (p→q) sama dengan (¬q→¬p)?". **Inti (120′):** (1) konektif & tabel kebenaran 35′; (2) klasifikasi formula 25′; (3) hukum aljabar logika & pembuktian ekuivalensi 35′; (4) latihan terbimbing 6 soal 25′. **Penutup (15′):** rangkuman, kuis formatif LMS, penugasan |
| Penilaian | Formatif — kuis LMS (non-graded), observasi latihan |
| Referensi | [1] Bab 1; [2] Bab 2 |

### Pertemuan 3 — Logika Predikat, Inferensi, dan Induksi Matematika

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-1.2** |
| Indikator | 1.2.1 Ketepatan kuantifikasi & aturan inferensi; 1.2.2 Ketepatan langkah induksi (basis, hipotesis, langkah) |
| Materi | Predikat dan domain; kuantor universal (∀) dan eksistensial (∃); negasi kuantor; aturan inferensi: modus ponens, modus tollens, silogisme hipotetis, silogisme disjungtif, konjungsi, adisi, resolusi; kesesatan logika umum; induksi matematika biasa dan kuat; verifikasi kebenaran algoritma (invarian loop) |
| Metode | Ceramah interaktif + latihan pembuktian terstruktur |
| Media | Slide, papan tulis, bank soal pembuktian LMS |
| **Kegiatan (150′)** | **Pendahuluan (15′):** kaitkan proposisi tunggal dengan predikat berkuantor. **Inti (120′):** (1) kuantor & negasinya 30′; (2) aturan inferensi dengan contoh argumen 30′; (3) struktur induksi biasa & kuat 35′; (4) latihan pembuktian 3 soal 25′. **Penutup (15′):** rangkuman, penugasan membaca [2] Bab 3 & 5 |
| Penilaian | Formatif — lembar pembuktian |
| Referensi | [1] Bab 2 & 5; [2] Bab 3 & 5 |

### Pertemuan 4 — Himpunan, Relasi Ekuivalensi, dan Poset  ⟶ **TUGAS 1 (20%)**

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-2.1** |
| Indikator | 2.1.1 Ketepatan klasifikasi sifat relasi; 2.1.2 Ketepatan penyusunan diagram Hasse |
| Materi | Himpunan, operasi himpunan, hukum himpunan, produk kartesius; relasi biner; sifat refleksif, simetris, antisimetris, transitif; relasi ekuivalensi dan kelas ekuivalensi; partisi; himpunan terurut parsial (Poset); elemen maksimal/minimal/terbesar/terkecil; diagram Hasse |
| Metode | Case-based learning, kerja individu terpandu |
| Media | Slide, formulir Tugas 1, lembar diagram Hasse |
| **Kegiatan (150′)** | **Pendahuluan (15′):** pengantar asesmen Tugas 1. **Inti (120′):** (1) operasi himpunan & relasi biner 30′; (2) sifat relasi & relasi ekuivalensi 30′; (3) Poset & diagram Hasse 25′; (4) pengerjaan Tugas 1 di kelas 35′. **Penutup (15′):** pengumpulan, penjelasan revisi, penugasan lanjutan |
| Penilaian | **Sumatif — Tugas 1 (20%)**, rubrik 4 dimensi (055_5) |
| Referensi | [1] Bab 6 & 9; [3] Bab 7 |

### Pertemuan 5 — Aljabar Boolean, Kombinatorika, dan Relasi Rekurensi

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-2.2** |
| Indikator | 2.2.1 Ketepatan penyederhanaan fungsi Boolean; 2.2.2 Ketepatan perhitungan kombinatorial |
| Materi | Fungsi Boolean dan representasinya; bentuk normal disjungtif dan konjungtif; penyederhanaan aljabar; kaidah penjumlahan dan perkalian; permutasi dan kombinasi (dengan/tanpa pengulangan); prinsip pigeonhole; prinsip inklusi–eksklusi; relasi rekurensi linier homogen dan metode akar karakteristik |
| Metode | Kuliah & latihan bertingkat |
| Media | Slide, papan tulis, lembar latihan bertingkat |
| **Kegiatan (150′)** | **Pendahuluan (15′):** refleksi Tugas 1, pertanyaan "berapa banyak kata sandi yang mungkin?". **Inti (120′):** (1) fungsi Boolean & bentuk normal 30′; (2) kaidah pencacahan & pigeonhole 35′; (3) permutasi–kombinasi 30′; (4) relasi rekurensi 25′. **Penutup (15′):** rangkuman, penugasan membaca [1] Bab 8 & 12 |
| Penilaian | Formatif — lembar latihan bertingkat |
| Referensi | [1] Bab 12 & 8; [3] Bab 11 & 12 |

### Pertemuan 6 — Struktur Graf dan Penelusuran

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-3.1** |
| Indikator | 3.1.1 Ketepatan representasi adjacency matrix/list; 3.1.2 Ketepatan penelusuran BFS/DFS |
| Materi | Terminologi graf (simpul, sisi, derajat, lintasan, siklus); graf sederhana, multigraf, pseudograf; isomorfisme; graf bipartit dan uji bipartit; keterhubungan dan komponen; matriks ketetanggaan (*adjacency matrix*) dan *adjacency list*; algoritma BFS dan DFS beserta kompleksitasnya |
| Metode | Ceramah & visualisasi interaktif |
| Media | Slide, visualisasi graf daring, papan tulis |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "bagaimana memetakan jaringan kampus?". **Inti (120′):** (1) terminologi & isomorfisme 30′; (2) keterhubungan & bipartit 25′; (3) representasi matrix vs list 30′; (4) BFS/DFS dengan penelusuran manual 35′. **Penutup (15′):** kuis formatif, penugasan |
| Penilaian | Formatif — kuis LMS + lembar penelusuran |
| Referensi | [1] Bab 10; [7] Bab 1 |

### Pertemuan 7 — Pohon, MST, dan Lintasan Terpendek

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-3.2** |
| Indikator | 3.2.1 Ketepatan MST Kruskal/Prim; 3.2.2 Ketepatan lintasan terpendek Dijkstra/Floyd–Warshall |
| Materi | Pohon dan sifatnya; pohon merentang (*spanning tree*); *Minimum Spanning Tree* dengan algoritma Kruskal dan Prim; lintasan dan sirkuit Euler; sirkuit Hamilton; algoritma Dijkstra (graf berbobot tak negatif); algoritma Floyd–Warshall (semua pasangan); analisis kompleksitas |
| Metode | Case method |
| Media | Slide, studi kasus topologi jaringan, lembar kerja algoritma |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "bagaimana merancang kabel jaringan dengan biaya minimum?". **Inti (120′)** (1) pohon & spanning tree 25′; (2) Kruskal & Prim 35′; (3) Euler & Hamilton 25′; (4) Dijkstra & Floyd–Warshall 35′. **Penutup (15′):** sintesis, penugasan membaca [6] Bab 21–23 |
| Penilaian | Formatif — lembar kerja algoritma |
| Referensi | [1] Bab 11; [6] Bab 21–23 |

### Pertemuan 8 — Evaluasi Tengah Semester (UTS)  ⟶ **UTS (30%)**

| Komponen | Uraian |
|---|---|
| Cakupan | CPMK-1, CPMK-2, CPMK-3 (tahap awal) — materi pekan 1–7 |
| Bentuk | Bagian I logika proposisi & predikat (25); II pembuktian induksi (20); III relasi, Poset, Boolean, kombinatorika (30); IV studi kasus graf (25) |
| Durasi | 150 menit, *closed book* |
| Pengawasan | Dosen + 1 pengawas; tata tertib ujian fakultas |
| Penilaian | Rubrik UTS (055_5), kunci jawaban terstandar |
| Tindak lanjut | Analisis butir soal; pengumuman nilai ≤ 7 hari; remedial sesuai kebijakan prodi |

### Pertemuan 9 — Deterministic Finite Automata (DFA)

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.1** |
| Indikator | 4.1.1 Kelengkapan 5-tuple DFA; 4.1.2 Ketepatan tabel transisi & diagram status |
| Materi | Alfabet, string, bahasa, operasi bahasa; definisi formal DFA $M=(Q,\Sigma,\delta,q_0,F)$; tabel transisi; diagram status; fungsi transisi yang diperluas $\hat{\delta}$; penerimaan string; bahasa yang dikenali DFA; contoh DFA untuk pola sederhana (jumlah bit genap, substring tertentu) |
| Metode | Ceramah & konstruksi bersama |
| Media | Slide, simulator JFLAP, papan tulis |
| **Kegiatan (150′)** | **Pendahuluan (15′):** refleksi UTS & rencana perbaikan; "bagaimana validator input bekerja?". **Inti (120′)** (1) konsep bahasa formal 25′; (2) definisi formal DFA 30′; (3) konstruksi DFA dari deskripsi bahasa 40′; (4) uji string & penelusuran 25′. **Penutup (15′):** rangkuman, penugasan |
| Penilaian | Formatif — lembar konstruksi DFA |
| Referensi | [4] Bab 2; [5] Bab 1 |

### Pertemuan 10 — NFA dan Konversi ke DFA

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.2** |
| Indikator | 4.2.1 Ketepatan konstruksi NFA; 4.2.2 Ketepatan subset construction |
| Materi | Definisi formal NFA; transisi non-deterministik dan ε-transisi; ε-closure; ekuivalensi NFA–DFA; algoritma *subset construction* (konstruksi himpunan bagian); ledakan jumlah status; pengantar ekspresi reguler dan hubungannya dengan otomata |
| Metode | Ceramah & latihan terstruktur |
| Media | Slide, simulator JFLAP, lembar latihan konversi |
| **Kegiatan (150′)** | **Pendahuluan (15′):** "mengapa mesin boleh menebak?". **Inti (120′)** (1) definisi NFA & ε-transisi 30′; (2) ε-closure 25′; (3) subset construction langkah demi langkah 40′; (4) latihan konversi 25′. **Penutup (15′):** rangkuman, penugasan membaca [4] Bab 3 |
| Penilaian | Formatif — lembar latihan konversi |
| Referensi | [4] Bab 2 & 3; [5] Bab 1 |

### Pertemuan 11 — Studi Kasus Pemodelan Graf dan Otomata

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.3** (penguatan CPMK-3 & CPMK-4) |
| Indikator | 4.3.1 Ketepatan pemodelan kasus; 4.3.2 Ketepatan justifikasi algoritma terpilih |
| Materi | Studi kasus terpadu: (a) optimasi topologi jaringan kampus dengan MST dan Dijkstra; (b) penjadwalan ujian dengan pewarnaan graf; (c) validasi format masukan sistem dengan DFA; pembahasan justifikasi pemilihan model dan algoritma |
| Metode | PjBL & case method |
| Media | Slide, template pemodelan, konsultasi asinkron |
| **Kegiatan (150′)** | **Pendahuluan (15′):** pengantar tugas proyek & pengelompokan. **Inti (120′)** (1) pembahasan tiga kasus 40′; (2) pembentukan kelompok & pemilihan tema 20′; (3) penyusunan draf formalisasi 40′; (4) konsultasi 20′. **Penutup (15′):** tenggat draf, arahan lanjutan |
| Penilaian | Formatif — draf formalisasi |
| Referensi | [6] Bab 21–23; [4] Bab 2 |

### Pertemuan 12 — Proyek Terapan dan Presentasi Antara  ⟶ **TUGAS 2 (20%)**

| Komponen | Uraian |
|---|---|
| Sub-CPMK | **Sub-CPMK-4.4** (integrasi 4.1 & 4.2) |
| Indikator | 4.4.1 Kelayakan model diskrit; 4.4.2 Kejelasan argumentasi formal |
| Materi | Presentasi progres proyek: formalisasi model, algoritma terpilih, contoh kerja manual, visualisasi, analisis kompleksitas |
| Metode | PjBL & presentasi |
| Media | Proyektor, timer, lembar penilaian presentasi |
| **Kegiatan (150′)** | **Pendahuluan (15′):** tata tertib presentasi & rubrik. **Inti (120′):** 4 kelompok × 25′ (15′ presentasi + 10′ tanya jawab & umpan balik). **Penutup (15′):** umpan balik menyeluruh, arahan revisi |
| Penilaian | **Sumatif — Tugas 2 (20%)**, rubrik 4 dimensi (055_5) |
| Referensi | [1]; [6] |

### Pertemuan 13 — Penyempurnaan Proyek

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK (penyempurnaan) |
| Indikator | 4.4.3 Ketepatan revisi; 4.4.4 Kualitas dokumentasi |
| Materi | Revisi berdasarkan umpan balik: kelengkapan formalisasi, ketepatan verifikasi manual, perbaikan visualisasi, penajaman analisis kompleksitas dan keterbatasan |
| Metode | PjBL & konsultasi klinis |
| Media | Lembar konsultasi, repositori dokumen kelompok |
| **Kegiatan (150′)** | **Pendahuluan (15′):** rekap umpan balik agregat. **Inti (120′):** konsultasi bergilir per kelompok 15′ × 8, diselingi kerja mandiri kelompok. **Penutup (15′):** kesepakatan tenggat final |
| Penilaian | Formatif — checklist revisi |
| Referensi | Seluruh materi CPMK-3 & CPMK-4 |

### Pertemuan 14 — Review dan Konsolidasi

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK |
| Indikator | Ketepatan identifikasi kesenjangan pemahaman |
| Materi | Rekapitulasi pekan 1–13; peta konsep terpadu proposisi → predikat → induksi → relasi → kombinatorika → graf → pohon → otomata; pembahasan soal terpilih |
| Metode | Diskusi & konsultasi |
| Media | Peta konsep besar, bank soal terpilih |
| **Kegiatan (150′)** | **Pendahuluan (15′):** penjelasan mekanisme review. **Inti (120′)** (1) penyusunan peta konsep bersama 40′; (2) pembahasan 8 soal kunci 50′; (3) tanya-jawab terbuka 30′. **Penutup (15′):** arahan UAS, penegasan cakupan |
| Penilaian | Formatif — partisipasi |
| Referensi | Rekapitulasi pekan 1–13 |

### Pertemuan 15 — Presentasi Final

| Komponen | Uraian |
|---|---|
| Sub-CPMK | Seluruh CPMK |
| Indikator | 4.4.5 Kualitas komunikasi formal; 4.4.6 Penguasaan saat tanya jawab |
| Materi | Presentasi hasil akhir proyek: model, algoritma, hasil verifikasi, kompleksitas, keterbatasan, kesimpulan |
| Metode | Presentasi tim & pleno |
| Media | Proyektor, timer, lembar penilaian |
| **Kegiatan (150′)** | **Pendahuluan (15′):** tata tertib. **Inti (120′):** 4 kelompok × 25′ (15′ presentasi + 10′ tanya jawab). **Penutup (15′):** apresiasi, arahan UAS |
| Penilaian | Formatif — rubrik presentasi (masuk komponen proses) |
| Referensi | Seluruh materi |

### Pertemuan 16 — Evaluasi Akhir Semester (UAS)  ⟶ **UAS (30%)**

| Komponen | Uraian |
|---|---|
| Cakupan | Komprehensif CPMK-1 s.d. CPMK-4 |
| Bentuk | I uraian logika/induksi/struktur diskrit (25); II uraian graf/pohon/lintasan (25); III studi kasus otomata (30); IV pemodelan terbuka (20) |
| Durasi | 150 menit, *closed book* |
| Penilaian | Rubrik UAS (055_5) |
| Tindak lanjut | Rekap nilai akhir, analisis ketercapaian CPMK/CPL, input SIAKAD ≤ 7 hari |

---

## 5. LEMBAR MONITORING PELAKSANAAN

| Pekan | Tanggal | Materi Terlaksana | Jumlah Hadir | Catatan Kejadian | Paraf Dosen |
|:--:|---|---|:--:|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |
| 13 | | | | | |
| 14 | | | | | |
| 15 | | | | | |
| 16 | | | | | |

---

## 6. CATATAN PELAKSANAAN DAN RENCANA KONTINGENSI

1. **Kehadiran minimum:** 75% dari 16 pertemuan (12 pertemuan) sebagai syarat mengikuti UAS.
2. **Pertemuan pengganti:** diselenggarakan jika terjadi hari libur nasional atau kegiatan fakultas, dengan materi setara dan bukti dokumentasi.
3. **Pembelajaran daring darurat:** seluruh materi tersedia di LMS; sesi sinkron melalui konferensi video dengan rekaman wajib diunggah.
4. **Keterbatasan laboratorium:** MK ini bertipe Teori (P = 0); seluruh latihan algoritma dan otomata dilakukan secara manual di kertas dan diverifikasi dengan simulator daring (JFLAP) pada perangkat mahasiswa. Tidak diperlukan lab khusus.
5. **Kebutuhan komputasi:** simulator JFLAP bersifat ringan (berbasis Java) dan tersedia gratis; untuk mahasiswa tanpa perangkat memadai disediakan sesi bersama di laboratorium komputer fakultas.
6. **Mahasiswa dengan kebutuhan khusus:** penyesuaian waktu asesmen dan format materi (sesuai kebijakan layanan disabilitas universitas).
7. **Integritas akademik:** setiap tugas wajib menyertakan Deklarasi Transparansi AI; dosen berhak melakukan verifikasi lisan 3 menit.
8. **Umpan balik:** hasil asesmen dikembalikan maksimal 7 hari kerja dengan komentar per dimensi rubrik.

---

*Dokumen ini merupakan penjabaran operasional dari `058_1_RPS_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md` dan konsisten dengan Dokumen 043 (Sub-CPMK & Boundary Guardrails).*
