# 072_3 — OUTLINE BUKU MODUL PEMBELAJARAN BERBASIS OBE
## STI-418 — DASAR KEAMANAN INFORMASI (*Fundamentals of Information Security*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.6.RPS-STI418` · **Bobot:** 2 SKS (`Teori`: `T=2, P=0`) · **Semester:** 4  
**CPL:** `CPL-07` (`P3` = 50%) & `CPL-11` (`KK3` = 50%) [Level `R`] · **BoK:** `BK-IS06`, `BK-IT06`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Dasar Keamanan Informasi & Manajemen Risiko Siber: CIA Triad, Kriptografi Terapan, Analisis Kerentanan OWASP Top 10, hingga Kerangka Kerja NIST CSF 2.0 & ISO/IEC 27001* |
| **Target Tebal Naskah** | 14 Bab Materi & Studi Kasus + 2 Unit Evaluasi ($\pm 170\text{–}195\text{ halaman}$ A4 selaras bobot 2 SKS) |
| **Pagar Pembatas Buku (*Guardrail*)** | Fokus pada fondasi keamanan defensif, kriptografi terapan, *vulnerability assessment* etis lokal, dan kerangka tata kelola dasar; tidak membahas eksploitasi biner/forensik malware (`STI-519`, `STB-501`), *ethical hacking* ofensif lanjut (`STB-602`), maupun audit COBIT penuh (`STB-701`). |

---

## 2. PETA KESELARASAN 14 BAB MODUL TERHADAP CPMK & SUB-CPMK

| Bagian | Bab | Judul Bab | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>CIA Triad & Kriptografi Kerahasiaan** | **Bab 1** | Prinsip **CIA Triad**, Lanskap Ancaman Siber Modern, & Etika Hukum Keamanan | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2** | Kriptografi Simetris Modern (**AES**), Mode **AES-GCM**, & Manajemen Kunci | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3** | Kriptografi Asimetris (**RSA & ECC**) serta Arsitektur **Hybrid Encryption** | Mg 3 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 4** | Klasifikasi Sensitivitas Data (**UU PDP**) & Perlindungan *Data-at-Rest / in-Transit* | Mg 4 | `CPMK-1` | `Sub-CPMK-1.1` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Integritas, PKI/TLS, & Kontrol Akses** | **Bab 5** | Fungsi *Hash* (**SHA-256**), **HMAC**, & Nir-Penyangkalan **Digital Signature** | Mg 5 | `CPMK-1` | `Sub-CPMK-1.2` | UTS (30%) |
| | **Bab 6** | **Public Key Infrastructure (PKI)**, Sertifikat **X.509 / TLS 1.3**, & **MFA** | Mg 6 | `CPMK-1, 2` | `Sub-CPMK-1.2, 2.2` | UTS (30%) |
| | **Bab 7** | Model Kontrol Akses (**DAC, MAC, RBAC, ABAC**) & Pertahanan Perimeter Dasar | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Bank Soal Kasus Integritas Kriptografi, PKI/TLS, Matriks RBAC, & Firewall (UTS)* | *Mg 8* | *`1 & 2`* | *`1.2 & 2.2`* | *UTS (30%)* |
| **Bagian III:<br>Analisis Kerentanan Web OWASP Top 10** | **Bab 8** | Metodologi *Vulnerability Assessment*, **CVE / CVSS**, & **OWASP A01–A02** | Mg 9 | `CPMK-2` | `Sub-CPMK-2.1` | Tugas 2 (20%) |
| | **Bab 9** | Anatomi & Pencegahan **OWASP A03 Injection (*SQLi, XSS*)** serta **A07 Auth** | Mg 10 | `CPMK-2` | `Sub-CPMK-2.1` | Tugas 2 (20%) |
| | **Bab 10** | *Security Misconfiguration*, *Supply Chain*, & Pemindaian Etis **OWASP ZAP** | Mg 11 | `CPMK-2` | `Sub-CPMK-2.1` | Tugas 2 (20%) |
| | **Bab 11** | Penyusunan Laporan *Vulnerability Assessment* & Prioritisasi Remediasi | Mg 12 | `CPMK-2` | `Sub-CPMK-2.1` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Risiko, NIST CSF 2.0, & ISO/IEC 27001** | **Bab 12** | Manajemen Risiko Keamanan Informasi: Matriks Risiko, **SLE–ARO–ALE**, & Perlakuan | Mg 13 | `CPMK-3` | `Sub-CPMK-3.1` | UAS (30%) |
| | **Bab 13** | Evaluasi Kesiapan & Respons Insiden Siber dengan **NIST CSF 2.0** | Mg 14 | `CPMK-3` | `Sub-CPMK-3.1` | UAS (30%) |
| | **Bab 14** | Standar **ISO/IEC 27001:2022 (*Annex A*)**, Kepatuhan **UU PDP**, & *Handoff* `STI-519` | Mg 15 | `CPMK-3` | `Sub-CPMK-3.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Studi Kasus Evaluasi Insiden NIST CSF 2.0 & Gap Analysis ISO 27001 (UAS)* | *Mg 16* | *`CPMK-3`* | *`3.1–3.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB BUKU MODUL

#### BAB 1: Prinsip CIA Triad, Lanskap Ancaman Siber Modern, & Etika Hukum Keamanan (Pekan 1)
* **Substansi:** *Confidentiality, Integrity, Availability, Authenticity, Non-Repudiation*, profil aktor ancaman, vektor *Social Engineering / Phishing / Ransomware*, dan batasan hukum UU ITE.

#### BAB 2: Kriptografi Simetris Modern (AES), Mode AES-GCM, & Manajemen Kunci (Pekan 2)
* **Substansi:** Prinsip Kerckhoffs, struktur *block cipher* **AES**, perbandingan mode `ECB`, `CBC`, dan **AES-GCM**, serta bahaya *hardcoded keys* dan daur ulang *Nonce/IV*.

#### BAB 3: Kriptografi Asimetris (RSA & ECC) serta Arsitektur Hybrid Encryption (Pekan 3)
* **Substansi:** Intuisi matematis pasangan kunci publik-privat **RSA** & kurva eliptik, pertukaran kunci *Diffie-Hellman*, dan penggabungan RSA + AES pada *Hybrid Encryption*.

#### BAB 4: Klasifikasi Sensitivitas Data (UU PDP) & Perlindungan Siklus Data (Pekan 4)
* **Substansi:** Skema klasifikasi aset informasi organisasi, Data Pribadi Spesifik menurut **UU No. 27/2022**, serta pemilihan kontrol enkripsi untuk *Data-at-Rest, Data-in-Transit,* dan *Backup*.

#### BAB 5: Fungsi Hash (SHA-256), HMAC, & Nir-Penyangkalan Digital Signature (Pekan 5)
* **Substansi:** Properti ketahanan pra-citra & tumbukan pada **SHA-256**, autentikasi pesan ber-kunci **HMAC**, serta pembuatan dan verifikasi **Digital Signature**.

#### BAB 6: Public Key Infrastructure (PKI), Sertifikat X.509 / TLS 1.3, & MFA (Pekan 6)
* **Substansi:** Hierarki *Certificate Authority (CA)*, validasi sertifikat **X.509**, alur jabat tangan **TLS 1.3**, pencabutan sertifikat, serta evaluasi faktor autentikasi **MFA / Passkeys**.

#### BAB 7: Model Kontrol Akses (DAC, MAC, RBAC, ABAC) & Pertahanan Perimeter Dasar (Pekan 7)
* **Substansi:** Perbandingan model akses, perancangan matriks **RBAC** berprinsip *Least Privilege & Separation of Duties*, serta penempatan *Firewall, DMZ, VPN, IDS,* dan *IPS*.

#### BAB 8: Metodologi Vulnerability Assessment, CVE / CVSS, & OWASP A01–A02 (Pekan 9)
* **Substansi:** Perbedaan penilaian kerentanan vs uji penetrasi, pembacaan katalog **CVE** & kalkulator **CVSS**, serta analisis *A01 Broken Access Control* dan *A02 Cryptographic Failures*.

#### BAB 9: Anatomi & Pencegahan OWASP A03 Injection (SQLi, XSS) serta A07 Auth Failures (Pekan 10)
* **Substansi:** Mekanisme *SQL Injection* dan *Cross-Site Scripting* pada aplikasi web beserta pertahanan berlapis (*Parameterized Queries, Output Encoding, CSP, Session Hardening*).

#### BAB 10: Security Misconfiguration, Supply Chain, & Pemindaian Etis OWASP ZAP (Pekan 11)
* **Substansi:** Kesalahan konfigurasi bawaan, kerentanan dependensi pihak ketiga (*SCA*), *SSRF*, dan prosedur pemindaian aman pada kontainer lokal menggunakan **OWASP ZAP**.

#### BAB 11: Penyusunan Laporan Vulnerability Assessment & Prioritisasi Remediasi (Pekan 12)
* **Substansi:** Validasi *False Positives*, struktur laporan teknis-eksekutif penilaian kerentanan, dan penyusunan peta jalan perbaikan berbasis tingkat risiko.

#### BAB 12: Manajemen Risiko Keamanan Informasi — Matriks Risiko, SLE–ARO–ALE, & Perlakuan (Pekan 13)
* **Substansi:** Identifikasi nilai aset, perhitungan kualitatif & kuantitatif (*SLE, ARO, ALE*), selera risiko organisasi, dan empat strategi perlakuan risiko.

#### BAB 13: Evaluasi Kesiapan & Respons Insiden Siber dengan NIST CSF 2.0 (Pekan 14)
* **Substansi:** Keenam fungsi inti **NIST CSF 2.0** (*Govern, Identify, Protect, Detect, Respond, Recover*), penyusunan profil kesenjangan, dan tahapan penanganan insiden *ransomware/breach*.

#### BAB 14: Standar ISO/IEC 27001:2022 (Annex A), Kepatuhan UU PDP, & Handoff ke STI-519 (Pekan 15)
* **Substansi:** Siklus PDCA sistem manajemen keamanan informasi, empat tema kontrol *Annex A* **ISO/IEC 27001:2022**, kewajiban hukum pengendali data **UU PDP**, dan jembatan ke `STI-519 Keamanan Informasi Lanjut`.
