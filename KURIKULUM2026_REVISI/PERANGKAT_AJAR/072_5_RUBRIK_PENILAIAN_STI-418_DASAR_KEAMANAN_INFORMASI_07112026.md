# 072_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-418 — DASAR KEAMANAN INFORMASI (*Fundamentals of Information Security*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.6.RPS-STI418` · **Klaster Rubrik Master (Dok 018):** Klaster 1 (`K-1`)  
**CPL:** `CPL-07` (`P3` = 50%) & `CPL-11` (`KK3` = 50%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN DASAR KEAMANAN INFORMASI (`K-1`)

Mengacu **Dokumen 018 §3 (Klaster `K-1`)**, penilaian pada `STI-418` menekankan ketepatan konseptual dan matematis dalam penerapan primitif kriptografi (**AES, RSA, SHA-256, Digital Signature, PKI/TLS**), ketelitian perancangan kontrol akses (**RBAC**) serta kedisiplinan etika saat melakukan penilaian kerentanan web **OWASP Top 10**, dan ketajaman analitis dalam mengevaluasi risiko serta kepatuhan keamanan berdasarkan **NIST CSF 2.0** dan **ISO/IEC 27001:2022**.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `Sub-CPMK-1.1` / `CPMK-1` / `CPL-07` [C3])
**Objek Penilaian:** Analisis **CIA Triad**, Klasifikasi Data Sensitif, & Implementasi Kriptografi **AES + RSA**.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Analisis Ancaman **CIA Triad** & Klasifikasi Data** | **30%** | Pemetaan ancaman terhadap dimensi *Confidentiality, Integrity, Availability* dan klasifikasi Data Pribadi UU PDP sangat presisi serta kontekstual. | Mengklasifikasikan aset data dan memetakan dampak CIA Triad secara tepat dan logis. | Menjelaskan dampak dasar CIA Triad dengan cukup benar namun klasifikasi sensitivitas data masih umum. | Sering tertukar antara pelanggaran *Confidentiality* (bocor) dan *Integrity* (diubah tanpa izin). | Tidak mampu memetakan prinsip dasar CIA Triad. |
| **2. Penerapan Kriptografi Simetris **AES** Aman** | **35%** | Mengimplementasikan **AES-256-GCM** dengan pembangkitan kunci acak kriptografis (`CSPRNG`), *Nonce/IV* unik, verifikasi *auth tag*, dan pengelolaan kunci yang aman. | Enkripsi dan dekripsi berkas dengan AES berjalan benar menggunakan mode operasi yang aman (`GCM/CBC`). | Enkripsi AES dasar berjalan, namun pengelolaan parameter *IV* atau pemisahan kunci masih sederhana. | Menggunakan mode `AES-ECB` yang tidak aman atau menanam kunci statis `'12345678'` di dalam skrip! | Gagal menjalankan enkripsi-dekripsi simetris AES. |
| **3. Penerapan Kriptografi Asimetris **RSA** & Skema Hibrida** | **35%** | Pembangkitan pasangan kunci **RSA** (*OAEP padding*) dan pembungkusan kunci sesi AES (*Hybrid Encryption*) berjalan akurat 100% disertai penjelasan alur yang jernih. | Berhasil mengenkripsi kunci sesi dengan kunci publik RSA dan membukanya kembali dengan kunci privat secara benar. | Pembangkitan kunci dan enkripsi pesan pendek RSA berhasil, namun penggabungan alur hibrida dengan AES kurang rapi. | Tertukar peran kunci publik dan kunci privat pada alur kerahasiaan pesan. | Tidak mengimplementasikan bagian kriptografi asimetris RSA. |

$$\text{Skor Tugas 1} = 0,30(K_1) + 0,35(K_2) + 0,35(K_3)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · Mengukur `Sub-CPMK-1.2` [15% `CPL-07`] & `Sub-CPMK-2.2` [15% `CPL-11`])
**Objek Penilaian:** Ujian Tertulis Kasus Terawasi: **SHA-256, Digital Signature, PKI/TLS** & **MFA, Matriks RBAC, Perimeter**.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Integritas **SHA-256/HMAC**, **Digital Signature**, & **PKI/TLS****<br>(`Sub-CPMK-1.2` → `CPL-07`) | **50%**<br>*(15% MK)* | Merancang skema *hash/HMAC*, arah kunci **Digital Signature** (*sign with sender's private key, verify with sender's public key*), dan validasi rantai CA **TLS 1.3** secara 100% akurat tanpa celah. | Menjelaskan dan menerapkan mekanisme SHA-256, tanda tangan digital, serta peran sertifikat X.509 dengan benar. | Memahami fungsi dasar *hashing* dan HTTPS, namun terdapat sedikit kekurangtelitian pada detail jabat tangan TLS/HMAC. | **Tertukar fatal** pada tanda tangan digital (menandatangani dengan kunci publik!) atau menyamakan *hashing* satu-arah dengan enkripsi dua-arah. | Gagal menjawab soal integritas kriptografi dan PKI. |
| **2. Desain **MFA**, Matriks **RBAC**, & Pertahanan Jaringan**<br>(`Sub-CPMK-2.2` → `CPL-11`) | **50%**<br>*(15% MK)* | Matriks **RBAC** menegakkan ketat *Least Privilege & Separation of Duties*, analisis faktor **MFA** tajam, dan penempatan *Firewall, DMZ, VPN,* serta *IDS vs IPS* sangat tepat. | Matriks RBAC valid bebas hak akses berlebih dan pemilihan kontrol jaringan sesuai kebutuhan skenario. | Mampu menyusun pembagian peran dasar RBAC dan membedakan fungsi umum firewall serta IDS/IPS. | Memberikan hak akses penuh pada peran staf biasa atau menyamakan dua kata sandi berbeda sebagai MFA (*padahal satu faktor yang sama!*). | Tidak mampu merancang matriks kontrol akses maupun kontrol jaringan. |

$$\text{Skor UTS} = 0,50(K_{1.2}) + 0,50(K_{2.2})$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `Sub-CPMK-2.1` / `CPMK-2` / `CPL-11` [C4])
**Objek Penilaian:** Laporan *Vulnerability Assessment* Aplikasi Web **OWASP Top 10** dengan **OWASP ZAP** (Target Lokal Legal).

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Identifikasi Kerentanan **OWASP Top 10** & Pemindaian Etis** | **40%** | Menemukan & memverifikasi $\ge 5$ kategori kerentanan **OWASP Top 10** secara akurat menggunakan **OWASP ZAP** pada kontainer lokal, lengkap pemilahan *false positive* dan bukti reproduksi bersih. | Mengidentifikasi 5 kerentanan OWASP Top 10 dengan bukti pemindaian OWASP ZAP yang valid di lingkungan lokal. | Menemukan 3–4 kategori kerentanan secara benar, namun hanya menempel keluaran mentah pemindai tanpa verifikasi manual. | Kurang dari 3 temuan valid atau salah mengklasifikasikan kategori OWASP Top 10. | **Nilai 0 & Sanksi Etika** jika memindai situs luar tanpa izin, atau tidak mengumpulkan tugas. |
| **2. Penilaian Keparahan **CVSS** & Analisis Akar Masalah** | **25%** | Menghitung vektor & skor **CVSS** tiap temuan secara presisi serta membedah tajam akar penyebab kerentanan di sisi aplikasi/konfigurasi. | Penilaian tingkat keparahan CVSS dan penjelasan dampak bisnis tiap kerentanan disusun dengan tepat. | Menyertakan label tingkat risiko (*High/Medium/Low*) secara wajar namun rincian metrik CVSS kurang lengkap. | Tingkat keparahan dinilai asal-asalan (mis. celah *SQL Injection* penuh diberi skor *Low*!). | Tidak menyertakan analisis dampak maupun tingkat keparahan. |
| **3. Rekomendasi Remediasi Teknis & Penguatan **RBAC**** | **35%** | Memberikan solusi perbaikan yang spesifik dan langsung dapat diterapkan (*contoh potongan kode aman parameterized query/CSP/RBAC check*) sesuai urutan prioritas risiko. | Rekomendasi mitigasi teknis untuk setiap temuan relevan, akurat, dan terurut berdasarkan prioritas. | Rekomendasi perbaikan benar secara konseptual namun masih ditulis terlalu normatif/umum. | Rekomendasi tidak nyambung dengan jenis kerentanannya (mis. menyarankan ganti kata sandi untuk menambal XSS). | Tidak menyertakan rencana remediasi kerentanan. |

$$\text{Skor Tugas 2} = 0,40(K_1) + 0,25(K_2) + 0,35(K_3)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · Mengukur `CPMK-3` / `CPL-07` [15%] & `CPL-11` [15%] [C5])
**Objek Penilaian:** Evaluasi Risiko Insiden Siber Berbasis **NIST CSF 2.0** & Penilaian Kontrol **ISO/IEC 27001:2022 + UU PDP**.

| Dimensi Kriteria (`K-1`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Evaluasi Risiko (*ALE*) & Respons Insiden **NIST CSF 2.0****<br>(`Sub-CPMK-3.1` → `CPL-07`) | **50%**<br>*(15% MK)* | Perhitungan *Risk Register (SLE/ARO/ALE)* akurat, evaluasi keenam fungsi **NIST CSF 2.0** (*Govern–Recover*) sangat tajam, dan urutan *Incident Response* (*Containment–Recovery*) bebas kesalahan fatal. | Menyusun penilaian risiko dan memetakan kesiapan serta respons insiden pada fungsi NIST CSF 2.0 dengan tepat. | Memetakan sebagian besar fungsi NIST CSF dan tahapan dasar penanganan insiden dengan cukup benar. | Salah menghitung risiko dasar atau mengusulkan respons insiden berbahaya (mis. menghapus barang bukti log sebelum dianalisis). | Tidak mampu mengevaluasi insiden dengan kerangka NIST CSF. |
| **2. Penilaian Kontrol **ISO/IEC 27001:2022**, **UU PDP**, & Penguasaan UAS**<br>(`Sub-CPMK-3.2` → `CPL-11`) | **50%**<br>*(15% MK)* | *Gap Analysis* memetakan tepat temuan ke 4 tema kontrol *Annex A* **ISO/IEC 27001:2022** serta kewajiban notifikasi/pelindungan **UU PDP** ($3\times 24\text{ jam}$), dan dijawab sangat meyakinkan saat sidang/ujian individu. | Pemetaan kesenjangan kontrol ISO/IEC 27001 dan kepatuhan UU PDP relevan serta dikuasai baik secara individu. | Menyebutkan beberapa kontrol keamanan ISO 27001 yang relevan secara umum dan lulus tanya-jawab dasar. | Mencampuradukkan standar ISO 27001 dengan hal di luar keamanan informasi atau abai terhadap kewajiban hukum kebocoran data pribadi. | Tidak menyerahkan analisis standar ISO 27001 atau tidak hadir UAS. |

$$\text{Skor UAS} = 0,50(K_{3.1}) + 0,50(K_{3.2})$$

---

## BAGIAN III — RUBRIK FORMATIF DISKUSI KASUS & ETIKA KEAMANAN MINGGUAN

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketepatan Analisis Defensif & Integritas Etika** | Aktif membedah akar penyebab insiden siber dengan perspektif defensif matang dan mematuhi 100% Pakta Etika Siber. | Menyelesaikan latihan kriptografi/analisis kasus mingguan tepat waktu dan patuh etika. | Mengikuti latihan kelas dengan pemahaman dasar yang memadai. | Pasif dalam latihan kelas atau menunjukkan kecerobohan etika pengujian. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-418` (`CPL-07` & `CPL-11` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai penuh penerapan kriptografi modern (**AES, RSA, SHA-256, Digital Signature, PKI/TLS**), cermat menilai kerentanan **OWASP Top 10** & merancang **RBAC**, serta tajam mengevaluasi risiko dan kepatuhan berdasarkan **NIST CSF 2.0**, **ISO/IEC 27001:2022**, dan **UU PDP**. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa mampu menerapkan mekanisme kriptografi kerahasiaan/integritas, melakukan *vulnerability assessment* etis dengan OWASP ZAP, serta menyusun evaluasi risiko dan kontrol keamanan berstandar internasional. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi standar ketuntasan minimal OBE ($\ge 65,0$) dalam konsep CIA Triad, penggunaan dasar AES/RSA/SHA-256, identifikasi celah utama OWASP Top 10, dan pemetaan dasar NIST CSF / ISO 27001. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih keliru memakai primitif kriptografi, menyusun kontrol akses yang bocor wewenang, atau belum mampu memetakan kontrol keamanan ke standar NIST/ISO. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai dasar keamanan informasi atau melanggar Pakta Etika Keamanan Siber / integritas akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-418` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menerapkan prinsip **CIA Triad** serta kriptografi simetris (**AES**) dan asimetris (**RSA**). | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menerapkan fungsi *hash* (**SHA-256**), **digital signature**, dan validasi **PKI/TLS** untuk integritas data. | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu menganalisis kerentanan aplikasi web **OWASP Top 10** menggunakan pemindai kerentanan secara etis. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu menerapkan autentikasi **MFA**, kontrol akses **RBAC**, dan prinsip pertahanan jaringan dasar. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu mengevaluasi risiko dan kesiapan respons insiden menggunakan kerangka **NIST CSF 2.0**. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu menilai kontrol keamanan informasi mengacu pada standar **ISO/IEC 27001:2022** dan **UU PDP**. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-418`)

```text
====================================================================================================================================
     LEMBAR REKAPITULASI PENILAIAN OBE — STI-418 DASAR KEAMANAN INFORMASI (2 SKS TEORI: T=2, P=0)
====================================================================================================================================
Semester / TA  : Semester 4 (Genap) / 2026-2027      CPL Dibebankan : CPL-07 (P3: 50%) & CPL-11 (KK3: 50%) [Level: Reinforce]
Klaster Rubrik : K-1 (Fondasi Sains & Komputasi)     Ambang OBE     : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mhs     | T1(20%) | UTS-A(15%) | UTS-B(15%) | T2(20%) | UAS-3.1(15%)| UAS-3.2(15%)| NA    | CPL-07 | CPL-11
   |           |              | [1.1:P3]| [1.2:P3]   | [2.2:KK3]  | [2.1:KK3]| [3.1:P3]   | [3.2:KK3]   | Akhir | (50%)  | (50%)
------------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1] | 88.0    | 86.0       | 88.0       | 90.0    | 88.0        | 88.0        | 88.10 | 87.40  | 88.80
2  | 250101002 | [Nama Mhs 2] | 78.0    | 76.0       | 78.0       | 80.0    | 78.0        | 78.0        | 78.10 | 77.40  | 78.80
3  | 250101003 | [Nama Mhs 3] | 68.0    | 66.0       | 68.0       | 70.0    | 68.0        | 68.0        | 68.10 | 67.40  | 68.80
------------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS               | 78.00   | 76.00      | 78.00      | 80.00   | 78.00       | 78.00       | 78.10 | 77.40  | 78.80
====================================================================================================================================
```
