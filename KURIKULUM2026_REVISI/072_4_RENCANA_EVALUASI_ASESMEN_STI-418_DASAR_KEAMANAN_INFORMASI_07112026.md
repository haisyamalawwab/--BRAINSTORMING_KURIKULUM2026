# 072_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-418 — DASAR KEAMANAN INFORMASI (*Fundamentals of Information Security*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.6.RPS-STI418` · **Bobot:** 2 SKS (`Teori`: `T=2, P=0`) · **Semester:** 4  
**Klaster Asesmen MK (Dok 018):** Klaster 1 (`K-1`) — Fondasi Sains, Matematika & Komputasi Dasar  
**CPL Dibebankan:** `CPL-07` (`P3` = **50%**) & `CPL-11` (`KK3` = **50%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU & KEPATUHAN IKU 7

Selaras **Dokumen 005, 008, 018,** dan **043**, mata kuliah `STI-418 Dasar Keamanan Informasi` (2 SKS `Teori`, 3 CPMK & 6 Sub-CPMK) menerapkan skema bobot baku (`20% / 30% / 20% / 30%`) yang memetakan keenam Sub-CPMK secara utuh dan seimbang (`50% CPL-07 + 50% CPL-11`):
* **Tugas 1 (Pekan 4 — 20%) → `Sub-CPMK-1.1` (`CPMK-1` / `CPL-07`)** — *Case-Based CIA Triad & Symmetric/Asymmetric Cryptographic Protection (AES & RSA)*.
* **UTS (Pekan 8 — 30%) → `Sub-CPMK-1.2` (15% `CPL-07`) + `Sub-CPMK-2.2` (15% `CPL-11`)** — *Supervised Exam: Cryptographic Integrity (SHA-256, Digital Signature, PKI/TLS) & Access/Perimeter Controls (MFA, RBAC, Firewall/IDS/IPS)*.
* **Tugas 2 (Pekan 12 — 20%) → `Sub-CPMK-2.1` (`CPMK-2` / `CPL-11`)** — *Case-Based Web Application Vulnerability Assessment (OWASP Top 10 with OWASP ZAP) & Remediation Report*.
* **UAS (Pekan 16 — 30%) → `Sub-CPMK-3.1` (15% `CPL-07`) + `Sub-CPMK-3.2` (15% `CPL-11`) (`CPMK-3`)** — *Case/Project-Based Cyber Incident Risk & NIST CSF 2.0 / ISO 27001 Security Gap Evaluation*.
* **Kepatuhan IKU 7 ($\ge 50\%$ Klaster `K-1` Dok 018; Target Dok 004 `55%`):** `Tugas 1 (20%) + Tugas 2 (20%) + UAS (30%) = 70%` berbasis studi kasus perlindungan kriptografi, penilaian kerentanan terisolasi, dan evaluasi insiden/kepatuhan organisasi.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-07`**<br>(`P3` — 50%)<br>*Level: R* | **`CPMK-1`**<br>(C3) | `Sub-CPMK-1.1` | Mg 4 | Studi kasus perlindungan data: Penerapan **CIA Triad**, enkripsi **AES**, & **RSA** hibrida | **RTM-1 (Tugas 1)** Artefak Kriptografi + Rubrik Analitik T1 | Sumatif | 20% | **35%** |
| | | `Sub-CPMK-1.2` | Mg 8 | Ujian tertulis terawasi 100': Penerapan **SHA-256, HMAC, Digital Signature,** & **PKI/TLS** | **Soal UTS Bagian A** (Integritas & PKI) + Rubrik Analitik UTS | Sumatif | 15% | |
| **`CPL-11`**<br>(`KK3` — 50%)<br>*Level: R* | **`CPMK-2`**<br>(C4) | `Sub-CPMK-2.2` | Mg 8 | Ujian tertulis terawasi 100': Perancangan **MFA, Matriks RBAC,** & kontrol *Firewall/IDS/IPS* | **Soal UTS Bagian B** (Kontrol Akses & Jaringan) + Rubrik UTS | Sumatif | 15% | **35%** |
| | | `Sub-CPMK-2.1` | Mg 12 | Studi kasus pemindaian lokal: Analisis kerentanan **OWASP Top 10** dengan *OWASP ZAP* & remediasi | **RTM-2 (Tugas 2)** Laporan *Vulnerability Assessment* + Rubrik T2 | Sumatif | 20% | |
| **`CPL-07` (15%)**<br>& **`CPL-11` (15%)**<br>*Level: R* | **`CPMK-3`**<br>(C5) | `Sub-CPMK-3.1`<br>*(`CPL-07`)* | Mg 16 | Studi kasus insiden + sidang: Evaluasi risiko (*ALE*) & kesiapan insiden berbasis **NIST CSF 2.0** | **Laporan Kasus & Ujian UAS Bagian NIST CSF** + Rubrik UAS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-3.2`<br>*(`CPL-11`)* | Mg 16 | Studi kasus tata kelola + sidang: Penilaian kontrol **ISO/IEC 27001:2022** & kepatuhan **UU PDP** | **Laporan *Gap Analysis* ISO 27001 & Sidang UAS** + Rubrik UAS | Sumatif | 15% | |
| **TOTAL** | **3 CPMK** | **6 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku (20/30/20/30)** | **4 Paket Instrumen Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI UJIAN

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: Perlindungan CIA Triad dengan AES & RSA)
* **Jadwal & Bobot:** Rilis **Pekan 3**, Kumpul & Verifikasi **Pekan 4** · Bobot **20%** (`Sub-CPMK-1.1` → `CPL-07`).
* **Spesifikasi Pengerjaan Individu:**
  1. Mengklasifikasikan 5 aset informasi sebuah klinik/fintech berdasarkan dampak **CIA Triad** dan kategori Data Pribadi UU PDP.
  2. Mengimplementasikan skrip/perintah terverifikasi untuk mengenkripsi berkas data sensitif menggunakan **AES-256-GCM** dan melindungi kunci sesi simetrisnya menggunakan pasangan kunci **RSA-2048/3072** (*Hybrid Encryption*), lengkap analisis mengapa kunci privat dan *Nonce* wajib dikelola secara aman.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Integritas Kriptografi, PKI/TLS, & Kontrol Akses RBAC)
* **Format & Bobot:** Ujian Tertulis Analisis Kasus Terawasi (**100 menit**, individu) · Bobot **30%** (`Sub-CPMK-1.2` [15% `CPL-07`] + `Sub-CPMK-2.2` [15% `CPL-11`]).
* **Spesifikasi Soal:**
  1. **Bagian A (`Sub-CPMK-1.2` — 50% UTS):** Menganalisis skenario pemalsuan dokumen/pesan dan merancang mekanisme verifikasi keutuhan serta keaslian pengirim menggunakan **SHA-256, HMAC, Digital Signature,** dan validasi sertifikat **X.509 TLS**.
  2. **Bagian B (`Sub-CPMK-2.2` — 50% UTS):** Merancang skema **MFA** tahan *phishing*, menyusun matriks izin **RBAC** 4 jabatan organisasi yang menegakkan *Least Privilege & Separation of Duties*, serta menempatkan aturan *Firewall, DMZ,* dan *IDS/IPS* pada diagram jaringan.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: Laporan Penilaian Kerentanan Web OWASP Top 10)
* **Jadwal & Bobot:** Rilis **Pekan 10**, Kumpul & Verifikasi **Pekan 12** · Bobot **20%** (`Sub-CPMK-2.1` → `CPL-11`).
* **Spesifikasi Teknis Individu (Wajib di Kontainer Lokal `127.0.0.1`!):**
  1. Menjalankan pemindaian kerentanan menggunakan **OWASP ZAP** dan pemeriksaan terarah terhadap kontainer latihan resmi (*OWASP Juice Shop* atau *DVWA*) di komputer lokal masing-masing.
  2. Menyusun **Vulnerability Assessment Report** profesional yang memuat minimal 5 temuan kerentanan berbeda dari daftar **OWASP Top 10**, skor keparahan **CVSS**, bukti tangkapan layar lokal, penyaringan *false positive*, dan rekomendasi perbaikan kode/konfigurasi **RBAC** yang tepat.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: Evaluasi Insiden NIST CSF 2.0 & ISO/IEC 27001)
* **Format & Bobot:** Bobot **30%** (`CPMK-3` → `CPL-07` [15%] & `CPL-11` [15%]), memadukan **Laporan Studi Kasus Evaluasi Risiko & Kesenjangan Keamanan (50% nilai UAS)** + **Ujian/Sidang Kasus Evaluasi Individu (50% nilai UAS, 100 menit)**:
  1. Diberikan studi kasus komprehensif sebuah organisasi layanan publik/perusahaan digital yang baru mengalami insiden kebocoran data dan pemerasan *ransomware*; mahasiswa menyusun *Risk Register* (*SLE/ARO/ALE*), mengevaluasi kelemahan kesiapan & tahapan respons insiden berdasarkan 6 fungsi **NIST CSF 2.0** (`Sub-CPMK-3.1`), serta menyusun matriks *Gap Analysis* terhadap kontrol *Annex A* **ISO/IEC 27001:2022** dan kewajiban hukum **UU PDP No. 27/2022** (`Sub-CPMK-3.2`).
  2. Pada sesi ujian/sidang Pekan 16, penguji menguji ketajaman pertimbangan prioritas kontrol keamanan secara individu.

---

## 4. FORMULA NILAI AKHIR, DISAGGREGASI MULTI-CPL, & AMBANG KETUNTASAN OBE

### 4.1 Rumus Nilai Akhir Mata Kuliah ($NA_{\text{STI-418}}$)
$$NA_{\text{STI-418}} = 0,20\,S_{\text{Tugas 1}} + 0,30\,S_{\text{UTS}} + 0,20\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

### 4.2 Rumus Disaggregasi Ketercapaian Multi-CPL & CPMK (Dokumen 004 & 008)
1. **Skor Tiap CPMK:**
   * $S_{\text{CPMK-1}} = \frac{0,20\,S_{\text{Tugas 1}} + 0,15\,S_{\text{UTS-A}}}{0,35}$
   * $S_{\text{CPMK-2}} = \frac{0,15\,S_{\text{UTS-B}} + 0,20\,S_{\text{Tugas 2}}}{0,35}$
   * $S_{\text{CPMK-3}} = 0,50\,S_{\text{UAS, Sub-3.1}} + 0,50\,S_{\text{UAS, Sub-3.2}}$
2. **Ketercapaian `CPL-07` (`P3` — bobot 50% MK dari `Sub-1.1` [20%] + `Sub-1.2` [15%] + `Sub-3.1` [15%]):**
   $$\text{Score}_{\text{CPL-07, STI-418}}(i) = \frac{0,20\,S_{\text{Tugas 1}}(i) + 0,15\,S_{\text{UTS-A}}(i) + 0,15\,S_{\text{UAS, Sub-3.1}}(i)}{0,50}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 2 \times 0,50 = 1,00\text{ SKS}$).*
3. **Ketercapaian `CPL-11` (`KK3` — bobot 50% MK dari `Sub-2.2` [15%] + `Sub-2.1` [20%] + `Sub-3.2` [15%]):**
   $$\text{Score}_{\text{CPL-11, STI-418}}(i) = \frac{0,15\,S_{\text{UTS-B}}(i) + 0,20\,S_{\text{Tugas 2}}(i) + 0,15\,S_{\text{UAS, Sub-3.2}}(i)}{0,50}$$
   *(bobot SKS tertimbang pada agregasi prodi $= 2 \times 0,50 = 1,00\text{ SKS}$).*

### 4.3 Ambang Ketuntasan OBE & Protokol Remedial
* **Ambang Lulus CPMK/CPL OBE:** Skor minimal **$\ge 65,0$ (C+ / 2,50)**; remedial diberikan maksimal 1 kali bagi mahasiswa dengan skor CPMK $< 65,0$ dengan nilai plafon pasca-remedial **70,0 (B)**.
