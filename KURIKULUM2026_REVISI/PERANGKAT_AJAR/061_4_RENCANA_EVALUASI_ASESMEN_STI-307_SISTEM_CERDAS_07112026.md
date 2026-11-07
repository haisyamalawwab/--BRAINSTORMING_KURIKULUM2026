# 061_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-307 — SISTEM CERDAS (*Intelligent Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI307` · **Bobot:** 2 SKS Teori · **Semester:** 3  
**Klaster Asesmen MK (Dok 018):** Klaster 3 (`K-3`) — Kecerdasan Artifisial, Cloud & Cybersecurity  
**CPL Dibebankan:** `CPL-06` (`P2` = **50%**) & `CPL-09` (`KK1` = **50%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK ATAS 3 CPMK & KEPATUHAN IKU 7

Sesuai **Dokumen 043 & 007**, `STI-307 Sistem Cerdas` (2 SKS Teori) memiliki **3 CPMK** dan **6 Sub-CPMK** yang dievaluasi melalui 4 titik asesmen baku MK Teori (`20% / 30% / 20% / 30%`):
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1`** (`CPL-06` = 20%) — Pencarian Heuristik *Greedy, A\*,* & *Minimax Alpha-Beta*.
* **UTS (Pekan 8 — 30%) → `CPMK-2`** (`CPL-06` = 15% + `CPL-09` = 15%) — Sistem Pakar *Forward/Backward Chaining* & *Certainty Factor*.
* **Tugas 2 (Pekan 12 — 20%) → `CPMK-3`** (`CPL-09` = 20%) — Perhitungan Analitis Komparatif *Fuzzy Mamdani* vs *Sugeno*.
* **UAS (Pekan 16 — 30%) → Implementasi `CPMK-3` (`scikit-fuzzy`) & Sintesis `CPMK-1..3`** (`CPL-06` = 15% + `CPL-09` = 15%).
* **Kepatuhan IKU 7 ($\ge 50\%$):** `Tugas 1 (20%) + Tugas 2 (20%) + UAS (30%)` = **70%** berbasis pemecahan kasus & purwarupa keputusan cerdas *(melampaui target minimal Dokumen 004 sebesar 60%)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total Titik (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-06`** (`P2`) | **`CPMK-1`** (C3) | `Sub-CPMK-1.1` | Mg 4 | Penugasan *problem-solving* kasus rute logistik: ekspansi simpul *Greedy Best-First* & **A\*** + kuis verifikasi 15' | **RTM-1 (Tugas 1)** Masalah 1–2 + Rubrik T1 | Sumatif | 12% | **20%** |
| **`CPL-06`** (`P2`) | **`CPMK-1`** (C3) | `Sub-CPMK-1.2` | Mg 4 | Penugasan *problem-solving*: pohon keputusan **Minimax** & **Alpha-Beta Pruning** | **RTM-1 (Tugas 1)** Masalah 3 + Rubrik T1 | Sumatif | 8% | |
| **`CPL-06`** (15%) & **`CPL-09`** (15%) | **`CPMK-2`** (C4) | `Sub-CPMK-2.1` | Mg 8 | Tes tertulis studi kasus terjadwal: perancangan basis aturan konsisten & jejak **Forward Chaining** | **Naskah Soal UTS** (Soal 1 & 2a) + Rubrik UTS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Tes tertulis studi kasus terjadwal: pohon sub-tujuan **Backward Chaining** & **Certainty Factor** | **Naskah Soal UTS** (Soal 2b & 3) + Rubrik UTS | Sumatif | 15% | |
| **`CPL-09`** (`KK1`) | **`CPMK-3`** (C4) | `Sub-CPMK-3.1` | Mg 12 | Penugasan studi kasus: perancangan fungsi keanggotaan & perhitungan lengkap **FIS Mamdani** | **RTM-2 (Tugas 2)** Bagian A + Kuis Verifikasi 15' | Sumatif | 11% | **20%** |
| **`CPL-09`** (`KK1`) | **`CPMK-3`** (C4) | `Sub-CPMK-3.2` | Mg 12 | Penugasan studi kasus: perhitungan **FIS Sugeno** Orde-0/1 & analisis komparatif | **RTM-2 (Tugas 2)** Bagian B + Rubrik T2 | Sumatif | 9% | |
| **`CPL-06`** (15%) & **`CPL-09`** (15%) | **`CPMK-3` & Sintesis `1..3`** (C4) | `Sub-CPMK-3.1, 3.2` + Integrasi `CPMK-2` | Mg 16 | Purwarupa Notebook Python **`scikit-fuzzy`** terverifikasi (40% UAS) + Ujian Tertulis Komprehensif 100' (60% UAS) | **Bundel Notebook `scikit-fuzzy`** & **Naskah Soal UAS** + Rubrik UAS | Sumatif | 30% | **30%** |
| **TOTAL** | **3 CPMK** | **6 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku MK Teori** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN (STANDAR KPT 2024 LAMPIRAN 23)

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Pencarian Ruang Status Heuristik & Minimax)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Kuis Verifikasi **Pekan 4** · Bobot **20%** (`CPMK-1` → `CPL-06`).
* **Objek & Batasan Pengerjaan Individu (Berparameter NIM):**
  1. **Masalah 1 (40%):** Diberikan graf jaringan pengiriman 10 simpul dengan bobot biaya tepi yang dimodifikasi 2 digit terakhir NIM beserta tabel jarak garis lurus $h(n)$. Buktikan apakah $h(n)$ bersifat *admissible* dan *consistent*, lalu susun tabel ekspansi lengkap `OPEN` dan `CLOSED` untuk **Greedy Best-First Search** dan **Algoritma A\***.
  2. **Masalah 2 (20%):** Hitung dan bandingkan jumlah simpul yang diekspansi, total biaya jalur solusi, serta kompleksitas ruang/waktu kedua algoritma pada Masalah 1.
  3. **Masalah 3 (40%):** Diberikan pohon keputusan kompetitif kedalaman 4 (16 daun berparameter NIM): hitung nilai propagasi **Minimax** dan tunjukkan secara eksplisit pembaruan batas $[\alpha, \beta]$ serta cabang yang terpotong pada **Alpha-Beta Pruning**.
* **Luaran:** `STI307_T1_Search_[NIM]_[Nama].pdf` di LMS Edlink + kuis konfirmasi 15 menit di kelas.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Sistem Pakar & Certainty Factor)
* **Format & Bobot:** Ujian Tertulis Luring Terjadwal (*Closed-Book*, **100 menit**) · Bobot **30%** (`CPMK-2` → 15% `CPL-06` + 15% `CPL-09`).
* **Rincian Soal:**
  1. **(35% — `Sub-CPMK-2.1`):** Berdasarkan narasi pengetahuan seorang pakar mutu pangan/diagnostik infrastruktur TI, rancang kamus simbol fakta, graf ketergantungan aturan, dan minimal **10 aturan produksi berantai** (2–3 lapis inferensi) yang bebas kontradiksi maupun siklus.
  2. **(35% — `Sub-CPMK-2.1 & 2.2`):** Telusuri basis aturan tersebut secara sistematis menggunakan tabel siklus **Forward Chaining** (dari kumpulan fakta awal) dan pohon pembuktian **Backward Chaining** (dari satu hipotesis target), serta jelaskan metode mana yang lebih efisien untuk kasus tersebut.
  3. **(30% — `Sub-CPMK-2.2`):** Hitung derajat keyakinan akhir kesimpulan sistem pakar menggunakan rumus **Certainty Factor (CF)** atas 3 jalur aturan yang aktif bersamaan.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Analisis Komparatif FIS Mamdani vs Sugeno)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Kuis Verifikasi **Pekan 12** · Bobot **20%** (`CPMK-3` → `CPL-09`).
* **Objek & Batasan Pengerjaan Individu (Berparameter NIM):**
  1. Merancang fungsi keanggotaan kurva bahu & segitiga/trapesium untuk 2 variabel input dan 1 variabel output beserta rumus matematis *piecewise*-nya.
  2. Menyusun matriks **9 aturan *fuzzy*** yang logis dan lengkap.
  3. Untuk pasangan input numerik tegas $(x_0, y_0)$ sesuai NIM, menghitung secara manual lengkap: (a) derajat keanggotaan *fuzzifikasi*; (b) $\alpha\text{-predikat}$ tiap aturan aktif; (c) keluaran tegas metode **Mamdani** (defuzzifikasi *Centroid* 10 titik sampel); dan (d) keluaran tegas metode **Sugeno** (*Weighted Average*), disertai analisis perbandingan keduanya.
* **Luaran:** `STI307_T2_Fuzzy_[NIM]_[Nama].pdf` di LMS Edlink + kuis konfirmasi 15 menit di kelas.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: `scikit-fuzzy` & Ujian Komprehensif)
* **Format & Bobot:** Bobot **30%** (`CPMK-3` & Sintesis → 15% `CPL-06` + 15% `CPL-09`), memadukan:
  1. **Bagian A — Purwarupa Notebook Python `scikit-fuzzy` Individu (40% nilai UAS):** Implementasi sistem pendukung keputusan berbasis *Rule-Screening + Fuzzy Inference* (`skfuzzy.control`), lengkap dengan grafik kurva keanggotaan, plot defuzzifikasi, *3D control surface*, rekonsiliasi terhadap perhitungan manual, dan uji sensitivitas 8 skenario batas. **Wajib murni simbolik/fuzzy — dilarang memakai model pelatihan `scikit-learn` atau *Neural Network*.**
  2. **Bagian B — Ujian Tertulis Komprehensif Luring 100 Menit (60% nilai UAS):** Soal perhitungan analitis FIS, penelusuran & pelengkapan kode `skfuzzy.control` di atas kertas (memastikan penguasaan otentik atas Bagian A), dan perancangan arsitektur sistem cerdas hibrid.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-307}}$)
$$NA_{\text{STI-307}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL (Dokumen 004 & 008)
1. **Ketercapaian `CPL-06` (`P2` — total bobot 50% MK: 20% T1 + 15% UTS + 15% UAS):**
   $$\text{Score}_{\text{CPL-06, STI-307}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,15\,S_{\text{UTS}}(i) + 0,15\,S_{\text{UAS}}(i)}{0,50} = 0,40\,S_{\text{Tugas 1}}(i) + 0,30\,S_{\text{UTS}}(i) + 0,30\,S_{\text{UAS}}(i)$$
   *(bobot SKS tertimbang pada agregasi prodi $= 2 \times 0,50 = 1,00\text{ SKS}$).*
2. **Ketercapaian `CPL-09` (`KK1` — total bobot 50% MK: 15% UTS + 20% T2 + 15% UAS):**
   $$\text{Score}_{\text{CPL-09, STI-307}}(i) = \frac{0,15\,S_{\text{UTS}}(i) + 0,20\,S_{\text{Tugas 2}}(i) + 0,15\,S_{\text{UAS}}(i)}{0,50} = 0,30\,S_{\text{UTS}}(i) + 0,40\,S_{\text{Tugas 2}}(i) + 0,30\,S_{\text{UAS}}(i)$$
   *(bobot SKS tertimbang pada agregasi prodi $= 2 \times 0,50 = 1,00\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)** pada skala baku UWG (`A: 81–100`, `B+: 76–80,99`, `B: 70–75,99`, `C+: 65–69,99`, `C: 56–64,99`, `D: 45–55,99`, `E: <45`).
* **Remedial & Handoff:** Mahasiswa dengan skor CPMK $< 65,0$ mengikuti 1 kali remedial terfokus pada CPMK terkait (skor maksimal pasca-remedial **70,0 / B**). Hasil evaluasi `CPMK-3` menjadi indikator kesiapan mahasiswa memasuki `STI-413 Pembelajaran Mesin` dan `STI-414 Pengantar NLP & Temu Balik Informasi` pada Semester 4.
