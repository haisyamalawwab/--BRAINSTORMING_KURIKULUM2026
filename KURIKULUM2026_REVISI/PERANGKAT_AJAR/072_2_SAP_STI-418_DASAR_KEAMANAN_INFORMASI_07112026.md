# 072_2 — SATUAN ACARA PERKULIAHAN (SAP) 16 PERTEMUAN
## STI-418 — DASAR KEAMANAN INFORMASI (*Fundamentals of Information Security*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.6.RPS-STI418` · **Bobot:** 2 SKS `Teori` (`TM 100'`, `PT 120'`, `BM 120'`) · **Semester:** 4  
**Prasyarat:** `STI-312` Jaringan Komputer & Komunikasi Data  
**CPL:** `CPL-07` (`P3` = 50%) & `CPL-11` (`KK3` = 50%) [Level `R`] · **Klaster Rubrik:** `K-1`  
**Tanggal Penyusunan:** 07 November 2026  

---

## PEDOMAN OPERASIONAL SAP & PAGAR PEMBATAS KELAS (*CLASSROOM GUARDRAILS*)

| Atribut Pelaksanaan | Ketentuan Baku Dosen Pengampu `STI-418` |
|---|---|
| **Struktur Waktu Tatap Muka (`100'`)** | **Bedah Insiden Nyata (`15'`)** · **Eksposisi Konsep & Demonstrasi Teknis (`55'`)** · **Latihan Analisis Terbimbing (`20'`)** · **Penutup & Refleksi Etika (`10'`)**, diikuti `PT 120'` & `BM 120'`. |
| **Aturan Etika Mutlak (*White-Hat Rule*)** | Seluruh latihan pemindaian kerentanan (**OWASP ZAP**) **HANYA BOLEH** diarahkan ke kontainer target latihan lokal (`127.0.0.1` — *OWASP Juice Shop / DVWA*). Pemindaian tanpa izin tertulis ke domain kampus/publik adalah pelanggaran berat akademik & UU ITE! |
| **Larangan Kelas (*Out-of-Scope*)** | ❌ **Dilarang** membahas eksploitasi biner mendalam, *reverse engineering malware*, & *threat hunting* (`STI-519` & `STB-501`), *offensive red-teaming* lanjut (`STB-602`), maupun audit korporat COBIT 2019 penuh (`STB-701`). |

### Tabel Peta Cepat 16 Pertemuan SAP

| Pertemuan | Sub-CPMK | Topik Inti & Aktivitas Kelas (`100'`) | Waktu | Evaluasi |
|:---:|:---:|---|:---:|---|
| **1** | `Sub-CPMK-1.1` | Pakta Etika Siber, Pilar **CIA Triad**, & Taksonomi Ancaman Modern | 100' | Formatif |
| **2** | `Sub-CPMK-1.1` | Kriptografi Simetris (**AES**), Bahaya ECB vs **AES-GCM**, & Manajemen Kunci | 100' | Formatif |
| **3** | `Sub-CPMK-1.1` | Kriptografi Asimetris (**RSA & ECC**) & Skema **Hybrid Encryption** | 100' | Formatif |
| **4** | `Sub-CPMK-1.1` | Klasifikasi Data Sensitif UU PDP & Verifikasi Studi Kasus **Tugas 1** | 100' | **Tugas 1 (20%)** |
| **5** | `Sub-CPMK-1.2` | Fungsi *Hash* (**SHA-256**), **HMAC**, & Nir-Penyangkalan **Digital Signature** | 100' | Formatif |
| **6** | `Sub-CPMK-1.2, 2.2` | Rantai Kepercayaan **PKI (X.509 & TLS 1.3)** serta **Multi-Factor Authentication** | 100' | Formatif |
| **7** | `Sub-CPMK-2.2` | Model Kontrol Akses (**DAC, MAC, RBAC, ABAC**) & Dasar *Firewall/DMZ/IDS/IPS* | 100' | Formatif |
| **8** | `1.2 & 2.2` | **Ujian Tengah Semester (UTS):** Integritas Kriptografi, PKI/TLS, RBAC, & Perimeter | 100' | **UTS (30%)** |
| **9** | `Sub-CPMK-2.1` | *Vulnerability Assessment*, Skor **CVSS / CVE**, & **OWASP A01–A02** | 100' | Formatif |
| **10** | `Sub-CPMK-2.1` | Bedah & Mitigasi **OWASP A03 Injection (*SQLi, XSS*)** & **A07 Auth Failures** | 100' | Formatif |
| **11** | `Sub-CPMK-2.1` | *Security Misconfiguration*, *Supply Chain*, & Pemindaian **OWASP ZAP** Lokal | 100' | Formatif |
| **12** | `Sub-CPMK-2.1` | Rencana Remediasi Terprioritas & Presentasi Verifikasi **Tugas 2** | 100' | **Tugas 2 (20%)** |
| **13** | `Sub-CPMK-3.1` | Manajemen Risiko Siber (*Risk Matrix, SLE–ARO–ALE*) & Perlakuan Risiko | 100' | Formatif |
| **14** | `Sub-CPMK-3.1` | *Tabletop Exercise* Respons Insiden Berbasis **NIST CSF 2.0** (6 Fungsi) | 100' | Formatif |
| **15** | `Sub-CPMK-3.2` | Evaluasi Kontrol **ISO/IEC 27001:2022 (*Annex A*)**, **UU PDP**, & Klinik UAS | 100' | Formatif |
| **16** | `CPMK-3` | **Evaluasi Akhir Semester (UAS):** Evaluasi Risiko & Kesenjangan *NIST CSF / ISO 27001* | 100' | **UAS (30%)** |

---

## RINCIAN SKENARIO MIKRO 16 PERTEMUAN

### PERTEMUAN 1 — Pakta Etika Siber, **CIA Triad**, & Lanskap Ancaman Siber
* **Sub-CPMK:** `Sub-CPMK-1.1` [C2→C3] · **Aktivitas (`100'`):** Penandatanganan Pakta Etika Keamanan Siber; membedah studi kasus nyata pelumpuhan pusat data akibat *ransomware* dan kebocoran jutaan data pelanggan menggunakan lensa **Confidentiality, Integrity, Availability (CIA Triad)** + *Authenticity & Non-Repudiation*, serta membedakan konsep *Asset, Vulnerability, Threat,* dan *Risk*.
* **PT (`120'`) & BM (`120'`):** Menganalisis 2 berita insiden siber di Indonesia dan memetakan pilar CIA mana yang terdampak utama.

### PERTEMUAN 2 — Kriptografi Simetris (**AES**), Mode Operasi Blok, & Manajemen Kunci
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Aktivitas (`100'`):** Mengapa dilarang keras merancang algoritma "sandi buatan sendiri" (*Don't roll your own crypto!*)? Membedah cara kerja standar **Advanced Encryption Standard (AES-128/256)**, demonstrasi visual kebocoran pola pada mode `ECB` vs keamanan terautentikasi pada **AES-GCM**, serta kesalahan fatal menyimpan kunci enkripsi di repositori Git.
* **PT (`120'`) & BM (`120'`):** Melakukan latihan enkripsi dan dekripsi berkas menggunakan perintah `openssl enc` / pustaka Python `cryptography`.

### PERTEMUAN 3 — Kriptografi Asimetris (**RSA & ECC**) & Skema **Hybrid Encryption**
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] · **Aktivitas (`100'`):** Menghubungkan aritmetika modular prima dari `STI-204 Matematika Diskrit dan Logika` ke pasangan kunci publik-privat **RSA**; menjelaskan mengapa RSA tidak dipakai mengenkripsi berkas video 1 GB secara langsung (lambat!), melainkan digabungkan dalam **Hybrid Encryption** (RSA mengenkripsi kunci sesi acak 256-bit, lalu AES mengenkripsi datanya). Merilis resmi **Tugas 1 (RTM-1)**.
* **PT (`120'`) & BM (`120'`):** Mengerjakan implementasi perlindungan kriptografi hibrida pada **Tugas 1**.

### PERTEMUAN 4 — Klasifikasi Sensitivitas Data (**UU PDP**) & Evaluasi Tugas 1
* **Sub-CPMK:** `Sub-CPMK-1.1` [C3] + **Evaluasi Sumatif Tugas 1 (`CPMK-1`, 20%)** · **Aktivitas (`100'`):** Memetakan kategori Data Pribadi Umum vs Data Pribadi Spesifik (rekam medis, biometrik, keuangan) menurut **UU No. 27 Tahun 2022 (UU PDP)** ke kebijakan enkripsi *Data-at-Rest* dan *Data-in-Transit*; dilanjutkan verifikasi dan tanya-jawab **Tugas 1**.
* **PT (`120'`) & BM (`120'`):** Membaca materi fungsi *hash* satu-arah dan tanda tangan digital.

### PERTEMUAN 5 — Fungsi *Hash* (**SHA-256**), **HMAC**, & **Digital Signature**
* **Sub-CPMK:** `Sub-CPMK-1.2` [C3] · **Aktivitas (`100'`):** Mendemonstrasikan *Avalanche Effect* pada **SHA-256** (mengubah satu titik pada dokumen 500 halaman merombak total 50% bit nilai *hash*!), penggunaan **HMAC** untuk verifikasi *webhook* pembayaran (mis. Midtrans/Xendit pada aplikasi `STI-416`), serta membedah cara kerja **Digital Signature** yang menjamin keaslian pengirim dan nir-penyangkalan (*Non-Repudiation*).
* **PT (`120'`) & BM (`120'`):** Latihan menandatangani berkas PDF/teks dan menguji kegagalan verifikasi saat 1 karakter berkas diubah.

### PERTEMUAN 6 — **Public Key Infrastructure (PKI)**, Sertifikat **X.509 / TLS 1.3**, & **MFA**
* **Sub-CPMK:** `Sub-CPMK-1.2` & `2.2` [C3→C4] · **Aktivitas (`100'`):** Bagaimana peramban Anda yakin kunci publik yang dikirim `klikbca.com` benar-benar milik BCA dan bukan milik peretas Wi-Fi kafe? Membedah peran *Root/Intermediate Certificate Authority (CA)*, anatomi sertifikat **X.509**, jabat tangan cepat **TLS 1.3**, serta evaluasi tingkat kekuatan **Multi-Factor Authentication (MFA)**: kerentanan *SIM-Swap* pada SMS OTP vs keamanan *TOTP Authenticator* dan *FIDO2 Passkeys*.
* **PT (`120'`) & BM (`120'`):** Menginspeksi rantai sertifikat TLS tiga situs layanan publik dan mencatat algoritma kuncinya.

### PERTEMUAN 7 — Model Kontrol Akses (**DAC, MAC, RBAC, ABAC**) & Pertahanan Jaringan Dasar + Klinik UTS
* **Sub-CPMK:** `Sub-CPMK-2.2` [C4] · **Aktivitas (`100'`):** Membandingkan empat paradigma kontrol akses (**DAC** kepemilikan berkas, **MAC** label rahasia militer, **RBAC** peran jabatan organisasi, dan **ABAC** atribut kontekstual jam/lokasi), prinsip emas **Least Privilege** & **Separation of Duties**, serta konsep arsitektur *Defense-in-Depth* jaringan (*Packet-Filtering vs Stateful Firewall, zona DMZ, VPN Tunneling,* dan perbedaan **IDS** vs **IPS**); ditutup klinik persiapan **UTS Pekan 8**.
* **PT (`120'`) & BM (`120'`):** Persiapan mandiri menghadapi UTS tertulis analisis keamanan.

### PERTEMUAN 8 — UJIAN TENGAH SEMESTER (UTS)
* **CPMK Diuji:** `Sub-CPMK-1.2` (`CPMK-1`, 15% `CPL-07`) & `Sub-CPMK-2.2` (`CPMK-2`, 15% `CPL-11`) · **Bobot:** **30%** · **Durasi:** `100 menit`.
* **Pelaksanaan:** Ujian tertulis analisis kasus terawasi mengenai integritas *hash/HMAC*, tanda tangan digital, rantai PKI/TLS, perancangan matriks RBAC bebas konflik wewenang, dan penempatan kontrol keamanan jaringan.

### PERTEMUAN 9 — *Vulnerability Assessment*, Standar **CVE / CVSS**, & **OWASP Top 10 (A01–A02)**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Aktivitas (`100'`):** Evaluasi UTS lalu membedakan secara jernih *Vulnerability Assessment* (menemukan & memprioritaskan daftar celah untuk ditambal) vs *Penetration Testing* (mensimulasikan eksploitasi mendalam di `STB-602`); membaca katalog **CVE** & menghitung vektor keparahan **CVSS**, serta membedah peringkat #1 dan #2 **OWASP Top 10**: `A01 Broken Access Control` & `A02 Cryptographic Failures`.
* **PT (`120'`) & BM (`120'`):** Menjalankan kontainer lokal `OWASP Juice Shop` dan memasang **OWASP ZAP** di mesin lokal.

### PERTEMUAN 10 — Bedah & Mitigasi **OWASP A03 Injection (*SQLi, XSS*)** & **A07 Auth Failures**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Aktivitas (`100'`):** Menganalisis anatomi serangan `' OR 1=1 --` (*SQL Injection*) dan penyuntikan `<script>` pencuri sesi (*Cross-Site Scripting / XSS*) serta kelemahan manajemen sesi/kata sandi (`A07`), lengkap demonstrasi langsung bagaimana *Parameterized Queries*, *HttpOnly Cookie*, dan header `Content-Security-Policy` mematikan serangan tersebut seketika (*selaras ko-semester `STI-416`*). Merilis resmi **Tugas 2 (RTM-2)**.
* **PT (`120'`) & BM (`120'`):** Mengidentifikasi celah injeksi & autentikasi pada aplikasi target lokal untuk **Tugas 2**.

### PERTEMUAN 11 — *Security Misconfiguration*, *Vulnerable Components*, & Pemindaian **OWASP ZAP**
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] · **Aktivitas (`100'`):** Membedah bahaya akun bawaan pabrik/`DEBUG=True` di produksi (`A05 Security Misconfiguration`), pustaka usang ber-CVE seperti tragedi *Log4Shell* (`A06 Vulnerable & Outdated Components`), kurangnya pencatatan audit (`A09`), dan *Server-Side Request Forgery* (`A10`); mendemonstrasikan cara menjalankan pemindaian otomatis & pasif **OWASP ZAP** terhadap target lokal `127.0.0.1:3000` serta memverifikasi temuan agar bebas laporan palsu (*false positive*).
* **PT (`120'`) & BM (`120'`):** Menyusun dokumen *Vulnerability Assessment & Remediation Report* pada **Tugas 2**.

### PERTEMUAN 12 — Penyusunan Rencana Remediasi Terprioritas & Evaluasi Tugas 2
* **Sub-CPMK:** `Sub-CPMK-2.1` [C4] + **Evaluasi Sumatif Tugas 2 (`CPMK-2`, 20%)** · **Aktivitas (`100'`):** Mengajarkan bagaimana menerjemahkan temuan teknis pemindai menjadi rekomendasi perbaikan yang dipahami manajemen dan dapat langsung dikerjakan tim *developer* berdasarkan prioritas **Risiko × Kemudahan Perbaikan**; melaksanakan verifikasi laporan **Tugas 2 (`Sub-CPMK-2.1`)**.
* **PT (`120'`) & BM (`120'`):** Membaca ringkasan eksekutif panduan resmi **NIST CSF 2.0**.

### PERTEMUAN 13 — Manajemen Risiko Keamanan Informasi (*SLE–ARO–ALE & Risk Register*)
* **Sub-CPMK:** `Sub-CPMK-3.1` [C5] · **Aktivitas (`100'`):** Mengapa anggaran keamanan sebesar Rp 500 juta untuk melindungi aset senilai Rp 20 juta adalah keputusan buruk? Melatih penilaian risiko kualitatif (*Matriks 5×5 Likelihood × Impact*) dan kuantitatif (**SLE = Asset Value × Exposure Factor**, **ALE = SLE × ARO**) serta pemilihan 4 opsi perlakuan risiko (*Mitigate, Transfer/Cyber Insurance, Avoid, Accept*).
* **PT (`120'`) & BM (`120'`):** Menyusun tabel *Risk Register* 8 skenario risiko untuk studi kasus proyek **UAS**.

### PERTEMUAN 14 — Evaluasi Kesiapan & Respons Insiden Siber Berbasis **NIST CSF 2.0**
* **Sub-CPMK:** `Sub-CPMK-3.1` [C5] · **Aktivitas (`100'`):** Membedah keenam fungsi inti **NIST Cybersecurity Framework (CSF) 2.0** (**Govern** [fungsi tata kelola baru di v2.0!], **Identify, Protect, Detect, Respond, Recover**); menggelar simulasi meja (*Tabletop Exercise*) pukul 02.00 dini hari ketika server rekam medis rumah sakit terkunci *ransomware*: mengevaluasi langkah *Containment, Eradication, Recovery,* dan pelaporan hukum secara sistematis.
* **PT (`120'`) & BM (`120'`):** Menyusun penilaian profil kesiapan *NIST CSF 2.0* untuk studi kasus UAS.

### PERTEMUAN 15 — Standar **ISO/IEC 27001:2022 (*Annex A*)**, Kepatuhan **UU PDP**, & Klinik UAS
* **Sub-CPMK:** `Sub-CPMK-3.2` [C5] · **Aktivitas (`100'`):** Membedah struktur Sistem Manajemen Keamanan Informasi (**ISMS ISO/IEC 27001:2022** Klausul 4–10 dan 93 kontrol *Annex A* yang dikelompokkan dalam 4 tema: *Organizational, People, Physical, Technological*) serta kewajiban kepatuhan **UU Pelindungan Data Pribadi No. 27 Tahun 2022** (dasar pemrosesan sah, hak subjek data, pejabat DPO, dan notifikasi gagal pelindungan data maks. $3\times 24\text{ jam}$); ditutup klinik UAS dan penjelasan *handoff* menuju `STI-519 Keamanan Informasi Lanjut`.
* **PT (`120'`) & BM (`120'`):** Merampungkan dokumen evaluasi kesenjangan *NIST CSF 2.0 & ISO/IEC 27001* siap sidang UAS.

### PERTEMUAN 16 — EVALUASI AKHIR SEMESTER (UAS)
* **CPMK Diuji:** **`CPMK-3`** (`Sub-CPMK-3.1` [15% `CPL-07`] & `Sub-CPMK-3.2` [15% `CPL-11`] [C5]) · **Bobot:** **30%** · **Durasi:** `100 menit`.
* **Pelaksanaan:** Menggabungkan **Penilaian Dokumen Studi Kasus Evaluasi Risiko Insiden & Kesenjangan Keamanan (*NIST CSF 2.0 & ISO/IEC 27001*) (50% nilai UAS)** dengan **Ujian/Sidang Kasus Evaluasi Keamanan Individu (50% nilai UAS)**.
