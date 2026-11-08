# 096_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STB-703 — Arsitektur Enterprise (TOGAF)

**Identitas:** `STB-703` Arsitektur Enterprise (TOGAF) · Semester 7 · 3 SKS (Teori) · Prasyarat `STI-306` · PL PL-2, PL-4 · PEO PEO-1, PEO-2 · IRM M.

## Identitas dan pengesahan

Prodi S1 SISTEKIN FSTI UWG. Koordinator, dosen dan tanggal pengesahan diisi oleh program studi. Beban mingguan: TM 150 menit + PT 180 menit + BM 180 menit. PT = tugas terstruktur; BM = belajar mandiri.

## CPL dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| CPL-06 (P2) | Menguasai konsep teoretis sistem informasi, analisis & perancangan sistem, arsitektur enterprise, metodologi pengembangan perangkat lunak, serta proses bisnis organisasi untuk transformasi digital. | M |
| CPL-07 (P3) | Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (*cloud*), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi. | M |
| CPL-12 (KK4) | Mampu merancang tata kelola TI (*IT Governance*), melakukan audit sistem informasi, serta memastikan kepatuhan terhadap standar industri dan manajemen risiko (COBIT, ITIL, ISO 27001). | M |

## CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD Dok 043 | Bloom | CPL |
| --- | --- | --- | --- |
| CPMK-1 | Mahasiswa (*A*) mampu **menguraikan** siklus Architecture Development Method (ADM Fase Preliminary s.d. H) (*B*) berdasarkan standar The Open Group Architecture Framework (TOGAF) (*C*) secara komprehensif (*D*). | C2 | `CPL-06` (`P2`) |
| CPMK-2 | Mahasiswa (*A*) mampu **memodelkan** 4 pilar arsitektur enterprise (Business, Data, Application, Technology Architecture) (*B*) menggunakan bahasa pemodelan standar ArchiMate (*C*) secara konsisten (*D*). | C4 | `CPL-06` (`P2`), `CPL-07` (`P3`), `CPL-12` (`KK4`) |
| CPMK-3 | Mahasiswa (*A*) mampu **menyusun** dokumen cetak biru Architecture Definition Document (ADD) (*B*) dengan analisis kesenjangan (*Gap Analysis As-Is vs To-Be*) dan peta jalan migrasi (*Migration Roadmap*) (*C*) secara profesional (*D*). | C5 | `CPL-12` (`KK4`) |

| Sub-CPMK | Kompetensi Dok 043 | CPMK sumber | Bloom |
| --- | --- | --- | --- |
| Sub-CPMK-1.1 | Menjelaskan pendekatan TOGAF ADM (Architecture Vision hingga Migration Planning). | CPMK-1 | C2 |
| Sub-CPMK-1.2 | Menjelaskan peran model arsitektur enterprise pada organisasi. | CPMK-1 | C2 |
| Sub-CPMK-2.1 | Memodelkan arsitektur business dan data menggunakan ArchiMate. | CPMK-2 | C4 |
| Sub-CPMK-2.2 | Memodelkan arsitektur application dan technology menggunakan ArchiMate. | CPMK-2 | C4 |
| Sub-CPMK-3.1 | Menyusun dokumen enterprise architecture yang selaras strategi organisasi. | CPMK-3 | C5 |
| Sub-CPMK-3.2 | Mengevaluasi kesenjangan arsitektur (gap analysis) dan rencana migrasi. | CPMK-3 | C5 |

## Matriks CPL–CPMK dan bobot asesmen

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-06` (`P2`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-06` (`P2`), `CPL-07` (`P3`), `CPL-12` (`KK4`) | — | 30% | 20% | — | 50% |
| CPMK-3 | `CPL-12` (`KK4`) | — | — | — | 30% | 30% |
| Total | — | 20% | 30% | 20% | 30% | 100% |

Bobot merupakan rancangan penilaian MK; CPMK yang mendukung lebih dari satu CPL tidak menggandakan nilai akhir. Nilai CPL tingkat prodi mengikuti formula Dok 008.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (20%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 70% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana 16 pertemuan

| Mg | Kemampuan | Materi | Metode | Beban | Asesmen |
| --- | --- | --- | --- | --- | --- |
| 1 | Mampu menguraikan hakikat Enterprise Architecture dan framework besar (C2) | Pengantar Enterprise Architecture (EA), Mengapa Organisasi Butuh EA?, TOGAF vs Zachman | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 2 | Mampu menguraikan struktur TOGAF ADM (Architecture Development Method) (C2) | TOGAF ADM: Siklus Iteratif 8 Fase, Architecture Continuum, Repository | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 3 | Mampu menyusun Fase Preliminary: Prinsip Arsitektur & Penyesuaian Framework (C4) | TOGAF Preliminary Phase: Prinsip Arsitektur Enterprise, Architecture Governance | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 4 | Mampu menyusun Fase A: Architecture Vision & Statement of Architecture Work (C4) | Fase A (Architecture Vision): Stakeholder Map, Nilai Bisnis, Vision Scope | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Tugas 1 20% |
| 5 | Mampu memodelkan elemen ArchiMate: Business Layer (Aktor, Proses, Peran) (C3) | Bahasa Pemodelan ArchiMate: Konsep Metamodel, Lapisan Bisnis & Notasi | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 6 | Mampu merancang Fase B: Business Architecture As-Is dan To-Be (C4) | Fase B (Business Architecture): Pemodelan Proses Bisnis, Kapabilitas Organisasi | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 7 | Mampu merancang Fase C: Data Architecture & Pemodelan Entitas Logis (C4) | Fase C (Information Systems - Data): Logical Data Entities, Data Flow ArchiMate | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 8 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Tertulis TOGAF ADM Fase Preliminary, Vision, & Arsitektur Bisnis/Data | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | UTS 30% |
| 9 | Mampu merancang Fase C: Application Architecture & Integrasi Antarmuka (C4) | Fase C (Information Systems - App): Komponen Aplikasi, Inter-Service API | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 10 | Mampu merancang Fase D: Technology Architecture Infrastruktur & Cloud (C4) | Fase D (Technology Architecture): Node Server, Jaringan, Perangkat Lunak Sistem | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 11 | Mampu melakukan Gap Analysis As-Is vs To-Be lintas 4 pilar arsitektur (C4) | Gap Analysis: Matriks Identifikasi Kesenjangan (Eliminasi, Penggantian, Baru) | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 12 | Mampu menyusun Fase E: Opportunities & Solutions dan Work Packages (C4) | Fase E (Opportunities & Solutions): Paket Kerja, Arsitektur Transisi (*Transition*) | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Tugas 2 20% |
| 13 | Mampu merancang Fase F: Migration Planning & Matriks Prioritisasi (C5) | Fase F (Migration Planning): Analisis Biaya/Manfaat, Matriks Risiko-Nilai | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 14 | Mampu menguraikan Fase G & H: Implementation Governance & Change Mgmt (C2) | Fase G & H: Tata Kelola Implementasi Arsitektur, Kepatuhan, & Manajemen Perubahan | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 15 | Mampu menyusun dokumen Architecture Definition Document (ADD) lengkap (C5) | Penyusunan Cetak Biru ADD & Simulasi Presentasi Transformasi Digital | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif |
| 16 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Ujian Cetak Biru Enterprise Architecture (ADD) & Model ArchiMate Lengkap | Analisis kasus / diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | UAS 30% |

## Ringkasan asesmen

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Jelaskan ADM dan rancang visi serta stakeholder arsitektur organisasi. Bukti: peta stakeholder, visi dan fase ADM |
| UTS | 8 | 30% | CPMK-2 | Modelkan arsitektur bisnis dan data menggunakan ArchiMate. Bukti: diagram model dan deskripsi hubungan |
| Tugas 2 | 12 | 20% | CPMK-2 | Lengkapi model aplikasi dan teknologi serta analisis gap awal. Bukti: diagram empat lapisan dan matriks gap |
| UAS | 16 | 30% | CPMK-3 | Susun ADD, gap as-is/to-be dan roadmap migrasi. Bukti: model lengkap, dokumen ADD dan roadmap |

## Pustaka utama dan pendukung

[The Open Group TOGAF Standard](https://www.opengroup.org/togaf) dan [ArchiMate](https://www.opengroup.org/archimate-forum/archimate-overview).

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS04` *Enterprise Architecture*, `BK-IT07` *System Integration*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur Enterprise Korporat, Framework TOGAF (Architecture Development Method / ADM: Tahap A s.d. H), 4 Lapisan Arsitektur (Bisnis, Data, Aplikasi, Teknologi), Migration Planning.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang perumusan kebijakan tata ruang perkotaan publik (Smart City), konfigurasi teknis Docker/Kubernetes di lapangan, koding modul program.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menyusun blueprint arsitektur korporat terpadu yang memandu seluruh transformasi digital organisasi.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
