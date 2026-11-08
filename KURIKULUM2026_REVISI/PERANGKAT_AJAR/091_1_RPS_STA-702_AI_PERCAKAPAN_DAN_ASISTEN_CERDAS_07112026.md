# 091_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STA-702 — AI Percakapan dan Asisten Cerdas

**Identitas:** `STA-702` AI Percakapan dan Asisten Cerdas · Semester 7 · 3 SKS (+P) · Prasyarat `STI-413`, `STI-416` · PL PL-1 · PEO PEO-1, PEO-2 · IRM M.

## Identitas dan pengesahan

Prodi S1 SISTEKIN FSTI UWG. Koordinator, dosen dan tanggal pengesahan diisi oleh program studi. Beban mingguan: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit. PT = tugas terstruktur; BM = belajar mandiri.

## CPL dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| CPL-09 (KK1) | Mampu menganalisis, merancang, dan mengembangkan sistem informasi cerdas terintegrasi kecerdasan artifisial (AI/ML, NLP, Computer Vision, Smart Sys, DSS) guna memecahkan masalah kompleks organisasi dan industri. | M |
| CPL-06 (P2) | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital. | M |

## CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD Dok 043 | Bloom | CPL |
| --- | --- | --- | --- |
| CPMK-1 | Mahasiswa (*A*) mampu **menerapkan** teknik Prompt Engineering tingkat lanjut (Few-Shot, Chain-of-Thought, ReAct) (*B*) menggunakan framework LangChain (*C*) dengan output terstruktur (*D*). | C3 | `CPL-09` (`KK1`) |
| CPMK-2 | Mahasiswa (*A*) mampu **merancang dan mengoptimalkan** sistem RAG multi-dokumen (*B*) menggunakan teknik Contextual Compression dan Reranking (*C*) dengan skor evaluasi RAGAS yang tinggi (*D*). | C6 | `CPL-06` (`P2`), `CPL-09` (`KK1`) |
| CPMK-3 | Mahasiswa (*A*) mampu **melakukan** Fine-Tuning model LLM open-source (*B*) menggunakan teknik Parameter-Efficient Fine-Tuning (QLoRA) (*C*) pada domain khusus (*D*). | C4 | `CPL-09` (`KK1`) |
| CPMK-4 | Mahasiswa (*A*) mampu **membangun** asisten virtual cerdas berbasis agen otonom (Tool Calling) (*B*) dengan integrasi multi-channel (WhatsApp API / Web Widget) (*C*) secara terpadu (*D*). | C6 | `CPL-09` (`KK1`) |

| Sub-CPMK | Kompetensi Dok 043 | CPMK sumber | Bloom |
| --- | --- | --- | --- |
| Sub-CPMK-1.1 | Menerapkan fine-tuning model LLM/Transformer untuk kebutuhan spesifik. | CPMK-1 | C3 |
| Sub-CPMK-1.2 | Menyusun prompt engineering yang efektif untuk tugas percakapan. | CPMK-1 | C3 |
| Sub-CPMK-2.1 | Membangun sistem RAG menggunakan LangChain dan vector database. | CPMK-2 | C6 |
| Sub-CPMK-2.2 | Mengimplementasikan agentic AI dengan tool-use dan pemanggilan fungsi. | CPMK-2 | C6 |
| Sub-CPMK-3.1 | Mengevaluasi kualitas respons percakapan asisten AI. | CPMK-3 | C4 |
| Sub-CPMK-3.2 | Mengintegrasikan asisten percakapan ke saluran layanan pengguna. | CPMK-3 | C4 |
| Sub-CPMK-4.1 | Membangun intelligent assistant end-to-end yang andal. | CPMK-4 | C6 |
| Sub-CPMK-4.2 | Menyempurnakan perilaku asisten berdasarkan evaluasi pengguna. | CPMK-4 | C6 |

## Matriks CPL–CPMK dan bobot asesmen

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-09` (`KK1`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-06` (`P2`), `CPL-09` (`KK1`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-09` (`KK1`) | — | — | 25% | — | 25% |
| CPMK-4 | `CPL-09` (`KK1`) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Bobot merupakan rancangan penilaian MK; CPMK yang mendukung lebih dari satu CPL tidak menggandakan nilai akhir. Nilai CPL tingkat prodi mengikuti formula Dok 008.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana 16 pertemuan

| Mg | Kemampuan | Materi | Metode | Beban | Asesmen |
| --- | --- | --- | --- | --- | --- |
| 1 | Mampu menguraikan evolusi Chatbot dari Rule-Based ke Large Language Models (C2) | Pengantar Conversational AI, Arsitektur Transformer, Foundation Models | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 2 | Mampu menerapkan Prompt Engineering: Zero-Shot, Few-Shot, Chain-of-Thought (C3) | Prompt Engineering Patterns: CoT, Step-Back, Self-Consistency Prompting | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 3 | Mampu membangun rantai pemrosesan teks via LangChain Core (C3) | LangChain Fundamentals: PromptTemplates, OutputParsers, LCEL Syntax | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 4 | Mampu mengonfigurasi memori percakapan (ConversationBufferMemory) (C3) | Memory & State Management: Buffer Memory, Summary Memory, Entity Memory | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 20% |
| 5 | Mampu membangun sistem RAG dasar dengan Vector Store Chroma / Pinecone (C4) | RAG Fundamentals: Text Splitting, Vector Ingestion, Vector Retriever | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 6 | Mampu mengoptimalkan retrieval via Multi-Query & Contextual Compression (C4) | Advanced RAG: Multi-Query Retriever, Ensemble, Contextual Compressor | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 7 | Mampu menerapkan Reranking (Cohere Rerank) dan evaluasi via RAGAS (C5) | RAG Evaluation: RAGAS Metrics (Faithfulness, Answer Relevance, Context Recall) | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 8 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Advanced RAG Pipeline & Prompt Engineering | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS 25% |
| 9 | Mampu menguraikan metode Parameter-Efficient Fine-Tuning (PEFT & LoRA) (C2) | LLM Fine-Tuning Concepts: Full Fine-Tuning vs LoRA, QLoRA 4-bit Precision | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 10 | Mampu menyiapkan dataset instruksi kustom dalam format Alpaca/ChatML (C3) | Dataset Preparation: Instruction Tuning Format, Data Filtering & Tokenization | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 11 | Mampu mengeksekusi pelatihan QLoRA pada model LLM open-source (Llama/Mistral) (C4) | Training Execution: HuggingFace TRL (SFTTrainer), BitsAndBytes, PEFT | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 12 | Mengevaluasi hasil fine-tuning QLoRA pada data berizin (C4) | Evaluasi QLoRA, log pelatihan, baseline dan batas perangkat | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 25% |
| 13 | Mampu menerapkan Guardrails untuk pencegahan halusinasi & prompt injection (C4) | AI Safety & Guardrails: NeMo Guardrails, Llama Guard, Content Moderation | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 14 | Mampu mengintegrasikan chatbot cerdas ke WhatsApp Business API & Web (C4) | Multi-Channel Integration: Webhook WhatsApp Business, Telegram, Web UI | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 15 | Mampu mendeploy asisten cerdas enterprise terpadu pada cloud server (C6) | PjBL Conversational AI Studio: Deployment Asisten Cerdas Terpadu | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 16 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Asisten Virtual Cerdas Conversational AI | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS 30% |

## Ringkasan asesmen

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Rancang dan uji prompt terstruktur untuk kumpulan pertanyaan berizin. Bukti: prompt, kasus uji dan analisis jawaban |
| UTS | 8 | 25% | CPMK-2 | Bangun RAG multi-dokumen dengan retrieval, reranking dan evaluasi. Bukti: kode, corpus berizin, sitasi dan metrik retrieval |
| Tugas 2 | 12 | 25% | CPMK-3 | Lakukan QLoRA pada model kecil atau simulasi jika perangkat terbatas dan evaluasi hasilnya. Bukti: konfigurasi, log latihan atau rencana simulasi dan evaluasi |
| UAS | 16 | 30% | CPMK-4 | Integrasikan tool calling dan kanal uji, uji kesalahan serta batas keamanan. Bukti: kode, demo, pengujian dan kartu sistem |

## Pustaka utama dan pendukung

Dokumentasi [Hugging Face PEFT](https://huggingface.co/docs/peft/) dan [LangChain](https://python.langchain.com/docs/).

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS16` *Artificial Intelligence*, `BK-IT02` *Applied AI*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur LLM Modern, Prompt Engineering Lanjut (Few-shot, CoT), Arsitektur RAG (Chunking, Vector Database Chroma/Milvus), Framework LangChain/LlamaIndex, Fine-tuning Efisien (LoRA/QLoRA).
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang mengulang rumus TF-IDF dasar, algoritma Naive Bayes teks klasik, pembuatan scraper web berita umum.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Membangun sistem asisten cerdas berbasis model bahasa besar tingkat korporat.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Jika GPU tidak tersedia, praktik QLoRA dapat berupa demonstrasi terbatas atau rencana teruji; keterbatasannya harus dinyatakan. Dok 043 menempatkan fine-tuning pada Sub-CPMK-1.1 meskipun rumusan CPMK-3 menilai fine-tuning; dan tool-use pada Sub-CPMK-2.2 meskipun rumusan CPMK-4 membahas agen. Bukti dinilai berdasarkan rumusan CPMK.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
