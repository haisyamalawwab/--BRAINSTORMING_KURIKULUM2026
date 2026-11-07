# 068_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-414 — PENGANTAR NLP & TEMU BALIK INFORMASI (*Introduction to NLP & Information Retrieval*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI414` · **Klaster Rubrik Master (Dok 018):** Klaster 3 (`K-3`)  
**CPL:** `CPL-06` (`P2` = 45%) & `CPL-09` (`KK1` = 55%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN PEMROSESAN BAHASA ALAMI & TEMU BALIK INFORMASI (`K-3`)

Mengacu **Dokumen 018 §3 (Klaster `K-3`)**, penilaian pada `STI-414` mengukur ketelitian pembersihan linguistik korpus bahasa alami, kebenaran struktur pengindeksan dan algoritma pemeringkatan temu balik (**Inverted Index, TF-IDF, BM25**) beserta validitas metrik *Precision/Recall/MAP*, ketajaman pemodelan klasifikasi teks/sentimen berbasis *Word Embedding* (**Word2Vec/FastText**) bebas kebocoran kosakata, serta keandalan purwarupa aplikasi cerdas berbasis pustaka modern.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-06` [C3])
**Objek Penilaian:** *Notebook* Tahapan **Text Preprocessing** Korpus Berderau & Konstruksi **VSM / TF-IDF**.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Ketepatan *Text Preprocessing* (*Tokenisasi, Normalisasi, Stopword, Stemming/Lemmatisasi*)**<br>(`Sub-CPMK-1.1`) | **45%** | Pembersihan Regex presisi, normalisasi kata tidak baku tepat, *stopword removal* selektif (menjaga kata negasi penting), dan *stemming/lemmatisasi* berjalan akurat tanpa merusak token bermakna. | Seluruh tahapan *preprocessing* diimplementasikan dengan rapi dan menghasilkan token yang bersih. | Tahapan dasar *lowercase, tokenisasi, stopword,* dan *stemming* berjalan, namun normalisasi kata *slang* masih sangat terbatas. | Urutan *preprocessing* terbalik (mis. menghapus spasi sebelum tokenisasi) sehingga merusak ratusan kata korpus! | Tidak mampu mengimplementasikan tahapan dasar *text preprocessing*. |
| **2. Konstruksi **Vector Space Model (VSM)** & **TF-IDF****<br>(`Sub-CPMK-1.2`) | **35%** | Konfigurasi `TfidfVectorizer` (`ngram_range, min_df, max_df, sublinear_tf`) optimal, matriks renggang efisien, dan perhitungan pencarian *Cosine Similarity* akurat dan tervalidasi. | Representasi VSM dan bobot TF-IDF terbangun benar serta fungsi kemiripan kosinus mengembalikan dokumen relevan. | Berhasil membangun matriks TF-IDF standar bawaan, namun belum memanfaatkan parameter pemangkasan derau kosakata. | Salah menggunakan vektor frekuensi mentah saat diminta TF-IDF atau salah rumus kemiripan kosinus. | Gagal membangun matriks representasi teks TF-IDF. |
| **3. Analisis Statistik Kosakata & Verifikasi Lab** | **20%** | Menyajikan perbandingan tajam ukuran kosakata, kata teratas, dan contoh kalimat sebelum vs sesudah *preprocessing* serta menjawab verifikasi lab dengan sempurna. | Menyertakan statistik perubahan kosakata yang jelas dan lulus verifikasi kode di lab. | Menampilkan beberapa contoh hasil pembersihan teks dengan cukup jelas. | Tidak ada evaluasi apakah hasil *preprocessing* benar-benar bersih atau justru mengosongkan dokumen. | Menyalin kode rekan atau gagal saat verifikasi lab. |

$$\text{Skor Tugas 1} = 0,45(K_1) + 0,35(K_2) + 0,20(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 25% MK · Mengukur `CPMK-2` / `CPL-06` [C4])
**Objek Penilaian:** Ujian Praktik 150 Menit: Konstruksi **Inverted Index, TF-IDF VSM, Okapi BM25,** & Evaluasi **Precision/Recall/F1/MAP**.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Konstruksi Struktur **Inverted Index****<br>(`Sub-CPMK-2.1`) | **30%** | Struktur kamus istilah $\rightarrow$ *posting list* (`doc_id`, frekuensi) terbangun bersih, cepat, dan fungsi kueri kata kunci mengembalikan kandidat dokumen dengan tepat 100%. | *Inverted index* terbangun benar dan mampu melayani pengambilan daftar dokumen per istilah kueri. | Struktur indeks dasar berfungsi, namun belum menyimpan informasi frekuensi atau panjang dokumen secara rapi. | Tidak membangun *inverted index* sejati (masih memindai ulang seluruh teks mentah di setiap kueri). | Kode pengindeksan gagal berjalan. |
| **2. Implementasi Pemeringkatan **Okapi BM25 & VSM****<br>(`Sub-CPMK-2.1`) | **35%** | Implementasi pemeringkatan **BM25** ($k_1, b$) dan **TF-IDF VSM** akurat, menghasilkan urutan peringkat relevan, dan disertai analisis perbandingan tajam antar-keduanya. | Kedua metode pemeringkatan (VSM dan BM25) berjalan benar dan menghasilkan peringkat dokumen yang valid. | Berhasil menjalankan salah satu metode pemeringkatan dengan benar penuh dan metode kedua secara parsial. | Rumus skor BM25/IDF keliru tanda sehingga dokumen paling tidak relevan justru muncul di peringkat 1! | Gagal mengimplementasikan sistem pemeringkatan temu balik. |
| **3. Evaluasi Kinerja IR (**Precision, Recall, F1, P@K, MAP**)**<br>(`Sub-CPMK-2.2`) | **35%** | Perhitungan **Precision, Recall, F1, P@5,** dan **MAP** terhadap berkas *qrels* 100% akurat beserta diagnosis tajam penyebab *false positive / false negative* pencarian. | Seluruh metrik evaluasi IR utama dihitung dengan benar dan diinterpretasikan secara tepat. | Menghitung *Precision, Recall,* dan *F1* dengan benar, namun terdapat kekeliruan kecil pada perataan *Average Precision* (MAP). | Salah membagi penyebut antara *Precision* (dibagi total terambil) dan *Recall* (dibagi total relevan di korpus). | Bagian evaluasi metrik IR tidak dikerjakan. |

$$\text{Skor UTS} = 0,30(K_1) + 0,35(K_2) + 0,35(K_3)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 25% MK · Mengukur `CPMK-3` / `CPL-09` [C4])
**Objek Penilaian:** Proyek **Word Embedding (Word2Vec & FastText)** serta **Klasifikasi Teks & Analisis Sentimen** Ber-**F1** Optimal.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Implementasi **Word2Vec & FastText** serta Agregasi Vektor**<br>(`Sub-CPMK-3.1`) | **35%** | Melatih **Word2Vec** & **FastText** secara tepat (hanya pada korpus latih!), membuktikan keunggulan *subword FastText* atas kata *typo/OOV*, dan membentuk vektor dokumen (*weighted pooling*) dengan bersih. | Implementasi Word2Vec/FastText dan konversi dokumen ke vektor fitur berjalan akurat dan teruji. | Berhasil melatih Word2Vec dasar dan merata-rata vektor kata (*mean pooling*), namun pengujian kasus OOV FastText masih ringkas. | Vektor dokumen rusak karena gagal menangani kata yang tidak ada di kamus Word2Vec (`ZeroDivision/NaN`). | Tidak mengimplementasikan representasi *word embedding*. |
| **2. Pengembangan Klasifikasi Teks & Capaian **F1-Score****<br>(`Sub-CPMK-3.2`) | **40%** | Membandingkan *Multinomial NB* dan *Linear SVM/Logistic* lintas representasi (TF-IDF N-Gram vs Embeddings) secara **100% bebas *vocabulary leakage*** dan mencapai **Macro-F1** optimal melalui penalaan sistematis. | Pipeline klasifikasi sentimen/teks bersih bebas *leakage* dan mencapai skor *F1* yang kompetitif serta tervalidasi. | Model klasifikasi teks berjalan dan dievaluasi dengan *F1-Score*, namun variasi fitur N-Gram atau parameter belum ditala maksimal. | **Terjadi *Vocabulary Leakage*** (menge-*fit* `TfidfVectorizer` pada seluruh teks sebelum *train/test split*) atau hanya melaporkan *Accuracy*. | Model klasifikasi teks gagal dilatih atau akurasi setara tebakan acak. |
| **3. Ketajaman *Linguistic Error Analysis* & Verifikasi Lab** | **25%** | Membedah minimal 10 contoh gagal prediksi secara linguistik tajam (negasi, kontras, sarkasme, ambiguitas domain) beserta usulan perbaikan nyata dan fasih saat diuji di lab. | Menyajikan analisis contoh kalimat salah prediksi yang relevan dan menguasai kodenya saat verifikasi lab. | Menampilkan beberapa kalimat salah prediksi namun penjelasannya masih bersifat umum. | Tidak memeriksa isi teks yang salah diprediksi model sama sekali. | Plagiarisme *notebook* atau gagal menjelaskan kode di lab. |

$$\text{Skor Tugas 2} = 0,35(K_1) + 0,40(K_2) + 0,25(K_3)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-09` [C5])
**Objek Penilaian:** **Purwarupa Aplikasi NLP / Mesin Pencari Cerdas** Terintegrasi Pustaka Modern (`spaCy`/`NLTK`/`HuggingFace`) + Sidang Uji Kueri.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Arsitektur Rancangan Solusi NLP / Mesin Pencari Cerdas**<br>(`Sub-CPMK-4.1`) | **30%** | Merancang arsitektur aplikasi yang memadukan secara cerdas teknik semester ini (mis. *Hybrid BM25 + Semantic Reranking + Filter NER + Sorotan Cuplikan*) untuk masalah pengguna yang nyata. | Rancangan alur pemrosesan teks/pencarian dan antarmuka purwarupa terstruktur jelas serta tepat guna. | Aplikasi memiliki alur dasar input kueri/teks $\rightarrow$ proses NLP/IR $\rightarrow$ tampilan hasil yang fungsional. | Rancangan terlalu dangkal (sekadar pembungkus 5 baris fungsi tunggal tanpa rekayasa korpus/alur pencarian). | Tidak memiliki rancangan arsitektur solusi yang jelas. |
| **2. Integrasi Pustaka/API NLP Modern (`spaCy`/`NLTK`/`HuggingFace`)**<br>(`Sub-CPMK-4.2`) | **35%** | Integrasi pustaka modern bersih, memakai *model caching* sehingga respons cepat, menangani input kosong/karakter aneh dengan aman, dan berjalan mulus saat diuji kueri langsung oleh dosen. | Integrasi pustaka `spaCy`/`NLTK`/`HuggingFace` berfungsi andal menghasilkan keluaran cerdas pada aplikasi purwarupa. | Integrasi pustaka NLP berjalan untuk kasus standar, namun pemuatan model belum di-*cache* atau agak lambat. | Pemanggilan pustaka/API sering *timeout/error* saat diberi kalimat baru di luar contoh demo. | Purwarupa gagal dijalankan saat sidang. |
| **3. Evaluasi Kuantitatif Kualitas Solusi (*IR/NLP Metrics*)** | **20%** | Menyertakan pengujian terukur atas $\ge 20$ kueri/sampel uji nyata (melaporkan *P@5 / MAP / F1* + latensi rata-rata) yang membuktikan peningkatan kualitas dibanding *baseline* sederhana. | Menyertakan tabel evaluasi metrik relevansi/akurasi yang valid untuk menilai kelayakan purwarupa. | Menyertakan pengujian fungsional beberapa contoh kueri namun metrik kuantitatifnya masih terbatas. | Hanya mengklaim aplikasi *"sudah akurat"* tanpa satu pun pengukuran metrik evaluasi. | Tidak ada pengujian dan dokumentasi evaluasi. |
| **4. Penguasaan Teknis Sidang & Tanya-Jawab Individu** | **15%** | Setiap anggota tim fasih menjelaskan cara kerja indeks, model NLP yang diintegrasikan, serta alasan pemilihan arsitekturnya secara kritis. | Anggota mampu mendemonstrasikan dan menjelaskan modul bagiannya dengan tepat. | Anggota memahami alur utama aplikasi dengan sedikit bantuan. | Tidak mampu menjelaskan kode integrasi maupun metrik evaluasi proyeknya sendiri. | Tidak hadir sidang UAS atau melanggar kejujuran akademik. |

$$\text{Skor UAS} = 0,30(K_1) + 0,35(K_2) + 0,20(K_3) + 0,15(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF PRAKTIKUM LABORATORIUM MINGGUAN (LAB 1–14)

| Kriteria Formatif Lab | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketuntasan & Kebersihan Eksperimen Teks** | Notebook lab selesai tuntas, menguji contoh kalimat Bahasa Indonesia sendiri, dan mencatat analisis hasil. | Notebook praktikum selesai tepat waktu dengan keluaran benar. | Menyelesaikan minimal 75% tahapan praktikum di lab. | Tidak menuntaskan latihan dasar praktikum mingguan. |
| **Kesadaran Efisiensi Komputasi Korpus** | Menggunakan operasi vektorisasi/matriks renggang dan menghindari *nested loop* lambat pada ribuan dokumen. | Kode berjalan dalam waktu wajar sesuai ukuran korpus latihan. | Kode menghasilkan jawaban benar namun masih memakai perulangan kurang efisien. | Kode macet/*hang* karena kesalahan struktur perulangan. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-414` (`CPL-06` & `CPL-09` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai penuh pemrosesan korpus dwibahasa, pembangunan mesin pencari **Inverted Index & BM25** terukur (*MAP/P@K*), klasifikasi teks berbasis **Word2Vec/FastText** ber-**F1** tinggi, serta mampu merancang purwarupa aplikasi NLP/pencarian cerdas modern yang andal. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa terampil menerapkan *text preprocessing*, TF-IDF VSM, BM25, evaluasi IR, *word embeddings*, klasifikasi sentimen, dan integrasi pustaka `spaCy`/`HuggingFace` pada purwarupa fungsional. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) dalam pembersihan teks dasar, representasi TF-IDF/BM25, klasifikasi sentimen standar, dan pembuatan purwarupa aplikasi NLP sederhana. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih merusak teks saat *preprocessing*, keliru menghitung metrik *Precision/Recall*, mengalami kebocoran kosakata uji, atau gagal mengintegrasikan pustaka NLP ke aplikasi. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai konsep dasar NLP dan temu balik informasi atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-414` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menerapkan tahapan *text preprocessing* (*tokenisasi, normalisasi, stopword, stemming/lemmatisasi*) secara akurat. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu membangun representasi teks **Vector Space Model (VSM)** dan **TF-IDF** pada korpus dokumen. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu mengimplementasikan sistem temu balik informasi menggunakan **Inverted Index** dan **Okapi BM25**. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu mengevaluasi kinerja sistem IR menggunakan metrik **Precision, Recall, F1,** dan **MAP**. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu mengimplementasikan *word embedding* (**Word2Vec & FastText**) untuk representasi semantik teks. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu mengembangkan model klasifikasi teks dan analisis sentimen (*Naive Bayes, SVM*) dengan **F1-Score** optimal. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu merancang purwarupa aplikasi NLP atau mesin pencari cerdas menggunakan `spaCy`/`NLTK`/`HuggingFace`. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu mengintegrasikan pustaka/API NLP modern sebagai solusi cerdas yang teruji bagi kebutuhan pengguna. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-414`)

```text
==============================================================================================================================
     LEMBAR REKAPITULASI PENILAIAN OBE — STI-414 PENGANTAR NLP & TEMU BALIK INFORMASI (2 SKS: T=1, P=1)
==============================================================================================================================
Semester / TA  : Semester 4 (Genap) / 2026-2027      CPL Dibebankan : CPL-06 (P2: 45%) & CPL-09 (KK1: 55%) [Level: Reinforce]
Klaster Rubrik : K-3 (AI, Cloud & Cybersecurity)     Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (25%)   | T2 (25%)    | UAS (30%)   | NA    | CPL-06 | CPL-09 | Huruf
   |           |                  | [CPMK-1:C3] | [CPMK-2:C4] | [CPMK-3:C4] | [CPMK-4:C5] | Akhir | (45%)  | (55%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 88.0        | 85.0        | 88.0        | 88.0        | 87.25 | 86.33  | 88.00  | A
2  | 250101002 | [Nama Mhs 2]     | 78.0        | 74.0        | 78.0        | 78.0        | 77.00 | 75.78  | 78.00  | B+
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0        | 68.00 | 66.89  | 68.91  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 78.00       | 75.00       | 78.67       | 78.00       | 77.42 | 76.33  | 78.30  | >=65:100%
==============================================================================================================================
```
