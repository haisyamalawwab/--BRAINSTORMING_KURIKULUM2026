# 061_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-307 — SISTEM CERDAS (*Intelligent Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI307` · **Bobot:** 2 SKS Teori · **Semester:** 3  
**CPL:** `CPL-06` (`P2` = 50%) & `CPL-09` (`KK1` = 50%) [Level `R`] · **BoK:** `BK-IS16`, `BK-IT02`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Sistem Cerdas Berbasis Pengetahuan: Algoritma Pencarian Heuristik, Sistem Pakar, dan Sistem Inferensi Logika Fuzzy dengan Python `scikit-fuzzy`* |
| **Target Tebal Naskah** | 14 Bab Materi Inti + 2 Unit Evaluasi ($\pm 160\text{–}190\text{ halaman}$ A4/B5 dilengkapi diagram penelusuran pohon pencarian, tabel jejak mesin inferensi, grafik kurva *fuzzy*, dan skrip lengkap `scikit-fuzzy`) |
| **Pagar Pembatas Isi Buku (*Guardrail*)** | Fokus murni pada **White-Box Symbolic & Fuzzy Reasoning**; bebas dari materi *Machine Learning* statistik (`STI-413 Pembelajaran Mesin`), *Deep Learning / Neural Networks* (`STI-624 Pembelajaran Mendalam & Jaringan Saraf`), NLP (`STI-414`), *Multi-Agent* (`STA-602`), dan *AHP/TOPSIS* (`STA-501`). |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP PEKAN, CPMK, & SUB-CPMK

| Bagian | Bab | Judul Bab Modul Pembelajaran | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Agen Rasional & Pencarian Ruang Status** | **Bab 1** | Paradigma AI Simbolik, Agen Cerdas Rasional, & Spesifikasi Lingkungan **PEAS** | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Formulasi Ruang Status & Pencarian Tanpa Informasi (*BFS, DFS, Uniform-Cost*) | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3** | Pencarian Heuristik Terinformasi: *Greedy Best-First Search* & Algoritma **A\*** | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 4** | Pencarian Kompetitif Bercabang: Algoritma **Minimax** & **Alpha-Beta Pruning** | Mg 4 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Representasi Pengetahuan & Sistem Pakar** | **Bab 5** | Arsitektur Sistem Pakar & Representasi Pengetahuan (*Semantic Net, Frame, Rules*) | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (30%) |
| | **Bab 6** | Mesin Inferensi Berbasis Aturan: **Forward Chaining** vs **Backward Chaining** | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1, 2.2` | UTS (30%) |
| | **Bab 7** | Penalaran Ketidakpastian pada Sistem Pakar dengan **Certainty Factor (CF)** | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Paket Latihan Penelusuran A\*, Minimax, & Sistem Pakar (Persiapan UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (30%)* |
| **Bagian III:<br>Logika Fuzzy & Komputasi `scikit-fuzzy`** | **Bab 8** | Fondasi Himpunan Kabur (*Fuzzy Sets*), Variabel Linguistik, & Operator Zadeh | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 9** | Tahap **Fuzzifikasi**: Perancangan Kurva Segitiga, Trapesium, Bahu, & *Gaussian* | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 10** | Mesin Inferensi *Fuzzy* Metode **Mamdani** (*Max-Min Composition* & *Centroid*) | Mg 11 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (20%) |
| | **Bab 11** | Mesin Inferensi *Fuzzy* Metode **Takagi-Sugeno** & Analisis Komparatif FIS | Mg 12 | `CPMK-3` | `Sub-CPMK-3.2` | **Tugas 2 (Mg 12)** |
| | **Bab 12** | Pemrograman Sistem Inferensi *Fuzzy* Menggunakan Python **`scikit-fuzzy`** | Mg 13 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | UAS (30%) |
| **Bagian IV:<br>Integrasi & Validasi Sistem Cerdas** | **Bab 13** | Arsitektur Hibrid *Rule-Fuzzy Decision System* & Analisis Sensitivitas Kurva | Mg 14 | `CPMK-2, 3` | `Sub-CPMK-2.2, 3.2` | UAS (30%) |
| | **Bab 14** | Pengujian Skenario Batas (*Edge-Case Audit*) & Peta *Handoff* Menuju `STI-413` | Mg 15 | `CPMK-1..3` | `1.1–3.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Paket Simulasi Komprehensif FIS & Verifikasi `scikit-fuzzy` (Persiapan UAS)* | *Mg 16* | *`CPMK-3`* | *`3.1–3.2` & Sintesis* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB

#### BAB 1: Paradigma AI Simbolik, Agen Cerdas Rasional, & Spesifikasi Lingkungan PEAS (Pekan 1)
* **Sub-Pokok Bahasan:** (1.1) Dua Mazhab Besar AI: Penalaran Simbolik (*Knowledge-Driven*) vs Pembelajaran Statistik (*Data-Driven*); (1.2) Konsep Agen Rasional dan Pemetaan **PEAS**; (1.3) Enam Karakteristik Lingkungan Tugas; (1.4) Kapan Bisnis Wajib Memakai Sistem Berbasis Aturan/*Fuzzy* yang Transparan (*Explainable*).

#### BAB 2: Formulasi Ruang Status & Pencarian Tanpa Informasi (*BFS, DFS, Uniform-Cost*) (Pekan 2)
* **Sub-Pokok Bahasan:** (2.1) Abstraksi Masalah Dunia Nyata ke Graf Ruang Status; (2.2) Struktur Pohon Pencarian vs Graf (`OPEN` & `CLOSED` *lists*); (2.3) Penelusuran & Kompleksitas *Breadth-First Search* (BFS), *Depth-First Search* (DFS), dan *Uniform-Cost Search* (UCS).

#### BAB 3: Pencarian Heuristik Terinformasi: *Greedy Best-First Search* & Algoritma A\* (Pekan 3)
* **Sub-Pokok Bahasan:** (3.1) Konstruksi Fungsi Heuristik $h(n)$ (Jarak *Manhattan*, *Euclidean*, & Relaksasi Masalah); (3.2) *Greedy Best-First Search* dan Kelemahan Jebakan Lokal; (3.3) Algoritma **A\*** ($f(n)=g(n)+h(n)$); (3.4) Pembuktian Sifat *Admissible* dan *Consistent Heuristic* untuk Jaminan Optimalitas.

#### BAB 4: Pencarian Kompetitif Bercabang: Algoritma Minimax & Alpha-Beta Pruning (Pekan 4)
* **Sub-Pokok Bahasan:** (4.1) Permainan Dua Agen *Zero-Sum* dan Fungsi Evaluasi Utilitas; (4.2) Algoritma **Minimax** pada Pohon Keputusan Bercabang; (4.3) Mekanisme Pemangkasan **Alpha-Beta Pruning** ($\alpha \ge \beta$) Langkah demi Langkah; (4.4) Pengaruh Pengurutan Langkah (*Move Ordering*) terhadap Efisiensi Ruang/Waktu.

#### BAB 5: Arsitektur Sistem Pakar & Representasi Pengetahuan (*Semantic Net, Frame, Rules*) (Pekan 5)
* **Sub-Pokok Bahasan:** (5.1) Anatomi Sistem Pakar (*Knowledge Base, Working Memory, Inference Engine, Explanation Facility*); (5.2) Jaringan Semantik (*Semantic Networks*) & Bingkai (*Frames*); (5.3) Kaidah Produksi `IF–THEN` dan Akuisisi Pengetahuan Pakar; (5.4) Deteksi Anomali Basis Aturan (Aturan Kontradiktif, Redundan, & Siklus Melingkar).

#### BAB 6: Mesin Inferensi Berbasis Aturan: Forward Chaining vs Backward Chaining (Pekan 6)
* **Sub-Pokok Bahasan:** (6.1) Siklus Eksekusi **Forward Chaining** (*Match – Conflict Resolution – Act*); (6.2) Strategi Resolusi Konflik (*Specificity, Rule Priority, Recency, Refractoriness*); (6.3) Algoritma Rekursif Sub-Tujuan **Backward Chaining**; (6.4) Pedoman Arsitektural Memilih *Forward* vs *Backward Chaining* pada Kasus Bisnis.

#### BAB 7: Penalaran Ketidakpastian pada Sistem Pakar dengan Certainty Factor (CF) (Pekan 7)
* **Sub-Pokok Bahasan:** (7.1) Sumber Ketidakpastian pada Fakta Pengguna dan Aturan Pakar; (7.2) Ukuran Kepercayaan ($MB$) dan Ketidakpercayaan ($MD$) Shortliffe-Buchanan; (7.3) Propagasi $CF$ pada Aturan Tunggal dan Premis Majemuk (`AND`/`OR`); (7.4) Rumus Kombinasi Bukti Paralel $CF_{\text{combine}}$ untuk Tanda Sama maupun Berlawanan.

#### BAB 8: Fondasi Himpunan Kabur (*Fuzzy Sets*), Variabel Linguistik, & Operator Zadeh (Pekan 9)
* **Sub-Pokok Bahasan:** (8.1) Kelemahan Ambang Batas Tegas (*Crisp Threshold*) pada Pengambilan Keputusan; (8.2) Definisi Himpunan *Fuzzy*, Semesta Pembicaraan, *Support, Core,* & *Crossover Point*; (8.3) Variabel Linguistik & Nilai Linguistik; (8.4) Operator Standar Zadeh (*Intersection* $\min$, *Union* $\max$, *Complement* $1-\mu$).

#### BAB 9: Tahap Fuzzifikasi: Perancangan Kurva Segitiga, Trapesium, Bahu, & Gaussian (Pekan 10)
* **Sub-Pokok Bahasan:** (9.1) Prinsip Partisi Semesta Pembicaraan yang Saling Tumpang-Tindih (*Overlapping*); (9.2) Rumus Sepotong-Sepotong Kurva Linear Naik/Turun, Segitiga (*Triangular*), dan Trapesium (*Trapezoidal*); (9.3) Kurva Bahu (*Shoulder*) untuk Batas Ekstrem Kiri/Kanan serta Kurva *Gaussian* & *Sigmoid*; (9.4) Contoh Perhitungan *Fuzzifikasi* Multi-Variabel.

#### BAB 10: Mesin Inferensi Fuzzy Metode Mamdani (*Max-Min Composition* & *Centroid*) (Pekan 11)
* **Sub-Pokok Bahasan:** (10.1) Penyusunan Matriks Aturan *Fuzzy* (*Fuzzy Associative Memory* / FAM); (10.2) Evaluasi Anteseden ($\alpha\text{-predikat}$) & Fungsi Implikasi `Min` (*Clipping*); (10.3) Komposisi Agregasi Antar-Aturan `Max`; (10.4) Lima Metode Defuzzifikasi pada Mamdani dengan Fokus Perhitungan Analitis & Diskrit **Centroid (COA)**.

#### BAB 11: Mesin Inferensi Fuzzy Metode Takagi-Sugeno & Analisis Komparatif FIS (Pekan 12)
* **Sub-Pokok Bahasan:** (11.1) Struktur Aturan **Sugeno Orde-Nol** (*Singleton Consequent*) dan **Sugeno Orde-Satu** (Fungsi Linier Input); (11.2) Perhitungan Defuzzifikasi Rata-Rata Terbobot (*Weighted Average*); (11.3) Studi Kasus Komparatif: Perbandingan Akurasi, Kehalusan Permukaan Kontrol, dan Kecepatan Komputasi Mamdani vs Sugeno.

#### BAB 12: Pemrograman Sistem Inferensi Fuzzy Menggunakan Python `scikit-fuzzy` (Pekan 13)
* **Sub-Pokok Bahasan:** (12.1) Arsitektur Modul `skfuzzy` dan `skfuzzy.control`; (12.2) Mendefinisikan `Antecedent`, `Consequent`, dan Semesta `np.arange`; (12.3) Merakit Basis Aturan `ctrl.Rule` dan Menjalankan `ControlSystemSimulation`; (12.4) Visualisasi Grafik Fungsi Keanggotaan, Area Defuzzifikasi, dan *3D Control Surface* beserta Rekonsiliasi dengan Hitungan Kertas.

#### BAB 13: Arsitektur Hibrid *Rule-Fuzzy Decision System* & Analisis Sensitivitas Kurva (Pekan 14)
* **Sub-Pokok Bahasan:** (13.1) Pola Integrasi Dua Tahap: *Hard-Rule Eligibility Screening* (`CPMK-2`) + *Fuzzy Gradual Scoring* (`CPMK-3`); (13.2) Implementasi Sistem Hibrid di Python Murni + `scikit-fuzzy`; (13.3) Analisis Sensitivitas Pergeseran Parameter Kurva dan Pencegahan Lubang Aturan (*Rule-Base Completeness Check*).

#### BAB 14: Pengujian Skenario Batas (*Edge-Case Audit*) & Peta Handoff Menuju `STI-413` (Pekan 15)
* **Sub-Pokok Bahasan:** (14.1) Protokol Pengujian Kebenaran & *Reproducibility* Sistem Cerdas Berbasis Aturan/Fuzzy; (14.2) Studi Kasus End-to-End: Sistem Penilaian Risiko Rantai Pasok & Rekomendasi Stok Cerdas; (14.3) Batas Paradigma Simbolik dan Jembatan *Handoff* Menuju `STI-413 Pembelajaran Mesin`, `STI-414 Pengantar NLP & Temu Balik Informasi`, `STA-501 Sistem Pendukung Keputusan`, serta `STA-602 Sistem Agen Cerdas`.
