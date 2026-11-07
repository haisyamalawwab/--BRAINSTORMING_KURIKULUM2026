# RUBRIK PENILAIAN
## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA

> **Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang
> **Dokumen induk:** `058_1_RPS_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md` dan `058_4_RENCANA_EVALUASI_ASESMEN_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md`
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
| Fokus | Penilaian **proses penalaran formal**, bukan hanya kesimpulan |

**Daftar rubrik dalam dokumen ini:**

| Kode | Rubrik | Digunakan pada | Bobot |
|:---:|---|:---:|:---:|
| R-A | Tugas 1 — Logika Formal dan Struktur Relasi | Pekan 4 | 20% |
| R-B | UTS — Logika Formal, Struktur Diskrit, dan Graf | Pekan 8 | 30% |
| R-C | Tugas 2 — Pemodelan Diskrit untuk Sistem Nyata | Pekan 12–13 | 20% |
| R-D | UAS — Evaluasi Komprehensif | Pekan 16 | 30% |
| R-E | Presentasi & Partisipasi (formatif → komponen proses) | Pekan 12 & 15 | Formatif |
| R-F | Sikap, Etika, dan Integritas Akademik (formatif → syarat kelulusan) | Sepanjang semester | Syarat |

---

## 2. PANDUAN PENSKORAN UMUM

### 2.1 Skor Level

| Level | Label | Rentang Skor | Deskripsi Umum |
|:---:|---|:---:|---|
| **4** | Sangat Baik | 86–100 | Pembuktian lengkap dan valid; setiap langkah terjustifikasi; melampaui harapan minimal |
| **3** | Baik | 76–85 | Pembuktian benar dengan kekeliruan minor pada notasi atau satu langkah yang diringkas |
| **2** | Cukup | 60–75 | Struktur pembuktian ada tetapi tidak lengkap; ada kekeliruan yang tidak fatal |
| **1** | Kurang | 0–59 | Tidak memenuhi tuntutan minimal; tidak ada kerangka pembuktian atau kekeliruan mendasar |

### 2.2 Rumus Skor Rubrik

$$Skor_{rubrik} = \sum_{d=1}^{D} (w_d \times s_d)$$

dengan $w_d$ = bobot dimensi ke-$d$ (jumlah = 1,0) dan $s_d$ = skor dimensi ke-$d$ (0–100).

### 2.3 Prinsip Penilaian Pembuktian (Wajib)

| Aturan | Ketentuan |
|---|---|
| **Skor per langkah** | Langkah pembuktian yang valid tetap memperoleh skor meskipun kesimpulan akhir keliru |
| **Kesimpulan tanpa langkah** | Maksimal 40% poin butir, meskipun kesimpulan benar |
| **Kesalahan logika** | Satu langkah yang tidak valid menggugurkan skor langkah itu dan langkah yang bergantung padanya |
| **Struktur wajib** | Pembuktian induksi tanpa basis/hipotesis/langkah eksplisit dinilai maksimal 50% poin butir |
| **Diagram berlabel** | Diagram Hasse, graf, atau diagram status tanpa label dinilai maksimal 50% poin butir |
| **Notasi** | Simbol baku ($\land$, $\lor$, $\lnot$, $\to$, $\leftrightarrow$, $\forall$, $\exists$); pelanggaran mengurangi skor dimensi kerapian |
| **Verifikasi** | Mahasiswa yang menuliskan cek ulang (uji string, uji relasi, uji sifat graf) mendapat nilai plus pada dimensi argumentasi |

### 2.4 Prinsip Anti-Kekeliruan Umum

| Kekeliruan | Pencegahan |
|---|---|
| *Halo effect* | Nilai tiap dimensi terpisah pada lembar skor per dimensi |
| *Central tendency* | Wajib memilih level, bukan angka bebas di tengah |
| *Leniency/severity* | Moderasi antar-kelas dan *double marking* pada 10% sampel |
| Penilaian berdasarkan panjang jawaban | Skor hanya berdasarkan bukti penalaran, bukan volume tulisan |

---

## 3. RUBRIK A — TUGAS 1: LOGIKA FORMAL DAN STRUKTUR RELASI (20%)

**Cakupan CPMK:** CPMK-1 (60%), CPMK-2 (40%) | **Sub-CPMK:** 1.1, 1.2, 2.1

| Dimensi (Bobot) | Level 4 — Sangat Baik (86–100) | Level 3 — Baik (76–85) | Level 2 — Cukup (60–75) | Level 1 — Kurang (< 60) |
|---|---|---|---|---|
| **A1. Ketepatan logika proposisi (25%)** | Tabel kebenaran lengkap; setiap langkah penyederhanaan aljabar logika valid dan hukumnya disebut | Tabel benar; satu langkah penyederhanaan diringkas tanpa menyebut hukum | Ada kesalahan penerapan hukum logika pada satu butir | Tabel kebenaran salah atau tidak lengkap |
| **A2. Ketepatan inferensi & kuantifikasi (30%)** | Seluruh aturan inferensi disebut dan diterapkan tepat; kuantor dan negasinya benar | Aturan tepat; 1–2 kekeliruan notasi kuantor | Argumen valid tetapi justifikasi aturan tidak lengkap | Tidak mampu membedakan aturan inferensi |
| **A3. Ketepatan pembuktian induksi (30%)** | Basis, hipotesis, dan langkah induksi lengkap; setiap transisi aljabar terjustifikasi | Ketiga komponen ada; satu transisi aljabar diringkas | Langkah induksi ada, tetapi basis atau hipotesis tidak dinyatakan | Tidak memahami struktur induksi |
| **A4. Ketepatan analisis relasi & Poset (15%)** | Seluruh sifat relasi diuji; diagram Hasse benar; elemen ekstremal diidentifikasi tepat | Sifat relasi benar; diagram kurang rapi | Satu sifat relasi keliru; elemen ekstremal sebagian benar | Tidak mampu menguji sifat relasi |

**Contoh perhitungan:**
A1 = 88, A2 = 80, A3 = 85, A4 = 90
→ Skor = (0,25×88) + (0,30×80) + (0,30×85) + (0,15×90) = 22,0 + 24,0 + 25,5 + 13,5 = **85,0 (Baik)**

**Ambang minimal kelulusan komponen:** 60. Skor < 60 wajib revisi dan dinilai ulang maksimal 7 hari setelah umpan balik.

---

## 4. RUBRIK B — UTS: LOGIKA FORMAL, STRUKTUR DISKRIT, DAN GRAF (30%)

**Cakupan CPMK:** CPMK-1 (35%), CPMK-2 (35%), CPMK-3 (30%) | **Bentuk:** 4 bagian

### 4.1 Alokasi Poin per Bagian

| Bagian | Fokus | Poin | CPMK |
|:--:|---|:--:|:--:|
| I | Logika proposisi & predikat | 25 | CPMK-1 |
| II | Pembuktian induksi & verifikasi algoritma | 20 | CPMK-1 |
| III | Relasi, Poset, aljabar Boolean, kombinatorika | 30 | CPMK-2 |
| IV | Studi kasus graf (representasi & penelusuran) | 25 | CPMK-3 |

### 4.2 Rubrik Uraian (diterapkan pada seluruh bagian)

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **B1. Penguasaan konsep formal (25%)** | Definisi dan teorema digunakan tepat; notasi logika sempurna; syarat keberlakuan disebut | Tepat dengan 1–2 kekeliruan notasi | Konsep dasar dipahami; ada kesalahan definisi | Salah memahami konsep inti |
| **B2. Keruntutan pembuktian (30%)** | Pembuktian sistematis dari premis ke konklusi; setiap langkah terjustifikasi | Sebagian besar runtut; ada lompatan kecil | Pembuktian terputus-putus; justifikasi minim | Tidak ada alur pembuktian |
| **B3. Ketepatan hasil & justifikasi algoritma (30%)** | Seluruh hasil benar; pemilihan algoritma dan urutan langkah terjustifikasi | Hasil benar; justifikasi ringkas | Sebagian besar hasil keliru atau algoritma tidak tepat | Hasil tidak relevan |
| **B4. Kelengkapan & kerapian jawaban (15%)** | Seluruh butir dijawab lengkap, diagram berlabel, urutan sesuai nomor | Seluruh butir dijawab; beberapa kurang rinci | Ada butir tidak dijawab | Banyak butir kosong |

### 4.3 Kunci Berlapis Bagian IV (Studi Kasus Graf, 25 poin)

| Elemen Jawaban | Poin | Kriteria |
|---|:--:|---|
| Menggambar graf dari matriks ketetanggaan | 6 | 6 poin bila seluruh 8 sisi tergambar benar; −1 per sisi hilang/salah |
| Menentukan derajat setiap simpul | 4 | 4 poin bila keenam derajat benar dan konsisten dengan *handshaking lemma* |
| Urutan pemilihan sisi Kruskal | 9 | 9 poin bila urutan benar dan setiap penolakan sisi (pembentuk siklus) dijelaskan |
| Total panjang kabel minimum | 3 | 3 poin bila hasil penjumlahan tepat dengan satuan meter |
| Interpretasi hasil | 3 | 3 poin bila dikaitkan dengan implikasi rekayasa (redundansi, biaya) |

---

## 5. RUBRIK C — TUGAS 2: PEMODELAN DISKRIT UNTUK SISTEM NYATA (20%)

**Cakupan CPMK:** CPMK-3 (30%), CPMK-4 (70%) | **Sub-CPMK:** 3.1, 3.2, 4.1, 4.2, 4.3, 4.4 | **Bentuk:** Laporan proyek + visualisasi + presentasi

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **C1. Ketepatan formalisasi model (30%)** | Model diskrit didefinisikan lengkap dan konsisten; seluruh asumsi dinyatakan dan dibenarkan | Model benar; satu komponen kurang eksplisit | Model benar sebagian; asumsi tidak jelas | Model tidak terbentuk |
| **C2. Ketepatan algoritma & verifikasi manual (25%)** | ≥ 2 contoh kerja benar; setiap langkah algoritma terverifikasi | Contoh benar; verifikasi sebagian | Satu contoh benar; verifikasi tidak ada | Hasil tidak dapat diverifikasi |
| **C3. Kualitas visualisasi & interpretasi (25%)** | Diagram akurat dan berlabel; interpretasi menghubungkan model dengan sistem nyata secara kritis | Diagram benar; interpretasi memadai | Diagram kurang informatif; interpretasi dangkal | Tanpa visualisasi atau diagram salah |
| **C4. Analisis kompleksitas & keterbatasan (20%)** | Kompleksitas dianalisis (mis. $O(E\log V)$) dan keterbatasan model dibahas kritis; laporan rapi; ≥ 6 rujukan IEEE | Analisis memadai; 4–5 rujukan | Analisis umum; < 4 rujukan | Tanpa analisis kompleksitas/keterbatasan |

### 5.1 Penilaian Kontribusi Tim (anti-*free-rider*)

| Kondisi | Penyesuaian Skor Individu |
|---|---|
| Kontribusi merata, terdokumentasi (log pertemuan, riwayat dokumen) | 100% dari skor kelompok |
| Kontribusi terbukti pada ≥ 3 dari 4 dimensi | 90–100% |
| Kontribusi parsial, tidak terdokumentasi | 70–89% |
| Kontribusi minimal / tidak dapat menjelaskan model saat verifikasi 3 menit | ≤ 50% |
| Tidak berkontribusi | 0% |

---

## 6. RUBRIK D — UAS: EVALUASI KOMPREHENSIF (30%)

**Cakupan CPMK:** CPMK-1 s.d. CPMK-4 | **Bentuk:** 4 bagian

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **D1. Penguasaan konsep komprehensif (25%)** | Mengaitkan logika–struktur–graf–otomata secara utuh; batas keberlakuan setiap konsep disebut | Konsep benar; keterkaitan antar-bagian sebagian | Konsep terpisah-pisah; keterkaitan lemah | Salah konsep mendasar |
| **D2. Ketepatan formalisasi & komputasi (30%)** | Seluruh definisi formal dan perhitungan tepat; notasi konsisten; langkah efisien | 1–2 kekeliruan minor | Beberapa kekeliruan yang memengaruhi hasil | Formalisasi tidak dapat diikuti |
| **D3. Kedalaman analisis & justifikasi (30%)** | Justifikasi setiap pilihan model/algoritma; implikasi perubahan parameter dianalisis | Justifikasi tepat; kurang mendalam | Justifikasi deskriptif | Tanpa justifikasi |
| **D4. Struktur & komunikasi matematis (15%)** | Uraian runtut; definisi dipakai tepat; kesimpulan eksplisit | Uraian jelas; kesimpulan ada | Uraian kurang runtut | Tidak terstruktur |

### 6.1 Kunci Berlapis Bagian III — Otomata (30 poin)

| Elemen | Poin | Kriteria |
|---|:--:|---|
| Konstruksi DFA lengkap (5-tuple + tabel transisi) | 12 | 6 poin 5-tuple benar; 4 poin tabel transisi lengkap; 2 poin status awal/akhir ditandai |
| Uji tiga string dengan jejak transisi | 10 | 3 poin per string benar (9) + 1 poin kerapian jejak |
| Konstruksi NFA dan konversi *subset construction* | 8 | 4 poin NFA benar; 4 poin hasil konversi konsisten (setiap status gabungan ε-closure) |
| Perbandingan jumlah status DFA vs NFA | 2 | 2 poin bila selisih dikuantifikasi dan penyebabnya dijelaskan |

### 6.2 Kunci Berlapis Bagian IV — Pemodelan Terbuka (20 poin)

| Elemen | Poin | Kriteria |
|---|:--:|---|
| Identifikasi entitas & relasi | 5 | 5 poin bila himpunan simpul/relasi didefinisikan dan batas domain eksplisit |
| Formalisasi model diskrit | 5 | 5 poin bila formalisasi tepat dan dapat dioperasikan |
| Prosedur algoritma | 6 | 6 poin bila algoritma tepat dengan urutan langkah lengkap |
| Interpretasi & validasi hasil | 4 | 4 poin bila hasil diuji terhadap batas kasus/konteks |

---

## 7. RUBRIK E — PRESENTASI DAN PARTISIPASI (FORMATIF)

**Digunakan:** Pekan 11 (konsultasi), Pekan 12 (presentasi antara), Pekan 15 (presentasi final)

| Dimensi (Bobot) | Level 4 (86–100) | Level 3 (76–85) | Level 2 (60–75) | Level 1 (< 60) |
|---|---|---|---|---|
| **E1. Penguasaan materi (40%)** | Menguasai penuh; mampu membuktikan ulang satu klaim di papan saat ditanya | Memahami materi; jawaban tepat dan logis | Pemahaman cukup; ragu saat tanya jawab | Tidak menguasai materi |
| **E2. Kualitas media visual (30%)** | Diagram graf/Hasse/otomata profesional dan berlabel; notasi formal benar pada slide | Slide rapi; label sebagian besar ada | Slide terlalu padat; label sering hilang | Slide buruk/tidak berstruktur |
| **E3. Artikulasi & alokasi waktu (30%)** | Lugas, percaya diri, kontak mata baik, tepat waktu | Komunikasi jelas; intonasi baik; waktu pas | Suara monoton; melebihi batas waktu | Komunikasi pasif; tidak terkontrol |

---

## 8. RUBRIK F — SIKAP, ETIKA, DAN INTEGRITAS AKADEMIK (SYARAT)

| Aspek | Indikator Terpenuhi | Indikator Tidak Terpenuhi |
|---|---|---|
| Kehadiran | ≥ 75% pertemuan | < 75% pertemuan → nilai maksimum D |
| Ketepatan pengumpulan | ≥ 80% tugas tepat waktu | < 50% tugas terlambat berat |
| Deklarasi AI | Seluruh tugas menyertakan deklarasi penggunaan AI/simulator | Ada tugas tanpa deklarasi |
| Orisinalitas | Kemiripan ≤ 25%; dapat menjelaskan pembuktian karyanya | Kemiripan > 25% atau tidak dapat menjelaskan karya |
| Sitasi pembuktian | Kerangka pembuktian dari sumber eksternal disitasi dengan benar | Kerangka disalin tanpa sitasi |
| Etika kelas | Menghormati dosen dan sesama; aktif konstruktif | Mengganggu, tidak menghormati, atau manipulatif |

**Konsekuensi:** pelanggaran integritas akademik berat (plagiarisme, pemalsuan hasil pembuktian, kerja sama terlarang) dikenakan nilai 0 pada komponen terkait dan diproses sesuai Peraturan Akademik Universitas.

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
| Tugas 1 | 85,0 | 20% | 17,00 |
| UTS | 73 | 30% | 21,90 |
| Tugas 2 | 87 | 20% | 17,40 |
| UAS | 80 | 30% | 24,00 |
| **Nilai Akhir** | | | **80,30 → B+** |

Ketercapaian CPMK mahasiswa tersebut:
- CPMK-1 = 0,60×85,0 + 0,40×73 = 51,00 + 29,20 = **80,2**
- CPMK-2 = 0,40×85,0 + 0,60×73 = 34,00 + 43,80 = **77,8**
- CPMK-3 = 0,20×73 + 0,30×87 + 0,50×80 = 14,60 + 26,10 + 40,00 = **80,7**
- CPMK-4 = 0,60×87 + 0,40×80 = 52,20 + 32,00 = **84,2**

Seluruh CPMK ≥ 60 → **tuntas CPMK**. Ketercapaian CPL:
- `CPL-05` (`P1`) = 0,70 × 80,30 = **56,21**
- `CPL-02` (`KU1`) = 0,30 × 80,30 = **24,09**

> **Catatan pembacaan:** nilai berbobot di atas adalah **kontribusi parsial** MK terhadap CPL program. Ketercapaian CPL penuh dihitung pada tingkat prodi dengan menjumlahkan kontribusi seluruh MK pembina CPL tersebut (Dokumen 008 Bagian 3.3–3.4).

---

## 10. LEMBAR REKAP PENILAIAN (SPEED GRADING SHEET)

```
================================================================================
LEMBAR ASESMEN OBE CEPAT — STI-204 MATEMATIKA DISKRIT DAN LOGIKA
Kelas: ____ | Semester: 2 | Tahun Akademik: ____ | Dosen: __________________
--------------------------------------------------------------------------------
No | NIM | Nama | T1 (20%)  | UTS (30%)   | T2 (20%)  | UAS (30%) | NA | Grade
   |     |      | [CPMK-1,2]| [CPMK-1,2,3]| [CPMK-3,4]| [Komp.]   |    |
--------------------------------------------------------------------------------
 1 |     |      |           |             |           |           |    |
 2 |     |      |           |             |           |           |    |
 3 |     |      |           |             |           |           |    |
--------------------------------------------------------------------------------
RATA-RATA CPMK-1: ____ | CPMK-2: ____ | CPMK-3: ____ | CPMK-4: ____
KETERCAPAIAN CPL: CPL-05 (P1) ____ | CPL-02 (KU1) ____
================================================================================
```

**Petunjuk pengisian:** isi skor 0–100 per komponen; NA dihitung otomatis dengan rumus 9.1; kolom Grade diisi berdasarkan tabel 9.2; rekap CPMK dihitung dengan rumus Bagian 6.2 dokumen 055_4.

---

## 11. MODERASI, VALIDASI, DAN TINDAK LANJUT

| Aktivitas | Ketentuan |
|---|---|
| Validasi rubrik sebelum digunakan | Ditelaah Koordinator RMK dan UPM FSTI |
| Verifikasi kunci jawaban | Setiap kunci (termasuk urutan Kruskal, jejak Dijkstra, dan tabel transisi DFA) diperiksa penelaah kedua sebelum ujian |
| Moderasi antar-kelas | 10% sampel dinilai ulang oleh dosen kedua; selisih > 10 poin dibahas bersama |
| Kalibrasi penilai | Sesi kalibrasi 60 menit sebelum penilaian tugas besar, menggunakan 3 sampel jawaban |
| Dokumentasi | Lembar skor per dimensi diarsipkan bersama artefak mahasiswa |
| Revisi rubrik | Dilakukan bila > 20% mahasiswa memperoleh level 1 pada dimensi yang sama |
| Pelaporan | Rekap ke Koordinator RMK paling lambat 7 hari setelah asesmen |

---

## 12. RIWAYAT REVISI

| Versi | Tanggal | Perubahan | Penyusun |
|:---:|:---:|---|---|
| 1.0 | 07 November 2026 | Penyusunan awal; 6 rubrik (A–F) untuk 4 CPMK, dilengkapi kunci berlapis dan penanganan 2 CPL | Tim Pengembang RPS SISTEKIN |

---

*Rubrik ini merupakan turunan langsung dari CPMK/Sub-CPMK Dokumen 043 dan skema asesmen Dokumen 008. Setiap perubahan bobot atau dimensi wajib disertai revisi dokumen 055_1 dan 055_4.*
