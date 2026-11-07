# 058_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA (*Discrete Mathematics and Logic*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI204`  
**Klaster Rubrik Master (Dok 018):** Klaster 1 (`K-1`) — Sains Dasar & Teori Formal  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** Panduan KPT 2024 Dikti (Tabel 18, 19, 20) · Dok 008 §4 · Dok 018 §3 · Dok 033 · `058_1_RPS_STI-204_...md` · `058_4_RENCANA_EVALUASI_ASESMEN_STI-204_...md`.

---

## BAGIAN I — PEDOMAN KALIBRASI RUBRIK KLASTER TEORI FORMAL (`K-1`)

Sesuai **Dokumen 018 §3**, penilaian pada `STI-204 Matematika Diskrit dan Logika` menilai ketajaman penalaran deduktif dan ketepatan pemodelan struktur diskrit melalui tiga pilar utama: **(1) Ketepatan Formalisasi Simbolik & Definisi Struktur**, **(2) Keabsahan Alur Pembuktian / Penelusuran Tabel Algoritmis**, serta **(3) Kelengkapan & Presisi Solusi Akhir**.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1`: `Sub-CPMK-1.1` & `1.2`)
**Objek Penilaian:** *Proof Set* Mandiri 4 Masalah: Ekuivalensi Aljabar Logika, Bukti Validitas Inferensi & Resolusi, *First-Order Logic*, dan Induksi Matematika Algoritma (+ Verifikasi Kelas).

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Ketepatan Formalisasi Simbolik Proposisi & Kuantor *FOL***<br>(`Sub-CPMK-1.1 & 1.2`) | **30%** | Seluruh kalimat aturan bisnis diterjemahkan presisi ke proposisi dan kuantor bersarang ($\forall, \exists$) dengan definisi domain jelas; negasi kuantor De Morgan akurat 100%. | Translasi proposisi dan predikat tepat; hanya terdapat ketidaklengkapan minor pada penulisan domain salah satu variabel. | Translasi proposisi benar, namun sempat tertukar urutan atau operator ($\wedge$ vs $\to$) di bawah kuantor eksistensial/universal pada 1 sub-soal. | Sering salah menerjemahkan arah implikasi ("hanya jika") dan gagal menegasikan kuantor bersarang dengan benar. | Tidak mampu memformulasikan pernyataan ke notasi logika simbolik. |
| **2. Keabsahan Alur Hukum Aljabar Logika & Aturan Inferensi**<br>(`Sub-CPMK-1.1 & 1.2`) | **35%** | Setiap langkah transformasi ekuivalensi dan bukti 2-kolom mencantumkan nama hukum/aturan inferensi (*Modus Ponens/Tollens, Resolusi*, dll.) secara eksplisit, sah, dan bebas lompatan logika. | Alur deduksi sah dari premis hingga kesimpulan; hanya 1–2 baris yang nama hukumnya disingkat atau digabung dua langkah sekaligus. | Mencapai kesimpulan dengan alur yang secara garis besar benar, namun beberapa baris tidak mencantumkan alasan hukum logika yang sah. | Terjebak sesat pikir (*fallacy*) atau mencampuradukkan hukum ekuivalensi dengan aturan inferensi satu arah. | Bukti tidak nyambung antar-baris atau hanya menuliskan tabel kebenaran raksasa ketika diminta bukti aljabar. |
| **3. Struktur & Ketelitian Pembuktian Induksi Matematika**<br>(`Sub-CPMK-1.2`) | **35%** | Langkah Basis, Hipotesis Induksi (untuk suatu $k \ge n_0$), dan Langkah Induktif ditulis terpisah dengan jernih, menggunakan hipotesis induksi secara sah untuk memverifikasi rumus/invarian algoritma, serta konsisten saat kuis verifikasi. | Ketiga tahapan induksi lengkap dan deduksi aljabarnya benar; penjelasan kesimpulan terminasi invarian algoritma sedikit ringkas. | Menuliskan Basis dan Langkah Induktif dengan cukup benar, namun penulisan kalimat Hipotesis Induksi kurang presisi (mis. menulis "asumsikan benar untuk semua $k$"). | Melakukan penalaran melingkar (*circular reasoning*: mengasumsikan $P(k+1)$ benar sejak awal pembuktian) atau gagal menguasai langkah dasar saat kuis kelas. | Bagian induksi matematika salah total atau tidak dikerjakan. |

$$\text{Skor Tugas 1} = 0,30(K_1) + 0,35(K_2) + 0,35(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `CPMK-2`: `Sub-CPMK-2.1` & `2.2`)
**Objek Penilaian:** Jawaban Ujian Tertulis 150 Menit: Relasi Ekuivalensi, *Poset* & Diagram Hasse, Aljabar Boolean Query, Kombinatorika, dan Relasi Rekurensi.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Pemodelan Relasi Ekuivalensi, *Poset*, & Diagram Hasse**<br>(Soal 1 — `Sub-CPMK-2.1`) | **30%** | Akurat menguji sifat refleksif/simetris/antisimetris/transitif, menggambar Diagram Hasse bersih tanpa garis refleksif/transitif redundan, serta menghasilkan urutan *topological sort* yang valid. | Pengujian sifat relasi dan urutan *topological sort* tepat; Diagram Hasse benar dengan 1 busur transitif lupa dihapus. | Memahami perbedaan relasi ekuivalensi vs *Poset*, namun salah menentukan salah satu elemen minimal/maksimal pada Diagram Hasse. | Menggambar graf berarah mentah lengkap dengan *self-loop* sebagai Diagram Hasse atau tertukar sifat simetris dengan antisimetris. | Gagal menguji sifat relasi maupun mengonstruksi *Poset*. |
| **2. Manipulasi Aljabar Boolean pada Predikat Query & Fungsi Diskrit**<br>(Soal 2 — `Sub-CPMK-2.2 & 2.1`) | **25%** | Menyederhanakan kondisi predikat kueri menjadi bentuk paling minimal menggunakan hukum Aljabar Boolean secara sah dan tepat menganalisis sifat injektif/surjektif fungsi *hash*. | Penyederhanaan predikat Boolean benar dan efisien; analisis sifat fungsi diskrit tepat dengan penjelasan singkat. | Berhasil mereduksi sebagian redundansi predikat Boolean meskipun belum mencapai bentuk paling sederhana. | Salah menerapkan hukum distributif/De Morgan sehingga mengubah arti hasil seleksi kueri. | Tidak mampu menyederhanakan ekspresi Boolean maupun menganalisis fungsi. |
| **3. Analisis Kaidah Kombinatorika Pencacahan**<br>(Soal 3 — `Sub-CPMK-2.2`) | **25%** | Tepat membedakan penggunaan *Inclusion-Exclusion*, *Pigeonhole*, permutasi, dan kombinasi sesuai syarat batasan soal dengan perhitungan akurat. | Pemilihan rumus kombinatorika tepat untuk seluruh bagian soal; terdapat maks. 1 selip hitung perkalian faktorial di akhir. | Benar pada soal permutasi/kombinasi dasar, namun kurang tepat mengurangi irisan rangkap tiga pada bagian *Inclusion-Exclusion*. | Tertukar antara rumus permutasi dan kombinasi pada mayoritas sub-soal. | Rumus dan penalaran pencacahan keliru seluruhnya. |
| **4. Penyelesaian Analitis Relasi Rekurensi**<br>(Soal 4 — `Sub-CPMK-2.1`) | **20%** | Menyusun persamaan karakteristik dengan benar, menentukan bentuk solusi umum (akar berbeda/kembar), dan menghitung konstanta dari nilai awal hingga rumus tertutup terverifikasi. | Persamaan karakteristik dan bentuk solusi umum tepat; hanya terdapat selip aritmetika kecil saat menyelesaikan sistem persamaan konstanta $\alpha_1, \alpha_2$. | Mampu mencari akar karakteristik dengan benar, namun keliru menuliskan bentuk umum saat menghadapi akar kembar atau belum memasukkan syarat awal. | Hanya menghitung beberapa suku barisan secara manual tanpa menemukan rumus tertutup $a_n$. | Tidak mampu menyelesaikan relasi rekurensi. |

$$\text{Skor UTS} = 0,30(K_1) + 0,25(K_2) + 0,25(K_3) + 0,20(K_4)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-3`: `Sub-CPMK-3.1` & `3.2`)
**Objek Penilaian:** Laporan Studi Kasus Pemodelan Graf & Pohon Optimasi Jaringan (6–8 hal. berparameter NIM): *Adjacency Matrix*, *Dijkstra*, *MST Kruskal & Prim*, dan Pewarnaan Graf.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Pemodelan Graf, *Adjacency Matrix*, $A^2$, & Analisis Euler**<br>(`Sub-CPMK-3.1`) | **25%** | *Adjacency Matrix* sesuai parameter NIM tanpa salah entri, perhitungan jumlah lintasan via $A^2$ akurat, dan analisis syarat derajat lintasan/sirkuit Euler sangat tepat. | *Adjacency Matrix* dan analisis Euler tepat; perhitungan $A^2$ benar dengan 1 selip penjumlahan kecil. | Matriks ketetanggaan benar, namun penjelasan syarat eksistensi lintasan vs sirkuit Euler kurang spesifik pada derajat simpul ganjil. | Matriks tidak simetris untuk graf tak berarah atau salah menafsirkan arti elemen matriks $A^2$. | Representasi matriks salah total atau menyalin parameter NIM mahasiswa lain. |
| **2. Ketelitian Tabel Penelusuran *Shortest Path* (*Dijkstra*)**<br>(`Sub-CPMK-3.1`) | **30%** | Tabel iterasi relaksasi jarak *Dijkstra* lengkap dari langkah ke-0 hingga seluruh simpul permanen, mencantumkan simpul pendahulu (*predecessor*), dan merekonstruksi jalur terpendek dengan benar 100%. | Tabel iterasi *Dijkstra* runtut dan menghasilkan jarak minimum yang tepat untuk hampir semua simpul (maks. 1 salah hitung bobot cabang non-utama). | Memahami prosedur pemilihan simpul berjarak terkecil pada *Dijkstra*, namun tidak menuliskan kolom *predecessor* secara lengkap atau keliru memperbarui 1–2 tetangga. | Mencampuradukkan langkah *Dijkstra* dengan *Prim* atau langsung menebak rute terpendek secara visual tanpa tabel iterasi algoritmis. | Tabel penelusuran *Dijkstra* salah konsep atau tidak disertakan. |
| **3. Konstruksi Pohon *MST* (*Kruskal & Prim*)**<br>(`Sub-CPMK-3.2`) | **25%** | Menuliskan urutan pemilihan $n-1$ sisi secara eksplisit (termasuk sisi yang ditolak karena membentuk siklus pada *Kruskal*), menghasilkan *MST* valid dengan total bobot minimum identik antara *Kruskal* dan *Prim*. | Urutan pemilihan sisi *Kruskal* dan *Prim* benar serta menghasilkan total bobot *MST* yang sama dan minimal. | Berhasil membentuk *MST* yang benar dengan salah satu metode, namun pada metode kedua sempat melewatkan urutan pemeriksaan siklus. | Subgraf hasil yang dipilih masih memuat siklus (bukan pohon!) atau jumlah sisinya tidak sama dengan $|V|-1$. | Gagal membedakan *Minimum Spanning Tree* dengan lintasan tunggal. |
| **4. Pewarnaan Graf Jadwal ($\chi(G)$) & Dokumentasi Visual**<br>(`Sub-CPMK-3.1`) | **20%** | Graf konflik jadwal dimodelkan akurat, pewarnaan urut derajat (*Welsh-Powell*) tepat tanpa simpul bertetangga sewarna, argumen batas bawah $\chi(G)$ (klik maksimum) tajam, dan diagram sangat rapi. | Graf konflik dan pembagian slot warna jadwal bebas bentrok sudah tepat serta visualisasi diagram jelas. | Pembagian jadwal bebas bentrok valid, tetapi jumlah warna yang dipakai belum minimal atau gambar graf kurang rapi. | Terdapat dua simpul bertetangga (jadwal bentrok) yang diberi warna/slot waktu yang sama. | Bagian pewarnaan graf tidak dikerjakan atau keliru memodelkan simpul dan sisi. |

$$\text{Skor Tugas 2} = 0,25(K_1) + 0,30(K_2) + 0,25(K_3) + 0,20(K_4)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4`: `Sub-CPMK-4.1` & `4.2`)
**Objek Penilaian:** Jawaban Ujian Komprehensif 150 Menit: Konstruksi 5-Tupel DFA, NFA/$\varepsilon$-NFA & Konversi *Subset Construction*, Minimasi DFA & *State Machine* Sistem, serta Sintesis.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Konstruksi 5-Tupel & Kelengkapan Transisi DFA**<br>(Kasus 1 — `Sub-CPMK-4.1`) | **30%** | Definisi 5-tupel $M=(Q,\Sigma,\delta,q_0,F)$ lengkap, setiap status memiliki tepat satu busur keluar untuk seluruh simbol $\Sigma$ (termasuk *trap state*), menerima tepat bahasa sasaran, dan jejak $\hat{\delta}$ presisi. | DFA menerima tepat bahasa yang diminta dan bersifat deterministik; hanya lupa menyertakan *trap state* pada gambar meskipun tabel transisinya menandai $\emptyset$/tolak. | DFA menerima mayoritas string pola yang benar, namun tanpa sengaja meloloskan 1 kasus batas (mis. string kosong $\varepsilon$) atau notasi 5-tupel kurang lengkap. | Rancangan yang dibuat sebenarnya masih bersifat nondeterministik (ada 2 busur bersimbol sama dari 1 status) ketika diminta DFA. | Otomata gagal mengenali pola dasar yang diminta soal. |
| **2. Perancangan NFA/$\varepsilon$-NFA & Ketelitian *Subset Construction***<br>(Kasus 2 — `Sub-CPMK-4.2`) | **35%** | Perhitungan $\varepsilon\text{-closure}(q)$ akurat untuk semua status, tabel **Subset Construction** hanya menelusuri himpunan status terjangkau secara tepat, dan penandaan himpunan status akhir DFA baru ($S \cap F \neq \emptyset$) benar 100%. | Himpunan $\varepsilon\text{-closure}$ dan alur *Subset Construction* benar; hanya terdapat 1 sel transisi himpunan gabungan yang kurang satu elemen status minor. | Memahami prosedur penggabungan himpunan status pada *Subset Construction*, namun lupa menerapkan $\varepsilon\text{-closure}$ kembali setelah membaca simbol input pada 1 langkah. | Mengubah NFA ke DFA hanya dengan menebak gambar baru tanpa menggunakan prosedur algoritmis *Subset Construction*. | Tidak memahami konsep $\varepsilon\text{-closure}$ maupun konversi NFA ke DFA. |
| **3. Minimasi Status DFA & Pemodelan *State Machine* Sistem**<br>(Kasus 3 — `Sub-CPMK-4.1 & 4.2`) | **25%** | Partisi ekuivalensi menghasilkan DFA berstatus paling minimum secara sah; model *state machine* transaksi digital mencakup seluruh aksi valid/batal/kedaluwarsa secara deterministik tanpa celah transisi ilegal. | Minimasi DFA benar dan rancangan *state machine* sistem logis serta mencakup skenario normal maupun gagal dengan baik. | Mampu menggabungkan sebagian status ekuivalen dan menyusun diagram alur status dasar, walau 1 transisi penanganan gagal belum didefinisikan. | Menggabungkan status akhir ($F$) dengan status non-akhir ($Q \setminus F$) pada saat minimasi sehingga merusak bahasa yang diterima. | Gagal melakukan minimasi maupun memodelkan transisi status sistem. |
| **4. Sintesis Logika–Graf–Otomata**<br>(Kasus 4 — Sintesis `CPMK-1..4`) | **10%** | Tepat memetakan graf transisi otomata ke matriks ketetanggaan berarah dan merumuskan predikat logika penjaga transisi dengan bersih. | Keterkaitan antara representasi matriks graf dan kondisi logika transisi dijelaskan dengan benar. | Mampu menyusun matriks ketetanggaan dari otomata namun perumusan kondisi logikanya masih kurang ringkas. | Hanya menjawab sebagian kecil tanpa menghubungkan konsep graf dan logika. | Kosong atau salah seluruhnya. |

$$\text{Skor UAS} = 0,30(K_1) + 0,35(K_2) + 0,25(K_3) + 0,10(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF AKTIVITAS PEMBUKTIAN & SIMULASI GRAF/OTOMATA DI KELAS

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Disiplin Penulisan Bukti & Notasi Himpunan** | Disiplin membedakan simbol $\in$ vs $\subseteq$, $\to$ vs $\Rightarrow$, serta selalu menyebutkan nama hukum/aturan pada setiap langkah. | Notasi rapi dan alur logis benar, hanya terdapat ketidaktepatan simbol sangat kecil. | Alur ide benar tetapi pencampuran simbol logika dan himpunan masih sering terjadi. | Langkah klaim tanpa dasar bukti atau notasi tidak bermakna matematis. |
| **Pengujian Kasus Batas (*Edge Cases*) pada Graf & FSA** | Mandiri menguji rancangan DFA/graf dengan kasus ekstrem ($\varepsilon$, string panjang 1, graf tak terhubung). | Menguji rancangan dengan beberapa string/lintasan contoh sesuai arahan dosen. | Hanya menguji 1 contoh positif tanpa memeriksa apakah input tidak valid ikut diterima. | Tidak melakukan verifikasi uji kasus atas rancangan yang dibuat. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat Capaian | Deskriptor Integratif Penguasaan `STI-204` (`CPL-05` [80%] & `CPL-02` [20%] — Level *Introduce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai pembuktian deduktif/induktif logika proposisi-predikat secara ketat, terampil memodelkan struktur *Poset*/Boolean/kombinatorika, mahir menganalisis optimasi jaringan dengan algoritma Graf & Pohon, serta presisi mengonstruksi dan mengonversi DFA/NFA. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa mampu menyusun bukti logika dan induksi dengan benar, menerapkan relasi, aljabar Boolean, dan kombinatorika secara tepat, serta akurat menelusuri algoritma *Dijkstra/MST* dan mengonstruksi model DFA/NFA. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar minimal ketuntasan OBE ($\ge 65,0$) dalam membuktikan argumen dasar, memodelkan relasi/kombinatorika, menjalankan langkah algoritma graf/pohon standar, dan merancang DFA/NFA sederhana. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih lemah dalam struktur pembuktian formal (melompati langkah induksi/inferensi) dan sering melakukan kesalahan sistematis saat menelusuri algoritma graf atau mengonversi NFA ke DFA. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai kaidah dasar logika maupun struktur diskrit, atau terbukti melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20 & DOK 033)

**Skala Persepsi:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-204` | Rujukan Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu membuktikan ekuivalensi dan validitas argumen logika proposisi menggunakan tabel kebenaran maupun hukum aljabar logika. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu memformulasikan pernyataan berkuantor *First-Order Logic* dan membuktikan kebenaran algoritma dengan Induksi Matematika. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu menerapkan relasi ekuivalensi dan mengonstruksi Diagram Hasse (*Poset*) pada pemodelan ketergantungan data/tugas. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menyederhanakan ekspresi logika kueri dengan Aljabar Boolean dan menerapkan kaidah kombinatorika pencacahan. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu menganalisis graf dengan *Adjacency Matrix*, lintasan Euler/Hamilton, dan algoritma rute terpendek *Dijkstra*. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu menerapkan algoritma pohon merentang minimum (*Kruskal & Prim*) untuk optimasi topologi jaringan. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu merancang model 5-tupel *Deterministic Finite Automata* (DFA) untuk pengenalan pola bahasa formal. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu merancang NFA/$\varepsilon$-NFA, mengonversinya ke DFA (*Subset Construction*), dan memodelkan transisi status sistem. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-204`)

```text
==============================================================================================================================
       LEMBAR REKAPITULASI PENILAIAN OBE MULTI-CPL — STI-204 MATEMATIKA DISKRIT DAN LOGIKA (3 SKS TEORI)
==============================================================================================================================
Semester / Tahun Akademik : Semester 2 (Genap) / 2026-2027       CPL : CPL-05 (P1: 80%), CPL-02 (KU1: 20%) [Level: Introduce]
Klaster Rubrik            : K-1 (Sains Dasar & Teori Formal)     Ambang OBE : >= 65.0 per CPMK & CPL (Target Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mhs     | T1(20%) | UTS(30%)| T2(20%) | UAS(30%)| CPL-05 (80%) | CPL-02 (20%) | Nilai | Huruf | OBE
   |           |              | [CPMK1] | [CPMK2] | [CPMK3] | [CPMK4] |     (P1)     |     (KU1)    | Akhir | Mutu  | >=65
------------------------------------------------------------------------------------------------------------------------------
1  | 260101001 | [Nama Mhs 1] |  86.0   |  82.0   |  88.0   |  84.0   |    84.00     |    87.00     | 84.60 |   A   | YA
2  | 260101002 | [Nama Mhs 2] |  74.0   |  72.0   |  76.0   |  70.0   |    72.00     |    75.00     | 72.60 |   B   | YA
3  | 260101003 | [Nama Mhs 3] |  68.0   |  66.0   |  70.0   |  66.0   |    66.75     |    69.00     | 67.20 |   C+  | YA
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS               |  76.00  |  73.33  |  78.00  |  73.33  |    74.25     |    77.00     | 74.80 | % >=65: 100%
==============================================================================================================================
```
