# 068_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-414 — PENGANTAR NLP & TEMU BALIK INFORMASI (*Introduction to NLP & Information Retrieval*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI414` · **Bobot:** 2 SKS `+P` (`TM 50'`, `Prak 170'`, `PT 60'`, `BM 60'`) · **Semester:** 4  
**Prasyarat:** `STI-307` Sistem Cerdas · **CPL:** `CPL-06` (`P2` = 45%) & `CPL-09` (`KK1` = 55%) [Level `R`]  
**Klaster Rubrik:** `K-3` · **Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu & Asisten Laboratorium `STI-414` |
|---|---|
| **Struktur Waktu per Sesi** | **Sesi Teori Padat (`50'`):** Pendahuluan `10'` · Inti Formulasi Linguistik/IR `30'` · Penutup `10'`<br>**Sesi Praktikum Lab (`170'`):** *Briefing* Korpus `15'` · Eksperimen Koding NLP/IR Terbimbing `135'` · Inspeksi Hasil & *Git Commit* `20'`, diikuti `PT 60'` & `BM 60'`. |
| **Fokus Keilmuan (*In-Scope*)** | Pemrosesan awal teks dwibahasa, **TF-IDF & Vector Space Model**, **Inverted Index & Okapi BM25**, metrik evaluasi IR (*Precision, Recall, F1, MAP*), *Word Embedding* (**Word2Vec, FastText**), klasifikasi teks/sentimen, serta purwarupa cerdas berbasis `NLTK`/`spaCy`/`HuggingFace`. |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** melatih arsitektur *Transformer Self-Attention* dari nol (ranah **`STI-624 Pembelajaran Mendalam & Jaringan Saraf`**) dan dilarang membahas *fine-tuning* LLM maupun *Enterprise RAG* penuh (ranah **`STA-702 AI Percakapan dan Asisten Cerdas`**). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti Teori (`50'`) & Modul Praktikum (`170'`) | Waktu Total | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Teori: Ambiguitas Bahasa & Hukum Zipf · Lab 1: Ekstraksi & Pembersihan **Regex** | 220' | Formatif Lab |
| **2** | `Sub-CPMK-1.1` | Teori: Tokenisasi, *Stopword*, **Stemming vs Lemmatization** · Lab 2: `Sastrawi` & `NLTK` | 220' | Formatif Lab |
| **3** | `Sub-CPMK-1.2` | Teori: *BoW, N-Gram*, **TF-IDF**, & **VSM Cosine** · Lab 3: Matriks Kemiripan Dokumen | 220' | Formatif Lab |
| **4** | `Sub-CPMK-1.1, 1.2` | Teori: Statistik Kosakata & Pemangkasan Dimensi · Lab 4: Verifikasi **Tugas 1** | 220' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-2.1` | Teori: Arsitektur **Inverted Index** & Boolean IR · Lab 5: Pembangunan *Posting Lists* | 220' | Formatif Lab |
| **6** | `Sub-CPMK-2.1` | Teori: Pemeringkatan Probabilistik **Okapi BM25** · Lab 6: Mesin Pencari BM25 vs TF-IDF | 220' | Formatif Lab |
| **7** | `Sub-CPMK-2.2` | Teori: Metrik Evaluasi IR (**Precision, Recall, F1, MAP**) · Lab 7: Uji *Qrels* & Klinik UTS | 220' | Formatif Lab |
| **8** | `CPMK-2` | **Ujian Tengah Semester (UTS):** *Live Coding* Sistem IR (*Inverted Index, BM25, Evaluasi*) | 150' | **UTS (25%)** |
| **9** | `Sub-CPMK-3.1` | Teori: Semantik Distribusional & **Word2Vec** · Lab 8: *CBOW / Skip-Gram* `Gensim` | 220' | Formatif Lab |
| **10** | `Sub-CPMK-3.1` | Teori: *Subword* **FastText** & Vektor Dokumen · Lab 9: Ketahanan *Typo/OOV* Bahasa Indonesia | 220' | Formatif Lab |
| **11** | `Sub-CPMK-3.2` | Teori: Klasifikasi Teks (*MNB & Linear SVM*) · Lab 10: Pipeline Analisis Sentimen | 220' | Formatif Lab |
| **12** | `Sub-CPMK-3.2` | Teori: Penanganan Negasi & Optimasi **F1-Score** · Lab 11: Bedah Galat & Uji **Tugas 2** | 220' | **Tugas 2 (25%)** |
| **13** | `Sub-CPMK-4.1` | Teori: *POS Tagging* & **Named Entity Recognition (NER)** · Lab 12: Ekstraksi Entitas `spaCy` | 220' | Formatif Lab |
| **14** | `Sub-CPMK-4.1, 4.2` | Teori: Integrasi Praktis Pustaka **HuggingFace** · Lab 13: *Hybrid Search* / *Smart NLP API* | 220' | Formatif Lab |
| **15** | `Sub-CPMK-4.1, 4.2` | Teori: Rekayasa Purwarupa Pencarian/NLP Pengguna · Lab 14: Uji Kelayakan & Klinik UAS | 220' | Formatif Lab |
| **16** | `CPMK-4` | **Evaluasi Akhir Semester (UAS):** Sidang Purwarupa NLP/Mesin Pencari & Uji Kueri Langsung | 150' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN (TEORI + PRAKTIKUM)

### PERTEMUAN 1 — Ambiguitas Bahasa Alami, Hukum Zipf, & Pembersihan **Regular Expressions**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C2→C3] · **Alat:** Python `re`, JupyterLab, Korpus Ulasan & Berita Indonesia.
* **Sesi Teori (`50'`):** Memperkenalkan tantangan unik teks bahasa manusia (polisemi, sarkasme, singkatan media sosial `"yg, gk, bgt, mantul"`) dan pola distribusi kata **Hukum Zipf**.
* **Sesi Praktikum Lab 1 (`170'`):** Menulis fungsi ekstraksi dan pembersihan pola **Regex** untuk menanggalkan tag HTML, URL, nomor identitas, emoji/simbol berlebih sambil tetap menjaga keutuhan angka/istilah penting.
* **PT (`60'`) & BM (`60'`):** Menyusun 8 aturan Regex pembersih korpus ulasan aplikasi lokal.

### PERTEMUAN 2 — **Text Preprocessing**: Tokenisasi, Normalisasi, *Stopwords*, & **Stemming vs Lemmatization**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Alat:** `NLTK`, `PySastrawi`, `spaCy`.
* **Sesi Teori (`50'`):** Membandingkan pemotongan imbuhan algoritmik (**Stemming** — algoritma Nazief-Adriani untuk afiksasi kompleks `me-...-kan` Bahasa Indonesia) dengan pengembalian lema kamus morfologis (**Lemmatization**), serta peringatan keras agar tidak menghapus kata negasi (`tidak, belum, jangan`) saat melakukan *stopword removal* untuk analisis sentimen!
* **Sesi Praktikum Lab 2 (`170'`):** Membangun modul `TextPreprocessor` terkonfigurasi untuk Bahasa Indonesia (`Sastrawi` + kamus normalisasi *slang*) dan Bahasa Inggris (`NLTK`/`spaCy`).
* **PT (`60'`) & BM (`60'`):** Mengukur kecepatan dan akurasi *stemming* pada 1.000 kalimat Bahasa Indonesia.

### PERTEMUAN 3 — Representasi **Vector Space Model (VSM)**, *N-Gram*, **TF-IDF**, & *Cosine Similarity*
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] · **Alat:** `CountVectorizer`, `TfidfVectorizer`, `cosine_similarity`.
* **Sesi Teori (`50'`):** Menguraikan transformasi dokumen teks menjadi vektor numerik berdimensi kosakata $|V|$: kelemahan *Bag-of-Words* mentah, penangkapan frasa urutan lokal dengan **N-Gram**, rumus bobot **TF-IDF**, dan pengukuran sudut kemiripan **Cosine Similarity** ($\cos\theta = \frac{\mathbf{q}\cdot\mathbf{d}}{\|\mathbf{q}\|\|\mathbf{d}\|}$). Merilis resmi **Tugas 1 (RTM-1)**.
* **Sesi Praktikum Lab 3 (`170'`):** Menghitung contoh kecil TF-IDF secara manual di kertas/spreadsheet lalu membuktikan kesamaannya dengan implementasi Python untuk mencari dokumen paling mirip terhadap sebuah kueri.
* **PT (`60'`) & BM (`60'`):** Mengerjakan *pipeline* pemrosesan korpus dan representasi TF-IDF pada **Tugas 1**.

### PERTEMUAN 4 — Analisis Statistik Kosakata, Pemangkasan Dimensi, & Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.1` & `1.2` [C3] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Alat:** `scikit-learn` & `matplotlib`.
* **Sesi Teori (`50'`):** Membahas efek pemangkasan kata langka/salah ketik (`min_df`) dan kata terlalu umum korpus (`max_df`), skala logaritmik `sublinear_tf=True`, serta penghematan memori matriks renggang (*CSR Sparse Matrix*).
* **Sesi Praktikum Lab 4 (`170'`):** Verifikasi langsung kode dan tanya-jawab 20 menit atas pengumpulan **Tugas 1 (`CPMK-1`)**, dilanjutkan eksperimen penyusutan ukuran kosakata hingga 70% tanpa menurunkan akurasi kemiripan.
* **PT (`60'`) & BM (`60'`):** Membaca konsep struktur data *Inverted Index* Manning Bab 1.

### PERTEMUAN 5 — Arsitektur Mesin Pencari: **Inverted Index** & *Boolean Retrieval*
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Alat:** Python struktur kamus & daftar terurut (*Posting Lists*).
* **Sesi Teori (`50'`):** Mengapa pencarian `LIKE '%kata%'` pada jutaan dokumen sangat lambat? Membedah arsitektur inti seluruh mesin pencari modern: **Inverted Index** (*Term Vocabulary* $\rightarrow$ *Sorted Posting List of DocIDs + Term Frequencies*) dan algoritma *linear merge* $O(x+y)$ untuk irisan kueri Boolean.
* **Sesi Praktikum Lab 5 (`170'`):** Mengimplementasikan kelas `InvertedIndex` dari nol di Python, mengindeks 3.000 dokumen dalam hitungan detik, dan membandingkan kecepatan kueri terindeks vs pemindaian linier.
* **PT (`60'`) & BM (`60'`):** Menambahkan pencatatan frekuensi kemunculan istilah per dokumen pada *posting list*.

### PERTEMUAN 6 — Pemeringkatan Probabilistik **Okapi BM25** vs **TF-IDF VSM**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Alat:** Implementasi kustom BM25 & pustaka `rank-bm25`.
* **Sesi Teori (`50'`):** Membongkar kelemahan TF-IDF linier (dokumen yang mengulang kata `"pajak"` 20 kali dianggap 20× lebih relevan daripada yang menyebut 2 kali!) dan bagaimana rumus standar emas industri **Okapi BM25** menyelesaikannya melalui saturasi frekuensi non-linier ($k_1 \approx 1,2\text{–}2,0$) dan normalisasi panjang dokumen ($b \approx 0,75$).
* **Sesi Praktikum Lab 6 (`170'`):** Membangun mesin pencari **BM25** di atas *Inverted Index*, menguji variasi nilai $k_1$ dan $b$, serta membandingkan 10 hasil teratasnya dengan TF-IDF VSM.
* **PT (`60'`) & BM (`60'`):** Menganalisis kasus kueri di mana BM25 mengungguli TF-IDF secara mencolok.

### PERTEMUAN 7 — Evaluasi Kuantitatif Sistem IR (**Precision, Recall, F1, P@K, MRR, & MAP**) + Klinik UTS
* **Sub-CPMK:** `Sub-CPMK-2.2` [C4] · **Alat:** Koleksi Uji IR berlabel relevansi (*Query Relevance Judgments / Qrels*).
* **Sesi Teori (`50'`):** Mengajarkan cara mengukur kualitas mesin pencari secara objektif: perbedaan evaluasi tak-berurut (**Precision, Recall, F1**) dan evaluasi peka urutan peringkat (**Precision@K**, **Mean Reciprocal Rank [MRR]**, serta **Mean Average Precision [MAP]**).
* **Sesi Praktikum Lab 7 (`170'`):** Menulis modul evaluator IR otomatis, membandingkan skor MAP antara variasi *preprocessing* (pakai *stemming* vs tanpa *stemming*) dan algoritma (TF-IDF vs BM25), serta simulasi ujian praktik **UTS Pekan 8**.
* **PT (`60'`) & BM (`60'`):** Persiapan mandiri menghadapi ujian praktik sistem IR pada UTS.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** **`CPMK-2`** (`Sub-CPMK-2.1` & `Sub-CPMK-2.2` [C4]) · **Bobot:** **25%** · **Durasi:** `150 menit` (*Live Coding* di Lab).
* **Pelaksanaan:** Mahasiswa membangun secara mandiri mesin pencari berbasis **Inverted Index**, **TF-IDF VSM**, dan **Okapi BM25** atas korpus baru yang diberikan saat ujian, lalu menghitung serta menganalisis metrik **Precision, Recall, F1, P@5,** dan **MAP** terhadap kueri uji.

### PERTEMUAN 9 — Semantik Distribusional & Representasi Padat **Word2Vec** (*CBOW & Skip-Gram*)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Alat:** `gensim.models.Word2Vec`, `PCA/t-SNE` plot.
* **Sesi Teori (`50'`):** Membahas hasil UTS lalu membuka babak semantik padat: *"You shall know a word by the company it keeps"* (Firth) — bagaimana jendela geser konteks pada **Word2Vec** (*Continuous Bag-of-Words* menebak kata tengah dari konteks vs *Skip-Gram* menebak konteks dari kata tengah) menghasilkan vektor padat $\mathbb{R}^{100\text{–}300}$ yang menempatkan sinonim berdekatan di ruang vektor.
* **Sesi Praktikum Lab 8 (`170'`):** Melatih model **Word2Vec** pada korpus puluhan ribu kalimat, menguji `.wv.most_similar()`, dan memvisualisasikan pengelompokan kata semantik di bidang 2D.
* **PT (`60'`) & BM (`60'`):** Membandingkan hasil tetangga kata pada variasi ukuran jendela konteks `window=2` vs `window=8`.

### PERTEMUAN 10 — *Subword Embeddings* (**FastText**) & Agregasi Vektor Dokumen
* **Sub-CPMK:** `Sub-CPMK-3.1` [C4] · **Alat:** `gensim.models.FastText`.
* **Sesi Teori (`50'`):** Apa kelemahan terbesar Word2Vec pada teks ulasan konsumen Indonesia yang penuh variasi ketikan seperti `"pengirimannya"`, `"pengirimanx"`, `"kirimnya"`? Menguraikan bagaimana **FastText** merepresentasikan setiap kata sebagai jumlah *character n-grams* (`<pe, pen, eng, ...>`) sehingga sanggup menghasilkan vektor akurat bahkan untuk kata *Out-of-Vocabulary* (OOV), dilanjutkan teknik *Mean Pooling* & *TF-IDF Weighted Pooling* untuk membentuk vektor kalimat/dokumen. Merilis resmi **Tugas 2 (RTM-2)**.
* **Sesi Praktikum Lab 9 (`170'`):** Membuktikan eksperimen ketahanan **FastText** terhadap kata *typo*/berimbuhan baru yang membuat Word2Vec gagal (`KeyError`), serta mengekstrak matriks fitur dokumen untuk klasifikasi.
* **PT (`60'`) & BM (`60'`):** Melatih *word embeddings* domain pada korpus **Tugas 2**.

### PERTEMUAN 11 — Pengembangan Model **Klasifikasi Teks & Analisis Sentimen** (*Naive Bayes & SVM*)
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] · **Alat:** `MultinomialNB`, `ComplementNB`, `LinearSVC`, `LogisticRegression`.
* **Sesi Teori (`50'`):** Menguraikan formulasi probabilistik **Multinomial Naive Bayes** dengan *Laplace Add-1 Smoothing* (sebagai *baseline* super cepat) dan mengapa **Linear SVM / Regularized Logistic Regression** sangat tangguh pada ruang teks berdimensi puluhan ribu fitur.
* **Sesi Praktikum Lab 10 (`170'`):** Membangun eksperimen komparatif klasifikasi topik dan analisis sentimen yang mengadu fitur **TF-IDF (1,2)-gram** melawan fitur **Word2Vec / FastText Embeddings** secara adil bebas *leakage*.
* **PT (`60'`) & BM (`60'`):** Menjalankan penalaan hiperparameter untuk mendongkrak *Macro F1-Score* pada **Tugas 2**.

### PERTEMUAN 12 — Analisis Kesalahan Linguistik, Optimasi **F1-Score**, & Evaluasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-3.2` [C4] + **Evaluasi Sumatif Tugas 2 (`CPMK-3`, 25%)** · **Alat:** `classification_report`, Inspeksi Dokumen Salah Prediksi.
* **Sesi Teori (`50'`):** Mengajarkan cara melakukan *Linguistic Error Analysis* pada kalimat yang salah diklasifikasikan model: jebakan kalimat kontras (`"Barangnya bagus sih, TAPI pengirimannya parah banget"`), sarkasme, dan kata kunci ambigu lintas domain.
* **Sesi Praktikum Lab 11 (`170'`):** Demonstrasi, verifikasi kode, dan tanya-jawab **Tugas 2 (`CPMK-3`)** di laboratorium, dilanjutkan pembagian kelompok proyek akhir purwarupa UAS.
* **PT (`60'`) & BM (`60'`):** Menyusun proposal ringkas 1 halaman skenario pengguna untuk purwarupa aplikasi NLP/IR UAS.

### PERTEMUAN 13 — Ekstraksi Informasi Praktis (*POS Tagging & Named Entity Recognition*) dengan **`spaCy`**
* **Sub-CPMK:** `Sub-CPMK-4.1` [C4→C5] · **Alat:** `spaCy`, `displaCy`, `EntityRuler`.
* **Sesi Teori (`50'`):** Mengajarkan bagaimana mengubah teks bebas menjadi metadata terstruktur menggunakan pelabelan kelas kata (**POS Tagging**) dan pengenalan entitas bernama (**NER**: tokoh, institusi, lokasi, nominal, tanggal) untuk memperkaya filter faset (*faceted search*) pada mesin pencari cerdas.
* **Sesi Praktikum Lab 12 (`170'`):** Membangun modul ekstraksi entitas otomatis menggunakan `spaCy` + aturan pola domain (`EntityRuler`) dan memvisualisasikannya dengan `displaCy`.
* **PT (`60'`) & BM (`60'`):** Mengintegrasikan fitur penandaan entitas/ekstraksi kata kunci ke rancangan purwarupa tim.

### PERTEMUAN 14 — Integrasi Pustaka/API **HuggingFace** untuk Pencarian Semantik & Solusi NLP Modern
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C5] · **Alat:** `transformers.pipeline`, `sentence-transformers` (model ringan siap pakai CPU).
* **Sesi Teori (`50'`):** Menunjukkan bagaimana rekayasawan sistem informasi mengintegrasikan ekosistem model *pretrained* modern (**HuggingFace Hub** / model multibahasa ringan) pada tingkat aplikasi — khususnya menggabungkan ketepatan kata kunci eksak **BM25** dengan kemiripan makna *Sentence Embeddings* (**Hybrid Search**), sambil menegaskan pagar kurikulum bahwa arsitektur internal *Transformer* akan dibedah di `STI-624` dan orkestrasi LLM/RAG penuh di `STA-702`.
* **Sesi Praktikum Lab 13 (`170'`):** Mengintegrasikan *pipeline* NLP modern atau *Semantic Reranker* ringan ke dalam *backend* fungsi pencarian/analisis proyek akhir tim dengan *caching* memori yang rapi.
* **PT (`60'`) & BM (`60'`):** Menyelesaikan pembangunan antarmuka pengguna interaktif purwarupa proyek UAS.

### PERTEMUAN 15 — Uji Kelayakan Purwarupa Aplikasi NLP / Mesin Pencari Cerdas & Klinik Pra-UAS
* **Sub-CPMK:** `Sub-CPMK-4.1` & `4.2` [C5] · **Alat:** Aplikasi Purwarupa (`Streamlit` / Web App), Set Kueri Pengujian.
* **Sesi Teori (`50'`):** Membahas standar evaluasi akhir sebuah purwarupa produk NLP/IR: relevansi jawaban (*P@5 / F1*), latensi respons per kueri ($< 1\text{–}2\text{ detik}$), kejelasan tampilan sorotan bukti teks (*snippet highlighting*), dan penanganan kueri kosong/asing.
* **Sesi Praktikum Lab 14 (`170'`):** *Cross-Team Query Testing & Coaching Clinic*: setiap tim menguji 10 kueri nyata (termasuk kueri sinonim & salah ketik) pada aplikasi tim rekan, mencatat skor relevansi, dan memoles purwarupa sebelum sidang UAS.
* **PT (`60'`) & BM (`60'`):** Finalisasi repositori Git dan laporan evaluasi purwarupa siap diuji pada Pekan 16.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-4`** (`Sub-CPMK-4.1` & `Sub-CPMK-4.2` [C5]) · **Bobot:** **30%** · **Durasi:** `150 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Repositori, Laporan Evaluasi Kuantitatif, & Purwarupa Aplikasi NLP / Mesin Pencari Cerdas (50% nilai UAS)** dengan **Sidang Pengujian Kueri Langsung & Verifikasi Teknis Individu (50% nilai UAS)** di laboratorium.
