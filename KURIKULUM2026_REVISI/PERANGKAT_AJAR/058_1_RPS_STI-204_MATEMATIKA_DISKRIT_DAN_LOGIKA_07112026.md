# RENCANA PEMBELAJARAN SEMESTER (RPS)

## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA
### *Discrete Mathematics and Logic*

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)
> **Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang
> **Nomor Dokumen SPMI:** 071030.B4.5.2.RPS-STI204
> **Tanggal Penyusunan:** 07 November 2026
> **Sumber Data:** Dokumen 005 (struktur & identitas), 007 (silabus), 043 (CPMK/Sub-CPMK/Boundary Guardrails), 003 (CPL), 008 & 018 (skema asesmen dan rubrik)

---

## HALAMAN 1 — SAMPUL DEPAN (LANDSCAPE)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                            UNIVERSITAS WIDYAGAMA                             │
│                    FAKULTAS SAINS DAN TEKNOLOGI INFORMASI                    │
│                                                                              │
│                                                                              │
│                  RENCANA PEMBELAJARAN SEMESTER (RPS)                         │
│                                                                              │
│                                                                              │
│                 STI-204 — MATEMATIKA DISKRIT DAN LOGIKA                      │
│                       Discrete Mathematics and Logic                         │
│                                                                              │
│                            BOBOT: 3 SKS (TEORI)                              │
│                                                                              │
│                                                                              │
│                    Penyusun: Tim Pengembang RPS SISTEKIN                     │
│                    Koordinator RMK Matematika & Sains Komputasi              │
│                                                                              │
│                                                                              │
│                            MALANG, NOVEMBER 2026                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## HALAMAN 2 — IDENTITAS, OTORISASI, DAN CAPAIAN PEMBELAJARAN (LANDSCAPE)

### A. Tabel Identitas Mata Kuliah

| Atribut | Spesifikasi |
|---|---|
| **MATA KULIAH (MK)** | Matematika Diskrit dan Logika / *Discrete Mathematics and Logic* |
| **KODE** | `STI-204` |
| **RUMPUN MK** | Matematika & Sains Komputasi (Core STI) |
| **BOBOT (sks)** | **T = 3** · **P = 0** — Total 3 SKS |
| **SEMESTER** | 2 (Genap) |
| **TGL PENYUSUNAN** | 07 November 2026 |
| **MATA KULIAH SYARAT** | `STI-103` Arsitektur dan Organisasi Sistem Teknologi Informasi |
| **DOSEN PENGAMPU** | Tim Pengampu Rumpun Matematika & Sains Komputasi (Core STI) |
| **BODY OF KNOWLEDGE** | `BK-IS10` *Applied Mathematics and Logic*; `BK-IS11` *Programming Fundamentals* |

### B. Blok Otorisasi

| Pengembang RPS | Koordinator RMK | Ketua Program Studi |
|:---:|:---:|:---:|
| Tim Pengembang RPS SISTEKIN | Koordinator RMK Matematika & Sains Komputasi | Ketua Prodi SISTEKIN FSTI |
| .......................... | .......................... | .......................... |

### C. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada MK

| Kode Baku (Alias) | Rumusan CPL (verbatim Dokumen 003) |
|:---:|---|
| **CPL-05** (`P1`) | Menguasai konsep dasar sains, matematika terapan (kalkulus, aljabar linear, statistika, matematika diskrit, logika) sebagai fondasi pemecahan masalah rekayasa sistem informasi dan komputasi cerdas yang kompleks. |
| **CPL-02** (`KU1`) | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam menganalisis permasalahan komputasi serta mengkaji implikasi pengembangan atau implementasi iptek sesuai kaidah, tata cara, dan etika ilmiah. |

Bobot kontribusi MK terhadap kedua CPL tersebut: **3 SKS** dari total MK pembina masing-masing CPL.

### D. Capaian Pembelajaran Mata Kuliah (CPMK)

| Kode | Rumusan CPMK (Format ABCD) | Bloom | CPL |
|:---:|---|:---:|:---:|
| **CPMK-1** | Mahasiswa (*A*) mampu **membuktikan** validitas argumen inferensi logika proposisi/predikat dan kebenaran algoritma (*B*) menggunakan tabel kebenaran, hukum aljabar logika, dan metode induksi matematika (*C*) secara runtut dan valid (*D*). | **C3** | `P1, KU1` |
| **CPMK-2** | Mahasiswa (*A*) mampu **menerapkan** konsep relasi ekuivalensi, himpunan terurut parsial (Poset), aljabar Boolean, dan kombinatorika (*B*) pada pemodelan struktur data dan logika query basis data (*C*) secara tepat (*D*). | **C3** | `CPL-05` (`P1`) |
| **CPMK-3** | Mahasiswa (*A*) mampu **menganalisis** struktur Graf dan Pohon (Tree) (*B*) menggunakan matriks representasi (Adjacency Matrix) dan algoritma penelusuran lintasan (*C*) untuk optimasi jaringan data/komputer (*D*). | **C4** | `P1, KU1` |
| **CPMK-4** | Mahasiswa (*A*) mampu **mengonstruksi** model otomata berhingga (Finite State Automata / FSA: DFA dan NFA) (*B*) untuk pengenalan pola bahasa formal dan transisi status sistem komputasi (*C*) secara akurat (*D*). | **C4** | `CPL-05` (`P1`) |

### E. Sub-Capaian Pembelajaran Mata Kuliah (Sub-CPMK)

| Kode | Kompetensi Spesifik | CPMK | Bloom |
|---:|---|:--:|:--:|
| **Sub-CPMK-1.1** | Membuktikan validitas argumen logika proposisi melalui tabel kebenaran dan hukum aljabar logika. | CPMK-1 | **C3** |
| **Sub-CPMK-1.2** | Menerapkan inferensi logika predikat dan induksi matematika untuk memverifikasi kebenaran algoritma. | CPMK-1 | **C3** |
| **Sub-CPMK-2.1** | Menerapkan relasi ekuivalensi dan himpunan terurut parsial (Poset) pada pemodelan struktur data. | CPMK-2 | **C3** |
| **Sub-CPMK-2.2** | Menerapkan aljabar Boolean dan kombinatorika pada logika query basis data. | CPMK-2 | **C3** |
| **Sub-CPMK-3.1** | Menganalisis struktur graf menggunakan matriks representasi (Adjacency Matrix) dan penelusuran lintasan. | CPMK-3 | **C4** |
| **Sub-CPMK-3.2** | Menerapkan pohon (tree) untuk optimasi lintasan pada jaringan data/komputer. | CPMK-3 | **C4** |
| **Sub-CPMK-4.1** | Mengonstruksi model DFA untuk pengenalan pola bahasa formal. | CPMK-4 | **C4** |
| **Sub-CPMK-4.2** | Mengonstruksi model NFA dan konversinya ke DFA untuk transisi status sistem komputasi. | CPMK-4 | **C4** |

### F. Matriks Korelasi CPL ↔ CPMK dan Bobot Penilaian

| CPMK | CPL | Pekan | Tugas 1 (20%) | UTS (30%) | Tugas 2 (20%) | UAS (30%) | Bobot CPMK |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CPMK-1 | `CPL-05` (`P1`), `CPL-02` (`KU1`) | 2–3, 8 | **60%** | **40%** | — | — | 100% |
| CPMK-2 | `CPL-05` (`P1`) | 4–5, 8 | **40%** | **60%** | — | — | 100% |
| CPMK-3 | `CPL-05` (`P1`), `CPL-02` (`KU1`) | 6–7, 8, 12, 16 | — | **20%** | **30%** | **50%** | 100% |
| CPMK-4 | `CPL-05` (`P1`) | 9–11, 12, 16 | — | — | **60%** | **40%** | 100% |
| **Total instrumen** | | | **20%** | **30%** | **20%** | **30%** | **100%** |

*Cara baca:* Skor CPMK-1 = 0,60 × Tugas 1 + 0,40 × UTS. Skor CPMK-2 = 0,40 × Tugas 1 + 0,60 × UTS. Skor CPMK-3 = 0,20 × UTS + 0,30 × Tugas 2 + 0,50 × UAS. Skor CPMK-4 = 0,60 × Tugas 2 + 0,40 × UAS. Nilai Akhir = 0,20×T1 + 0,30×UTS + 0,20×T2 + 0,30×UAS.

**Kontribusi terhadap CPL:** MK ini membina dua CPL. Bobot distribusi internal: `CPL-05` (`P1`) 70%, `CPL-02` (`KU1`) 30% (ditetapkan berdasarkan dominasi indikator tiap CPMK).

### G. Deskripsi Singkat Mata Kuliah

Mata kuliah ini membangun **bahasa penalaran formal** yang menjadi fondasi seluruh rekayasa sistem informasi cerdas. Bagian pertama menurunkan logika dari bawah: proposisi, tabel kebenaran, tautologi dan kontradiksi, hukum-hukum aljabar logika, ekuivalensi logis, aturan inferensi (modus ponens, modus tollens, silogisme, resolusi), logika predikat dengan kuantor universal–eksistensial, serta induksi matematika biasa dan kuat sebagai alat verifikasi kebenaran algoritma. Bagian kedua membahas struktur diskrit yang menyusun data: himpunan, relasi biner, relasi ekuivalensi, partisi, himpunan terurut parsial (Poset) dan diagram Hasse, aljabar Boolean, serta kombinatorika (permutasi, kombinasi, prinsip pigeonhole, relasi rekurensi) yang menjadi dasar analisis kompleksitas. Bagian ketiga memindahkan struktur tersebut ke representasi mesin: graf, isomorfisme, keterhubungan, representasi *adjacency matrix* dan *adjacency list*, penelusuran BFS/DFS, lintasan Euler dan sirkuit Hamilton, pohon dan *Minimum Spanning Tree* (Kruskal/Prim), serta lintasan terpendek (Dijkstra, Floyd–Warshall) untuk optimasi topologi jaringan. Bagian akhir memperkenalkan teori bahasa formal: DFA, NFA, dan konversi NFA→DFA melalui *subset construction*, sebagai model transisi status sistem komputasi. Seluruh pembahasan berada pada **level matematis formal**; implementasi struktur data di memori dan perancangan gerbang fisik diserahkan ke MK lain sesuai pagar *Out-of-Scope* Dokumen 043. MK ini menjadi prasyarat langsung bagi `STI-307` (Sistem Cerdas) dan penopang `FST-203` (Struktur Data dan Algoritma).

### H. Bahan Kajian (Body of Knowledge)

| Kode | Nomenklatur BoK | Cakupan dalam MK |
|:---:|---|---|
| `BK-IS10` | *Applied Mathematics and Logic* | Logika proposisi & predikat, teori himpunan, relasi, kombinatorika, teori graf, pohon, otomata berhingga |
| `BK-IS11` | *Programming Fundamentals* | Penerapan logika formal pada verifikasi algoritma, analisis kompleksitas, dan pemodelan status program |

**Pokok bahasan:** (1) logika proposisi, tabel kebenaran, ekuivalensi; (2) logika predikat, kuantor, aturan inferensi; (3) induksi matematika & verifikasi algoritma; (4) himpunan, relasi biner, relasi ekuivalensi, Poset; (5) aljabar Boolean, kombinatorika, relasi rekurensi; (6) graf: terminologi, representasi, BFS/DFS; (7) pohon, MST, lintasan terpendek; (8) evaluasi tengah semester; (9) DFA; (10) NFA & konversi ke DFA; (11) studi kasus pemodelan graf; (12) proyek terapan & presentasi antara; (13) penyempurnaan proyek; (14) review & konsolidasi; (15) presentasi final; (16) evaluasi akhir semester.

### I. Pustaka

**Pustaka Utama**

| No | Referensi |
|:---:|---|
| [1] | Rosen, K.H. (2019). *Discrete Mathematics and Its Applications*, 8th ed. McGraw-Hill. ISBN 978-1-259-67651-2. |
| [2] | Epp, S.S. (2020). *Discrete Mathematics with Applications*, 5th ed. Cengage Learning. ISBN 978-1-337-69419-3. |
| [3] | Grimaldi, R.P. (2004). *Discrete and Combinatorial Mathematics: An Applied Introduction*, 5th ed. Pearson. ISBN 978-0-321-21103-1. |

**Pustaka Pendukung**

| No | Referensi |
|:---:|---|
| [4] | Hopcroft, J.E., Motwani, R. & Ullman, J.D. (2006). *Introduction to Automata Theory, Languages, and Computation*, 3rd ed. Pearson. ISBN 978-0-321-45536-9. |
| [5] | Sipser, M. (2012). *Introduction to the Theory of Computation*, 3rd ed. Cengage. ISBN 978-1-133-18779-0. |
| [6] | Cormen, T.H., Leiserson, C.E., Rivest, R.L. & Stein, C. (2022). *Introduction to Algorithms*, 4th ed. MIT Press. ISBN 978-0-262-04630-5. |
| [7] | Diestel, R. (2017). *Graph Theory*, 5th ed. Springer. ISBN 978-3-662-53621-6. |
| [8] | Johnsonbaugh, R. (2018). *Discrete Mathematics*, 8th ed. Pearson. ISBN 978-0-321-96468-7. |

---

## HALAMAN 3–4 — MATRIKS RENCANA PEMBELAJARAN 16 PEKAN (LANDSCAPE)

**Identitas waktu:** 3 SKS Teori → TM = 150 menit/pekan; PT = 180 menit/pekan; BM = 180 menit/pekan.

| Mg | Sub-CPMK (Kemampuan Akhir) | Indikator Penilaian | Kriteria & Teknik | Luring (TM/PT/BM) | Daring | Materi Pembelajaran [Pustaka] | Bobot |
|:--:|---|---|---|---|---|---|:--:|
| 1 | Orientasi MK & kontrak belajar (fondasi CPMK-1) | Ketepatan menjelaskan ruang lingkup, capaian, dan skema asesmen | Kriteria: kelengkapan jawaban; Teknik: tanya-jawab lisan | Kuliah interaktif; TM 150′ / PT 180′ / BM 180′ | Forum perkenalan di LMS; unduh kontrak belajar | Ruang lingkup matematika diskrit, peta CPL–CPMK, aturan akademik & etika AI [1] Bab 1 | — |
| 2 | **Sub-CPMK-1.1** — Membuktikan validitas argumen logika proposisi | 1.1.1 Ketepatan tabel kebenaran; 1.1.2 Ketepatan penerapan hukum aljabar logika | Kriteria: ketepatan prosedur; Teknik: kuis formatif, latihan terbimbing | Kuliah & latihan; TM 150′ / PT 180′ / BM 180′ | Kuis LMS (formatif, non-graded) | Proposisi, operasi logika, tabel kebenaran, tautologi–kontradiksi–kontingensi, hukum De Morgan & distributif [1] Bab 1; [2] Bab 2 | — |
| 3 | **Sub-CPMK-1.2** — Menerapkan inferensi logika predikat & induksi matematika | 1.2.1 Ketepatan kuantifikasi & aturan inferensi; 1.2.2 Ketepatan langkah induksi (basis, hipotesis, langkah) | Kriteria: kebenaran langkah pembuktian; Teknik: latihan terstruktur | Ceramah interaktif + latihan; TM 150′ / PT 180′ / BM 180′ | Bank soal pembuktian di LMS | Logika predikat, kuantor universal–eksistensial, modus ponens/tollens, silogisme, resolusi, induksi biasa & kuat, verifikasi algoritma [1] Bab 2 & 5; [2] Bab 3 & 5 | — |
| **4** | **Sub-CPMK-2.1** — Menerapkan relasi ekuivalensi & himpunan terurut parsial (Poset) | 2.1.1 Ketepatan klasifikasi sifat relasi; 2.1.2 Ketepatan penyusunan diagram Hasse | Kriteria: rubrik analitik (4 dimensi); Teknik: **Tugas 1** — kuis + problem solving | Case-based learning; TM 150′ / PT 180′ / BM 180′ | Submit Tugas 1 via LMS (PDF) | Himpunan & operasinya, relasi biner, relasi ekuivalensi, partisi, Poset, elemen ekstremal, diagram Hasse [1] Bab 6 & 9; [3] Bab 7 | **20%** |
| 5 | **Sub-CPMK-2.2** — Menerapkan aljabar Boolean & kombinatorika | 2.2.1 Ketepatan penyederhanaan fungsi Boolean; 2.2.2 Ketepatan perhitungan kombinatorial | Kriteria: ketepatan hasil; Teknik: latihan bertingkat | Kuliah & latihan; TM 150′ / PT 180′ / BM 180′ | Latihan bertingkat di LMS | Fungsi Boolean, bentuk normal, kaidah pencacahan, permutasi, kombinasi, pigeonhole, relasi rekurensi [1] Bab 12 & 8; [3] Bab 11 & 12 | — |
| 6 | **Sub-CPMK-3.1** — Menganalisis struktur graf dengan matriks representasi | 3.1.1 Ketepatan representasi adjacency matrix/list; 3.1.2 Ketepatan penelusuran BFS/DFS | Kriteria: ketepatan analisis; Teknik: latihan & kuis formatif | Ceramah & visualisasi; TM 150′ / PT 180′ / BM 180′ | Visualisasi graf interaktif di LMS | Terminologi graf, derajat simpul, isomorfisme, bipartit, keterhubungan, adjacency matrix & list, BFS/DFS [1] Bab 10; [7] Bab 1 | — |
| 7 | **Sub-CPMK-3.2** — Menerapkan pohon untuk optimasi lintasan jaringan | 3.2.1 Ketepatan MST Kruskal/Prim; 3.2.2 Ketepatan lintasan terpendek Dijkstra/Floyd–Warshall | Kriteria: ketepatan hasil & justifikasi; Teknik: studi kasus terstruktur | Case method; TM 150′ / PT 180′ / BM 180′ | Analisis kasus topologi jaringan di LMS | Pohon & sifatnya, spanning tree, MST Kruskal–Prim, lintasan Euler & sirkuit Hamilton, Dijkstra, Floyd–Warshall [1] Bab 11; [6] Bab 21–23 | — |
| **8** | **EVALUASI TENGAH SEMESTER (UTS)** | Ketuntasan CPMK-1, CPMK-2, CPMK-3 (tahap awal) | Kriteria: kunci jawaban terstandar; Teknik: ujian tertulis terjadwal | Ujian; TM 150′ | — | Materi pekan 1–7 | **30%** |
| 9 | **Sub-CPMK-4.1** — Mengonstruksi model DFA | 4.1.1 Kelengkapan 5-tuple DFA; 4.1.2 Ketepatan tabel transisi & diagram status | Kriteria: ketepatan konstruksi; Teknik: latihan terbimbing | Ceramah & konstruksi bersama; TM 150′ / PT 180′ / BM 180′ | Simulator DFA daring (JFLAP) | Alfabet, string, bahasa, definisi formal DFA, tabel transisi, diagram status, string acceptance [4] Bab 2; [5] Bab 1 | — |
| 10 | **Sub-CPMK-4.2** — Mengonstruksi model NFA & konversinya ke DFA | 4.2.1 Ketepatan konstruksi NFA; 4.2.2 Ketepatan subset construction | Kriteria: ketepatan konversi; Teknik: latihan terstruktur | Ceramah & latihan; TM 150′ / PT 180′ / BM 180′ | Latihan konversi di LMS | NFA, ε-transisi, ekuivalensi NFA–DFA, subset construction, pengantar ekspresi reguler [4] Bab 2 & 3; [5] Bab 1 | — |
| 11 | Penguatan CPMK-3 & CPMK-4 — studi kasus pemodelan graf & otomata | 4.3.1 Ketepatan pemodelan kasus; 4.3.2 Ketepatan justifikasi algoritma terpilih | Kriteria: ketajaman pemodelan; Teknik: kerja kelompok terpandu | PjBL / Case Method; TM 150′ / PT 180′ / BM 180′ | Konsultasi asinkron | Studi kasus: optimasi topologi jaringan, penjadwalan, validasi input berbasis FSA [6] Bab 21–23; [4] Bab 2 | — |
| **12** | **Sub-CPMK-4.2 (integrasi)** — Proyek terapan lanjut & presentasi antara | 4.4.1 Kelayakan model diskrit; 4.4.2 Kejelasan argumentasi formal | Kriteria: rubrik analitik (4 dimensi); Teknik: **Tugas 2** — laporan proyek + presentasi | PjBL / Presentasi; TM 150′ / PT 180′ / BM 180′ | Submit Tugas 2 via LMS | Integrasi logika–graf–otomata pada kasus nyata [1]; [6] | **20%** |
| 13 | Penyempurnaan proyek berdasarkan umpan balik | 4.4.3 Ketepatan revisi; 4.4.4 Kualitas dokumentasi | Kriteria: checklist revisi; Teknik: konsultasi klinis | PjBL / Konsultasi; TM 150′ / PT 180′ / BM 180′ | Konsultasi asinkron | Seluruh materi CPMK-3 & CPMK-4 | — |
| 14 | Review & konsolidasi seluruh CPMK | Ketepatan identifikasi kesenjangan pemahaman | Kriteria: kelengkapan peta konsep; Teknik: review bersama | Diskusi / Konsultasi; TM 150′ / PT 180′ / BM 180′ | Pembahasan soal terpilih di LMS | Rekapitulasi pekan 1–13 | — |
| 15 | Presentasi final / demonstrasi hasil | 4.4.5 Kualitas komunikasi formal; 4.4.6 Penguasaan saat tanya jawab | Kriteria: rubrik presentasi; Teknik: presentasi tim | Presentasi & pleno; TM 150′ / PT 180′ / BM 180′ | Unggah slide & rekaman | Seluruh materi CPMK-1 s.d. CPMK-4 | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS)** | Ketuntasan komprehensif CPMK-1 s.d. CPMK-4 | Kriteria: kunci jawaban & rubrik esai; Teknik: ujian komprehensif | Ujian; TM 150′ | — | Materi pekan 1–15 | **30%** |
| | **TOTAL BOBOT PENILAIAN** | | | | | | **100%** |

**Keterangan waktu:** TM = tatap muka (1 SKS = 50 menit/pekan); PT = penugasan terstruktur (1 SKS = 60 menit/pekan); BM = belajar mandiri (1 SKS = 60 menit/pekan). Mata kuliah ini tidak memiliki komponen praktikum (P = 0); latihan otomata dilakukan dengan simulator daring (JFLAP) yang dijalankan pada perangkat mahasiswa.

---

## HALAMAN 5 — LAMPIRAN 1: NASKAH TUGAS 1 + RUBRIK (PORTRAIT)

### A. Naskah Tugas 1 — Kuis & Problem Solving "Logika Formal dan Struktur Relasi"

**Pekan:** 4 | **Bobot:** 20% | **CPMK:** CPMK-1 & CPMK-2 | **Bentuk:** Individu | **Durasi:** 150 menit

**Instruksi:**

1. Susun tabel kebenaran untuk $((p \to q) \land (q \to r)) \to (p \to r)$ dan tentukan apakah formula tersebut tautologi. Buktikan kesimpulan Anda menggunakan hukum aljabar logika tanpa tabel kebenaran.
2. Periksa validitas argumen berikut dengan aturan inferensi. Sebutkan aturan yang dipakai pada setiap langkah.
   > Jika sistem terhubung ke jaringan, maka *firewall* aktif. *Firewall* tidak aktif. Karena itu, sistem tidak terhubung ke jaringan.
3. Nyatakan pernyataan berikut dalam logika predikat, lalu tentukan nilai kebenarannya pada domain bilangan bulat.
   (a) "Setiap bilangan bulat genap dapat dinyatakan sebagai jumlah dua bilangan prima."
   (b) "Terdapat bilangan bulat $n$ sehingga $n^2 = n$."
4. Buktikan dengan **induksi matematika** bahwa untuk setiap $n \ge 1$ berlaku $\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$. Tuliskan basis, hipotesis induksi, dan langkah induksi secara eksplisit.
5. Diberikan $A = \{1,2,3,4,6,12\}$ dengan relasi "membagi" ($a \mid b$). Tunjukkan bahwa $(A, \mid)$ adalah Poset, gambarkan diagram Hasse-nya, dan tentukan elemen maksimal, minimal, terbesar, serta terkecil.
6. Diberikan relasi $R$ pada $\{1,2,3,4\}$ dengan $R = \{(1,1),(2,2),(3,3),(4,4),(1,2),(2,1)\}$. Periksa apakah $R$ merupakan relasi ekuivalensi, lalu tentukan kelas-kelas ekuivalensinya.

**Ketentuan:** dikerjakan individual; seluruh langkah pembuktian wajib ditulis; jawaban akhir tanpa langkah dinilai maksimal 40% poin butir; kalkulator tidak diperlukan.

**Deliverable:** berkas PDF jawaban bertahap + diagram Hasse.

### B. Rubrik Penilaian Tugas 1 (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Ketepatan logika proposisi (25%)** | Tabel kebenaran lengkap; penyederhanaan aljabar logika valid pada setiap langkah | Tabel benar; satu langkah penyederhanaan diringkas | Ada kesalahan hukum logika pada satu butir | Tabel kebenaran salah atau tidak lengkap |
| **2. Ketepatan inferensi & kuantifikasi (30%)** | Seluruh aturan inferensi disebut dan diterapkan tepat; kuantor dan negasi benar | Aturan tepat; 1–2 kekeliruan notasi kuantor | Argumen valid tetapi justifikasi aturan tidak lengkap | Tidak mampu membedakan aturan inferensi |
| **3. Ketepatan pembuktian induksi (30%)** | Basis, hipotesis, dan langkah induksi lengkap serta terjustifikasi pada setiap transisi | Ketiga komponen ada; satu transisi aljabar diringkas | Langkah induksi ada tetapi basis atau hipotesis tidak dinyatakan | Tidak memahami struktur induksi |
| **4. Ketepatan analisis relasi & Poset (15%)** | Sifat relasi diuji lengkap; diagram Hasse benar; elemen ekstremal diidentifikasi tepat | Sifat relasi benar; diagram kurang rapi | Satu sifat relasi keliru; elemen ekstremal sebagian benar | Tidak mampu menguji sifat relasi |

---

## HALAMAN 6 — LAMPIRAN 2: NASKAH UTS + RUBRIK (PORTRAIT)

### A. Naskah UTS — Ujian Tertulis Logika Formal, Struktur Diskrit, dan Graf

**Pekan:** 8 | **Bobot:** 30% | **CPMK:** CPMK-1, CPMK-2, CPMK-3 | **Bentuk:** Individu, *closed book* | **Durasi:** 150 menit

**Struktur soal:**

| Bagian | Bentuk | Jumlah | Poin | Cakupan |
|:--:|---|:--:|:--:|---|
| I | Uraian singkat (logika proposisi & predikat) | 4 | 25 | CPMK-1 |
| II | Uraian pembuktian (induksi & verifikasi algoritma) | 2 | 20 | CPMK-1 |
| III | Uraian terstruktur (relasi, Poset, Boolean, kombinatorika) | 3 | 30 | CPMK-2 |
| IV | Studi kasus graf (representasi & penelusuran) | 2 | 25 | CPMK-3 |

**Contoh butir Bagian IV:**
> Sebuah jaringan kampus terdiri atas 6 ruang server yang dihubungkan kabel berbiaya tetap. Matriks ketetanggaan (adjacency matrix) jarak antar-ruang (dalam meter) adalah:
>
> $$A = \begin{pmatrix} 0 & 4 & 0 & 0 & 0 & 8 \\ 4 & 0 & 8 & 0 & 0 & 11 \\ 0 & 8 & 0 & 7 & 0 & 4 \\ 0 & 0 & 7 & 0 & 9 & 14 \\ 0 & 0 & 0 & 9 & 0 & 10 \\ 8 & 11 & 4 & 14 & 10 & 0 \end{pmatrix}$$
>
> (a) Gambarkan graf tak berarah yang diwakili matriks tersebut dan tentukan derajat setiap simpul. (10 poin)
> (b) Tentukan *Minimum Spanning Tree*-nya dengan algoritma Kruskal, tuliskan urutan sisi yang dipilih, dan hitung total panjang kabel minimum. (15 poin)

**Ketentuan:** *closed book*; seluruh langkah wajib ditulis; jawaban akhir tanpa langkah dinilai maksimal 40% poin butir.

### B. Rubrik Penilaian UTS (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Penguasaan konsep formal (25%)** | Definisi dan teorema digunakan tepat; notasi logika sempurna | Tepat dengan 1–2 kekeliruan notasi | Konsep dasar dipahami; ada kesalahan definisi | Salah memahami konsep inti |
| **2. Keruntutan pembuktian (30%)** | Pembuktian sistematis dari premis ke konklusi; setiap langkah terjustifikasi | Sebagian besar runtut; ada lompatan kecil | Pembuktian terputus-putus | Tidak ada alur pembuktian |
| **3. Ketepatan hasil & justifikasi algoritma (30%)** | Seluruh hasil benar; pemilihan algoritma dan urutan langkah terjustifikasi | Hasil benar; justifikasi ringkas | Sebagian besar hasil keliru atau algoritma tidak tepat | Hasil tidak relevan |
| **4. Kelengkapan & kerapian jawaban (15%)** | Seluruh butir dijawab lengkap, diagram berlabel, terbaca | Seluruh butir dijawab; beberapa kurang rinci | Ada butir tidak dijawab | Banyak butir kosong |

---

## HALAMAN 7 — LAMPIRAN 3: NASKAH TUGAS 2 + RUBRIK (PORTRAIT)

### A. Naskah Tugas 2 — Proyek Terapan "Pemodelan Diskrit untuk Sistem Nyata"

**Pekan:** 12 | **Bobot:** 20% | **CPMK:** CPMK-3 & CPMK-4 | **Bentuk:** Kelompok 3–4 orang | **Durasi:** 3 pekan

**Instruksi:**

1. Pilih **satu** dari tiga tema berikut:
   - **T1:** Pemodelan topologi jaringan kampus sebagai graf berbobot, penentuan MST untuk perencanaan kabel, dan lintasan terpendek antar-*gateway* dengan Dijkstra.
   - **T2:** Pemodelan penjadwalan mata kuliah/ujian sebagai masalah pewarnaan graf, dengan analisis bilangan kromatik dan pembuktian batas bawahnya.
   - **T3:** Perancangan *Finite State Automaton* (DFA) untuk validasi format masukan sistem (mis. NIM, alamat surel kampus, kode mata kuliah) beserta konversi NFA→DFA dan uji string.
2. Sajikan **formalisasi matematis** lengkap: definisi himpunan, relasi, graf $G=(V,E)$, atau 5-tuple otomata $M=(Q,\Sigma,\delta,q_0,F)$.
3. Sertakan **minimal dua contoh kerja manual** yang dapat diverifikasi langkah demi langkah.
4. Buat **visualisasi** (diagram graf berlabel bobot, diagram Hasse, atau diagram status otomata).
5. Analisis **kompleksitas** algoritma yang dipakai (mis. $O(E \log V)$ untuk Kruskal) dan **keterbatasan model** (asumsi, skala, kasus tepi).
6. Format: laporan 10–14 halaman, sitasi IEEE minimal 6 rujukan (≥ 2 buku teks matematika diskrit), font 11 pt, spasi 1,15.
7. Wajib menyertakan **Deklarasi Transparansi AI** dan pembagian peran tim.

**Deliverable:** laporan PDF + lampiran perhitungan + slide ringkas 6 halaman.

### B. Rubrik Penilaian Tugas 2 (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Ketepatan formalisasi model (30%)** | Model diskrit didefinisikan lengkap dan konsisten; seluruh asumsi dinyatakan | Model benar; satu komponen kurang eksplisit | Model benar sebagian; asumsi tidak jelas | Model tidak terbentuk |
| **2. Ketepatan algoritma & verifikasi manual (25%)** | ≥ 2 contoh kerja benar, langkah algoritma terverifikasi | Contoh benar; verifikasi sebagian | Satu contoh benar; verifikasi tidak ada | Hasil tidak dapat diverifikasi |
| **3. Kualitas visualisasi & interpretasi (25%)** | Diagram akurat dan berlabel; interpretasi menghubungkan model dengan sistem nyata | Diagram benar; interpretasi memadai | Diagram kurang informatif; interpretasi dangkal | Tanpa visualisasi |
| **4. Analisis kompleksitas & keterbatasan (20%)** | Kompleksitas dan keterbatasan dianalisis kritis; laporan rapi; ≥ 6 rujukan IEEE | Analisis memadai; 4–5 rujukan | Analisis umum; < 4 rujukan | Tanpa analisis |

---

## HALAMAN 8 — LAMPIRAN 4: NASKAH UAS + RUBRIK (PORTRAIT)

### A. Naskah UAS — Evaluasi Komprehensif Matematika Diskrit

**Pekan:** 16 | **Bobot:** 30% | **CPMK:** CPMK-1, CPMK-2, CPMK-3, CPMK-4 | **Bentuk:** Individu | **Durasi:** 150 menit

**Struktur soal:**

| Bagian | Bentuk | Poin | Cakupan |
|:--:|---|:--:|---|
| I | Uraian: logika, induksi, dan struktur diskrit | 25 | CPMK-1, CPMK-2 |
| II | Uraian: graf, pohon, dan lintasan terpendek | 25 | CPMK-3 |
| III | Studi kasus terintegrasi: konstruksi dan analisis otomata | 30 | CPMK-4 |
| IV | Pemodelan terbuka: perancangan model diskrit untuk kasus baru | 20 | CPMK-3, CPMK-4 |

**Contoh butir Bagian III:**
> Diberikan bahasa $L = \{w \in \{0,1\}^* \mid w \text{ memuat substring } "01" \text{ tepat satu kali}\}$.
> (a) Konstruksi DFA minimal yang menerima $L$; tuliskan 5-tuple lengkap dan tabel transisinya. (12 poin)
> (b) Uji DFA tersebut terhadap string `0010`, `0101`, dan `111`. Tunjukkan jejak transisi setiap string. (10 poin)
> (c) Konstruksi NFA untuk bahasa yang sama, lalu konversikan ke DFA dengan *subset construction*. Bandingkan jumlah status kedua model. (8 poin)

**Ketentuan:** *closed book*; seluruh langkah dan justifikasi wajib ditulis.

### B. Rubrik Penilaian UAS (Total 100 poin)

| Dimensi (Bobot) | Sangat Baik (86–100) | Baik (76–85) | Cukup (60–75) | Kurang (< 60) |
|---|---|---|---|---|
| **1. Penguasaan konsep komprehensif (25%)** | Mengaitkan logika–struktur–graf–otomata secara utuh dan koheren | Konsep benar; keterkaitan sebagian | Konsep terpisah-pisah | Salah konsep mendasar |
| **2. Ketepatan formalisasi & komputasi (30%)** | Seluruh definisi formal dan perhitungan tepat; notasi konsisten | 1–2 kekeliruan minor | Beberapa kekeliruan yang memengaruhi hasil | Formalisasi tidak dapat diikuti |
| **3. Kedalaman analisis & justifikasi (30%)** | Justifikasi setiap pilihan model/algoritma; implikasi perubahan parameter dianalisis | Justifikasi tepat; kurang mendalam | Justifikasi deskriptif | Tanpa justifikasi |
| **4. Struktur & komunikasi matematis (15%)** | Uraian runtut; definisi dipakai tepat; kesimpulan eksplisit | Uraian jelas; kesimpulan ada | Uraian kurang runtut | Tidak terstruktur |

---

## HALAMAN 9 — LEMBAR VALIDASI DAN PENGESAHAN (PORTRAIT)

| Memvalidasi,<br>Unit Penjaminan Mutu FSTI | Malang, 07 November 2026<br>Dosen Pengampu Mata Kuliah |
|:---:|:---:|
| ..........................<br>NUPTK. .......................... | ..........................<br>NIDN/NUPTK. .......................... |

<br>

| Mengesahkan,<br>Ketua Program Studi S1 Sistem dan Teknologi Informasi |
|:---:|
| ..........................<br>NUPTK. .......................... |

---

## LAMPIRAN TEKNIS — KESESUAIAN DENGAN TEMPLATE MASTER RPS FSTI UWG

### A. Pemetaan 18 Tag Nilai Tunggal (`{{...}}`)

| Tag | Nilai Terisi |
|---|---|
| `{{namamk}}` | Matematika Diskrit dan Logika |
| `{{kodemk}}` | STI-204 |
| `{{rumpunmk}}` | Matematika & Sains Komputasi (Core STI) |
| `{{skst}}` | 3 |
| `{{sksp}}` | 0 |
| `{{sms}}` | 2 (Genap) |
| `{{tglsusun}}` | 07 November 2026 |
| `{{pengembangrps}}` | Tim Pengembang RPS SISTEKIN |
| `{{koordinatormk}}` | Koordinator RMK Matematika & Sains Komputasi |
| `{{ketuaprodi}}` | Ketua Prodi SISTEKIN FSTI |
| `{{kodeprodi}}` | B4.5.2.RPS-STI204 |
| `{{prodi}}` | Sistem dan Teknologi Informasi |
| `{{namadosen}}` | Tim Pengampu Rumpun Matematika & Sains Komputasi |
| `{{nuptk}}` | .......................... |
| `{{deskripsimk}}` | Lihat Bagian G Halaman 2 |
| `{{bahankajian}}` | BK-IS10, BK-IS11 — lihat Bagian H Halaman 2 |
| `{{dosenpengampu}}` | Tim Pengampu Rumpun Matematika & Sains Komputasi (Core STI) |
| `{{mkprasyarat}}` | STI-103 |

### B. Pemetaan 25 Tag Blok Isi (`[...]`)

| Tag | Lokasi | Sumber Isi |
|---|---|---|
| `[nocpl]`, `[cpl]` | Hal 2 | Bagian C (2 baris CPL: CPL-05 (P1), CPL-02 (KU1)) |
| `[nocpmk]`, `[cpmk]` | Hal 2 | Bagian D (4 CPMK) |
| `[nosubcpmk]`, `[subcpmk]` | Hal 2 | Bagian E (8 Sub-CPMK) |
| `[tabelkolerasi]` | Hal 2 | Bagian F (matriks CPL×CPMK, total 100%) |
| `[pustakautama]` | Hal 2 | Bagian I — 3 pustaka utama |
| `[pustakapendukung]` | Hal 2 | Bagian I — 5 pustaka pendukung |
| `[mingguke]` … `[bobot_nilai]` | Hal 3–4 | Kolom 1–8 tabel 16 pekan |
| `[penugasan1]`, `[rubriktugas1]` | Hal 5 | Lampiran 1 |
| `[soaluts]`, `[rubrikuts]` | Hal 6 | Lampiran 2 |
| `[tugas2]`, `[rubriktugas2]` | Hal 7 | Lampiran 3 |
| `[soaluas]`, `[rubrikuas]` | Hal 8 | Lampiran 4 |

### C. Pernyataan Kepatuhan Skema Asesmen

| Komponen | Pekan | Bobot | Target CPMK | Status |
|:---:|:---:|:---:|:---:|:---:|
| Tugas 1 | 4 | 20% | CPMK-1 & CPMK-2 | Sesuai |
| UTS | 8 | 30% | CPMK-1, CPMK-2, CPMK-3 | Sesuai |
| Tugas 2 | 12 | 20% | CPMK-3 & CPMK-4 | Sesuai |
| UAS | 16 | 30% | CPMK-1 s.d. CPMK-4 (komprehensif) | Sesuai |
| **Total** | | **100%** | | **Lulus** |

### D. Kepatuhan Boundary Guardrails (Dokumen 043)

| Kategori | Isi |
|---|---|
| **In-Scope (diajarkan)** | Logika proposisi, logika predikat, aljabar Boolean formal, teori himpunan, relasi dan fungsi diskrit, kombinatorika, teori graf, pohon (*tree*) |
| **Out-of-Scope (tidak diajarkan)** | Perancangan gerbang fisik mikroprosesor (*hardware wiring*), pengodean struktur data dinamis dengan manajemen memori, analisis diferensial–integral |
| **Handoff Anchor** | Menyerahkan struktur memori fisik dan implementasi graf ke `FST-203` / `STI-308`; kalkulus diferensial–integral ke `STI-102`; rangkaian gerbang ke `STI-103` |

---

*Dokumen ini disusun dari Dokumen 005, 007, 043, 003, 008, dan 018. Rujukan pustaka merupakan usulan standar bidang ilmu dan tetap terbuka untuk validasi KBK/GPM. Dokumen pendamping: `058_2_SAP_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md`, `058_3_OUTLINE_MODUL_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md`, `058_4_RENCANA_EVALUASI_ASESMEN_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md`, `058_5_RUBRIK_PENILAIAN_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md`.*
