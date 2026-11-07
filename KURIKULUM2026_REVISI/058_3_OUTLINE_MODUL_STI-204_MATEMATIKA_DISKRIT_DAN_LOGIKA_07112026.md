# OUTLINE BUKU MODUL PEMBELAJARAN
## STI-204 — MATEMATIKA DISKRIT DAN LOGIKA

> **Jenis dokumen:** Kerangka (*outline*) buku modul ajar yang diturunkan dari RPS
> **Dokumen induk:** `058_1_RPS_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md`
> **Rujukan kurikulum:** Dokumen 005, 007, 043 (Sub-CPMK & Boundary Guardrails), 003 (CPL)
> **Tanggal:** 07 November 2026

---

## 1. METADATA MODUL

| Atribut | Keterangan |
|---|---|
| Judul modul | *Matematika Diskrit dan Logika: dari Pembuktian Formal hingga Otomata Berhingga* |
| Kode MK | `STI-204` |
| Penulis | Tim Pengampu Rumpun Matematika & Sains Komputasi (Core STI) |
| Penelaah | Koordinator RMK Matematika & Sains Komputasi; Unit Penjaminan Mutu FSTI |
| Jenjang / Semester | S1 / Semester 2 |
| Bobot | 3 SKS Teori (TM 150′ + PT 180′ + BM 180′ per pekan) |
| Prasyarat | `STI-103` Arsitektur dan Organisasi Sistem Teknologi Informasi |
| Target pembaca | Mahasiswa S1 SISTEKIN tahun pertama; dosen pengampu; asisten tutorial |
| Estimasi tebal | 250–290 halaman A5 (atau 195–225 halaman A4) |
| Bahasa | Indonesia, dengan istilah teknis Inggris dalam tanda kurung miring |
| Bentuk | Buku modul cetak + e-modul (PDF interaktif dengan tautan simulator JFLAP dan visualisasi graf) |
| Status ISBN | Dalam pengajuan Perpustakaan Nasional RI |
| Edisi | Edisi 1 (2027) |

---

## 2. DASAR DAN BATAS PENYUSUNAN

| Aspek | Ketentuan |
|---|---|
| Sumber capaian | CPMK-1 s.d. CPMK-4 dan Sub-CPMK-1.1 s.d. 4.2 dari Dokumen 043 |
| Sumber materi | Pokok bahasan Tabel 9.C Dokumen 007 dan BoK `BK-IS10`, `BK-IS11` |
| Batas isi (*in-scope*) | Logika proposisi, logika predikat, aljabar Boolean formal, teori himpunan, relasi dan fungsi diskrit, kombinatorika, teori graf, pohon (*tree*) |
| Batas larangan (*out-of-scope*) | Perancangan gerbang fisik mikroprosesor (*hardware wiring*) → `STI-103`; pengodean struktur data dinamis dengan manajemen memori → `FST-203`/`STI-308`; analisis diferensial–integral → `STI-102` |
| Titik serah terima | Struktur memori fisik & implementasi graf → `FST-203` / `STI-308`; rangkaian gerbang logika fisik → `STI-103`; kalkulus → `STI-102` |

---

## 3. CAPAIAN MODUL

Setelah menuntaskan modul ini, mahasiswa mampu:

1. **Membuktikan** validitas argumen inferensi logika proposisi/predikat dan kebenaran algoritma menggunakan tabel kebenaran, hukum aljabar logika, dan metode induksi matematika secara runtut dan valid (CPMK-1, C3).
2. **Menerapkan** konsep relasi ekuivalensi, himpunan terurut parsial (Poset), aljabar Boolean, dan kombinatorika pada pemodelan struktur data dan logika *query* basis data secara tepat (CPMK-2, C3).
3. **Menganalisis** struktur graf dan pohon menggunakan matriks representasi (*adjacency matrix*) dan algoritma penelusuran lintasan untuk optimasi jaringan data/komputer (CPMK-3, C4).
4. **Mengonstruksi** model otomata berhingga (DFA dan NFA) untuk pengenalan pola bahasa formal dan transisi status sistem komputasi secara akurat (CPMK-4, C4).

---

## 4. PETA BAB ↔ SUB-CPMK ↔ PEKAN ↔ ASESMEN

| Bab | Judul Bab | Sub-CPMK | Pekan | CPMK | Asesmen Terkait |
|:--:|---|---|:--:|:--:|---|
| 1 | Logika Proposisi dan Bahasa Pembuktian | 1.1 | 2 | CPMK-1 | **Tugas 1**, UTS |
| 2 | Logika Predikat, Inferensi, dan Induksi Matematika | 1.2 | 3 | CPMK-1 | Tugas 1, UTS |
| 3 | Himpunan, Relasi, dan Himpunan Terurut Parsial | 2.1 | 4 | CPMK-2 | **Tugas 1**, UTS |
| 4 | Aljabar Boolean, Kombinatorika, dan Relasi Rekurensi | 2.2 | 5 | CPMK-2 | UTS, UAS |
| 5 | Teori Graf dan Representasinya | 3.1 | 6 | CPMK-3 | UTS, Tugas 2 |
| 6 | Pohon, Pohon Merentang Minimum, dan Lintasan Terpendek | 3.2 | 7 | CPMK-3 | UTS, Tugas 2, UAS |
| 7 | Otomata Berhingga Deterministik (DFA) | 4.1 | 9 | CPMK-4 | Tugas 2, UAS |
| 8 | Otomata Berhingga Non-deterministik (NFA) dan Konversinya | 4.2 | 10 | CPMK-4 | **Tugas 2**, UAS |
| 9 | Pemodelan Diskrit Terpadu untuk Sistem Nyata | 4.3, 4.4 | 11–12 | CPMK-3, CPMK-4 | **Tugas 2**, UAS |
| Lampiran A | Glosarium, Tabel Hukum Logika, dan Rumus Kombinatorika | — | — | — | — |
| Lampiran B | Kumpulan Soal Pembuktian Terpandu dan Kunci | — | — | — | — |

**Total bab inti:** 9 bab. Setiap bab setara 1–2 pekan pertemuan (16 pekan termasuk UTS & UAS).

---

## 5. STRUKTUR BAKU SETIAP BAB

Setiap bab wajib memuat tujuh komponen berikut, dengan urutan tetap:

| No | Komponen | Isi Wajib | Estimasi |
|:--:|---|---|:--:|
| 1 | **Peta Kompetensi** | Sub-CPMK yang dibina, CPMK induk, indikator kinerja | 0,5 hlm |
| 2 | **Uraian Materi** | 3–6 sub-bab, masing-masing dengan definisi formal, contoh, dan **jebakan pembuktian** | 12–20 hlm |
| 3 | **Sorotan Kasus (Case Spotlight)** | Satu penerapan komputasi nyata + pertanyaan analitis | 1,5 hlm |
| 4 | **Rangkuman** | 5–8 butir kunci dalam bentuk poin bernomor | 0,5 hlm |
| 5 | **Latihan Terbimbing** | 8–12 soal bertingkat (C2–C4) dengan petunjuk pengerjaan | 1,5 hlm |
| 6 | **Tes Formatif Mandiri** | 10 soal pilihan ganda + 3 esai pendek, kunci di lampiran daring | 2 hlm |
| 7 | **Rujukan Bab** | 3–6 sitasi IEEE, sinkron dengan daftar pustaka RPS | 0,3 hlm |

**Kekhususan modul ini:** setiap bab yang memuat pembuktian wajib menyertakan kotak **"Struktur Pembuktian Baku"** (asumsi → yang akan dibuktikan → langkah → kesimpulan) agar mahasiswa tidak menulis pembuktian tanpa kerangka.

---

## 6. OUTLINE RINCI PER BAB

### BAB 1 — Logika Proposisi dan Bahasa Pembuktian
**Sub-CPMK:** 1.1 | **Pekan:** 2 | **Estimasi:** 26 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 1.1 | Proposisi, nilai kebenaran, dan variabel proposisional |
| 1.2 | Konektif logika: negasi, konjungsi, disjungsi, XOR, implikasi, bikondisional |
| 1.3 | Konstruksi tabel kebenaran dan prioritas operator |
| 1.4 | Tautologi, kontradiksi, dan kontingensi |
| 1.5 | Hukum-hukum aljabar logika (identitas, dominasi, idempoten, negasi ganda, komutatif, asosiatif, distributif, De Morgan, absorpsi) |
| 1.6 | Ekuivalensi logis dan pembuktian deret ekuivalensi tanpa tabel kebenaran |
| 1.7 | Bentuk normal disjungtif/konjungtif dan keterkaitannya dengan rangkaian logika (level konseptual) |
| 1.8 | Kesalahan umum: menyamakan implikasi dengan konvers, salah menerapkan De Morgan |

**Kegiatan belajar:** latihan tabel kebenaran (PT 120′), pembuktian ekuivalensi (PT 90′), diskusi keterkaitan dengan rangkaian (TM 35′).
**Tes formatif:** 6 tabel kebenaran + 4 pembuktian ekuivalensi dengan hukum logika.

---

### BAB 2 — Logika Predikat, Inferensi, dan Induksi Matematika
**Sub-CPMK:** 1.2 | **Pekan:** 3 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 2.1 | Predikat, domain, dan fungsi proposisional |
| 2.2 | Kuantor universal dan eksistensial; kuantor bersarang |
| 2.3 | Negasi pernyataan berkuantor dan translasi bahasa alami |
| 2.4 | Aturan inferensi: modus ponens, modus tollens, silogisme hipotetis, silogisme disjungtif, konjungsi, adisi, resolusi |
| 2.5 | Kesalahan penalaran (*fallacy*): *affirming the consequent*, *denying the antecedent* |
| 2.6 | Induksi matematika biasa: basis, hipotesis, langkah |
| 2.7 | Induksi kuat dan penerapannya pada relasi rekurensi |
| 2.8 | Verifikasi kebenaran algoritma: invarian *loop* dan terminasi |
| 2.9 | Kesalahan umum: melompat dari $n=k$ ke $n=k+2$, menggunakan kesimpulan sebagai premis |

**Kegiatan belajar:** latihan translasi & inferensi (PT 120′), pembuktian induksi bertingkat (PT 120′), diskusi invarian *loop* (TM 30′).
**Tes formatif:** 4 translasi berkuantor + 3 pembuktian induksi lengkap.

---

### BAB 3 — Himpunan, Relasi, dan Himpunan Terurut Parsial
**Sub-CPMK:** 2.1 | **Pekan:** 4 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 3.1 | Himpunan, notasi pembentuk himpunan, himpunan semesta, himpunan kuasa |
| 3.2 | Operasi himpunan: gabungan, irisan, komplemen, selisih, beda simetris |
| 3.3 | Hukum aljabar himpunan dan pembuktian identitas himpunan |
| 3.4 | Produk kartesius dan relasi biner |
| 3.5 | Sifat relasi: refleksif, irefleksif, simetris, antisimetris, transitif |
| 3.6 | Relasi ekuivalensi, kelas ekuivalensi, dan partisi |
| 3.7 | Relasi terurut parsial (Poset) dan diagram Hasse |
| 3.8 | Elemen maksimal, minimal, terbesar, terkecil, batas atas/bawah, *lattice* |
| 3.9 | Penerapan: pemodelan keterkaitan tabel basis data dan dependensi fungsional |

**Kegiatan belajar:** latihan uji sifat relasi (PT 150′), penyusunan diagram Hasse (PT 90′), persiapan Tugas 1 (TM 35′).
**Tes formatif:** 3 relasi diuji lengkap + 2 diagram Hasse.

---

### BAB 4 — Aljabar Boolean, Kombinatorika, dan Relasi Rekurensi
**Sub-CPMK:** 2.2 | **Pekan:** 5 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 4.1 | Fungsi Boolean dan representasinya dalam tabel kebenaran |
| 4.2 | Bentuk normal disjungtif (SOP) dan konjungtif (POS) |
| 4.3 | Penyederhanaan fungsi Boolean secara aljabar |
| 4.4 | Kaidah penjumlahan dan perkalian dalam pencacahan |
| 4.5 | Permutasi dan kombinasi dengan/tanpa pengulangan |
| 4.6 | Prinsip pigeonhole dan penerapannya pada analisis tabrakan *hash* |
| 4.7 | Prinsip inklusi–eksklusi |
| 4.8 | Relasi rekurensi linier homogen dan metode akar karakteristik |
| 4.9 | Penerapan: analisis jumlah kemungkinan *password*/token dan kompleksitas pencarian |

**Kegiatan belajar:** latihan pencacahan bertingkat (PT 150′), penyelesaian rekurensi (PT 90′), diskusi penerapan *hash* (TM 30′).
**Tes formatif:** 6 soal kombinatorika + 2 penyelesaian rekurensi.

---

### BAB 5 — Teori Graf dan Representasinya
**Sub-CPMK:** 3.1 | **Pekan:** 6 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 5.1 | Definisi graf, simpul, sisi, *loop*, sisi ganda; graf sederhana, multigraf, pseudograf |
| 5.2 | Derajat simpul dan *handshaking lemma* |
| 5.3 | Lintasan, siklus, keterhubungan, dan komponen terhubung |
| 5.4 | Isomorfisme graf dan uji isomorfisme sederhana |
| 5.5 | Graf bipartit dan uji bipartit dengan pewarnaan dua warna |
| 5.6 | Representasi: *adjacency matrix*, *adjacency list*, *incidence matrix* |
| 5.7 | Penelusuran Breadth-First Search (BFS) dan Depth-First Search (DFS) |
| 5.8 | Kompleksitas dan pemilihan representasi berdasarkan kepadatan graf |
| 5.9 | Kesalahan umum: menganggap graf berarah sama dengan tak berarah pada matriks ketetanggaan |

**Kegiatan belajar:** penelusuran manual BFS/DFS (PT 150′), latihan representasi matrix–list (PT 90′), visualisasi graf (TM 35′).
**Tes formatif:** 3 penelusuran BFS/DFS + 2 konversi representasi.

---

### BAB 6 — Pohon, Pohon Merentang Minimum, dan Lintasan Terpendek
**Sub-CPMK:** 3.2 | **Pekan:** 7 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 6.1 | Definisi pohon dan sifat ekuivalennya (terhubung, asiklik, $n-1$ sisi) |
| 6.2 | Pohon berakar, pohon-$m$, pohon biner, dan traversal |
| 6.3 | Pohon merentang (*spanning tree*) |
| 6.4 | *Minimum Spanning Tree*: algoritma Kruskal dan struktur *union-find* |
| 6.5 | *Minimum Spanning Tree*: algoritma Prim dan pemilihan struktur data |
| 6.6 | Lintasan dan sirkuit Euler (teorema Euler) |
| 6.7 | Sirkuit Hamilton dan kompleksitas pencariannya |
| 6.8 | Algoritma Dijkstra untuk lintasan terpendek satu sumber |
| 6.9 | Algoritma Floyd–Warshall untuk semua pasangan |
| 6.10 | Perbandingan kompleksitas dan pemilihan algoritma berdasarkan kasus |

**Kegiatan belajar:** penelusuran Kruskal/Prim manual (PT 150′), latihan Dijkstra/Floyd–Warshall (PT 120′), studi kasus topologi jaringan (TM 30′).
**Tes formatif:** 1 MST lengkap + 2 lintasan terpendek dengan jejak tabel.

---

### BAB 7 — Otomata Berhingga Deterministik (DFA)
**Sub-CPMK:** 4.1 | **Pekan:** 9 | **Estimasi:** 26 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 7.1 | Alfabet, string, panjang string, operasi konkatenasi dan *Kleene star* |
| 7.2 | Bahasa sebagai himpunan string dan operasi bahasa |
| 7.3 | Definisi formal DFA $M=(Q,\Sigma,\delta,q_0,F)$ |
| 7.4 | Tabel transisi dan diagram status |
| 7.5 | Fungsi transisi diperluas $\hat{\delta}$ dan penerimaan string |
| 7.6 | Konstruksi DFA dari deskripsi bahasa (paritas, substring, prefiks/sufiks) |
| 7.7 | Pembuktian kebenaran DFA melalui invarian status |
| 7.8 | Kesalahan umum: status akhir tidak ditandai, transisi tidak lengkap untuk seluruh $\Sigma$ |

**Kegiatan belajar:** konstruksi DFA bertingkat (PT 150′), uji string manual (PT 90′), simulasi JFLAP (TM 30′).
**Tes formatif:** 3 konstruksi DFA + uji 5 string per otomata.

---

### BAB 8 — Otomata Berhingga Non-deterministik (NFA) dan Konversinya
**Sub-CPMK:** 4.2 | **Pekan:** 10 | **Estimasi:** 28 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 8.1 | Definisi formal NFA dan perbedaan dengan DFA |
| 8.2 | Transisi non-deterministik dan ε-transisi |
| 8.3 | ε-closure dan perhitungannya |
| 8.4 | Ekuivalensi NFA dan DFA |
| 8.5 | Algoritma *subset construction* langkah demi langkah |
| 8.6 | Ledakan jumlah status dan reduksi DFA |
| 8.7 | Pengantar ekspresi reguler dan hubungannya dengan otomata berhingga |
| 8.8 | Penerapan: validasi format masukan, pemindai leksikal sederhana, transisi status protokol |
| 8.9 | Kesalahan umum: lupa memasukkan ε-closure pada setiap langkah konversi |

**Kegiatan belajar:** latihan ε-closure (PT 90′), konversi subset construction (PT 150′), simulasi JFLAP (TM 30′).
**Tes formatif:** 1 konversi lengkap NFA→DFA + analisis jumlah status.

---

### BAB 9 — Pemodelan Diskrit Terpadu untuk Sistem Nyata
**Sub-CPMK:** 4.3, 4.4 | **Pekan:** 11–12 | **Estimasi:** 28 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 9.1 | Kerangka pemodelan: identifikasi entitas → relasi → struktur → algoritma |
| 9.2 | Kasus A: perencanaan topologi jaringan (graf berbobot, MST, Dijkstra) |
| 9.3 | Kasus B: penjadwalan dan alokasi sumber daya (pewarnaan graf) |
| 9.4 | Kasus C: validasi masukan sistem (DFA/NFA) |
| 9.5 | Kasus D: analisis dependensi basis data (relasi ekuivalensi, Poset) |
| 9.6 | Analisis kompleksitas dan pemilihan algoritma |
| 9.7 | Penyusunan laporan teknis berbasis bukti |
| 9.8 | Presentasi dan pertahanan model |

**Kegiatan belajar:** penyusunan formalisasi (TM 40′), verifikasi manual (PT 120′), penyusunan laporan proyek (PT 180′).
**Tes formatif:** 3 soal pemodelan terbuka dengan justifikasi algoritma.

---

### LAMPIRAN A — Glosarium, Tabel Hukum Logika, dan Rumus Kombinatorika
**Estimasi:** 14 halaman. Memuat ≥ 80 entri istilah (proposisi, kuantor, tautologi, Poset, pigeonhole, MST, DFA, ε-closure, dan lain-lain) beserta padanan Inggris; tabel lengkap hukum aljabar logika dan hukum himpunan; tabel rumus permutasi–kombinasi; tabel kompleksitas algoritma graf.

### LAMPIRAN B — Kumpulan Soal Pembuktian Terpandu dan Kunci
**Estimasi:** 30 halaman. Memuat 60 soal bertingkat (C2–C4) lengkap dengan petunjuk dan kerangka pembuktian, serta 4 paket latihan UTS/UAS mandiri dengan kunci ringkas.

---

## 7. SPESIFIKASI TEKNIS PENULISAN

| Aspek | Ketentuan |
|---|---|
| Ukuran halaman | A5 (148 × 210 mm), margin 2 cm |
| Tipografi | Body 10,5 pt *serif* (Times New Roman / Book Antiqua); judul sans-serif; spasi 1,15 |
| Tata letak | Satu kolom untuk pembuktian dan diagram; dua kolom untuk uraian naratif |
| Notasi | Simbol logika baku ($\land$, $\lor$, $\lnot$, $\to$, $\leftrightarrow$, $\forall$, $\exists$); himpunan dengan kurung kurawal; graf $G=(V,E)$; otomata $M=(Q,\Sigma,\delta,q_0,F)$ |
| Diagram | Digambar vektor (SVG); diagram Hasse, graf berlabel bobot, dan diagram status otomata wajib konsisten gayanya |
| Sitasi | IEEE *numbered*, konsisten dengan daftar pustaka RPS |
| Istilah asing | Ditulis miring pada kemunculan pertama, disertai padanan Indonesia |
| Warna | Aksen biru tua untuk kotak definisi; hijau untuk kotak "Struktur Pembuktian Baku"; abu untuk kotak galat umum |
| Aksesibilitas | Kontras teks ≥ 4,5:1; diagram memiliki teks alternatif; simbol logika diberi penjelasan verbal |

---

## 8. RENCANA PRODUKSI DAN KENDALI MUTU

| Tahap | Aktivitas | Keluaran | Penanggung Jawab | Durasi |
|:--:|---|---|---|---|
| P1 | Finalisasi outline & alokasi penulis per bab | Dokumen outline ini | Koordinator RMK | 1 pekan |
| P2 | Penulisan draf bab 1–5 | Draf 55% | Tim penulis | 8 pekan |
| P3 | Penulisan draf bab 6–9 + lampiran | Draf 100% | Tim penulis | 6 pekan |
| P4 | Verifikasi matematis (cek ulang setiap pembuktian & kunci) | Lembar verifikasi | Dua penelaah internal | 3 pekan |
| P5 | Uji simulator (semua DFA/NFA di bab 7–9 dijalankan di JFLAP) | Laporan uji simulator | Asisten laboratorium | 2 pekan |
| P6 | Telaah sejawat & uji keterbacaan mahasiswa | Laporan telaah + uji 20 responden | Tim penulis | 2 pekan |
| P7 | Penyuntingan bahasa & tata letak | Naskah siap cetak | Penyunting | 2 pekan |
| P8 | Pengajuan ISBN & pencetakan terbatas | ISBN + 50 eksemplar | Prodi & perpustakaan | 3 pekan |

### Checklist mutu sebelum cetak

- [ ] Seluruh Sub-CPMK RPS memiliki bab/sub-bab pembina yang eksplisit.
- [ ] Tidak ada materi yang masuk kategori *out-of-scope* Dokumen 043 (tidak ada *wiring* gerbang fisik, tidak ada kode struktur data bermemori dinamis, tidak ada kalkulus).
- [ ] Setiap pembuktian induksi memiliki basis, hipotesis, dan langkah yang terverifikasi.
- [ ] Seluruh diagram Hasse, graf berbobot, dan diagram status otomata telah diperiksa ulang.
- [ ] Setiap DFA/NFA di modul dapat dijalankan di JFLAP tanpa galat.
- [ ] Seluruh kunci jawaban di lampiran B terverifikasi.
- [ ] Setiap bab memiliki peta kompetensi, kasus, rangkuman, latihan, dan tes formatif.
- [ ] Seluruh sitasi IEEE valid dan dapat ditelusuri; tidak ada rujukan fiktif.
- [ ] Notasi konsisten lintas bab (mis. selalu $\lnot$ untuk negasi, bukan tanda minus).
- [ ] Uji keterbacaan: ≥ 80% responden menilai materi mudah diikuti.

---

## 9. KETERKAITAN DENGAN DOKUMEN LAIN

| Dokumen | Keterkaitan |
|---|---|
| `058_1_RPS_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md` | Sumber capaian, materi, dan titik asesmen |
| `058_2_SAP_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md` | Sumber alokasi waktu dan urutan kegiatan per pekan |
| `058_4_RENCANA_EVALUASI_ASESMEN_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md` | Sumber bobot dan jadwal evaluasi |
| `058_5_RUBRIK_PENILAIAN_STI-204_MATEMATIKA_DISKRIT_DAN_LOGIKA_07112026.md` | Sumber kriteria penilaian latihan dan tes formatif |
| Dokumen 043 | Batas isi (*in-scope*, *out-of-scope*, *handoff anchor*) |
| Dokumen 037 | Demarkasi silabus antar-MK |

---

*Outline ini merupakan rancangan kerja penulisan modul; perubahan judul bab wajib melalui persetujuan Koordinator RMK dan dicatat dalam riwayat revisi.*
