# OUTLINE BUKU MODUL PEMBELAJARAN
## STI-102 — KALKULUS

> **Jenis dokumen:** Kerangka (*outline*) buku modul ajar yang diturunkan dari RPS
> **Dokumen induk:** `056_1_RPS_STI-102_KALKULUS_07112026.md`
> **Rujukan kurikulum:** Dokumen 005, 007, 043 (Sub-CPMK & Boundary Guardrails), 003 (CPL)
> **Tanggal:** 07 November 2026

---

## 1. METADATA MODUL

| Atribut | Keterangan |
|---|---|
| Judul modul | *Kalkulus untuk Komputasi: Limit, Diferensial, Integral, dan Optimasi Analitik* |
| Kode MK | `STI-102` |
| Penulis | Tim Pengampu Rumpun Sains Komputasi (Core STI) |
| Penelaah | Koordinator RMK Sains Komputasi; Unit Penjaminan Mutu FSTI |
| Jenjang / Semester | S1 / Semester 1 |
| Bobot | 3 SKS Teori (TM 150′ + PT 180′ + BM 180′ per pekan) |
| Prasyarat | — |
| Target pembaca | Mahasiswa S1 SISTEKIN tahun pertama; dosen pengampu; asisten tutorial |
| Estimasi tebal | 240–280 halaman A5 (atau 190–220 halaman A4) |
| Bahasa | Indonesia, dengan istilah teknis Inggris dalam tanda kurung miring |
| Bentuk | Buku modul cetak + e-modul (PDF interaktif dengan tautan GeoGebra/Desmos) |
| Status ISBN | Dalam pengajuan Perpustakaan Nasional RI |
| Edisi | Edisi 1 (2027) |

---

## 2. DASAR DAN BATAS PENYUSUNAN

| Aspek | Ketentuan |
|---|---|
| Sumber capaian | CPMK-1 s.d. CPMK-4 dan Sub-CPMK-1.1 s.d. 4.2 dari Dokumen 043 |
| Sumber materi | Pokok bahasan Tabel C Dokumen 007 dan BoK `BK-IS10`, `BK-IT01` |
| Batas isi (*in-scope*) | Fungsi, limit & kontinuitas, turunan simbolik analitis, integral tentu/tak tentu, deret Taylor/Maclaurin, optimasi gradien analitik |
| Batas larangan (*out-of-scope*) | Komputasi klaster terdistribusi Spark/Kafka, perhitungan galat aproksimasi numerik klasik, penerapan matriks–vektor multidimensi (kewenangan `STA-601`, `STI-205`) |
| Titik serah terima | Aljabar matriks → `STI-205`; matematika diskrit → `STI-204`; komputasi terdistribusi → `STA-601` |

---

## 3. CAPAIAN MODUL

Setelah menuntaskan modul ini, mahasiswa mampu:

1. **Menghitung** limit fungsi aljabar/transenden dan memeriksa kontinuitas menggunakan kaidah kalkulus baku (CPMK-1, C3).
2. **Menerapkan** konsep turunan fungsi univariat dan multivariat serta gradien pada permasalahan laju perubahan dan optimasi ekstremum (CPMK-2, C3).
3. **Menganalisis** permasalahan integral tentu dan tak tentu menggunakan teknik substitusi dan integrasi parsial untuk pemodelan fungsi komputasi (CPMK-3, C4).
4. **Merumuskan** aplikasi kalkulus diferensial–integral pada algoritma optimasi penurunan gradien dan luasan data secara matematis (CPMK-4, C4).

---

## 4. PETA BAB ↔ SUB-CPMK ↔ PEKAN ↔ ASESMEN

| Bab | Judul Bab | Sub-CPMK | Pekan | CPMK | Asesmen Terkait |
|:--:|---|---|:--:|:--:|---|
| 1 | Fungsi, Model Matematika, dan Bahasa Kalkulus | Pengantar 1.1 | 1–2 | CPMK-1 | Tugas 1, UTS |
| 2 | Limit dan Kontinuitas | 1.1 | 2 | CPMK-1 | **Tugas 1**, UTS |
| 3 | Teknik Lanjut Limit dan Bentuk Tak Tentu | 1.2 | 3 | CPMK-1 | Tugas 1, UTS |
| 4 | Diferensial Univariat dan Aturan Turunan | 2.1 | 4 | CPMK-2 | **Tugas 1**, UTS |
| 5 | Turunan Parsial, Gradien, dan Optimasi Ekstremum | 2.1, 2.2 | 4–5 | CPMK-2 | UTS, UAS |
| 6 | Antiturunan dan Teknik Integrasi | 3.1 | 6 | CPMK-3 | UTS, Tugas 2 |
| 7 | Integral Tentu dan Aplikasi Geometri | 3.2 | 7 | CPMK-3 | UTS, Tugas 2, UAS |
| 8 | Deret Taylor, Maclaurin, dan Aproksimasi Fungsi | 4.3 | 11 | CPMK-4 | Tugas 2, UAS |
| 9 | Kalkulus untuk Optimasi Mesin dan Pemodelan Data | 4.1, 4.2 | 9–10, 12 | CPMK-4 | **Tugas 2**, UAS |
| Lampiran A | Glosarium, Tabel Integral, dan Tabel Turunan | — | — | — | — |
| Lampiran B | Kumpulan Soal Terpandu dan Kunci | — | — | — | — |

**Total bab inti:** 9 bab. Setiap bab setara 1–2 pekan pertemuan (16 pekan termasuk UTS & UAS).

---

## 5. STRUKTUR BAKU SETIAP BAB

Setiap bab wajib memuat tujuh komponen berikut, dengan urutan tetap:

| No | Komponen | Isi Wajib | Estimasi |
|:--:|---|---|:--:|
| 1 | **Peta Kompetensi** | Sub-CPMK yang dibina, CPMK induk, indikator kinerja | 0,5 hlm |
| 2 | **Uraian Materi** | 3–6 sub-bab, masing-masing dengan contoh bertahap dan galat umum mahasiswa | 12–20 hlm |
| 3 | **Sorotan Kasus (Case Spotlight)** | Satu penerapan komputasi nyata + pertanyaan analitis | 1,5 hlm |
| 4 | **Rangkuman** | 5–8 butir kunci dalam bentuk poin bernomor | 0,5 hlm |
| 5 | **Latihan Terbimbing** | 8–12 soal bertingkat (C2–C4) dengan petunjuk pengerjaan | 1,5 hlm |
| 6 | **Tes Formatif Mandiri** | 10 soal pilihan ganda + 3 esai pendek, kunci di lampiran daring | 2 hlm |
| 7 | **Rujukan Bab** | 3–6 sitasi IEEE, sinkron dengan daftar pustaka RPS | 0,3 hlm |

---

## 6. OUTLINE RINCI PER BAB

### BAB 1 — Fungsi, Model Matematika, dan Bahasa Kalkulus
**Sub-CPMK:** Pengantar 1.1 | **Pekan:** 1–2 | **Estimasi:** 20 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 1.1 | Konsep fungsi, domain, range, dan notasi $f: X \to Y$ |
| 1.2 | Ragam fungsi: linear, kuadratik, polinomial, rasional, eksponensial, logaritma, trigonometri |
| 1.3 | Fungsi komposit dan fungsi invers |
| 1.4 | Grafik fungsi dan transformasi (geser, skala, refleksi) |
| 1.5 | Model matematika sederhana: pertumbuhan, peluruhan, dan fungsi biaya |
| 1.6 | Kesalahan umum: salah menentukan domain, keliru membaca notasi komposisi |

**Kegiatan belajar:** membaca (BM 90′), latihan sketsa grafik (PT 90′), diskusi model matematika (TM 35′).
**Tes formatif:** identifikasi domain–range dan sketsa grafik untuk 8 fungsi berbeda.

---

### BAB 2 — Limit dan Kontinuitas
**Sub-CPMK:** 1.1 | **Pekan:** 2 | **Estimasi:** 26 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 2.1 | Definisi intuitif limit dan notasi $\lim_{x \to a} f(x) = L$ |
| 2.2 | Limit satu sisi dan syarat keberadaan limit dua sisi |
| 2.3 | Sifat-sifat limit (jumlah, selisih, hasil kali, hasil bagi, pangkat, akar) |
| 2.4 | Limit di ketakhinggaan dan perilaku asimtotik |
| 2.5 | Definisi kontinuitas dan tiga syaratnya |
| 2.6 | Klasifikasi diskontinuitas: *removable*, *jump*, *infinite* |
| 2.7 | Teorema Nilai Antara dan implikasinya pada pencarian akar |

**Kegiatan belajar:** latihan limit aljabar (PT 120′), visualisasi GeoGebra (TM 35′), kuis LMS.
**Tes formatif:** 6 limit aljabar + 4 butir uji kontinuitas.

---

### BAB 3 — Teknik Lanjut Limit dan Bentuk Tak Tentu
**Sub-CPMK:** 1.2 | **Pekan:** 3 | **Estimasi:** 24 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 3.1 | Teorema apit (*squeeze theorem*) dan penerapannya |
| 3.2 | Limit trigonometri khusus: $\lim_{x\to0} \frac{\sin x}{x}$, $\lim_{x\to0} \frac{1-\cos x}{x}$ |
| 3.3 | Bentuk tak tentu: $0/0$, $\infty/\infty$, $\infty - \infty$, $0 \cdot \infty$, $1^\infty$ |
| 3.4 | Dalil L'Hôpital dan syarat keberlakuannya |
| 3.5 | Limit bilangan $e$ dan kaitannya dengan pertumbuhan kontinu |
| 3.6 | Kesalahan umum: menerapkan L'Hôpital pada bentuk yang bukan tak tentu |

**Kegiatan belajar:** latihan bertingkat (PT 120′), pembahasan kasus batas (TM 35′).
**Tes formatif:** 8 limit bentuk tak tentu dengan justifikasi pemilihan metode.

---

### BAB 4 — Diferensial Univariat dan Aturan Turunan
**Sub-CPMK:** 2.1 | **Pekan:** 4 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 4.1 | Definisi turunan sebagai limit dan interpretasi geometris |
| 4.2 | Notasi turunan (Leibniz, Lagrange, Newton) dan maknanya |
| 4.3 | Aturan pangkat, konstan, jumlah, dan selisih |
| 4.4 | Aturan hasil kali dan hasil bagi |
| 4.5 | Aturan rantai dan diferensiasi implisit |
| 4.6 | Turunan tingkat tinggi dan interpretasi fisis (percepatan) |
| 4.7 | Turunan fungsi transenden (eksponensial, logaritma, trigonometri) |

**Kegiatan belajar:** latihan aturan turunan (PT 180′), persiapan Tugas 1 (TM 40′).
**Tes formatif:** 12 soal diferensiasi campuran dengan langkah lengkap.

---

### BAB 5 — Turunan Parsial, Gradien, dan Optimasi Ekstremum
**Sub-CPMK:** 2.1, 2.2 | **Pekan:** 4–5 | **Estimasi:** 32 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 5.1 | Fungsi dua variabel dan permukaan $z = f(x,y)$ |
| 5.2 | Turunan parsial orde pertama dan kedua |
| 5.3 | Vektor gradien dan interpretasi arah |
| 5.4 | Aturan rantai multivariat |
| 5.5 | Laju perubahan dan *related rates* |
| 5.6 | Titik kritis, uji turunan pertama, dan uji turunan kedua |
| 5.7 | Optimasi terapan: biaya, luas, volume, dan efisiensi |
| 5.8 | Matriks Hessian dan uji titik pelana (pengantar, tanpa aljabar matriks penuh) |

**Kegiatan belajar:** latihan optimasi (PT 150′), studi kasus biaya (TM 50′).
**Tes formatif:** 3 soal optimasi lengkap dengan pembuktian minimum/maksimum.

---

### BAB 6 — Antiturunan dan Teknik Integrasi
**Sub-CPMK:** 3.1 | **Pekan:** 6 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 6.1 | Antiturunan dan integral tak tentu; konstanta integrasi |
| 6.2 | Tabel integral dasar |
| 6.3 | Substitusi-u dan pemilihan substitusi yang tepat |
| 6.4 | Integrasi parsial $\int u\,dv = uv - \int v\,du$ dan heuristik ILATE |
| 6.5 | Integrasi fungsi rasional sederhana (dekomposisi parsial pengantar) |
| 6.6 | Integral fungsi trigonometri dan eksponensial |
| 6.7 | Kesalahan umum: lupa konstanta integrasi, salah diferensial substitusi |

**Kegiatan belajar:** latihan bertingkat (PT 180′), pembahasan strategi pemilihan teknik (TM 35′).
**Tes formatif:** 10 integral tak tentu campuran.

---

### BAB 7 — Integral Tentu dan Aplikasi Geometri
**Sub-CPMK:** 3.2 | **Pekan:** 7 | **Estimasi:** 28 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 7.1 | Jumlah Riemann dan definisi integral tentu |
| 7.2 | Teorema Dasar Kalkulus I dan II |
| 7.3 | Sifat-sifat integral tentu dan teorema nilai rata-rata integral |
| 7.4 | Luas daerah di bawah kurva dan antara dua kurva |
| 7.5 | Volume benda putar: metode cakram, cincin, dan kulit tabung |
| 7.6 | Panjang busur dan luas permukaan (pengantar) |
| 7.7 | Penerapan pada akumulasi kuantitas kontinu |

**Kegiatan belajar:** latihan aplikasi geometri (PT 150′), visualisasi GeoGebra (TM 35′).
**Tes formatif:** 2 soal luas daerah + 2 soal volume benda putar.

---

### BAB 8 — Deret Taylor, Maclaurin, dan Aproksimasi Fungsi
**Sub-CPMK:** 4.3 | **Pekan:** 11 | **Estimasi:** 24 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 8.1 | Polinom Taylor orde-$n$ di sekitar titik $a$ |
| 8.2 | Deret Maclaurin dan deret fungsi umum ($e^x$, $\sin x$, $\cos x$, $\ln(1+x)$) |
| 8.3 | Sisa galat Lagrange dan estimasi ketelitian |
| 8.4 | Konsep konvergensi deret (pengantar, tanpa teori deret lanjut) |
| 8.5 | Aproksimasi fungsi dalam implementasi komputasi |
| 8.6 | Keterbatasan: radius konvergensi dan titik singular |

**Kegiatan belajar:** konstruksi deret (PT 120′), estimasi galat (TM 35′).
**Tes formatif:** ekspansi 3 fungsi + estimasi galat orde berikutnya.

---

### BAB 9 — Kalkulus untuk Optimasi Mesin dan Pemodelan Data
**Sub-CPMK:** 4.1, 4.2 | **Pekan:** 9–10, 12 | **Estimasi:** 30 halaman

| Sub-bab | Pokok Bahasan |
|---|---|
| 9.1 | Fungsi kerugian (*loss function*) dan fungsi objektif |
| 9.2 | Turunan parsial sebagai dasar arah penurunan |
| 9.3 | Derivasi aturan pembaruan *Gradient Descent* |
| 9.4 | Pengaruh *learning rate*: konvergensi, osilasi, divergensi |
| 9.5 | Integral sebagai akumulasi kontinu dan rata-rata fungsi |
| 9.6 | Pemodelan luasan data dan ekspektasi variabel kontinu |
| 9.7 | Studi kasus: optimasi biaya, akumulasi *bandwidth*, laju permintaan |

**Kegiatan belajar:** derivasi bersama (TM 70′), simulasi iterasi manual (PT 120′), penyusunan proyek (PT 180′).
**Tes formatif:** 3 soal yang menghubungkan gradien dengan perilaku algoritma.

---

### LAMPIRAN A — Glosarium, Tabel Integral, dan Tabel Turunan
**Estimasi:** 12 halaman. Memuat ≥ 70 entri istilah (limit, kontinuitas, gradien, antiturunan, deret, konvergensi) beserta padanan Inggris, tabel turunan & integral standar, serta tabel identitas trigonometri yang dipakai.

### LAMPIRAN B — Kumpulan Soal Terpandu dan Kunci
**Estimasi:** 28 halaman. Memuat 60 soal bertingkat (C2–C4) lengkap dengan petunjuk pengerjaan dan kunci jawaban ringkas, serta 4 paket soal latihan UTS/UAS mandiri.

---

## 7. SPESIFIKASI TEKNIS PENULISAN

| Aspek | Ketentuan |
|---|---|
| Ukuran halaman | A5 (148 × 210 mm), margin 2 cm |
| Tipografi | Body 10,5 pt *serif* (Times New Roman / Book Antiqua); judul sans-serif; spasi 1,15 |
| Tata letak | Satu kolom untuk derivasi matematis (lebar penuh); dua kolom untuk uraian naratif |
| Rumus | Diketik dengan LaTeX/MathType; penomoran rumus per bab, mis. (4.3) |
| Sitasi | IEEE *numbered*, konsisten dengan daftar pustaka RPS |
| Istilah asing | Ditulis miring pada kemunculan pertama, disertai padanan Indonesia |
| Warna | Aksen biru tua untuk kotak definisi; abu untuk kotak galat umum |
| Aksesibilitas | Kontras teks ≥ 4,5:1; gambar memiliki teks alternatif pada versi digital; deskripsi verbal untuk setiap grafik |

---

## 8. RENCANA PRODUKSI DAN KENDALI MUTU

| Tahap | Aktivitas | Keluaran | Penanggung Jawab | Durasi |
|:--:|---|---|---|---|
| P1 | Finalisasi outline & alokasi penulis per bab | Dokumen outline ini | Koordinator RMK | 1 pekan |
| P2 | Penulisan draf bab 1–5 | Draf 55% | Tim penulis | 8 pekan |
| P3 | Penulisan draf bab 6–9 + lampiran | Draf 100% | Tim penulis | 6 pekan |
| P4 | Verifikasi matematis (cek ulang setiap derivasi & kunci) | Lembar verifikasi | Dua penelaah internal | 3 pekan |
| P5 | Telaah sejawat & uji keterbacaan mahasiswa | Laporan telaah + uji 20 responden | Tim penulis | 2 pekan |
| P6 | Penyuntingan bahasa & tata letak | Naskah siap cetak | Penyunting | 2 pekan |
| P7 | Pengajuan ISBN & pencetakan terbatas | ISBN + 50 eksemplar | Prodi & perpustakaan | 3 pekan |

### Checklist mutu sebelum cetak

- [ ] Seluruh Sub-CPMK RPS memiliki bab/sub-bab pembina yang eksplisit.
- [ ] Tidak ada materi yang masuk kategori *out-of-scope* Dokumen 043 (tidak ada Spark/Kafka, tidak ada numerik aproksimatif, tidak ada matriks–vektor multidimensi).
- [ ] Setiap derivasi matematis telah diperiksa ulang oleh penelaah kedua.
- [ ] Seluruh kunci jawaban di lampiran B terverifikasi.
- [ ] Setiap bab memiliki peta kompetensi, kasus, rangkuman, latihan, dan tes formatif.
- [ ] Seluruh sitasi IEEE valid dan dapat ditelusuri; tidak ada rujukan fiktif.
- [ ] Notasi konsisten lintas bab (mis. selalu gunakan $\nabla f$, bukan campuran grad dan $\nabla$).
- [ ] Uji keterbacaan: ≥ 80% responden menilai materi mudah diikuti.

---

## 9. KETERKAITAN DENGAN DOKUMEN LAIN

| Dokumen | Keterkaitan |
|---|---|
| `056_1_RPS_STI-102_KALKULUS_07112026.md` | Sumber capaian, materi, dan titik asesmen |
| `056_2_SAP_STI-102_KALKULUS_07112026.md` | Sumber alokasi waktu dan urutan kegiatan per pekan |
| `056_4_RENCANA_EVALUASI_ASESMEN_STI-102_KALKULUS_07112026.md` | Sumber bobot dan jadwal evaluasi |
| `056_5_RUBRIK_PENILAIAN_STI-102_KALKULUS_07112026.md` | Sumber kriteria penilaian latihan dan tes formatif |
| Dokumen 043 | Batas isi (*in-scope*, *out-of-scope*, *handoff anchor*) |
| Dokumen 037 | Demarkasi silabus antar-MK |

---

*Outline ini merupakan rancangan kerja penulisan modul; perubahan judul bab wajib melalui persetujuan Koordinator RMK dan dicatat dalam riwayat revisi.*
