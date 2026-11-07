# 060_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-306 — ANALISIS DAN PERANCANGAN SISTEM INFORMASI (*Information Systems Analysis and Design*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI306` · **Klaster Rubrik Master (Dok 018):** Klaster 4 (`K-4`)  
**CPL:** `CPL-02` (`KU1` = 20%) & `CPL-06` (`P2` = 80%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN KLASTER SINTESIS & REKAYASA SISTEM (`K-4`)

Selaras dengan **Dokumen 018 §3 (Klaster `K-4`)** dan **Panduan KPT 2024**, penilaian pada `STI-306` mengukur kualitas artefak cetak biru rekayasa sistem berdasarkan ketajaman analisis masalah pemangku kepentingan nyata, kepatuhan ketat terhadap standar pemodelan internasional (**IEEE 830 / ISO 29148, OMG BPMN 2.0, OMG UML 2.5, IEEE 1016**), konsistensi keterlacakan antar-model, serta akuntabilitas penguasaan individu.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `CPL-02` [C4])
**Objek Penilaian:** Bukti Elisitasi Pemangku Kepentingan + Dokumen **SRS IEEE 830 / ISO 29148** + Kuis Verifikasi Kelas.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Ketajaman Elisitasi Kebutuhan & Diagnosis Masalah PIECES**<br>(`Sub-CPMK-1.1`) | **30%** | Instrumen wawancara/observasi sangat tajam, bukti lapangan otentik, dan akar masalah pemangku kepentingan terpetakan mendalam pada kerangka PIECES. | Bukti elisitasi nyata lengkap dan analisis masalah PIECES relevan serta logis dengan konteks mitra. | Elisitasi dilakukan secara dasar, namun penggalian masalah masih di permukaan gejala (*symptom*). | Pertanyaan elisitasi dangkal/mengarahkan dan tanpa konteks pemangku kepentingan nyata. | Tidak menyertakan bukti elisitasi atau memalsukan data wawancara. |
| **2. Kualitas Spesifikasi FR & NFR Berstandar IEEE 830**<br>(`Sub-CPMK-1.2`) | **35%** | Seluruh $\ge 12$ FR dan $\ge 6$ NFR ditulis atomik, bernomor unik, bebas kata ambigu, dan memiliki target metrik kuantitatif yang 100% dapat diuji (*testable*). | FR dan NFR memenuhi struktur IEEE 830 dengan baik; hanya 1–2 butir NFR yang metrik ujinya kurang spesifik. | Pemilahan FR vs NFR cukup benar, namun masih ditemukan beberapa kata sifat kabur (*"cepat", "mudah"*) tanpa ukuran. | Mencampuradukkan FR dengan NFR atau hanya menulis daftar fitur satu baris tanpa spesifikasi perilaku. | Struktur dokumen tidak mengikuti standar SRS IEEE 830 sama sekali. |
| **3. Keterlacakan (*Traceability* RTM) & Konsistensi Kuis Verifikasi** | **20%** | Setiap FR tertelusur utuh ke masalah bisnis dan sumber *stakeholder* pada matriks RTM; hasil kuis verifikasi kelas selaras penuh. | Matriks RTM dan prioritas MoSCoW lengkap serta selaras dengan jawaban kuis verifikasi kelas. | Matriks RTM tersedia namun ada beberapa kebutuhan yang belum terpetakan ke masalah asal. | Tidak menyertakan RTM atau gagal menjelaskan isi SRS sendiri saat kuis verifikasi. | Terbukti menyalin SRS pihak lain (*plagiarisme*). |
| **4. Struktur & Tata Tulis Dokumen Rekayasa Formal** | **15%** | Dokumen sangat rapi, ruang lingkup & batasan sistem tegas, istilah teknis konsisten berstandar industri. | Dokumen rapi dan lengkap sesuai seluruh bab templat SRS IEEE 830. | Format cukup rapi tetapi masih terdapat salah ketik dan ketidakkonsistenan penomoran. | Dokumen tidak terstruktur dan banyak bagian templat SRS yang terlewat. | Naskah tidak layak baca atau tidak lengkap. |

$$\text{Skor Tugas 1} = 0,30(K_1) + 0,35(K_2) + 0,20(K_3) + 0,15(K_4)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `CPMK-2` / `CPL-06` [C4])
**Objek Penilaian:** Jawaban Ujian Tertulis Studi Kasus 150 Menit: Pemodelan **BPMN 2.0 *As-Is***, Analisis Inefisiensi, & Perancangan **BPMN 2.0 *To-Be***.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Kepatuhan Sintaks & Semantik Notasi OMG BPMN 2.0**<br>(`Sub-CPMK-2.1`) | **35%** | Penggunaan *Pool, Lane, Start/Intermediate/End Event, Task,* dan pasangan *Gateway* (`XOR/AND/OR`) 100% sah, bebas *deadlock*, serta tepat membedakan *Sequence Flow* vs *Message Flow*. | Simbol BPMN 2.0 tepat dan logis; hanya terdapat 1 kekurangtepatan minor pada pelabelan kondisi keluar *Gateway*. | Alur utama proses tergambar cukup benar, namun ada pencampuran *Sequence Flow* lintas *Pool* atau *Gateway* tidak berpasangan rapi. | Menggunakan simbol flowchart lama (bukan BPMN 2.0) atau terdapat *deadlock* fatal (membuka `XOR` menutup `AND`). | Tidak menguasai notasi dasar BPMN 2.0. |
| **2. Ketajaman Analisis Inefisiensi *As-Is* & Desain *To-Be***<br>(`Sub-CPMK-2.2`) | **35%** | Tepat membongkar $\ge 4$ *bottleneck*/aktivitas NVA pada alur *As-Is* dan merancang alur *To-Be* yang memangkas birokrasi berulang secara rasional beserta metrik efisiensi. | Analisis *bottleneck* tepat dan model *To-Be* menunjukkan peningkatan efisiensi proses yang jelas dan terukur. | Mampu menunjukkan masalah pada *As-Is*, namun model *To-Be* hanya memindahkan langkah manual ke komputer tanpa penyederhanaan alur. | Perbedaan antara model *As-Is* dan *To-Be* sangat minim dan tanpa analisis efisiensi. | Hanya menggambar salah satu model atau gagal menganalisis kasus. |
| **3. Ketepatan Ekstraksi Layanan Sistem & Hak Akses Aktor** | **20%** | Seluruh *User/Service Task* pada BPMN *To-Be* diturunkan secara presisi menjadi daftar layanan sistem informasi dan matriks peran aktor. | Pemetaan aktivitas *To-Be* ke layanan sistem sebagian besar lengkap dan konsisten. | Daftar layanan sistem dituliskan, tetapi ada beberapa *Task* pada BPMN *To-Be* yang terlewat. | Daftar fitur yang ditulis lepas dan tidak nyambung dengan diagram BPMN *To-Be*. | Bagian pemetaan layanan sistem kosong. |
| **4. Tata Letak Visual & Keterbacaan Alur Diagram** | **10%** | Alur kiri-ke-kanan sangat bersih, penamaan aktivitas berpola *Kata Kerja + Objek* konsisten, garis tidak semrawut. | Diagram rapi, mudah ditelusuri, dan pelabelan aktivitas jelas. | Diagram masih dapat dibaca meskipun terdapat beberapa garis bersilangan yang membingungkan. | Diagram sangat berantakan dan label aktivitas tidak informatif. | Diagram tidak selesai atau tak terbaca. |

$$\text{Skor UTS} = 0,35(K_1) + 0,35(K_2) + 0,20(K_3) + 0,10(K_4)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-3` / `CPL-06` [C4])
**Objek Penilaian:** Paket Pemodelan **UML 2.5** (*Use Case + Fully Dressed Spec, Activity, Class, Sequence, State Machine*) + Verifikasi.

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Ketepatan Pemodelan Fungsional (*Use Case & Activity*)**<br>(`Sub-CPMK-3.1`) | **25%** | Batas sistem, aktor, arah panah `<<include>>`/`<<extend>>`, skenario *fully dressed* (normal + eksepsi), dan *Activity Diagram* (*swimlane, fork/join*) 100% akurat. | *Use Case*, tabel skenario, dan *Activity Diagram* tepat; hanya ada kekurangan kecil pada rincian alur alternatif. | Fungsionalitas utama termodelkan baik, namun sempat terbalik arah panah `<<extend>>` atau kurang *exception flow*. | Menggambar *Use Case* seperti diagram alir berurutan (salah konsep dasar *Use Case*). | Diagram fungsional tidak sesuai standar UML 2.5. |
| **2. Ketepatan Pemodelan Struktural & Dinamis (*Class, Sequence, State*)**<br>(`Sub-CPMK-3.2`) | **35%** | *Class Diagram* lengkap (atribut, operasi, *visibility*, *multiplicity*, *composition/aggregation*), *Sequence Diagram* tepat memakai fragmen `alt`/`loop`, dan *State Machine* akurat. | Ketiga diagram struktural/dinamis benar secara notasi UML 2.5 dengan maks. 1–2 kekurangan kecil pada parameter operasi. | Kelas dan urutan interaksi dasar benar, namun *Class Diagram* belum mencantumkan metode operasi (masih mirip ERD) atau tanpa fragmen kondisi. | Banyak kesalahan notasi *lifeline*/pesan pada *Sequence Diagram* dan *State Machine* kacau. | Tidak mampu memodelkan kelas maupun interaksi objek. |
| **3. Konsistensi Silang Antar-Diagram UML (*Cross-Model Consistency*)** | **25%** | Konsistensi 100% tanpa cacat: setiap skenario *Use Case* hadir di *Sequence*, dan setiap pesan metode di *Sequence* tercatat persis pada operasi kelas tujuan di *Class Diagram*. | Konsistensi antar-diagram terjaga kuat; hanya terdapat 1–2 perbedaan penamaan metode minor. | Ide besar kelima diagram nyambung, tetapi cukup banyak pesan di *Sequence Diagram* yang tidak punya operasi padanan di *Class Diagram*. | Kelima diagram tampak berdiri sendiri-sendiri dengan nama kelas/fitur yang saling bertabrakan. | Diagram tidak saling berhubungan sama sekali. |
| **4. Kerapian Standar UML 2.5 & Penguasaan Verifikasi Kelas** | **15%** | Notasi bersih berstandar OMG UML 2.5 dan mahasiswa mampu menjelaskan alasan desain setiap relasi secara lugas saat verifikasi. | Notasi rapi dan mahasiswa menjawab pertanyaan verifikasi dengan tepat. | Notasi cukup rapi dan mampu menjelaskan bagian utama modelnya saat verifikasi. | Kesulitan menjelaskan makna simbol pada diagram buatannya sendiri. | Tidak hadir verifikasi atau terindikasi plagiasi model. |

$$\text{Skor Tugas 2} = 0,25(K_1) + 0,35(K_2) + 0,25(K_3) + 0,15(K_4)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-4` / `CPL-06` [C5])
**Objek Penilaian:** Bundel **Software Design Document (SDD — IEEE 1016)** (60% UAS) + Sidang Pertahanan Individu (40% UAS).

| Dimensi Kriteria (`K-4`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Keselarasan Solusi Arsitektur dengan Kebutuhan Bisnis & NFR**<br>(`Sub-CPMK-4.2`) | **30%** | Keputusan arsitektur, navigasi dialog berbasis peran, dan kontrol keamanan menjawab tuntas masalah bisnis mitra serta seluruh target NFR pada SRS secara rasional. | Rancangan SDD selaras baik dengan kebutuhan bisnis dan sebagian besar NFR terjawab melalui spesifikasi desain. | Rancangan menjawab kebutuhan fungsional utama, namun aspek NFR (keamanan/kinerja) hanya dibahas normatif. | Terdapat ketidaksinkronan mencolok antara masalah mitra di SRS dengan desain di SDD. | Desain tidak relevan dengan kebutuhan sistem. |
| **2. Kelengkapan & Presisi Teknis SDD (*Package, Deployment, DB, API*)**<br>(`Sub-CPMK-4.1`) | **30%** | *Package & Deployment Diagram*, pemetaan skema relasional 3NF + kamus data, dan kontrak REST API ($\ge 8$ endpoint lengkap JSON *payload* & kode HTTP) siap diimplementasikan langsung oleh programmer `STI-309`/`STI-416`. | Seluruh bab teknis SDD lengkap dan akurat; hanya terdapat kekurangan minor pada salah satu skema error JSON API. | Arsitektur paket dan skema tabel ada, namun spesifikasi kontrak API masih terlalu umum (belum merinci struktur *payload*). | Banyak komponen inti SDD kosong atau salah memetakan relasi kelas ke tabel basis data. | Dokumen SDD sangat dangkal dan tidak layak dijadikan acuan konstruksi. |
| **3. Keterlacakan Ujung-ke-Ujung (*End-to-End Traceability*) & Kerja Tim** | **20%** | Matriks keterlacakan menautkan `SRS ↔ BPMN ↔ UML ↔ Tabel DB ↔ API` 100% utuh tanpa *orphan requirement*; kontribusi seluruh anggota tim merata dan terdokumentasi. | Keterlacakan antar-bab SDD konsisten baik dan kolaborasi tim berjalan seimbang. | Matriks keterlacakan tersedia namun masih ada beberapa ketidaksinkronan nama kolom/atribut antar-bab. | Terdeteksi timpang kontribusi (*free-rider*) dan banyak inkonsistensi antar-anggota di dalam 1 SDD. | Tidak ada matriks keterlacakan dan kerja tim gagal. |
| **4. Mutu Dokumen IEEE 1016 & Ketajaman Pertahanan Sidang Individu** | **20%** | Naskah SDD berstandar profesional industri dan mahasiswa mampu mempertahankan alasan arsitektural serta menjawab uji silang penguji secara kritis dan meyakinkan. | Dokumen rapi sesuai IEEE 1016 dan mahasiswa menjawab pertanyaan penguji atas modulnya dengan baik. | Presentasi cukup jelas dan mahasiswa mampu menjelaskan alur dasar bagian yang dikerjakannya. | Gagap menjelaskan hubungan modulnya dengan arsitektur tim saat diuji individu. | Tidak hadir sidang atau gagal mempertanggungjawabkan isi SDD. |

$$\text{Skor UAS} = 0,30(K_1) + 0,30(K_2) + 0,20(K_3) + 0,20(K_4)$$

---

## BAGIAN III — RUBRIK FORMATIF AKTIVITAS KELAS & KLINIK PEMODELAN

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Partisipasi *Peer-Audit* SRS & Model** | Aktif menemukan ambiguitas SRS atau celah konsistensi BPMN/UML rekan secara konstruktif berbasis aturan standar. | Memberikan masukan telaah sejawat yang relevan pada sesi lokakarya kelas. | Hadir mengikuti lokakarya namun pasif memberi umpan balik. | Tidak menyiapkan draf artefak mingguan untuk sesi klinik kelas. |
| **Kepatuhan *Boundary Guardrail* Desain** | Fokus tajam pada ketelitian spesifikasi analisis & arsitektur tanpa melenceng ke koding prematur. | Mematuhi batas artefak analisis-desain sesuai arahan dosen. | Kadang mencampur istilah kode implementasi spesifik ke dalam diagram konseptual. | Mengabaikan pemodelan dan langsung membuat tangkapan layar kode seadanya. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-306` (`CPL-02` & `CPL-06` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa mampu berperan layaknya *Junior System Analyst* profesional: mengelisitasi kebutuhan kompleks menjadi SRS IEEE 830 yang presisi, merekayasa ulang proses bisnis BPMN 2.0 secara tajam, serta merancang paket UML 2.5 dan SDD IEEE 1016 yang 100% konsisten dan siap diimplementasikan. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa menguasai dengan sangat baik penyusunan SRS, pemodelan BPMN 2.0 *As-Is/To-Be*, kelima diagram inti UML 2.5, dan penyusunan dokumen SDD dengan keterlacakan yang solid. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi ambang ketuntasan minimal OBE ($\ge 65,0$) dalam menyusun spesifikasi SRS dasar, memodelkan BPMN 2.0 dan UML 2.5 standar, serta merakit dokumen desain sistem. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih menghasilkan spesifikasi kebutuhan yang ambigu, sering melanggar aturan sintaks BPMN/UML, dan menyusun SDD yang belum konsisten antar-bagiannya. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menghasilkan artefak analisis dan perancangan sistem yang valid atau melanggar integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-306` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menggali kebutuhan fungsional dan non-fungsional dari pemangku kepentingan nyata secara sistematis. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menyusun dokumen spesifikasi kebutuhan perangkat lunak (SRS) yang terukur sesuai standar IEEE 830. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu memodelkan proses bisnis lintas-peran menggunakan standar notasi BPMN 2.0 tanpa cacat sintaks. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menganalisis inefisiensi proses *As-Is* dan merancang proses bisnis *To-Be* yang lebih efisien. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu merancang *Use Case Diagram*, spesifikasi skenario naratif, dan *Activity Diagram* UML 2.5 secara konsisten. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu merancang *Class Diagram*, *Sequence Diagram*, dan *State Machine Diagram* yang saling selaras. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |
| 7 | Saya mampu menyusun spesifikasi arsitektur paket, pemetaan skema basis data, dan kontrak REST API di dalam dokumen SDD. | `Sub-CPMK-4.1` | 1 – 2 – 3 – 4 – 5 |
| 8 | Saya mampu memastikan keterlacakan utuh desain perangkat lunak terhadap kebutuhan bisnis organisasi. | `Sub-CPMK-4.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-306`)

```text
==============================================================================================================================
       LEMBAR REKAPITULASI PENILAIAN OBE — STI-306 ANALISIS DAN PERANCANGAN SISTEM INFORMASI (3 SKS TEORI)
==============================================================================================================================
Semester / TA  : Semester 3 (Ganjil) / 2026-2027     CPL Dibebankan : CPL-02 (KU1: 20%) & CPL-06 (P2: 80%) [Level: Reinforce]
Klaster Rubrik : K-4 (Sintesis & Rekayasa Sistem)    Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)    | UTS (30%)   | T2 (20%)    | UAS (30%)   | NA    | CPL-02 | CPL-06 | Huruf
   |           |                  | [CPMK-1:C4] | [CPMK-2:C4] | [CPMK-3:C4] | [CPMK-4:C5] | Akhir | (20%)  | (80%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 85.0        | 82.0        | 86.0        | 88.0        | 85.20 | 85.00  | 85.25  | A
2  | 250101002 | [Nama Mhs 2]     | 76.0        | 74.0        | 75.0        | 78.0        | 75.80 | 76.00  | 75.75  | B
3  | 250101003 | [Nama Mhs 3]     | 68.0        | 66.0        | 70.0        | 68.0        | 67.80 | 68.00  | 67.75  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 76.33       | 74.00       | 77.00       | 78.00       | 76.27 | 76.33  | 76.25  | >=65:100%
==============================================================================================================================
```
