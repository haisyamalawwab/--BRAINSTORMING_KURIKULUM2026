# 068_3 — OUTLINE BUKU MODUL PEMBELAJARAN & PRAKTIKUM BERBASIS OBE
## STI-414 — PENGANTAR NLP & TEMU BALIK INFORMASI (*Introduction to NLP & Information Retrieval*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI414` · **Bobot:** 2 SKS (`T=1, P=1`) · **Semester:** 4  
**CPL:** `CPL-06` (`P2` = 45%) & `CPL-09` (`KK1` = 55%) [Level `R`] · **BoK:** `BK-IS16`, `BK-IT02`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR + PRAKTIKUM

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Pemrosesan Bahasa Alami & Sistem Temu Balik Informasi Praktis: Preprocessing Korpus Indonesia, Inverted Index, Okapi BM25, Word Embeddings, hingga Purwarupa Pencarian Cerdas* |
| **Target Tebal Naskah** | 14 Bab Materi Ringkas-Tajam + 14 Modul Praktikum Laboratorium + 2 Unit Evaluasi ($\pm 185\text{–}215\text{ halaman}$ A4 selaras bobot 2 SKS `+P`) |
| **Pagar Pembatas Buku (*Guardrail*)** | Fokus pada representasi matematis teks, pencarian IR klasik/hibrida, klasifikasi teks, dan integrasi pustaka NLP siap pakai; tidak melatih *Transformer* dari nol (`STI-624`) dan tidak membahas *fine-tuning* LLM/RAG enterprise (`STA-702`). |

---

## 2. PETA KESELARASAN 14 BAB & 14 MODUL PRAKTIKUM TERHADAP CPMK & SUB-CPMK

| Bagian | Bab & Lab | Judul Bab Materi & Modul Praktikum | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Text Preprocessing & Vector Space Model** | **Bab 1 / Lab 1** | Tantangan Bahasa Alami, Hukum Zipf, & Ekstraksi Pola **Regular Expressions** | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2 / Lab 2** | **Text Preprocessing** Dwibahasa: Tokenisasi, Normalisasi, *Stopword*, & *Stemming/Lemmatization* | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3 / Lab 3** | Representasi *Bag-of-Words*, **N-Gram**, Pembobotan **TF-IDF**, & **Vector Space Model** | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | Tugas 1 (20%) |
| | **Bab 4 / Lab 4** | Analisis Statistik Korpus, Reduksi Dimensi Kosakata, & Optimasi Matriks Renggang | Mg 4 | `CPMK-1` | `Sub-CPMK-1.1, 1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Sistem Temu Balik Informasi (IR)** | **Bab 5 / Lab 5** | Arsitektur Pengindeksan Mesin Pencari: **Inverted Index** & *Boolean Retrieval* | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 6 / Lab 6** | Model Pemeringkatan Probabilistik **Okapi BM25** & Perbandingan dengan VSM | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 7 / Lab 7** | Metodologi Evaluasi Kinerja IR: **Precision, Recall, F1, Precision@K, MRR, & MAP** | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Simulasi Ujian Praktik Konstruksi & Evaluasi Mesin Pencari BM25 (UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (25%)* |
| **Bagian III:<br>Word Embeddings & Klasifikasi Teks** | **Bab 8 / Lab 8** | Semantik Distribusional & Representasi Vektor Padat **Word2Vec (*CBOW & Skip-Gram*)** | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 9 / Lab 9** | *Subword Embeddings* **FastText** Penangkal *Typo/OOV* & Pembentukan Vektor Dokumen | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 10 / Lab 10** | Pengembangan Model **Klasifikasi Teks & Analisis Sentimen** (*Naive Bayes & SVM*) | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (25%) |
| | **Bab 11 / Lab 11** | Penanganan Negasi, Optimasi **F1-Score**, & *Linguistic Error Analysis* | Mg 12 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Integrasi Pustaka Modern & Purwarupa** | **Bab 12 / Lab 12** | Ekstraksi Informasi Praktis (*POS Tagging & Named Entity Recognition*) dengan **`spaCy`** | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13 / Lab 13** | Integrasi Pustaka/API **HuggingFace** untuk Pencarian Hibrida & Analisis Teks Cerdas | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 14 / Lab 14** | Rekayasa **Purwarupa Aplikasi NLP / Mesin Pencari Cerdas** & *Handoff* ke `STI-624`/`STA-702` | Mg 15 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Purwarupa Pencarian/NLP & Protokol Pengujian Kueri Langsung (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB & MODUL PRAKTIKUM

#### BAB 1 & LAB 1: Tantangan Bahasa Alami, Hukum Zipf, & Ekstraksi Pola Regular Expressions (Pekan 1)
* **Materi & Praktikum:**Tingkatan analisis linguistik, karakteristik morfologi aglutinatif Bahasa Indonesia, distribusi frekuensi kata Zipf, serta operasi pencocokan & substitusi **Regex** Python.

#### BAB 2 & LAB 2: Text Preprocessing Dwibahasa (Pekan 2)
* **Materi & Praktikum:** *Word/Sentence Tokenization*, normalisasi leksikon *slang*, penyaringan *stopwords* ramah sentimen, algoritma *stemming* Nazief-Adriani (`Sastrawi`) vs Porter, dan *lemmatization* (`NLTK`/`spaCy`).

#### BAB 3 & LAB 3: Representasi *Bag-of-Words*, N-Gram, Pembobotan TF-IDF, & Vector Space Model (Pekan 3)
* **Materi & Praktikum:** Matriks istilah-dokumen, tangkapan urutan lokal **N-Gram**, formulasi varian **TF-IDF**, serta pemeringkatan kemiripan sudut **Cosine Similarity** pada **VSM**.

#### BAB 4 & LAB 4: Analisis Statistik Korpus, Reduksi Dimensi Kosakata, & Matriks Renggang (Pekan 4)
* **Materi & Praktikum:** Pengaturan `min_df`, `max_df`, `max_features`, `sublinear_tf`, dan efisiensi memori struktur matriks renggang SciPy CSR.

#### BAB 5 & LAB 5: Arsitektur Pengindeksan Mesin Pencari: Inverted Index & *Boolean Retrieval* (Pekan 5)
* **Materi & Praktikum:** Tahapan konstruksi kamus istilah dan *sorted posting lists*, algoritma penggabungan daftar terurut, serta *Positional Index* untuk pencarian frasa eksak.

#### BAB 6 & LAB 6: Model Pemeringkatan Probabilistik Okapi BM25 (Pekan 6)
* **Materi & Praktikum:** Penurunan intuitif skor **BM25**, saturasi non-linier $k_1$, normalisasi panjang dokumen $b$, dan eksperimen komparatif terhadap TF-IDF VSM.

#### BAB 7 & LAB 7: Metodologi Evaluasi Kinerja IR: Precision, Recall, F1, Precision@K, MRR, & MAP (Pekan 7)
* **Materi & Praktikum:** Penyusunan *test collection* & *relevance judgments*, kurva *Interpolated Precision–Recall*, perhitungan **P@K, F1, MRR,** dan **MAP**.

#### BAB 8 & LAB 8: Semantik Distribusional & Representasi Vektor Padat Word2Vec (Pekan 9)
* **Materi & Praktikum:** Perbandingan vektor renggang vs vektor padat berdimensi rendah, arsitektur **CBOW** dan **Skip-Gram** dengan *Negative Sampling*, serta eksplorasi kemiripan semantik di `Gensim`.

#### BAB 9 & LAB 9: *Subword Embeddings* FastText & Pembentukan Vektor Dokumen (Pekan 10)
* **Materi & Praktikum:** Dekomposisi kata menjadi *character n-grams* pada **FastText**, ketangguhan terhadap *typo* dan kata berimbuhan baru (*OOV*), serta agregasi *Mean / TF-IDF Weighted Pooling*.

#### BAB 10 & LAB 10: Pengembangan Model Klasifikasi Teks & Analisis Sentimen (Pekan 11)
* **Materi & Praktikum:** Teorema Bayes & *Laplace Smoothing* pada **Multinomial Naive Bayes**, **Linear SVM** pada dimensi teks, serta perancangan *pipeline* klasifikasi bebas kebocoran kosakata.

#### BAB 11 & LAB 11: Penanganan Negasi, Optimasi F1-Score, & *Linguistic Error Analysis* (Pekan 12)
* **Materi & Praktikum:** Rekayasa fitur negasi & *bigram*, penanganan ketidakseimbangan kelas sentimen dengan **Macro-F1**, dan bedah kasus salah klasifikasi.

#### BAB 12 & LAB 12: Ekstraksi Informasi Praktis (*POS Tagging & NER*) dengan `spaCy` (Pekan 13)
* **Materi & Praktikum:** Pelabelan kelas kata, ekstraksi otomatis tokoh/organisasi/lokasi/tanggal (**NER**), penambahan pola khusus domain dengan `EntityRuler`, dan ekstraksi kata kunci dokumen.

#### BAB 13 & LAB 13: Integrasi Pustaka/API HuggingFace untuk Pencarian Hibrida & Solusi NLP (Pekan 14)
* **Materi & Praktikum:** Pemanggilan efisien *pretrained NLP pipelines* dan *sentence embeddings* ringan untuk menggabungkan **BM25 Lexical Search + Semantic Reranking** (*Hybrid Search*).

#### BAB 14 & LAB 14: Rekayasa Purwarupa Aplikasi NLP / Mesin Pencari Cerdas & *Handoff* (Pekan 15)
* **Materi & Praktikum:** Pembangunan antarmuka pencarian/analisis teks interaktif lengkap sorotan cuplikan relevan (*snippet highlighting*), pengujian kualitas pengguna, serta jembatan menuju `STI-624` dan `STA-702`.
