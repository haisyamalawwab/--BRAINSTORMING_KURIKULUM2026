# 072_1 — RENCANA PEMBELAJARAN SEMESTER (RPS) BERBASIS OBE
## STI-418 — DASAR KEAMANAN INFORMASI (*Fundamentals of Information Security*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  
**Fakultas:** Fakultas Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  
**Kurikulum:** Kurikulum OBE SISTEKIN 2026 (Permendikbudristek No. 53/2023 · Panduan KPT Dikti 2024 · APTIKOM OBE SI v2.0 / IS2020 & IT2017)  
**Nomor Dokumen:** `071030.B4.5.6.RPS-STI418`  
**Tanggal Penyusunan:** 07 November 2026  

---

## HALAMAN 1 — IDENTITAS MATA KULIAH & OTORISASI

| Atribut | Spesifikasi Resmi (Selaras Dokumen 003, 004, 005, 007, 008, 018, 037, & 043) |
|---|---|
| **Nama Mata Kuliah (ID / EN)** | Dasar Keamanan Informasi / *Fundamentals of Information Security* |
| **Kode Mata Kuliah** | `STI-418` *(Kurikulum OBE SISTEKIN 2026)* |
| **Rumpun Mata Kuliah** | Infrastruktur TI, Komputasi Awan & Keamanan (*Core STI*) |
| **Bobot SKS & Tipe** | **2 SKS (`Teori`)** (`T = 2, P = 0`) — Tatap Muka & Demonstrasi Keamanan Terisolasi `2×50' = 100'`, Penugasan Terstruktur `2×60' = 120'`, Belajar Mandiri `2×60' = 120'` per pekan |
| **Semester / Tahun Akademik** | Semester 4 (Genap) — Tahap Penguatan Jaminan Keamanan Informasi (*Reinforce*) |
| **Mata Kuliah Prasyarat** | `STI-312` Jaringan Komputer & Komunikasi Data |
| **Mitra Ko-Semester & Hilir (*Handoff*)** | Bersinergi dengan `STI-416` Pengembangan Web Back End & `STI-417` Komputasi Awan; menjadi fondasi wajib bagi `STI-519` Keamanan Informasi Lanjut (Sem 5), `STB-501` Keamanan Jaringan dan Forensik Digital, `STB-602` Keamanan Aplikasi dan Pengujian Penetrasi (Ethical Hacking), & `STB-701` Tata Kelola Infrastruktur & Audit Keamanan TI |
| **Status pada Peta IRM (Dok 004)** | **R (*Reinforce*)** pada `CPL-07` (`P3` = **50%**) dan `CPL-11` (`KK3` = **50%**) |
| **Klaster Rubrik Asesmen (Dok 018)** | **Klaster 1 (`K-1`)** — Fondasi Sains, Matematika & Komputasi Dasar (Bobot MK `Teori`: Tugas 1 `20%` · UTS `30%` · Tugas 2 `20%` · UAS `30%`) |
| **Pengembang RPS** | Tim KBK Infrastruktur Jaringan, Cloud & Keamanan Siber |
| **Koordinator RMK** | Dr. Istiadi, S.T., M.T. |
| **Ketua Program Studi** | Ahmad Fairuzabadi, S.Kom., M.Kom. |
| **Dosen Pengampu** | 1. [Nama Dosen Pengampu 1] *(Koordinator MK)*<br>2. [Nama Dosen Pengampu 2] |

---

## HALAMAN 2 — CAPAIAN PEMBELAJARAN, KORELASI, DESKRIPSI, & PUSTAKA

### 1. Capaian Pembelajaran Lulusan (CPL) yang Dibebankan pada Mata Kuliah (Dokumen 003 & 004)

| Kode Baku (Alias) | Ranah | Rumusan Resmi CPL Kurikulum OBE SISTEKIN 2026 (Verbatim Dokumen 003) | Level IRM | Bobot Kontribusi MK |
|:---:|---|---|:---:|:---:|
| **`CPL-07`** (`P3`) | Pengetahuan | Menguasai arsitektur komputer, sistem operasi, jaringan komputer, komputasi awan, serta prinsip keamanan informasi dan manajemen risiko siber. | **R** (*Reinforce*) | **50%** |
| **`CPL-11`** (`KK3`) | Keterampilan Khusus | Mampu merancang, mengkonfigurasi, mengamankan, dan mengelola infrastruktur jaringan, layanan komputasi awan (*cloud*), serta sistem keamanan informasi organisasi. | **R** (*Reinforce*) | **50%** |

### 2. Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Level Taksonomi Bloom (Verbatim Dokumen 043 & 007)

| Kode CPMK | Rumusan Capaian Pembelajaran Mata Kuliah (ABCD) | Level Bloom | CPL Didukung | Poros Evaluasi (Bobot) |
|:---:|---|:---:|:---:|:---:|
| **`CPMK-1`** | Mahasiswa (*A*) mampu **menerapkan prinsip dasar keamanan informasi (*CIA Triad*) serta mekanisme kriptografi simetris (*AES*), asimetris (*RSA*), fungsi *hash* (*SHA-256*), dan *digital signature*** (*B*) untuk perlindungan kerahasiaan dan integritas data (*C*) secara tepat (*D*). | **C3** (*Apply*) | `CPL-07` (`P3`) | **Tugas 1 (20%) + UTS Bagian A (15%) = 35%** |
| **`CPMK-2`** | Mahasiswa (*A*) mampu **menganalisis ancaman dan kerentanan aplikasi web berdasarkan *OWASP Top 10* serta menerapkan mekanisme kontrol akses (*RBAC*)** dan pertahanan jaringan dasar (*B*) menggunakan pemindai kerentanan resmi pada lingkungan uji terisolasi (*C*) secara bertanggung jawab (*D*). | **C4** (*Analyze*) | `CPL-11` (`KK3`) | **UTS Bagian B (15%) + Tugas 2 (20%) = 35%** |
| **`CPMK-3`** | Mahasiswa (*A*) mampu **mengevaluasi risiko insiden siber serta menilai kepatuhan praktik keamanan informasi organisasi** (*B*) mengacu pada kerangka kerja standar internasional (**NIST CSF** dan **ISO/IEC 27001**) (*C*) secara sistematis (*D*). | **C5** (*Evaluate*) | `CPL-07` (`P3`) & `CPL-11` (`KK3`) | **UAS — Pekan 16 (30%)** |

### 3. Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) — Verbatim Dokumen 043

| Kode Sub-CPMK | Rumusan Kompetensi Spesifik | Mendukung CPMK | Level Bloom | Pekan |
|:---:|---|:---:|:---:|:---:|
| **`Sub-CPMK-1.1`** | Menerapkan prinsip **CIA Triad** serta kriptografi simetris (**AES**) dan asimetris (**RSA**) untuk kerahasiaan data. | `CPMK-1` | **C3** | Mg 1–4 |
| **`Sub-CPMK-1.2`** | Menerapkan fungsi *hash* (**SHA-256 / HMAC**), **digital signature**, dan sertifikat **PKI / TLS** untuk integritas & nir-penyangkalan. | `CPMK-1` | **C3** | Mg 5–6 |
| **`Sub-CPMK-2.2`** | Menerapkan mekanisme autentikasi (**MFA**), model kontrol akses (**DAC, MAC, RBAC, ABAC**), dan pertahanan perimeter (*Firewall/IDS/IPS*). | `CPMK-2` | **C4** | Mg 6–7 |
| **`Sub-CPMK-2.1`** | Menganalisis kerentanan aplikasi web **OWASP Top 10** dengan pemindai kerentanan (*OWASP ZAP*) serta merumuskan remediasinya. | `CPMK-2` | **C4** | Mg 9–12 |
| **`Sub-CPMK-3.1`** | Mengevaluasi risiko dan respons insiden keamanan menggunakan kerangka **NIST Cybersecurity Framework (CSF 2.0)**. | `CPMK-3` | **C5** | Mg 13–14 |
| **`Sub-CPMK-3.2`** | Menilai kontrol keamanan informasi menggunakan standar **ISO/IEC 27001:2022** serta kepatuhan **UU PDP No. 27/2022**. | `CPMK-3` | **C5** | Mg 14–15 |

### 4. Peta Analisis Pembelajaran (*Instructional Analysis* — Standar KPT 2024)

```text
[CPMK-3: Evaluasi Risiko Insiden & Praktik Keamanan Organisasi Berbasis NIST CSF 2.0 & ISO/IEC 27001 (C5) — Mg 13–16 (UAS 30%)]
      ▲  (Sub-CPMK-3.1: Risk Assessment ALE & NIST CSF 2.0 Govern–Recover | Sub-CPMK-3.2: ISO/IEC 27001 Annex A & UU PDP Audit)
      │
[CPMK-2: Kontrol Akses (RBAC/MFA), Pertahanan Perimeter, & Analisis Kerentanan Web OWASP Top 10 (C4) — Mg 6–12 (UTS B 15% + T2 20%)]
      ▲  (Sub-CPMK-2.2: MFA, RBAC, Firewall/IDS/IPS [Mg 6–7] | Sub-CPMK-2.1: Ethical Vulnerability Assessment OWASP ZAP [Mg 9–12])
      │
[CPMK-1: Prinsip CIA Triad & Kriptografi Terapan (AES, RSA, SHA-256, Digital Signature, PKI/TLS) (C3) — Mg 1–6 (T1 20% + UTS A 15%)]
         (Sub-CPMK-1.1: Threat Landscape, CIA Triad, AES-GCM & RSA [Mg 1–4] | Sub-CPMK-1.2: SHA-256, HMAC, Signature & TLS [Mg 5–6])
      ▲
[Fondasi Prasyarat: STI-312 Jaringan Komputer & Komunikasi Data (TCP/IP, Port, DNS, HTTP/TLS) + Aritmetika Modular STI-204]
```

### 5. Matriks Korelasi CPL – CPMK – Sub-CPMK – Instrumen & Bobot Penilaian

| CPL | CPMK | Sub-CPMK Terkait | Tugas 1 (Mg 4) | UTS (Mg 8) | Tugas 2 (Mg 12) | UAS (Mg 16) | Total Bobot CPMK | Kontribusi ke CPL |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **`CPL-07`** (`P3`) | **`CPMK-1`** | `Sub-CPMK-1.1` (T1: 20%), `Sub-CPMK-1.2` (UTS A: 15%) | **20%** | **15%** | — | — | **35%** | **`CPL-07` = 50%** *(20%+15%+15%)* |
| **`CPL-11`** (`KK3`) | **`CPMK-2`** | `Sub-CPMK-2.2` (UTS B: 15%), `Sub-CPMK-2.1` (T2: 20%) | — | **15%** | **20%** | — | **35%** | **`CPL-11` = 50%** *(15%+20%+15%)* |
| **`CPL-07`** (`15%`) & **`CPL-11`** (`15%`) | **`CPMK-3`** | `Sub-CPMK-3.1` (`P3`: 15%), `Sub-CPMK-3.2` (`KK3`: 15%) | — | — | — | **30%** | **30%** | *(Terdisagregasi 15% `P3` + 15% `KK3`)* |
| **Total** | **3 CPMK** | **6 Sub-CPMK** | **20%** | **30%** | **20%** | **30%** | **100%** | **100%** |

> **Kepatuhan IKU 7 ($\ge 50\%$ Klaster `K-1` Dok 018; Target Dok 004 `55%`):** `Tugas 1 (20% — Case-Based CIA Triad & Applied Cryptographic Protection) + Tugas 2 (20% — Case-Based OWASP Top 10 Vulnerability Assessment & Remediation) + UAS (30% — Case/Project-Based Incident Risk & NIST CSF / ISO 27001 Security Gap Evaluation)` = **70%** *(melampaui target 55% Dokumen 004)*.

### 6. Deskripsi Singkat Mata Kuliah & *Boundary Guardrails* (Dokumen 037 & 043)

Mata kuliah `STI-418 Dasar Keamanan Informasi` (2 SKS `Teori`) menanamkan pola pikir defensif (*security-by-design*), etika profesional keamanan siber, dan penguasaan kontrol perlindungan informasi bagi setiap calon arsitek maupun pengembang sistem informasi. Mahasiswa menguasai pilar **CIA Triad** (*Confidentiality, Integrity, Availability*) beserta *Authenticity & Non-Repudiation*, lanskap ancaman siber modern, penerapan kriptografi standar industri (**AES**, **RSA**, pertukaran kunci *Diffie-Hellman*, fungsi *hash* **SHA-256 / HMAC**, **Digital Signature**, dan rantai kepercayaan **PKI / TLS 1.3**), autentikasi multi-faktor (**MFA**), model kontrol akses (**DAC, MAC, RBAC, ABAC**), pertahanan jaringan dasar (*Firewall, VPN, IDS/IPS*), analisis kerentanan aplikasi web **OWASP Top 10** menggunakan pemindai kerentanan resmi pada target lokal legal, serta evaluasi manajemen risiko dan kepatuhan berdasarkan **NIST CSF 2.0**, **ISO/IEC 27001:2022**, dan **UU Pelindungan Data Pribadi (UU No. 27 Tahun 2022)**.

* **🟢 IN-SCOPE (Wajib Diajarkan):** **CIA Triad**, taksonomi ancaman & *Social Engineering*, kriptografi terapan (**AES, RSA, SHA-256, Digital Signature, PKI/TLS**), **MFA & RBAC**, konsep *Firewall/VPN/IDS/IPS*, *Vulnerability Assessment* dasar atas **OWASP Top 10** di lingkungan lokal terisolasi, kalkulasi risiko (*Asset, Threat, Vulnerability, Impact, ALE*), serta kerangka **NIST CSF 2.0** & **ISO/IEC 27001:2022**.
* **❌ OUT-OF-SCOPE (Dilarang Diajarkan — Anti-Overlap Dok 037):**
  1. Dilarang mengajarkan eksploitasi biner tingkat memori (*buffer overflow*), *reverse engineering malware*, *proactive threat hunting*, maupun operasi *SIEM/SOAR* lanjut (ranah **`STI-519 Keamanan Informasi Lanjut`** dan **`STB-501 Keamanan Jaringan dan Forensik Digital`**).
  2. Dilarang melakukan pengujian penetrasi aktif pada sistem eksternal/publik di luar target lab lokal legal (ranah etika hukum UU ITE; pengujian penetrasi mendalam dipelajari di **`STB-602 Keamanan Aplikasi dan Pengujian Penetrasi`**).
  3. Dilarang membahas audit tata kelola TI korporat COBIT 2019 menyeluruh (ranah **`STB-701 Tata Kelola Infrastruktur & Audit Keamanan TI`**).
* **🔄 HANDOFF ANCHOR:** Menjadi pijakan wajib menuju **`STI-519 Keamanan Informasi Lanjut`**, **`STB-501`**, dan **`STB-602`**.

### 7. Bahan Kajian (*Body of Knowledge*) & Daftar Pustaka

* **Bahan Kajian Primer:** `BK-IS06` (*Information Security & Risk Management*) & `BK-IT06` (*Cybersecurity Principles*).

**Pustaka Utama:**
1. Whitman, M. E., & Mattord, H. J. (2022). *Principles of Information Security* (7th ed.). Cengage Learning.
2. Stallings, W., & Brown, L. (2023). *Computer Security: Principles and Practice* (5th ed.). Pearson.

**Pustaka Pendukung:**
3. NIST. (2024). *The NIST Cybersecurity Framework (CSF) 2.0*. National Institute of Standards and Technology.
4. ISO/IEC. (2022). *ISO/IEC 27001:2022 — Information security, cybersecurity and privacy protection — Information security management systems*.
5. OWASP Foundation. (2021/2025). *OWASP Top 10 Web Application Security Risks* & Republik Indonesia, *UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)*.

---

## HALAMAN 3–7 — MATRIKS RENCANA PEMBELAJARAN 16 PERTEMUAN

| Mg Ke- | Kemampuan Akhir Tiap Tahapan Belajar (Sub-CPMK) | Indikator Penilaian | Kriteria & Teknik Penilaian | Bentuk, Metode & Pengalaman Belajar (Luring: Tatap Muka & Demo Keamanan) `[Estimasi Waktu]` | Pengalaman Belajar Daring / LMS Edlink | Materi Pembelajaran `[Rujukan]` | Bobot (%) |
|:---:|---|---|---|---|---|---|:---:|
| **1** | **Orientasi, Pakta Etika Siber, & `Sub-CPMK-1.1` (Bagian I):** Menganalisis pilar **CIA Triad** (*Confidentiality, Integrity, Availability* + *Non-Repudiation*) & taksonomi pelaku/ancaman siber [C2→C3] | 1.1.1 Ketepatan memetakan dampak sebuah insiden nyata (*ransomware* pusat data / kebocoran data pelanggan / DDoS) terhadap dimensi **C, I,** dan **A**.<br>1.1.2 Kepatuhan menandatangani Pakta Etika Keamanan Siber (hanya menguji pada lingkungan *sandbox* berizin!). | **Kriteria:** Pemetaan dampak CIA Triad tepat dan memahami konsekuensi hukum UU ITE & UU PDP.<br>**Teknik:** Bedah kasus insiden siber nasional di kelas. | **Interactive Case Lecture**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Penandatanganan Pakta Etika Keamanan Siber & kontrak belajar di LMS Edlink. | Pilar **CIA Triad**, *Parkerían Hexad*, Lanskap Ancaman (*Phishing, Ransomware, Insider Threat*), & Etika Hukum Siber `[1] Bab 1–2; [2] Bab 1` | — |
| **2** | **`Sub-CPMK-1.1` (Bagian II):** Menerapkan **Kriptografi Simetris Modern (*AES*)**, mode operasi blok (*ECB yang bocor pola vs CBC vs **AES-GCM** Authenticated Encryption*), & manajemen kunci [C3] | 1.1.3 Ketepatan mendemonstrasikan mengapa mode `AES-ECB` membocorkan siluet gambar penguin dan mengapa **AES-256-GCM** wajib menggunakan *Nonce/IV* unik serta menyimpan kunci di luar kode sumber. | **Kriteria:** Enkripsi-dekripsi berkas/data dengan `OpenSSL` / Python `cryptography` berjalan akurat dan aman.<br>**Teknik:** Demonstrasi & latihan enkripsi simetris **AES**. | **Interactive Crypto Demo**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Kuis perbedaan *Stream vs Block Cipher* & bahaya *ECB/Key Reuse* di LMS Edlink. | Konsep *Confusion & Diffusion*, Standar **AES**, Bahaya Mode ECB vs Keunggulan **AES-GCM**, & Perlindungan *Data-at-Rest* `[2] Bab 2 & 20` | — |
| **3** | **`Sub-CPMK-1.1` (Bagian III):** Menerapkan **Kriptografi Asimetris (*RSA & ECC*)** serta skema **Hybrid Encryption** untuk distribusi kunci rahasia melalui saluran tak-aman [C3] | 1.1.4 Ketepatan menjelaskan masalah distribusi kunci simetris dan bagaimana pasangan *Public Key & Private Key* (**RSA** — berakar pada aritmetika modular `STI-204`!) berpadu dengan **AES** dalam *Hybrid Encryption*. | **Kriteria:** Pembangkitan pasangan kunci RSA/Ed25519 dan pembungkusan kunci sesi simetris dilakukan secara benar.<br>**Teknik:** Latihan pembangkitan kunci publik-privat dengan `OpenSSL` & rilis resmi **Tugas 1 (RTM-1)**. | **Problem-Based Crypto Lecture**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi studi kasus perlindungan kriptografi **Tugas 1 (RTM-1)** di LMS Edlink. | Masalah Pertukaran Kunci, Kriptografi Kunci Publik (**RSA**, *Diffie-Hellman*, *Elliptic Curve*), & Skema **Hybrid Encryption** `[2] Bab 2 & 21` | — |
| **4** | **`Sub-CPMK-1.1` (Integrasi Perlindungan Data):** Klasifikasi sensitivitas data (*Publik, Internal, Rahasia, Data Pribadi Spesifik UU PDP*) & strategi enkripsi *Data-at-Rest vs Data-in-Transit* [C3]<br>*(+ Evaluasi Tugas 1 atas `Sub-CPMK-1.1`)* | 1.1.5 Ketepatan merancang dan menguji skema perlindungan kriptografi simetris/asimetris yang tepat bagi aset data sensitif organisasi. | **Kriteria:** **Rubrik Analitik Tugas 1 (`K-1`)**.<br>**Teknik:** Pengumpulan & Verifikasi Studi Kasus Implementasi **AES & RSA** (**Tugas 1**). | **Case Review & Verifikasi Tugas 1**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas **Tugas 1 (`Sub-CPMK-1.1`)** di LMS Edlink. | Klasifikasi Data Sensitif, Manajemen Siklus Kunci (*Key Rotation, KMS*), & Verifikasi **Tugas 1** `[1] Bab 8; [5]` | **20%**<br>*(Tugas 1 — `CPMK-1`)* |
| **5** | **`Sub-CPMK-1.2` (Bagian I):** Menerapkan fungsi *hash* kriptografis (**SHA-256 / SHA-3**), *Avalanche Effect*, **HMAC**, & pembuatan/verifikasi **Digital Signature** [C3] | 1.2.1 Ketepatan membuktikan sifat satu-arah dan ketahanan tumbukan **SHA-256** (serta mengapa MD5/SHA-1 sudah usang!).<br>1.2.2 Ketepatan membedakan alur enkripsi asimetris (kunci publik penerima) vs **Digital Signature** (ditandatangani dengan **kunci privat pengirim**, diverifikasi dengan **kunci publik pengirim**!). | **Kriteria:** Tidak tertukar arah pemakaian kunci publik-privat antara enkripsi dan tanda tangan digital.<br>**Teknik:** Latihan verifikasi integritas berkas SHA-256 & penandatanganan dokumen digital. | **Interactive Integrity Studio**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Kuis perbedaan *Hash* vs *HMAC* vs *Digital Signature* di LMS Edlink. | Fungsi *Hash* (**SHA-256**), *Message Authentication Code* (**HMAC**), & Nir-Penyangkalan dengan **Digital Signature** `[2] Bab 2 & 21` | — |
| **6** | **`Sub-CPMK-1.2` (Bagian II) & `Sub-CPMK-2.2` (Bagian I):** Rantai kepercayaan **PKI (X.509 Certificate Authority & TLS 1.3 Handshake)** serta mekanisme **Multi-Factor Authentication (MFA)** [C3→C4] | 1.2.3 Ketepatan menginspeksi sertifikat X.509 HTTPS situs web untuk mendeteksi serangan *Man-in-the-Middle (MitM)*.<br>2.2.1 Ketepatan mengevaluasi tiga faktor autentikasi (*Something You Know, Have, Are*) pada **TOTP / Passkeys WebAuthn**. | **Kriteria:** Mampu menelusuri *Certificate Chain* TLS 1.3 dan menjelaskan ketahanan *Phishing-Resistant MFA*.<br>**Teknik:** Inspeksi sertifikat TLS peramban & analisis faktor MFA. | **TLS & Authentication Lecture**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Panduan inspeksi `openssl s_client` di LMS Edlink. | **Public Key Infrastructure (PKI)**, Sertifikat **X.509**, Cara Kerja **TLS 1.3**, & **Multi-Factor Authentication (MFA)** `[2] Bab 3 & 22` | — |
| **7** | **`Sub-CPMK-2.2` (Bagian II):** Model Kontrol Akses (**DAC, MAC, RBAC, ABAC**) & Arsitektur Pertahanan Jaringan Dasar (*Defense-in-Depth, Firewall, DMZ, VPN, IDS vs IPS*) + Klinik UTS [C4] | 2.2.2 Ketepatan merancang matriks hak akses **Role-Based Access Control (RBAC)** berprinsip *Least Privilege & Separation of Duties* serta membedakan fungsi deteksi pasif **IDS** vs pemblokiran sejalur **IPS**. | **Kriteria:** Matriks RBAC bebas konflik wewenang (*pembuat pengajuan dana dilarang menjadi penyetuju tunggal!*) & aturan firewall tepat.<br>**Teknik:** Latihan perancangan matriks RBAC + aturan firewall & klinik UTS. | **Access Control & Perimeter Studio + Klinik UTS**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Bank soal latihan pra-UTS di LMS Edlink. | Model **DAC, MAC, RBAC, ABAC**, Prinsip *Least Privilege & Separation of Duties*, serta Dasar **Firewall, DMZ, VPN, IDS/IPS** `[1] Bab 5–6; [2] Bab 4 & 9` | — |
| **8** | **UJIAN TENGAH SEMESTER (UTS) — Mengukur `Sub-CPMK-1.2` (`CPMK-1`, 15%) & `Sub-CPMK-2.2` (`CPMK-2`, 15%) [C3–C4]** | Ketepatan menerapkan skema integritas **SHA-256, HMAC, Digital Signature, & PKI/TLS** serta menganalisis rancangan **MFA, Matriks RBAC,** dan aturan pertahanan perimeter (*Firewall/IDS/IPS*). | **Kriteria:** **Rubrik Analitik UTS (`K-1`)**.<br>**Teknik:** Ujian Tertulis Kasus & Analisis Keamanan Terawasi (*Closed-Book*). | **Ujian Tengah Semester Terawasi**<br>`[100 menit]` | Pengarsipan lembar jawaban & nilai `Sub-CPMK-1.2` serta `Sub-CPMK-2.2` pada portal OBE. | Materi **SHA-256, Digital Signature, PKI/TLS, MFA, RBAC,** & Pertahanan Jaringan Dasar (Pekan 5–7) | **30%**<br>*(UTS — `CPMK-1` 15% + `CPMK-2` 15%)* |
| **9** | **`Sub-CPMK-2.1` (Bagian I):** Metodologi *Vulnerability Assessment* vs *Penetration Testing*, Standar Penilaian Keparahan **CVSS / CVE**, & Bedah **OWASP Top 10** (*A01 Broken Access Control & A02 Cryptographic Failures*) [C4] | 2.1.1 Ketepatan menghitung/menafsirkan skor keparahan **CVSS v3.1/v4.0** (*Critical, High, Medium, Low*) pada katalog kerentanan publik **CVE**.<br>2.1.2 Ketepatan menganalisis akar masalah *Broken Access Control* dan *Cryptographic Failures*. | **Kriteria:** Memahami batas tegas *Vulnerability Assessment* defensif dan prioritisasi perbaikan berbasis CVSS.<br>**Teknik:** Bedah laporan CVE nyata & penyiapan kontainer target lokal `OWASP Juice Shop`. | **OWASP & CVSS Case Lecture**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Panduan menjalankan target latihan legal `docker run bkimminich/juice-shop` secara lokal di LMS Edlink. | *Vulnerability Assessment*, Basis Data **CVE & Skor CVSS**, serta **OWASP Top 10**: *A01 Broken Access Control & A02 Cryptographic Failures* `[5]; [2] Bab 11` | — |
| **10** | **`Sub-CPMK-2.1` (Bagian II):** Bedah Mekanisme & Pencegahan **OWASP A03 Injection (*SQL Injection & Cross-Site Scripting / XSS*)** serta **A07 Identification & Authentication Failures** [C4] | 2.1.3 Ketepatan menganalisis bagaimana kueri konkatenasi string memungkinkan *SQL Injection* dan bagaimana skrip tak-disanitasi memicu *Stored/Reflected XSS*, beserta solusi pencegahannya (*Parameterized Queries, Output Encoding, Content-Security-Policy*). | **Kriteria:** Mampu menunjuk baris kode rentan dan menuliskan perbaikan kode aman (*bersinergi dengan `STI-416`*).<br>**Teknik:** Bedah perbandingan kode rentan vs kode aman di kelas. | **Secure Coding Analysis Lecture**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Rilis resmi penugasan *Vulnerability Assessment* **Tugas 2 (RTM-2)** di LMS Edlink. | **OWASP Top 10**: *A03 Injection (SQLi, XSS)*, *A07 Auth Failures*, *Parameterized Queries*, & *Content Security Policy (CSP)* `[5]` | — |
| **11** | **`Sub-CPMK-2.1` (Bagian III):** Bedah **OWASP A05 Security Misconfiguration, A06 Vulnerable & Outdated Components (*Software Supply Chain*), A09 Logging Failures, & A10 SSRF** serta Pemindaian dengan **OWASP ZAP** [C4] | 2.1.4 Ketepatan menjalankan pemindai kerentanan resmi (**OWASP ZAP** + audit dependensi `npm audit / pip-audit`) terhadap aplikasi uji lokal terisolasi serta memilah *True Positive* dari *False Positive*. | **Kriteria:** Pemindaian hanya dilakukan pada `localhost` kontainer latihan resmi dan laporan temuan akurat.<br>**Teknik:** Demonstrasi & latihan pemindaian **OWASP ZAP** pada *OWASP Juice Shop / DVWA*. | **Vulnerability Scanning Studio**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Templat Laporan *Vulnerability Assessment & Remediation* standar industri di LMS Edlink. | *Security Misconfiguration*, Kerentanan Pustaka Pihak Ketiga (*SCA*), **OWASP ZAP Baseline/Spider Scan**, & Triage *False Positives* `[5]` | — |
| **12** | **`Sub-CPMK-2.1` & `2.2` (Remediasi & Verifikasi):** Penyusunan Rencana Remediasi Terprioritas (*Risk-Based Patching & RBAC Hardening*) [C4]<br>*(+ Evaluasi Tugas 2 atas `Sub-CPMK-2.1`)* | 2.1.5 Ketepatan menyusun laporan hasil penilaian kerentanan **OWASP Top 10** lengkap bukti temuan, skor CVSS, analisis dampak bisnis, dan rekomendasi perbaikan teknis yang dapat dieksekusi tim pengembang. | **Kriteria:** **Rubrik Analitik Tugas 2 (`K-1`)**.<br>**Teknik:** Pengumpulan & Presentasi Verifikasi Laporan *Vulnerability Assessment* (**Tugas 2**). | **Remediation Review & Uji Tugas 2**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan berkas **Tugas 2 (`Sub-CPMK-2.1`)** di LMS Edlink. | Prioritisasi Remediasi Kerentanan, *Secure SDLC* Dasar, & Verifikasi **Tugas 2** `[1] Bab 7; [5]` | **20%**<br>*(Tugas 2 — `CPMK-2`)* |
| **13** | **`Sub-CPMK-3.1` (Bagian I):** Manajemen Risiko Keamanan Informasi (*Asset Valuation, Threat, Vulnerability, Likelihood × Impact Matrix, SLE/ARO/ALE*) & 4 Strategi Perlakuan Risiko [C5] | 3.1.1 Ketepatan menghitung eksposur risiko (*Single Loss Expectancy & Annualized Loss Expectancy*) serta memilih strategi perlakuan risiko yang tepat (**Mitigate, Transfer, Avoid, Accept**). | **Kriteria:** Matriks risiko dan justifikasi biaya kontrol keamanan $\le$ nilai kerugian tahunan (*ALE*) logis.<br>**Teknik:** Lokakarya penyusunan *Information Security Risk Register*. | **Risk Management Case Studio**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Spesifikasi studi kasus audit/evaluasi akhir **UAS** dirilis di LMS Edlink. | Metodologi Manajemen Risiko Siber, Matriks *Likelihood × Impact*, Kalkulasi **SLE–ARO–ALE**, & Strategi *Risk Treatment* `[1] Bab 4; [2] Bab 14` | — |
| **14** | **`Sub-CPMK-3.1` (Bagian II):** Evaluasi Kesiapan & Penanganan Insiden Siber menggunakan **NIST Cybersecurity Framework (CSF 2.0)**: **Govern, Identify, Protect, Detect, Respond, Recover** [C5] | 3.1.2 Ketepatan mengevaluasi celah kesiapan organisasi pada keenam fungsi inti **NIST CSF 2.0** dan menyusun alur respons insiden (*Preparation $\rightarrow$ Detection & Analysis $\rightarrow$ Containment, Eradication & Recovery $\rightarrow$ Post-Incident Lessons Learned*). | **Kriteria:** Evaluasi *Current Profile vs Target Profile* NIST CSF 2.0 tajam dan langkah *Containment* insiden tepat (tidak langsung mematikan paksa RAM barang bukti atau membayar tebusan!).<br>**Teknik:** *Tabletop Exercise* serangan *ransomware* rumah sakit/kampus. | **NIST CSF Tabletop Simulation**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Unduh lembar kerja profil fungsi **NIST CSF 2.0** di LMS Edlink. | Kerangka Kerja **NIST CSF 2.0** (*Govern, Identify, Protect, Detect, Respond, Recover*) & Siklus *Incident Response* (NIST SP 800-61) `[3]; [1] Bab 9` | — |
| **15** | **`Sub-CPMK-3.2`:** Evaluasi Sistem Manajemen Keamanan Informasi (**ISMS ISO/IEC 27001:2022** & 4 Tema Kontrol *Annex A*: *Organizational, People, Physical, Technological*) serta Kepatuhan **UU PDP No. 27/2022** + Klinik UAS [C5] | 3.2.1 Ketepatan menilai tingkat pemenuhan kontrol *Annex A* **ISO/IEC 27001:2022** (*Statement of Applicability* dasar) dan kewajiban pengendali data pada **UU PDP** (mis. kewajiban pemberitahuan kebocoran data $3\times 24\text{ jam}$!). | **Kriteria:** Pemetaan kesenjangan (*Gap Analysis*) terhadap klausul ISO 27001 & UU PDP akurat dan praktis.<br>**Teknik:** Latihan penyusunan *Gap Analysis* singkat & klinik persiapan UAS. | **ISO 27001 & UU PDP Compliance Review**<br>`[TM: 100']`<br>`[PT: 120']` · `[BM: 120']` | Pengumpulan laporan studi kasus evaluasi risiko & tata kelola keamanan proyek UAS di LMS Edlink. | Struktur **ISO/IEC 27001:2022**, 93 Kontrol *Annex A*, Kewajiban **UU PDP No. 27/2022**, *Security Awareness*, & *Handoff* ke `STI-519` `[4]; [5]` | — |
| **16** | **EVALUASI AKHIR SEMESTER (UAS) — Mengukur `CPMK-3` (`Sub-CPMK-3.1` [15%] & `Sub-CPMK-3.2` [15%]) [C5]** | Ketajaman mengevaluasi insiden dan risiko siber organisasi menggunakan kerangka **NIST CSF 2.0** serta menilai kesenjangan kontrol keamanan informasi berdasarkan standar **ISO/IEC 27001:2022** dan kepatuhan **UU PDP**. | **Kriteria:** **Rubrik Analitik UAS (`K-1`)**.<br>**Teknik:** Penilaian Laporan Studi Kasus *Security Risk & NIST CSF / ISO 27001 Gap Assessment* (50% UAS) + Ujian/Sidang Evaluasi Kasus Insiden Individu (50% UAS). | **Sidang & Ujian Kasus Evaluasi Insiden Siber (*NIST CSF & ISO/IEC 27001*)**<br>`[100 menit]` | Pengarsipan laporan evaluasi & rekap nilai `CPL-07` dan `CPL-11` pada portal OBE. | Sintesis Manajemen Risiko Siber, Respons Insiden **NIST CSF 2.0**, Standar **ISO/IEC 27001:2022**, & Kepatuhan **UU PDP** | **30%**<br>*(UAS — `CPMK-3`)* |

---

## HALAMAN 8–10 — LAMPIRAN INSTRUMEN PENILAIAN & RUBRIK RINGKAS

### Lampiran 1 — Tugas 1 (Pekan 4 · Bobot 20% · Mengukur `Sub-CPMK-1.1` / `CPMK-1` / `CPL-07` [C3])
* **Bentuk Instrumen:** Studi Kasus & Eksperimen Terbimbing **Perlindungan CIA Triad dengan Kriptografi Simetris (AES) dan Asimetris (RSA)**: mahasiswa mengklasifikasikan aset data organisasi, mengimplementasikan enkripsi-dekripsi berkas rahasia dengan **AES-256-GCM** serta pembungkusan kunci sesi dengan **RSA** (*Hybrid Encryption* menggunakan `OpenSSL` / Python `cryptography`), dan membuktikan kelemahan mode yang tidak aman.
* **Bobot Kriteria Rubrik (`K-1`):** (1) Ketepatan analisis ancaman **CIA Triad** & klasifikasi sensitivitas data = **30%**; (2) Ketepatan penerapan enkripsi simetris **AES** & manajemen *IV/Key* = **35%**; (3) Ketepatan penerapan kriptografi asimetris **RSA** & skema hibrida = **35%**.

### Lampiran 2 — Ujian Tengah Semester / UTS (Pekan 8 · Bobot 30% · Mengukur `Sub-CPMK-1.2` [`CPL-07`: 15%] & `Sub-CPMK-2.2` [`CPL-11`: 15%])
* **Bentuk Instrumen:** **Ujian Tertulis Analisis Kasus Keamanan Terawasi** (100 menit, individu): Bagian A menguji penerapan **SHA-256, HMAC, Digital Signature,** dan verifikasi rantai sertifikat **PKI/TLS 1.3** (`Sub-CPMK-1.2`); Bagian B menguji perancangan skema **MFA**, matriks hak akses **RBAC** bebas konflik *Separation of Duties*, serta pemilihan kontrol **Firewall / DMZ / IDS / IPS** (`Sub-CPMK-2.2`).
* **Bobot Kriteria Rubrik (`K-1`):** (1) Ketepatan penerapan **SHA-256, Digital Signature, & PKI/TLS** (`Sub-CPMK-1.2` → `CPL-07`) = **50%** *(15% MK)*; (2) Ketepatan analisis **MFA, Matriks RBAC,** & kontrol jaringan dasar (`Sub-CPMK-2.2` → `CPL-11`) = **50%** *(15% MK)*.

### Lampiran 3 — Tugas 2 (Pekan 12 · Bobot 20% · Mengukur `Sub-CPMK-2.1` / `CPMK-2` / `CPL-11` [C4])
* **Bentuk Instrumen:** Proyek Studi Kasus **Penilaian Kerentanan Aplikasi Web (*OWASP Top 10 Vulnerability Assessment Report*)** pada lingkungan kontainer lokal legal (*OWASP Juice Shop / DVWA*): menggunakan **OWASP ZAP** dan inspeksi aman, mahasiswa menemukan minimal 5 kategori kerentanan **OWASP Top 10**, menghitung skor keparahan **CVSS**, memilah *false positive*, serta merumuskan rekomendasi perbaikan kode dan kontrol akses **RBAC** yang konkret.
* **Bobot Kriteria Rubrik (`K-1`):** (1) Ketepatan identifikasi & pembuktian etis kerentanan **OWASP Top 10** dengan *OWASP ZAP* = **40%**; (2) Ketepatan penilaian keparahan **CVSS** & analisis akar masalah = **25%**; (3) Kualitas rekomendasi remediasi teknis & penguatan kontrol akses = **35%**.

### Lampiran 4 — Evaluasi Akhir Semester / UAS (Pekan 16 · Bobot 30% · Mengukur `CPMK-3` / `CPL-07` [15%] & `CPL-11` [15%] [C5])
* **Bentuk Instrumen:** **Studi Kasus Komprehensif Evaluasi Insiden Siber & Kesenjangan Keamanan Organisasi (*NIST CSF 2.0 & ISO/IEC 27001 Gap Assessment*)** (50% nilai UAS: dokumen *Risk Register*, evaluasi respons insiden berbasis 6 fungsi **NIST CSF 2.0**, serta pemetaan kontrol *Annex A* **ISO/IEC 27001:2022** & kepatuhan **UU PDP** atas studi kasus kebocoran data/serangan *ransomware* organisasi) + **Sidang/Ujian Kasus Evaluasi Individu** (50% nilai UAS, 100 menit).
* **Bobot Kriteria Rubrik (`K-1`):** (1) Ketajaman evaluasi risiko (*Risk Register / ALE*) & rencana respons insiden berbasis **NIST CSF 2.0** (`Sub-CPMK-3.1` → `CPL-07`) = **50%** *(15% MK)*; (2) Ketepatan penilaian kontrol **ISO/IEC 27001:2022**, kepatuhan **UU PDP**, & penguasaan individu saat ujian/sidang (`Sub-CPMK-3.2` → `CPL-11`) = **50%** *(15% MK)*.

---

## HALAMAN 11 — PENGESAHAN DOKUMEN RPS

| Disusun Oleh | Diperiksa Oleh (GPM / Koordinator RMK) | Disahkan Oleh (Ketua Program Studi) |
|---|---|---|
| **Tim KBK Infrastruktur, Cloud & Keamanan**<br><br><br>*(Tanda Tangan)*<br>**[Nama Dosen Koordinator MK]** | **Koordinator Rumpun Mata Kuliah**<br><br><br>*(Tanda Tangan)*<br>**Dr. Istiadi, S.T., M.T.** | **Ketua Prodi S1 SISTEKIN FSTI UWG**<br><br><br>*(Tanda Tangan & Stempel)*<br>**Ahmad Fairuzabadi, S.Kom., M.Kom.** |
