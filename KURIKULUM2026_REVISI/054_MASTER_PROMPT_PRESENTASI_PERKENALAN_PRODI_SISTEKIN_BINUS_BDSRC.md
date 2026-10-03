# 054 — Master Prompt Presentasi Perkenalan Prodi SISTEKIN untuk Tim Kerja Sama BINUS (BDSRC)

| Atribut | Nilai |
|---|---|
| **Keperluan** | Presentasi perkenalan Prodi S1 Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG di hadapan tim kerja sama Universitas Bina Nusantara (BINUS), khususnya Laboratorium AI / **BDSRC (Bioinformatics & Data Science Research Center)** |
| **Tanggal acara** | 1 Oktober 2026 |
| **Durasi deck** | 5 slide (16:9) |
| **Identitas visual** | Dominan **oranye + putih**, aksen **ungu** |
| **Aset logo** | Lihat Bagian 2 (tersedia lokal di `ASSETS_PRESENTASI_BINUS_BDSRC/`) |
| **Presenter** | Ahmad Fairuzabadi, S.Kom., M.Kom. (Kaprodi SISTEKIN) |

---

## Bagian 1 — Cara Pakai

Copy **seluruh isi Bagian 3** (MASTER PROMPT) ke generator presentasi pilihan:
- **ZCode** (tool `presentations:pptx` → hasil `.pptx` siap edit), atau
- AI slide generator (Gamma, Tome, Copilot, dsb.), atau
- Desainer manusia sebagai design brief.

Generator **wajib** mengunduh/memakai aset logo pada Bagian 2 dan **hanya boleh memakai fakta** pada sub-bab "Fakta Kunci" — dilarang mengarang angka, akreditasi, atau nama.

---

## Bagian 2 — Aset Resmi (terverifikasi 30/09/2026)

| Aset | Sumber | Catatan |
|---|---|---|
| Logo Prodi SISTEKIN (lockup horizontal) | `https://sistekin.widyagama.ac.id/assets/images/logo-final.webp` | 799×269, latar transparan; sudah dikonversi → `ASSETS_PRESENTASI_BINUS_BDSRC/logo_sistekin.png` |
| Lambang UWG (perisai) | `https://widyagama.ac.id/wp-content/uploads/2025/11/cropped-Lambang-UWG-Latar-Belakang-Putih-Teks-Hitam-scaled-1.png` | 512×512 PNG → `ASSETS_PRESENTASI_BINUS_BDSRC/lambang_uwg.png` |
| Lambang + teks UWG (lockup horizontal) | `https://widyagama.ac.id/wp-content/uploads/2026/01/lambang_teks.png` | 1640×500 PNG transparan → `ASSETS_PRESENTASI_BINUS_BDSRC/lambang_teks_uwg.png` |
| Logo BINUS & BDSRC (opsional, courtesy) | `https://binus.ac.id` dan `https://research.binus.ac.id/bdsrc/` | Letakkan hanya di slide cover sebagai simbol pertemuan kerja sama; minta versi resmi ke pihak BINUS sebelum diedarkan |
| Logo khusus FSTI | Belum tersedia daring terpisah | Gunakan lockup SISTEKIN (sudah memuat identitas FSTI UWG) atau potong dari materi Instagram `@fsti.uwg` |

---

## Bagian 3 — MASTER PROMPT (copy dari sini)

```
# PERAN
Kamu adalah desainer presentasi eksekutif dan konsultan komunikasi akademik.
Buatkan presentasi PowerPoint profesional 5 slide (16:9) untuk perkenalan
Program Studi S1 Sistem dan Teknologi Informasi (SISTEKIN), Fakultas Sains dan
Teknologi Informasi (FSTI), Universitas Widyagama Malang, di hadapan tim kerja
sama Universitas Bina Nusantara (BINUS) — khususnya BDSRC (Bioinformatics &
Data Science Research Center), pusat riset AI/Big Data BINUS.

# TUJUAN PRESENTASI
1. Memperkenalkan identitas, visi, dan keunggulan SISTEKIN sebagai prodi baru
   berbasis AI.
2. Menunjukkan keselarasan arah riset & kurikulum SISTEKIN dengan fokus BDSRC
   (Big Data, AI, data science) — SISTEKIN memposisikan diri sebagai PARTNER
   INTEGRASI AI ke sistem & platform nyata, bukan kompetitor riset algoritma.
3. Menutup dengan 5 peluang kolaborasi konkret dan ajakan bertindak.

# SPESIFIKASI TEKNIS
- Format: .pptx, 16:9, teks tetap editable (bukan gambar).
- Tepat 5 slide, urutan wajib sesuai rancangan di bawah.
- Bahasa Indonesia formal-dinamis (product-pitch tone, bukan seminar akademik);
  istilah teknis boleh dalam bahasa Inggris (AI, Big Data, Machine Learning).
- Setiap slide maksimal ~40 kata di badan slide; detail disampaikan lisan.

# DESIGN SYSTEM (WAJIB)
Palet warna:
- Oranye utama     #F26A21  (blok besar, header band, angka besar)
- Oranye gradien   #D94E12 → #F26A21  (latar slide cover & penutup)
- Putih            #FFFFFF  (dominan latar slide isi)
- Ungu aksen       #5B2D8E  (garis penegas, ikon, highlight kata kunci,
                             subjudul — porsi kecil, ±10% tiap slide)
- Ungu terang      #7C3AED  (hanya untuk hover-highlight / garis tipis)
- Teks netral      #1F2937 (judul), #4B5563 (isi)

Tipografi:
- Judul: Montserrat Bold (fallback: Arial Black), 32-44 pt.
- Isi: Inter / Open Sans Regular, 16-20 pt; caption 12 pt.
- Angka sorotan (146 SKS, 2025, dsb.): Montserrat ExtraBold 60-72 pt oranye.

Layout:
- Slide cover: latar gradien oranye; lambang UWG kiri-atas, logo SISTEKIN
  kanan-atas (keduanya putih-box bila latar gelap); logo BINUS + BDSRC
  opsional di tengah-bawah dengan caption "Forum Kerja Sama".
- Slide isi: header band oranye tipis berisi judul slide; lambang UWG kecil
  (±0,5 inci) di pojok kanan-atas SETIAP slide; footer strip ungu tipis dengan
  "SISTEKIN FSTI UWG × BINUS BDSRC — 2026" + nomor halaman.
- Ikon: gaya flat monokrom (oranye/ungu), satu keluarga ikon, jangan campur.
- Ruang kosong cukup; tidak ada teks menyentuh tepi (margin min. 0,6 inci).

# FAKTA KUNCI — SATU-SATUNYA SUMBER DATA (LARANG MENGARANG ANGKA/NAMA)
- SISTEKIN diresmikan 4 September 2025, SK Kemendiktisaintek No. 747/B/O/2025.
- Akreditasi: Baik (prodi baru).
- Lokasi: Kampus II, Jl. Borobudur No. 35, Malang (gedung FSTI, lantai 4).
- Kaprodi: Ahmad Fairuzabadi, S.Kom., M.Kom. (bidang HCI).
- Keahlian dosen: machine learning, image processing, text mining, fuzzy logic,
  VR/AR, audio signal processing.
- Total 146 SKS; model pembelajaran problem-solving & project-based.
- Visi 2045: prodi yang bermutu, mandiri, bermartabat, berwawasan global,
  unggul dalam pengembangan sistem & teknologi informasi cerdas terintegrasi
  kecerdasan artifisial serta technopreneurship berbasis kebutuhan masyarakat
  dan industri.
- 4 Profil Lulusan Kurikulum 2026 (Dok. 002): PL-1 Intelligent Information
  Systems & Data/AI Engineer; PL-2 Cloud Infrastructure, Cybersecurity &
  Smart Systems Integrator; PL-3 UI/UX Designer & Digital Platform Engineer;
  PL-4 Digital Technopreneur & IT Product Innovator. (PL-1/PL-2 dari
  peminatan P1/P2, PL-3 dari P3, PL-4 lintas peminatan.)
- Catatan: framing lama "4 area fokus" (AI & Intelligent Systems; IoT &
  Multimedia; UX & Gamification; Semantic Systems & Digital Services) berasal
  dari konten website K2025 — TIDAK dipakai lagi di deck ini (revisi
  30/09/2026, lihat Bagian 4).
- MK unggulan: Machine Learning, Internet of Things, UI/UX, Data Warehouse &
  BI, Smart City (sebagian dengan praktikum).
- Kurikulum OBE 2026 (baru): 3 peminatan @18 SKS — Integrated Smart Systems;
  Cloud Infrastructure & Cybersecurity; Digital Platform Engineering; MBKM
  hingga 20 SKS di semester 6-7; 4 titik asesmen baku per mata kuliah.
- BDSRC BINUS: Bioinformatics & Data Science Research Center, riset Big Data &
  IIoT sensor analytics, AI R&D, bioinformatics/data science.
- Kontak: sistekin.widyagama.ac.id · Instagram/TikTok @fsti.uwg ·
  Universitas Widyagama Malang.

# RANCANGAN 5 SLIDE

## SLIDE 1 — COVER
Latar gradien oranye tua→oranye, lambang UWG kiri-atas, logo SISTEKIN
kanan-atas, logo BINUS & BDSRC di tengah-bawah (caption "Forum Kerja Sama").
- Kicker kecil ungu terang: FORUM KERJA SAMA FSTI UWG × BINUS BDSRC
- Judul (putih, besar): SISTEKIN — S1 Sistem dan Teknologi Informasi
- Subjudul: Fakultas Sains dan Teknologi Informasi · Universitas Widyagama Malang
- Tagline (italik, putih): "Integrator AI ke Sistem & Platform Nyata"
- Baris presenter: Ahmad Fairuzabadi, S.Kom., M.Kom. (Kaprodi) ·
  1 Oktober 2026 · Malang

## SLIDE 2 — PROFIL SINGKAT & VISI 2045
Latar putih, 2 kolom.
- Kolom kiri (angka sorotan oranye besar, 3 stat chip):
  2025 — resmi berdiri (SK Kemendiktisaintek No. 747/B/O/2025) ·
  Baik — status akreditasi · 146 — total SKS
- Kolom kanan: kartu ungu muda berisi ringkasan Visi 2045 (1 kalimat):
  "Unggul dalam pengembangan sistem & teknologi informasi CERDAS terintegrasi
  AI serta technopreneurship berbasis kebutuhan masyarakat dan industri."
- Bawah: 4 pill profil lulusan (label kecil PL-n ungu + nama): PL-1 Intelligent
  Information Systems & Data/AI Engineer · PL-2 Cloud Infrastructure,
  Cybersecurity & Smart Systems Integrator · PL-3 UI/UX Designer & Digital
  Platform Engineer · PL-4 Digital Technopreneur & IT Product Innovator.
- 1 kalimat positioning (tebal, aksen ungu): TI berfokus riset algoritma AI
  murni — SISTEKIN mengintegrasikan AI ke sistem & platform nyata untuk UMKM,
  pendidikan, layanan publik, dan industri kreatif.

## SLIDE 3 — KURIKULUM OBE 2026 BERBASIS PROYEK
Latar putih.
- Baris atas: 3 kartu peminatan (kartu putih, border oranye, ikon ungu):
  P1 Integrated Smart Systems · P2 Cloud Infrastructure & Cybersecurity ·
  P3 Digital Platform Engineering — masing-masing "@18 SKS".
- Baris tengah: strip oranye berisi 4 angka: OBE (Outcome-Based Education,
  Permendikbudristek 53/2023) · Project-Based Learning · MBKM hingga 20 SKS
  (semester 6-7) · 4 titik asesmen baku per mata kuliah.
- Baris bawah: chip MK unggulan: Machine Learning · IoT · UI/UX ·
  Data Warehouse & BI · Smart City.
- 1 kalimat penutup: mahasiswa lulus dengan PORTOFOLIO PROYEK NYATA, bukan
  sekadar transkrip.

## SLIDE 4 — KAPASITAS RISET & SINERGI DENGAN BDSRC
Latar putih, 2 kolom dengan panah sinergi di tengah.
- Kolom kiri "SISTEKIN FSTI UWG" (ikon oranye): keahlian dosen (ML, image
  processing, text mining, fuzzy logic, VR/AR, audio signal processing) ·
  lab komputer, lab multimedia & IoT, ruang kolaborasi · fokus penerapan:
  smart city Malang, UMKM, pendidikan, industri kreatif.
- Kolom kanan "BINUS BDSRC" (ikon ungu): Big Data & IIoT sensor analytics ·
  AI R&D · bioinformatics & data science.
- Tengah bawah, banner oranye: "Kami membawa USE CASE & IMPLEMENTASI;
  BDSRC membawa kedalaman riset & data — kombinasi riset terapan dari
  hulu (model) ke hilir (sistem nyata)."

## SLIDE 5 — PELUANG KOLABORASI & AJAKAN
Latar gradien oranye (echo cover), teks putih, aksen ungu.
- Judul: 5 Peluang Kolaborasi SISTEKIN × BDSRC
- 5 item bernomor (angka ungu terang):
  1. MBKM — magang & riset mahasiswa SISTEKIN di BDSRC (konversi hingga 20 SKS)
  2. Riset & publikasi bersama (AI terapan, big data, smart systems)
  3. Guest lecture & dosen praktisi lintas kampus
  4. Proyek nyata bersama — capstone/penelitian kolaboratif berbasis use case Malang
  5. Community engagement — pemberdayaan digital UMKM & layanan publik
- Baris kontak (ikon + teks): sistekin.widyagama.ac.id · @fsti.uwg ·
  Kampus II Jl. Borobudur No. 35 Malang
- CTA (badge ungu): "Mari mulai dari satu proyek perintis — semester ini."

# GAYA & LARANGAN
- Jangan gunakan kata "prodi kecil/baru rapuh"; framing prodi baru = lincah,
  mutakhir, berorientasi industri.
- Jangan menampilkan angka akreditasi poin/BAN-PT, jumlah mahasiswa, jumlah
  dosen, atau peringkat — tidak tersedia di sumber resmi.
- Jangan menjanjikan kerja sama formal (MoA/MoU) — cukup "peluang kolaborasi".
- Konsisten: SISTEKIN (prodi) = FSTI (fakultas) = Universitas Widyagama
  Malang (UWG); lawan bicara: BINUS & BDSRC.

# CHECKLIST PENERIMAAN (verifikasi sebelum selesai)
[ ] Tepat 5 slide, urutan sesuai rancangan.
[ ] Lambang UWG tampak di semua slide; logo SISTEKIN di cover.
[ ] Dominasi oranye-putih dengan aksen ungu pada SEMUA slide (tidak ada warna
    lain di luar palet).
[ ] Semua angka/nama hanya dari Fakta Kunci; nol karangan.
[ ] Teks badan ≤ ~40 kata per slide; tidak ada teks terpotong/tabrakan.
[ ] Footer + nomor halaman ada di slide 2-5.
```

---

## Bagian 4 — Catatan Penggunaan & Variasi

1. **Versi bilingual:** bila pertemuan berlangsung bilingual (umum di forum BINUS), minta generator menambahkan subjudul bahasa Inggris pada judul tiap slide — jangan menggandakan isi badan slide.
2. **Kontingensi slide:** jika waktu memungkinkan diperpanjang, slide kandidat ke-6 adalah "Roadmap Kolaborasi 2026-2027" (MoA → riset perintis → MBKM batch pertama); jangan digabung ke slide 5 agar CTA tetap tegas.
3. **Logo BINUS/BDSRC:** sebelum presentasi, konfirmasi ke tim BINUS apakah logo mereka boleh tampil di materi kami; jika tidak, hapus dari cover tanpa mengubah layout (kolom teks menyesuaikan otomatis).
4. **Sinkron dengan K2026:** poin "Kurikulum OBE 2026 / 3 peminatan" pada Slide 3 berasal dari konsensus dokumen kurikulum 2026 (Dok. 005/006). Jika saat presentasi struktur peminatan belum disosialisasikan resmi ke publik, ganti framing menjadi "kurikulum baru yang sedang diluncurkan" tanpa mengubah angka.
5. **Log revisi 30/09/2026 — Slide 2:** baris "4 AREA FOKUS" (framing website K2025) diganti menjadi **"4 PROFIL LULUSAN — KURIKULUM 2026"** (PL-1 s.d. PL-4, nama resmi Dok. 002). Alasan: menyelaraskan deck dengan struktur kurikulum 2026 dan menghindari duplikasi dengan 3 peminatan yang sudah tampil di Slide 3. Slide lain tidak berubah.

---

*Dokumen ini adalah master prompt tunggal untuk pembangkitan presentasi; ubah hanya Bagian 3 jika ada keputusan konten baru, dan catat perubahannya di sini.*
