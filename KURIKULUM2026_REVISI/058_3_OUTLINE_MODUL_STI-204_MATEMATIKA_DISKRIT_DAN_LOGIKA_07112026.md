# 058_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA (*Discrete Mathematics and Logic*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI204`  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** `058_1_RPS_STI-204_...md` · `058_2_SAP_STI-204_...md` · Dok 007 §9 · Dok 043.

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Buku Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Matematika Diskrit dan Logika Komputasi untuk Rekayasa Sistem Informasi & Kecerdasan Artifisial* |
| **Kode & Bobot MK** | `STI-204` · 3 SKS Teori (`TM 150'`, `PT 180'`, `BM 180'`) · Semester 2 · Prasyarat: `STI-103` |
| **CPL & BoK Didukung** | `CPL-05` (`P1`: 80%), `CPL-02` (`KU1`: 20%) [Level *Introduce*] · `BK-IS10` (*Applied Mathematics and Logic*), `BK-IS11` (*Programming Fundamentals*) |
| **Target Tebal Naskah Utuh** | 14 Bab Materi Inti + 2 Unit Evaluasi Komprehensif ($\pm 195\text{–}235\text{ halaman}$ A4/B5 dilengkapi contoh bukti 2-kolom, tabel jejak algoritma graf, dan diagram transisi FSA) |
| **Anatomi Baku Setiap Bab** | (1) *Sub-CPMK & Indikator*; (2) *Vignette Masalah Sistem Informasi/AI*; (3) *Definisi, Teorema, & Contoh Bukti Langkah demi Langkah*; (4) *Panduan Visualisasi Peramban Ringan*; (5) *Kotak Boundary Guardrail & Handoff*; (6) *Rangkuman Simbol & Hukum*; (7) *Soal Latihan Mandiri Berjenjang (10–14 Soal)*. |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen Terkait |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Logika Formal, Inferensi, & Induksi** | **Bab 1** | Logika Proposisional, Tabel Kebenaran, & Hukum Ekuivalensi Aljabar Logika | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Aturan Inferensi Formal, Prinsip Resolusi, & Logika Predikat (*FOL*) | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | Tugas 1 (20%) |
| | **Bab 3** | Metode Pembuktian, Induksi Matematika, & Verifikasi Kebenaran Algoritma | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Relasi, Poset, Aljabar Boolean, & Kombinatorika** | **Bab 4** | Himpunan, Relasi Ekuivalensi, *Poset*, Diagram Hasse, & Urutan Topologis | Mg 4 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 5** | Fungsi Diskrit (*Hashing*) & Aljabar Boolean Formal pada Logika Query | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | UTS (30%) |
| | **Bab 6** | Kombinatorika Terapan: Pencacahan, *Pigeonhole*, Permutasi, & Kombinasi | Mg 6 | `CPMK-2` | `Sub-CPMK-2.2` | UTS (30%) |
| | **Bab 7** | Pemodelan & Penyelesaian Relasi Rekurensi Linier Homogen | Mg 7 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Paket Latihan Pembuktian & Pemodelan Struktur Diskrit (Persiapan UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| **Bagian III:<br>Teori Graf & Pohon untuk Optimasi Jaringan** | **Bab 8** | Dasar Teori Graf, Graf Khusus, Isomorfisme, & *Adjacency Matrix* | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 9** | Penelusuran Lintasan, Euler/Hamilton, & Algoritma *Shortest Path* | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 10** | Teori Pohon (*Tree*) & Optimasi Jaringan *Minimum Spanning Tree* (*MST*) | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (20%) |
| | **Bab 11** | Pewarnaan Graf (*Graph Coloring* Jadwal) & Pohon Kode Optimal *Huffman* | Mg 12 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Bahasa Formal & Otomata Berhingga (FSA)** | **Bab 12** | Bahasa Formal, Ekspresi Reguler Dasar, & Konstruksi DFA Pengenal Pola | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13** | *Nondeterministic Finite Automata* (NFA/$\varepsilon$-NFA) & Konversi *Subset* | Mg 14 | `CPMK-4` | `Sub-CPMK-4.2` | UAS (30%) |
| | **Bab 14** | Minimasi Status DFA & Pemodelan Transisi Status Sistem Komputasi | Mg 15 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Paket Studi Kasus Graf, Pohon, & Konstruksi Otomata (Persiapan UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2` & Sintesis* | *UAS (30%)* |

---

## 3. RINCIAN OUTLINE SUBSTANSI TIAP BAB

### BAGIAN I — LOGIKA FORMAL, INFERENSI, DAN INDUKSI (`CPMK-1`)

#### BAB 1: Logika Proposisional, Tabel Kebenaran, & Hukum Ekuivalensi Aljabar Logika (Pekan 1)
* **Sub-CPMK:** `Sub-CPMK-1.1` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  1.1 Dari Sirkuit Biner (`STI-103`) Menuju Penalaran Simbolik Formal (`STI-204`)  
  1.2 Proposisi Atomik dan Penghubung Logika (`¬, ∧, ∨, ⊕`)  
  1.3 Implikasi ($p \to q$), Bikondisional ($p \leftrightarrow q$), serta Konvers, Invers, dan Kontraposisi dalam Spesifikasi Aturan Bisnis  
  1.4 Tabel Kebenaran, Tautologi, Kontradiksi, dan Kontingensi  
  1.5 Hukum-Hukum Aljabar Logika dan Pembuktian Ekuivalensi Simbolik Tanpa Tabel Kebenaran
* **Guardrail Bab 1:** Tidak menggambar ulang rangkaian gerbang silikon/ALU yang sudah tuntas di `STI-103`.
* **Latihan Bab 1:** 12 soal formalisasi kalimat persyaratan sistem dan pembuktian ekuivalensi aljabar logika.

#### BAB 2: Aturan Inferensi Formal, Prinsip Resolusi, & Logika Predikat (*FOL*) (Pekan 2)
* **Sub-CPMK:** `Sub-CPMK-1.1` & `Sub-CPMK-1.2` (C3/C4) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  2.1 Struktur Argumen Valid dan Aturan Inferensi (*Modus Ponens, Modus Tollens, Silogisme Hipotetis, Silogisme Disjungtif, Penjumlahan, Penyederhanaan*)  
  2.2 Deteksi Sesat Pikir Logis (*Fallacies*: *Affirming the Conclusion* & *Denying the Hypothesis*)  
  2.3 Bentuk Klausa dan Aturan Inferensi **Resolusi** sebagai Fondasi Penalaran Otomatis AI  
  2.4 Logika Predikat Orde Pertama (*First-Order Logic*): Predikat, Domain Pembicaraan, Kuantor Universal ($\forall$), dan Kuantor Eksistensial ($\exists$)  
  2.5 Kuantor Bersarang, Hukum De Morgan untuk Negasi Kuantor, serta Aturan Inferensi Berkuantor (*UI, UG, EI, EG*)
* **Konteks Kasus TI:** Memverifikasi konsistensi aturan kebijakan kontrol akses berbasis peran (*Role-Based Access Control Policy*) dan mengantar konsep *Knowledge Base* untuk `STI-307 Sistem Cerdas`.
* **Latihan Bab 2:** 12 soal bukti validitas argumen 2-kolom dan negasi kuantor bersarang.

#### BAB 3: Metode Pembuktian, Induksi Matematika, & Verifikasi Kebenaran Algoritma (Pekan 3)
* **Sub-CPMK:** `Sub-CPMK-1.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  3.1 Anatomi Teorema dan Teknik Pembuktian: Bukti Langsung, Bukti Kontraposisi, Bukti Kontradiksi, & Contoh Penyangkal (*Counterexample*)  
  3.2 Prinsip Induksi Matematika Biasa (*Basis Step, Inductive Hypothesis, Inductive Step*) pada Rumus Deret & Ketaksamaan  
  3.3 Induksi Matematika Kuat (*Strong Induction*) dan Prinsip Pengurutan Rapi (*Well-Ordering*)  
  3.4 Definisi Rekursif dan Pembuktian Kebenaran Algoritma Iteratif (*Loop Invariant*) serta Rekursif Sederhana
* **Latihan Bab 3 & Panduan Tugas 1:** 10 soal pembuktian induksi matematika dan verifikasi algoritma + panduan penyelesaian **RTM-1 (Tugas 1)**.

---

### BAGIAN II — RELASI, POSET, ALJABAR BOOLEAN, DAN KOMBINATORIKA (`CPMK-2`)

#### BAB 4: Himpunan, Relasi Ekuivalensi, *Poset*, Diagram Hasse, & Urutan Topologis (Pekan 4)
* **Sub-CPMK:** `Sub-CPMK-2.1` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  4.1 Operasi Aljabar Himpunan, Himpunan Kuasa $\mathcal{P}(A)$, dan Perkalian Kartesian $A \times B$  
  4.2 Relasi Biner, Representasi Matriks 0–1, serta Sifat Refleksif, Simetris, Antisimetris, dan Transitif  
  4.3 Relasi Ekuivalensi, Kelas Ekuivalensi, dan Partisi Himpunan (Contoh: Kongruensi Modulo $m$)  
  4.4 Himpunan Terurut Parsial (*Partially Ordered Set / Poset*) dan Konstruksi **Diagram Hasse**  
  4.5 Elemen Maksimal/Minimal dan Algoritma *Topological Sorting* pada Penjadwalan Ketergantungan Tugas
* **Konteks Kasus TI:** Pemodelan urutan kompilasi paket perangkat lunak (*dependency graph*) dan pengelompokan partisi rekaman duplikat.
* **Latihan Bab 4:** 10 soal pemeriksaan sifat relasi, kelas ekuivalensi, dan konstruksi Diagram Hasse/*topological sort*.

#### BAB 5: Fungsi Diskrit (*Hashing*) & Aljabar Boolean Formal pada Logika Query (Pekan 5)
* **Sub-CPMK:** `Sub-CPMK-2.1` & `Sub-CPMK-2.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  5.1 Fungsi Diskrit, Sifat Injektif, Surjektif, Bijektif, Komposisi, dan Invers Fungsi  
  5.2 Fungsi *Floor*, *Ceiling*, dan Prinsip Matematis Fungsi Pemetaan *Modulo Hashing*  
  5.3 Struktur Aksiomatik Aljabar Boolean $(B, +, \cdot, ')$ dan Prinsip Dualitas  
  5.4 Bentuk Normal Disjungtif (DNF / *Sum-of-Minterms*) dan Bentuk Normal Konjungtif (CNF / *Product-of-Maxterms*)  
  5.5 Penerapan Hukum Aljabar Boolean untuk Menyederhanakan Ekspresi Predikat Seleksi Query Basis Data
* **Guardrail Bab 5:** Fokus pada ekspresi logika relasional abstrak ($\sigma_{P_1 \wedge (P_2 \vee P_3)}$); koding sintaks SQL fisik diserahkan ke `FST-207 Sistem Basis Data`.
* **Latihan Bab 5:** 10 soal analisis bijeksi/*hashing* dan penyederhanaan ekspresi predikat kueri kompleks.

#### BAB 6: Kombinatorika Terapan: Pencacahan, *Pigeonhole*, Permutasi, & Kombinasi (Pekan 6)
* **Sub-CPMK:** `Sub-CPMK-2.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  6.1 Kaidah Penjumlahan, Kaidah Perkalian, dan Pencacahan dengan Diagram Pohon Keputusan  
  6.2 Prinsip Inklusi-Eksklusi (*Inclusion-Exclusion*) untuk Kardinalitas Gabungan Himpunan Data Beririsan  
  6.3 Prinsip Sarang Merpati (*Pigeonhole Principle*) dan Bukti Matematis *Hash/Port Collision*  
  6.4 Permutasi dan Kombinasi (Tanpa Pengulangan & Dengan Pengulangan) serta Teorema Binomial  
  6.5 Aplikasi Kombinatorika pada Estimasi Ruang Kunci Keamanan dan Kombinasi Atribut/Indeks Query
* **Latihan Bab 6:** 12 soal studi masalah kombinatorika sistem informasi.

#### BAB 7: Pemodelan & Penyelesaian Relasi Rekurensi Linier Homogen (Pekan 7)
* **Sub-CPMK:** `Sub-CPMK-2.1` & `Sub-CPMK-2.2` (C3) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  7.1 Memodelkan Proses Bertahap & Algoritma Rekursif dengan Relasi Rekurensi  
  7.2 Penyelesaian Relasi Rekurensi dengan Substitusi Mundur (*Backward Substitution*)  
  7.3 Relasi Rekurensi Linier Homogen Berkoefisien Konstan: Metode Persamaan Karakteristik (Akar Berbeda & Akar Kembar)  
  7.4 Pengantar Relasi Rekurensi *Divide-and-Conquer* sebagai Jembatan menuju Analisis Kompleksitas di `FST-203`
* **Latihan Bab 7 & Unit Evaluasi E1:** 10 soal pemodelan & penyelesaian relasi rekurensi + **Paket Simulasi Lengkap UTS (`CPMK-2`)**.

---

### BAGIAN III — TEORI GRAF DAN POHON UNTUK OPTIMASI JARINGAN (`CPMK-3`)

#### BAB 8: Dasar Teori Graf, Graf Khusus, Isomorfisme, & *Adjacency Matrix* (Pekan 9)
* **Sub-CPMK:** `Sub-CPMK-3.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  8.1 Model Graf Tak Berarah, Graf Berarah (*Digraph*), dan Graf Berbobot dalam Sistem Informasi  
  8.2 Terminologi Derajat Simpul, Teorema Jabat Tangan, dan Kelas Graf Khusus (Lengkap $K_n$, Siklus $C_n$, Roda $W_n$, Hiperkubus $Q_n$)  
  8.3 Graf Bipartit dan Pemodelan Masalah Penugasan / Rekomendasi Dua Sisi  
  8.4 Representasi Matriks: **Adjacency Matrix**, **Incidence Matrix**, dan Makna Perpangkatan $A^k$ dalam Menghitung Lintasan  
  8.5 Isomorfisme Graf dan Pengujian Invarian Struktural
* **Guardrail Bab 8:** Tidak menulis kode *class/struct pointer* graf di bahasa pemrograman (`FST-203 Struktur Data dan Algoritma`).
* **Latihan Bab 8:** 10 soal *Adjacency Matrix*, perpangkatan matriks lintasan, dan uji isomorfisme.

#### BAB 9: Penelusuran Lintasan, Euler/Hamilton, & Algoritma *Shortest Path* (Pekan 10)
* **Sub-CPMK:** `Sub-CPMK-3.1` (C4) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  9.1 Jalan (*Walk*), Jejak (*Trail*), Lintasan (*Path*), Sirkuit, dan Komponen Terhubung / Terhubung Kuat  
  9.2 Penelusuran Sistematis *Breadth-First Search* (BFS) dan *Depth-First Search* (DFS) secara Matematis  
  9.3 Lintasan & Sirkuit Euler (Teorema Derajat Genap) vs Lintasan & Sirkuit Hamilton (*Traveling Salesperson Problem* Pengantar)  
  9.4 Algoritma **Dijkstra** untuk Lintasan Terpendek dari Satu Sumber (*Single-Source Shortest Path*)  
  9.5 Algoritma **Floyd-Warshall** Berbasis Matriks untuk Lintasan Terpendek Semua Pasangan Simpul
* **Konteks Kasus TI:** Penentuan jalur pengiriman paket data berlatensi total minimum pada topologi jaringan *backbone* antar-pusat data.
* **Latihan Bab 9:** 10 soal analisis Euler/Hamilton dan penelusuran tabel *Dijkstra* & *Floyd-Warshall*.

#### BAB 10: Teori Pohon (*Tree*) & Optimasi Jaringan *Minimum Spanning Tree* (*MST*) (Pekan 11)
* **Sub-CPMK:** `Sub-CPMK-3.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  10.1 Definisi dan Karakterisasi Matematis Pohon ($n$ Simpul, $n-1$ Sisi, Jalur Tunggal Unik)  
  10.2 Pohon Berakar, Pohon $m$-ary & Biner, serta Tinggi dan Batas Jumlah Daun  
  10.3 Penelusuran Pohon (*Preorder, Inorder, Postorder*) dan Evaluasi Pohon Ekspresi Notasi Polandia  
  10.4 Pohon Merentang (*Spanning Tree*) dan Pohon Merentang Minimum (*Minimum Spanning Tree / MST*)  
  10.5 Analisis & Penelusuran **Algoritma Kruskal** dan **Algoritma Prim** pada Perancangan Infrastruktur Jaringan
* **Latihan Bab 10:** 10 soal sifat pohon biner, pohon ekspresi, dan konstruksi *MST Kruskal/Prim*.

#### BAB 11: Pewarnaan Graf (*Graph Coloring* Jadwal) & Pohon Kode Optimal *Huffman* (Pekan 12)
* **Sub-CPMK:** `Sub-CPMK-3.1` & `Sub-CPMK-3.2` (C4) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  11.1 Graf Planar, Rumus Euler $v - e + r = 2$, dan Pengantar Teorema Empat Warna  
  11.2 Pewarnaan Simpul Graf, Bilangan Kromatik $\chi(G)$, dan Algoritma Heuristik *Welsh-Powell*  
  11.3 Studi Kasus Pemodelan Penjadwalan Ujian / Pemeliharaan Server Bebas Konflik dengan Pewarnaan Graf  
  11.4 Kode Prefiks (*Prefix Codes*) dan Konstruksi Pohon Biner Optimal **Huffman** untuk Kompresi Data
* **Latihan Bab 11 & Panduan Tugas 2:** 10 soal pewarnaan graf jadwal & konstruksi kode *Huffman* + panduan finalisasi **RTM-2 (Tugas 2)**.

---

### BAGIAN IV — BAHASA FORMAL DAN OTOMATA BERHINGGA (`CPMK-4`)

#### BAB 12: Bahasa Formal, Ekspresi Reguler Dasar, & Konstruksi DFA Pengenal Pola (Pekan 13)
* **Sub-CPMK:** `Sub-CPMK-4.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  12.1 Alfabet ($\Sigma$), String ($w$), Konkatenasi, Kleene Closure ($\Sigma^*$), dan Bahasa Formal ($L$)  
  12.2 Pengantar Ekspresi Reguler (*Regular Expressions*) dalam Pencocokan Pola Teks  
  12.3 Definisi Formal 5-Tupel *Deterministic Finite Automata* (DFA) $M = (Q, \Sigma, \delta, q_0, F)$  
  12.4 Representasi Diagram Transisi Status, Tabel Transisi, dan Fungsi Transisi Diperluas $\hat{\delta}(q_0, w)$  
  12.5 Teknik Perancangan DFA: Pelacakan Sisa Modulo, Pencocokan Substring, dan Penanganan *Dead/Trap State*
* **Latihan Bab 12:** 10 soal konstruksi 5-tupel DFA pengenal pola kode dan token sistem.

#### BAB 13: *Nondeterministic Finite Automata* (NFA/$\varepsilon$-NFA) & Konversi *Subset* (Pekan 14)
* **Sub-CPMK:** `Sub-CPMK-4.2` (C4) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  13.1 Konsep Nondeterminisme pada Otomata dan Perbedaannya dengan DFA  
  13.2 Definisi Formal NFA ($\delta: Q \times \Sigma \to \mathcal{P}(Q)$) dan Kriteria Penerimaan String  
  13.3 Otomata dengan Transisi Spontan ($\varepsilon$-NFA) dan Prosedur Perhitungan Himpunan $\varepsilon\text{-Closure}(q)$  
  13.4 Teorema Ekuivalensi Bahasa Reguler: Membuktikan Setiap NFA Memiliki Padanan DFA  
  13.5 Prosedur Sistematis **Subset Construction** (*Lazy Reachable States Evaluation*) untuk Mengonversi NFA / $\varepsilon$-NFA menjadi DFA
* **Latihan Bab 13:** 10 soal perancangan NFA/$\varepsilon$-NFA dan tabel konversi lengkap ke DFA.

#### BAB 14: Minimasi Status DFA & Pemodelan Transisi Status Sistem Komputasi (Pekan 15)
* **Sub-CPMK:** `Sub-CPMK-4.1` & `Sub-CPMK-4.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  14.1 Mengapa Jumlah Status Otomata Perlu Diminimalkan? Penghapusan *Unreachable States*  
  14.2 Status Tak Terbedakan (*Indistinguishable States*) dan Algoritma Partisi Ekuivalensi / *Table-Filling* untuk Minimasi DFA  
  14.3 Pemodelan Proses Bisnis & Protokol Perangkat Lunak sebagai *Finite State Machine* (Siklus Pesanan *E-Commerce*, Pembayaran *Escrow*, & Sesi Otentikasi)  
  14.4 Audit Kelengkapan Transisi & Pencegahan *Unintended Deadlock State* pada Desain Sistem Informasi  
  14.5 Peta Kesinambungan *Handoff* `STI-204` menuju `STI-307 Sistem Cerdas` dan `STI-306 Analisis dan Perancangan Sistem Informasi`
* **Latihan Bab 14 & Unit Evaluasi E2:** 8 soal minimasi DFA dan pemodelan *state machine* transaksi digital + **Paket Simulasi Lengkap UAS (`CPMK-4` & Sintesis)**.
