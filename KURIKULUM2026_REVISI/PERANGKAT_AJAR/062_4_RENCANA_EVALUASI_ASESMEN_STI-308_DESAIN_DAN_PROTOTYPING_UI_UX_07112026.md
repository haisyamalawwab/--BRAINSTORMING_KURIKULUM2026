# 062_4 — RENCANA EVALUASI DAN ASESMEN PEMBELAJARAN BERBASIS OBE
## STI-308 — DESAIN & PROTOTYPING UI/UX (*UI/UX Design & Prototyping*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI308` · **Bobot:** 3 SKS `+P` (`T=2, P=1`) · **Semester:** 3  
**Klaster Asesmen MK (Dok 008 & 018):** Klaster 2 (`K-2`) — Skema Baku MK Praktikum (`+P`: `20% / 25% / 25% / 30%`)  
**CPL Dibebankan:** `CPL-13` (`KK5` = **100%**) [Level `R` — *Reinforce*]  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. ARSITEKTUR EVALUASI 4 TITIK BAKU MK `+P` & KEPATUHAN IKU 7

Sesuai **Dokumen 008 & 043**, sebagai mata kuliah bertipe **`+P` (Praktikum Studio)**, `STI-308 Desain & Prototyping UI/UX` menerapkan distribusi bobot baku **`20% / 25% / 25% / 30%`** dengan pemetaan *1-to-1* ke 4 CPMK:
* **Tugas 1 (Pekan 4 — 20%) → `CPMK-1`** — *User Research & Design Thinking Discovery Brief*.
* **UTS (Pekan 8 — 25%) → `CPMK-2`** — *Hands-on Studio Exam & Project Validation: IA, User Flow, & Wireframe*.
* **Tugas 2 (Pekan 12 — 25%) → `CPMK-3`** — *Figma Design System & WCAG 2.1 AA High-Fidelity Interactive Prototype*.
* **UAS (Pekan 16 — 30%) → `CPMK-4`** — *SUS Usability Testing Report, 10 Heuristics Audit, Redesigned Prototype v2.0 & Portfolio Defense*.
* **Kepatuhan IKU 7 ($\ge 50\%$):** `Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%)` = **75%** berbasis pemecahan kasus & proyek studio tim *(persis selaras dengan angka resmi Dokumen 004 untuk `STI-308` = 75%)*.

---

## 2. MATRIKS DISTRIBUSI BOBOT PENILAIAN TERHADAP CPL, CPMK, & SUB-CPMK (KPT 2024 TABEL 26)

| Kode CPL | Kode CPMK (Bloom) | Kode Sub-CPMK | Pekan Uji | Bentuk & Teknik Penilaian | Instrumen Penilaian | Sifat | Bobot Sub (%) | Total CPMK (%) |
|:---:|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **`CPL-13`**<br>(`KK5` — 100%)<br>*Level: R* | **`CPMK-1`**<br>(C4) | `Sub-CPMK-1.1` | Mg 4 | Proyek eksplorasi kasus nyata: Wawancara kontekstual $\ge 5$ pengguna, *Affinity Diagram*, & *User Persona* | **RTM-1 (Tugas 1)** Bagian Riset + Verifikasi Individu | Sumatif | 11% | **20%** |
| | | `Sub-CPMK-1.2` | Mg 4 | Proyek eksplorasi kasus nyata: Sintesis *Empathy Map*, *Customer Journey Map*, & *POV/HMW Design Thinking* | **RTM-1 (Tugas 1)** Bagian Sintesis + Rubrik T1 | Sumatif | 9% | |
| **`CPL-13`**<br>(`KK5` — 100%)<br>*Level: R* | **`CPMK-2`**<br>(C4) | `Sub-CPMK-2.1` | Mg 8 | Ujian praktik studio Figma (50%) + validasi proyek (50%): *Card Sorting*, *Sitemap*, & *User Flow* | **Soal Praktik UTS** & Berkas IA Proyek + Rubrik UTS | Sumatif | 12% | **25%** |
| | | `Sub-CPMK-2.2` | Mg 8 | Ujian praktik studio Figma (50%) + validasi proyek (50%): *Low-Fidelity Wireframe* ber-*8pt Grid* | **Soal Praktik UTS** & Berkas *Wireframe* + Rubrik UTS | Sumatif | 13% | |
| **`CPL-13`**<br>(`KK5` — 100%)<br>*Level: R* | **`CPMK-3`**<br>(C6) | `Sub-CPMK-3.1` | Mg 12 | Inspeksi milestone studio Figma: *Design System* (*Variables, Auto-Layout, Variants*) & *Hi-Fi Interactive Prototype* | **RTM-2 (Tugas 2)** Berkas `.fig` Proyek + Uji Klik | Sumatif | 16% | **25%** |
| | | `Sub-CPMK-3.2` | Mg 12 | Inspeksi milestone studio Figma: Audit & remediasi aksesibilitas **WCAG 2.1 Level AA** | **RTM-2 (Tugas 2)** Lembar Audit WCAG + Rubrik T2 | Sumatif | 9% | |
| **`CPL-13`**<br>(`KK5` — 100%)<br>*Level: R* | **`CPMK-4`**<br>(C5) | `Sub-CPMK-4.1` | Mg 16 | *Demo Day* & sidang akhir: Eksekusi *Usability Testing* pada $\ge 5$ pengguna & perhitungan kuantitatif **SUS** | **Laporan Uji Kebergunaan** & Sidang UAS + Rubrik UAS | Sumatif | 15% | **30%** |
| | | `Sub-CPMK-4.2` | Mg 16 | *Demo Day* & sidang akhir: Audit **10 Heuristik Nielsen**, iterasi *Before–After* `v2.0`, & studi kasus portofolio | **Purwarupa `v2.0` & Portofolio UI/UX** + Sidang UAS | Sumatif | 15% | |
| **TOTAL** | **4 CPMK** | **8 Sub-CPMK** | **16 Pekan** | **4 Titik Evaluasi Baku MK `+P`** | **4 Paket Instrumen Studio Lengkap** | **Sumatif** | **100%** | **100%** |

---

## 3. RENCANA TUGAS MAHASISWA (RTM) & SPESIFIKASI EVALUASI STUDIO

### 3.1 Rencana Tugas Mahasiswa 1 (RTM-1 — Tugas 1: *User Research & Design Thinking Brief*)
* **Jadwal & Bobot:** Rilis **Pekan 2**, Kumpul & Verifikasi **Pekan 4** · Bobot **20%** (`CPMK-1`).
* **Batasan Luaran Wajib:**
  1. Dokumentasi wawancara kontekstual nyata minimal **5 responden** (masing-masing anggota tim wajib mewawancarai minimal 2 responden berbeda dengan bukti foto/rekaman izin *informed consent*).
  2. Kanvas FigJam terstruktur memuat *Affinity Diagram*, *Empathy Map*, **2 User Persona berbasis bukti**, **Customer Journey Map** kondisi berjalan, serta perumusan **POV & 3 How Might We (HMW)**.
  3. Verifikasi lisan kontribusi per individu di studio Pekan 4.

### 3.2 Spesifikasi Ujian Tengah Semester (UTS — Pekan 8: Ujian Praktik Studio & Validasi IA/Wireframe)
* **Format & Bobot:** Durasi **170 menit** di laboratorium studio · Bobot **25%** (`CPMK-2`), terdiri atas:
  1. **Bagian A — *Live Figma Wireframing Challenge* Individu (50% nilai UTS, 115 menit):** Diberikan 1 narasi kasus singkat layanan baru; setiap mahasiswa wajib merancang secara mandiri di Figma diagram *User Flow* + **4 layar *Low-Fi Wireframe*** yang rapi mengikuti *8pt Grid*, *Auto-Layout* dasar, dan mencakup minimal 1 layar penanganan kesalahan/kondisi kosong.
  2. **Bagian B — Validasi Paket IA & *Wireframe* Proyek Tim (50% nilai UTS, 55 menit):** Pemeriksaan hasil *Card Sorting*, *Sitemap*, *User Flow*, dan 12+ layar *Wireframe* proyek beserta pemeriksaan *Version History* Figma tiap anggota.

### 3.3 Rencana Tugas Mahasiswa 2 (RTM-2 — Tugas 2: *Design System & WCAG Hi-Fi Prototype*)
* **Jadwal & Bobot:** Rilis **Pekan 9**, Inspeksi Studio **Pekan 12** · Bobot **25%** (`CPMK-3`).
* **Batasan Luaran Wajib pada Berkas Figma Proyek:**
  1. Halaman **`01 — Design System`**: memuat *Figma Variables / Design Tokens* (palet warna, skala tipografi, spasi *8pt*, radius), serta minimal **10 komponen induk ber-*Auto-Layout* & *Variants*** (tanpa warna *hardcoded* liar).
  2. Halaman **`02 — Hi-Fi Interactive Prototype`**: minimal **15 layar *High-Fidelity*** yang dirangkai interaktif penuh untuk minimal **3 skenario tugas utama** (setiap anggota tim bertanggung jawab atas minimal 1 alur tugas utuh).
  3. Halaman **`03 — WCAG 2.1 Level AA Audit`**: bukti pemeriksaan rasio kontras ($\ge 4,5:1$ teks normal, $\ge 3:1$ komponen/teks besar), ukuran bidang sentuh $\ge 44\times 44\text{ px}$, indikator status fokus, dan uji simulasi buta warna.

### 3.4 Spesifikasi Evaluasi Akhir Semester (UAS — Pekan 16: *Usability Report, Iteration v2.0, & Demo Day*)
* **Format & Bobot:** Durasi **170 menit** · Bobot **30%** (`CPMK-4`), menilai:
  1. **Laporan & Data Mentah *Usability Testing* ($\ge 5$ Partisipan Eksternal):** tingkat penyelesaian tugas, waktu pengerjaan, tabulasi *Rainbow Spreadsheet*, serta perhitungan lengkap skor **System Usability Scale (SUS)** dan maknanya.
  2. **Matriks Audit *10 Usability Heuristics* Jakob Nielsen:** lengkap dengan tangkapan layar temuan, *Severity Rating* (`0–4`), dan rekomendasi perbaikan.
  3. **Purwarupa Iterasi Final `v2.0` (*Before vs After*) & Naskah Studi Kasus Portofolio UI/UX**, dipertahankan secara individu di hadapan dosen penguji.

---

## 4. FORMULA NILAI AKHIR, KONTRIBUSI `CPL-13`, & PROTOKOL REMEDIAL

### 4.1 Rumus Nilai Akhir & Ketercapaian `CPL-13` (`KK5`)
$$\text{Score}_{\text{CPMK-1}} = S_{\text{Tugas 1}}, \quad \text{Score}_{\text{CPMK-2}} = S_{\text{UTS}}, \quad \text{Score}_{\text{CPMK-3}} = S_{\text{Tugas 2}}, \quad \text{Score}_{\text{CPMK-4}} = S_{\text{UAS}}$$
$$NA_{\text{STI-308}} = 0,20\,S_{\text{Tugas 1}} + 0,25\,S_{\text{UTS}} + 0,25\,S_{\text{Tugas 2}} + 0,30\,S_{\text{UAS}}$$

Karena 100% bobot `STI-308` mendukung **`CPL-13` (`KK5`)** pada level *Reinforce* (`R`):
$$\text{Score}_{\text{CPL-13, STI-308}}(i) = NA_{\text{STI-308}}(i) \quad (\text{bobot SKS tertimbang} = 3 \times 1,00 = 3,00\text{ SKS})$$

### 4.2 Keaslian Karya Figma & Remedial OBE
* **Verifikasi Jejak Versi (*Figma Version History*):** Dosen wajib memeriksa riwayat pengeditan akun masing-masing mahasiswa di Figma untuk mencegah duplikasi templat siap pakai dari *Figma Community* maupun ketimpangan kontribusi tim.
* **Ambang Ketuntasan & Remedial:** Batas minimal kelulusan CPMK/CPL adalah **$\ge 65,0$ (C+)**. Mahasiswa yang memperoleh nilai $< 65,0$ pada salah satu CPMK diberi 1 kali kesempatan perbaikan terarah pada artefak studio terkait dengan skor maksimal pasca-remedial **70,0 (B)**.
