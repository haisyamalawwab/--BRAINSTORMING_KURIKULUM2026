# 068_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-414 — PENGANTAR NLP & TEMU BALIK INFORMASI (*Introduction to NLP & Information Retrieval*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.2.RPS-STI414`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Pengantar NLP & Temu Balik Informasi / *Introduction to NLP & Information Retrieval* |
| **Kode Mata Kuliah** | `STI-414` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Kecerdasan Artifisial & Rekayasa Data (*Core STI*) |
| **Bobot SKS & Tipe** | **2 SKS (`+P`)** (`T = 1, P = 1`) — Tatap Muka `1×50' = 50'`, Praktikum Terbimbing `1×170' = 170'`, Penugasan Terstruktur `1×60' = 60'`, Belajar Mandiri `1×60' = 60'` per pekan |
| **Semester / Tahun Akademik** | Semester 4 (Genap) — Tahap Penguatan Pemrosesan Teks & Pencarian Cerdas (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `STI-307` Sistem Cerdas |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Bersinergi dengan `STI-413` Pembelajaran Mesin; menyerahkan pemodelan jaringan saraf sekuensial/Transformer ke `STI-624` Pembelajaran Mendalam & Jaringan Saraf, layanan cerdas ke `STI-726` Integrasi Layanan Cerdas Berbasis AI, & agen LLM/RAG ke `STA-702` AI Percakapan dan Asisten Cerdas |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-06` (`P2` = **45%**) dan `CPL-09` (`KK1` = **55%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 3 (`K-3`)** — Kecerdasan Artifisial, Cloud & Cybersecurity (Bobot MK `+P`: Tugas 1 `20%` · UTS `25%` · Tugas 2 `25%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Sistem Cerdas & Sains Data |
| **Koordinator RMK** | Dr. Istiadi, S.T., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-06`** (`P2`) | Pengetahuan | Menguasai konsep sistem informasi, analisis & pemodelan proses bisnis, arsitektur enterprise, manajemen proyek TI, serta konsep dasar kecerdasan artifisial dan pembelajaran mesin. | **R** (*Reinforce*) | **45%** |
| **`CPL-09`** (`KK1`) | Keterampilan Khusus | Mampu merancang, melatih, mengevaluasi, dan mengintegrasikan model kecerdasan artifisial (*Machine Learning, Deep Learning, NLP, Computer Vision*) ke dalam sistem informasi cerdas. | **R** (*Reinforce*) | **55%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **menerapkan tahapan pemrosesan awal teks** (*Text Preprocessing: tokenisasi, normalisasi, stopword removal, stemming/lemmatisasi*) (*B*) pada korpus teks bahasa alami (*C*) secara akurat (*D*). | **C3** (*Apply*) | `CPL-06` (`P2`) | **Tugas 1 — Pekan 4 (20%)** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **menganalisis dan membangun model representasi teks serta sistem temu balik informasi** (*Information Retrieval: TF-IDF, Vector Space Model, BM25, Inverted Index*) (*B*) untuk pencarian dokumen relevan (*C*) dengan presisi dan *recall* terukur (*D*). | **C4** (*Analyze*) | `CPL-06` (`P2`) | **UTS — Pekan 8 (25%)** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **mengembangkan model klasifikasi teks dan analisis sentimen** (*B*) menggunakan teknik *machine learning* dan *word embedding* (*Word2Vec, FastText*) (*C*) dengan metrik *F1-score* optimal (*D*). | **C4** (*Analyze*) | `CPL-09` (`KK1`) | **Tugas 2 — Pekan 12 (25%)** |
| **`CPMK-4`** | Mahasiswa (*A*) mampu **merancang purwarupa aplikasi pemrosesan bahasa alami atau mesin pencari cerdas** (*B*) dengan mengintegrasikan API/library NLP modern (*HuggingFace / spaCy / NLTK*) (*C*) sebagai solusi cerdas kebutuhan pengguna (*D*). | **C5** (*Evaluate*) | `CPL-09` (`KK1`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Menerapkan tahapan *text preprocessing* (*tokenisasi, normalisasi, stopword, stemming/lemmatisasi*). | `CPMK-1` | **C3** | Mg 1–3 |
| **`Sub-CPMK-1.2`** | Membangun representasi teks *Vector Space Model* (VSM) dan **TF-IDF** pada korpus. | `CPMK-1` | **C3** | Mg 3–4 |
| **`Sub-CPMK-2.1`** | Mengimplementasikan *Information Retrieval* dengan **BM25** dan **inverted index**. | `CPMK-2` | **C4** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Mengevaluasi kinerja IR menggunakan metrik **presisi, recall, dan F1** (*serta Precision@K / MAP*). | `CPMK-2` | **C4** | Mg 7 |
| **`Sub-CPMK-3.1`** | Mengimplementasikan *word embedding* dasar (**Word2Vec / FastText**) untuk representasi teks padat. | `CPMK-3` | **C4** | Mg 9–10 |
| **`Sub-CPMK-3.2`** | Mengembangkan model klasifikasi teks dan analisis sentimen (*Naive Bayes, SVM teks*) dengan **F1** optimal. | `CPMK-3` | **C4** | Mg 11–12 |
| **`Sub-CPMK-4.1`** | Merancang purwarupa aplikasi NLP/mesin pencari menggunakan library modern (`spaCy`/`NLTK`/`HuggingFace`). | `CPMK-4` | **C5** | Mg 13–14 |
| **`Sub-CPMK-4.2`** | Mengintegrasikan API/library NLP modern sebagai solusi cerdas kebutuhan pengguna yang teruji. | `CPMK-4` | **C5** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-4: Purwarupa Aplikasi NLP / Mesin Pencari Cerdas Berbasis spaCy/NLTK/HuggingFace (C5) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-4.1: POS/NER spaCy & Hybrid Search/NLP Design | Sub-CPMK-4.2: Pretrained Pipeline Integration & Evaluation)
      │
[CPMK-3: Klasifikasi Teks, Analisis Sentimen, & Dense Word Embedding Word2Vec/FastText (C4) — Mg 9–12 (Tugas 2 25%)]
      ▲  (Sub-CPMK-3.1: CBOW/Skip-Gram Word2Vec & Subword FastText | Sub-CPMK-3.2: Multinomial NB & Linear SVM Sentiment F1)
      │
[CPMK-2: Sistem Temu Balik Informasi (Inverted Index, VSM, Okapi BM25) & Evaluasi IR (C4) — Mg 5–8 (UTS 25%)]
      ▲  (Sub-CPMK-2.1: Posting List Inverted Index, Cosine VSM, BM25 Ranking | Sub-CPMK-2.2: Precision@K, Recall, F1, MAP)
      │
[CPMK-1: Tahapan Text Preprocessing Korpus Bahasa Alami & Representasi Dasar TF-IDF (C3) — Mg 1–4 (Tugas 1 20%)]
         (Sub-CPMK-1.1: Regex, Tokenization, Normalization, Stopword, Stemming/Lemmatization | Sub-CPMK-1.2: BoW, N-Gram, TF-IDF)
      ▲
[Fondasi Prasyarat: STI-307 Sistem Cerdas + Sinergi Vektor/Cosine STI-205 & Klasifikasi STI-413]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-06`** (`P2`) | **`CPMK-1`** | `Sub-CPMK-1.1`, `Sub-CPMK-1.2` | **20%** | — | — | — | **20%** | **`CPL-06` = 45%** |
| **`CPL-06`** (`P2`) | **`CPMK-2`** | `Sub-CPMK-2.1`, `Sub-CPMK-2.2` | — | **25%** | — | — | **25%** | *(20% + 25%)* |
| **`CPL-09`** (`KK1`) | **`CPMK-3`** | `Sub-CPMK-3.1`, `Sub-CPMK-3.2` | — | — | **25%** | — | **25%** | **`CPL-09` = 55%** |
| **`CPL-09`** (`KK1`) | **`CPMK-4`** | `Sub-CPMK-4.1`, `Sub-CPMK-4.2` | — | — | — | **30%** | **30%** | *(25% + 30%)* |
| **Total** | **4 CPMK** | **8 Sub-CPMK** | **20%** | **25%** | **25%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-3` Dok 018):** `Tugas 1 (20% — Case-Based Indonesian/English Noisy Corpus Preprocessing) + Tugas 2 (25% — Case-Based Sentiment/Topic Classification with Word Embeddings) + UAS (30% — Project-Based Smart Search / NLP Application Prototype)` = **75%** *(melampaui ambang 50% dan selaras penuh dengan target IKU 7 Dokumen 004)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-414 Pengantar NLP & Temu Balik Informasi` (2 SKS `+P`) membekali mahasiswa dengan dasar matematis dan keahlian rekayasa praktis untuk mengolah teks tak-terstruktur serta membangun mesin pencari dokumen relevan. Mahasiswa mempelajari pembersihan korpus bahasa alami Bahasa Indonesia dan Inggris (*Regex, tokenisasi, normalisasi kata gaul/singkatan, stopword removal, stemming Nazief-Adriani `Sastrawi` & Porter, lemmatisasi*), pemodelan ruang vektor renggang (*Bag-of-Words, N-Gram, **TF-IDF**, Cosine Similarity*), arsitektur **Information Retrieval** (*Inverted Index, Boolean Retrieval,* & pemeringkatan probabilistik **Okapi BM25**) beserta evaluasi *Precision, Recall, F1, Precision@K,* dan *MAP*, representasi vektor padat (*Word2Vec CBOW/Skip-Gram* & *FastText*), klasifikasi teks & analisis sentimen (*Multinomial Naive Bayes, Linear SVM*), hingga perancangan purwarupa aplikasi NLP/pencarian cerdas yang mengintegrasikan pustaka modern (`NLTK`, `spaCy`, dan *pretrained pipeline* `HuggingFace`).

* **🟢 IN-SCOPE (Wajib Diajarkan):** *Text Preprocessing* (`NLTK`, `Sastrawi`, `spaCy`), *N-Gram*, **Vector Space Model (VSM) & TF-IDF**, **Inverted Index & Okapi BM25**, metrik evaluasi IR (*Precision, Recall, F1, P@K, MAP*), *Word Embedding* dasar (**Word2Vec, FastText**), klasifikasi teks & analisis sentimen (*Naive Bayes, SVM*), *POS Tagging / NER* praktis, serta integrasi pustaka/API NLP modern pada purwarupa aplikasi.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. **Dilarang menurunkan atau melatih arsitektur *Transformer Self-Attention* / RNN-LSTM dari nol** (ranah eksklusif **`STI-624 Pembelajaran Mendalam & Jaringan Saraf`**; pada `STI-414` model *pretrained* `HuggingFace` hanya dipanggil pada tahap akhir integrasi inferensi tingkat aplikasi).
  2. Dilarang membahas *fine-tuning* *Large Language Models* (LLM LoRA/QLoRA), rekayasa agen percakapan multi-giliran, maupun arsitektur *Enterprise Retrieval-Augmented Generation* (RAG) penuh (ranah eksklusif peminatan **`STA-702 AI Percakapan dan Asisten Cerdas`**).
* **🔄 HANDOFF ANCHOR:** Menguasai representasi matematis teks, pencarian *BM25/TF-IDF* (fondasi *lexical search* pada *Hybrid RAG* masa depan!), dan klasifikasi teks; menyerahkan arsitektur saraf mendalam ke **`STI-624 Pembelajaran Mendalam & Jaringan Saraf`** serta sistem asisten berbasis LLM/RAG ke **`STA-702 AI Percakapan dan Asisten Cerdas`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS16` (*Artificial Intelligence & Intelligent Systems*) & `BK-IT02` (*Applied AI & Intelligent Technologies*).

**Pustaka Utama:**
1. Jurafsky, D., & Martin, J. H. (2024). *Speech and Language Processing* (3rd ed. draft, Bab 2–6: *Regex, N-Grams, Naive Bayes Sentiment, Vector Semantics & Embeddings*). Stanford University.
2. Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval*. Cambridge University Press. *(Klasik Emas Inverted Index, TF-IDF, BM25, & IR Evaluation)*

**Pustaka Pendukung:**
3. Vajjala, S., Majumder, B., Gupta, A., & Surana, H. (2020). *Practical Natural Language Processing*. O'Reilly Media.
4. Dokumentasi Teknis `NLTK`, `PySastrawi`, `Gensim` (*Word2Vec/FastText*), `rank-bm25`, `spaCy`, & `HuggingFace Transformers Pipeline`.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring: Teori + Praktikum) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi & `Sub-CPMK-1.1` (Bagian I):** Menguraikan tantangan ambiguitas bahasa alami, karakteristik korpus Bahasa Indonesia vs Inggris, & ekstraksi pola **Regular Expressions (Regex)** [C2→C3] | 1.1.1 Ketepatan mengidentifikasi ambiguitas leksikal/sintaksis dan derau teks media sosial/dokumen.<br>1.1.2 Ketepatan menyusun pola **Regex** Python (`re`) untuk membersihkan URL, mention, tagar, email, nomor telepon, dan tanda baca. | **Kriteria:** Ekspresi Regex akurat tanpa merusak kata bermakna.<br>**Teknik:** Pemeriksaan *notebook* praktikum pembersihan teks mentah. | **Kuliah Ringkas** `[TM: 50']`<br>**Praktikum Lab 1:** Penyiapan Ekosistem NLP Python & Pembersihan Korpus dengan **Regular Expressions** `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Kontrak belajar, unduh korpus latihan dwibahasa di LMS Edlink. | Lanskap NLP & IR, Hukum Zipf & Heaps pada Korpus, serta **Regular Expressions** `[1] Bab 2` | — |
| **2** | **`Sub-CPMK-1.1` (Bagian II):** Menerapkan tahapan **Text Preprocessing**: *Tokenization*, *Case Folding & Slang Normalization*, *Stopword Removal*, serta **Stemming vs Lemmatization** [C3] | 1.1.3 Ketepatan menerapkan normalisasi kamus kata tidak baku Bahasa Indonesia, penyaringan *stopwords* kontekstual (hati-hati jangan menghapus kata negasi `"tidak/bukan"` untuk analisis sentimen!), serta membandingkan **Stemming** (`Sastrawi` Nazief-Adriani / Porter) vs **Lemmatization** (`NLTK`/`spaCy`). | **Kriteria:** *Pipeline preprocessing* modular menghasilkan token bersih dan menjaga kata bermuatan makna.<br>**Teknik:** Uji komparasi *over-stemming / under-stemming* di lab. | **Ceramah & Live Demo** `[TM: 50']`<br>**Praktikum Lab 2:** Konstruksi Modul **Text Preprocessing** Bahasa Indonesia (`Sastrawi`) & Inggris (`NLTK`/`spaCy`) `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Kuis perbedaan *Stemming* vs *Lemmatization* di LMS Edlink. | *Tokenization*, Normalisasi Teks Tidak Baku, *Stopword Removal* Kontekstual, **Stemming**, & **Lemmatization** `[1] Bab 2; [3] Bab 2` | — |
| **3** | **`Sub-CPMK-1.2`:** Membangun model representasi teks diskrit: *Bag-of-Words* (BoW), **N-Gram** (*Unigram, Bigram, Trigram*), **TF-IDF**, & kemiripan dokumen **Cosine Similarity** [C3] | 1.2.1 Ketepatan menghitung bobot $\text{TF-IDF}(t,d,D) = \text{tf}(t,d) \times \log\frac{N}{\text{df}(t)}$ secara manual maupun dengan `TfidfVectorizer`.<br>1.2.2 Ketepatan menghitung **Cosine Similarity** pada **Vector Space Model (VSM)** untuk mengukur kemiripan kueri–dokumen. | **Kriteria:** Perhitungan manual matriks TF-IDF & *Cosine Similarity* selaras keluaran program.<br>**Teknik:** Latihan hitung + implementasi pencocokan dokumen di lab. | **Problem-Based Lecture** `[TM: 50']`<br>**Praktikum Lab 3:** Representasi *BoW, N-Gram*, **TF-IDF**, & Matriks Kemiripan **VSM Cosine** `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Rilis resmi spesifikasi & korpus **Tugas 1 (RTM-1)** di LMS Edlink. | Representasi Teks Renggang: *Bag-of-Words*, **N-Gram**, Pembobotan **TF-IDF**, & **Vector Space Model (VSM)** `[1] Bab 3 & 6; [2] Bab 6` | — |
| **4** | **`Sub-CPMK-1.1` & `1.2` (Evaluasi Korpus):** Analisis statistik kosakata korpus (*Zipf's Law, OOV Rate, Sparsity*) & optimalisasi parameter `TfidfVectorizer` (`min_df, max_df, sublinear_tf`) [C3]<br>*(+ Evaluasi Tugas 1 atas `CPMK-1`)* | 1.2.3 Ketepatan memangkas dimensi matriks renggang tanpa kehilangan informasi pembeda menggunakan ambang `min_df` dan `max_df`. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-3`)**.<br>**Teknik:** Pengumpulan *Notebook* Pemrosesan Korpus & VSM/TF-IDF + Verifikasi Kode Lab 20'. | **Review & Verifikasi Tugas 1** `[TM: 50']`<br>**Praktikum Lab 4:** Penalaan Kosakata **TF-IDF** & Verifikasi Langsung **Tugas 1 (`CPMK-1`)** `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Pengumpulan berkas **Tugas 1 (`CPMK-1`)** di LMS Edlink. | Analisis Statistik Korpus, Reduksi Kosakata (`min_df`, `max_df`), & Evaluasi *Pipeline Preprocessing* `[2] Bab 5–6` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-2.1` (Bagian I):** Merancang dan mengimplementasikan struktur data **Inverted Index** (*Dictionary & Posting Lists*) serta pencarian **Boolean Retrieval** (`AND, OR, NOT`) [C4] | 2.1.1 Ketepatan membangun struktur **Inverted Index** dari ribuan dokumen sehingga pencarian kata bekerja dalam waktu sub-linier (tanpa memindai seluruh teks satu per satu!).<br>2.1.2 Ketepatan mengimplementasikan penggabungan dua *sorted posting lists* (`AND/OR`). | **Kriteria:** Indeks terbalik bekerja cepat dan hasil kueri Boolean 100% akurat.<br>**Teknik:** Praktikum membangun struktur *Inverted Index* dari nol di Python. | **Interactive Lecture IR** `[TM: 50']`<br>**Praktikum Lab 5:** Konstruksi Struktur **Inverted Index**, *Positional Index*, & *Boolean Query Engine* `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Kuis penelusuran irisan *Posting Lists* di LMS Edlink. | Arsitektur Mesin Pencari: Pengindeksan Dokumen, **Inverted Index**, *Posting Lists*, & *Boolean Retrieval* `[2] Bab 1–2` | — |
| **6** | **`Sub-CPMK-2.1` (Bagian II):** Menganalisis dan mengimplementasikan algoritma pemeringkatan probabilistik **Okapi BM25** dibanding **TF-IDF Cosine** [C4] | 2.1.3 Ketepatan menganalisis peran parameter saturasi frekuensi kata $k_1$ dan normalisasi panjang dokumen $b$ pada rumus **Okapi BM25**.<br>2.1.4 Ketepatan membandingkan kualitas peringkat dokumen teratas antara VSM TF-IDF dan **BM25**. | **Kriteria:** Mesin pencari **BM25** berhasil mengembalikan daftar dokumen terurut relevan dengan cepat.<br>**Teknik:** Praktikum komparasi peringkat TF-IDF vs BM25 pada korpus berita/jurnal. | **Case-Based Ranking Lecture** `[TM: 50']`<br>**Praktikum Lab 6:** Implementasi & Penalaan Mesin Pencari **Okapi BM25** (`rank_bm25` / kustom) `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Catatan perbandingan peringkat VSM vs BM25 di LMS Edlink. | *Ranked Retrieval*, Kelemahan TF-IDF Murni pada Dokumen Panjang, & Model Probabilistik **Okapi BM25** `[2] Bab 11` | — |
| **7** | **`Sub-CPMK-2.2`:** Mengevaluasi kinerja sistem *Information Retrieval* menggunakan *Ground-Truth Relevance Judgments* (**Precision, Recall, F1, Precision@K, MRR, & MAP**) serta Klinik UTS [C4] | 2.2.1 Ketepatan menghitung **Precision, Recall, F1-Score, Precision@K ($P@5, P@10$), Reciprocal Rank (MRR),** dan **Mean Average Precision (MAP)** atas sekumpulan kueri uji (*qrels*). | **Kriteria:** Perhitungan metrik evaluasi IR 100% akurat & interpretasi kegagalan temu balik tajam.<br>**Teknik:** Praktikum evaluasi kuantitatif mesin pencari + klinik pra-UTS. | **Problem-Solving IR Metrics** `[TM: 50']`<br>**Praktikum Lab 7:** Evaluasi Kuantitatif Sistem IR (**Precision, Recall, F1, P@K, MAP**) & Klinik UTS `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Simulasi ujian praktik pembangunan & evaluasi IR di LMS Edlink. | Evaluasi Sistem *Information Retrieval*: Koleksi Uji Cranfield, **Precision, Recall, F1**, *Precision@K*, **MRR**, & **MAP** `[2] Bab 8` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `CPMK-2` (`Sub-CPMK-2.1` & `Sub-CPMK-2.2`) [C4]** | Keberhasilan membangun sistem temu balik informasi (**Inverted Index, TF-IDF VSM, & Okapi BM25**) atas korpus uji baru di laboratorium serta mengevaluasi kinerjanya secara terukur dengan metrik **Precision, Recall, F1, & P@K/MAP**. | **Kriteria:** **Rubrik Analitik UTS Praktik (`K-3`)**.<br>**Teknik:** Ujian Praktik *Live Coding* Sistem IR Terawasi di Laboratorium. | **Ujian Praktik Sistem Temu Balik Informasi di Lab**<br>`[150 menit]` | Pengarsipan *notebook* ujian & nilai `CPMK-2` pada portal OBE. | Materi **TF-IDF VSM, Inverted Index, Okapi BM25,** & Metrik Evaluasi IR (Pekan 3–7) | **25%**<br>*(UTS — `CPMK-2`)* |
| **9** | **`Sub-CPMK-3.1` (Bagian I):** Mengimplementasikan semantik distribusional & *Word Embedding* padat menggunakan **Word2Vec** (*CBOW vs Skip-Gram*) [C4] | 3.1.1 Ketepatan menjelaskan keterbatasan *one-hot / TF-IDF* (tidak menangkap sinonim `"mobil" ≈ "kendaraan"`) dan hipotesis distribusional.<br>3.1.2 Ketepatan melatih/memuat model **Word2Vec** (`gensim`) serta mengeksplorasi tetangga kata terdekat & analogi vektor. | **Kriteria:** Vektor kata menangkap kedekatan semantik pada korpus domain.<br>**Teknik:** Praktikum pelatihan & visualisasi proyeksi 2D *Word2Vec*. | **Interactive Lecture Embeddings** `[TM: 50']`<br>**Praktikum Lab 8:** Pelatihan & Eksplorasi Semantik **Word2Vec (*CBOW & Skip-Gram*)** dengan `Gensim` `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Unduh panduan *Word Embeddings* di LMS Edlink. | Semantik Distribusional, Representasi Padat (*Dense Embeddings*), & Arsitektur **Word2Vec** (*CBOW, Skip-Gram*) `[1] Bab 6` | — |
| **10** | **`Sub-CPMK-3.1` (Bagian II):** Mengimplementasikan **FastText** (*Subword Character N-Grams* penangkal kata salah ketik/*Out-of-Vocabulary*) & agregasi vektor dokumen [C4] | 3.1.3 Ketepatan membandingkan ketahanan **FastText** vs **Word2Vec** saat menghadapi kata berimbuhan/salah ketik (*typo/OOV*) khas ulasan Bahasa Indonesia.<br>3.1.4 Ketepatan membentuk vektor dokumen (*Mean/TF-IDF Weighted Pooling*) sebagai fitur masukan model ML. | **Kriteria:** Bukti eksperimen menunjukkan *FastText* tetap menghasilkan vektor bermakna pada kata OOV.<br>**Teknik:** Praktikum komparasi Word2Vec vs FastText pada ulasan *e-commerce*. | **Case-Based Subword Lecture** `[TM: 50']`<br>**Praktikum Lab 9:** **FastText** untuk Penanganan *OOV/Typo* & Pembentukan *Document Embeddings* `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Rilis resmi spesifikasi **Tugas 2 (RTM-2)** di LMS Edlink. | *Subword Embeddings* (**FastText**), Penanganan *Out-of-Vocabulary* (OOV), & Strategi *Document Vector Pooling* `[1] Bab 6; [3] Bab 3` | — |
| **11** | **`Sub-CPMK-3.2` (Bagian I):** Mengembangkan model **Klasifikasi Teks & Analisis Sentimen** menggunakan *Multinomial Naive Bayes*, *Logistic Regression*, & *Linear SVM* [C4] | 3.2.1 Ketepatan membangun *pipeline* klasifikasi teks (membandingkan fitur **TF-IDF N-Gram** vs **Word2Vec/FastText Embeddings**) dengan *Laplace Smoothing* pada **Multinomial Naive Bayes** dan **Linear SVM**. | **Kriteria:** *Pipeline* klasifikasi teks bebas kebocoran kosakata uji (*vectorizer fit only on train!*).<br>**Teknik:** Praktikum analisis sentimen 3 kelas (*Positif, Netral, Negatif*) ulasan berbahasa Indonesia. | **Problem-Based Sentiment Lab** `[TM: 50']`<br>**Praktikum Lab 10:** Pengembangan Model **Klasifikasi Teks & Analisis Sentimen** (*MNB & Linear SVM*) `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Kuis *Laplace Smoothing* & *Pipeline* Teks di LMS Edlink. | Klasifikasi Teks: **Multinomial Naive Bayes**, **Linear SVM** untuk Dimensi Tinggi, & Analisis Sentimen `[1] Bab 4; [3] Bab 4` | — |
| **12** | **`Sub-CPMK-3.2` (Bagian II):** Optimasi **Macro/Weighted F1-Score** & analisis kegagalan linguistik (*sarkasme, negasi ganda, kata kunci domain*) pada klasifikasi teks [C4]<br>*(+ Evaluasi Tugas 2 atas `CPMK-3`)* | 3.2.2 Ketepatan menala fitur N-Gram (mis. *bigram* `"tidak puas"` vs *unigram* `"puas"`), parameter model, dan menganalisis *Confusion Matrix* per kelas hingga mencapai **F1-Score** optimal. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-3`)**.<br>**Teknik:** Demo & Bedah Eksperimen Klasifikasi Teks/Sentimen (**Tugas 2**) di Laboratorium. | **Error Analysis & Uji Tugas 2** `[TM: 50']`<br>**Praktikum Lab 11:** Analisis Kesalahan Linguistik, Optimasi **F1-Score**, & Verifikasi **Tugas 2** `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Pengumpulan berkas **Tugas 2 (`CPMK-3`)** di LMS Edlink. | Penanganan Negasi dengan *Bigram*, Evaluasi **Macro-F1**, & *Linguistic Error Analysis* `[1] Bab 4` | **25%**<br>*(Tugas 2 — `CPMK-3`)* |
| **13** | **`Sub-CPMK-4.1`:** Mengekstraksi struktur informasi teks (*POS Tagging, Named Entity Recognition / NER, & Keyword Extraction*) menggunakan **`spaCy` / `NLTK`** [C4→C5] | 4.1.1 Ketepatan menggunakan *pipeline* **`spaCy`** untuk mengenali entitas bernama (*Person, Organization, Location, Date*) dan pola aturan `EntityRuler` untuk ekstraksi informasi dokumen. | **Kriteria:** Ekstraksi entitas dan kata kunci memperkaya fungsionalitas pencarian/analisis dokumen.<br>**Teknik:** Praktikum ekstraksi entitas otomatis dari korpus berita/dokumen organisasi. | **Interactive Lecture Information Extraction** `[TM: 50']`<br>**Praktikum Lab 12:** *POS Tagging*, **Named Entity Recognition (NER)**, & *EntityRuler* dengan **`spaCy`** `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Spesifikasi proyek purwarupa akhir UAS dirilis di LMS Edlink. | *Sequence Labeling* Praktis: *Part-of-Speech (POS) Tagging*, **Named Entity Recognition (NER)**, & Ekstraksi Kata Kunci dengan `spaCy` `[3] Bab 5` | — |
| **14** | **`Sub-CPMK-4.1` & `4.2`:** Mengintegrasikan *Pretrained Embeddings / Inference Pipeline* dari **HuggingFace** untuk pencarian semantik ringan (*Lexical BM25 + Semantic Reranking*) atau analisis teks cerdas [C5] | 4.2.1 Ketepatan mengintegrasikan API/pustaka `HuggingFace` (*pretrained sentence-transformers / sentiment / zero-shot pipeline* tingkat pemakaian aplikasi — **tanpa melatih arsitektur Transformer dari nol** sesuai pagar `STI-624`/`STA-702`!). | **Kriteria:** Integrasi model/pustaka modern berjalan efisien (dengan *caching* pemuatan model) di perangkat lokal.<br>**Teknik:** Praktikum membangun prototipe *Hybrid Lexical-Semantic Search* / *Smart Document Analyzer*. | **Case-Based Modern NLP Integration** `[TM: 50']`<br>**Praktikum Lab 13:** Integrasi Pustaka **`HuggingFace` / `spaCy`** untuk *Semantic Search / Text Intelligence* `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Contoh kode pemuatan `st.cache_resource` untuk model NLP ringan di LMS Edlink. | Integrasi Praktis Pustaka/API NLP Modern (`spaCy`, `HuggingFace Pipeline`), Pencarian Hibrida (*BM25 + Semantic Similarity*), & Efisiensi Memori `[3]; [4]` | — |
| **15** | **`Sub-CPMK-4.1` & `4.2` (Sintesis Purwarupa):** Merampungkan dan menguji kelayakan pengguna atas **Purwarupa Aplikasi NLP / Mesin Pencari Cerdas** serta Klinik Pra-UAS [C5] | 4.2.2 Ketepatan menyatukan alur *preprocessing*, mesin indeks/model NLP, dan antarmuka pengguna interaktif (`Streamlit` / Web UI) lengkap metrik relevansi/akurasi yang terukur. | **Kriteria:** Purwarupa responsif, relevan menjawab kueri uji nyata, dan bebas *crash*.<br>**Teknik:** Uji coba silang kueri jebakan antar-kelompok & klinik pra-UAS di lab. | **Prototype Review & Klinik UAS** `[TM: 50']`<br>**Praktikum Lab 14:** Uji Kelayakan **Purwarupa Aplikasi NLP / Mesin Pencari Cerdas** & Persiapan Sidang UAS `[Prak: 170']`<br>`[PT: 60']` · `[BM: 60']` | Pengumpulan draf repositori & laporan evaluasi proyek UAS di LMS Edlink. | Arsitektur Aplikasi Pencarian/NLP End-to-End, Pengujian Kueri Pengguna, & *Handoff* menuju `STI-624` dan `STA-702` `[3]; [4]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-4` (`Sub-CPMK-4.1` & `Sub-CPMK-4.2`) [C5]** | Kualitas perancangan, ketepatan integrasi pustaka/API NLP modern (`spaCy`/`NLTK`/`HuggingFace`), serta bukti kinerja terukur dari **Purwarupa Aplikasi NLP atau Mesin Pencari Cerdas** sebagai solusi kebutuhan pengguna. | **Kriteria:** **Rubrik Analitik UAS (`K-3`)**.<br>**Teknik:** Penilaian Repositori, Laporan Evaluasi Kualitas Solusi, & Demo Purwarupa (50% UAS) + Sidang Pengujian Kueri Langsung & Verifikasi Individu (50% UAS). | **Sidang *Showcase* Purwarupa Mesin Pencari / Aplikasi NLP & Uji Kueri Langsung**<br>`[150 menit]` | Pengarsipan repositori proyek, laporan evaluasi, & rekap nilai `CPL-06` dan `CPL-09` pada portal OBE. | Integrasi Komprehensif Pemrosesan Teks, *Information Retrieval*, Klasifikasi/NER, & Pustaka NLP Modern | **30%**<br>*(UAS — `CPMK-4`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `CPMK-1` / `CPL-06` [C3])
* **Bentuk Instrumen:** Proyek Individu **Text Preprocessing & TF-IDF Vector Space Pipeline** pada Korpus Berderau Bahasa Indonesia/Inggris + Verifikasi Kode Lab: mahasiswa membersihkan minimal 2.000 dokumen/ulasan mentah menggunakan Regex, normalisasi kata tidak baku, *stopword removal* selektif, dan *stemming/lemmatization*, lalu membangun representasi **TF-IDF & Vector Space Model** lengkap analisis perbandingan kosakata sebelum vs sesudah pembersihan.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan tahapan *tokenisasi, normalisasi, stopword,* & *stemming/lemmatisasi* (`Sub-CPMK-1.1`) = **45%**; (2) Ketepatan konstruksi matriks **VSM & TF-IDF** serta kemiripan kosinus (`Sub-CPMK-1.2`) = **35%**; (3) Analisis pengurangan derau kosakata & verifikasi lab = **20%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 25% · Mengukur `CPMK-2` / `CPL-06` [C4])
* **Bentuk Instrumen:** **Ujian Praktik *Live Coding* Sistem Temu Balik Informasi di Laboratorium** (150 menit, individu): diberikan korpus ratusan artikel beserta himpunan kueri uji dan label relevansi (*ground-truth qrels*), mahasiswa mengimplementasikan **Inverted Index**, membandingkan hasil pencarian **TF-IDF VSM** vs **Okapi BM25**, serta menghitung metrik **Precision, Recall, F1-Score, Precision@5,** dan **MAP**.
* **Bobot Kriteria Rubrik (`K-3`):** (1) Kebenaran struktur **Inverted Index** & pencarian dasar = **30%**; (2) Ketepatan implementasi pemeringkatan **TF-IDF VSM & Okapi BM25** (`Sub-CPMK-2.1`) = **35%**; (3) Akurasi perhitungan evaluasi **Precision, Recall, F1, & MAP** (`Sub-CPMK-2.2`) = **35%**.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 25% · Mengukur `CPMK-3` / `CPL-09` [C4])
* **Bentuk Instrumen:** Proyek Analitik **Klasifikasi Teks & Analisis Sentimen Berbasis Word Embedding** (diverifikasi di lab): mahasiswa melatih representasi **Word2Vec & FastText**, membandingkannya dengan fitur **TF-IDF N-Gram** menggunakan pengklasifikasi *Multinomial Naive Bayes* dan *Linear SVM*, mengoptimalkan **Macro F1-Score**, serta menyajikan bedah kesalahan linguistik (*negasi, sarkasme, OOV*).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Ketepatan implementasi & analisis **Word2Vec / FastText** (`Sub-CPMK-3.1`) = **35%**; (2) Ketepatan pemodelan klasifikasi/sentimen bebas *vocabulary leakage* & capaian **F1-Score** (`Sub-CPMK-3.2`) = **40%**; (3) Ketajaman analisis kesalahan linguistik & verifikasi kode = **25%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-4` / `CPL-09` [C5])
* **Bentuk Instrumen:** **Proyek Akhir Purwarupa Aplikasi NLP atau Mesin Pencari Cerdas** (50% nilai UAS: aplikasi fungsional yang mengintegrasikan teknik IR/klasifikasi semester ini dengan pustaka modern `spaCy`/`NLTK`/`HuggingFace` untuk memecahkan masalah pencarian pengetahuan kampus/analisis umpan balik publik lengkap evaluasi kuantitatif) + **Sidang Uji Kueri Langsung & Verifikasi Individu** (50% nilai UAS, 150 menit).
* **Bobot Kriteria Rubrik (`K-3`):** (1) Kualitas arsitektur rancangan solusi NLP/mesin pencari (`Sub-CPMK-4.1`) = **30%**; (2) Ketepatan & keandalan integrasi pustaka/API NLP modern (`spaCy`/`NLTK`/`HuggingFace` — `Sub-CPMK-4.2`) = **35%**; (3) Bukti evaluasi kuantitatif ketepatan solusi pada kueri/teks uji nyata = **20%**; (4) Penguasaan teknis individu saat sidang langsung = **15%**.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Sistem Cerdas & Sains Data**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Istiadi, S.T., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
