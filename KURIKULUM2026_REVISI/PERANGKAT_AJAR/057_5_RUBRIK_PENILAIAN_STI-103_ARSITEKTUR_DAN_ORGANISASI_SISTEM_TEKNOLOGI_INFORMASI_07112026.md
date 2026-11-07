# RUBRIK PENILAIAN
## STI-103 — ARSITEKTUR DAN ORGANISASI SISTEM TEKNOLOGI INFORMASI

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang
> **Dokumen induk:** `057_1_RPS_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md` dan `057_4_RENCANA_EVALUASI_ASESMEN_STI-103_ARSITEKTUR_DAN_ORGANISASI_SISTEM_TEKNOLOGI_INFORMASI_07112026.md`
> **Rujukan rubrik master:** Dokumen 008 (Rubrik 1–3) dan Dokumen 018 (4 klaster rubrik)
> **Tanggal:** 07 November 2026

---

## 1. PRINSIP DAN CAKUPAN

| Aspek | Ketentuan |
|---|---|
| Jenis rubrik | **Analitik** untuk seluruh asesmen sumatif (kriteria terpisah, skor teragregasi) |
| Jumlah level | 4 level: Sangat Baik (4), Baik (3), Cukup (2), Kurang (1) |
| Skala skor | 0–100 per dimensi |
| Transparansi | Rubrik dibagikan sebelum asesmen dilaksanakan |
| Konsistensi | Digunakan sama pada seluruh kelas paralel |
| Fokus | Penilaian **proses analisis rekayasa**, bukan hanya jawaban akhir |

**Daftar rubrik dalam dokumen ini:**

| Kode | Rubrik | Digunakan pada | Bobot |
|:---:|---|:---:|:---:|
| R-A | Tugas 1 — Dari Bit ke ALU | Pekan 4 | 20% |
| R-B | UTS — Representasi Data, Logika Digital, dan Arsitektur | Pekan 8 | 30% |
| R-C | Tugas 2 — Rancangan Platform Komputasi | Pekan 12–13 | 20% |
| R-D | UAS — Evaluasi Komprehensif | Pekan 16 | 30% |
| R-E | Presentasi & Partisipasi (formatif → komponen proses) | Pekan 12 & 15 | Formatif |
| R-F | Sikap, Etika, dan Integritas Akademik (formatif → syarat kelulusan) | Sepanjang semester | Syarat |

---

## 2. PANDUAN PENSKORAN UMUM

### 2.1 Skor Level

| Level | Label | Rentang Skor | Deskripsi Umum |
|:---:|---|:---:|---|
| **4** | Sangat Baik | 86–100 | Penguasaan penuh, analisis teknis mendalam, justifikasi kuantitatif, melampaui harapan minimal |
| **3** | Baik | 76–85 | Menguasai materi, prosedur benar dengan kekeliruan minor, memenuhi seluruh tuntutan |
| **2** | Cukup | 60–75 | Memenuhi sebagian tuntutan, ada kekeliruan teknis yang tidak fatal |
| **1** | Kurang | 0–59 | Tidak memenuhi tuntutan minimal, kekeliruan mendasar, atau tidak lengkap |

### 2.2 Rumus Skor Rubrik

$$Skor_{rubrik} = \sum_{d=1}^{D} (w_d \times s_d)$$

dengan $w_d$ = bobot dimensi ke-$d$ (jumlah = 1,0) dan $s_d$ = skor dimensi ke-$d$ (0–100).

### 2.3 Prinsip Penilaian Teknis (Wajib)

| Aturan | Ketentuan |
|---|---|
| **Skor per langkah** | Metode dan alur analisis benar memperoleh skor meskipun hasil akhir keliru akibat kesalahan hitung |
| **Jawaban tanpa langkah** | Maksimal 40% poin butir, meskipun jawaban akhir benar |
| **Diagram wajib berlabel** | Diagram tanpa label dinilai maksimal 50% poin butir terkait |
| **Satuan kuantitatif** | Perhitungan tanpa satuan (ns, MB/s, W) mengurangi 1 poin per butir |
| **Notasi** | Biner ditulis dengan subskrip 2, heksadesimal dengan awalan `0x`; pelanggaran mengurangi skor dimensi kerapian |
| **Justifikasi** | Rekomendasi tanpa argumen teknis dinilai maksimal 50% poin butir |

### 2.4 Prinsip Anti-Kekeliruan Umum

| Kekeliruan | Pencegahan |
|---|---|
| *Halo effect* (nilai satu dimensi memengaruhi dimensi lain) | Nilai tiap dimensi terpisah pada lembar skor per dimensi |
| *Central tendency* (semua nilai di tengah) | Wajib memilih level, bukan angka bebas di tengah |
| *Leniency/severity* | Moderasi antar-kelas dan *double marking* pada 10% sampel |
| Penilaian berdasarkan usaha, bukan bukti | Skor hanya berdasarkan bukti pada artefak yang dikumpulkan |

---

## 3. RUBRIK A — TUGAS 1: DARI BIT KE ALU (20%)

**Cakupan CPMK:** CPMK-1 (50%), CPMK-2 (50%) | **Sub-CPMK:** 1.1, 1.2, 2.1

| Dimensi (Bobot) | Level 4 — Sangat Baik (86–100) | Level 3 — Baik (76–85) | Level 2 — Cukup (60–75) | Level 1 — Kurang (< 60) |
|---|---|---|---|---|
| **A1. Ketepatan representasi data (25%)** | Seluruh konversi dan format IEEE 754 tepat; *sign*, *exponent* (bias 127), dan *mantissa* ditulis eksplisit; hasil hex benar | Tepat dengan 1 kekeliruan minor pada *mantissa* | Ada kesalahan konversi pada 2 butir | Tidak menguasai sistem bilangan |
| **A2. Ketepatan analisis rangkaian logika (30%)** | Tabel kebenaran, K-map, dan persamaan benar; rangkaian hasil ekuivalen secara fungsional dan tergambar rapi | Persamaan benar; gambar rangkaian kurang rapi atau kurang berlabel | Penyederhanaan benar sebagian; rangkaian tidak ekuivalen | Tabel kebenaran salah |
| **A3. Pemahaman siklus instruksi (30%)** | Seluruh register (PC, IR, MAR, MDR) dan urutan lima tahap tepat; diagram alur konsisten dengan *datapath* | Urutan benar; 1–2 peran register kurang tepat | Urutan benar sebagian; peran register tertukar | Tidak memahami siklus instruksi |
| **A4. Kerapian & tata tulis teknis (15%)** | Notasi biner/hex konsisten; gambar berlabel lengkap; seluruh butir dijawab | Notasi konsisten; gambar kurang berlabel | Notasi tidak konsisten; ada butir tidak dijawab | Jawaban tidak terbaca |

**Contoh perhitungan:**
A1 = 88, A2 = 82, A3 = 90, A4 = 86
→ Skor = (0,25×88) + (0,30×82) + (0,30×90) + (0,15×86) = 22,0 + 24,6 + 27,0 + 12,9 = **86,5 (Sangat Baik)**

**Ambang minimal kelulusan komponen:** 60. Skor < 60 wajib revisi dan dinilai ulang maksimal 7 hari setelah umpan balik.

---

## 4. RUBRIK B — UTS: REPRESENTASI DATA, LOGIKA DIGITAL, DAN ARSITEKTUR (30%)

**Cakupan CPMK:** CPMK-1 (35%), CPMK-2 (30%), CPMK-3 (35%) | **Bentuk:** 4 bagian

### 4.1 Alokasi Poin per Bagian

| Bagian | Fokus | Poin | CPMK |
|:--:|---|:--:|:--:|
| I | Representasi data & IEEE 754 | 20 | CPMK-1 |
| II | Siklus instruksi & *datapath* | 15 | CPMK-1 |
| III | Rangkaian kombinasional & sekuensial | 30 | CPMK-2 |
| IV | Studi kasus komparatif (CISC/RISC, memori) | 35 | CPMK-3 |

### 4.2 Rubrik Uraian (diterapkan pada seluruh bagian)

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **B1. Penguasaan konsep arsitektur (25%)** | Definisi, register, dan mekanisme dijelaskan tepat dan saling terkait | Tepat dengan 1–2 kekeliruan minor | Beberapa kekeliruan konseptual yang memengaruhi jawaban | Salah memahami konsep inti |
| **B2. Ketepatan analisis rangkaian (25%)** | Analisis kombinasional dan sekuensial tepat; *timing* konsisten; diagram waktu benar | Sebagian besar tepat; satu kesalahan fungsional kecil | Analisis dangkal atau ada kesalahan fungsional | Tidak mampu menganalisis |
| **B3. Kualitas analisis komparatif (30%)** | Komparasi multidimensi (ISA, performa, daya, biaya, ekosistem) dengan *trade-off* eksplisit | Komparasi jelas; dua dimensi utama tercakup | Komparasi dangkal; satu dimensi | Tidak ada komparasi |
| **B4. Ketepatan kuantitatif & kelengkapan (20%)** | Seluruh perhitungan AMAT/*hit ratio* benar dengan interpretasi dan satuan tepat | Perhitungan benar; interpretasi ringkas | Ada kesalahan hitung atau satuan | Tidak menjawab perhitungan |

### 4.3 Kunci Berlapis Bagian IV (Studi Kasus Komparatif, 35 poin)

| Elemen Jawaban | Poin | Kriteria |
|---|:--:|---|
| Perbandingan CISC vs RISC untuk beban kerja (i) | 10 | 10 poin bila ≥ 3 argumen teknis tepat (ISA, *pipelining*, memori, daya) |
| Perbandingan untuk beban kerja (ii) | 8 | 8 poin bila pilihan platform tepat dengan justifikasi daya/performa |
| Perhitungan AMAT | 9 | 4 poin formula benar; 3 poin substitusi nilai; 2 poin satuan & hasil |
| Interpretasi dampak desain | 8 | 8 poin bila dikaitkan dengan keputusan ukuran cache, asosiativitas, atau lokalitas kode |

---

## 5. RUBRIK C — TUGAS 2: RANCANGAN PLATFORM KOMPUTASI (20%)

**Cakupan CPMK:** CPMK-3 (40%), CPMK-4 (60%) | **Sub-CPMK:** 3.1, 3.2, 4.1, 4.2, 4.3, 4.4 | **Bentuk:** Laporan proyek + diagram + presentasi

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **C1. Karakterisasi beban kerja (25%)** | Profil beban kerja dikuantifikasi (CPU/memori/I/O) dengan asumsi eksplisit, realistis, dan terjustifikasi | Profil memadai; asumsi sebagian tersurat | Profil generik; asumsi tidak jelas | Tidak ada karakterisasi |
| **C2. Kelayakan rancangan platform (30%)** | Rancangan konsisten dengan profil beban; pilihan arsitektur dan strategi virtualisasi terjustifikasi teknis | Rancangan layak; justifikasi memadai | Rancangan generik; justifikasi lemah | Rancangan tidak dapat diimplementasikan |
| **C3. Ketepatan estimasi kuantitatif (25%)** | Seluruh estimasi (inti CPU, memori, AMAT/*throughput*) dihitung benar, bersatuan, dan diinterpretasikan | Estimasi benar; interpretasi ringkas | Ada kesalahan hitung atau estimasi tidak lengkap | Tidak ada estimasi |
| **C4. Evaluasi *data center* & *trade-off* (20%)** | Analisis daya, PUE, redundansi, dan *trade-off* biaya–performa–risiko kritis dan terukur | Analisis memadai; *trade-off* disebut | Analisis umum | Mengabaikan aspek *data center* |

### 5.1 Penilaian Kontribusi Tim (anti-*free-rider*)

| Kondisi | Penyesuaian Skor Individu |
|---|---|
| Kontribusi merata, terdokumentasi (log pertemuan, riwayat dokumen) | 100% dari skor kelompok |
| Kontribusi terbukti pada ≥ 3 dari 4 dimensi | 90–100% |
| Kontribusi parsial, tidak terdokumentasi | 70–89% |
| Kontribusi minimal / tidak dapat menjelaskan rancangan saat verifikasi 3 menit | ≤ 50% |
| Tidak berkontribusi | 0% |

---

## 6. RUBRIK D — UAS: EVALUASI KOMPREHENSIF (30%)

**Cakupan CPMK:** CPMK-1 s.d. CPMK-4 | **Bentuk:** 4 bagian

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **D1. Penguasaan konsep komprehensif (25%)** | Mengaitkan representasi data, ALU, ISA, memori, I/O, dan virtualisasi secara utuh dan koheren | Konsep benar; keterkaitan antar-bagian sebagian | Konsep terpisah-pisah; keterkaitan lemah | Salah konsep mendasar |
| **D2. Ketepatan analisis teknis (30%)** | Analisis kuantitatif tepat; implikasi desain dijelaskan; satuan dan asumsi benar | Analisis tepat; interpretasi ringkas | Analisis umum; tanpa kuantifikasi | Analisis tidak berdasar |
| **D3. Kedalaman evaluasi & *trade-off* (30%)** | Evaluasi kritis multi-kriteria (biaya, daya, performa, risiko) dengan rekomendasi tegas | Evaluasi jelas; dua kriteria utama | Evaluasi dangkal; satu kriteria | Tidak ada evaluasi |
| **D4. Struktur & komunikasi teknis (15%)** | Uraian runtut; terminologi tepat; kesimpulan eksplisit dan konsisten | Uraian jelas; kesimpulan ada | Uraian kurang runtut | Tidak terstruktur |

### 6.1 Kunci Berlapis Bagian III — Virtualisasi & *Data Center* (25 poin)

| Elemen | Poin | Kriteria |
|---|:--:|---|
| Evaluasi kelayakan *overcommitment* memori | 8 | 5 poin analisis (pemanfaatan 62%, risiko *swapping*); 3 poin rekomendasi |
| Perbandingan *hypervisor* Tipe 1 vs Tipe 2 | 6 | 3 poin karakteristik tiap tipe; 3 poin kesesuaian dengan kebutuhan |
| Pertimbangan alternatif kontainer | 4 | 4 poin bila isolasi, kepadatan, dan *startup* dibandingkan |
| Strategi konsolidasi & dampak PUE/daya | 7 | 4 poin strategi; 3 poin estimasi dampak kuantitatif |

### 6.2 Kunci Berlapis Bagian IV — Perancangan Solusi Terbuka (20 poin)

| Elemen | Poin | Kriteria |
|---|:--:|---|
| Identifikasi kebutuhan & batasan | 5 | 5 poin bila kebutuhan fungsional dan batasan (anggaran/daya) eksplisit |
| Pemilihan komponen platform | 6 | 6 poin bila prosesor, memori, dan I/O dipilih konsisten dengan beban kerja |
| Perhitungan kelayakan | 5 | 5 poin bila estimasi kuantitatif benar dan bersatuan |
| Risiko & mitigasi | 4 | 4 poin bila ≥ 2 risiko teknis disertai mitigasi konkret |

---

## 7. RUBRIK E — PRESENTASI DAN PARTISIPASI (FORMATIF)

**Digunakan:** Pekan 6 (*gallery walk*), Pekan 12 (presentasi antara), Pekan 15 (presentasi final)

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **E1. Penguasaan materi (40%)** | Menguasai penuh; mampu menggambar ulang diagram arsitektur di papan saat ditanya | Memahami materi; jawaban tepat dan logis | Pemahaman cukup; ragu saat tanya jawab | Tidak menguasai materi |
| **E2. Kualitas media visual (30%)** | Diagram arsitektur profesional; blok berlabel; data terstruktur dalam tabel | Slide rapi; label sebagian besar ada | Slide terlalu padat; label sering hilang | Slide buruk/tidak berstruktur |
| **E3. Artikulasi & alokasi waktu (30%)** | Lugas, percaya diri, kontak mata baik, tepat waktu | Komunikasi jelas; intonasi baik; waktu pas | Suara monoton; melebihi batas waktu | Komunikasi pasif; tidak terkontrol |

---

## 8. RUBRIK F — SIKAP, ETIKA, DAN INTEGRITAS AKADEMIK (SYARAT)

| Aspek | Indikator Terpenuhi | Indikator Tidak Terpenuhi |
|---|---|---|
| Kehadiran | ≥ 75% pertemuan | < 75% pertemuan → nilai maksimum D |
| Ketepatan pengumpulan | ≥ 80% tugas tepat waktu | < 50% tugas terlambat berat |
| Deklarasi AI | Seluruh tugas menyertakan deklarasi penggunaan AI/simulator | Ada tugas tanpa deklarasi |
| Orisinalitas | Kemiripan ≤ 25%; dapat menjelaskan diagram/analisis karyanya | Kemiripan > 25% atau tidak dapat menjelaskan karya |
| Sitasi diagram | Diagram dari sumber eksternal disitasi dengan benar | Diagram disalin tanpa sitasi |
| Etika kelas | Menghormati dosen dan sesama; aktif konstruktif | Mengganggu, tidak menghormati, atau manipulatif |

**Konsekuensi:** pelanggaran integritas akademik berat (plagiarisme, pemalsuan data perhitungan, kerja sama terlarang) dikenakan nilai 0 pada komponen terkait dan diproses sesuai Peraturan Akademik Universitas.

---

## 9. REKAPITULASI BOBOT DAN KONVERSI

### 9.1 Rekap Bobot Asesmen

| Rubrik | Bobot terhadap NA | Skor Maksimum |
|:---:|:---:|:---:|
| R-A Tugas 1 | 20% | 100 |
| R-B UTS | 30% | 100 |
| R-C Tugas 2 | 20% | 100 |
| R-D UAS | 30% | 100 |
| **Total** | **100%** | |

### 9.2 Konversi Nilai

| NA | Huruf | Bobot | Status |
|:---:|:---:|:---:|:---:|
| 86–100 | A | 4,00 | Lulus |
| 76–85 | B+ | 3,50 | Lulus |
| 70–75 | B | 3,00 | Lulus |
| 66–69 | C+ | 2,50 | Lulus |
| 60–65 | C | 2,00 | Lulus (batas) |
| 56–59 | D | 1,00 | Tidak lulus |
| 0–55 | E | 0,00 | Tidak lulus |

### 9.3 Contoh Perhitungan Lengkap

| Komponen | Skor | Bobot | Kontribusi |
|:---:|:---:|:---:|:---:|
| Tugas 1 | 86,5 | 20% | 17,30 |
| UTS | 74 | 30% | 22,20 |
| Tugas 2 | 85 | 20% | 17,00 |
| UAS | 78 | 30% | 23,40 |
| **Nilai Akhir** | | | **79,90 → B+** |

Ketercapaian CPMK mahasiswa tersebut:
- CPMK-1 = 0,50×86,5 + 0,50×74 = 43,25 + 37,00 = **80,3**
- CPMK-2 = 0,50×86,5 + 0,40×74 + 0,10×78 = 43,25 + 29,60 + 7,80 = **80,7**
- CPMK-3 = 0,10×74 + 0,40×85 + 0,50×78 = 7,40 + 34,00 + 39,00 = **80,4**
- CPMK-4 = 0,60×85 + 0,40×78 = 51,00 + 31,20 = **82,2**

Seluruh CPMK ≥ 60 → **tuntas CPMK**. Ketercapaian CPL:
- `CPL-05` (`P1`) = 0,25 × 79,90 = **19,98** (ambang ≥ 65,0 pada skala CPL penuh → lihat catatan)
- `CPL-07` (`P3`) = 0,45 × 79,90 = **35,96**
- `CPL-02` (`KU1`) = 0,30 × 79,90 = **23,97**

> **Catatan pembacaan:** nilai berbobot di atas adalah **kontribusi parsial** MK terhadap CPL program. Ketercapaian CPL penuh dihitung pada tingkat prodi dengan menjumlahkan kontribusi seluruh MK pembina CPL tersebut (Dokumen 008 Bagian 3.3–3.4).

---

## 10. LEMBAR REKAP PENILAIAN (SPEED GRADING SHEET)

```
================================================================================
LEMBAR ASESMEN OBE CEPAT — STI-103 ARSITEKTUR DAN ORGANISASI SISTEM TI
Kelas: ____ | Semester: 1 | Tahun Akademik: ____ | Dosen: __________________
--------------------------------------------------------------------------------
No | NIM | Nama | T1 (20%)  | UTS (30%)   | T2 (20%)  | UAS (30%) | NA | Grade
   |     |      | [CPMK-1,2]| [CPMK-1,2,3]| [CPMK-3,4]| [Komp.]   |    |
--------------------------------------------------------------------------------
 1 |     |      |           |             |           |           |    |
 2 |     |      |           |             |           |           |    |
 3 |     |      |           |             |           |           |    |
--------------------------------------------------------------------------------
RATA-RATA CPMK-1: ____ | CPMK-2: ____ | CPMK-3: ____ | CPMK-4: ____
KETERCAPAIAN CPL: CPL-05 (P1) ____ | CPL-07 (P3) ____ | CPL-02 (KU1) ____
================================================================================
```

**Petunjuk pengisian:** isi skor 0–100 per komponen; NA dihitung otomatis dengan rumus 9.1; kolom Grade diisi berdasarkan tabel 9.2; rekap CPMK dihitung dengan rumus Bagian 6.2 dokumen 055_4.

---

## 11. MODERASI, VALIDASI, DAN TINDAK LANJUT

| Aktivitas | Ketentuan |
|---|---|
| Validasi rubrik sebelum digunakan | Ditelaah Koordinator RMK dan UPM FSTI |
| Verifikasi kunci jawaban | Setiap kunci (termasuk tabel kebenaran dan perhitungan AMAT) diperiksa penelaah kedua sebelum ujian |
| Moderasi antar-kelas | 10% sampel dinilai ulang oleh dosen kedua; selisih > 10 poin dibahas bersama |
| Kalibrasi penilai | Sesi kalibrasi 60 menit sebelum penilaian tugas besar, menggunakan 3 sampel jawaban |
| Dokumentasi | Lembar skor per dimensi diarsipkan bersama artefak mahasiswa |
| Revisi rubrik | Dilakukan bila > 20% mahasiswa memperoleh level 1 pada dimensi yang sama |
| Pelaporan | Rekap ke Koordinator RMK paling lambat 7 hari setelah asesmen |

---

## 12. RIWAYAT REVISI

| Versi | Tanggal | Perubahan | Penyusun |
|:---:|:---:|---|---|
| 1.0 | 07 November 2026 | Penyusunan awal; 6 rubrik (A–F) untuk 4 CPMK, dilengkapi kunci berlapis dan penanganan 3 CPL | Tim Pengembang RPS SISTEKIN |

---

*Rubrik ini merupakan turunan langsung dari CPMK/Sub-CPMK Dokumen 043 dan skema asesmen Dokumen 008. Setiap perubahan bobot atau dimensi wajib disertai revisi dokumen 055_1 dan 055_4.*
