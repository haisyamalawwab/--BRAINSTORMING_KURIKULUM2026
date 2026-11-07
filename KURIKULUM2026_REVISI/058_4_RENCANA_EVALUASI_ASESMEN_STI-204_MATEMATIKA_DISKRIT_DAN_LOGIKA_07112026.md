# 058_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA (*Discrete Mathematics and Logic*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 2 — Tahap Fondasi Lanjut)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI204`  
**Klaster Asesmen MK (Dok 018):** Klaster 1 (`K-1`) — Sains Dasar & Teori Formal  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** Panduan KPT 2024 Dikti (Tabel 16–21, Tabel 26, & Lampiran RTM) · Dok 004 (`P = 80%, KU = 20%`) · Dok 007 §9 · Dok 008 (Formula Multi-CPL Attainment & Skema 4x Evaluasi) · Dok 018 · Dok 041 Lampiran 23 · `058_1_RPS_STI-204_...md`.

---

## 1. ARSITEKTUR PENILAIAN KLASTER TEORI FORMAL (`K-1`) & KEPATUHAN IKU 7

Mata kuliah `STI-204 Matematika Diskrit dan Logika` (3 SKS Teori) berada pada **Klaster 1 (`K-1`)** dengan fokus penilaian pada **keabsahan pembuktian deduktif/induktif, ketepatan representasi matematis struktur diskrit, ketelitian penelusuran algoritma graf/pohon, dan akurasi konstruksi otomata berhingga**:
* **Pemetaan 1-ke-1 Instrumen ke CPMK:** `Tugas 1 (20%) → CPMK-1`, `UTS (30%) → CPMK-2`, `Tugas 2 (20%) → CPMK-3`, dan `UAS (30%) → CPMK-4`.
* **Keselarasan Proporsi Multi-CPL Dokumen 004:** Sesuai matriks bobot domain Dokumen 004 (`P = 80%`, `KU = 20%`) dan pemetaan CPMK Dokumen 007 Tabel 9.B (`CPMK-1` & `CPMK-3` mendukung `P1 + KU1`; `CPMK-2` & `CPMK-4` mendukung `P1`), kontribusi mata kuliah terbagi presisi menjadi **`CPL-05` (`P1`) = 80%** dan **`CPL-02` (`KU1`) = 20%**.
* **Verifikasi Kepatuhan IKU 7 ($\ge 50\%$):** Komponen pemecahan kasus & masalah terapan meliputi **Tugas 1 (20% — *Policy Inference & Algorithm Verification Proof*), Tugas 2 (20% — *Network Graph & Scheduling Optimization Case*), dan UAS (30% — *Pattern Recognition & System State Machine Construction Case*) = 70%**, melampaui standar minimal nasional IKU 7 (**50%**).

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP MULTI-CPL, CPMK, & SUB-CPMK (STANDAR KPT 2024 TABEL 26)

| Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Instrumen Penilaian | `CPL-05` (`P1`) | `CPL-02` (`KU1`) | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | **RTM-1 (Tugas 1)** Bagian A & B: Pembuktian ekuivalensi aljabar logika & validitas inferensi proposisi | 5% | 5% | 10% | **20%** |
| | `Sub-CPMK-1.2` | Mg 4 | **RTM-1 (Tugas 1)** Bagian C & D: Inferensi *First-Order Logic* & bukti Induksi Matematika algoritma | 5% | 5% | 10% | |
| **`CPMK-2`**<br>(C3) | `Sub-CPMK-2.1` | Mg 8 | **Naskah Soal UTS** (Soal 1 & 4): Pemodelan relasi ekuivalensi, *Poset* (Diagram Hasse), & relasi rekurensi | 15% | 0% | 15% | **30%** |
| | `Sub-CPMK-2.2` | Mg 8 | **Naskah Soal UTS** (Soal 2 & 3): Aljabar Boolean predikat kueri basis data & kombinatorika pencacahan | 15% | 0% | 15% | |
| **`CPMK-3`**<br>(C4) | `Sub-CPMK-3.1` | Mg 12 | **RTM-2 (Tugas 2)** Bagian A, B, & D: *Adjacency Matrix*, Euler/Hamilton, *Dijkstra*, & pewarnaan graf | 5% | 5% | 10% | **20%** |
| | `Sub-CPMK-3.2` | Mg 12 | **RTM-2 (Tugas 2)** Bagian C: Optimasi tulang punggung jaringan dengan pohon *MST* (*Kruskal & Prim*) | 5% | 5% | 10% | |
| **`CPMK-4`**<br>(C4) | `Sub-CPMK-4.1` | Mg 16 | **Naskah Soal UAS** (Kasus 1 & separuh 3): Konstruksi 5-tupel DFA pengenal pola & minimasi status DFA | 14% | 0% | 14% | **30%** |
| | `Sub-CPMK-4.2` | Mg 16 | **Naskah Soal UAS** (Kasus 2, separuh 3, & 4): Konstruksi NFA/$\varepsilon$-NFA, konversi *Subset*, & *state machine* sistem | 16% | 0% | 16% | |
| **TOTAL** | **8 Sub-CPMK** | **16 Pekan** | **4 Paket Instrumen Sumatif (+ Aktivitas Formatif Mingguan 0%)** | **80%** | **20%** | **100%** | **100%** |

---

## 3. KISI-KISI INSTRUMEN EVALUASI (*ASSESSMENT BLUEPRINT*)

| Titik Evaluasi | Pekan | Durasi / Format | Sub-CPMK Diuji | Level Bloom | Rincian Butir / Bagian Penilaian | Bobot Internal | Bobot MK |
|---|:---:|---|---|:---:|---|:---:|:---:|
| **1. Tugas 1** | Mg 4 | Penugasan Mandiri Terstruktur (1 pekan) + Kuis Konfirmasi 10' | `Sub-CPMK-1.1`<br>`Sub-CPMK-1.2` | C3 | • Masalah 1: Translasi aturan bisnis & bukti ekuivalensi via hukum aljabar logika<br>• Masalah 2: Bukti 2-kolom kesahihan argumen 5 premis via aturan inferensi & resolusi<br>• Masalah 3: Formalisasi pernyataan kuantor *FOL* bersarang & negasi De Morgan<br>• Masalah 4: Bukti kebenaran deret/invarian algoritma menggunakan Induksi Matematika | 25%<br>25%<br>20%<br>30% | **20%** |
| **2. UTS** | Mg 8 | Ujian Tertulis Luring Terjadwal (*Closed-Book*, 150 menit) | `Sub-CPMK-2.1`<br>`Sub-CPMK-2.2` | C3 | • Soal 1: Uji sifat relasi ekuivalensi, Diagram Hasse *Poset*, & *topological sort*<br>• Soal 2: Penyederhanaan predikat logika kueri basis data via Aljabar Boolean & sifat fungsi<br>• Soal 3: Studi masalah kombinatorika (*inclusion-exclusion*, *Pigeonhole*, permutasi/kombinasi)<br>• Soal 4: Penyelesaian relasi rekurensi linier homogen orde-2 (akar karakteristik) | 30%<br>25%<br>25%<br>20% | **30%** |
| **3. Tugas 2** | Mg 12 | Laporan Studi Kasus Pemodelan Graf & Pohon Jaringan (6–8 hal. A4, 2 pekan) | `Sub-CPMK-3.1`<br>`Sub-CPMK-3.2` | C4 | • Bagian A: Pemodelan topologi ke *Adjacency Matrix*, $A^2$, & analisis Euler/Hamilton<br>• Bagian B: Tabel penelusuran lengkap **Algoritma Dijkstra** rute latensi terendah<br>• Bagian C: Konstruksi **Minimum Spanning Tree** dengan **Kruskal & Prim** serta komparasinya<br>• Bagian D: Pemodelan **Pewarnaan Graf** ($\chi(G)$) untuk jadwal pemeliharaan bebas bentrok | 25%<br>30%<br>25%<br>20% | **20%** |
| **4. UAS** | Mg 16 | Ujian Tertulis Komprehensif Luring (*Closed-Book*, 150 menit) | `Sub-CPMK-4.1`<br>`Sub-CPMK-4.2`<br>*(+ Sintesis)* | C4 | • Kasus 1: Konstruksi 5-tupel, diagram, & tabel transisi **DFA** pengenal pola token + jejak $\hat{\delta}$<br>• Kasus 2: Konstruksi **NFA / $\varepsilon$-NFA**, perhitungan $\varepsilon\text{-closure}$, & konversi **Subset Construction** ke DFA<br>• Kasus 3: Minimasi status DFA & pemodelan *Finite State Machine* proses transaksi digital<br>• Kasus 4: Sintesis keterkaitan matriks ketetanggaan graf transisi & predikat logika penjaga status | 25%<br>35%<br>25%<br>15% | **30%** |

---

## 4. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN (STANDAR KPT 2024 LAMPIRAN 23)

### 4.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Kode / SKS** | Matematika Diskrit dan Logika / `STI-204` / 3 SKS Teori |
| **Minggu Rilis & Batas Kumpul** | Dirilis: **Pekan 3** · Batas Pengumpulan: **Pekan 4** (melalui LMS Edlink + kuis konfirmasi 10 menit di kelas) |
| **Bobot Penilaian** | **20%** dari Nilai Akhir Mata Kuliah |
| **CPMK & Sub-CPMK Tujuan** | **`CPMK-1`** (`Sub-CPMK-1.1` & `Sub-CPMK-1.2`): Membuktikan validitas argumen inferensi logika proposisi/predikat dan kebenaran algoritma menggunakan tabel kebenaran, hukum aljabar logika, dan induksi matematika secara runtut dan valid. |
| **1. Tujuan Tugas** | Membentuk disiplin pembuktian matematis formal agar mahasiswa mampu memvalidasi konsistensi aturan bisnis sistem dan kebenaran logika algoritma tanpa bergantung pada coba-coba (*trial and error*). |
| **2. Objek Garapan** | Empat masalah pembuktian formal (*Proof Set* Bab 1–3) yang mencakup kebijakan kontrol akses keamanan sistem informasi, aturan bisnis berkuantor *First-Order Logic*, dan pseudocode algoritma komputasi diskrit. |
| **3. Batasan yang Harus Dikerjakan** | 1. Pada bukti ekuivalensi aljabar logika dan inferensi, **setiap baris transformasi wajib mencantumkan nama hukum/aturan inferensi resmi** yang dipakai (mis. *Hukum De Morgan, Hukum Distributif, Modus Tollens, Resolusi*).<br>2. Pada soal *First-Order Logic*, domain variabel dan arti simbol predikat wajib didefinisikan secara eksplisit sebelum menulis ekspresi kuantor.<br>3. Pada soal Induksi Matematika, wajib memisahkan dengan jelas tiga bagian: **(i) Langkah Basis**, **(ii) Hipotesis Induksi**, dan **(iii) Langkah Induktif** dengan menandai tepat di mana hipotesis induksi disubstitusikan. |
| **4. Metode / Cara Pengerjaan** | Dikerjakan **secara individu** (tulisan tangan rapi terbaca jelas dipindai ke `.pdf` atau ketik $\LaTeX$ / *Equation Editor*). |
| **5. Deskripsi Luaran Tugas** | Berkas tunggal `STI204_T1_[NIM]_[Nama].pdf` berisi penyelesaian berurutan Masalah 1–4 beserta pernyataan integritas akademik. |
| **6. Kriteria & Bobot Penilaian** | Dinilai dengan **Rubrik Analitik Tugas 1 (`058_5`)**: (1) Ketepatan formalisasi simbolik proposisi & kuantor *FOL* (30%); (2) Keabsahan & kelengkapan alasan langkah hukum logika/aturan inferensi (35%); (3) Ketepatan struktur & deduksi Induksi Matematika (35%). |

---

### 4.2 Spesifikasi Instrumen Ujian Tengah Semester (UTS — Pekan 8)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Bentuk & Durasi Ujian** | Ujian Tertulis Luring Terjadwal (*Closed-Book*), durasi **150 menit**. |
| **Bobot & Target Capaian** | **30%** dari Nilai Akhir · Mengukur **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C3]). |
| **Rincian 4 Butir Soal** | 1. **(30% — `Sub-CPMK-2.1`)** Diberikan relasi ketergantungan antar-8 modul pembangunan aplikasi enterprise: buktikan bahwa relasi tersebut merupakan *Poset*, gambarkan **Diagram Hasse**-nya, tentukan elemen minimal/maksimal, dan susun urutan kompilasi valid dengan *Topological Sorting* (disertai 1 sub-soal partisi kelas ekuivalensi).<br>2. **(25% — `Sub-CPMK-2.2`)** Diberikan kondisi predikat seleksi kueri basis data majemuk yang redundan: sederhanakan menggunakan hukum-hukum **Aljabar Boolean formal** hingga jumlah operasi logika minimum dan analisis sifat injektif/surjektif suatu fungsi pemetaan *hash* kunci data.<br>3. **(25% — `Sub-CPMK-2.2`)** Selesaikan studi masalah kombinatorika kardinalitas hasil gabungan kueri (*Inclusion-Exclusion*), jaminan bentrokan slot (*Pigeonhole Principle*), serta pencacahan kombinasi/permutasi konfigurasi akses.<br>4. **(20% — `Sub-CPMK-2.1`)** Tentukan solusi eksplisit tertutup $a_n$ dari suatu relasi rekurensi linier homogen orde-2 beserta kondisi awalnya menggunakan metode persamaan karakteristik. |

---

### 4.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2)

| Komponen RTM | Uraian Rinci Instruksi Resmi |
|---|---|
| **Mata Kuliah / Kode / SKS** | Matematika Diskrit dan Logika / `STI-204` / 3 SKS Teori |
| **Minggu Rilis & Batas Kumpul** | Dirilis: **Pekan 10** · Batas Pengumpulan: **Pekan 12** (melalui LMS Edlink + kuis konfirmasi 10 menit di kelas) |
| **Bobot Penilaian** | **20%** dari Nilai Akhir Mata Kuliah |
| **CPMK & Sub-CPMK Tujuan** | **`CPMK-3`** (`Sub-CPMK-3.1` & `Sub-CPMK-3.2` [C4]): Menganalisis struktur Graf dan Pohon menggunakan matriks representasi (*Adjacency Matrix*) dan algoritma penelusuran lintasan untuk optimasi jaringan data/komputer. |
| **1. Tujuan Tugas** | Melatih kemampuan mahasiswa memodelkan infrastruktur jaringan komunikasi dan masalah penjadwalan organisasi ke dalam struktur Graf dan Pohon serta menyelesaikannya secara analitis-sistematis. |
| **2. Objek Garapan** | Studi kasus perencanaan jaringan serat optik & perutean data antar-10 gedung layanan publik/kampus terpadu (bobot sisi disesuaikan secara unik dengan parameter 2 digit akhir NIM mahasiswa) beserta matriks bentrok jadwal pemeliharaan 8 server layanan. |
| **3. Batasan yang Harus Dikerjakan** | 1. **Bagian A:** Menyusun **Adjacency Matrix** berbobot maupun tak berbobot, menghitung baris terkait pada $A^2$ untuk jumlah rute 2-lompatan, dan menganalisis eksistensi sirkuit/lintasan Euler untuk inspeksi seluruh jalur kabel.<br>2. **Bagian B:** Menelusuri langkah demi langkah dalam bentuk **tabel iterasi lengkap Algoritma Dijkstra** untuk menentukan rute latensi terkecil dari Pusat Data (Simpul $S$) ke seluruh gedung lainnya beserta pohon jalur terpendeknya.<br>3. **Bagian C:** Mengonstruksi **Minimum Spanning Tree (MST)** penarikan kabel fiber optik baru menggunakan **Algoritma Kruskal** dan memverifikasi kesamaan bobot minimumnya menggunakan **Algoritma Prim**.<br>4. **Bagian D:** Memodelkan jadwal pemeliharaan server sebagai graf konflik dan menerapkan **Pewarnaan Graf (*Welsh-Powell*)** untuk menentukan bilangan kromatik $\chi(G)$ slot waktu minimum.<br>5. **Batasan Guardrail:** Fokus pada pemodelan & tabel penelusuran matematis; tidak mengumpulkan kode program implementasi graf (ranah `FST-203`). |
| **4. Metode / Cara Pengerjaan** | Dikerjakan **secara individu** dalam dokumen laporan terstruktur (6–8 halaman A4) dilengkapi gambar visualisasi graf yang rapi. |
| **5. Deskripsi Luaran Tugas** | Berkas `.pdf` bernama `STI204_T2_[NIM]_[Nama].pdf` berisi diagram graf berlabel, matriks, tabel iterasi *Dijkstra*, urutan pemilihan sisi *Kruskal/Prim*, pewarnaan graf, dan deklarasi kejujuran akademik. |
| **6. Kriteria & Bobot Penilaian** | Dinilai dengan **Rubrik Analitik Tugas 2 (`058_5`)**: (1) Akurasi *Adjacency Matrix*, $A^2$, & analisis Euler (25%); (2) Ketelitian tabel iterasi *Dijkstra* & rekonstruksi rute (30%); (3) Ketepatan konstruksi *MST Kruskal & Prim* (25%); (4) Ketepatan pewarnaan graf jadwal & kerapian diagram (20%). |

---

### 4.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16)

| Komponen Spesifikasi | Uraian Rinci Pelaksanaan |
|---|---|
| **Bentuk & Durasi Ujian** | Ujian Tertulis Komprehensif Luring Terjadwal (*Closed-Book*), durasi **150 menit**. |
| **Bobot & Target Capaian** | **30%** dari Nilai Akhir · Mengukur **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C4]) serta sintesis lintas-materi diskrit. |
| **Rincian 4 Kasus Soal** | 1. **(25% — `Sub-CPMK-4.1`)** Konstruksikan definisi formal **5-tupel $M=(Q, \Sigma, \delta, q_0, F)$**, diagram transisi lengkap (termasuk *trap state* bila diperlukan), dan tabel transisi **DFA** untuk memvalidasi pola string kode transaksi tertentu, lalu tunjukkan jejak evaluasi $\hat{\delta}(q_0, w)$ untuk 1 string valid dan 1 string tidak valid.<br>2. **(35% — `Sub-CPMK-4.2`)** Diberikan spesifikasi bahasa gabungan pola atau diagram **$\varepsilon$-NFA**: hitung himpunan $\varepsilon\text{-closure}(q)$ untuk setiap status, lalu terapkan algoritma **Subset Construction** secara sistematis untuk menghasilkan tabel transisi dan diagram **DFA** ekuivalennya.<br>3. **(25% — `Sub-CPMK-4.1 & 4.2`)** Lakukan minimasi jumlah status pada suatu DFA menggunakan partisi ekuivalensi, kemudian modelkan aturan alur hidup pesanan/pembayaran digital 5-status menjadi mesin transisi status yang deterministik dan bebas status buntu tak disengaja.<br>4. **(15% — Sintesis `CPMK-1..4`)** Representasikan diagram transisi suatu otomata sederhana ke dalam *Adjacency Matrix* berarah dan rumuskan kondisi penjaga transisinya (*guard condition*) dalam ekspresi logika formal yang ringkas. |

---

## 5. FORMULA PERHITUNGAN NILAI, MULTI-CPL ATTAINMENT, & KONVERSI MUTU

### 5.1 Rumus Nilai per CPMK dan Nilai Akhir Mata Kuliah ($NA_{\text{STI-204}}$)

Sesuai pemetaan 1-ke-1 **Dokumen 008 §3**:
$$\text{Score}_{\text{CPMK-1}} = S_{\text{Tugas 1}}, \quad \text{Score}_{\text{CPMK-2}} = S_{\text{UTS}}, \quad \text{Score}_{\text{CPMK-3}} = S_{\text{Tugas 2}}, \quad \text{Score}_{\text{CPMK-4}} = S_{\text{UAS}}$$

Nilai Akhir Mata Kuliah ($0\text{–}100$):
$$NA_{\text{STI-204}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 5.2 Formula Skor Ketercapaian 2 CPL pada `STI-204` (Selaras Dokumen 004: `P = 80%`, `KU = 20%`)

1. **Skor Ketercapaian `CPL-05` (`P1` — Bobot 80% MK / Kredit $3 \times 0,80 = 2,40\text{ SKS}$):** Didukung oleh `CPMK-1` (10%), `CPMK-2` (30%), `CPMK-3` (10%), dan `CPMK-4` (30%):
   $$\text{Score}_{\text{CPL-05}}(i) = \frac{10\,S_{\text{Tugas 1}}(i) + 30\,S_{\text{UTS}}(i) + 10\,S_{\text{Tugas 2}}(i) + 30\,S_{\text{UAS}}(i)}{80} = 0,125\,S_{\text{Tugas 1}} + 0,375\,S_{\text{UTS}} + 0,125\,S_{\text{Tugas 2}} + 0,375\,S_{\text{UAS}}$$

2. **Skor Ketercapaian `CPL-02` (`KU1` — Bobot 20% MK / Kredit $3 \times 0,20 = 0,60\text{ SKS}$):** Didukung oleh penalaran pembuktian formal `CPMK-1` (10%) dan analisis jaringan graf `CPMK-3` (10%):
   $$\text{Score}_{\text{CPL-02}}(i) = \frac{10\,S_{\text{Tugas 1}}(i) + 10\,S_{\text{Tugas 2}}(i)}{20} = 0,50\,S_{\text{Tugas 1}}(i) + 0,50\,S_{\text{Tugas 2}}(i)$$

*(Verifikasi Identitas Aljabar: $0,80\,\text{Score}_{\text{CPL-05}} + 0,20\,\text{Score}_{\text{CPL-02}} \equiv 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}} = NA_{\text{STI-204}}$ — 100% konsisten!)*

### 5.3 Tabel Konversi Huruf Mutu & Ambang Ketuntasan OBE

| Rentang Skor ($0\text{–}100$) | Huruf Mutu | Angka Mutu | Status Kelulusan MK | Status Ketercapaian CPL/CPMK OBE ($\ge 65,0$) |
|:---:|:---:|:---:|:---:|:---:|
| $81,00 \text{ – } 100,00$ | **A** | 4,00 | Lulus | **Tercapai (Exemplary)** |
| $76,00 \text{ – } 80,99$ | **B+** | 3,50 | Lulus | **Tercapai (Proficient)** |
| $70,00 \text{ – } 75,99$ | **B** | 3,00 | Lulus | **Tercapai (Satisfactory)** |
| $65,00 \text{ – } 69,99$ | **C+** | 2,50 | Lulus | **Tercapai Minimum Ambang OBE ($\ge 65,0$)** |
| $56,00 \text{ – } 64,99$ | **C** | 2,00 | Lulus Administratif | *Belum Mencapai Target OBE (< 65,0 — Remedial CPMK Terkait)* |
| $45,00 \text{ – } 55,99$ | **D** | 1,00 | Tidak Lulus | **Tidak Tercapai** |
| $0,00 \text{ – } 44,99$ | **E** | 0,00 | Tidak Lulus | **Tidak Tercapai** |

---

## 6. PROTOKOL REMEDIAL, INTEGRITAS PEMBUKTIAN ANTI-HALUSINASI AI, & SIKLUS PPEPP

1. **Pencegahan Bukti Semu Hasil LLM (*Anti-Pseudo-Proof Protocol*):** Model bahasa generatif sering menghasilkan bukti induksi atau konversi NFA $\to$ DFA yang tampak meyakinkan secara kalimat namun melompati justifikasi hukum atau salah menghitung $\varepsilon\text{-closure}$. Oleh sebab itu, Tugas 1 dan Tugas 2 mewajibkan parameterisasi NIM unik serta **kuis verifikasi tertulis 10 menit di awal kelas** saat pengumpulan tugas.
2. **Remedial Spesifik Berbasis CPMK:** Mahasiswa dengan skor komponen $< 65,0$ pada salah satu `CPMK-1..4` diberikan 1 kali kesempatan ujian/tugas perbaikan terarah pada CPMK terkait dengan batas nilai maksimal remedial **70,0 (B)**.
3. **Evaluasi PPEPP & Handoff ke Semester 3:** Portofolio ketercapaian `CPMK-1` (*FOL* & Resolusi) serta `CPMK-3` (Pencarian Graf) diteruskan kepada koordinator `STI-307 Sistem Cerdas` di Semester 3 sebagai pijakan kesiapan awal kohor.
