# KDS-2026 — Survey, Analisis Kritis, dan Pemetaan Kebutuhan Dosen SISTEKIN 2026–2027
## Bidang Kajian & Konsentrasi · Bidang Ilmu · Rumpun Ilmu menurut nomenklatur SISTER Kemdiktisaintek

> **Status: DRAF [U], belum disahkan.** Dokumen ini menilai kecukupan dan kesesuaian dosen Program Studi S1 **Sistem dan Teknologi Informasi (SISTEKIN)**, Fakultas Sains dan Teknologi Informasi (FSTI), Universitas Widya Gama Malang (UWG), untuk periode **2026/2027**, lalu memetakan setiap dosen ke **Rumpun Ilmu → Pohon Ilmu → Cabang Ilmu → Ranting Ilmu** sesuai nomenklatur yang dipakai SISTER Kemdiktisaintek.
>
> **Kode dokumen: KDS-2026** (*Kebutuhan Dosen SISTEKIN*). Berkas ini sengaja **tidak** memakai nomor `000`–`054` (namespace dokumen induk) maupun `055`–`100` (namespace perangkat ajar), sesuai `PERANGKAT_AJAR/README.md` butir 2 dan `AGENTS.md` butir 9.
>
> Berkas terkait: [PKR-2026 pemetaan klaster](PEMETAAN_KLASTER_RANTING_ILMU_SISTEKIN_CS2023_APTIKOM_10112026.md) · [005 struktur & peminatan](005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md) · [013 rekomendasi mitigasi](013_REKOMENDASI_SOLUSI_DAN_MITIGASI_KELEMAHAN_KURIKULUM.md) · [025 cross-track 2027](025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md)

---

## 1. Ringkasan eksekutif

| Temuan | Angka | Konsekuensi |
|---|---|---|
| Prodi baru, SK pendirian **747/B/O/2025** (4 September 2025) | usia ~14 bulan | Rasio dan DTPS masih "sehat" semata karena mahasiswa sedikit, bukan karena kapasitas |
| Mahasiswa aktif 2026 | **7 orang** (PDDIKTI: 5 terdaftar; rasio 1:1,25) | Rasio rasmi **tidak informatif** — lihat §4.1 |
| Proyeksi 2027 | **10–15 orang** | Rasio DTPS 1:2 s.d. 1:3; skor LAM INFOKOM untuk rasio justru **rendah** (lihat §3.2) |
| Dosen tetap homebase SISTEKIN (PDDIKTI, Gasal 2026) | **5 orang**, semua S2 | Lolos ambang minimal 5, **belum** lolos skor penuh |
| Lektor | **2 orang** | 40% DTPS — di bawah ambang skor 4 |
| Proyeksi Asisten Ahli | **2 orang** | AA bukan masalah; yang bermasalah komposisi Lektor+ |
| Calon Doktor (S3) | **2 orang** | 40% — di bawah 50% untuk skor penuh S3 |
| Kaprodi | Lektor, **homebase prodi lain** (Bisnis Digital) | Legal, tetapi menciptakan **C-1** pada §5.3 |
| Beban SKS prodi yang harus ditutup | **30–36 SKS per semester** (146 SKS ÷ 8) | 5 dosen × 12 SKS = 60 SKS kapasitas → beban mengajar **bukan** kendala |
| **Kendala riil** | **Sebaran bidang** + **administrasi SISTER** | 4 dari 29 MK inti tidak punya pengampu berbidang (lihat §4.3) |

**Tiga kesimpulan pokok:**

1. **Jumlah dosen bukan masalah; sebaran dan legalitas administrasilah masalahnya.** Lima dosen tetap sudah memenuhi ambang minimal, dan kapasitas mengajar tiga kali lipat kebutuhan. Yang tidak dimiliki prodi adalah **dosen berbidang jaringan/siber, sistem operasi/infrastruktur, dan tata kelola SI** — padahal ketiganya adalah tulang punggung klaster P2 dan 9 MK inti.
2. **Satu-satunya rekrutmen yang benar-benar mendesak pada 2027 adalah 1 dosen bergelar Doktor** di bidang infrastruktur/jaringan/keamanan siber, dengan syarat rumpun SISTER harus **Ilmu Formal → Komputer**. Ini menutup tiga celah sekaligus: 50% DTPS S3, kompetensi klaster P2, dan kesesuaian bidang untuk akreditasi.
3. **Risiko terbesar bukan kekurangan dosen, melainkan ketidaksesuaian Rumpun Ilmu SISTER.** Karena SISTER mewajibkan rumpun dipilih berdasarkan **ijazah tertinggi**, bukan homebase, dua dosen SISTEKIN berpotensi tercatat pada cabang di luar Komputer — dan itu memutus rantai bukti "DTPS berbidang sesuai kompetensi inti prodi" yang menjadi basis hampir seluruh butir Kriteria 4 LAM INFOKOM.

---

## 2. Metode, sumber, dan batas bukti

### 2.1 Sumber yang dipakai

| Kode | Sumber | Dipakai untuk |
|---|---|---|
| **[S]** | `005` — struktur 146 SKS/55 MK, sebaran 8 semester | Beban MK dan sebaran semester |
| **[S]** | `PKR-2026` — pemetaan klaster, 21 BK-IS + 15 BK-IT | Kesamaan bidang MK ↔ klaster |
| **[S]** | `013`, `025` — mitigasi dan rekomendasi cross-track | Kapasitas dan rencana pengembangan |
| **[P]** | PDDIKTI — detail prodi 59201 (tangkapan layar pengguna, Gasal 2026) | Jumlah dosen, pendidikan, rasio |
| **[P]** | Situs resmi `sistekin.widyagama.ac.id` — halaman prodi & direktori dosen | Nama, jabatan struktural, bidang kepakaran naratif |
| **[R]** | SISTER Kemdiktisaintek — Informasi Umum Rumpun Ilmu; Tahapan Pengisian; Tahapan Validasi | Hierarki dan aturan pengisian rumpun |
| **[R]** | Kepdirjen Dikti **163/E/KPT/2022** | Nama prodi 201 *Sistem dan Teknologi Informasi*; inisial rumpun **Kom** |
| **[R]** | Permendikbud **124/2014** (rumpun, pohon, cabang ilmu) dan **154/2014** (rumpun & gelar) | Definisi 6 rumpun; rumpun formal = sistem formal teoritis |
| **[R]** | Daftar Rumpun, Pohon, dan Cabang Ilmu SISTER (versi 5 Juni 2024) | Nama resmi cabang ilmu di pohon Komputer |
| **[R]** | LAM INFOKOM — instrumen APS/LKPS 2.1 | Ambang dan rumus skor DTPS, S3, jabfung, rasio |
| **[R]** | UU 14/2005 Pasal 72; Permendikbud 3/2020 Pasal 30 | BKD 12–16 SKS; pembimbing utama ≤10 mahasiswa |

### 2.2 Batas bukti yang harus diakui

- **PDDIKTI tidak dapat dibaca langsung** dari lingkungan ini (halaman memuat konten dinamis; API menolak koneksi). Angka dosen dan mahasiswa diambil dari **tangkapan layar yang pengguna kirim**. Rincian seperti NIDN tiap dosen pada daftar "Dosen Penghitung Rasio" tidak dapat diverifikasi silang.
- **Website prodi memuat konten yang saling bertentangan** (§4.1). Saya menandai kontradiksinya, tidak memilih salah satu tanpa bukti.
- **Bidang kepakaran dosen di direktori website adalah narasi pemasaran**, bukan data SISTER. Pemetaan rumpun di §5 adalah **usulan berbasis gelar + jejak publikasi**, **bukan** salinan isian SISTER.
- **Data jabatan fungsional** hanya tersedia agregat ("2 Lektor"). Saya **tidak** tahu siapa yang Lektor; §5.3 memakai tanda `[?]` dan **harus** dikonfirmasi ke Bagian Kepegawaian.
- **Tidak ada data** jumlah mahasiswa per angkatan, status dosen (DTP/DTT), NIDK/NIDN per orang, atau homebase resmi tiga dosen yang menurut pengguna berada di luar SISTEKIN.
- **Nama-nama pada daftar "Dosen Penghitung Rasio" (10 nama) tidak seluruhnya dapat dicocokkan** dengan 5 nama pada daftar "Tenaga Pendidik" ber-NIDN. Lihat C-2 di §4.2.

---

## 3. Dasar normatif: apa yang sebenarnya diukur oleh aturan

### 3.1 Rumpun Ilmu di SISTER — hierarki dan aturan pemilihan

SISTER memakai hierarki **Rumpun Ilmu → Pohon Ilmu → Kelompok Ilmu → Cabang Ilmu → (Ranting Ilmu)**.

| Lapis | Wajib? | Keterangan resmi |
|---|---|---|
| **Rumpun Ilmu** | **Wajib** | 6 rumpun menurut UU 12/2012 Pasal 10 & Permendikbud 124/2014 |
| **Pohon Ilmu** (Bidang Ilmu Utama) | **Wajib** | Turunan langsung rumpun |
| **Kelompok Ilmu** | **Wajib** | Muncul pada panduan pengisian 2024 |
| **Cabang Ilmu** | **Opsional** | Boleh dikosongkan |
| **Ranting Ilmu** | **Tidak diisi dosen** | Diisi **operator PAK** saat pengajuan kenaikan jabatan |

**Aturan pemilihan yang menentukan seluruh analisis di dokumen ini** (kutipan makna, bukan verbatim):

> Rumpun ilmu dipilih berdasarkan **pendidikan formal tertinggi dan terakhir (S2/S3)** — terutama ketika harus memilih di antara cabang ilmu — dan **tidak** berdasarkan homebase atau prodi tempat dosen saat ini ditugaskan. Jika pengajaran dan pendidikan selaras, pemilihan boleh mengacu pada pengajaran.

Konsekuensi yang sering disalahpahami:

1. **Homebase prodi tidak menentukan rumpun.** Dosen berhomebase SISTEKIN tetap boleh (dan harus) tercatat pada rumpun ijazahnya. Ini **sah** dan bahkan **dianjurkan** — tetapi punya konsekuensi akreditasi (§3.3).
2. **Rumpun Ilmu ≠ Bidang Ilmu ≠ Bidang Kajian.** Tiga istilah ini sering tertukar dalam dokumen prodi:

| Istilah | Milik siapa | Isi | Contoh SISTEKIN |
|---|---|---|---|
| **Rumpun/Pohon/Cabang/Ranting Ilmu** | **Dosen** (SISTER) | Taksonomi ijazah & kepakaran dosen | Formal → Komputer → Ilmu Komputer/Informatika → *machine learning* |
| **Bidang Ilmu / Body of Knowledge** | **Prodi** | Isi keilmuan kurikulum | 21 BK-IS + 15 BK-IT (Dokumen 003) |
| **Bidang Kajian / Konsentrasi** | **Prodi** | Pengelompokan MK & jalur minat | 3 klaster: P1, P2, P3 (PKR-2026) |

Kesalahan mencampur ketiganya adalah **akar** dari banyak temuan di §4.3 dan §8.
3. **Rumpun Ilmu kini menjadi gerbang layanan**: dipakai untuk **BKD mulai Gasal 2024/2025**, **Serdos mulai Gelombang 2/2024**, dan **kenaikan jabatan peralihan**. Rumpun yang salah **bukan** kesalahan administratif ringan — ia memblokir karier dosen.
4. **Rumpun Ilmu tidak menggantikan** data Serdos yang sudah ada; keduanya tercatat berdampingan.

### 3.2 Prodi 59201 dalam nomenklatur resmi

| Atribut | Nilai | Dasar |
|---|---|---|
| Kode prodi | **59201** | PDDIKTI (detail prodi); struktur digit dibahas di catatan di bawah |
| Nama resmi | **Sistem dan Teknologi Informasi** / *Information System and Technology* | Kepdirjen 163/E/KPT/2022, no. 201 |
| Inisial gelar | **Kom** (S.Kom.) | Kepdirjen 163/E/KPT/2022 Ketiga |
| **Rumpun Ilmu** | **Rumpun Ilmu Formal** (Formal Sciences) | UU 12/2012; Permendikbud 124/2014 Pasal 5 ayat (5) |
| **Pohon Ilmu** | **Komputer** (Computer) | Daftar Rumpun–Pohon–Cabang Ilmu SISTER |
| **Cabang Ilmu** | **Sistem dan Teknologi Informasi** (Information System and Technology) — tersedia sebagai cabang resmi | idem |

> **Catatan kode 59201 vs 57101.** Kode prodi membaca: `5` = S1, `9` = ... , `2` = rumpun, `01` = prodi. Kode **59201** yang dipakai UWG **berbeda digit rumpunnya** dari contoh umum `57101`/`57201` yang beredar untuk prodi sejenis. **Saya tidak dapat memverifikasi pembacaan digit ini** karena tabel kodefikasi resmi tidak terbaca utuh dari sumber yang dapat saya akses. Ini masuk daftar **U-01** dan **wajib** dikonfirmasi ke PDDIKTI/LLDIKTI — bila digit rumpun pada kode prodi tidak konsisten dengan Rumpun Ilmu Formal, **seluruh rantai bukti rumpun prodi perlu ditinjau**.

Dua fakta yang menguntungkan prodi:

- **"Sistem dan Teknologi Informasi" adalah cabang ilmu resmi** di pohon Komputer — bukan nama karangan. Rantai **Formal → Komputer → Sistem dan Teknologi Informasi** dapat dipertanggungjawabkan apa adanya.
- Pohon Komputer menyediakan cabang yang **sangat** relevan dengan tiga klaster SISTEKIN — daftar lengkap di §5.1.

### 3.3 Ambang LAM INFOKOM yang dipakai di dokumen ini

Dirangkum dari instrumen APS/LKPS LAM INFOKOM (versi 2.1) dan matriks penilaian yang beredar:

| Butir | Rumus | Skor 4 | Catatan |
|---|---|---|---|
| **Kecukupan DTPS** | NDTPS | **≥ 12**, atau 5 ≤ NDTPS < 12 dengan **PDTT ≤ 40%** | NDTPS < 5 → **skor 0** |
| **Kualifikasi akademik** | PDS3 = NDS3/NDTPS | **≥ 50%** | Sarjana: S3 > 50% |
| **Jabatan akademik** | PGBLKL = (GB+LK+L)/NDTPS | **≥ 70%** (sarjana) | Di bawah 70% → skor = 2 + (20 × PGBLKL)/7 |
| **Rasio mahasiswa** | RMD = NM/NDTPS | **15 ≤ RMD ≤ 25** | Sumber lain: skor 4 bila **≤ 1:60** |

**Definisi DTPS yang krusial:** *dosen tetap yang ditugaskan sebagai pengampu mata kuliah **dengan bidang keahlian yang sesuai dengan kompetensi inti prodi***. DTPS **tidak harus** berhomebase di prodi yang diakreditasi — *resource sharing* diperbolehkan — **selama** tridharma-nya sesuai BoK prodi.

**Dua jebakan yang harus disadari:**

1. **Untuk prodi kecil, rasio yang rendah justru menurunkan skor.** Dengan 7 mahasiswa dan NDTPS 5, RMD = 1,4 → **di bawah** ambang 15. Bila instrumen yang berlaku memakai pita 15–25, skor rasio SISTEKIN **rendah bukan karena kekurangan dosen, melainkan karena kekurangan mahasiswa**. Ini kebalikan dari intuisi umum dan sering luput dari pembahasan prodi baru.
2. **Ambang "NDTPS ≥ 12" tidak terjangkau dan tidak perlu dikejar.** Pita skor 5–12 masih memberi skor baik bila PDTT ≤ 40%. Mengejar 12 DTPS untuk 10–15 mahasiswa akan menghancurkan efisiensi dan justru memperburuk rasio.

### 3.4 Beban kerja, pembimbingan, dan EWMP

| Ketentuan | Angka | Dasar |
|---|---|---|
| BKD minimum–maksimum | **12–16 SKS** per semester | UU 14/2005 Pasal 72(2); PP 37/2009 Pasal 8 |
| Pendidikan + penelitian minimum | **9 SKS** | PP 37/2009 |
| Dosen dengan tugas tambahan (Kaprodi) | pendidikan minimal **3 SKS** | Pedoman BKD |
| Tugas belajar (S3) | laporan kemajuan **setara 12 SKS** | Pedoman BKD |
| Pembimbing utama TA | **≤ 10 mahasiswa** | Permendikbud 3/2020 Pasal 30(3) |
| EWMP | acuan 12–16 SKS | Permendikbud 3/2020 Pasal 30(4) |

**Implikasi untuk SISTEKIN:** dengan 7 mahasiswa (2026) dan 15 mahasiswa (2027), **pembimbingan TA bukan kendala sama sekali** — batas 10/dosen berarti kapasitas 50 bimbingan untuk 5 DTPS. Kekhawatiran "dosen kurang untuk membimbing" **tidak berdasar** pada skala ini.

---

## 4. Survey: kondisi riil SISTEKIN 2026

### 4.1 Data dasar dan kontradiksinya

| Variabel | Nilai 2026 | Nilai proyeksi 2027 | Sumber |
|---|---|---|---|
| Mahasiswa aktif | **7** (PDDIKTI menampilkan 5 terdaftar) | **10–15** | [P] tangkapan layar; proyeksi pengguna **[U]** |
| Dosen tetap (PT) | **5** | ? | [P] |
| Dosen tidak tetap | **0** | ? | [P] |
| Total dosen | **5** | ? | [P] |
| Dosen penghitung rasio | **4** | ? | [P] |
| Rasio dosen:mahasiswa (PDDIKTI) | **1 : 1,25** | 1 : 2 s.d. 1 : 3 | hitung: 5/4? lihat catatan |
| Status | **Aktif** | — | [P] |
| Peringkat akreditasi | **Baik** | — | [P] & website |
| Jenjang | **S1** | — | [P] |

> **Catatan aritmetika:** PDDIKTI menulis "1:1,25". Dengan 5 mahasiswa dan 4 dosen penghitung rasio, 5/4 = **1,25** — jadi rasio itu **mahasiswa per dosen**, bukan sebaliknya. Dengan 7 mahasiswa dan 4 dosen penghitung rasio, rasio menjadi **1,75**. Angka ini penting karena **basis rasio adalah "dosen penghitung rasio" (4), bukan total dosen (5)**.

**Tiga kontradiksi di website prodi** yang harus dibereskan sebelum dokumen apa pun dipublikasikan:

| # | Kontradiksi | Bukti |
|---|---|---|
| K-1 | Halaman prodi menyebut **"5 Dosen Homebase"**, tetapi halaman direktori menampilkan **6 dosen berlabel "Sistem dan Teknologi Informasi"** | Halaman utama vs `direktori-dosen.html` — **baik** Fairuzabadi (Kaprodi) maupun Fairuzabadi disebut berhomebase **Bisnis Digital**, sementara daftar lainnya memuat **Devi Septiani** dan **Mamba'us Sa'adah** yang **tidak muncul** di PDDIKTI |
| K-2 | Halaman prodi menyebut Kaprodi **Ahmad Fairuzabadi**; direktori menempatkan Fairuzabadi di **Bisnis Digital** — konsisten dengan keterangan pengguna "Kaprodi Lektor tapi di homebase Prodi Lain" | `index.html` vs `direktori-dosen.html` |
| K-3 | Halaman prodi menyebut **"4 Area Fokus"** dan menyatakan eksplisit "bukan pilihan peminatan formal", sedangkan Dokumen `005` menetapkan **3 peminatan formal @18 SKS** | `index.html` vs `005` §1.4 — **harus** diselaraskan |

### 4.2 Dua daftar dosen yang tidak dapat direkonsiliasi

**Daftar A — "Tenaga Pendidik" (5 nama, semuanya ber-NIDN, semua S2, Dosen Tetap):**

| # | Nama | NIDN | NUPTK | Pend. |
|---|---|---|---|---|
| 1 | Rangga Pahlevi Putra | 0710119104 | 8442769670130393 | S2 |
| 2 | Yusriel Ardian | 0713107503 | 3345753654131093 | S2 |
| 3 | Leo Hutri Wicaksono | 0717088906 | 0149767668130483 | S2 |
| 4 | Ismail Akbar | — | 1743774675130282 | S2 |
| 5 | Affi Nizar Suksmawati | 9907160799 | 6057774675230203 | S2 |

**Daftar B — "Dosen Penghitung Rasio" (10 nama, semua S2, Dosen Tetap):** Daftar A **ditambah** Fitri Marisa (**S3**), Ahmad Fairuzabadi, Halimatus Khalidawati Salmah, Syahroni Wahyu Iriananda, Firman Nurdiyansyah, Niken Paramita, Abdul Wahid.

| Temuan | Penjelasan | Dampak |
|---|---|---|
| **C-2a** | Daftar B memuat **10 nama** padahal PDDIKTI menulis **"Jumlah Dosen Penghitung Rasio = 4"**. Kemungkinan: 10 nama adalah **seluruh dosen FSTI** (semua prodi), sedangkan "4" adalah subset yang menghitung rasio SISTEKIN | Perlu kejelasan **siapa 4 orang itu** — angka rasio 1:1,25 bertumpu pada 4 |
| **C-2b** | **Fitri Marisa** dan **Ahmad Fairuzabadi** = **Dekan** dan **Kaprodi** — keduanya berstatus Dosen Tetap di prodi lain (TI dan Bisnis Digital) | Keterlibatan mereka di SISTEKIN **wajar** sebagai *resource sharing*, **tetapi tidak boleh** dihitung sebagai DTPS homebase SISTEKIN |
| **C-2c** | Empat nama di Daftar A (**Rangga, Yusriel, Leo, Affi**) **tidak muncul** di direktori website; dua nama di direktori (**Devi Septiani, Mamba'us Sa'adah**) **tidak muncul** di PDDIKTI Gasal 2026 | Kemungkinan dosen baru/kontrak yang belum tercatat, atau dosen pindah. **Wajib** dipastikan sebelum PTS menghitung DTPS |
| **C-2d** | **Niken Paramita** (S.S., M.Pd. — linguistik) dan **Wiwin Purnomowati** (M.Si. — ekonomi) berada di daftar FSTI | Bila keduanya **dihitung** dalam DTPS SISTEKIN, **tidak ada** cabang ilmu Komputer yang sesuai → **wajib** dikeluarkan dari NDTPS |

### 4.3 Beban mengajar: kapasitas vs kebutuhan

Kebutuhan SKS prodi per semester (dihitung ulang dari `005` §3):

| Semester | MK prodi (STI/STA/STB/STC) | MK FSTI | MKWU | Total SKS |
|---|:---:|:---:|:---:|:---:|
| 1 | 8 | 5 | 6 | **19** |
| 2 | 6 | 12 | 2 | **20** |
| 3 | 20 | 0 | 0 | **20** |
| 4 | 16 | 3 | 2 | **21** |
| 5 | 18 | 0 | 3 | **21** |
| 6 | 9 | 10 | 0 | **19** |
| 7 | 20 | 0 | 0 | **20** |
| 8 | 0 | 6 | 0 | **6** |
| **Total** | **97** | **36** | **13** | **146** ✓ |

**Perhitungan kecukupan:**

| Ukuran | Nilai | Penilaian |
|---|---|---|
| Beban puncak per semester | **21 SKS** (Sem 4, 5) | — |
| Kapasitas 4 dosen × 12 SKS | 48 SKS | ✅ cukup 2,3× |
| Kapasitas 3 dosen (setelah Kaprodi & pejabat struktural dikurangi) | 36 SKS | ✅ masih cukup 1,7× |
| **MK prodi saja** (97 SKS ÷ 8 semester) | **12,1 SKS/semester** | ✅ dapat ditangani **1 dosen** secara BKD, 2 dosen secara wajar |
| **Kesimpulan** | — | **Beban mengajar BUKAN masalah.** Klaim "kekurangan dosen" tidak dapat dibenarkan dengan data SKS |

**Yang justru bermasalah: sebaran bidang.** Dari 29 MK inti STI, berikut yang **tidak** punya pengampu berbidang di antara 5 DTPS (§5.6):

| MK inti | Bidang | DTPS berbidang? |
|---|---|---|
| `STI-312` Jaringan Komputer | Jaringan | ❌ tidak ada |
| `STI-417` Komputasi Awan | Cloud/Infrastruktur | ❌ tidak ada |
| `STI-418` + `STI-519` Keamanan Informasi (2 MK) | Keamanan siber | ❌ tidak ada |
| `STI-310` Sistem Operasi | OS/Infrastruktur | ❌ tidak ada |
| `STI-103` Arsitektur & Organisasi Sistem TI | Arsitektur komputer | ❌ tidak ada |
| `STI-523` Manajemen Proyek TI | Manajemen proyek/SI | ❌ tidak ada (parsial) |
| `STI-306` Analisis & Perancangan SI | Analisis SI | ⚠️ parsial — bergantung isian SISTER "Manajemen Sistem Informasi" |
| `STI-309` Rekayasa Perangkat Lunak | RPL | ⚠️ parsial |
| **Klaster P2 (Cloud & Cybersecurity)** — 6 MK peminatan | Infrastruktur/siber | ❌ **tidak ada satu pun DTPS homebase berbidang** |

**Ini temuan paling penting dokumen ini**: klaster **P2** — yang di `PKR-2026` menyentuh **13 BK** dan menjadi klaster **volume** — **kekurangan pengampu paling parah**, padahal klaster ini justru yang paling mudah dijual dan paling dibutuhkan Malang Raya.

---

## 5. Pemetaan dosen → Rumpun / Pohon / Cabang / Ranting Ilmu

### 5.1 Daftar cabang ilmu resmi (pohon Komputer) yang relevan

Dari Daftar Rumpun, Pohon, dan Cabang Ilmu SISTER (5 Juni 2024), pohon **Komputer** pada **Rumpun Ilmu Formal** memuat antara lain:

| Cabang Ilmu (resmi) | Bahasa Inggris | Klaster SISTEKIN yang terlayani |
|---|---|---|
| Ilmu Komputer atau Informatika | Computer Science or Informatics | P1, P3 |
| Kecerdasan Buatan / Kecerdasan Buatan dan Robotik | Artificial Intelligence (and Robotics) | **P1** |
| Sistem Informasi | Information System | P2 (tata kelola), P3 |
| **Sistem dan Teknologi Informasi** | Information System and Technology | **identitas prodi** |
| Teknologi Informasi | Information Technology | P2, P3 |
| Rekayasa Perangkat Lunak | Software Engineering | P3 |
| Rekayasa Sistem Komputer | Computer System Engineering | P2 |
| Keamanan Sistem Informasi | Information Systems Security | **P2** |
| Teknik Pengamanan Siber / Rekayasa Keamanan Siber | Cyber Security Techniques / Engineering | **P2** |
| Manajemen Basis Data | Database Management | P1, P3 |
| Pengembangan Aplikasi Bergerak | Mobile-Application Development | P3 |
| Pengembangan Aplikasi Multiplatform | Multiplatform Application Development | P3 |
| Pengembangan Perangkat Lunak Situs | Web Software Developer | P3 |
| Perancangan Permainan / Teknologi Permainan | Game Design / Game Technology | P3 |
| Teknologi Komputer Grafis | Computer Graphics Technology | P3 |
| Teknologi Rekayasa Multimedia | Multimedia Engineering Technology | P3 |
| Sistem Informasi Kota Cerdas | Smart City Information Management | P1 (Smart City) |
| Administrasi Sistem Informasi Teknologi | IT System Administration | P2 |
| Dukungan Teknis Teknologi Informasi | IT Technical Support | P2 |

> Daftar ini **tidak lengkap** — file resmi memuat puluhan cabang lain (termasuk cabang non-Komputer). Yang ditampilkan hanya yang **relevan** dengan tiga klaster SISTEKIN. **Cabang yang tidak ada dalam daftar resmi tidak boleh dipakai**, sekalipun terdengar masuk akal (mis. "MLOps", "Cloud Computing", "Data Science" **tidak** berdiri sebagai cabang; keduanya masuk ke Informatika/Kecerdasan Buatan/Sistem dan Teknologi Informasi).

### 5.2 Pemetaan usulan untuk 5 dosen tetap homebase SISTEKIN

**Kolom "usulan" = [U], bukan isian SISTER.** Dasar penilaian: gelar + jejak publikasi + bidang yang dinyatakan di direktori. **Status jabfung harus dikonfirmasi** — lihat §5.3.

| # | Dosen | Gelar | Rumpun Ilmu | Pohon Ilmu | Cabang Ilmu (usulan) | Ranting Ilmu (usulan) | Klaster | Bukti/dasar |
|---|---|---|---|---|---|---|---|---|
| 1 | **Ahmad Fairuzabadi** *(Kaprodi, homebase Bisnis Digital)* | S.Kom., M.Kom. | Formal | Komputer | **Sistem dan Teknologi Informasi** | Interaksi Manusia–Komputer & desain pengalaman | P3 | Direktori: *Human Computer Interaction (HCI)* |
| 2 | **Rangga Pahlevi Putra** | S.Pd., **M.T.** | Formal | Komputer | **Ilmu Komputer atau Informatika** *(alternatif: Teknologi Komputer Grafis)* | Visi komputer, biometrik, pemrosesan citra | P1 / P3 | Direktori: *Image Processing, Biometric System*; publikasi klasifikasi logo & CNN |
| 3 | **Ismail Akbar** | S.Kom., M.Kom. | Formal | Komputer | **Kecerdasan Buatan** | Optimasi berbantuan pembelajaran, text mining | P1 | Direktori: *Learning-Augmented Optimization, Text Mining, AI* |
| 4 | **Affi Nizar Suksmawati** | S.Kom., **M.Cs.** | Formal | Komputer | **Kecerdasan Buatan** | Sistem pakar, logika fuzzy, *machine learning* | P1 | Direktori: *Machine Learning, Expert System, Fuzzy Logic*; gelar M.Cs. (Magister Computer Science) |
| 5 | **Yusriel Ardian** | — , S2 | Formal **?** | Komputer **?** | **tidak dapat ditetapkan** | — | — | Tidak ada di direktori website; gelar S2 tidak tercantum. **Butuh konfirmasi (U-03)** |
| 6 | **Leo Hutri Wicaksono** | S.T., M.Eng. | **Terapan ? / Formal ?** | **Teknik ?** | **tidak dapat ditetapkan** | — | P2 (potensi) | Publikasi teridentifikasi bertopik **efisiensi energi listrik** & **komposit serat** — bukan Komputer. **Butuh konfirmasi (U-04)** |

**Catatan penting atas kolom "Cabang Ilmu":**

- **Cabang Ilmu bersifat opsional** di SISTER. Untuk dosen yang kepakarannya tidak pas pada satu cabang, **mengosongkan cabang lebih aman** daripada memilih yang salah. Yang **wajib** dan tidak boleh salah adalah **Rumpun + Pohon**.
- **Pemetaan ini tidak boleh disalin mentah** ke SISTER. Dosen sendiri yang mengisi, Admin PT yang memvalidasi, dan dasar formalnya **ijazah** — bukan direktori website.
- Untuk **Rangga** (S.Pd. → M.T.), pilihan cabang **"Ilmu Komputer atau Informatika"** lebih aman daripada cabang sempit, karena jenjang S1-nya kependidikan.

### 5.3 Konflik jabatan fungsional — butir paling rawan

Data pengguna: **2 Lektor**, **2 proyeksi AA**, **calon Doktor 2 orang**, **Kaprodi Lektor**.

| # | Dosen | Jabfung | Dasar | Risiko |
|---|---|---|---|---|
| 1 | Ahmad Fairuzabadi | **Lektor** *(sesuai keterangan pengguna)* | homebase **Bisnis Digital** | Bila dihitung DTPS SISTEKIN, ia menyumbang 1 Lektor — tetapi **jabfung-nya milik prodi lain** |
| 2 | *?* | **Lektor** | belum teridentifikasi | — |
| 3 | *?* | **Asisten Ahli** | belum teridentifikasi | — |
| 4 | *?* | **Asisten Ahli** | belum teridentifikasi | — |
| 5 | *?* | **Asisten Ahli**? | belum teridentifikasi | — |

**Perhitungan skor LAM INFOKOM atas kemungkinan terbaik** (asumsi: Fairuzabadi tidak dihitung sebagai DTPS SISTEKIN; 5 DTPS homebase dengan 1 Lektor + 4 AA):

| Skenario | NDTPS | L+LK+GB | PGBLKL | Skor jabfung | PDS3 | Skor S3 |
|---|---:|---:|---:|---:|---:|---:|
| **A. Hari ini** (5 homebase; 2 Lektor termasuk Kaprodi prodi lain) | 5 | 2 | **40%** | **3,14** | **0%** | **2,0** |
| **B. 2027, tanpa perubahan** (5 homebase; 1 Lektor, 2 AA naik, 2 calon doktor belum lulus) | 5 | 2 | 40% | 3,14 | 0% | 2,0 |
| **C. 2027, 2 calon doktor lulus** (S3 = 2/5) | 5 | 3 (2 L + 1 LK?) | 60% | **4,0** ✅ | **40%** | **3,6** |
| **D. 2027, +1 dosen S3 baru** (NDTPS 6, S3 = 3/6) | 6 | 3 | 50% | 4,0 ✅ | **50%** ✅ | **4,0** ✅ |

**Bacaan kritis:**

1. **Ambang "≥70% Lektor+" tidak akan tercapai dalam waktu dekat** dan **tidak perlu** dikejar secara artifisial. Dengan 5–6 DTPS, dibutuhkan **4–5 orang Lektor**. Skenario C sudah memberi **4,0** — artinya cukup **dua kenaikan jabatan** untuk keluar dari zona skor rendah. Prioritasnya bukan menambah dosen, melainkan **mempercepat AA → Lektor yang sudah ada**.
2. **PDS3 adalah titik terlemah kedua.** 0% hari ini; 40% bila dua calon doktor lulus (masih < 50%). Skenario D adalah satu-satunya jalan ke skor 4 — **dan itulah dasar rekomendasi rekrutmen di §7**.
3. **Risiko administrasi yang lebih halus:** bila Kaprodi dihitung sebagai DTPS SISTEKIN, jumlah Lektor menjadi 2/5 = 40% **tetapi** basis NDTPS bisa berubah menjadi 6 (bila dosen luar ikut dihitung), sehingga PGBLKL turun ke **33%**. **Setiap penambahan nama ke DTPS memperburuk PGBLKL** bila yang ditambah bukan Lektor. Ini perangkap nyata pada prodi kecil.
4. **Dua "calon Doktor" belum tentu berdampak pada PDS3.** PDS3 menghitung dosen yang **sudah** bergelar Doktor. Selama statusnya "sedang menempuh", kontribusinya **nol** — kecuali bila PTS memakai ketentuan khusus tugas belajar (laporan kemajuan setara 12 SKS untuk BKD, **bukan** untuk PDS3).

---

## 6. Analisis kritis: jurang antara kapasitas dan kompetensi

### 6.1 Peta cakupan bidang (5 DTPS homebase)

| Rumpun bidang | MK inti STI | Jumlah MK | DTPS berbidang | Status |
|---|---|:---:|---|---|
| Kecerdasan Buatan / ML | STI-307, 413, 414, 520, 624, 726 | 6 | Akbar, Affi (**2**) | ✅ **kuat** |
| Visi komputer / citra | (menopang STI-413, 520, 624) | — | Rangga (**1**) | ✅ cukup |
| Web / mobile / platform | STI-311, 416, 522, 625 | 4 | Ismail (parsial, *web & mobile programming*) | ⚠️ **tipis** |
| UI/UX & HCI | STI-308 | 1 | Fairuzabadi (homebase lain) | ⚠️ **bergantung prodi lain** |
| Sistem informasi & analisis | STI-101, 306, 415 | 3 | Devi* (di luar PDDIKTI) | ⚠️ **tidak pasti** |
| Manajemen proyek TI | STI-523 | 1 | — | ❌ **kosong** |
| **Jaringan, cloud, OS, arsitektur** | **STI-103, 310, 312, 417** | **4** | **—** | ❌ **kosong** |
| **Keamanan informasi** | **STI-418, 519** | **2** | **—** | ❌ **kosong** |
| Multimedia / AR-VR / game | STI-308 (parsial), STC-701 | 1–2 | Devi*, Mamba'us* (di luar PDDIKTI) | ⚠️ **tidak pasti** |
| Matematika & statistika | STI-102, 204, 205, FST-408 | 4 | — | ❌ **kosong** |
| Rekayasa perangkat lunak | STI-309 | 1 | — | ❌ **kosong** |
| Etika, metodologi, capstone | FST-206, 611, 613, 610 | 4 | — | ⚠️ tersebar |

\* tidak muncul di PDDIKTI Gasal 2026.

**Tiga MK wajib yang paling berisiko** karena merupakan **prasyarat** bagi MK lain namun tidak punya pengampu berbidang:

| MK | Prasyarat untuk | Risiko bila diajar tanpa kepakaran |
|---|---|---|
| `STI-312` Jaringan Komputer | STI-417 Cloud, STI-521 IoT, STB-501 | P2 kehilangan fondasi |
| `STI-417` Komputasi Awan | STB-601 Cloud & DevOps | Klaster P2 tumbang |
| `STI-418`+`STI-519` Keamanan | STB-501, STB-602, STB-701 | Klaster P2 tumbang |

### 6.2 Ketidaksesuaian klaster ↔ kapasitas dosen

| Klaster | BK tersentuh (PKR-2026) | DTPS homebase berbidang klaster | Rasio | Penilaian |
|---|---:|---|---:|---|
| **P1 Integrated Smart Systems** | 7 | Akbar, Affi, Rangga (**3**) | 3/6 MK | ✅ **kuat** — klaster paling siap |
| **P2 Cloud & Cybersecurity** | 13 | **0** (hanya Fairuzabadi untuk P3/HCI) | **0/6 MK** | ❌ **kritis** |
| **P3 Digital Platform Engineering** | 13 | Fairuzabadi (1, homebase lain); Rangga (parsial) | 0–1/6 MK | ⚠️ **lemah** |

**Analisis kritis.** Kurikulum sudah dirancang dengan **tiga klaster seimbang 18 SKS**, tetapi **kapasitas dosen sangat tidak seimbang**: P1 punya 3 dosen, P2 **nol**. Akibatnya:

- Bila 7 mahasiswa angkatan 2026 memilih P2 — dan P2 adalah klaster dengan **pasar terbesar** (cloud & cybersecurity adalah dua dari tiga kekurangan talenta digital terbesar) — prodi **tidak punya dosen tetap berbidang** untuk mengajarkannya. Pengajaran akan bergantung pada dosen TI (Aviv, Syahroni, Istiadi) atau praktisi.
- Ini **bukan** pelanggaran aturan (dosen lintas prodi sah), tetapi **melemahkan** bukti "DTPS sesuai kompetensi inti" untuk **separuh** kurikulum peminatan.
- Sebaliknya, **P1 diisi 3 dosen untuk 6 MK** — *over-supply* relatif. Bobot riset prodi (AI/ML/text mining) memang kuat, tetapi **tidak boleh** menjadi satu-satunya wajah prodi.

### 6.3 Kebutuhan dosen 2026–2027: bukan "berapa", tetapi "siapa"

**Kebutuhan mengajar (SKS) per 2027** dengan 10–15 mahasiswa:

| Skenario mahasiswa | Rombel per MK | Beban mengajar | Kesimpulan |
|---|---|---|---|
| **7** (2026) | 1 rombel | 21 SKS/semester (puncak) | 2 dosen cukup |
| **10–15** (2027) | 1 rombel (belum perlu paralel) | 21 SKS/semester | 2 dosen cukup |
| **> 40** | 2 rombel pada MK inti | ~32 SKS/semester | 3 dosen |

→ **Tidak ada kebutuhan menambah dosen karena alasan beban mengajar sampai mahasiswa mendekati 40 orang.**

**Kebutuhan karena alasan kompetensi dan akreditasi** — inilah yang riil:

| # | Kebutuhan | Jenis | Prioritas | Dasar |
|---|---|---|---|---|
| **N-1** | **1 dosen DTPS bergelar Doktor** bidang **jaringan / infrastruktur / keamanan siber** (rumpun Formal → Komputer) | **Rekrutmen** | **TINGGI — 2027** | Menutup PDS3 → 50%; mengisi 4 MK inti kosong; memberi P2 pengampu |
| **N-2** | **1 dosen (boleh DTT/praktisi)** bidang **DevOps / cloud / SRE** untuk STB-601, STA-701 | **Praktisi / DTT** | **TINGGI — 2027** | Menutup G-06 (5 MK teori murni) & P2 |
| **N-3** | Percepatan **AA → Lektor** untuk 2 dosen | **Pengembangan** | **TINGGI — 2026/2027** | PGBLKL 40% → 60–80%; skor jabfung 3,14 → 4,0 |
| **N-4** | Penyelesaian **S3** dua calon doktor | **Pengembangan** | **TINGGI — 2027/2028** | PDS3 0% → 40% |
| **N-5** | Konfirmasi & penetapan **cabang ilmu SISTER** untuk Yusriel, Leo, Devi, Mamba'us | **Administrasi** | **TINGGI — segera** | Mencegah DTPS ineligible (§8) |
| **N-6** | **1 dosen** bidang **tata kelola SI / audit TI** untuk P2 (STB-701–703) | **Rekrutmen/praktisi** | **SEDANG — 2028** | 3 MK P2 bertumpu COBIT/ITIL/TOGAF tanpa pengampu |
| **N-7** | **1 dosen** bidang **RPL / rekayasa platform** untuk STI-309, STI-625, STC-602/702 | **Rekrutmen** | **SEDANG — 2028** | MK wajib tanpa pengampu |
| **N-8** | **1 dosen** bidang **matematika/statistika terapan** | **Rekrutmen/DTT** | **RENDAH** | STI-102/204/205, FST-408 dapat *resource sharing* FMIPA |

**Angka minimum yang dapat dipertahankan sampai 2028: 5 DTPS homebase.** Rekomendasi **+1 DTPS S3 (N-1)** pada 2027 → **6 DTPS**. Penambahan ke-7 dan seterusnya baru diperlukan bila mahasiswa **> 40** atau bila P2 dibuka sebagai klaster unggulan penuh.

---

## 7. Rencana pemenuhan 2026–2027

### 7.1 Peta jalan tiga horizon

| Horizon | Fokus | Aksi konkret | Ukuran keberhasilan |
|---|---|---|---|
| **Q4 2026 (segera)** | **Legalitas & data** | (a) Kunci isian **Rumpun–Pohon–Cabang** 6 dosen di SISTER dan validasi Admin PT; (b) rekonsiliasi Daftar A vs B PDDIKTI; (c) tetapkan **siapa 4 dosen penghitung rasio**; (d) selaraskan 3 vs 4 area fokus (K-3) | Semua DTPS punya rumpun **Formal → Komputer** tervalidasi; satu daftar dosen tunggal |
| **Semester Gasal 2026/2027** | **Jabfung & penugasan** | (a) Ajukan **AA → Lektor** untuk 2 dosen yang memenuhi syarat; (b) tetapkan **penugasan mengajar** agar MK berisiko (STI-312/417/418/519) diampu dosen dengan latar terdekat **atau** *team teaching* dengan TI; (c) bentuk **tim pengampu klaster** P1/P2/P3 | 2 pengajuan Lektor berjalan; tidak ada MK tanpa penanggung jawab bidang |
| **2027** | **Rekrutmen & kemitraan** | (a) **Rekrut 1 DTPS S3** (jaringan/siber); (b) kontrak **1 praktisi** cloud/DevOps; (c) ajukan **Praktisi Mengajar** untuk STB-601/STA-701; (d) dorong 2 calon doktor menyelesaikan studi | NDTPS 6; PDS3 ≥ 50%; P2 punya pengampu |

### 7.2 Profil rekrutmen N-1 (spesifikasi yang dapat langsung dipakai)

| Atribut | Syarat | Alasan |
|---|---|---|
| **Gelar** | **S3 (Doktor)** bidang Ilmu Komputer/Informatika/Sistem dan Teknologi Informasi | Menutup PDS3 |
| **Rumpun SISTER** | Formal → Komputer (cabang: Teknologi Informasi / Keamanan Sistem Informasi / Sistem dan Teknologi Informasi) | Wajib agar dihitung DTPS |
| **Bidang** | Jaringan komputer, komputasi awan, atau keamanan siber | Menutup 4 MK kosong + klaster P2 |
| **Jabfung** | Diutamakan **Lektor** | Menutup PGBLKL |
| **Beban** | Siap **12–16 SKS**; bersedia mengampu STI-312, STI-417, STI-418/519, STB-501, STB-601 | Penugasan langsung |
| **EWMP** | Penuh waktu, bukan *resource sharing* | Menambah NDTPS, bukan memindah |

**Peringatan penting:** merekrut doktor bidang **AI/ML** akan memperkuat P1 yang **sudah kuat** dan **tidak** menyelesaikan klaster P2. Ini kesalahan prioritisasi yang paling mungkin terjadi karena P1 adalah bidang riset yang sudah mapan di prodi.

### 7.3 Yang **tidak** perlu dilakukan

| Usulan yang sering muncul | Mengapa tidak perlu (2026–2027) |
|---|---|
| Menambah dosen agar rasio "ideal" 1:25 | Rasio sekarang 1:1,4–1:1,75; masalahnya **kelebihan** dosen relatif, bukan kekurangan |
| Mengejar NDTPS ≥ 12 | Untuk 10–15 mahasiswa, ini **memperburuk** rasio dan efisiensi; pita 5–12 sah |
| Merekrut dosen AA bidang AI | Memperkuat klaster yang sudah 3 dosen; **tidak** menutup celah mana pun |
| Menambah peminatan ke-4 | Kapasitas dosen belum menutup 3 peminatan yang ada |
| Menghitung dosen prodi lain sebagai DTPS homebase | Menurunkan PGBLKL bila bukan Lektor, dan berisiko **temuan** saat asesmen lapangan |

---

## 8. Risiko dan temuan yang harus ditutup

| # | Risiko | Kemungkinan | Dampak | Mitigasi |
|---|---|---|---|---|
| **R-01** | Dosen SISTEKIN mengisi Rumpun Ilmu **bukan** Formal/Komputer (mis. mengikuti homebase) | Sedang | DTPS tidak dihitung; butir Kriteria 4 jatuh | Sosialisasi aturan "ijazah, bukan homebase"; validasi Admin PT |
| **R-02** | **Leo Hutri Wicaksono** (M.Eng., publikasi energi/komposit) tercatat di luar Komputer | **Tinggi** | 1 dari 5 DTPS hilang → NDTPS 4 → **skor 0** (< 5) | Konfirmasi ijazah; bila di luar Komputer, **wajib** tambah DTPS |
| **R-03** | Devi Septiani & Mamba'us Sa'adah mengajar tetapi tidak tercatat di PDDIKTI | Sedang | DTPS tidak sah; BKD bermasalah | Pemutakhiran PDDIKTI sebelum Gasal 2026/2027 |
| **R-04** | Kaprodi (homebase Bisnis Digital) dihitung DTPS SISTEKIN | Sedang | PGBLKL & NDTPS berubah tidak konsisten antar dokumen | Tetapkan satu kebijakan tertulis; sebut status *resource sharing* secara eksplisit |
| **R-05** | Klaster P2 dibuka tanpa pengampu berbidang | **Tinggi** | Mutu pembelajaran & bukti DTPS lemah | Rekrut N-1 **sebelum** P2 dipromosikan |
| **R-06** | Dua calon doktor tidak lulus pada 2027 | Sedang | PDS3 tetap 0–40% | Target studi tertulis; dukungan disertasi |
| **R-07** | Prodi memakai istilah "konsentrasi" padahal kurikulum belum punya jalur formal | Sedang | Temuan ketidaksesuaian dokumen | Selaraskan `005` (3 peminatan) vs website (4 area fokus) — K-3 |
| **R-08** | Rekrutmen diarahkan ke AI karena riset prodi kuat | **Tinggi** | P1 over-supply, P2 tetap kosong | Pakai spesifikasi §7.2 sebagai dokumen pengadaan |

### 8.1 Butir keputusan terbuka [U]

| Kode | Butir | Pemilik |
|---|---|---|
| **U-01** | Konfirmasi pembacaan **kode prodi 59201** terhadap tabel kodefikasi (digit rumpun) | PDDIKTI/LLDIKTI |
| **U-02** | Tetapkan **siapa 4 dosen penghitung rasio** dan **siapa 5 DTPS homebase** | Kepegawaian + Kaprodi |
| **U-03** | Konfirmasi **ijazah S2 Yusriel Ardian** (bidang & institusi) | Kepegawaian |
| **U-04** | Konfirmasi **ijazah S2 Leo Hutri Wicaksono** — apakah Komputer atau Teknik | Kepegawaian |
| **U-05** | Tetapkan status **Devi Septiani** & **Mamba'us Sa'adah** (dosen tetap/kontrak; homebase) | Kepegawaian |
| **U-06** | Konfirmasi **siapa 2 Lektor** dan **siapa 2 proyeksi AA** | Kepegawaian |
| **U-07** | Kebijakan tertulis: apakah **Kaprodi** dihitung sebagai DTPS SISTEKIN untuk LKPS | Kaprodi + Penjaminan Mutu |
| **U-08** | Selaraskan **3 peminatan** (`005`) dengan **4 area fokus** (website) | Kaprodi |
| **U-09** | Keputusan **rekrutmen N-1** (doktor jaringan/siber) untuk 2027 | Dekan + Yayasan |
| **U-10** | Keputusan **kontrak praktisi** cloud/DevOps (N-2) | Dekan |

---

## 9. Kesimpulan

1. **SISTEKIN tidak kekurangan dosen.** Lima DTPS homebase untuk 7–15 mahasiswa adalah **kelebihan kapasitas** dalam arti beban mengajar (kebutuhan riil hanya ~12 SKS prodi per semester).
2. **SISTEKIN kekurangan dosen berbidang infrastruktur, jaringan, dan keamanan siber.** Empat MK inti wajib dan seluruh klaster P2 (13 BK) tidak memiliki pengampu tetap berbidang. Ini **satu-satunya** alasan kompetensi yang benar-benar mendesak.
3. **Risiko terbesar bersifat administratif, bukan akademik.** Karena SISTER memilih rumpun berdasarkan **ijazah**, dua dosen berpotensi tercatat di luar Komputer — cukup untuk menjatuhkan NDTPS ke 4 dan skor DTPS ke **0**. Ini dapat dicegah dalam hitungan minggu dan **harus** menjadi prioritas sebelum rekrutmen apa pun.
4. **Prioritas investasi 2027, berurutan:** (1) validasi rumpun SISTER + rekonsiliasi data dosen; (2) percepatan **2 AA → Lektor**; (3) **rekrutmen 1 DTPS S3** jaringan/siber; (4) **kontrak 1 praktisi** cloud/DevOps; (5) penyelesaian S3 dua calon doktor.
5. **Jangan menambah peminatan, jangan mengejar NDTPS 12, jangan merekrut AI.** Ketiganya terlihat "membangun" tetapi tidak menutup satu pun celah nyata pada skala 10–15 mahasiswa.

---

## 10. Rujukan

1. **[R]** Undang-Undang No. 12 Tahun 2012 tentang Pendidikan Tinggi, Pasal 10 (rumpun ilmu).
2. **[R]** Permendikbud No. 124 Tahun 2014 tentang Rumpun, Pohon, dan Cabang Ilmu Pengetahuan dan Teknologi untuk Pembentukan Lembaga Akreditasi Mandiri — Pasal 1 angka 2; Pasal 2 ayat (1); Pasal 5 ayat (5)–(7).
3. **[R]** Permendikbud No. 154 Tahun 2014 tentang Rumpun Ilmu Pengetahuan dan Teknologi serta Gelar Lulusan Perguruan Tinggi.
4. **[R]** Keputusan Dirjen Dikti, Riset, dan Teknologi No. **163/E/KPT/2022** tentang Nama Program Studi pada Jenis Pendidikan Akademik dan Pendidikan Profesi — Lampiran I no. 201 *Sistem dan Teknologi Informasi*; Ketiga (inisial rumpun **Kom**).
5. **[R]** SISTER Kemdiktisaintek — *Informasi Umum Rumpun Ilmu*; *Tahapan Pengisian Rumpun Ilmu oleh Dosen*; *Tahapan Validasi Rumpun Ilmu oleh Admin PT*; *Daftar Rumpun, Pohon, dan Cabang Ilmu* (diperbarui 5 Juni 2024).
6. **[R]** Undang-Undang No. 14 Tahun 2005 tentang Guru dan Dosen, Pasal 72; PP No. 37 Tahun 2009 Pasal 8; Permendikbud No. 3 Tahun 2020 Pasal 30 (BKD, EWMP, pembimbing utama).
7. **[R]** LAM INFOKOM — Instrumen Akreditasi Program Studi Sarjana (APS/LKPS 2.1) dan matriks penilaian: butir kecukupan DTPS, kualifikasi akademik DTPS, jabatan akademik DTPS, rasio mahasiswa–DTPS.
8. **[P]** PDDIKTI — Detail Program Studi 59201 *Sistem dan Teknologi Informasi*, FSTI Universitas Widya Gama, Semester Gasal 2026 (tangkapan layar pengguna).
9. **[P]** `https://sistekin.widyagama.ac.id/index.html` — halaman prodi (SK 747/B/O/2025; visi-misi; 146 SKS; 4 area fokus; 5 dosen homebase).
10. **[P]** `https://sistekin.widyagama.ac.id/direktori-dosen.html` — direktori 14 dosen FSTI beserta bidang kepakaran naratif.
11. **[S]** Dokumen `005`, `013`, `025`, dan `PKR-2026` di repositori ini — struktur kurikulum, mitigasi, rekomendasi 2027, dan pemetaan klaster.
