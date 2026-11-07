# 073_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STI-519 — Keamanan Informasi Lanjut

**Identitas:** `STI-519` Keamanan Informasi Lanjut · Semester 5 · 3 SKS (Teori) · Prasyarat: `STI-418` · PL-2 · PEO-1 · IRM M · Rubrik K-3.

## 1. Identitas dan otorisasi

Prodi S1 Sistem dan Teknologi Informasi, FSTI Universitas Widyagama Malang. Dosen pengampu, koordinator RMK, tanggal dan tanda tangan: **diisi pada pengesahan**. Beban per minggu: **TM 150 menit + PT 180 menit + BM 180 menit**; PT = penugasan terstruktur, BM = belajar mandiri.

## 2. CPL yang dibebankan

| CPL | Rumusan Dok 003 | IRM |
| --- | --- | --- |
| `CPL-12` (`KK4`) | Mampu merancang tata kelola TI (*IT Governance*), melakukan audit sistem informasi, serta memastikan kepatuhan terhadap standar industri dan manajemen risiko (COBIT, ITIL, ISO 27001). | M |
| `CPL-07` (`P3`) | Menguasai prinsip dan konsep infrastruktur TI, jaringan komputer, komputasi awan (*cloud*), keamanan informasi & siber, tata kelola TI, serta manajemen proyek sistem dan teknologi informasi. | M |
| `CPL-11` (`KK3`) | Mampu merancang, mengintegrasikan, dan mengelola infrastruktur komputasi awan (Cloud/DevOps), sistem sensor cerdas (IoT), dan ketahanan siber (*Cybersecurity*) secara andal, terukur, dan aman. | M |

## 3. CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD (Dok 043) | Bloom | CPL (Dok 004) |
| --- | --- | --- | --- |
| `CPMK-1` | Mahasiswa (*A*) mampu **merancang dan mengeksekusi** tahapan uji penetrasi keamanan (*Penetration Testing*) (*B*) sesuai standar PTES dan MITRE ATT&CK (*C*) dengan etika *Red Teaming* profesional (*D*). | C4 | CPL-12 (KK4) |
| `CPMK-2` | Mahasiswa (*A*) mampu **melakukan** audit sistem manajemen keamanan informasi (*B*) berdasarkan klausul dan kontrol keamanan ISO/IEC 27001:2022 (*C*) dalam bentuk dokumen Statement of Applicability (SoA) (*D*). | C4 | CPL-07 (P3), CPL-11 (KK3) |
| `CPMK-3` | Mahasiswa (*A*) mampu **menyusun** rencana tanggap insiden (*Incident Response Plan*) dan melakukan analisis forensik digital dasar (*B*) pada kasus insiden kebocoran data (*C*) secara terstruktur (*D*). | C5 | CPL-11 (KK3), CPL-12 (KK4) |

| Kode | Kompetensi spesifik Dok 043 | CPMK menurut Dok 043 | Bloom |
| --- | --- | --- | --- |
| `Sub-CPMK-1.1` | Menganalisis tahapan penetration testing sesuai standar PTES dan MITRE ATT&CK. | `CPMK-1` | C4 |
| `Sub-CPMK-1.2` | Mengonfigurasi vulnerability assessment menggunakan OpenVAS/Nessus. | `CPMK-1` | C4 |
| `Sub-CPMK-2.1` | Mengidentifikasi kerentanan aplikasi web OWASP Top 10 menggunakan BurpSuite. | `CPMK-2` | C4 |
| `Sub-CPMK-2.2` | Menganalisis binary dasar menggunakan reverse engineering (Ghidra). | `CPMK-2` | C4 |
| `Sub-CPMK-3.1` | Mengevaluasi proses incident response pada insiden keamanan. | `CPMK-3` | C5 |
| `Sub-CPMK-3.2` | Mengevaluasi kepatuhan terhadap kontrol audit ISO/IEC 27001. | `CPMK-3` | C5 |

## 4. Analisis pembelajaran dan korelasi penilaian

Alur belajar: pengenalan dan pemodelan → penerapan dan analisis → integrasi serta evaluasi. Penilaian bersifat kumulatif; pengalokasian nilai CPMK berikut merupakan rancangan operasional, bukan bobot resmi CPL prodi.

| CPMK | CPL terkait | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | CPL-12 (KK4) | 20% | 30% | — | — | 50% |
| CPMK-2 | CPL-07 (P3), CPL-11 (KK3) | — | — | 20% | — | 20% |
| CPMK-3 | CPL-11 (KK3), CPL-12 (KK4) | — | — | — | 30% | 30% |
| Total | — | 20% | 30% | 20% | 30% | 100% |

CPL yang didukung bersama oleh sebuah CPMK menggunakan **bukti yang sama**; nilai tidak dijumlahkan ulang sebagai persentase nilai akhir. Cara menghitung capaian masing-masing CPL dijelaskan di dokumen 4.

**IKU 7:** Tugas 1 (20%) + Tugas 2 (20%) + UAS (30%) = 70% nilai direncanakan melalui case method / proyek tim. Target Dok 004 70% (untuk peminatan menggunakan baris STA/B/C semester 5). Bentuk ini adalah rencana operasional, bukan klaim realisasi; simpan bukti kerja sama, aktivitas dan penilaian individual. Persentase jenis metode berbeda dari komposisi indikatif Dok 004 dan memerlukan validasi prodi.

## 5. Deskripsi dan rencana 16 pertemuan

Mata kuliah mengembangkan kompetensi sesuai CPMK melalui kasus di atas dengan aplikasi web latihan lokal, Burp Suite, OpenVAS/Nessus, Ghidra dan log simulasi. Teknik penilaian dan indikator spesifik tiap instrumen ada pada dokumen 4 dan 5.

| Mg | Sub-CPMK terkait | Kemampuan / indikator | Materi | Metode | Alokasi belajar per minggu | Asesmen |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sub-CPMK-1.1 | Mampu menguraikan etika Red Teaming dan metodologi standar PTES (C2) | Pengantar Penetration Testing, Standar PTES, Hukum & Etika Ethical Hacking | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 2 | Sub-CPMK-1.1 | Menganalisis informasi aset fiktif dan ruang lingkup yang disetujui. | Pengumpulan informasi secara terbatas | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 3 | Sub-CPMK-1.2 | Mengonfigurasi pemindaian pada target lab berizin dan memvalidasi temuan. | Manajemen kerentanan CVE/CVSS dan pemindaian lokal | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 4 | Sub-CPMK-2.1 | Mengidentifikasi kerentanan pada aplikasi latihan dan merekomendasikan remediasi. | OWASP Top 10 dan bukti kerentanan aplikasi | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Tugas 1 (20%) |
| 5 | Sub-CPMK-1.1 | Menganalisis kontrol identitas dan lapisan pertahanan pada kasus. | Zero Trust dan defense in depth pada aplikasi | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 6 | Sub-CPMK-2.2 | Menganalisis biner contoh yang aman tanpa eksploitasi kernel. | Reverse engineering biner dasar dengan Ghidra | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 7 | Sub-CPMK-1.1 | Menyusun laporan temuan dan memetakan taktik yang relevan. | Pelaporan PTES dan pemetaan MITRE ATT&CK | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 8 | Sub-CPMK-1.1, Sub-CPMK-1.2, Sub-CPMK-2.1, Sub-CPMK-2.2 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Praktik Penetration Testing & Analisis Laporan Kerentanan | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | UTS (30%) |
| 9 | Sub-CPMK-3.2 | Mampu menguraikan struktur standar ISO/IEC 27001:2022 Klausul 4-10 (C2) | Standar ISO/IEC 27001:2022: Konteks Organisasi, Kepemimpinan, Operasi | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 10 | Sub-CPMK-3.2 | Mampu menganalisis 93 kontrol keamanan Annex A ISO/IEC 27001:2022 (C4) | Kontrol Keamanan Annex A: Organisasional, Orang, Fisik, Teknologi | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 11 | Sub-CPMK-3.2 | Mampu menyusun dokumen Statement of Applicability (SoA) & Gap Analysis (C4) | Audit Keamanan: Penyusunan Dokumen SoA & Analisis Kesenjangan Sistem | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 12 | Sub-CPMK-3.2 | Mampu menganalisis risiko keamanan siber berbasis ISO 27005 & NIST SP 800-30 (C4) | Manajemen Risiko Siber: Risk Assessment, Risk Treatment Plan (RTP) | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Tugas 2 (20%) |
| 13 | Sub-CPMK-3.1 | Mampu merancang prosedur kerja Computer Security Incident Response Team (C5) | Manajemen Insiden Siber: CSIRT Workflow, Triase Insiden, Kontaimen | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 14 | Sub-CPMK-3.1 | Menyusun langkah preservasi dan chain of custody pada kasus simulasi tanpa forensik memori tingkat rendah. | Preservasi bukti digital dasar | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 15 | Sub-CPMK-3.2 | Mampu menyusun Dokumen Kebijakan Keamanan Informasi (ISMS Policy) (C5) | Penyusunan Kebijakan Keamanan Organisasi & Simulasi Audit Eksternal | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | Formatif, tanpa bobot |
| 16 | Sub-CPMK-3.1, Sub-CPMK-3.2 | EVALUASI AKHIR SEMESTER (UAS) | Evaluasi Komprehensif Laporan Uji Penetrasi Profesional & Naskah Audit ISO 27001 | Case method / proyek; diskusi dan latihan | TM 150 menit + PT 180 menit + BM 180 menit | UAS (30%) |

## 6. Ringkasan instrumen

- **Tugas 1 (20%, pekan 4): Rencana dan asesmen kerentanan** — Rumuskan ruang lingkup dan aturan keterlibatan; identifikasi risiko aplikasi latihan, klasifikasi CVE/CVSS dan langkah mitigasi. Bukti: Rules of engagement, inventaris aset, bukti hasil pemindaian dan rekomendasi. Cek: otorisasi dan batas target; ketepatan CVSS; bukti dapat ditelusuri.
- **UTS (30%, pekan 8): Ujian analisis penetrasi aplikasi** — Analisis temuan OWASP pada aplikasi uji dan petakan tahapan PTES ke MITRE ATT&CK; susun validasi non-destruktif. Bukti: Jawaban kasus individual, matriks temuan-bukti-mitigasi. Cek: validitas temuan dan perbedaan indikasi dengan bukti; prioritas perbaikan.
- **Tugas 2 (20%, pekan 12): Audit kontrol dan SoA** — Dari skenario organisasi, petakan kontrol ISO/IEC 27001:2022 dan bukti, lalu susun SoA dan gap. Bukti: Matriks kontrol, alasan penerapan/pengecualian, bukti dan rencana tindak lanjut. Cek: keterlacakan klausul, keputusan SoA dan kelayakan tindakan.
- **UAS (30%, pekan 16): Respons insiden dan pertahanan** — Evaluasi skenario kebocoran, urutkan triase, containment, preservasi bukti dasar dan komunikasi insiden; kaitkan audit dan hasil uji. Bukti: Incident response plan, kronologi, rekomendasi hardening dan presentasi. Cek: prioritas dampak, preservasi bukti, batas kewenangan dan kelayakan pemulihan.

## Acuan, batas dan keputusan penyelarasan

**BoK (Dok 043):** `BK-IS06` *Information Security*, `BK-IT06` *Cybersecurity Principles*. Klasifikasi pembina menurut Dok 004: primer BK-IS06 dan BK-IT06.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Keamanan Sistem Operasi Lanjut, Zero Trust Architecture, Manajemen Kerentanan (CVE/CVSS), Security Information & Event Management (SIEM dasar), Penetrasi Web Dasar (OWASP Top 10), Defense in Depth.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang forensik memori tingkat rendah, eksploitasi zero-day kernel, penyusunan roadmap arsitektur keamanan korporasi.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Menguasai hardening dan pertahanan sistem; menyerahkan manajemen risiko dan kepatuhan ke `STB-602`.

**Catatan rekonsiliasi:** Dokumen 043 mengaitkan Sub-CPMK-2.1/2.2 (OWASP/biner) dengan CPMK-2 (audit), dan Sub-CPMK-3.2 (audit) dengan CPMK-3 (insiden); bukti teknis digunakan lintas CPMK. Jadwal mengikuti kompetensi substansinya, bukan menyembunyikan ketidaksesuaian ini. Materi agresif Dok 007 dibatasi menjadi analisis etis lokal; forensik memori tingkat rendah diserahkan ke STB-501. Identitas dan prasyarat mengikuti Dok 005/051; rumusan CPMK/Sub-CPMK mengikuti Dok 043, tema mingguan mengadaptasi Dok 007 sepanjang tidak melanggar batas Dok 037/043. Ketidakcocokan antardokumen dicatat untuk validasi koordinator, bukan diubah diam-diam.

**Skenario terapan:** Aplikasi layanan kampus memiliki laporan kerentanan; hanya lingkungan uji terisolasi dengan izin tertulis yang boleh digunakan.

**Sumber:**
1. Dokumen 003 dan 004: rumusan CPL, matriks IRM dan BoK.
2. Dokumen 005 dan 051: identitas, beban dan prasyarat mata kuliah.
3. Dokumen 007 dan 043: CPMK, Sub-CPMK dan rencana pembelajaran.
4. Dokumen 008 dan 018: pengukuran OBE dan klaster asesmen.
5. Dokumen 037 dan 043: boundary guardrails dan handoff.
6. Rujukan teknis: PTES Technical Guidelines; MITRE ATT&CK; ISO/IEC 27001:2022; OWASP Top 10.
