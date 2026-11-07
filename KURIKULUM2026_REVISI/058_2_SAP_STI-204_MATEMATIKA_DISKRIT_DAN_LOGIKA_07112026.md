# 058_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA (*Discrete Mathematics and Logic*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI204`  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** `058_1_RPS_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md` · Dok 032 (Modalitas Pembelajaran SCL KPT 2024) · Dok 043 (Boundary Guardrails).

---

## BAGIAN I — IDENTITAS & REKAPITULASI OPERASIONAL PERKULIAHAN

| Atribut Operasional | Ketentuan Pelaksanaan di Kelas |
|---|---|
| **Kode & Nama Mata Kuliah** | `STI-204` — Matematika Diskrit dan Logika (*Discrete Mathematics and Logic*) — Kurikulum OBE SISTEKIN 2026 |
| **Bobot & Tipe Perkuliahan** | **3 SKS Teori** (`T=3, P=0`) · Semester 2 (Genap) · Prasyarat: `STI-103` Arsitektur dan Organisasi Sistem Teknologi Informasi |
| **CPL & CPMK Dibebankan** | `CPL-05` (`P1`: 80%), `CPL-02` (`KU1`: 20%) [Level *Introduce*] · `CPMK-1` (C3), `CPMK-2` (C3), `CPMK-3` (C4), `CPMK-4` (C4) |
| **Durasi per Pertemuan (SN-Dikti)** | **Tatap Muka (TM): 150 menit** ($3 \times 50'$) · **Penugasan Terstruktur (PT): 180 menit** ($3 \times 60'$) · **Belajar Mandiri (BM): 180 menit** ($3 \times 60'$) |
| **Struktur Baku Waktu Tatap Muka** | **Pendahuluan & Kasus Pemicu:** `20 menit` · **Kegiatan Inti (Eksplorasi Formal + *Guided Proof / Graph / Automata Workshop*):** `110 menit` · **Penutup, Cek Pemahaman & Tindak Lanjut:** `20 menit` |
| **Alat Bantu Visualisasi Konsep** | Papan Tulis Lebar, Proyektor, Alat Visualisasi Konseptual Berbasis Peramban (*GraphOnline* untuk graf/Dijkstra/MST & *Automatarium / FSM Simulator* untuk pengujian string DFA/NFA tanpa beban koding), LMS Edlink. |
| **Pagar Pembatas Kelas (*Guardrails*)** | 🟢 Fokus pada pembuktian logika proposisi/predikat, induksi matematika, relasi/*Poset*/Boolean formal/kombinatorika/rekurensi, analisis matematis graf & pohon, serta konstruksi DFA/NFA.<br>❌ **Larangan Kelas:** Dilarang membahas rakitan sirkuit gerbang fisik mikroprosesor (`STI-103`), menulis koding struktur data *pointer/linked-list* graf di C++/Java/Python (`FST-203 Struktur Data dan Algoritma`), koding tabel SQL fisik (`FST-207 Sistem Basis Data`), atau kalkulus limit-turunan kontinu (`STI-102`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Fokus Sesi Perkuliahan | Strategi SCL Utama | Durasi TM | Evaluasi |
|:---:|:---:|---|---|:---:|:---:|
| **1** | `Sub-CPMK-1.1` | Kontrak Belajar, Logika Proposisi, Tabel Kebenaran, & Hukum Aljabar Logika | *Interactive Lecture & Proof Drill* | 150' | Formatif |
| **2** | `Sub-CPMK-1.1, 1.2` | Aturan Inferensi Formal, Resolusi, & Logika Predikat Orde Pertama (*FOL*) | *Problem-Solving & Policy Case* | 150' | Formatif |
| **3** | `Sub-CPMK-1.2` | Strategi Pembuktian, Induksi Matematika (Biasa/Kuat), & Verifikasi Algoritma | *Problem-Based Learning (PBL)* | 150' | Formatif (Rilis Tugas 1) |
| **4** | `Sub-CPMK-2.1` | Himpunan, Relasi Ekuivalensi (Partisi), *Poset*, Diagram Hasse, & *Topological Sort* | *Case-Based Dependency Modeling* | 150' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1, 2.2` | Sifat Fungsi Diskrit (*Hashing*) & Aljabar Boolean pada Predikat Query Basis Data | *Problem-Solving Class* | 150' | Formatif |
| **6** | `Sub-CPMK-2.2` | Kombinatorika: Penjumlahan/Perkalian, *Pigeonhole*, Permutasi, & Kombinasi | *Case-Based Cardinality Analysis* | 150' | Formatif |
| **7** | `Sub-CPMK-2.1, 2.2` | Relasi Rekurensi Linier Homogen (Akar Karakteristik) & Konsolidasi Pra-UTS | *Problem-Solving Workshop* | 150' | Formatif |
| **8** | `CPMK-2` (& `CPMK-1`) | **Ujian Tengah Semester (UTS) — Relasi/*Poset*, Boolean Query, & Kombinatorika** | *Analytical Written Exam* | 150' | **UTS (30%)** |
| **9** | `Sub-CPMK-3.1` | Teori Graf, Derajat, Graf Bipartit, Isomorfisme, & *Adjacency Matrix* | *Visual Discovery & Matrix Drill* | 150' | Formatif |
| **10** | `Sub-CPMK-3.1` | Jejak BFS/DFS, Euler/Hamilton, & Lintasan Terpendek (*Dijkstra & Floyd-Warshall*) | *Case-Based Network Routing* | 150' | Formatif (Rilis Tugas 2) |
| **11** | `Sub-CPMK-3.2` | Teori Pohon (*Tree*), Pohon Biner, & *Minimum Spanning Tree* (*Kruskal & Prim*) | *Case Method Backbone Design* | 150' | Formatif |
| **12** | `Sub-CPMK-3.1, 3.2` | Pewarnaan Graf (*Graph Coloring* Jadwal) & Pohon Kode Optimal *Huffman* | *Problem-Solving Class* | 150' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-4.1` | Bahasa Formal, Alfabet, Ekspresi Reguler Dasar, & Konstruksi DFA | *Guided Automata Design* | 150' | Formatif |
| **14** | `Sub-CPMK-4.2` | Konstruksi NFA & $\varepsilon$-NFA serta Algoritma *Subset Construction* (NFA $\to$ DFA) | *Step-by-Step Conversion Workshop* | 150' | Formatif |
| **15** | `Sub-CPMK-4.1, 4.2` | Minimasi Status DFA & Studi Kasus Pemodelan *State Machine* Sistem TI + Review UAS | *Case Method & Synthesis Clinic* | 150' | Formatif |
| **16** | `CPMK-4` (& `1–3`) | **Ujian Akhir Semester (UAS) — Konstruksi DFA/NFA, Konversi, & *State Machine*** | *Comprehensive Written Exam* | 150' | **UAS (30%)** |

---

## BAGIAN II — RINCIAN SATUAN ACARA PERKULIAHAN PER PERTEMUAN (PERTEMUAN 1 s.d. 16)

---

### PERTEMUAN 1 — Kontrak Belajar, Logika Proposisi, Tabel Kebenaran, & Hukum Aljabar Logika
* **Kemampuan Akhir (`Sub-CPMK-1.1` [C3]):** Memformulasikan pernyataan logika proposisi dan membuktikan ekuivalensi logis melalui tabel kebenaran serta hukum aljabar logika.
* **Indikator Capaian:** (1) Menerjemahkan spesifikasi aturan sistem berbahasa Indonesia ke ekspresi simbolik (`¬, ∧, ∨, ⊕, →, ↔`) dan menentukan konvers, invers, serta kontraposisi; (2) Membuktikan tautologi dan ekuivalensi logis menggunakan tabel kebenaran maupun deretan hukum aljabar logika secara sah.
* **Pokok Bahasan:** Orientasi RPS OBE, Batas `STI-103` (Sirkuit Biner) vs `STI-204` (Penalaran Formal), Proposisi Majemuk, Implikasi & Jebakan Bahasa Sehari-hari, serta Hukum Ekuivalensi Logika.
* **Metode & Media:** *Interactive Lecture & Proof Drill*; Papan Tulis, Salindia Kasus Aturan Bisnis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memperkenalkan RPS `STI-204`, posisi mata kuliah sebagai jembatan menuju `FST-203`, `FST-207`, dan `STI-307`, lalu memantik kasus bug persyaratan beasiswa/diskon aplikasi akibat salah menerjemahkan kalimat *"Hanya jika pengguna terverifikasi..."* ($p \to q$ vs $q \to p$). | Menyimak kontrak belajar dan mendiskusikan mengapa implikasi $p \to q$ bernilai benar saat $p$ salah (*vacuously true*). | 20' | RPS `STI-204` & Slide |
| **Kegiatan Inti** | Menguraikan operator proposisi, pembedaan tegas antara konvers ($q \to p$), invers ($\neg p \to \neg q$), dan kontraposisi ($\neg q \to \neg p \equiv p \to q$), dilanjutkan pelatihan pembuktian ekuivalensi logis tanpa tabel kebenaran menggunakan Hukum Implikasi ($\neg p \vee q$), De Morgan, Distributif, Negasi, dan Absorpsi (karena tabel kebenaran meledak menjadi $2^{20}$ baris untuk 20 variabel!). | Berlatih berpasangan menerjemahkan 5 aturan otorisasi sistem ke simbol logika dan menurunkan bukti aljabar logika langkah demi langkah lengkap dengan nama hukum di tiap baris. | 110' | `[1]` Bab 1.1–1.3, `[3]` Bab 1 |
| **Penutup** | Merangkum kesalahan klasik (mis. menganggap $p \to q \equiv q \to p$) dan memberikan lembar latihan mandiri Pekan 1. | Mengerjakan kuis kilat 4 soal ekuivalensi implikasi di LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 10 soal translasi aturan bisnis dan pembuktian ekuivalensi aljabar logika pada Bab 1 Modul Ajar.

---

### PERTEMUAN 2 — Aturan Inferensi Formal, Resolusi, & Logika Predikat Orde Pertama (*FOL*)
* **Kemampuan Akhir (`Sub-CPMK-1.1` & `Sub-CPMK-1.2` [C3/C4]):** Membuktikan validitas argumen dengan aturan inferensi proposisi serta menerapkan inferensi logika predikat berkuantor.
* **Indikator Capaian:** (1) Menyusun bukti formal kesahihan argumen multi-premis menggunakan *Modus Ponens, Modus Tollens, Silogisme Hipotetis, Silogisme Disjungtif,* dan *Resolusi* (serta mengenali sesat pikir *fallacy*); (2) Memformulasikan ekspresi *First-Order Logic* (*FOL*) dengan kuantor $\forall$ dan $\exists$, menegasi kuantor bersarang, dan melakukan instansiasi/generalisasi universal.
* **Pokok Bahasan:** Aturan Inferensi & Sesat Pikir (*Affirming the Conclusion*), Prinsip Resolusi Robinson (Fondasi AI Simbolik), Fungsi Proposisi/Predikat $P(x,y)$, Kuantor $\forall$ & $\exists$, Negasi Kuantor De Morgan, dan Inferensi Berkuantor.
* **Metode & Media:** *Problem-Solving & Policy Case*; Papan Tulis, Lembar Kasus Audit Aturan Akses, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menyajikan 4 kalimat aturan keamanan jaringan perusahaan dan bertanya: *"Berdasarkan keempat aturan ini, dapatkah kita menyimpulkan secara pasti bahwa Server Basis Data tidak terhubung ke Wi-Fi Tamu?"* | Mencoba merangkai rantai deduksi logis dari premis-premis yang diberikan. | 20' | Slide Kasus Audit Akses |
| **Kegiatan Inti** | Bagian 1 (50'): Melatih penyusunan bukti 2-kolom (Pernyataan & Alasan Inferensi) termasuk aturan **Resolusi** $((p \vee q) \wedge (\neg p \vee r) \Rightarrow q \vee r)$. Bagian 2 (60'): Menjelaskan mengapa logika proposisi tidak cukup untuk menyatakan *"Setiap mahasiswa memiliki tepat satu dosen wali"*, memperkenalkan kuantor $\forall x\,\exists y$, perbedaan drastis urutan $\forall x\,\exists y\,P(x,y)$ vs $\exists y\,\forall x\,P(x,y)$, aturan negasi $\neg(\forall x\,P(x)) \equiv \exists x\,\neg P(x)$, serta aturan *Universal Instantiation*. | Kelompok menyelesaikan 4 soal bukti validitas argumen inferensi dan 4 soal formalisasi + negasi aturan sistem menggunakan kuantor *FOL*. | 110' | `[1]` Bab 1.4–1.6, `[2]` Bab 2–3 |
| **Penutup** | Menunjukkan bagaimana materi *FOL* dan Resolusi hari ini akan dipakai langsung pada `STI-307 Sistem Cerdas` (Semester 3) untuk *Knowledge Representation & Reasoning*. | Mengunggah hasil latihan kelompok ke LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan 10 soal bukti inferensi formal dan kuantor bersarang.

---

### PERTEMUAN 3 — Strategi Pembuktian, Induksi Matematika, & Verifikasi Kebenaran Algoritma
* **Kemampuan Akhir (`Sub-CPMK-1.2` [C3]):** Menerapkan metode pembuktian dan induksi matematika untuk membuktikan teorema diskrit serta memverifikasi kebenaran algoritma.
* **Indikator Capaian:** (1) Membedakan dan menerapkan bukti langsung, kontraposisi, dan kontradiksi; (2) Membuktikan rumus jumlahan, ketaksamaan ($2^n > n^2$), sifat keterbagian, serta *loop invariant* / fungsi rekursif sederhana menggunakan Induksi Matematika biasa dan kuat secara runtut.
* **Pokok Bahasan:** Bukti Langsung/Kontraposisi/Kontradiksi, Prinsip Efek Domino Induksi Matematika (*Basis Step, Inductive Hypothesis, Inductive Step*), Induksi Kuat (*Strong Induction*), dan Verifikasi Kebenaran Invarian Algoritma.
* **Metode & Media:** *Problem-Based Learning* (PBL); Papan Tulis, Pseudocode Algoritma Sederhana, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Mengajukan pertanyaan kritis rekayasa perangkat lunak: *"Menguji sebuah fungsi dengan 1.000 contoh angka dan semuanya benar belum menjamin fungsi tersebut bebas bug pada angka ke-1.001—bagaimana cara membuktikan kebenarannya untuk SELURUH $n \ge 1$?"* | Memahami keterbatasan pengujian sampel (*testing*) dibandingkan verifikasi matematis (*formal verification*). | 20' | Pseudocode & Slide |
| **Kegiatan Inti** | Menguraikan anatomi wajib bukti Induksi Matematika (mengapa tidak boleh mengasumsikan $P(k+1)$ sejak awal!), melatih bukti induksi pada deret jumlah operasi algoritma bersarang, ketaksamaan pertumbuhan kompleksitas, induksi kuat pada bilangan Fibonacci/pecahan koin, serta pembuktian kebenaran invarian simpal (*loop invariant*: Inisialisasi, Pemeliharaan, Terminasi) pada pseudocode pencarian/perpangkatan cepat. | Berlatih menyusun naskah bukti induksi yang lengkap dan rapi di papan tulis dengan saling mengaudit apakah hipotesis induksi telah digunakan secara sah. | 110' | `[1]` Bab 1.7 & 5.1–5.4, `[3]` Bab 4 |
| **Penutup** | Merangkum ketuntasan penuh `CPMK-1` dan **merilis resmi naskah RTM-1 (Tugas 1 — Bobot 20%)** di LMS Edlink untuk dikumpulkan pada Pekan 4. | Mengunduh instruksi Tugas 1 dan mencermati rubrik penilaian keruntutan bukti. | 20' | Dokumen RTM-1 di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan secara mandiri seluruh 4 masalah pembuktian pada **Tugas 1 (`CPMK-1`)**.

---

### PERTEMUAN 4 — Himpunan, Relasi Ekuivalensi, & Himpunan Terurut Parsial (*Poset*) + Evaluasi Tugas 1
* **Kemampuan Akhir (`Sub-CPMK-2.1` [C3]):** Menerapkan konsep himpunan, relasi ekuivalensi, dan *Poset* pada pemodelan struktur data serta penjadwalan tugas berprasyarat, sekaligus menuntaskan evaluasi sumatif **Tugas 1 (20%)**.
* **Indikator Capaian:** (1) Memeriksa sifat refleksif, simetris, antisimetris, dan transitif suatu relasi biner (baik dalam himpunan pasangan maupun matriks biner) serta menentukan kelas ekuivalensi/partisi; (2) Menggambar **Diagram Hasse** dari suatu *Poset* $(S, \preceq)$, menentukan elemen maksimal/minimal/terbesar/terkecil, dan menghasilkan urutan linear valid dengan *Topological Sorting*.
* **Pokok Bahasan:** Operasi Himpunan & Hasil Kali Kartesian, Relasi Biner & Penutupan (*Closure*), Relasi Ekuivalensi & Partisi Data, serta *Partially Ordered Set* (*Poset*), Diagram Hasse, dan *Topological Sort*.
* **Metode & Media:** *Case-Based Dependency Modeling*; Papan Tulis, Kasus Pohon Prasyarat Mata Kuliah / *Build System*, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memverifikasi pengumpulan **Tugas 1 (20%)** di LMS Edlink dan mengadakan kuis verifikasi singkat 10 menit (1 soal negasi kuantor / langkah dasar induksi) di kelas. | Memastikan Tugas 1 telah terunggah dan mengerjakan soal verifikasi mandiri. | 20' | LMS Edlink & Kertas Kuis |
| **Kegiatan Inti** | Menjelaskan operasi himpunan dan matriks relasi biner; membedakan relasi ekuivalensi (refleksif + simetris + transitif $\Rightarrow$ mengelompokkan pengguna/data ke partisi saling lepas) vs pengurutan parsial/*Poset* (refleksif + **antisimetris** + transitif $\Rightarrow$ memodelkan hierarki ketergantungan tugas). Memandu latihan menggambar Diagram Hasse dan mengeksekusi *Topological Sorting* pada jadwal pembangunan modul proyek sistem informasi (atau urutan pengambilan MK berprasyarat!). | Kelompok memodelkan daftar ketergantungan 8 tugas proyek menjadi matriks relasi, menggambar Diagram Hasse-nya, dan menentukan urutan eksekusi tugas yang valid. | 110' | `[1]` Bab 2.1–2.2 & 9.1–9.6, `[3]` Bab 2–3 |
| **Penutup** | Menekankan perbedaan relasi matematis dengan tabel relasional basis data serta mengantar Pekan 5 (Fungsi Diskrit & Aljabar Boolean Query). | Mengumpulkan lembar kerja Diagram Hasse kelompok. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 8 soal relasi ekuivalensi, kelas kongruensi modulo, dan konstruksi Diagram Hasse *Poset*.
* **Evaluasi Sumatif Pekan Ini:** **Tugas 1 (Bobot 20%)** dinilai menggunakan Rubrik Analitik Tugas 1 (`058_5`).

---

### PERTEMUAN 5 — Sifat Fungsi Diskrit (*Hashing*) & Aljabar Boolean pada Predikat Query Basis Data
* **Kemampuan Akhir (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C3]):** Menerapkan sifat fungsi diskrit dan aljabar Boolean formal pada pemodelan pemetaan data serta optimasi kondisi logika query basis data.
* **Indikator Capaian:** (1) Mengklasifikasikan fungsi injektif (*one-to-one*), surjektif (*onto*), bijektif, fungsi invers, serta memodelkan fungsi *hash* $h(k) = k \bmod m$; (2) Menerapkan aksioma, dualitas, dan teorema Aljabar Boolean untuk menyederhanakan ekspresi logika kondisi seleksi (*filter predicate*) pada kueri basis data sehingga evaluasi atribut menjadi jauh lebih ringan.
* **Pokok Bahasan:** Fungsi Diskrit, Bijeksi, Fungsi *Floor/Ceiling* & *Modulo Hashing*, Struktur Aljabar Boolean $(B, +, \cdot, ')$, Bentuk Kanonik DNF/CNF (*Minterm/Maxterm*), dan Penyederhanaan Ekspresi Logika Query Basis Data.
* **Metode & Media:** *Problem-Solving Class*; Papan Tulis, Studi Kasus *Predicate Pushdown/Simplification*, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membagikan umpan balik Tugas 1, lalu memperlihatkan ekspresi filter pencarian transaksi e-commerce yang berbelit-belit hasil gabungan beberapa aturan bisnis: bagaimana menyederhanakannya secara matematis tanpa mengubah himpunan baris data yang dihasilkan? | Mengamati bahwa klausa kondisi bertumpuk dapat direpresentasikan sebagai variabel-variabel Aljabar Boolean ($A, B, C, D$). | 20' | Slide Kasus Predikat Query |
| **Kegiatan Inti** | Bagian 1 (45'): Menganalisis fungsi injektif/surjektif/bijektif dalam pengkodean ID unik dan pemetaan alamat tabel *hash*. Bagian 2 (65'): Mengupas struktur aksiomatik Aljabar Boolean abstrak (berbeda sudut pandang dengan penyolderan gerbang di `STI-103`: di sini diterapkan pada himpunan & predikat kueri relasional!), bentuk normal konjungtif/disjungtif, serta penyederhanaan kondisi logika kompleks agar mesin basis data mengevaluasi sesedikit mungkin kondisi *(tanpa menulis koding DDL/DML SQL yang menjadi ranah `FST-207`)*. | Menyederhanakan 6 kasus ekspresi predikat kueri panjang menjadi bentuk Boolean paling ringkas dan membuktikan kesamaan himpunan hasil seleksinya. | 110' | `[1]` Bab 2.3 & 12, `[3]` Bab 5 |
| **Penutup** | Menyimpulkan sinergi langsung materi pekan ini dengan mata kuliah ko-semester `FST-207 Sistem Basis Data` dan `FST-203 Struktur Data dan Algoritma`. | Menyelesaikan 1 soal cepat penyederhanaan predikat Boolean 3 kondisi. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan mandiri 10 soal sifat fungsi diskrit dan penyederhanaan aljabar Boolean pada logika kueri.

---

### PERTEMUAN 6 — Kombinatorika Terapan pada Pencacahan Struktur Data & Kardinalitas Query
* **Kemampuan Akhir (`Sub-CPMK-2.2` [C3]):** Menerapkan kaidah kombinatorika pencacahan pada permasalahan kapasitas pengkodean, keamanan ruang kunci, dan estimasi kardinalitas kombinasi data.
* **Indikator Capaian:** (1) Menerapkan aturan penjumlahan, aturan perkalian, prinsip *Inclusion-Exclusion* ($|A \cup B \cup C|$), dan *Pigeonhole Principle*; (2) Menghitung permutasi, kombinasi, dan kombinasi dengan pengulangan pada skenario sistem informasi nyata.
* **Pokok Bahasan:** Kaidah Dasar Pencacahan, Prinsip *Inclusion-Exclusion* pada Gabungan Hasil Query, Prinsip Sarang Merpati (*Pigeonhole Principle* pada Bentrokan *Hash*/IP/Port), Permutasi, Kombinasi, dan Teorema Binomial.
* **Metode & Media:** *Case-Based Cardinality Analysis*; Papan Tulis, Lembar Kasus Keamanan & Data, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Mengajukan teka-teki sistem: *"Berapa minimal pengguna aktif bersamaan agar kita 100% yakin pasti ada minimal dua pengguna yang memetakan sesi ke slot bucket hash 1.024 yang sama?"* | Menjawab cepat `1.025 pengguna` dan mengenali kekuatan *Pigeonhole Principle*. | 20' | Slide Kasus *Hash Bucket* |
| **Kegiatan Inti** | Membedah prinsip *Inclusion-Exclusion* untuk menghitung kardinalitas gabungan himpunan data beririsan (`|A ∪ B ∪ C|`), melatih pembedaan tajam permutasi vs kombinasi pada masalah kekuatan kata sandi (*brute-force keyspace*), jumlah pasangan perbandingan entitas (*all-pairs comparison* $\binom{n}{2}$), pemilihan subset kolom/indeks basis data, dan distribusi beban tugas ke server. | Kelompok memecahkan 8 studi masalah kombinatorika komputasi dan mempresentasikan cara memodelkan batasan syarat khusus pada tiap soal. | 110' | `[1]` Bab 6, `[3]` Bab 6 |
| **Penutup** | Merangkum panduan diagnostik pemilihan rumus kombinatorika (urutan penting vs tidak, boleh berulang vs tidak). | Mengikuti kuis formatif 4 soal kombinatorika di LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 10 soal latihan kombinatorika dan *Inclusion-Exclusion*.

---

### PERTEMUAN 7 — Relasi Rekurensi Linier Homogen & Konsolidasi Pemodelan Diskrit Pra-UTS
* **Kemampuan Akhir (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C3]):** Menyelesaikan relasi rekurensi linier homogen dan mengintegrasikan penguasaan materi `CPMK-2` menjelang UTS.
* **Indikator Capaian:** (1) Memodelkan jumlah langkah/kemungkinan barisan diskrit ke dalam relasi rekurensi beserta kondisi awalnya; (2) Menyelesaikan relasi rekurensi linier homogen berkoefisien konstan orde-1 dan orde-2 (akar karakteristik riil berbeda maupun kembar) menjadi rumus eksplisit tertutup $a_n$.
* **Pokok Bahasan:** Pemodelan Rekurensi (Menara Hanoi, Barisan Biner Tanpa `'00'` Berurutan, Pertumbuhan Pohon Rekursi), Metode Persamaan Karakteristik, dan Klinik Persiapan UTS.
* **Metode & Media:** *Problem-Solving Workshop*; Papan Tulis, Paket Simulasi UTS, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan masalah pengiriman kode biner panjang-$n$ yang melarang kemunculan dua bit `0` berturutan: bagaimana mencari rumus langsung banyak string valid untuk $n$ berapa pun? | Menemukan pola rekursif $a_n = a_{n-1} + a_{n-2}$ dari pengamatan kasus $n=1, 2, 3, 4$. | 20' | Papan Tulis |
| **Kegiatan Inti** | Bagian 1 (60'): Menurunkan metode persamaan karakteristik $r^2 - c_1 r - c_2 = 0$ baik untuk kasus dua akar berbeda ($a_n = \alpha_1 r_1^n + \alpha_2 r_2^n$) maupun akar kembar ($a_n = \alpha_1 r_0^n + \alpha_2 n r_0^n$). Bagian 2 (50'): Klinik bedah simulasi soal komprehensif persiapan **UTS Pekan 8** (`Relasi/Poset`, `Aljabar Boolean Query`, `Kombinatorika`, & `Relasi Rekurensi`). | Menyelesaikan 4 soal relasi rekurensi hingga memperoleh rumus tertutup terverifikasi untuk $n=1,2,3$, lalu berdiskusi membahas soal simulasi UTS. | 110' | `[1]` Bab 8.1–8.2, `[2]` Bab 5 |
| **Penutup** | Membagikan kisi-kisi resmi, bobot per butir soal, dan kriteria Rubrik Analitik **UTS Pekan 8 (Bobot 30%)**. | Mencatat kisi-kisi UTS dan menanyakan klarifikasi konsep yang belum mantap. | 20' | Kisi-Kisi UTS di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan mandiri paket simulasi soal UTS di LMS Edlink.

---

### PERTEMUAN 8 — EVALUASI TENGAH SEMESTER (UTS)
* **Kemampuan Akhir Diuji (`CPMK-2` [C3] & penguatan `CPMK-1`):** Menerapkan konsep relasi ekuivalensi, himpunan terurut parsial (*Poset*), aljabar Boolean, kombinatorika, dan relasi rekurensi pada pemodelan struktur data serta logika kueri basis data secara tepat.
* **Bentuk & Durasi:** Ujian Tertulis Pemecahan Masalah & Kasus Pemodelan Diskrit Terjadwal (*Closed-Book*), **150 menit**.
* **Bobot Penilaian Sumatif:** **30%** terhadap Nilai Akhir Mata Kuliah.

| Tahap | Aktivitas Pengawas / Dosen | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan daftar hadir berita acara UTS, pengaturan tempat duduk, pembacaan tata tertib kejujuran akademik, dan pembagian naskah soal UTS. | Menandatangani presensi dan menyiapkan alat tulis. | 10' | Berita Acara & Naskah UTS |
| **Pelaksanaan Ujian** | Mengawasi pelaksanaan ujian secara tertib. | Mengerjakan 4 butir soal utama (*Poset*/Diagram Hasse/*Topological Sort*, penyederhanaan Aljabar Boolean kueri & fungsi diskrit, kasus kombinatorika, serta penyelesaian relasi rekurensi). | 135' | Lembar Jawaban UTS |
| **Pengumpulan** | Mengumpulkan dan menghitung kelengkapan lembar jawaban. | Menyerahkan lembar jawaban secara tertib. | 5' | Bundel Jawaban UTS |

---

### PERTEMUAN 9 — Teori Graf Dasar, Graf Khusus, Isomorfisme, & Matriks Representasi (*Adjacency Matrix*)
* **Kemampuan Akhir (`Sub-CPMK-3.1` [C4]):** Menganalisis struktur dan sifat graf menggunakan terminologi formal serta matriks representasi (*Adjacency & Incidence Matrix*).
* **Indikator Capaian:** (1) Menganalisis jenis graf, teorema jabat tangan ($\sum \deg(v) = 2|E|$), graf bipartit (pemodelan penugasan *user–item*), dan menguji isomorfisme dua graf dengan invarian struktural; (2) Menyusun *Adjacency Matrix* $A$ (biner maupun berbobot) serta menganalisis arti matematis elemen $(i,j)$ pada matriks $A^2, A^3$ dalam menghitung banyak rute koneksi.
* **Pokok Bahasan:** Definisi Graf $G=(V,E)$, Graf Berarah/Tak Berarah/Berbobot, Derajat, Subgraf, Graf Lengkap & Bipartit, Isomorfisme Graf, serta *Adjacency Matrix* dan *Incidence Matrix*.
* **Metode & Media:** *Visual Discovery & Matrix Drill*; *GraphOnline Web Visualizer*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membahas evaluasi umum UTS, lalu memperlihatkan bagaimana peta jalan Google Maps, pertemanan jejaring sosial, topologi router internet, dan sistem rekomendasi produk semuanya bermuara pada satu struktur matematika yang sama: **Graf**! | Menyimak umpan balik UTS dan mengidentifikasi apa yang menjadi simpul (*vertex*) serta sisi (*edge*) pada ke-4 contoh sistem tersebut. | 20' | Pembahasan UTS & Slide |
| **Kegiatan Inti** | Menguraikan klasifikasi graf, pembuktian cepat teorema jabat tangan, pengujian graf bipartit 2-warna untuk sistem pencocokan (*matching*), pemeriksaan invarian isomorfisme (jumlah simpul, sisi, barisan derajat, panjang siklus), serta konstruksi **Adjacency Matrix** dan perhitungan $A^2$ untuk menemukan koneksi derajat-2 ("teman dari teman") secara aljabar. *(Menjaga guardrail: implementasi koding array/linked-list di memori diserahkan ke `FST-203`)*. | Berlatih mengubah topologi jaringan komputer ke *Adjacency Matrix*, menguji apakah dua topologi jaringan tampak berbeda ternyata isomorfik, dan menghitung jumlah lintasan panjang-2 antar-simpul. | 110' | `[1]` Bab 10.1–10.4, `[3]` Bab 8, GraphOnline |
| **Penutup** | Merangkum keunggulan vs kelemahan *Adjacency Matrix* pada graf padat vs graf jarang (*sparse*) dan mengantar algoritma penelusuran lintasan Pekan 10. | Menyelesaikan kuis singkat 4 soal sifat graf di LMS Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 10 soal analisis invarian isomorfisme, graf bipartit, dan *Adjacency Matrix* pada Bab 8 Modul Ajar.

---

### PERTEMUAN 10 — Penelusuran Lintasan Graf, Euler/Hamilton, & Algoritma *Shortest Path* (*Dijkstra & Floyd-Warshall*)
* **Kemampuan Akhir (`Sub-CPMK-3.1` [C4]):** Menganalisis keterhubungan lintasan graf dan menerapkan algoritma penelusuran lintasan terpendek untuk optimasi jaringan data.
* **Indikator Capaian:** (1) Menelusuri urutan simpul BFS & DFS secara matematis serta menentukan eksistensi lintasan/sirkuit Euler (syarat derajat genap) dan Hamilton; (2) Menelusuri tabel iterasi **Algoritma Dijkstra** (*single-source shortest path*) dan pembaruan matriks **Floyd-Warshall** (*all-pairs shortest path*) beserta rekonstruksi jalur optimalnya.
* **Pokok Bahasan:** Keterhubungan Komponen Graf, Urutan Penelusuran BFS vs DFS, Teorema Sirkuit/Lintasan Euler & Masalah Sirkuit Hamilton (*TSP Pengantar*), serta Algoritma *Dijkstra* dan *Floyd-Warshall*.
* **Metode & Media:** *Case-Based Network Routing*; Lembar Kerja Tabel *Dijkstra*, *GraphOnline*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan masalah klasik Jembatan Königsberg Euler berdampingan dengan masalah kurir logistik yang harus mengunjungi tiap gudang tepat satu kali (Hamilton): mengapa yang pertama mudah diputuskan dalam hitungan detik sedangkan yang kedua sangat sulit pada skala besar? | Menganalisis perbedaan melewati setiap **sisi** tepat sekali (Euler) vs setiap **simpul** tepat sekali (Hamilton). | 20' | Slide Königsberg & Topologi Logistik |
| **Kegiatan Inti** | Menguraikan syarat perlu dan cukup lintasan/sirkuit Euler, analisis sirkuit Hamilton, penelusuran sistematis BFS/DFS (aturan urutan alfabetis simpul), lalu memandu langkah demi langkah pengisian tabel relaksasi jarak $d[v] = \min(d[v], d[u] + w(u,v))$ pada **Algoritma Dijkstra** untuk mencari rute latensi milidetik terkecil pada jaringan 8 router, diikuti prinsip pembaruan matriks jarak **Floyd-Warshall**. | Kelompok menelusuri tabel lengkap Algoritma Dijkstra pada studi kasus jaringan paket data antar-kota dan memverifikasi jalur terpendek beserta total latensinya. | 110' | `[1]` Bab 10.5–10.6, `[3]` Bab 8 |
| **Penutup** | Menekankan batasan penting Algoritma Dijkstra (bobot sisi non-negatif) dan **merilis resmi naskah RTM-2 (Tugas 2 — Bobot 20%)** di LMS Edlink untuk dikumpulkan pada Pekan 12. | Mengunduh instruksi studi kasus jaringan Tugas 2 di Edlink. | 20' | Dokumen RTM-2 di Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mulai mengerjakan Bagian 1 & 2 laporan **Tugas 2** (*Adjacency Matrix*, Euler/Hamilton, & penelusuran tabel *Dijkstra*).

---

### PERTEMUAN 11 — Teori Pohon (*Tree*) & Optimasi Jaringan dengan *Minimum Spanning Tree* (*Kruskal & Prim*)
* **Kemampuan Akhir (`Sub-CPMK-3.2` [C4]):** Menganalisis sifat matematis Pohon (*Tree*) dan menerapkan algoritma *Minimum Spanning Tree* (*Kruskal & Prim*) untuk optimasi infrastruktur jaringan.
* **Indikator Capaian:** (1) Menganalisis teorema ekuivalensi pohon ($|E|=|V|-1$, terhubung tanpa siklus), pohon berakar $m$-ary/biner, dan penelusuran *preorder, inorder, postorder* pada pohon ekspresi aritmetika/logika; (2) Menerapkan **Algoritma Kruskal** dan **Algoritma Prim** untuk mengonstruksi pohon merentang berbiaya total minimum (*MST*).
* **Pokok Bahasan:** Sifat Matematis Pohon, Pohon Berakar & Pohon Biner Penuh, Notasi Prefiks/Infiks/Postfiks Pohon Ekspresi, Konsep *Spanning Tree*, serta Algoritma *Greedy* **Kruskal** dan **Prim**.
* **Metode & Media:** *Case Method Backbone Design*; Studi Kasus Jaringan Serat Optik Kampus, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membandingkan dua tujuan rekayasa jaringan yang sering tertukar oleh mahasiswa: *"Kapan kita memakai Dijkstra (rute tercepat dari A ke Z) vs kapan kita memakai Minimum Spanning Tree (menghubungkan seluruh 10 gedung kampus dengan total panjang galian kabel fiber optik paling murah)?"* | Membedakan secara tajam masalah *Shortest Path Tree* terhadap satu titik sumber vs *Minimum Spanning Tree* berbiaya gabungan terkecil. | 20' | Slide Komparasi *SPT vs MST* |
| **Kegiatan Inti** | Membuktikan sifat $|E|=|V|-1$ pada pohon, melatih penelusuran *preorder/inorder/postorder* pada pohon ekspresi, lalu membedah mekanisme pemilihan sisi termurah bebas siklus pada **Algoritma Kruskal** dan penumbuhan pohon bertetangga pada **Algoritma Prim** di atas graf berbobot nyata. | Kelompok merancang jalur pemasangan kabel fiber optik paling hemat untuk kasus 9 gedung menggunakan baik Kruskal maupun Prim, lalu membuktikan bahwa keduanya menghasilkan bobot minimum yang sama. | 110' | `[1]` Bab 11.1–11.5, `[3]` Bab 9 |
| **Penutup** | Merangkum kriteria pemilihan algoritma pohon dan memeriksa progres pengerjaan Tugas 2 mahasiswa. | Melanjutkan bagian *MST* pada draf laporan Tugas 2. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Menyelesaikan bagian *MST* pada **Tugas 2** dan membaca materi pewarnaan graf serta kode *Huffman* untuk Pekan 12.

---

### PERTEMUAN 12 — Pewarnaan Graf (*Graph Coloring*) pada Penjadwalan & Pohon *Huffman* + Evaluasi Tugas 2
* **Kemampuan Akhir (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C4]):** Menerapkan pewarnaan graf untuk optimasi penjadwalan bebas konflik dan pohon *Huffman* untuk pengkodean data efisien, serta menuntaskan evaluasi sumatif **Tugas 2 (20%)**.
* **Indikator Capaian:** (1) Memodelkan masalah bentrok jadwal/alokasi kanal frekuensi sebagai graf konflik, menerapkan algoritma pewarnaan simpul (*Welsh-Powell*), dan menentukan bilangan kromatik $\chi(G)$; (2) Mengonstruksi pohon biner kode prefiks **Huffman** dari frekuensi karakter dan menghitung rasio penghematan bit.
* **Pokok Bahasan:** Graf Planar & Teorema Empat Warna Pengantar, Pewarnaan Simpul & Bilangan Kromatik $\chi(G)$ untuk Penjadwalan, serta Pohon Kode Prefiks Optimal *Huffman*.
* **Metode & Media:** *Problem-Solving Class*; Studi Kasus Penjadwalan Ujian Fakultas, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Memverifikasi pengumpulan **Tugas 2 (20%)** di LMS Edlink dan mengadakan kuis verifikasi singkat 10 menit (1 soal kecil langkah *Dijkstra/MST*) di kelas. | Memastikan laporan Tugas 2 terunggah dan mengerjakan soal verifikasi individu. | 20' | LMS Edlink & Kertas Kuis |
| **Kegiatan Inti** | Bagian 1 (55'): Menunjukkan bagaimana menyusun jadwal 8 mata kuliah agar tidak ada satu pun mahasiswa yang mengalami bentrok jam ujian dengan mengubah mata kuliah menjadi simpul, bentrok peserta menjadi sisi, dan slot jam ujian menjadi **warna simpul** ($\chi(G)$ slot minimum!). Bagian 2 (55'): Memperagakan pembangunan *Huffman Tree* dari bawah ke atas untuk kompresi teks tanpa kehilangan informasi (*lossless*). | Berlatih mewarnai graf konflik penjadwalan dengan algoritma *Welsh-Powell* serta mengonstruksi kode biner *Huffman* dan membandingkan jumlah bit totalnya terhadap ASCII ukuran tetap. | 110' | `[1]` Bab 10.8 & 11.2, `[3]` Bab 8–9 |
| **Penutup** | Merangkum ketuntasan `CPMK-3` dan membuka Bagian IV (`CPMK-4`, Pekan 13–15): bagaimana graf berarah berlabel menjadi mesin abstrak pengenal bahasa dan pengendali status sistem (*Finite State Automata*). | Mencatat jembatan keterhubungan graf berarah dengan diagram transisi otomata. | 20' | Salindia Jembatan `CPMK-4` |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Membaca Bab 12 Modul Ajar tentang Bahasa Formal dan *Deterministic Finite Automata* (DFA).
* **Evaluasi Sumatif Pekan Ini:** **Tugas 2 (Bobot 20%)** dinilai menggunakan Rubrik Analitik Tugas 2 (`058_5`).

---

### PERTEMUAN 13 — Bahasa Formal & Konstruksi *Deterministic Finite Automata* (DFA)
* **Kemampuan Akhir (`Sub-CPMK-4.1` [C4]):** Mengonstruksi model *Deterministic Finite Automata* (DFA) secara formal dan akurat untuk pengenalan pola bahasa reguler.
* **Indikator Capaian:** (1) Mendefinisikan komponen alfabet $\Sigma$, string, bahasa $L \subseteq \Sigma^*$, ekspresi reguler dasar, serta 5-tupel formal DFA $M = (Q, \Sigma, \delta, q_0, F)$; (2) Mengonstruksi diagram transisi dan tabel transisi DFA yang lengkap (setiap status memiliki tepat satu busur keluar untuk setiap simbol di $\Sigma$, termasuk *trap/dead state* bila perlu) dan membuktikan penerimaan string dengan fungsi transisi diperluas $\hat{\delta}(q_0, w)$.
* **Pokok Bahasan:** Hierarki Bahasa Formal Pengantar, Alfabet & Operasi Bahasa, Ekspresi Reguler Dasar, Definisi Formal 5-Tupel DFA, serta Strategi Perancangan DFA Pengenal Pola.
* **Metode & Media:** *Guided Automata Design*; Simulator Web *Automatarium*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Membagikan umpan balik Tugas 2, lalu memantik konteks praktis: *"Saat Anda mengetik alamat email atau kode voucher di formulir web, bagaimana komputer memvalidasi apakah pola karakternya sah hanya dalam sekali baca dari kiri ke kanan?"* | Menghubungkan fitur *Regex validation* dan *lexical scanner* dengan model mesin berstatus hingga. | 20' | Pembahasan Tugas 2 & Slide |
| **Kegiatan Inti** | Menguraikan 5-tupel formal $M=(Q, \Sigma, \delta, q_0, F)$, aturan emas determinisme DFA (tidak boleh ada transisi ganda untuk simbol yang sama dan tidak boleh melupakan transisi simbol alfabet yang tersisa!), lalu memandu perancangan bertingkat 5 DFA: (a) string berakhiran `'01'`, (b) string memuat jumlah `'1'` genap dan `'0'` ganjil, (c) kode produk berawalan huruf diikuti tepat 3 digit, dan (d) bilangan biner habis dibagi 3. | Merancang diagram dan tabel transisi DFA secara berkelompok, menuliskan penelusuran formal $\hat{\delta}(q_0, w) \in F$, dan memvalidasi rancangan pada simulator web *Automatarium* dengan 6 kasus uji (3 valid, 3 tidak valid). | 110' | `[1]` Bab 13.2–13.3, `[4]` Bab 2.1–2.2, Automatarium |
| **Penutup** | Merangkum jebakan umum perancangan DFA (mis. lupa menangani *dead state* atau menerima string kosong $\varepsilon$ yang seharusnya ditolak). | Mengunggah tangkapan skema DFA dan tabel transisi latihan ke Edlink. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Mengerjakan 8 soal perancangan 5-tupel DFA pengenal pola bahasa formal pada Bab 12 Modul Ajar.

---

### PERTEMUAN 14 — Konstruksi NFA / $\varepsilon$-NFA & Konversi *Subset Construction* ke DFA
* **Kemampuan Akhir (`Sub-CPMK-4.2` [C4]):** Mengonstruksi model *Nondeterministic Finite Automata* (NFA & $\varepsilon$-NFA) dan mengonversinya menjadi DFA ekuivalen.
* **Indikator Capaian:** (1) Merancang NFA ($\delta: Q \times \Sigma \to \mathcal{P}(Q)$) dan $\varepsilon$-NFA untuk pola bahasa gabungan/perulangan serta menghitung $\varepsilon\text{-closure}(q)$ secara teliti; (2) Menerapkan algoritma **Subset Construction** langkah demi langkah (hanya membangkitkan himpunan bagian status yang terjangkau dari status awal) untuk menghasilkan DFA yang ekuivalen.
* **Pokok Bahasan:** Konsep Nondeterminisme (Percabangan Tebakan Paralel), Definisi Formal NFA & Transisi Spontan $\varepsilon$-NFA, Perhitungan $\varepsilon\text{-Closure}$, Teorema Ekuivalensi NFA $\equiv$ DFA, dan Algoritma *Subset Construction*.
* **Metode & Media:** *Step-by-Step Conversion Workshop*; Simulator *Automatarium*, Papan Tulis, Lembar Kerja Tabel *Subset*, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Meminta mahasiswa merancang DFA untuk bahasa *"semua string biner yang simbol ke-3 dari belakang adalah `1`"* (butuh $2^3=8$ status rumit!), lalu menunjukkan betapa mudahnya masalah yang sama digambar hanya dengan **4 status** menggunakan **NFA**! | Menyadari keunggulan NFA: sangat intuitif dirancang manusia, lalu dapat diubah secara algoritmis menjadi DFA cepat untuk dieksekusi mesin. | 20' | Papan Tulis |
| **Kegiatan Inti** | Menjelaskan cara kerja pohon penelusuran paralel NFA ($\hat{\delta}(q_0, w) \cap F \neq \emptyset$ berarti diterima!), definisi $\varepsilon\text{-closure}$ pada $\varepsilon$-NFA (jembatan dari Ekspresi Reguler Thompson ke otomata), lalu memandu pengerjaan tabel **Subset Construction** secara disiplin termasuk penanganan himpunan kosong $\emptyset$ sebagai *dead state* dan penandaan seluruh status himpunan yang memuat minimal satu anggota $F$ sebagai *accepting state* DFA baru. | Mengerjakan 3 latihan lengkap perancangan NFA/$\varepsilon$-NFA diikuti konversi *Subset Construction* menjadi tabel & diagram DFA, lalu membandingkan perilaku kedua mesin pada string uji yang sama. | 110' | `[1]` Bab 13.3–13.4, `[4]` Bab 2.3–2.5 |
| **Penutup** | Merangkum alur konversi *Regex $\to$ $\varepsilon$-NFA $\to$ NFA $\to$ DFA* yang bekerja di balik mesin pencari teks modern. | Menyelesaikan 1 soal cepat penentuan $\varepsilon\text{-closure}$ semua status. | 20' | LMS Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Latihan mandiri 6 soal konstruksi NFA dan konversi *Subset Construction* ke DFA.

---

### PERTEMUAN 15 — Minimasi Status DFA, Pemodelan *State Machine* Sistem TI, & Review Pra-UAS
* **Kemampuan Akhir (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C4]):** Meminimalkan jumlah status DFA dan mengonstruksi model transisi status sistem komputasi nyata, serta mengonsolidasikan seluruh `CPMK-1..4` menjelang UAS.
* **Indikator Capaian:** (1) Mereduksi DFA hasil konversi menjadi DFA minimal melalui eliminasi status tak terjangkau dan metode partisi ekuivalensi / *table-filling*; (2) Mengonstruksi model *Finite State Machine* untuk alur proses sistem informasi nyata (siklus status pesanan/pembayaran digital, mesin otentikasi percobaan login dengan *lockout*, atau protokol jabatan tangan komunikasi) serta mengaudit ada/tidaknya celah transisi ilegal.
* **Pokok Bahasan:** Algoritma Minimasi Status DFA, Pemodelan Transisi Status Sistem Komputasi (*Business/Protocol Finite State Machine*), dan Klinik Sintesis Pra-UAS.
* **Metode & Media:** *Case Method & Synthesis Clinic*; Studi Kasus Alur Pembayaran *E-Wallet*, Papan Tulis, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa (SCL) | Durasi | Sumber/Media |
|---|---|---|:---:|---|
| **Pendahuluan** | Menyajikan kasus bug nyata sistem *e-commerce* di mana pesanan yang sudah berstatus `CANCELLED` ternyata masih bisa berpindah ke `SHIPPED` ketika *webhook* pembayaran terlambat datang—akibat pengembang tidak merancang *Finite State Machine* formal! | Menganalisis pentingnya mendefinisikan tabel transisi status secara formal dan deterministik sebelum menulis kode *back-end*. | 20' | Studi Kasus Bug Transisi Pesanan |
| **Kegiatan Inti** | Bagian 1 (65'): Melatih metode partisi ekuivalensi 0-ekuivalen, 1-ekuivalen, dst. untuk meminimalkan jumlah status DFA, dilanjutkan bengkel kasus pemodelan siklus hidup transaksi digital & otentikasi akun berbatas 3 kali gagal login menggunakan FSA. Bagian 2 (45'): Klinik review komprehensif persiapan **UAS Pekan 16**. | Kelompok memodelkan spesifikasi proses sistem menjadi diagram & tabel transisi FSA yang kedap celah, meminimalkan DFA latihan, dan membahas soal simulasi UAS. | 110' | `[4]` Bab 4.4, `[5]` Bab 1–2 |
| **Penutup** | Membagikan kisi-kisi resmi **UAS Pekan 16 (Bobot 30%)**, kriteria Rubrik Analitik UAS, dan meminta mahasiswa mengisi survei refleksi ketercapaian `Sub-CPMK` di LMS Edlink. | Mengisi survei refleksi diri `STI-204` di Edlink dan mencatat kisi-kisi UAS. | 20' | Kisi-Kisi UAS & Survei Edlink |

* **Penugasan Terstruktur (`PT: 180'`) & Belajar Mandiri (`BM: 180'`):** Persiapan komprehensif menghadapi UAS menggunakan paket soal latihan pada Unit Evaluasi E2 Modul Ajar.

---

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **Kemampuan Akhir Diuji (`CPMK-4` [C4] & Sintesis Komprehensif `CPMK-1` s.d. `CPMK-4`):** Mengonstruksi model otomata berhingga (DFA dan NFA beserta konversinya ke DFA minimal) untuk pengenalan pola bahasa formal dan pemodelan transisi status sistem komputasi secara akurat.
* **Bentuk & Durasi:** Ujian Tertulis Komprehensif Terjadwal di Kelas (*Closed-Book*), **150 menit**.
* **Bobot Penilaian Sumatif:** **30%** terhadap Nilai Akhir Mata Kuliah.

| Tahap | Aktivitas Pengawas / Dosen | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan daftar hadir berita acara UAS, pembacaan tata tertib integritas akademik, dan pembagian naskah soal UAS. | Menandatangani daftar hadir dan menyiapkan peralatan ujian. | 10' | Berita Acara & Naskah UAS |
| **Pelaksanaan Ujian** | Mengawasi pelaksanaan ujian secara objektif dan tertib. | Mengerjakan 4 studi kasus konstruksi & sintesis (konstruksi 5-tupel DFA pengenal pola, perancangan NFA/$\varepsilon$-NFA & konversi *Subset Construction*, minimasi DFA & pemodelan *state machine* transaksi sistem, serta sintesis logika-graf-otomata). | 135' | Lembar Jawaban UAS |
| **Penutupan** | Mengumpulkan lembar jawaban, menutup perkuliahan semester secara resmi, dan menyampaikan jadwal publikasi rincian capaian `CPL-05` & `CPL-02` di Edlink/SIAKAD. | Menyerahkan lembar jawaban dan mengakhiri perkuliahan semester. | 5' | Bundel Jawaban UAS |

---

## BAGIAN III — PROTOKOL PENGELOLAAN KELAS, SINERGI KO-SEMESTER, & PENJAGAAN GUARDRAIL

1. **Sinergi Horizontal Semester 2 tanpa Tumpang Tindih:** Pada Semester 2, mahasiswa mengambil `STI-204 Matematika Diskrit dan Logika` bersamaan dengan `FST-203 Struktur Data dan Algoritma` dan `FST-207 Sistem Basis Data`. Dosen pengampu `STI-204` menjaga disiplin batas keilmuan: menggunakan contoh konteks struktur data (*Poset, Graf, Tree*) dan predikat kueri (*Aljabar Boolean*) murni pada **tataran representasi, pembuktian, dan penelusuran matematis di atas kertas**, sementara implementasi koding memori dan sintaks SQL fisik diserahkan penuh kepada kedua mata kuliah praktikum ko-semester tersebut.
2. **Penilaian Ketelitian Formal (*Formal Rigor*):** Dalam pembuktian logika/induksi (Pekan 1–4) maupun konstruksi graf/otomata (Pekan 9–16), kelengkapan pendefinisian notasi himpunan (seperti 5-tupel $M=(Q,\Sigma,\delta,q_0,F)$ dan penyebutan eksplisit nama aturan inferensi) merupakan bagian tak terpisahkan dari indikator penilaian.
