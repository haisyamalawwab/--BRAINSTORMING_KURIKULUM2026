# 068_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-414 — PENGANTAR NLP & TEMU BALIK INFORMASI (*Introduction to NLP & Information Retrieval*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI414` · **Bobot:** 2 SKS (`T=1, P=1`) · **Semester:** 4  
**Klaster Asesmen MK (Dok 018):** Klaster 3 (`K-3`) — Kecerdasan Artifisial, Cloud & Cybersecurity  
**CPL Dibebankan:** `CPL-06` (`P2` = **45%**) & `CPL-09` (`KK1` = **55%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 008, 018,** dan **043**, mata kuliah `STI-414 Pengantar NLP & Temu Balik Informasi` (2 SKS `+P`) menerapkan skema bobot baku Klaster `K-3` (`20% / 25% / 25% / 30%`) dengan pemetaan 1-ke-1 ke keempat CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1` (`CPL-06` / `P2`)** — *Case-Based Corpus Text Preprocessing & VSM/TF-IDF Representation*.
* **UTS (Pekan 8 — 25%) → `CPMK-2` (`CPL-06` / `P2`)** — *Live Lab Exam: Inverted Index, BM25 Retrieval Engine, & Precision/Recall/MAP Evaluation*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3` (`CPL-09` / `KK1`)** — *Case-Based Text Classification & Sentiment Analysis with Word2Vec/FastText*.
* **UAS (Pekan 16 — 30%) → `CPMK-4` (`CPL-09` / `KK1`)** — *Project-Based Smart Search Engine / NLP Application Prototype (spaCy/NLTK/HuggingFace) & Live Query Defense*.
* **Kepatuhan IKU 7 ($\ge 55\%$ Klaster `K-3` Dok 018):** `Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) = 75%` berbasis studi kasus korpus nyata dan proyek purwarupa cerdas.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-06`**<br>(`P2` — 45%)<br>*Level: R* | **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus korpus berderau: Penerapan akurat *tokenisasi, normalisasi, stopword,* & *stemming/lemmatisasi* | **RTM-1 (Tugas 1)** + Verifikasi Kode Lab + Rubrik T1 | Sumatif | 11% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Studi kasus korpus: Konstruksi representasi **Vector Space Model (VSM)** & **TF-IDF** | **RTM-1 (Tugas 1)** + Uji Kemiripan Dokumen + Rubrik T1 | Sumatif | 9% | |
| **`CPL-06`**<br>(`P2` — 45%)<br>*Level: R* | **`CPMK-2`**<br>(C4) | `Sub-CPMK-2.1` | Mg 8 | Ujian praktik lab 150': Implementasi **Inverted Index** & pemeringkatan **Okapi BM25 / VSM** | **Soal Praktik UTS** (Bagian Konstruksi IR) + Rubrik UTS | Sumatif | 13% | **25%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Ujian praktik lab 150': Evaluasi kuantitatif sistem IR dengan **Precision, Recall, F1,** & **MAP** | **Soal Praktik UTS** (Bagian Evaluasi IR) + Rubrik UTS | Sumatif | 12% | |
| **`CPL-09`**<br>(`KK1` — 55%)<br>*Level: R* | **`CPMK-3`**<br>(C4) | `Sub-CPMK-3.1` | Mg 12 | Proyek analitik teks: Implementasi *word embedding* (**Word2Vec & FastText**) pada korpus domain | **RTM-2 (Tugas 2)** Bagian Embedding + Rubrik Analitik T2 | Sumatif | 11% | **25%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Proyek analitik teks: Pengembangan model klasifikasi teks & analisis sentimen (*NB, SVM*) ber-**F1** optimal | **RTM-2 (Tugas 2)** Bagian Klasifikasi + Demo Lab + Rubrik T2 | Sumatif | 14% | |
| **`CPL-09`**<br>(`KK1` — 55%)<br>*Level: R* | **`CPMK-4`**<br>(C5) | `Sub-CPMK-4.1` | Mg 16 | Proyek purwarupa + sidang: Perancangan arsitektur aplikasi NLP / mesin pencari cerdas | **Repositori & Laporan Proyek UAS** + Rubrik Analitik UAS | Sumatif | 14% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | Proyek purwarupa + uji kueri langsung: Integrasi pustaka/API NLP modern (`spaCy`/`NLTK`/`HuggingFace`) | **Demo Purwarupa & Sidang Individu UAS** + Rubrik UAS | Sumatif | 16% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/25/25/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN PRAKTIK

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Pemrosesan Awal Korpus & Representasi VSM/TF-IDF)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Verifikasi Lab **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-06`).
* **Spesifikasi Pengerjaan Individu:**
  1. Diberikan korpus $\ge 2.000$ teks ulasan/berita mentah berbahasa Indonesia (mengandung HTML, URL, singkatan *slang*, dan imbuhan kompleks); mahasiswa membangun modul `TextPreprocessor` lengkap *tokenisasi, normalisasi, stopword removal* selektif, dan *stemming* (`Sastrawi`) / *lemmatisasi*.
  2. Membangun matriks **TF-IDF & Vector Space Model**, menampilkan penyusutan ukuran kosakata sebelum vs sesudah *preprocessing*, dan menguji pencarian kemiripan kosinus 5 kueri contoh.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Konstruksi & Evaluasi Sistem Temu Balik Informasi)
* **Format & Bobot:** Ujian Praktik *Live Coding* di Laboratorium (**150 menit**, individu) · Bobot **25%** (`CPMK-2` → `CPL-06`).
* **Spesifikasi Soal Praktik:**
  1. Diberikan korpus ratusan dokumen akademik/berita beserta 15 kueri uji dan berkas penilaian relevansi (*qrels*); mahasiswa wajib membangun **Inverted Index**, mengimplementasikan pencarian berperingkat **TF-IDF VSM** dan **Okapi BM25**, serta membandingkan hasil keduanya.
  2. Menghitung secara terprogram metrik **Precision, Recall, F1-Score, Precision@5,** dan **Mean Average Precision (MAP)** serta menuliskan analisis singkat kueri mana yang gagal dan mengapa.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Klasifikasi Teks & Analisis Sentimen Berbasis Word Embedding)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Demo Lab **Pekan 12** · Bobot **25%** (`CPMK-3` → `CPL-09`).
* **Spesifikasi Teknis:**
  1. Melatih representasi **Word2Vec** dan **FastText** pada korpus ulasan/tiket layanan ($\ge 3.000$ dokumen berlabel) serta mendemonstrasikan keunggulan *FastText* pada kata *typo/OOV*.
  2. Mengembangkan dan membandingkan model klasifikasi teks/sentimen (*Multinomial Naive Bayes* & *Linear SVM / Logistic Regression*) antara fitur **TF-IDF N-Gram** vs **Word2Vec/FastText Embeddings** (100% bebas kebocoran kosakata uji!), mengoptimalkan **Macro F1-Score**, dan menyajikan bedah 10 kalimat yang salah terklasifikasi.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Purwarupa Aplikasi NLP / Mesin Pencari Cerdas)
* **Format & Bobot:** Bobot **30%** (`CPMK-4` → `CPL-09`), memadukan **Proyek Purwarupa Tim (50% nilai UAS)** + **Sidang Uji Kueri Langsung & Verifikasi Individu (50% nilai UAS, 150 menit)**:
  1. Membangun aplikasi fungsional (mis. *Mesin Pencari Cerdas Skripsi/Regulasi Kampus dengan Hybrid BM25 + Semantic Reranking & Filter NER*, atau *Dashboard Analisis Sentimen & Ekstraksi Entitas Keluhan Publik*) yang mengintegrasikan teknik IR/klasifikasi semester ini dengan pustaka/API NLP modern (`spaCy`, `NLTK`, dan/atau `HuggingFace`).
  2. Menyajikan bukti evaluasi terukur (*P@5 / MAP* atau *F1-Score* pada set uji) dan berhasil menjawab pengujian kueri spontan dari dosen penguji saat sidang.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-414}}$)
$$NA_{\text{STI-414}} = 0,20\,S_{\text{Tugas 1}} + 0,25\,S_{\text{UTS}} + 0,25\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004 & 008)
1. **Ketercapaian `CPL-06` (`P2` — bobot 45% MK dari `CPMK-1` [20%] + `CPMK-2` [25%]):**
   $$\text{Score}_{\text{CPL-06, STI-414}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,25\,S_{\text{UTS}}(i)}{0,45}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 2 \times 0,45 = 0,90\text{ SKS}$).*
2. **Ketercapaian `CPL-09` (`KK1` — bobot 55% MK dari `CPMK-3` [25%] + `CPMK-4` [30%]):**
   $$\text{Score}_{\text{CPL-09, STI-414}}(i) = \frac{0,25\,S_{\text{Tugas 2}}(i) + 0,30\,S_{\text{UAS}}(i)}{0,55}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 2 \times 0,55 = 1,10\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**; remedial diberikan maksimal 1 kali bagi mahasiswa dengan skor CPMK $< 65,0$ dengan nilai plafon pasca-remedial **70,0 (B)**.
