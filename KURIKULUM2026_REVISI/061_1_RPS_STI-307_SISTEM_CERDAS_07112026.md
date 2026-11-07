# 061_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-307 — SISTEM CERDAS (*Intelligent Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI307`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Sistem Cerdas / *Intelligent Systems* |
| **Kode Mata Kuliah** | `STI-307` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Kecerdasan Artifisial & Sains Data (*Core STI*) |
| **Bobot SKS & Tipe** | **2 SKS Teori** (`T = 2, P = 0`) — Tatap Muka `2×50' = 100'`, Penugasan Terstruktur `2×60' = 120'`, Belajar Mandiri `2×60' = 120'` per pekan |
| **Semester / Tahun Akademik** | Semester 3 (Ganjil) — Tahap Penguatan Penalaran Simbolik AI (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `STI-204` Matematika Diskrit dan Logika, `FST-204` Pengantar Kecerdasan Artifisial & Data |
| **Mata Kuliah Hilir (*Handoff*)** | `STI-413` Pembelajaran Mesin, `STI-414` Pengantar NLP & Temu Balik Informasi, `STA-501` Sistem Pendukung Keputusan, `STA-602` Sistem Agen Cerdas |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-06` (`P2`) dan `CPL-09` (`KK1`) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 3 (`K-3`)** — Kecerdasan Artifisial, Cloud & Cybersecurity (Skema Bobot MK Teori Dok 043/007: Tugas 1 `20%` · UTS `30%` · Tugas 2 `20%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Kecerdasan Artifisial & Sistem Cerdas |
| **Koordinator RMK** | Dr. Roni Wahyu, S.Kom., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-06`** (`P2`) | Pengetahuan | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital *(khususnya representasi pengetahuan simbolik & logika penalaran sistem cerdas bisnis)*. | **R** (*Reinforce*) | **50%** |
| **`CPL-09`** (`KK1`) | Keterampilan Khusus | Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas terintegrasi kecerdasan artifisial (AI/ML, NLP, Computer Vision, Smart Sys, DSS) guna memecahkan masalah kompleks organisasi dan industri. | **R** (*Reinforce*) | **50%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **menerapkan** algoritma pencarian heuristic (*A\*, Greedy Best-First, Minimax*) (*B*) pada permasalahan optimasi ruang status (*C*) dengan kompleksitas ruang/waktu terukur (*D*). | **C3** (*Apply*) | `CPL-06` (`P2`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **merancang** sistem pakar (*Expert System*) dengan metode penalaran *Forward Chaining* dan *Backward Chaining* (*B*) berbasis basis aturan (*C*) secara logis dan konsisten (*D*). | **C4** (*Analyze*) | `CPL-06` (`P2`), `CPL-09` (`KK1`) | **UTS — Pekan 8 (30%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **mengimplementasikan** sistem inferensi logika fuzzy (*Mamdani* dan *Sugeno*) (*B*) untuk pengambilan keputusan dalam kondisi ketidakpastian (*C*) menggunakan Python *Scikit-Fuzzy* (*D*). | **C4** (*Analyze*) | `CPL-09` (`KK1`), Sintesis `CPL-06` | **Tugas 2 — Pekan 12 (20%)** & **UAS Sintesis — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Menerapkan algoritma pencarian heuristik *A\** dan *Greedy Best-First* pada optimasi ruang status. | `CPMK-1` | **C3** | Mg 1–3 |
| **`Sub-CPMK-1.2`** | Menerapkan algoritma *Minimax* (beserta *Alpha-Beta Pruning*) pada permasalahan pengambilan keputusan bercabang. | `CPMK-1` | **C3** | Mg 4 |
| **`Sub-CPMK-2.1`** | Merancang sistem pakar dengan penalaran *Forward Chaining* berbasis basis aturan. | `CPMK-2` | **C4** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Merancang sistem pakar dengan penalaran *Backward Chaining* (serta penanganan ketidakpastian *Certainty Factor*) secara logis dan konsisten. | `CPMK-2` | **C4** | Mg 6–7 |
| **`Sub-CPMK-3.1`** | Mengimplementasikan sistem inferensi logika fuzzy metode *Mamdani* untuk pengambilan keputusan. | `CPMK-3` | **C4** | Mg 9–11 & 13 |
| **`Sub-CPMK-3.2`** | Mengimplementasikan sistem inferensi logika fuzzy metode *Sugeno* untuk pengambilan keputusan serta menyintesiskan sistem cerdas berbasis pengetahuan-fuzzy. | `CPMK-3` | **C4** | Mg 12–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[Sintesis Sistem Cerdas Hibrid Berbasis Aturan & Inferensi Fuzzy dengan Python Scikit-Fuzzy — Mg 13–16 (UAS 30%)]
      ▲
[CPMK-3: Sistem Inferensi Logika Fuzzy Mamdani & Sugeno untuk Ketidakpastian (C4) — Mg 9–13 (Tugas 2 20%)]
      ▲  (Sub-CPMK-3.1: Himpunan Fuzzy, Fuzzifikasi, Inferensi Mamdani Max-Min | Sub-CPMK-3.2: Inferensi Sugeno & Scikit-Fuzzy)
      │
[CPMK-2: Perancangan Sistem Pakar Forward & Backward Chaining Berbasis Aturan (C4) — Mg 5–8 (UTS 30%)]
      ▲  (Sub-CPMK-2.1: Representasi Pengetahuan & Forward Chaining | Sub-CPMK-2.2: Backward Chaining & Certainty Factor)
      │
[CPMK-1: Algoritma Pencarian Ruang Status Heuristik A*, Greedy, & Minimax (C3) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: Agen PEAS, BFS/DFS/UCS, Greedy Best-First, A* Admissible | Sub-CPMK-1.2: Minimax & Alpha-Beta Pruning)
      ▲
[Fondasi Prasyarat: STI-204 Matematika Diskrit dan Logika & FST-204 Pengantar Kecerdasan Artifisial & Data]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot | Kontribusi CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-06`** (`P2`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-06` = 50%** |
| **`CPL-06`** & **`CPL-09`** | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **30%**<br>*(15% P2 + 15% KK1)* | — | — | **30%** | *(20% + 15% + 15% P2)* |
| **`CPL-09`** (`KK1`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **20%** | — | **20%** | **`CPL-09` = 50%** |
| **`CPL-06`** & **`CPL-09`** | **Sintesis `CPMK-1..3`** | Penekanan utama `Sub-CPMK-3.1 & 3.2` + integrasi `CPMK-2` | — | — | — | **30%**<br>*(15% P2 + 15% KK1)* | **30%** | *(15% + 20% + 15% KK1)* |
| **Total** | **3 CPMK** | **6 Sub-CPMK** | **20%** | **30%** | **20%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 50\%$):** `Tugas 1 (20% — Case-Based Heuristic Route & Adversarial Search) + Tugas 2 (20% — Case-Based Mamdani vs Sugeno Fuzzy Design) + UAS (30% — Mini-Project & Ujian Evaluasi Sistem Cerdas Python Scikit-Fuzzy)` = **70%** ($\ge 50\%$, melampaui target minimal Dokumen 004 sebesar 60%).

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-307 Sistem Cerdas` (2 SKS Teori) meletakkan fondasi **Kecerdasan Artifisial Simbolik, Pencarian Ruang Status, dan Penalaran Ketidakpastian Berbasis Pengetahuan (*Knowledge-Based & Fuzzy Intelligent Systems*)** setelah mahasiswa menuntaskan logika formal pada `STI-204 Matematika Diskrit dan Logika` dan literasi AI pada `FST-204 Pengantar Kecerdasan Artifisial & Data`. Materi berfokus pada perancangan agen rasional (kerangka PEAS), algoritma pencarian tak terinformasi (*BFS, DFS, UCS*) dan heuristik terinformasi (*Greedy Best-First Search, A\*, Minimax* dengan *Alpha-Beta Pruning*), representasi pengetahuan (*Semantic Networks, Frames, Production Rules*), mesin inferensi sistem pakar (*Forward Chaining, Backward Chaining,* dan *Certainty Factor*), serta sistem inferensi logika *Fuzzy* metode **Mamdani** dan **Sugeno** yang disimulasikan menggunakan pustaka Python `scikit-fuzzy`.

* **🟢 IN-SCOPE (Wajib Diajarkan):** Kerangka agen PEAS, pencarian ruang status (*BFS, DFS, UCS, Greedy Best-First, A\*, Minimax, Alpha-Beta Pruning*), representasi pengetahuan simbolik, sistem pakar berbasis aturan (*Forward/Backward Chaining* & *Certainty Factor*), serta sistem inferensi logika *Fuzzy* (*Mamdani* & *Sugeno* dengan Python `scikit-fuzzy`) dan arsitektur hibrid *Rule-Fuzzy*.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Kurikulum Dok 037 & 043):**
  1. **Dilarang keras** mengajarkan algoritma *Machine Learning* statistik/probabilistik (`scikit-learn` regresi, pohon keputusan data-driven, SVM, *clustering*) maupun *Perceptron / Artificial Neural Networks / Deep Learning* — seluruh materi tersebut menjadi ranah eksklusif **`STI-413 Pembelajaran Mesin`** (Semester 4) dan **`STI-624 Pembelajaran Mendalam & Jaringan Saraf`** (Semester 6).
  2. Dilarang mengajarkan pemrosesan teks bahasa alami atau *word embeddings* (ranah **`STI-414 Pengantar NLP & Temu Balik Informasi`**).
  3. Dilarang mengajarkan *Multi-Agent Systems* & *Reinforcement Learning* (ranah **`STA-602 Sistem Agen Cerdas`**) maupun metode MCDM *AHP/TOPSIS/SAW* (ranah **`STA-501 Sistem Pendukung Keputusan`**).
* **🔄 HANDOFF ANCHOR:** Menuntaskan paradigma AI simbolik & penalaran *white-box* berbasis aturan/fuzzy, kemudian menyerahkan paradigma pembelajaran berbasis data probabilistik ke **`STI-413 Pembelajaran Mesin`**, teks ke **`STI-414`**, SPK multikriteria ke **`STA-501`**, dan agen otonom ke **`STA-602`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS16` (*Artificial Intelligence & Intelligent Systems*) & `BK-IT02` (*Applied AI & Intelligent Technologies*).

**Pustaka Utama:**
1. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. *(Bab 1–5 & Bab 7–9: Intelligent Agents, Search, Adversarial Search, Logical Knowledge-Based Agents)*.
2. Giarratano, J. C., & Riley, G. D. (2005). *Expert Systems: Principles and Programming* (4th ed.). Course Technology.
3. Ross, T. J. (2016). *Fuzzy Logic with Engineering Applications* (4th ed.). Wiley.
4. Kusumadewi, S., & Purnomo, H. (2013). *Aplikasi Logika Fuzzy untuk Pendukung Keputusan* (Edisi ke-2). Graha Ilmu.

**Pustaka Pendukung & Perangkat Komputasi:**
5. Dokumentasi Resmi Python `scikit-fuzzy` (`skfuzzy.control`) & `NetworkX` untuk visualisasi ruang status dan kurva fungsi keanggotaan *fuzzy*.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Pengantar):** Menguraikan konsep agen cerdas, rasionalitas, dan spesifikasi lingkungan **PEAS** [C2→C3] | 1.1.1 Ketepatan membedakan AI simbolik (*knowledge-driven*) vs AI statistik (*data-driven*).<br>1.1.2 Ketepatan merumuskan *Performance, Environment, Actuators, Sensors* (PEAS) dan sifat lingkungan (*observable, deterministic, episodic, static, discrete*). | **Kriteria:** Kuis diagnostik formatif.<br>**Teknik:** Diskusi pemetaan PEAS pada kasus sistem cerdas industri. | **Kuliah Interaktif & Diskusi Kasus**<br>`[TM: 2×50' = 100']`<br>Analisis spesifikasi PEAS untuk 4 studi kasus bisnis/layanan publik:<br>`[PT: 120']` · `[BM: 120']` | Kontrak perkuliahan, unduh modul & panduan instalasi Python `scikit-fuzzy` di LMS Edlink. | Kontrak Belajar, Paradigma Sistem Cerdas Simbolik vs Pembelajaran Mesin, Arsitektur Agen Rasional & Lingkungan PEAS `[1] Bab 1–2` | — |
| **2** | **`Sub-CPMK-1.1`:** Merumuskan ruang status (*state space*) dan menelusuri algoritma pencarian buta (*BFS, DFS, Uniform-Cost Search*) [C3] | 1.1.3 Ketepatan memodelkan masalah sebagai tupel `(Initial State, Actions, Transition, Goal Test, Path Cost)`.<br>1.1.4 Ketepatan menelusuri antrean *frontier* pada *BFS, DFS,* dan *UCS* beserta perbandingan *completeness, optimality, time & space complexity*. | **Kriteria:** Ketepatan jejak *search tree*.<br>**Teknik:** Latihan penelusuran graf ruang status di kelas. | **Problem-Solving Class**<br>`[TM: 2×50' = 100']`<br>Latihan penelusuran rute logistik dengan BFS, DFS, dan UCS:<br>`[PT: 120']` · `[BM: 120']` | Kuis mandiri kompleksitas *Big-O* pencarian buta di LMS Edlink. | Formulasi Masalah Ruang Status & *Uninformed Search*: *Breadth-First Search (BFS), Depth-First Search (DFS), Uniform-Cost Search (UCS)* `[1] Bab 3` | — |
| **3** | **`Sub-CPMK-1.1`:** Menerapkan algoritma pencarian heuristik **Greedy Best-First Search** dan **A\* (*A-Star*)** pada optimasi ruang status [C3] | 1.1.5 Ketepatan mengevaluasi fungsi $f(n) = h(n)$ (*Greedy*) vs $f(n) = g(n) + h(n)$ (*A\**).<br>1.1.6 Ketepatan membuktikan syarat *admissibility* ($0 \le h(n) \le h^*(n)$) dan *consistency* heuristik agar *A\** menjamin solusi optimal. | **Kriteria:** Ketepatan tabel ekspansi simpul `OPEN`/`CLOSED`.<br>**Teknik:** *Workshop* perhitungan manual rute optimal *A\**. | **Problem-Solving Workshop *Heuristic Search***<br>`[TM: 2×50' = 100']`<br>Pengerjaan bagian awal *problem set* Tugas 1:<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi instruksi **Tugas 1 (RTM-1)** di LMS Edlink. | *Informed (Heuristic) Search*: Fungsi Heuristik, *Greedy Best-First Search*, Algoritma **A\***, Sifat *Admissible & Consistent Heuristics* `[1] Bab 3` | — |
| **4** | **`Sub-CPMK-1.2`:** Menerapkan algoritma **Minimax** dan **Alpha-Beta Pruning** pada keputusan kompetitif bercabang [C3]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 1.2.1 Ketepatan menghitung nilai propagasi balik simpul `MAX` dan `MIN` pada pohon permainan.<br>1.2.2 Ketepatan memangkas cabang tak relevan dengan batas $\alpha$ dan $\beta$ serta menghitung penghematan evaluasi simpul. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-3`)**.<br>**Teknik:** Pengumpulan *Problem Set* Pencarian Heuristik & *Adversarial* + Kuis Verifikasi Kelas 15'. | **Case-Based Learning & Verifikasi Tugas 1**<br>`[TM: 2×50' = 100']`<br>Latihan pemangkasan pohon keputusan $\alpha\text{-}\beta$:<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas **Tugas 1 (`CPMK-1`)** di LMS Edlink. | *Adversarial Search*: Pohon Permainan Dua Agen, Algoritma **Minimax**, & Optimasi **Alpha-Beta Pruning** `[1] Bab 5` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1`:** Menyusun arsitektur **Sistem Pakar** dan representasi pengetahuan berbasis aturan (*Semantic Networks, Frames, Production Rules*) [C4] | 2.1.1 Ketepatan memetakan komponen *Knowledge Base, Working Memory, Inference Engine, Explanation Facility,* dan *Knowledge Acquisition*.<br>2.1.2 Ketepatan menerjemahkan pengetahuan pakar domain menjadi aturan produksi `IF–THEN` yang bebas kontradiksi dan siklus tak berujung. | **Kriteria:** Kelengkapan & konsistensi basis aturan.<br>**Teknik:** Latihan akuisisi aturan diagnosis kerusakan perangkat/kelayakan kredit. | **Ceramah Interaktif & Latihan Basis Pengetahuan**<br>`[TM: 2×50' = 100']`<br>Perancangan tabel fakta dan minimal 15 aturan produksi berantai:<br>`[PT: 120']` · `[BM: 120']` | Forum diskusi perbedaan aturan prosedural `if-else` biasa vs *Knowledge Base* terpisah di Edlink. | Arsitektur *Expert Systems*, Representasi Pengetahuan (*Semantic Nets, Frames, Production Rules*), & Resolusi Konflik Aturan `[1] Bab 7; [2] Bab 1–3` | — |
| **6** | **`Sub-CPMK-2.1` & `Sub-CPMK-2.2`:** Merancang dan menelusuri mesin inferensi **Forward Chaining** (*Data-Driven*) vs **Backward Chaining** (*Goal-Driven*) [C4] | 2.1.3 Ketepatan menelusuri siklus *Match–Conflict Resolution–Act* pada *Forward Chaining* beserta perubahan *Working Memory*.<br>2.2.1 Ketepatan menelusuri pohon sub-tujuan rekursif pada *Backward Chaining* dan memilih metode yang tepat sesuai rasio fakta awal terhadap jumlah hipotesis tujuan. | **Kriteria:** Ketepatan tabel jejak inferensi.<br>**Teknik:** Bedah kasus pembandingan *Forward* vs *Backward Chaining*. | **Case Method Class (*Inference Engine Trace*)**<br>`[TM: 2×50' = 100']`<br>Penelusuran lengkap satu kasus sistem pakar dengan kedua metode:<br>`[PT: 120']` · `[BM: 120']` | Latihan interaktif penelusuran pohon *Backward Chaining* di LMS Edlink. | Mesin Inferensi Sistem Pakar: Penalaran **Forward Chaining** vs **Backward Chaining**, Strategi Resolusi Konflik, & Kriteria Pemilihan Metode `[2] Bab 4–6` | — |
| **7** | **`Sub-CPMK-2.2`:** Menghitung penalaran ketidakpastian pada sistem pakar menggunakan **Certainty Factor (CF)** & Klinik Pra-UTS [C4] | 2.2.2 Ketepatan menghitung $CF(H,E) = MB - MD$, aturan premis majemuk (`AND` = $\min$, `OR` = $\max$), serta kombinasi bukti paralel $CF_{\text{combine}}(CF_1, CF_2)$.<br>2.2.3 Kesiapan mengaudit konsistensi basis aturan jelang UTS. | **Kriteria:** Presisi perhitungan nilai keyakinan $CF \in [-1, 1]$.<br>**Teknik:** Latihan studi kasus diagnosis dengan bobot keyakinan pakar & pengguna. | **Problem-Solving Class *Certainty Factor***<br>`[TM: 2×50' = 100']`<br>Persiapan komprehensif menghadapi UTS Pekan 8:<br>`[PT: 120']` · `[BM: 120']` | Kuis simulasi UTS di LMS Edlink. | Penanganan Ketidakpastian Sistem Pakar: Teori **Certainty Factor (CF)** Shortliffe-Buchanan & Konsolidasi Materi Pekan 1–7 `[2] Bab 7–8` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C4]** | Ketepatan merancang basis aturan sistem pakar yang konsisten, menelusuri inferensi *Forward Chaining* dan *Backward Chaining*, serta menghitung tingkat keyakinan kesimpulan dengan *Certainty Factor*. | **Kriteria:** **Rubrik Analitik UTS (`K-3`)**.<br>**Teknik:** Ujian tertulis studi kasus terjadwal (*Closed-Book*). | **Ujian Tertulis Luring Terjadwal**<br>`[100 menit]` | Pengarsipan nilai `CPMK-2` pada sistem OBE/Edlink. | Materi Sistem Pakar Berbasis Aturan, *Forward/Backward Chaining*, & *Certainty Factor* (fokus utama Pekan 5–7) | **30%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1`:** Membedakan himpunan tegas (*Crisp Set*) vs himpunan kabur (*Fuzzy Set*) serta menerapkan operator logika *Fuzzy* [C3→C4] | 3.1.1 Ketepatan menjelaskan konsep variabel linguistik, semesta pembicaraan, dan derajat keanggotaan $\mu_A(x) \in [0, 1]$.<br>3.1.2 Ketepatan menghitung operasi himpunan *Fuzzy* (*Zadeh Intersection* $\min$, *Union* $\max$, *Complement* $1-\mu$). | **Kriteria:** Ketepatan perhitungan $\mu(x)$.<br>**Teknik:** Latihan transformasi batasan bisnis kaku menjadi variabel linguistik *fuzzy*. | **Kuliah Interaktif & Latihan Dasar Fuzzy**<br>`[TM: 2×50' = 100']`<br>Identifikasi variabel linguistik input/output untuk studi kasus kelompok:<br>`[PT: 120']` · `[BM: 120']` | Unduh lembar rumus kurva keanggotaan *fuzzy* di LMS Edlink. | Pengantar Teori Himpunan *Fuzzy* Lotfi Zadeh: *Crisp vs Fuzzy*, Variabel Linguistik, & Operasi Dasar Himpunan *Fuzzy* `[3] Bab 1–2; [4] Bab 2` | — |
| **10** | **`Sub-CPMK-3.1`:** Merancang fungsi keanggotaan (*Fuzzifikasi*: Linear Naik/Turun, Segitiga, Trapesium, Bahu, & Gaussian) [C4] | 3.1.3 Ketepatan merumuskan persamaan matematis sepotong-sepotong (*piecewise*) kurva segitiga, trapesium, dan bahu untuk batas domain nyata.<br>3.1.4 Ketepatan menghitung nilai derajat keanggotaan hasil *fuzzifikasi* suatu masukan numerik tegas (*crisp input*). | **Kriteria:** Ketepatan grafik & rumus domain kurva.<br>**Teknik:** Latihan perancangan partisi fungsi keanggotaan 3–5 himpunan linguistik. | **Problem-Solving Class *Fuzzification***<br>`[TM: 2×50' = 100']`<br>Perancangan kurva keanggotaan kasus penilaian kredit/suhu gudang/kinerja vendor:<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi instruksi **Tugas 2 (RTM-2)** di LMS Edlink. | Tahap **Fuzzifikasi**: Perancangan Kurva Linear, Segitiga (*Triangular*), Trapesium (*Trapezoidal*), Bahu, & *Gaussian* `[3] Bab 4; [4] Bab 2` | — |
| **11** | **`Sub-CPMK-3.1`:** Menyusun dan menghitung mesin inferensi *Fuzzy* metode **Mamdani** (*Min Implication, Max Aggregation, & Centroid Defuzzification*) [C4] | 3.1.5 Ketepatan menghitung nilai $\alpha\text{-predikat}$ tiap aturan fuzzy, pemotongan daerah himpunan keluaran (*clipping*), agregasi komposisi `Max-Min`, dan titik pusat massa **Centroid (COA)** secara analitis/diskrit. | **Kriteria:** Ketepatan langkah perhitungan manual Mamdani.<br>**Teknik:** *Case-Based Learning* perhitungan 4 aturan aktif metode Mamdani. | **Case-Based Learning Inferensi Mamdani**<br>`[TM: 2×50' = 100']`<br>Perhitungan tangan lengkap kasus *Fuzzy Mamdani* pada lembar kerja:<br>`[PT: 120']` · `[BM: 120']` | Video panduan visualisasi *Centroid Defuzzification* di LMS Edlink. | *Fuzzy Inference System* (FIS) **Metode Mamdani**: Implikasi `Min`, Komposisi Aturan `Max`, & Metode Defuzzifikasi (*Centroid, Bisector, MOM*) `[3] Bab 5; [4] Bab 3` | — |
| **12** | **`Sub-CPMK-3.2`:** Menyusun dan menghitung mesin inferensi *Fuzzy* metode **Takagi-Sugeno-Kang (Sugeno)** Orde-0 & Orde-1 [C4]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 3.2.1 Ketepatan menghitung keluaran tegas tiap aturan ($z_i = k$ atau $z_i = p_i x + q_i y + r_i$) dan rata-rata terbobot (*Weighted Average* $Z = \frac{\sum \alpha_i z_i}{\sum \alpha_i}$).<br>3.2.2 Ketepatan membandingkan efisiensi komputasi Sugeno vs interpretabilitas Mamdani. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-3`)**.<br>**Teknik:** Pengumpulan Studi Kasus Perhitungan Komparatif Mamdani vs Sugeno + Kuis Verifikasi 15'. | **Problem-Solving Workshop Sugeno & Verifikasi Tugas 2**<br>`[TM: 2×50' = 100']`<br>Eksplorasi awal notebook simulasi `scikit-fuzzy`:<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas **Tugas 2 (`CPMK-3`)** di LMS Edlink. | *Fuzzy Inference System* **Metode Sugeno** (Orde-0 & Orde-1), *Weighted Average Defuzzification*, & Komparasi Mamdani vs Sugeno `[3] Bab 5; [4] Bab 4` | **20%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-3.1` & `Sub-CPMK-3.2`:** Mengimplementasikan sistem inferensi *Fuzzy* menggunakan pustaka Python **`scikit-fuzzy`** [C4] | 3.2.3 Ketepatan mendefinisikan `Antecedent`, `Consequent`, fungsi keanggotaan (`trimf`, `trapmf`), `Rule`, `ControlSystem`, dan `ControlSystemSimulation` di Python.<br>3.2.4 Kesesuaian keluaran program Python dengan perhitungan manual di atas kertas. | **Kriteria:** Kebenaran eksekusi skrip & kecocokan verifikasi.<br>**Teknik:** Demonstrasi *live notebook* & eksperimen permukaan kontrol 3D (*control surface*). | **Demo Terbimbing & Workshop Komputasi `scikit-fuzzy`**<br>`[TM: 2×50' = 100']`<br>Implementasi model *fuzzy* studi kasus mini dalam Jupyter Notebook:<br>`[PT: 120']` · `[BM: 120']` | Unggah latihan notebook `.ipynb` `scikit-fuzzy` di LMS Edlink. | Implementasi Komputasi FIS dengan Python **`scikit-fuzzy`**: Pemodelan Variabel, Aturan, Simulasi, & Visualisasi *3D Control Surface* `[5]` | — |
| **14** | **Sintesis `CPMK-2` & `CPMK-3`:** Merancang arsitektur **Sistem Cerdas Hibrid Simbolik (*Rule-Based Expert + Fuzzy Inference*)** & Pengujian Sensitivitas Aturan [C4] | 3.2.5 Ketepatan mengintegrasikan pra-penyaringan aturan logika tegas (*Forward/Backward Chaining*) dengan mesin inferensi *Fuzzy* pada masalah bisnis bernuansa.<br>3.2.6 Ketepatan menganalisis sensitivitas perubahan batas kurva keanggotaan terhadap stabilitas keputusan *(tanpa pelatihan ML/Neural Network sesuai guardrail!)*. | **Kriteria:** Rasionalitas arsitektur hibrid & ketajaman analisis sensitivitas.<br>**Teknik:** Bedah arsitektur & *tuning* parameter fungsi keanggotaan berbasis pengetahuan pakar. | **Case Method Workshop (*Hybrid Expert-Fuzzy Architecture*)**<br>`[TM: 2×50' = 100']`<br>Penyempurnaan purwarupa mini-proyek sistem cerdas Python:<br>`[PT: 120']` · `[BM: 120']` | Panduan batas tegas *White-Box Symbolic/Fuzzy AI* (`STI-307`) vs *Data-Driven ML* (`STI-413`) di Edlink. | Arsitektur Hibrid *Expert-Fuzzy Decision System*, Validasi Konsistensi & Uji Sensitivitas Kurva, serta Peta *Handoff* ke `STI-413 Pembelajaran Mesin` `[2] Bab 10; [4] Bab 6` | — |
| **15** | **Review & Konsolidasi `CPMK-1..3`:** Klinik Verifikasi *Mini-Project* Python `scikit-fuzzy` & Persiapan Evaluasi Akhir [C4] | 3.2.7 Keterulangan eksekusi (*reproducibility*) notebook sistem cerdas dan ketepatan interpretasi hasil uji skenario batas (*edge cases*). | **Kriteria:** Ceklis *reproducibility* & kelengkapan dokumentasi.<br>**Teknik:** *Code & Rule Walkthrough* pra-UAS di kelas. | **Presentasi Ringkas & Klinik Pra-UAS**<br>`[TM: 2×50' = 100']`<br>Finalisasi laporan & latihan soal komprehensif UAS:<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas notebook & laporan ringkas sistem cerdas di LMS Edlink. | Konsolidasi Pencarian Heuristik, Sistem Pakar, & Sistem Inferensi *Fuzzy* serta Evaluasi Skenario Uji Batas `[1]; [2]; [3]; [5]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-3` & Sintesis `CPMK-1..3` [C4]** | Ketepatan implementasi & analisis sistem inferensi *Fuzzy* dengan Python `scikit-fuzzy` (40% UAS) serta ketajaman penyelesaian ujian komprehensif tertulis atas inferensi *Fuzzy* dan integrasi sistem cerdas berbasis aturan (60% UAS). | **Kriteria:** **Rubrik Analitik UAS (`K-3`)**.<br>**Teknik:** Penilaian Purwarupa Notebook Python `scikit-fuzzy` Terverifikasi (40% UAS) + Ujian Tertulis Komprehensif Luring (60% UAS, 100 menit). | **Ujian Tertulis Komprehensif & Verifikasi Karya Individu**<br>`[100 menit]` | Pengarsipan portofolio dan rekap nilai `CPL-06` & `CPL-09` di portal OBE. | Evaluasi Komprehensif Sistem Inferensi Logika *Fuzzy* (*Mamdani & Sugeno*), `scikit-fuzzy`, & Sintesis Sistem Cerdas | **30%**<br>*(UAS — `CPMK-3` & Sintesis)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-06` [C3])
* **Bentuk Instrumen:** *Problem Set* Mandiri Berparameter NIM: (1) Formulasi ruang status & penelusuran tabel ekspansi `OPEN`/`CLOSED` algoritma **Greedy Best-First** vs **A\*** pada jaringan distribusi logistik disertai pembuktian *admissibility* heuristik; (2) Penelusuran pohon keputusan **Minimax** 4 lapis dengan **Alpha-Beta Pruning** beserta analisis kompleksitas waktu/ruang (+ kuis konfirmasi 15 menit di kelas).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan formulasi ruang status & sifat heuristik *admissible* = **30%**; (2) Keruntutan penelusuran *Greedy, A\*,* & pemangkasan *Alpha-Beta* = **45%**; (3) Presisi jalur biaya optimal & analisis kompleksitas = **25%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 30% · Mengukur `CPMK-2` / `CPL-06` 15% + `CPL-09` 15% [C4])
* **Bentuk Instrumen:** Ujian Tertulis Luring Terjadwal (*Closed-Book*, 100 menit, 3 studi kasus): (1) Perancangan basis pengetahuan sistem pakar (minimal 10 aturan berantai bebas kontradiksi) dari narasi pakar domain; (2) Penelusuran meja lengkap (*working memory & conflict set trace*) dengan **Forward Chaining** dan pohon sub-tujuan **Backward Chaining**; (3) Perhitungan tingkat keyakinan diagnosis akhir menggunakan **Certainty Factor (CF)**.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan struktur & konsistensi logika basis aturan `IF–THEN` = **35%**; (2) Ketepatan jejak mesin inferensi *Forward* & *Backward Chaining* = **40%**; (3) Akurasi perhitungan *Certainty Factor* & rekomendasi kesimpulan = **25%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 20% · Mengukur `CPMK-3` / `CPL-09` [C4])
* **Bentuk Instrumen:** Studi Kasus Analitis Komparatif **Fuzzy Mamdani vs Fuzzy Sugeno** Berparameter NIM (individu + kuis verifikasi 15 menit): merancang kurva fungsi keanggotaan 2 variabel input & 1 variabel output, menyusun matriks 9 aturan *fuzzy*, serta menghitung secara manual langkah demi langkah keluaran tegas metode **Mamdani** (*Centroid*) dan metode **Sugeno** (*Weighted Average*) untuk vektor uji spesifik.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan desain fungsi keanggotaan & perhitungan *fuzzifikasi* = **30%**; (2) Ketepatan inferensi implikasi/komposisi & defuzzifikasi Mamdani vs Sugeno = **45%**; (3) Analisis perbandingan hasil keputusan kedua metode = **25%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-3` & Sintesis / `CPL-06` 15% + `CPL-09` 15% [C4])
* **Bentuk Instrumen:** Terdiri atas **Purwarupa Notebook Python `scikit-fuzzy` Terverifikasi (40% nilai UAS)** yang memodelkan pengambil keputusan cerdas (bebas *Machine Learning* `scikit-learn` / *Neural Network* sesuai *guardrail*) dan membandingkannya dengan hitungan manual, ditambah **Ujian Tertulis Komprehensif Luring 100 Menit (60% nilai UAS)** yang menguji penguasaan analitis FIS, penelusuran kode `scikit-fuzzy`, serta sintesis arsitektur sistem cerdas berbasis aturan-fuzzy.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Metodologi pemodelan sistem inferensi *fuzzy* & kepatuhan *guardrail* simbolik = **35%**; (2) Kebenaran komputasi `scikit-fuzzy` & presisi perhitungan ujian tertulis = **35%**; (3) Ketajaman analisis sensitivitas/skenario batas = **20%**; (4) *Reproducibility* & dokumentasi notebook = **10%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Kecerdasan Artifisial & Sistem Cerdas**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Roni Wahyu, S.Kom., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
