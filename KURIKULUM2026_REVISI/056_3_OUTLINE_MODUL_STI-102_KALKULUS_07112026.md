# 056_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-102 — KALKULUS (*Calculus*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Semester 1 — Tahap Fondasi)  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI102`  
**Tanggal Penyusunan:** 07 November 2026  
**Rujukan:** `056_1_RPS_STI-102_KALKULUS_07112026.md` · `056_2_SAP_STI-102_KALKULUS_07112026.md` · Dok 007 §4 · Dok 043.

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Buku Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Kalkulus Terapan untuk Sistem Cerdas dan Teknologi Informasi* |
| **Kode & Bobot MK** | `STI-102` · 3 SKS Teori (`TM 150'`, `PT 180'`, `BM 180'`) · Semester 1 |
| **CPL & BoK Didukung** | `CPL-05` (`P1` — Level *Introduce*) · `BK-IS10` (*Applied Mathematics and Logic*) & `BK-IT01` (*IT Fundamentals*) |
| **Target Tebal Naskah Utuh** | 14 Bab Materi Inti + 2 Unit Evaluasi Komprehensif ($\pm 180\text{–}220\text{ halaman}$ A4/B5 termasuk grafik geometri & kunci langkah soal terpilih) |
| **Anatomi Baku Setiap Bab** | (1) *Peta Sub-CPMK & Indikator*; (2) *Motivasi Konteks Komputasi/AI*; (3) *Uraian Konsep, Teorema, & Intuisi Geometri*; (4) *Contoh Soal Bertingkat (Dasar → Menengah → Kasus Sistem TI)*; (5) *Kotak Peringatan Kesalahan Umum & Guardrail*; (6) *Rangkuman Rumus Esensial*; (7) *Latihan Mandiri Berjenjang (10–15 Soal)*. |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen Terkait |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Fungsi, Limit, & Kontinuitas** | **Bab 1** | Sistem Bilangan Riil, Pertidaksamaan, Nilai Mutlak, & Fungsi dalam Komputasi | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Limit Fungsi Aljabar, Limit Sepihak, Teorema Limit, & Perilaku Asimtotik | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | Tugas 1 (20%) |
| | **Bab 3** | Limit Fungsi Transenden, Bentuk Tak Tentu, & Kontinuitas Fungsi | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Kalkulus Diferensial, Gradien, & Optimasi** | **Bab 4** | Konsep Turunan, Keterdiferensialan, & Aturan Dasar Diferensiasi Univariat | Mg 4 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 5** | Aturan Rantai (*Chain Rule*), Implisit, Turunan Parsial Multivariat, & Vektor Gradien | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 6** | Laju Perubahan, Nilai Ekstrem Lokal/Global, Kecekungan, & Uji Turunan | Mg 6 | `CPMK-2` | `Sub-CPMK-2.2` | UTS (30%) |
| | **Bab 7** | Pemodelan Optimasi Ekstremum pada Masalah Biaya, Industri, & Kapasitas TI | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Paket Latihan Komprehensif & Simulasi Ujian Tengah Semester (UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| **Bagian III:<br>Kalkulus Integral & Geometri Luas/Volume** | **Bab 8** | Konsep Antiturunan, Integral Tak Tentu, & Teknik Integrasi Substitusi | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 9** | Teknik Integrasi Parsial (*Integration by Parts*) & Pecahan Parsial | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 10** | Jumlah Riemann, Integral Tentu, & Teorema Dasar Kalkulus I–II | Mg 11 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | Tugas 2 (20%) |
| | **Bab 11** | Aplikasi Integral Tentu: Luas Daerah Antar-Kurva & Volume Benda Putar | Mg 12 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Kalkulus untuk Optimasi AI & Luasan Data** | **Bab 12** | Formulasi Matematis *Gradient Descent* pada Fungsi Kerugian (*Loss Function*) | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13** | Aturan Rantai pada Graf Komputasi & Karakteristik Lanskap Optimasi | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 14** | Aplikasi Integral untuk Pemodelan Luasan Data Komputasi & Kurva *AUC* | Mg 15 | `CPMK-4` | `Sub-CPMK-4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Paket Sintesis Akhir & Simulasi Ujian Akhir Semester (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2` & Sintesis* | *UAS (30%)* |

---

## 3. RINCIAN OUTLINE SUBSTANSI TIAP BAB

### BAGIAN I — FUNGSI, LIMIT, DAN KONTINUITAS (`CPMK-1`)

#### BAB 1: Sistem Bilangan Riil, Pertidaksamaan, Nilai Mutlak, & Fungsi dalam Komputasi (Pekan 1)
* **Sub-CPMK:** `Sub-CPMK-1.1` (C3) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  1.1 Mengapa Kalkulus Dibutuhkan Insinyur Sistem Cerdas? (Dari Variabel Kontinu hingga *Machine Learning*)  
  1.2 Sistem Bilangan Riil, Notasi Selang (*Intervals*), dan Penyelesaian Pertidaksamaan Polinomial/Rasional  
  1.3 Nilai Mutlak $|x-a| < \delta$: Tafsir Jarak, Galat Pengukuran, dan Toleransi Numerik  
  1.4 Konsep Fungsi, Domain–Range, Operasi & Komposisi Fungsi $(f \circ g)(x)$  
  1.5 Fungsi Khusus dalam Komputasi: Fungsi Sepotong-Sepotong (*Piecewise*), *Floor/Ceiling*, dan Fungsi Aktivasi ReLU $f(x)=\max(0,x)$
* **Konteks Kasus TI:** Pemodelan fungsi biaya berlangganan *cloud storage* bertingkat (*tiered pricing*) dan penentuan domain valid rumus waktu respons sistem.
* **Latihan Bab 1:** 12 soal berjenjang (pertidaksamaan rasional, nilai mutlak, komposisi fungsi, dan sketsa fungsi *piecewise*).
* **Guardrail Bab 1:** Tidak membahas aksioma kelengkapan bilangan riil/topologi analisis riil abstrak.

#### BAB 2: Limit Fungsi Aljabar, Limit Sepihak, Teorema Limit, & Perilaku Asimtotik (Pekan 2)
* **Sub-CPMK:** `Sub-CPMK-1.1` & `Sub-CPMK-1.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  2.1 Pengertian Intuitif Limit melalui Pendekatan Numerik dan Grafik  
  2.2 Limit Kiri, Limit Kanan, dan Kriteria Eksistensi Limit Dua Arah  
  2.3 Teorema Limit Utama dan Strategi Penyelesaian Bentuk Tak Tentu Aljabar $0/0$ (Pemfaktoran & Rasionalisasi Sekawan)  
  2.4 Limit Tak-Hingga ($\lim_{x\to c} f(x) = \pm\infty$) dan Limit di Tak-Hingga ($\lim_{x\to\infty} f(x)$)  
  2.5 Penentuan Asimtot Tegak dan Asimtot Datar pada Fungsi Kinerja Komputasi
* **Konteks Kasus TI:** Analisis perilaku batas latensi rata-rata antrean server $L(x) = \frac{x}{\mu - x}$ saat laju kedatangan $x$ mendekati kapasitas maksimum $\mu$ (asimtot tegak) dan efisiensi biaya rata-rata per pengguna saat $n \to \infty$ (asimtot datar).
* **Latihan Bab 2:** 12 soal perhitungan limit sepihak, bentuk $0/0$ akar sekawan, dan perilaku asimtotik.
* **Guardrail Bab 2:** Pembuktian formal $\varepsilon\text{–}\delta$ dikenalkan secara intuitif-geometris saja tanpa membebani pembuktian abstrak rumit.

#### BAB 3: Limit Fungsi Transenden, Bentuk Tak Tentu, & Kontinuitas Fungsi (Pekan 3)
* **Sub-CPMK:** `Sub-CPMK-1.1` & `Sub-CPMK-1.2` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  3.1 Teorema Apit (*Squeeze Theorem*) dan Identitas Dasar Limit Trigonometri ($\lim_{x\to 0}\frac{\sin x}{x}=1$, $\lim_{x\to 0}\frac{1-\cos x}{x}=0$)  
  3.2 Fungsi Eksponensial Alami, Bilangan Euler $e = \lim_{n\to\infty}(1+\frac{1}{n})^n$, dan Limit Logaritma Natural  
  3.3 Tiga Syarat Kontinuitas Fungsi pada Suatu Titik dan Kontinuitas pada Selang Tertutup $[a,b]$  
  3.4 Klasifikasi Titik Diskontinuitas (*Removable, Jump,* dan *Infinite Discontinuity*)  
  3.5 Teorema Nilai Antara (*Intermediate Value Theorem*) dan Makna Kemulusan Fungsi
* **Konteks Kasus TI:** Penentuan parameter transisi tarif/kuota agar kurva penagihan layanan digital tersambung kontinu tanpa lonjakan mendadak (*jump*).
* **Latihan Bab 3 & Persiapan Tugas 1:** 14 soal limit transenden dan uji kontinuitas fungsi sambungan + panduan pengerjaan **RTM-1 (Tugas 1)**.

---

### BAGIAN II — KALKULUS DIFERENSIAL, GRADIEN, DAN OPTIMASI (`CPMK-2`)

#### BAB 4: Konsep Turunan, Keterdiferensialan, & Aturan Dasar Diferensiasi Univariat (Pekan 4)
* **Sub-CPMK:** `Sub-CPMK-2.1` (C3) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  4.1 Masalah Garis Singgung (*Tangent Line*) dan Laju Perubahan Sesaat  
  4.2 Definisi Turunan sebagai Limit Hasil Bagi Selisih $f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$  
  4.3 Hubungan Keterdiferensialan dengan Kontinuitas (Studi Kasus Sudut Tajam pada ReLU & $|x|$)  
  4.4 Aturan Baku Diferensiasi: Konstanta, Pangkat, Kelipatan, Jumlah/Selisih, Hasil Kali, dan Hasil Bagi  
  4.5 Turunan Fungsi Trigonometri, Eksponensial ($e^x, a^x$), dan Logaritma Natural ($\ln x$)
* **Konteks Kasus TI:** Membandingkan sifat keterdiferensialan fungsi aktivasi ReLU vs *Softplus* $g(x)=\ln(1+e^x)$ di titik $x=0$.
* **Latihan Bab 4:** 12 soal diferensiasi aturan dasar, persamaan garis singgung, dan uji keterdiferensialan.

#### BAB 5: Aturan Rantai (*Chain Rule*), Implisit, Turunan Parsial Multivariat, & Vektor Gradien (Pekan 5)
* **Sub-CPMK:** `Sub-CPMK-2.1` (C3) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  5.1 Aturan Rantai (*Chain Rule*) pada Komposisi Fungsi Satu Peubah ($\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}$)  
  5.2 Pembuktian Sifat Turunan Fungsi Logistik Sigmoid $\sigma'(x) = \sigma(x)(1-\sigma(x))$ dan $\tanh'(x) = 1 - \tanh^2(x)$  
  5.3 Diferensiasi Implisit dan Turunan Tingkat Tinggi ($f'', f'''$)  
  5.4 Fungsi Dua atau Lebih Peubah $z = f(x,y)$: Peta Kontur (*Level Curves*) dan Permukaan 3D  
  5.5 Turunan Parsial Orde Pertama ($\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}$), Orde Kedua, dan Penyusunan Vektor Gradien $\nabla f(x,y)$
* **Konteks Kasus TI:** Menghitung vektor gradien permukaan galat prediksi $\nabla E(w_1, w_2)$ dan menafsirkan arah kemiringan tercuram pada peta kontur.
* **Latihan Bab 5:** 14 soal *Chain Rule* berlapis, implisit, turunan parsial, dan evaluasi vektor gradien pada titik tertentu.
* **Guardrail Bab 5:** Notasi vektor gradien dibatasi pada vektor kolom 2–3 peubah nyata; operasi ruang vektor umum, matriks transformasi, dan dekomposisi matriks diserahkan ke `STI-205 Aljabar Linear dan Matriks`.

#### BAB 6: Laju Perubahan, Nilai Ekstrem Lokal/Global, Kecekungan, & Uji Turunan (Pekan 6)
* **Sub-CPMK:** `Sub-CPMK-2.2` (C3/C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  6.1 Laju Perubahan Terkait (*Related Rates*) dalam Pemodelan Dinamis  
  6.2 Nilai Maksimum/Minimum Mutlak pada Selang Tertutup $[a,b]$ dan Titik Kritis ($f'(c)=0$ atau $f'(c)$ tak ada)  
  6.3 Kemonotonan Fungsi (Naik/Turun) dan Uji Turunan Pertama untuk Ekstrem Lokal  
  6.4 Kecekungan Kurva (*Concavity*), Titik Belok (*Inflection Point*), dan Uji Turunan Kedua  
  6.5 Pengantar Kondisi Stasioner Fungsi Dua Peubah ($\nabla f(x,y) = \mathbf{0}$) dan Aturan L'Hôpital untuk Bentuk Tak Tentu
* **Konteks Kasus TI:** Analisis titik puncak beban trafik harian sistem informasi akademik dan penentuan waktu *maintenance window* pada lembah minimum beban.
* **Latihan Bab 6:** 12 soal laju perubahan, klasifikasi titik kritis, kecekungan, dan titik stasioner fungsi dua variabel sederhana.

#### BAB 7: Pemodelan Optimasi Ekstremum pada Masalah Biaya, Industri, & Kapasitas TI (Pekan 7)
* **Sub-CPMK:** `Sub-CPMK-2.2` (C3/C4) · **Estimasi Halaman:** 12–14 hlm.
* **Sub-Pokok Bahasan:**
  7.1 Metodologi 5 Langkah Pemodelan Masalah Optimasi Nyata dengan Kalkulus  
  7.2 Kasus Optimasi Ekonomi & Sistem Enterprise: Maksimasi Laba ($MR = MC$) dan *Economic Order Quantity* (EOQ) pada Rantai Pasok  
  7.3 Kasus Optimasi Infrastruktur TI: Minimasi Fungsi Biaya Gabungan Kapasitas Komputasi Cloud vs Penalti Latensi  
  7.4 Kasus Optimasi Ukuran Paket Data / *Throughput* Efektif Kanal Jaringan
* **Konteks Kasus TI:** Menurunkan rumus EOQ $Q^* = \sqrt{\frac{2DS}{H}}$ secara langsung menggunakan turunan pertama dan kedua fungsi biaya total persediaan.
* **Latihan Bab 7 & Unit Evaluasi E1:** 10 soal cerita pemodelan optimasi + **Paket Simulasi Lengkap UTS (`CPMK-2`)**.

---

### BAGIAN III — KALKULUS INTEGRAL DAN GEOMETRI LUAS/VOLUME (`CPMK-3`)

#### BAB 8: Konsep Antiturunan, Integral Tak Tentu, & Teknik Integrasi Substitusi (Pekan 9)
* **Sub-CPMK:** `Sub-CPMK-3.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  8.1 Antiturunan sebagai Operasi Balikan Diferensiasi dan Makna Konstanta Integrasi $C$  
  8.2 Rumus Baku Integral Tak Tentu Fungsi Aljabar, Trigonometri, dan Eksponensial  
  8.3 Persamaan Diferensial Terpisah Sederhana / Masalah Nilai Awal ($y'(t) = g(t), y(0)=y_0$)  
  8.4 Teknik Integrasi Substitusi (`u-substitution`) sebagai Kebalikan Aturan Rantai
* **Konteks Kasus TI:** Merekonstruksi fungsi akumulasi pertumbuhan pengguna aplikasi dari fungsi laju pertumbuhan harian yang diketahui nilai awalnya.
* **Latihan Bab 8:** 14 soal antiturunan, masalah nilai awal, dan strategi pemisalan variabel $u$.

#### BAB 9: Teknik Integrasi Parsial (*Integration by Parts*) & Pecahan Parsial (Pekan 10)
* **Sub-CPMK:** `Sub-CPMK-3.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  9.1 Penurunan Rumus Integrasi Parsial $\int u\,dv = uv - \int v\,du$ dari Aturan Hasil Kali  
  9.2 Strategi Pemilihan $u$ dan $dv$ Menggunakan Hierarki LIATE serta Metode Tabular untuk Parsial Berulang  
  9.3 Dekomposisi Pecahan Parsial untuk Fungsi Rasional (Faktor Linear Berbeda & Faktor Linear Berulang)  
  9.4 Kerangka Analisis Pemilihan Teknik Integrasi (*Decision Tree*: Langsung vs Substitusi vs Parsial vs Pecahan Parsial)
* **Konteks Kasus TI:** Menyelesaikan bentuk integral $\int x e^{-\lambda x}dx$ yang kelak menjadi dasar perhitungan nilai ekspektasi waktu tunggu layanan server eksponensial.
* **Latihan Bab 9:** 12 soal diagnostik pemilihan metode dan perhitungan integrasi parsial/pecahan parsial.

#### BAB 10: Jumlah Riemann, Integral Tentu, & Teorema Dasar Kalkulus I–II (Pekan 11)
* **Sub-CPMK:** `Sub-CPMK-3.1` & `Sub-CPMK-3.2` (C3/C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  10.1 Masalah Luas Daerah, Partisi Selang, dan Jumlah Riemann $\sum_{i=1}^n f(x_i^*)\Delta x_i$  
  10.2 Definisi Integral Tentu sebagai Limit Jumlah Riemann dan Sifat-Sifat Linearitas/Aditivitas/Simetri  
  10.3 Nilai Rata-Rata Fungsi Kontinu pada Selang $[a,b]$  
  10.4 Teorema Dasar Kalkulus I (Turunan Fungsi Akumulasi) dan Teorema Dasar Kalkulus II ($\int_a^b f(x)\,dx = F(b)-F(a)$)  
  10.5 Transformasi Batas Integrasi pada Substitusi Tentu dan Integrasi Parsial Tentu
* **Konteks Kasus TI:** Menghitung rata-rata suhu sensor *data center* selama satu siklus pendinginan dari kurva fungsi kontinu $T(t)$.
* **Latihan Bab 10:** 12 soal Jumlah Riemann, sifat simetri fungsi ganjil/genap, dan TDK I–II.

#### BAB 11: Aplikasi Integral Tentu: Luas Daerah Antar-Kurva & Volume Benda Putar (Pekan 12)
* **Sub-CPMK:** `Sub-CPMK-3.2` (C3/C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  11.1 Perbedaan Integral Bertanda (*Net Signed Area*) vs Luas Geometris Mutlak $\int_a^b |f(x)|\,dx$  
  11.2 Perhitungan Luas Daerah di Antara Dua Kurva (Pias Tegak $dx$ dan Pias Mendatar $dy$)  
  11.3 Volume Benda Putar dengan Metode Cakram (*Disk Method*)  
  11.4 Volume Benda Putar Berongga dengan Metode Cincin (*Washer Method*)
* **Konteks Kasus TI:** Menghitung luasan selisih penghematan daya antara kurva konsumsi server lama vs server tervirtualisasi baru selama 12 bulan operasi, serta volume kubah pelindung sensor IoT.
* **Latihan Bab 11 & Panduan Tugas 2:** 12 soal sketsa daerah, luas antar-kurva, dan volume benda putar + panduan penyelesaian **RTM-2 (Tugas 2)**.

---

### BAGIAN IV — KALKULUS UNTUK OPTIMASI AI DAN PEMODELAN LUASAN DATA (`CPMK-4`)

#### BAB 12: Formulasi Matematis *Gradient Descent* pada Fungsi Kerugian (*Loss Function*) (Pekan 13)
* **Sub-CPMK:** `Sub-CPMK-4.1` (C4) · **Estimasi Halaman:** 16–18 hlm.
* **Sub-Pokok Bahasan:**
  12.1 Dari Pencarian Akar $\nabla J = \mathbf{0}$ ke Optimasi Iteratif: Mengapa Algoritma *Gradient Descent* Diperlukan?  
  12.2 Anatomi Fungsi Kerugian Kuadrat Rata-Rata (*Mean Squared Error / MSE*) $J(w,b) = \frac{1}{n}\sum_{i=1}^n (wx_i + b - y_i)^2$  
  12.3 Penurunan Analitis Komponen Gradien $\frac{\partial J}{\partial w}$ dan $\frac{\partial J}{\partial b}$  
  12.4 Persamaan Pembaruan Parameter $\theta^{(t+1)} = \theta^{(t)} - \eta \nabla J(\theta^{(t)})$ dan Simulasi Langkah demi Langkah di Atas Kertas  
  12.5 Analisis Matematis Pengaruh *Learning Rate* $\eta$: Konvergensi Monoton, Osilasi, dan Divergensi (*Overshooting*)
* **Konteks Kasus TI:** Simulasi tangan lengkap 3 iterasi *Gradient Descent* untuk mencocokkan garis prediksi pada 3 titik data pengamatan nyata tanpa bantuan pustaka *black-box*.
* **Latihan Bab 12:** 10 soal penurunan gradien berbagai fungsi kerugian ($L_2$, fungsi kuadratik terboboti) dan analisis batas konvergensi $\eta$.
* **Guardrail Bab 12:** Fokus 100% pada penurunan rumus kalkulus dan iterasi numerik kecil; dilarang melebar ke penulisan *pipeline training* `scikit-learn`/`PyTorch` (`STI-413`/`STI-624`).

#### BAB 13: Aturan Rantai pada Graf Komputasi & Karakteristik Lanskap Optimasi (Pekan 14)
* **Sub-CPMK:** `Sub-CPMK-4.1` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  13.1 Merepresentasikan Fungsi Komposisi Bersusun sebagai Graf Komputasi Berarah  
  13.2 Penelusuran Nilai Maju (*Forward Evaluation*) dan Perkalian Turunan Parsial Mundur (*Chain Rule / Mathematical Backprop*)  
  13.3 Studi Kasus Kalkulus Unit Neuron Tunggal: $z = wx+b \to \hat{y} = \sigma(z) \to L = \frac{1}{2}(\hat{y}-y)^2$  
  13.4 Geometri Lanskap Optimasi: Fungsi Konveks vs Non-Konveks, Minimum Lokal vs Global, dan Titik Pelana (*Saddle Point*)  
  13.5 Telaah Kalkulus Peluruhan Turunan (*Vanishing Derivative*) ketika $\sigma'(z) \to 0$ pada Nilai $|z|$ Ekstrem
* **Konteks Kasus TI:** Membuktikan secara analitis mengapa gradien fungsi aktivasi sigmoid mengecil drastis di daerah jenuh dibandingkan ReLU untuk $z > 0$.
* **Latihan Bab 13:** 10 soal graf komputasi berantai dan identifikasi titik pelana vs minimum lokal.

#### BAB 14: Aplikasi Integral untuk Pemodelan Luasan Data Komputasi & Kurva *AUC* (Pekan 15)
* **Sub-CPMK:** `Sub-CPMK-4.2` (C4) · **Estimasi Halaman:** 14–16 hlm.
* **Sub-Pokok Bahasan:**
  14.1 Pemodelan Akumulasi Laju Kontinu pada Sistem TI: Volume Trafik Jaringan $V = \int_{t_1}^{t_2} r(t)\,dt$ dan Konsumsi Energi Server  
  14.2 Aproksimasi Integral pada Data Pengukuran Diskrit: Aturan Trapesium (*Trapezoidal Rule*)  
  14.3 Matematika di Balik Metrik Evaluasi Model Klasifikasi: Luas di Bawah Kurva (*Area Under the Curve / AUC*) pada Ruang $[0,1]^2$  
  14.4 Pengantar Fungsi Rapat Data Kontinu Non-Negatif: Syarat Normalisasi Luas Total $\int_{-\infty}^{\infty} f(x)\,dx = 1$ dan Luas Selang $[a,b]$  
  14.5 Peta Keterhubungan *Handoff* Kalkulus menuju `STI-205`, `FST-408`, dan `STI-413`
* **Konteks Kasus TI:** Menghitung nilai *AUC* dari kurva fungsi analitis sederhana dan dari tabel 5 titik koordinat *(False Positive Rate, True Positive Rate)* menggunakan aturan trapesium.
* **Latihan Bab 14 & Unit Evaluasi E2:** 10 soal pemodelan luasan data komputasi + **Paket Simulasi Lengkap UAS (`CPMK-4` & Sintesis)**.
* **Guardrail Bab 14:** Fungsi rapat kontinu hanya dibahas dari sisi syarat kalkulus integral ($\ge 0$ dan luas $= 1$); teori peluang aksiomatik, distribusi normal baku $Z$, dan uji hipotesis diserahkan penuh ke `FST-408 Probabilitas dan Statistika`.
