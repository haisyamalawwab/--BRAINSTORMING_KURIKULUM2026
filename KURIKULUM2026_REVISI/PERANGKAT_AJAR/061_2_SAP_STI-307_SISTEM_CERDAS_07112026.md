# 061_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-307 — SISTEM CERDAS (*Intelligent Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI307` · **Bobot:** 2 SKS Teori (`TM 100'`, `PT 120'`, `BM 120'`) · **Semester:** 3  
**Prasyarat:** `STI-204` Matematika Diskrit dan Logika, `FST-204` Pengantar Kecerdasan Artifisial & Data  
**CPL:** `CPL-06` (`P2` = 50%) & `CPL-09` (`KK1` = 50%) [Level `R`] · **Klaster Rubrik:** `K-3`  
**Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu `STI-307` |
|---|---|
| **Alokasi Waktu 2 SKS Teori** | **Pendahuluan `15'` · Kegiatan Inti `70'` · Penutup & Refleksi `15'`** (Total Tatap Muka = `100 menit`), diikuti `PT 120'` dan `BM 120'`. |
| **Fokus Keilmuan (*In-Scope*)** | Agen cerdas PEAS, pencarian ruang status (*BFS, DFS, UCS, Greedy Best-First, A\*, Minimax + Alpha-Beta*), sistem pakar (*Forward/Backward Chaining, Certainty Factor*), serta sistem inferensi logika *Fuzzy* (*Mamdani & Sugeno* dengan Python `scikit-fuzzy`). |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang keras** mengajarkan pelatihan model *Machine Learning* statistik (`scikit-learn`), *Perceptron / Neural Network / Deep Learning* (ranah **`STI-413 Pembelajaran Mesin`** & **`STI-624 Pembelajaran Mendalam & Jaringan Saraf`**), NLP (**`STI-414`**), *Multi-Agent/RL* (**`STA-602`**), maupun SPK *AHP/TOPSIS* (**`STA-501`**). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Perkuliahan | Metode Utama | Waktu TM | Evaluasi |
|:---:|:---:|---|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Pengantar Sistem Cerdas Simbolik, Agen Rasional, & Lingkungan PEAS | Kuliah Interaktif & Studi Kasus | 100' | Formatif |
| **2** | `Sub-CPMK-1.1` | Formulasi Ruang Status & *Uninformed Search* (*BFS, DFS, UCS*) | *Problem-Solving Class* | 100' | Formatif |
| **3** | `Sub-CPMK-1.1` | *Informed Search*: Fungsi Heuristik, *Greedy Best-First*, & Algoritma **A\*** | *Problem-Solving Workshop* | 100' | Formatif |
| **4** | `Sub-CPMK-1.2` | *Adversarial Search*: Algoritma **Minimax** & **Alpha-Beta Pruning** | *Case-Based Learning* | 100' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Arsitektur Sistem Pakar & Representasi Pengetahuan (*Rules, Frames, Semantic Net*) | Ceramah & Latihan Aturan | 100' | Formatif |
| **6** | `Sub-CPMK-2.1, 2.2` | Mesin Inferensi Sistem Pakar: **Forward Chaining** vs **Backward Chaining** | *Case Method Class* | 100' | Formatif |
| **7** | `Sub-CPMK-2.2` | Penalaran Ketidakpastian pada Sistem Pakar: Teori **Certainty Factor (CF)** | *Problem-Solving Class* | 100' | Formatif |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** Sistem Pakar, *Chaining*, & *Certainty Factor* | Ujian Tertulis Terjadwal | 100' | **UTS (30%)** |
| **9** | `Sub-CPMK-3.1` | Teori Himpunan *Fuzzy*: *Crisp vs Fuzzy*, Variabel Linguistik, & Operator Zadeh | Kuliah & Latihan Konsep | 100' | Formatif |
| **10** | `Sub-CPMK-3.1` | **Fuzzifikasi**: Perancangan Kurva Segitiga, Trapesium, Bahu, & *Gaussian* | *Problem-Solving Class* | 100' | Formatif |
| **11** | `Sub-CPMK-3.1` | *Fuzzy Inference System* Metode **Mamdani** (*Max-Min* & *Centroid*) | *Case-Based Learning* | 100' | Formatif |
| **12** | `Sub-CPMK-3.2` | *Fuzzy Inference System* Metode **Sugeno** & Komparasi Mamdani–Sugeno | *Problem-Solving Workshop* | 100' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-3.1, 3.2` | Implementasi Komputasi Logika *Fuzzy* dengan Python **`scikit-fuzzy`** | Demo & *Live Notebook* | 100' | Formatif |
| **14** | Sintesis `2 & 3` | Arsitektur Hibrid *Rule-Fuzzy Decision System* & Analisis Sensitivitas Kurva | *Case Method Workshop* | 100' | Formatif |
| **15** | `CPMK-1..3` | Klinik Verifikasi Purwarupa `scikit-fuzzy` & Konsolidasi Pra-UAS | *Walkthrough* & Konsultasi | 100' | Formatif |
| **16** | `CPMK-3` & Sintesis | **Evaluasi Akhir Semester (UAS):** Verifikasi `scikit-fuzzy` & Ujian Komprehensif | Ujian Tertulis + Verifikasi | 100' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN

### PERTEMUAN 1 — Pengantar Sistem Cerdas Simbolik, Agen Rasional, & Lingkungan PEAS
* **Sub-CPMK:** `Sub-CPMK-1.1` (Pengantar, C2→C3) · **Media:** Salindia Bab 1, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menyampaikan kontrak belajar, memetakan kelanjutan langsung dari logika proposisi/predikat `STI-204 Matematika Diskrit dan Logika` dan taksonomi AI `FST-204`, serta menegaskan kapan organisasi membutuhkan *White-Box Symbolic/Fuzzy AI* dibanding *Black-Box Machine Learning*. | Menyimak posisi mata kuliah pada alur AI SISTEKIN dan menjawab kuis diagnostik 5 soal di LMS Edlink. | 15' | RPS `061_1` |
| **Kegiatan Inti** | Menjelaskan konsep *Rational Agent*, pemetaan **PEAS** (*Performance measure, Environment, Actuators, Sensors*), dan 6 dimensi sifat lingkungan tugas (*fully vs partially observable, deterministic vs stochastic, episodic vs sequential, static vs dynamic, discrete vs continuous, single vs multi-agent*). | Dalam kelompok kecil membedah spesifikasi PEAS dan sifat lingkungan untuk 3 sistem: (a) Penjadwalan Rute Kurir Kota, (b) Sistem Pakar Triage Klinik, dan (c) Pengendali Suhu *Cold-Storage* Pertanian. | 70' | `[1]` Bab 1–2 |
| **Penutup** | Merangkum kaitan sifat lingkungan dengan pemilihan teknik AI (pencarian, aturan, atau *fuzzy*). | Mencatat tugas mandiri analisis PEAS di LMS Edlink. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menyusun tabel analisis PEAS untuk 4 domain layanan bisnis dan membaca Russell & Norvig Bab 3.

---

### PERTEMUAN 2 — Formulasi Ruang Status & *Uninformed Search* (*BFS, DFS, UCS*)
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Media:** Papan Tulis, Graf Rute Kota Jawa Timur, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan peta jaringan jalan antar-gudang distribusi di Malang Raya dan bertanya bagaimana komputer mencari rute terbaik secara sistematis dari graf yang telah dipelajari di `STI-204 Matematika Diskrit dan Logika`. | Mengidentifikasi simpul awal, tujuan, dan bobot jarak/waktu tempuh pada graf. | 15' | `[1]` Bab 3 |
| **Kegiatan Inti** | Mengajarkan formulasi formal masalah ruang status, perbedaan struktur antrean *frontier* FIFO (*Breadth-First Search*), tumpukan LIFO (*Depth-First Search*), dan antrean berprioritas biaya kumulatif $g(n)$ (*Uniform-Cost Search*), lengkap dengan evaluasi 4 kriteria: *Completeness, Optimality, Time Complexity, & Space Complexity* dalam parameter $b, d, m$. | Menelusuri langkah demi langkah isi `OPEN` (*frontier*) dan `CLOSED` (*explored set*) untuk graf berbobot 8 simpul menggunakan BFS, DFS, dan UCS. | 70' | `[1]` Bab 3 |
| **Penutup** | Membandingkan mengapa BFS gagal optimal saat bobot tepi berbeda-beda sedangkan UCS optimal namun lambat karena mencari ke segala arah. | Menyimpulkan motivasi perlunya fungsi pemandu arah (*heuristik*) pada pekan depan. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Mengerjakan 5 soal penelusuran BFS, DFS, dan UCS beserta analisis kompleksitasnya.

---

### PERTEMUAN 3 — Pencarian Heuristik: *Greedy Best-First Search* & Algoritma **A\***
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Media:** Lembar Kerja Penelusuran *A\**, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Memperkenalkan intuisi jarak garis lurus (*Euclidean/Manhattan distance*) sebagai estimasi biaya sisa menuju tujuan $h(n)$. | Menghitung nilai heuristik Manhattan pada contoh kisi (*grid*) gudang otomatis. | 15' | `[1]` Bab 3 |
| **Kegiatan Inti** | Menjelaskan cara kerja **Greedy Best-First Search** ($f(n)=h(n)$ — cepat tetapi dapat terjebak jalur suboptimal) vs **Algoritma A\*** ($f(n)=g(n)+h(n)$), lalu membuktikan mengapa syarat **Admissible Heuristic** ($0 \le h(n) \le h^*(n)$, tidak pernah *overestimate*) dan **Consistent/Monotonic Heuristic** ($h(n) \le c(n,a,n') + h(n')$) menjamin optimalitas *A\**. | Mengeksekusi penelusuran lengkap tabel `OPEN`/`CLOSED` algoritma *Greedy* dan *A\** pada satu graf logistik yang sengaja memuat jebakan heuristik menipu, lalu membandingkan total biaya rute keduanya. | 70' | `[1]` Bab 3 |
| **Penutup** | Merilis instruksi resmi **Tugas 1 (RTM-1)** yang akan dikumpulkan pada Pekan 4. | Mencatat parameterisasi NIM dan kriteria rubrik Tugas 1. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menyelesaikan bagian *Heuristic Search* pada **Tugas 1**.

---

### PERTEMUAN 4 — *Adversarial Search*: **Minimax** & **Alpha-Beta Pruning** (+ Tugas 1)
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Media:** Pohon Permainan, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Melaksanakan kuis konfirmasi tertulis 15 menit atas pengerjaan **Tugas 1 (`CPMK-1`)**. | Mengerjakan kuis verifikasi *A\** dan heuristik secara mandiri (*closed-book*). | 20' | Instrumen T1 |
| **Kegiatan Inti** | Menguraikan pencarian pada lingkungan kompetitif dua agen berlawanan tujuan (*zero-sum*): propagasi nilai utilitas dari daun ke akar pada **Minimax** (`MAX` memilih maksimum, `MIN` memilih minimum), diikuti teknik **Alpha-Beta Pruning** ($\alpha$ batas bawah terbaik `MAX`, $\beta$ batas atas terbaik `MIN`, pangkas saat $\alpha \ge \beta$) yang memangkas kompleksitas efektif dari $O(b^m)$ menuju $O(b^{m/2})$. | Menelusuri dari kiri ke kanan pohon permainan kedalaman 4, menghitung nilai Minimax tiap simpul internal, dan memberi tanda silang eksplisit pada cabang-cabang yang terpotong oleh syarat $\alpha \ge \beta$. | 65' | `[1]` Bab 5 |
| **Penutup** | Membahas bagaimana urutan penjelajahan simpul memengaruhi banyaknya cabang yang berhasil dipangkas. | Mengumpulkan berkas final **Tugas 1** di LMS Edlink. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Latihan mandiri 4 pohon *Alpha-Beta Pruning* dan membaca Giarratano Bab 1–3 tentang Sistem Pakar.

---

### PERTEMUAN 5 — Arsitektur Sistem Pakar & Representasi Pengetahuan Berbasis Aturan
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Media:** Diagram Blok *Expert System*, Tabel Akuisisi Aturan.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menjelaskan mengapa pemisahan eksplisit antara **Basis Pengetahuan (*Knowledge Base*)** dan **Mesin Inferensi (*Inference Engine*)** membuat sistem pakar jauh lebih mudah dirawat dibanding ribuan `if-else` yang tertanam kaku di kode aplikasi. | Membandingkan pemeliharaan aturan bisnis yang terpisah vs *hard-coded*. | 15' | `[2]` Bab 1 |
| **Kegiatan Inti** | Memaparkan komponen utama *Expert System* (*Knowledge Base, Working Memory, Inference Engine, Explanation Facility, User Interface*), metode representasi pengetahuan (*Semantic Networks, Frames,* dan *Production Rules* `IF premis THEN konklusi`), serta audit cacat basis aturan (*redundant rules, conflicting rules, subsumed rules, circular rules*). | Merancang *Decision Table* dan menurunkannya menjadi basis aturan minimal 12 aturan produksi berantai (2–3 level kesimpulan antara) untuk kasus diagnosis gangguan jaringan atau kelayakan bantuan UMKM, lalu mengaudit bebasnya aturan dari siklus melingkar. | 70' | `[1]` Bab 7; `[2]` Bab 1–3 |
| **Penutup** | Mengulas 2 contoh basis aturan mahasiswa dan menunjukkan cara kerja *Explanation Facility* (`WHY` & `HOW`). | Menyempurnakan graf ketergantungan aturan (*Rule Dependency Graph*) masing-masing. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Merampungkan rancangan basis aturan 15 *rules* siap ditelusuri pekan depan.

---

### PERTEMUAN 6 — Mesin Inferensi: **Forward Chaining** vs **Backward Chaining**
* **Sub-CPMK:** `Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4] · **Media:** Lembar Jejak *Working Memory*, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Memantik perbandingan: kapan seorang dokter mengumpulkan semua gejala dulu baru menyimpulkan (*data-driven*), dan kapan seorang teknisi mulai dari satu hipotesis kerusakan lalu mengecek buktinya satu per satu (*goal-driven*)? | Mengaitkan kedua situasi tersebut dengan *Forward Chaining* dan *Backward Chaining*. | 15' | `[2]` Bab 4 |
| **Kegiatan Inti** | Mendemonstrasikan penelusuran tabel siklus **Forward Chaining** (*Match → Conflict Set → Conflict Resolution [Specificity, Recency, Priority] → Fire Rule & Update Working Memory*) serta penelusuran tumpukan/pohon sub-tujuan **Backward Chaining** untuk membuktikan satu hipotesis target, disertai pedoman pemilihan arsitektur berdasarkan bentuk kipas graf aturan (*fan-in vs fan-out*). | Menelusuri satu basis aturan 10 *rules* menggunakan kedua metode secara berurutan dan membandingkan jumlah pertanyaan/pemeriksaan fakta yang dibutuhkan. | 70' | `[2]` Bab 4–6 |
| **Penutup** | Merangkum perbedaan jejak bukti `HOW` dan alasan pertanyaan `WHY` pada mesin inferensi. | Mengunggah hasil latihan tabel jejak inferensi ke LMS Edlink. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menyelesaikan 4 studi kasus penelusuran *Forward* dan *Backward Chaining*.

---

### PERTEMUAN 7 — Penanganan Ketidakpastian: **Certainty Factor (CF)** & Klinik Pra-UTS
* **Sub-CPMK:** `Sub-CPMK-2.2` [C4] · **Media:** Lembar Rumus *Certainty Factor*, Paket Latihan UTS.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan keterbatasan logika biner benar/salah murni ketika gejala nyata di lapangan bersifat tidak pasti (*"daun agak menguning, keyakinan petani 0,7"*). | Mengamati perlunya bobot keyakinan pada fakta maupun aturan pakar. | 15' | `[2]` Bab 7 |
| **Kegiatan Inti** | Mengajarkan formulasi **Certainty Factor (CF)**: ukuran kepercayaan $MB$, ketidakpercayaan $MD$, aturan tunggal $CF(H,e) = CF_{\text{user}}(e) \times CF_{\text{rule}}$, aturan premis majemuk (`AND` memakai $\min$, `OR` memakai $\max$), serta rumus penggabungan dua aturan yang mendukung hipotesis yang sama ($CF_1 + CF_2(1 - CF_1)$ untuk keduanya positif), dilanjutkan klinik simulasi soal **UTS Pekan 8**. | Menghitung nilai *Certainty Factor* akhir dari 3 jalur aturan yang bermuara ke satu hipotesis diagnosis dan berlatih menyelesaikan soal simulasi UTS. | 70' | `[2]` Bab 7–8 |
| **Penutup** | Menyampaikan kisi-kisi resmi dan rubrik penilaian **UTS (`CPMK-2`, 30%)**. | Mencatat ketelitian tanda positif/negatif pada rumus kombinasi $CF$. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Belajar mandiri persiapan UTS atas materi Sistem Pakar & *Certainty Factor*.

---

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]) · **Bobot:** **30%** · **Durasi:** `100 menit` (Tertulis Luring Terjadwal).

| Tahap | Aktivitas Pengawasan | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Pemeriksaan kehadiran, pembagian naskah studi kasus UTS, dan pembacaan tata tertib *closed-book*. | Menyiapkan alat tulis dan kalkulator ilmiah non-programmable. | 10' | Tata Tertib UTS |
| **Pelaksanaan** | Mengawasi pengerjaan 3 soal studi kasus: (1) Perancangan basis aturan konsisten; (2) Jejak *Forward* & *Backward Chaining*; (3) Perhitungan *Certainty Factor* multi-aturan. | Mengerjakan naskah ujian secara mandiri, jujur, dan sistematis. | 85' | Soal UTS `STI-307` |
| **Pengumpulan** | Mengumpulkan lembar jawaban urut presensi dan menandatangani berita acara. | Menyerahkan lembar jawaban ujian. | 5' | Berita Acara |
* **PT & BM:** Evaluasi pasca-UTS dan membaca Ross Bab 1–2 tentang himpunan *Fuzzy*.

---

### PERTEMUAN 9 — Pengantar Logika *Fuzzy*: Himpunan *Crisp vs Fuzzy* & Operator Zadeh
* **Sub-CPMK:** `Sub-CPMK-3.1` [C3→C4] · **Media:** Salindia Grafik Keanggotaan, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Membahas umpan balik hasil UTS, lalu menunjukkan absurditas batas tegas (*crisp*): jika "Suhu Panas $\ge 30^\circ\text{C}$", apakah $29,9^\circ\text{C}$ tiba-tiba dianggap tidak panas sama sekali ($\mu=0$)? | Memahami perbedaan ketidakpastian probabilistik (peluang kejadian) vs kekaburan linguistik (*vagueness* derajat keanggotaan *fuzzy*). | 15' | `[3]` Bab 1 |
| **Kegiatan Inti** | Menjelaskan konsep semesta pembicaraan (*universe of discourse*), variabel linguistik, himpunan *fuzzy* & fungsi keanggotaan $\mu_A(x) \in [0,1]$, sifat *core, support, crossover point*, serta operator standar Zadeh (`AND` / irisan = $\min(\mu_A, \mu_B)$, `OR` / gabungan = $\max(\mu_A, \mu_B)$, `NOT` / komplemen = $1 - \mu_A$). | Merumuskan variabel linguistik masukan dan keluaran beserta rentang semesta pembicaraan untuk kasus penentuan skor kelayakan pemasok atau durasi irigasi otomatis. | 70' | `[3]` Bab 1–2; `[4]` Bab 2 |
| **Penutup** | Merangkum 4 blok utama *Fuzzy Inference System* (`Fuzzifier → Rule Base → Inference Engine → Defuzzifier`). | Menyimpan rancangan variabel linguistik awal untuk diteruskan pada Pekan 10. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Latihan perhitungan operasi himpunan *fuzzy* diskrit dan kontinu.

---

### PERTEMUAN 10 — **Fuzzifikasi**: Perancangan Fungsi Keanggotaan Segitiga, Trapesium, Bahu, & Gaussian
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Media:** Kertas Grafik, Kalkulator, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan bagaimana satu angka masukan tegas (mis. `Permintaan = 3.400 unit`) dapat mengaktifkan dua himpunan *fuzzy* sekaligus (`Sedang` dengan $\mu=0,6$ dan `Tinggi` dengan $\mu=0,4$). | Mengamati titik potong kurva tumpang-tindih (*overlapping membership functions*). | 15' | `[4]` Bab 2 |
| **Kegiatan Inti** | Menurunkan rumus matematis fungsi keanggotaan **Linear Naik, Linear Turun, Segitiga** $(a,b,c)$, **Trapesium** $(a,b,c,d)$, **Bahu Kiri/Kanan** untuk ujung domain ekstrem, dan **Gaussian**, serta melatih perhitungan *fuzzifikasi* presisi pada berbagai titik uji. | Menggambar partisi kurva fungsi keanggotaan untuk 2 variabel input & 1 variabel output dan menghitung nilai $\mu$ tepat untuk sejumlah masukan numerik. | 70' | `[3]` Bab 4; `[4]` Bab 2 |
| **Penutup** | Merilis instruksi resmi **Tugas 2 (RTM-2)** berparameter NIM (dikumpulkan Pekan 12). | Mencatat parameter batas kurva sesuai digit NIM masing-masing. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menyusun fungsi keanggotaan dan matriks aturan untuk pengerjaan awal **Tugas 2**.

---

### PERTEMUAN 11 — *Fuzzy Inference System* Metode **Mamdani** (*Max-Min* & *Centroid*)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Media:** Lembar Perhitungan Mamdani, Visualisasi Luas Daerah, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menampilkan matriks *Fuzzy Associative Memory* (FAM) $3\times 3 = 9$ aturan dan menanyakan bagaimana menggabungkan beberapa aturan yang aktif bersamaan menjadi satu angka keputusan tegas. | Mengidentifikasi aturan mana saja yang bernilai $\alpha\text{-predikat} > 0$ dari hasil *fuzzifikasi*. | 15' | `[4]` Bab 3 |
| **Kegiatan Inti** | Mengajarkan alur lengkap **FIS Metode Mamdani**: (1) Evaluasi anteseden tiap aturan menghasilkan $\alpha_i$; (2) Implikasi `Min` memotong tinggi kurva konsekuen (*clipping*); (3) Agregasi `Max` menyatukan seluruh daerah terpotong; (4) **Defuzzifikasi Centroid / Center of Area (COA)** ($z^* = \frac{\int z\mu(z)\,dz}{\int \mu(z)\,dz}$ dan hampiran titik sampel diskrit $z^* = \frac{\sum z_j \mu(z_j)}{\sum \mu(z_j)}$) serta pengenalan *Mean of Maximum* (MOM). | Menghitung secara manual sampai tuntas keluaran *Centroid* pada studi kasus penentuan jumlah produksi pabrik (*Permintaan* & *Persediaan* $\to$ *Produksi*) dan menggambarkan arsiran daerah agregasinya. | 70' | `[3]` Bab 5; `[4]` Bab 3 |
| **Penutup** | Memeriksa ketepatan pembagian luas/titik sampel pada hasil hitungan mahasiswa. | Mencocokkan langkah perhitungan manual Mamdani untuk diterapkan ke **Tugas 2**. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menyelesaikan bagian perhitungan Mamdani pada **Tugas 2**.

---

### PERTEMUAN 12 — *Fuzzy Inference System* Metode **Sugeno** & Verifikasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 20%)** · **Media:** Lembar Kerja Sugeno, LMS Edlink.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Melaksanakan kuis konfirmasi tertulis 15 menit atas pengerjaan **Tugas 2 (`CPMK-3`)**. | Mengerjakan kuis verifikasi *fuzzifikasi* & inferensi secara mandiri. | 20' | Instrumen T2 |
| **Kegiatan Inti** | Mengajarkan **FIS Metode Takagi-Sugeno-Kang (Sugeno)**: konsekuen aturan tidak berupa himpunan kabur melainkan konstanta (*Orde-0*: `THEN z = k`) atau fungsi linier masukan (*Orde-1*: `THEN z = p*x + q*y + r`), dengan defuzzifikasi langsung menggunakan **Weighted Average** ($Z = \frac{\sum \alpha_i z_i}{\sum \alpha_i}$), lalu membandingkan kapan memilih Mamdani (intuitif bagi pakar manusia) vs Sugeno (sangat cepat untuk kendali *real-time* & optimasi). | Menghitung kasus yang sama dengan metode Sugeno Orde-0 dan Orde-1, membandingkan selisih angka keluarannya serta beban perhitungannya dibanding Mamdani. | 65' | `[3]` Bab 5; `[4]` Bab 4 |
| **Penutup** | Menginstruksikan kesiapan lingkungan Jupyter / Google Colab dengan pustaka `scikit-fuzzy` untuk Pekan 13. | Mengumpulkan berkas final **Tugas 2** dan memverifikasi instalasi `scikit-fuzzy`. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menginstal `numpy`, `matplotlib`, dan `scikit-fuzzy` serta membaca dokumentasi `skfuzzy.control`.

---

### PERTEMUAN 13 — Implementasi Sistem Inferensi *Fuzzy* dengan Python **`scikit-fuzzy`**
* **Sub-CPMK:** `Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C4] · **Media:** Proyektor, Jupyter Notebook / Google Colab, Pustaka `scikit-fuzzy`.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menunjukkan bagaimana 3 halaman hitungan kertas Pekan 11–12 dapat dieksekusi dan divisualisasikan dalam hitungan milidetik menggunakan API `skfuzzy.control`. | Membuka lingkungan notebook Python masing-masing. | 15' | `[5]` |
| **Kegiatan Inti** | Mendemonstrasikan secara langsung pembuatan `ctrl.Antecedent`, `ctrl.Consequent`, pendefinisian kurva `fuzz.trimf` & `fuzz.trapmf`, penulisan `ctrl.Rule` dengan operator `&` dan `|`, perakitan `ctrl.ControlSystem` & `ctrl.ControlSystemSimulation`, pencetakan plot area defuzzifikasi `.view(sim=...)`, serta pembangkitan permukaan respons 3D (*3D Control Surface*) untuk memvalidasi kehalusan keputusan di seluruh ruang input. | Mengkodekan ulang kasus Tugas 2 berparameter NIM masing-masing di `scikit-fuzzy`, membandingkan angka keluaran Python dengan hitungan manualnya, dan menganalisis penyebab selisih desimal halus akibat resolusi diskretisasi semesta. | 70' | `[5]` |
| **Penutup** | Merilis panduan penyusunan purwarupa mini-proyek sistem cerdas untuk komponen **UAS Pekan 16**. | Mengunggah notebook hasil verifikasi ke LMS Edlink. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Mengembangkan notebook sistem cerdas pada domain kasus pilihan individu/pasangan.

---

### PERTEMUAN 14 — Arsitektur Hibrid *Rule-Fuzzy Decision System* & Analisis Sensitivitas Kurva
* **Sub-CPMK:** Sintesis `CPMK-2` & `CPMK-3` [C4] · **Media:** Notebook Python, Diagram Arsitektur Hibrid.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menjelaskan pola nyata di industri: aturan kebijakan mutlak (*hard constraints*, mis. usia minimum atau syarat legal) diperiksa dulu oleh **Rule-Based Expert Filter** (`CPMK-2`), baru skor kelayakan bernuansanya dihitung oleh **Fuzzy Inference Engine** (`CPMK-3`)! | Memahami sinergi antara sistem pakar tegas dan logika *fuzzy* dalam satu alur keputusan. | 15' | `[2]` Bab 10 |
| **Kegiatan Inti** | Membimbing perancangan alur hibrid *Rule-Based Pre-Screening + Fuzzy Scoring* di Python murni + `scikit-fuzzy`, mengajarkan teknik **Analisis Sensitivitas & Uji Batas (*Edge-Case Testing*)** (menggeser titik bahu/puncak kurva untuk mengecek apakah ada wilayah input kosong yang menghasilkan galat defuzzifikasi nol), serta menjelaskan peta transisi ke `STI-413 Pembelajaran Mesin` *(di mana aturan dipelajari dari data historis, bukan ditulis pakar — menjaga ketat guardrail tanpa koding Neural Network/ML di `STI-307`!)*. | Menambahkan lapis aturan pra-kelayakan logis dan pengujian sensitivitas 10 skenario uji pada purwarupa notebook sistem cerdas masing-masing. | 70' | `[2]` Bab 10; `[4]` Bab 6 |
| **Penutup** | Mengecek agar tidak ada mahasiswa yang melenceng memakai `sklearn` klasifikasi di proyek `STI-307`. | Mencatat perbaikan kelengkapan skenario uji batas pada notebook. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Menyelesaikan pengujian sensitivitas dan dokumentasi penjelasan aturan pada notebook.

---

### PERTEMUAN 15 — Klinik Verifikasi Purwarupa `scikit-fuzzy` & Konsolidasi Pra-UAS
* **Sub-CPMK:** Konsolidasi `CPMK-1` s.d. `CPMK-3` [C4] · **Media:** Proyektor, Ceklis *Reproducibility* `K-3`.

| Tahap | Aktivitas Dosen | Aktivitas Mahasiswa | Durasi | Rujukan |
|---|---|---|:---:|---|
| **Pendahuluan** | Menyampaikan ceklis kesiapan komponen purwarupa UAS (`requirements.txt`, *reproducibility*, plot kurva keanggotaan, plot *defuzzifikasi*, dan analisis hasil). | Menyiapkan berkas notebook untuk dicek keterulangan eksekusinya. | 15' | RPS `061_1` |
| **Kegiatan Inti** | Melaksanakan *Code & Rule Walkthrough* sampel purwarupa mahasiswa di kelas, mengkritisi kelengkapan cakupan aturan *fuzzy* (agar tidak ada kombinasi input yang tak terdefinisi), serta membahas latihan soal sintesis persiapan ujian tertulis **UAS Pekan 16**. | Mendemonstrasikan hasil eksekusi notebook, memperbaiki celah aturan yang ditemukan, dan berlatih menjawab soal analitis FIS & sistem cerdas. | 70' | `[1]; [2]; [3]; [5]` |
| **Penutup** | Mengingatkan tenggat unggah berkas purwarupa notebook sebelum ujian tertulis UAS Pekan 16 dimulai. | Memfinalisasi dan mengunggah bundel notebook + laporan ringkas ke LMS Edlink. | 15' | LMS Edlink |
* **PT (`120'`) & BM (`120'`):** Persiapan komprehensif menghadapi ujian tertulis UAS Pekan 16.

---

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-3`** & Sintesis `CPMK-1..3` [C4] · **Bobot:** **30%** · **Durasi:** `100 menit`.

| Tahap | Aktivitas Dosen / Penguji | Aktivitas Mahasiswa | Durasi | Instrumen |
|---|---|---|:---:|---|
| **Persiapan** | Memverifikasi kelengkapan unggahan notebook `scikit-fuzzy` seluruh peserta dan membagikan naskah soal ujian tertulis komprehensif luring. | Mengisi daftar hadir dan menyiapkan alat tulis. | 10' | Berita Acara UAS |
| **Pelaksanaan** | Mengawasi pengerjaan naskah ujian tertulis komprehensif (perhitungan analitis FIS Mamdani/Sugeno, penelusuran & koreksi cuplikan skrip `skfuzzy.control` untuk memverifikasi kemandirian atas notebook yang dikumpulkan, serta perancangan arsitektur hibrid pakar-fuzzy). | Mengerjakan ujian tertulis komprehensif secara mandiri dan presisi. | 85' | Soal UAS `STI-307` |
| **Penutupan** | Mengumpulkan lembar jawaban dan menutup rangkaian perkuliahan semester. | Menyerahkan lembar jawaban ujian secara tertib. | 5' | Portal OBE |
