# 010 — Rancangan Matriks CPL, CPMK, BoK dan Boundary Guardrails

## KOM-312, KOM-526 dan KFC-506 — Teknik Informatika UWG 2026

> **Status: USULAN untuk ditinjau, belum disahkan.** Identitas dan relasi sumber yang ditandai **[S]** disalin dari buku KPT; seluruh CPMK, Sub-CPMK, target, isi mingguan, alokasi waktu, asesmen, teknologi dan batas materi di bawah adalah **[U] usulan**, bukan RPS yang sudah berlaku. **[K]** berarti perlu konfirmasi. Struktur mengacu pada [Dokumen 043 SISTEKIN](../KURIKULUM2026_REVISI/043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md) hanya sebagai contoh format; identitas, CPL, BK, aturan dan isi SISTEKIN tidak dipindahkan sebagai ketentuan Teknik Informatika.

## 1. Dasar dan konvensi

### 1.1 Rujukan dan status

| Rujukan | Pemakaian | Batas |
|---|---|---|
| [Buku KPT OBE Teknik Informatika UWG 2026, 11 September 2026](../KPT_FIX_3PRODI/KPT%20Program%20Studi/Buku%20KPT%20OBE%20Teknik%20Informatika%20UWG%202026%20%5BUpdate%2011%20September%202026%5D.docx), SHA-256 `a54a570150d0f7d38d633e72104b326062981818599101017dd3a7b4dfb2601d` | [S] Tabel 11, 13–16, 18; pengecekan terbatas tiga baris Tabel 19. | Ekstraksi utama tidak menemukan rumusan CPMK per MK; RPS dan workbook terpisah belum diperiksa. |
| [001 CPL](001_CPL_TEKNIK_INFORMATIKA_07112026_0859.md), [003 BK](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md), [004 MK–CPL–BK](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md), [009 analisis tiga MK](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md) | Keterlacakan identitas, CPL dan BK UWG; catatan perbedaan sumber. | Transkripsi dan pemeriksaan terbatas, bukan pengesahan maupun bukti pelaksanaan. |
| [005 pemetaan APTIKOM](005_PEMETAAN_APTIKOM_MK_INFORMATIKA_07112026_0910.md), [008 Tabel 4 APTIKOM Informatika](008_TABEL_4_RUMUSAN_BAHAN_KAJIAN_APTIKOM_INFORMATIKA_07112026_0942.md) | [U] Pembanding kandidat berdasarkan judul. | A05/A14/A19 adalah alias untuk area APTIKOM pada 005, bukan kode BK UWG dan bukan bukti isi atau cakupan mata kuliah. |
| [002 CPMK](002_CPMK_TEKNIK_INFORMATIKA_07112026_0859.md) | Prinsip CPMK/Sub-CPMK dan contoh format kodifikasi. | Contoh kode dan bobot tidak menjadi rumusan resmi per MK. |

**CPL04 [S]**, berlaku untuk tiga MK menurut Tabel 18:

> Mampu menganalisis kebutuhan pengguna dan organisasi serta merancang, mengimplementasikan, menguji, mengintegrasikan, dan memelihara sistem informasi atau perangkat lunak berkualitas dengan arsitektur, antarmuka, basis data, algoritma, struktur data, dan platform yang sesuai.

CPL04 berkaitan dengan **PL01 dan PL04** menurut Tabel 11, dan dengan **BK02** sebagai bahan kajian utama menurut Tabel 14. BK yang lebih luas pada Tabel 15 dicatat apa adanya; relasi tambahan dan cakupannya memerlukan validasi, bukan otomatis CPL tambahan.

### 1.2 Waktu, kode, dan penilaian usulan

- **Prasyarat formal, pembagian teori/praktik dan rincian beban 3 SKS belum terverifikasi [K].** Tanda `+P` tidak otomatis berarti komposisi tertentu.
- Agar kolom waktu dapat direncanakan, **skenario kerja [U]** mengasumsikan **2 SKS teori + 1 SKS praktikum**, dengan **100 menit tatap muka + 170 menit praktikum terbimbing = 270 menit** per minggu pembelajaran. Kode **A** pada tabel berarti skenario ini, bukan ketetapan prodi. Durasi **PT dan BM belum ditetapkan**, sehingga belum dimasukkan ke total 270 menit. Bila pembagian SKS atau standar waktu prodi berbeda, seluruh alokasi harus dihitung ulang.
- Kode **E** pada minggu 8 dan 16 berarti **usulan slot evaluasi hingga 270 menit**; durasi, moda dan apakah menggunakan waktu praktikum mengikuti jadwal serta keputusan institusi. Bukan tambahan otomatis terhadap A. Tugas sumatif disiapkan dalam waktu PT yang alokasinya masih menunggu ketentuan prodi.
- Empat titik **Tugas 1 20%, UTS 25%, Tugas 2 25%, UAS 30%** dan ambang **4 dari 5 butir/kasus** di setiap instrumen adalah **[U] simulasi**, bukan aturan resmi TI. Setiap instrumen diberi satu CPMK utama agar bobot tidak terhitung ganda. Kinerja tiap butir dinilai sesuai bukti; target ketercapaian CPMK tetap memerlukan kebijakan prodi. Nilai akhir MK = `(20×T1 + 25×UTS + 25×T2 + 30×UAS)/100`, dengan skor setiap instrumen 0–100.
- Instrumen berisi lima butir uji/cek bernilai sama sebagai rancangan awal. Bukti wajib menunjukkan **kondisi, langkah, hasil diharapkan dan aktual**, termasuk alasan gagal dan perbaikan. Asesmen dapat memakai keterampilan sebelumnya sebagai prasyarat; **penilaian utama** tetap fokus CPMK yang dipetakan. Jika kerja kelompok, catat kontribusi dan lakukan demonstrasi/penjelasan individu.
- Kode `CPMK04.1`–`CPMK04.4` dan `Sub-CPMK04.x.y` mengikuti **contoh pola kodifikasi** pada 002, tetapi kode dan rumusannya di sini adalah usulan. Kode bersifat **lokal per MK**: `KOM-312/CPMK04.1` berbeda dari `KOM-526/CPMK04.1`; bukan identitas CPMK lintas MK yang sama.
- Lima butir adalah uji minimum per instrumen; standar mutu, integritas akademik, batas remedial, pembobotan dan kelayakan waktu memerlukan persetujuan pengampu/prodi. **Bobot MK tidak sama dengan nilai ketercapaian CPL lintas MK.**

## 2. Peta perbandingan tiga MK

| Atribut | KOM-312 Pemrograman Web | KOM-526 Sistem Aplikasi Web | KFC-506 Sistem Aplikasi Lintas Platform |
|---|---|---|---|
| Semester / SKS / tipe [S] | 3 / 3 / +P | 5 / 3 / +P | 5 / 3 / +P; wajib konsentrasi MC |
| Prasyarat formal [K] | Belum terverifikasi; usulan FST-102 | Belum terverifikasi; usulan KOM-312 dan FST-207 | Belum terverifikasi; usulan FST-102 dan KOM-311 |
| CPL [S] | CPL04 | CPL04 | CPL04 |
| BK UWG pada Tabel 15 [S] | BK02, BK09, BK10 | BK02, BK03, BK04, BK05, BK06, BK07, BK08 | BK02 |
| Kandidat APTIKOM menurut 005 [U] | A05 Software Development Fundamentals; A14 Programming Fundamentals; A19 Specialized Platform Development | A05 Software Development Fundamentals; A19 Specialized Platform Development | A05 Software Development Fundamentals; A19 Specialized Platform Development |
| Fokus pembeda [U] | Fondasi halaman web semantik, responsif dan interaktif di sisi klien. | Sistem web dengan logika server, data, autentikasi dasar dan pengujian integrasi. | Satu basis kode aplikasi lintas platform; adaptasi, state dan uji pada dua target. |

Handoff di bawah **bukan prasyarat formal**. Mahasiswa pada KOM-526 dan KFC-506 perlu asesmen diagnostik untuk mengetahui fondasi awal; urutan MK semester 5 yang sama tidak boleh diasumsikan sebagai hubungan saling mendahului.

---

## 3. KOM-312 — Pemrograman Web (+P)

### 3.1 Identitas, CPL dan BoK

| Atribut | Isi dan status |
|---|---|
| Identitas [S] | KOM-312; Pemrograman Web (+P); semester 3; 3 SKS; non-konsentrasi pada Tabel 18. |
| Prasyarat / T:P [K] | Prasyarat resmi dan pembagian teori–praktik belum terverifikasi; usulan FST-102 dan diagnostik awal pada bagian 8. Asumsi waktu A pada bagian 1.2 bukan keputusan resmi. |
| CPL [S] | CPL04, rumusan pada bagian 1.1; dibebankan pada Tabel 18. |
| BK UWG [S] | **BK02** Algoritma dan Rekayasa Perangkat Lunak; **BK09** Komunikasi, Profesionalisme dan Kolaborasi; **BK10** Manajemen Proyek dan Technopreneurship — Tabel 15. BK09/BK10 perlu klarifikasi keterkaitan dan bukti asesmen; bukan otomatis CPL tambahan. |
| BoK APTIKOM [U] | A05, A14 dan A19 merupakan kandidat berdasarkan judul, bukan pemetaan resmi. |

### 3.2 CPMK dan Sub-CPMK [U]

Setiap rumusan berikut menggunakan kondisi tugas praktikum dan kriteria minimum yang dijabarkan pada instrumen di bagian 3.4. Target 4/5 adalah usulan, bukan ambang resmi.

| Kode lokal | CPMK terukur | Bloom | CPL |
|---|---|---|---|
| CPMK04.1 | Mahasiswa mampu **menyusun** halaman HTML semantik untuk kasus yang diberikan, termasuk konten dan formulir, dengan memenuhi minimal 4 dari 5 cek Tugas 1. | C3 | CPL04 |
| CPMK04.2 | Mahasiswa mampu **menerapkan** CSS dan tata letak responsif pada halaman yang diberikan, dengan memenuhi minimal 4 dari 5 cek UTS pada dua lebar layar. | C3 | CPL04 |
| CPMK04.3 | Mahasiswa mampu **mengimplementasikan** interaksi JavaScript dan validasi masukan sisi klien pada kasus yang diberikan, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C3 | CPL04 |
| CPMK04.4 | Mahasiswa mampu **membangun dan menguji** halaman web responsif interaktif pada kasus yang disepakati serta mendokumentasikan hasil, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 | CPL04 |

| Kode lokal | Sub-CPMK operasional | CPMK | Bloom |
|---|---|---|---|
| Sub-CPMK04.1.1 | Menyusun struktur dokumen semantik, heading, konten, gambar dan navigasi. | CPMK04.1 | C3 |
| Sub-CPMK04.1.2 | Membuat tabel dan formulir berlabel dengan validasi HTML dasar. | CPMK04.1 | C3 |
| Sub-CPMK04.2.1 | Menerapkan selektor, warna, tipografi dan box model pada kasus. | CPMK04.2 | C3 |
| Sub-CPMK04.2.2 | Menggunakan Flexbox dan media query untuk dua lebar layar. | CPMK04.2 | C3 |
| Sub-CPMK04.3.1 | Menulis variabel, fungsi dan percabangan untuk membaca serta memvalidasi masukan. | CPMK04.3 | C3 |
| Sub-CPMK04.3.2 | Menghubungkan elemen halaman dan fungsi dengan DOM/event serta menampilkan hasil. | CPMK04.3 | C3 |
| Sub-CPMK04.4.1 | Mengintegrasikan HTML, CSS dan JavaScript dasar pada halaman sesuai kasus. | CPMK04.4 | C6 |
| Sub-CPMK04.4.2 | Menjalankan dan mencatat pengujian navigasi, interaksi, responsivitas dan perbaikan. | CPMK04.4 | C4 |

### 3.3 Rencana 16 pertemuan [U]

A = skenario 100 menit tatap muka + 170 menit praktik; E = slot evaluasi usulan hingga 270 menit. Keduanya bersyarat sebagaimana bagian 1.2; PT/BM belum ditetapkan.

| Pekan | Sub-CPMK | Topik dan kegiatan | Metode | Waktu | Bukti / asesmen |
|---:|---|---|---|---|---|
| 1 | 04.1.1 | Orientasi web, browser, struktur dokumen, teks dan heading. | Kuliah, demonstrasi, praktik | A | Formatif: halaman profil awal. |
| 2 | 04.1.1 | Elemen semantik, tautan, navigasi dan gambar ber-alt. | Praktik, umpan balik | A | Formatif: halaman informasi dan cek navigasi. |
| 3 | 04.1.2 | Tabel, formulir, label, tipe input dan validasi HTML. | Demonstrasi, praktik | A | Formatif: tabel dan formulir simulasi. |
| 4 | 04.1.1, 04.1.2, 04.2.1 | Tugas HTML dan pengantar CSS; penilaian T1 hanya pada HTML. | Penugasan, praktik | A | **Tugas 1: 20%, CPMK04.1.** |
| 5 | 04.2.1 | Selektor, cascade dasar, warna, tipografi dan box model. | Kuliah, praktik | A | Formatif: stylesheet dan kartu. |
| 6 | 04.2.2 | Flexbox: container, item, alignment, wrap dan gap. | Demonstrasi, praktik | A | Formatif: navigasi dan kartu fleksibel. |
| 7 | 04.2.2 | Media query, pengujian dua lebar layar dan perbaikan overflow. | Praktik, diskusi | A | Formatif: tangkapan layar dua lebar. |
| 8 | 04.2.1, 04.2.2 | Evaluasi CSS dan layout responsif. | Ujian praktik | E | **UTS: 25%, CPMK04.2.** |
| 9 | 04.3.1 | JavaScript dasar: nilai, tipe, operator dan fungsi. | Kuliah, latihan | A | Formatif: fungsi dan keluaran sederhana. |
| 10 | 04.3.1 | Percabangan dan validasi masukan, termasuk nilai kosong/tidak valid. | Praktik, uji kasus | A | Formatif: fungsi dengan kasus valid dan invalid. |
| 11 | 04.3.2 | DOM/event, membaca input dan memperbarui keluaran secara aman. | Demonstrasi, praktik | A | Formatif: purwarupa interaksi. |
| 12 | 04.3.1, 04.3.2 | Menyelesaikan dan menguji interaksi berbasis formulir. | Praktik, demonstrasi | A | **Tugas 2: 25%, CPMK04.3.** |
| 13 | 04.4.1 | Perencanaan kasus halaman, konten berizin dan sketsa. | Studi kasus, diskusi | A | Formatif: rancangan dan kerangka halaman. |
| 14 | 04.4.1 | Integrasi HTML, CSS dan interaksi JavaScript. | Praktik proyek | A | Formatif: purwarupa. |
| 15 | 04.4.2 | Uji navigasi, interaksi, keyboard dan dua lebar; perbaikan. | Pengujian, umpan balik | A | Formatif: catatan kasus dan perbaikan. |
| 16 | 04.4.1, 04.4.2 | Demonstrasi, penjelasan kode dan penyerahan halaman. | Ujian proyek | E | **UAS: 30%, CPMK04.4.** |

### 3.4 Instrumen utama dan bukti [U]

| Instrumen | CPMK / bobot | Lima butir cek bernilai sama; target usulan ≥4/5 | Bukti minimum |
|---|---|---|---|
| Tugas 1, pekan 4 | 04.1 / 20% | (1) struktur semantik; (2) hierarki heading; (3) navigasi dan gambar ber-alt; (4) tabel berheader; (5) formulir berlabel dan validasi HTML. | HTML, aset berizin dan daftar cek; CSS tidak dinilai. |
| UTS, pekan 8 | 04.2 / 25% | (1) selektor/tipografi; (2) box model; (3) Flexbox; (4) tampilan lebar terbaca; (5) tampilan sempit terbaca tanpa overflow utama. | Berkas HTML/CSS dan tangkapan dua lebar. |
| Tugas 2, pekan 12 | 04.3 / 25% | (1) input valid menghasilkan keluaran benar; (2) input kosong ditolak; (3) input tidak valid ditolak; (4) event tombol memperbarui DOM; (5) reset memulihkan kondisi awal. | HTML/JS, tabel lima uji dan penjelasan individu. |
| UAS, pekan 16 | 04.4 / 30% | (1) HTML/CSS/JS terintegrasi; (2) navigasi berfungsi; (3) interaksi berfungsi; (4) dua lebar dan keyboard diuji; (5) hasil uji, perbaikan dan langkah menjalankan dicatat. | Halaman berjalan lokal, dokumentasi dan demonstrasi individu. |

### 3.5 Boundary guardrails [U]

| Jenis | Batas yang diusulkan — untuk ditinjau, bukan larangan resmi |
|---|---|
| In-scope | HTML semantik dan formulir; CSS/Flexbox responsif; JavaScript dasar, DOM/event dan validasi klien; halaman lokal dan uji dasar. |
| Out-of-scope | Implementasi autentikasi/otorisasi server, basis data server dan sistem web penuh menjadi fokus rancangan KOM-526; aplikasi lintas runtime menjadi fokus rancangan KFC-506. Validasi klien tidak menggantikan keamanan server. |
| Handoff | Artefak HTML/CSS/JS, kemampuan membaca input dan hasil uji dapat menjadi bekal **usulan** untuk KOM-526 atau KFC-506, setelah kesepakatan pengampu. Bukan prasyarat formal. |

---

## 4. KOM-526 — Sistem Aplikasi Web (+P)

### 4.1 Identitas, CPL dan BoK

| Atribut | Isi dan status |
|---|---|
| Identitas [S] | KOM-526; Sistem Aplikasi Web (+P); semester 5; 3 SKS; non-konsentrasi pada Tabel 18. |
| Prasyarat / T:P [K] | Belum terverifikasi; usulan KOM-312 dan FST-207 serta diagnostik awal pada bagian 8, bukan aturan prasyarat resmi. Pembagian teori–praktik perlu konfirmasi. |
| CPL [S] | CPL04, rumusan pada bagian 1.1; Tabel 18. |
| BK UWG [S] | Tabel 15: **BK02** Algoritma dan Rekayasa Perangkat Lunak; **BK03** Data dan Kecerdasan Artifisial; **BK04** Multimedia dan Interaksi Digital; **BK05** Bahasa Alami dan Sistem Cerdas Lanjut; **BK06** Arsitektur, Sistem, Jaringan, Cloud, Mobile dan IoT; **BK07** Keamanan, Privasi, Etika dan Hukum Digital; **BK08** Riset dan Inovasi Informatika. Nama/ruang lingkup lengkap di [003](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md). |
| Rekonsiliasi [K] | Tabel 14 mengaitkan CPL04 dengan BK02. Tabel 16 menyebut MK ini sebagai contoh pada CPL05, 06, 08 dan 09; pembebanan tambahan dan relevansi BK03–BK08 masih perlu disepakati. Usulan di sini tidak menambah CPL. |
| BoK APTIKOM [U] | A05 dan A19 adalah kandidat dari judul pada 005, bukan penetapan resmi. |

### 4.2 CPMK dan Sub-CPMK [U]

| Kode lokal | CPMK terukur | Bloom | CPL |
|---|---|---|---|
| CPMK04.1 | Mahasiswa mampu **merancang** kebutuhan, alur dan model data untuk kasus sistem web yang diberikan, dengan minimal 4 dari 5 cek rancangan Tugas 1 terpenuhi. | C6 | CPL04 |
| CPMK04.2 | Mahasiswa mampu **mengimplementasikan** rute dan operasi CRUD server–basis data pada kasus yang diberikan, dengan minimal 4 dari 5 kasus UTS lulus. | C3 | CPL04 |
| CPMK04.3 | Mahasiswa mampu **menerapkan dan menguji** autentikasi, pembatasan akses dan validasi server dasar pada aplikasi latihan, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C3 | CPL04 |
| CPMK04.4 | Mahasiswa mampu **mengintegrasikan dan menguji** sistem web sesuai rancangan serta mendokumentasikan hasil, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 | CPL04 |

| Kode lokal | Sub-CPMK operasional | CPMK | Bloom |
|---|---|---|---|
| Sub-CPMK04.1.1 | Menganalisis aktor, kebutuhan dan alur kasus yang dapat diuji. | CPMK04.1 | C4 |
| Sub-CPMK04.1.2 | Merancang entitas, relasi dan keterkaitan kebutuhan–data. | CPMK04.1 | C6 |
| Sub-CPMK04.2.1 | Mengimplementasikan rute, handler dan respons server sesuai kasus. | CPMK04.2 | C3 |
| Sub-CPMK04.2.2 | Menghubungkan operasi create, read, update dan delete dengan penyimpanan data. | CPMK04.2 | C3 |
| Sub-CPMK04.3.1 | Menerapkan login, logout, sesi dan pembatasan akses berdasarkan peran. | CPMK04.3 | C3 |
| Sub-CPMK04.3.2 | Menerapkan validasi server dan penggunaan kueri terparameter pada data masukan. | CPMK04.3 | C3 |
| Sub-CPMK04.4.1 | Mengintegrasikan rute, data, antarmuka dan akses sesuai rancangan. | CPMK04.4 | C6 |
| Sub-CPMK04.4.2 | Menguji alur normal dan kesalahan serta mendokumentasikan hasil dan perbaikan. | CPMK04.4 | C4 |

### 4.3 Rencana 16 pertemuan [U]

A dan E mengikuti skenario bersyarat pada bagian 1.2; PT/BM belum ditetapkan. Empat varian teknis dan rincian 16 minggu tersedia pada [bagian 13](#13-empat-varian-implementasi-kom-526-u); bahasa/framework dan database dipilih pengampu sesuai fasilitas, tidak diasumsikan sebagai standar resmi.

| Pekan | Sub-CPMK | Topik dan kegiatan | Metode | Waktu | Bukti / asesmen |
|---:|---|---|---|---|---|
| 1 | 04.1.1 | Diagnostik fondasi web, orientasi kasus, peran klien dan server. | Diskusi, demonstrasi | A | Formatif: peta aktor dan alur awal. |
| 2 | 04.1.1 | Kebutuhan fungsional, peran, alur dan kriteria penerimaan. | Studi kasus, lokakarya | A | Formatif: daftar kebutuhan. |
| 3 | 04.1.2 | Pemodelan entitas/relasi dan keterkaitan kebutuhan dengan data. | Praktik perancangan | A | Formatif: diagram dan contoh data dummy. |
| 4 | 04.1.1, 04.1.2, 04.2.1 | Penyerahan rancangan; pengantar rute dan handler server. | Presentasi, praktik | A | **Tugas 1: 20%, CPMK04.1.** |
| 5 | 04.2.1 | Rute, metode permintaan, handler dan respons. | Kuliah, praktik | A | Formatif: rute yang dapat diuji. |
| 6 | 04.2.2 | Koneksi database dan operasi create/read dengan data dummy. | Demonstrasi, praktik | A | Formatif: tambah dan tampil data. |
| 7 | 04.2.2 | Update/delete dan penanganan data yang tidak ditemukan. | Praktik, uji | A | Formatif: CRUD dan catatan uji. |
| 8 | 04.2.1, 04.2.2 | Evaluasi implementasi server dan database. | Ujian praktik | E | **UTS: 25%, CPMK04.2.** |
| 9 | 04.3.1 | Akun, login dan logout pada lingkungan lokal. | Demonstrasi, praktik | A | Formatif: alur login/logout. |
| 10 | 04.3.1 | Sesi, akses berdasar peran dan penolakan akses. | Studi kasus, praktik | A | Formatif: matriks peran dan uji akses. |
| 11 | 04.3.2 | Validasi di server, kueri terparameter dan penanganan kesalahan. | Praktik, uji kasus | A | Formatif: pengujian input valid/tidak valid. |
| 12 | 04.3.1, 04.3.2 | Penyelesaian dan pengujian modul akses/validasi. | Praktik, demonstrasi | A | **Tugas 2: 25%, CPMK04.3.** |
| 13 | 04.4.1 | Integrasi antarmuka, rute, data dan akses sesuai rancangan. | Praktik proyek | A | Formatif: purwarupa terintegrasi. |
| 14 | 04.4.1 | Melengkapi alur kasus dan data dummy; evaluasi konsistensi rancangan. | Praktik, konsultasi | A | Formatif: alur aplikasi end-to-end. |
| 15 | 04.4.2 | Uji normal dan gagal, perbaikan, dokumentasi menjalankan lokal. | Pengujian, umpan balik | A | Formatif: hasil uji dan daftar perbaikan. |
| 16 | 04.4.1, 04.4.2 | Demonstrasi sistem, hasil uji dan penjelasan individu. | Ujian proyek | E | **UAS: 30%, CPMK04.4.** |

### 4.4 Instrumen utama dan bukti [U]

| Instrumen | CPMK / bobot | Lima butir cek bernilai sama; target usulan ≥4/5 | Bukti minimum |
|---|---|---|---|
| Tugas 1, pekan 4 | 04.1 / 20% | (1) aktor dan peran teridentifikasi; (2) minimal tiga kebutuhan dapat diuji; (3) alur utama tergambar; (4) minimal dua entitas dan relasinya terdefinisi; (5) kebutuhan terhubung ke data/alur. | Dokumen kebutuhan, alur, model data dan penjelasan individu. |
| UTS, pekan 8 | 04.2 / 25% | (1) create; (2) read; (3) update; (4) delete; (5) permintaan untuk data yang tidak ditemukan ditangani. | Server, database dummy dan hasil lima uji CRUD. |
| Tugas 2, pekan 12 | 04.3 / 25% | (1) login valid; (2) login tidak valid ditolak; (3) akses peran tidak berwenang ditolak; (4) logout mengakhiri akses sesi; (5) masukan invalid ditolak server dan data diproses dengan kueri terparameter. | Kode, matriks peran dan hasil uji; gunakan pustaka pengelolaan kata sandi yang aman dan data dummy. |
| UAS, pekan 16 | 04.4 / 30% | (1) alur sesuai rancangan terintegrasi; (2) data tersimpan dan terbaca; (3) pembatasan akses bekerja; (4) alur salah ditangani dan dicatat; (5) petunjuk lokal, hasil uji dan perbaikan tersedia. | Aplikasi lokal, data dummy, hasil uji dan demonstrasi individu. |

**Batas keamanan:** latihan ini hanya mengajarkan praktik dasar, bukan jaminan sistem siap produksi atau audit keamanan lengkap. Jangan gunakan kredensial atau data pribadi nyata.

### 4.5 Boundary guardrails [U]

| Jenis | Batas yang diusulkan — untuk ditinjau, bukan larangan resmi |
|---|---|
| In-scope | Kebutuhan dan model data aplikasi; server, rute, CRUD; login/peran, validasi server dan kueri terparameter; integrasi, pengujian dan dokumentasi lokal. |
| Out-of-scope | Pendalaman pembuatan aplikasi multiruntime satu basis kode direncanakan pada KFC-506; pengembangan komponen web dasar dari nol bukan fokus utama. Infrastruktur produksi berskala besar dan audit keamanan lanjutan tidak menjadi target rancangan ini. |
| Handoff | Fondasi klien dari KOM-312 dapat digunakan setelah diagnostik. Kontrak data atau API latihan **boleh** disepakati bersama KFC-506, tetapi dua MK semester 5 tidak saling menjadi prasyarat tanpa keputusan prodi; sediakan mock mandiri. |

---

## 5. KFC-506 — Sistem Aplikasi Lintas Platform (+P)

### 5.1 Identitas, CPL dan BoK

| Atribut | Isi dan status |
|---|---|
| Identitas [S] | KFC-506; Sistem Aplikasi Lintas Platform (+P); semester 5; 3 SKS; wajib konsentrasi MC pada Tabel 18. |
| Prasyarat / T:P [K] | Belum terverifikasi; usulan FST-102 dan KOM-311 serta diagnostik awal pada bagian 8, bukan aturan prasyarat resmi. Pembagian teori–praktik perlu konfirmasi. |
| CPL [S] | CPL04, rumusan pada bagian 1.1; Tabel 18. |
| BK UWG [S] | **BK02** Algoritma dan Rekayasa Perangkat Lunak pada Tabel 15, sesuai BK utama CPL04 pada Tabel 14. |
| BoK APTIKOM [U] | A05 dan A19 adalah kandidat berdasarkan judul pada 005; bukan pengesahan area atau teknologi tertentu. |

### 5.2 CPMK dan Sub-CPMK [U]

| Kode lokal | CPMK terukur | Bloom | CPL |
|---|---|---|---|
| CPMK04.1 | Mahasiswa mampu **membangun dan menjalankan** aplikasi sederhana dari satu basis kode pada dua target yang disepakati, dengan minimal 4 dari 5 cek Tugas 1 terpenuhi. | C3 | CPL04 |
| CPMK04.2 | Mahasiswa mampu **menerapkan** antarmuka adaptif dan aksesibel dasar pada dua target kasus yang diberikan, dengan minimal 4 dari 5 cek UTS terpenuhi. | C3 | CPL04 |
| CPMK04.3 | Mahasiswa mampu **mengimplementasikan dan menguji** navigasi, state dan penyimpanan lokal pada kasus aplikasi, dengan minimal 4 dari 5 kasus Tugas 2 lulus. | C3 | CPL04 |
| CPMK04.4 | Mahasiswa mampu **mengintegrasikan dan menguji** aplikasi lintas platform sesuai kasus serta mendokumentasikan hasil, dengan minimal 4 dari 5 cek UAS terpenuhi. | C6 | CPL04 |

| Kode lokal | Sub-CPMK operasional | CPMK | Bloom |
|---|---|---|---|
| Sub-CPMK04.1.1 | Menyiapkan proyek dan mengidentifikasi kode bersama serta konfigurasi target. | CPMK04.1 | C3 |
| Sub-CPMK04.1.2 | Menjalankan dan menguji fungsi sederhana pada dua target berbeda. | CPMK04.1 | C3 |
| Sub-CPMK04.2.1 | Menyusun layout adaptif dan komponen sesuai ukuran serta platform. | CPMK04.2 | C3 |
| Sub-CPMK04.2.2 | Menguji label, fokus keyboard dan umpan balik interaksi dasar. | CPMK04.2 | C4 |
| Sub-CPMK04.3.1 | Mengelola state dan navigasi antarhalaman sesuai kasus. | CPMK04.3 | C3 |
| Sub-CPMK04.3.2 | Menyimpan dan memulihkan data lokal serta menangani kegagalan sederhana. | CPMK04.3 | C3 |
| Sub-CPMK04.4.1 | Mengintegrasikan fitur dari satu basis kode dan menjalankannya pada dua target. | CPMK04.4 | C6 |
| Sub-CPMK04.4.2 | Menyusun uji lintas target, mencatat hasil dan keterbatasan serta perbaikan. | CPMK04.4 | C4 |

### 5.3 Rencana 16 pertemuan [U]

A dan E mengikuti skenario bersyarat pada bagian 1.2; PT/BM belum ditetapkan. Dua target harus berbeda runtime/platform, bukan hanya dua ukuran layar. Contoh **browser desktop + emulator Android** atau pasangan lain ditetapkan pengampu setelah memastikan SDK, lisensi, emulator/perangkat dan akses mahasiswa. Framework tidak ditetapkan di sini; gunakan mock lokal agar tidak bergantung pada kelas semester 5 lain.

| Pekan | Sub-CPMK | Topik dan kegiatan | Metode | Waktu | Bukti / asesmen |
|---:|---|---|---|---|---|
| 1 | 04.1.1 | Diagnostik pemrograman; konsep basis kode bersama dan dua target. | Diskusi, demonstrasi | A | Formatif: daftar kebutuhan alat dan kemampuan awal. |
| 2 | 04.1.1 | Menyiapkan proyek dan konfigurasi dua target. | Praktik terbimbing | A | Formatif: proyek awal dan panduan setup. |
| 3 | 04.1.2 | Menjalankan contoh, input sederhana dan perbedaan target. | Demonstrasi, praktik | A | Formatif: hasil berjalan pada kedua target. |
| 4 | 04.1.1, 04.1.2 | Menyerahkan contoh satu basis kode dan demonstrasi dua target. | Praktik, demonstrasi | A | **Tugas 1: 20%, CPMK04.1.** |
| 5 | 04.2.1 | Layout adaptif dan komponen lintas platform. | Kuliah, praktik | A | Formatif: tampilan pada dua target. |
| 6 | 04.2.1 | Adaptasi ukuran, orientasi dan batas kemampuan target. | Praktik, diskusi | A | Formatif: perbandingan hasil dua target. |
| 7 | 04.2.2 | Label, fokus keyboard, umpan balik dan uji aksesibilitas dasar. | Praktik, uji | A | Formatif: daftar cek aksesibilitas. |
| 8 | 04.2.1, 04.2.2 | Evaluasi antarmuka adaptif pada dua target. | Ujian praktik | E | **UTS: 25%, CPMK04.2.** |
| 9 | 04.3.1 | State, perubahan data dan pemutakhiran tampilan. | Demonstrasi, praktik | A | Formatif: state dan perubahan UI. |
| 10 | 04.3.1 | Navigasi antarhalaman dan konsistensi state. | Praktik, uji | A | Formatif: alur dua halaman. |
| 11 | 04.3.2 | Penyimpanan lokal, pemulihan data dan penanganan kesalahan. | Praktik, studi kasus | A | Formatif: uji persistensi dan kegagalan. |
| 12 | 04.3.1, 04.3.2 | Penyelesaian fitur state/navigasi dan data lokal. | Praktik, demonstrasi | A | **Tugas 2: 25%, CPMK04.3.** |
| 13 | 04.4.1 | Rancang kasus proyek dan integrasi fitur satu basis kode. | Studi kasus, praktik | A | Formatif: rancangan dan purwarupa. |
| 14 | 04.4.1 | Adaptasi proyek untuk dua target; mock lokal opsional. | Praktik proyek | A | Formatif: proyek berjalan pada dua target. |
| 15 | 04.4.2 | Uji lintas target, dokumentasi perbedaan dan perbaikan. | Pengujian, umpan balik | A | Formatif: matriks uji dan keterbatasan. |
| 16 | 04.4.1, 04.4.2 | Demonstrasi dua target, hasil uji dan penjelasan individu. | Ujian proyek | E | **UAS: 30%, CPMK04.4.** |

### 5.4 Instrumen utama dan bukti [U]

| Instrumen | CPMK / bobot | Lima butir cek bernilai sama; target usulan ≥4/5 | Bukti minimum |
|---|---|---|---|
| Tugas 1, pekan 4 | 04.1 / 20% | (1) target A berjalan; (2) target B berjalan; (3) aksi sederhana berjalan pada A; (4) aksi sama berjalan pada B; (5) kode bersama dan konfigurasi kedua target dapat ditunjukkan. | Satu proyek, petunjuk menjalankan dan bukti dua target. |
| UTS, pekan 8 | 04.2 / 25% | (1) layout target A terbaca; (2) layout target B terbaca; (3) kontrol memiliki label; (4) fokus/keyboard dasar diuji pada target yang mendukung; (5) interaksi memberi umpan balik yang jelas pada kedua target. | Proyek UI, tangkapan dua target dan daftar hasil uji. |
| Tugas 2, pekan 12 | 04.3 / 25% | (1) state berubah sesuai aksi; (2) navigasi maju/kembali bekerja; (3) data tersimpan lokal; (4) data dipulihkan saat aplikasi dibuka ulang; (5) kegagalan penyimpanan atau data invalid memberi pesan yang dapat dipahami. | Proyek, data dummy, tabel lima uji dan penjelasan individu. |
| UAS, pekan 16 | 04.4 / 30% | (1) basis kode bersama terintegrasi; (2) fitur utama berjalan pada target A; (3) fitur utama berjalan pada target B; (4) hasil uji/perbedaan target dan perbaikan dicatat; (5) petunjuk menjalankan dan demonstrasi tersedia. | Satu proyek, bukti dua target, matriks uji dan demonstrasi individu. |

### 5.5 Boundary guardrails [U]

| Jenis | Batas yang diusulkan — untuk ditinjau, bukan larangan resmi |
|---|---|
| In-scope | Satu basis kode untuk dua target, konfigurasi, UI adaptif, aksesibilitas dasar, navigasi/state, penyimpanan lokal, pengujian dan dokumentasi lintas target. |
| Out-of-scope | Implementasi server CRUD dan autentikasi server bukan fokus utama; gunakan mock yang disediakan atau kontrak data yang disepakati. Pendalaman fitur native spesifik perangkat, distribusi produksi dan operasi infrastruktur bukan target wajib rancangan awal ini. |
| Handoff | Fondasi pemrograman diperiksa melalui diagnostik; kontrak/mock dari KOM-526 hanya jika disepakati, tanpa ketergantungan jadwal resmi. Artefak dan temuan lintas target dapat menjadi masukan bagi **KFC-601 Sistem Aplikasi Mobile**, setelah koordinasi dan tanpa menganggapnya prasyarat formal. |

---

## 6. Matriks keterlacakan asesmen usulan

Kode CPMK pada setiap baris merujuk ke MK di kolom pertama. Nilai dalam tabel adalah **bobot instrumen terhadap nilai akhir MK**, bukan persentase ketercapaian CPL.

| MK | CPMK04.1 / T1 pekan 4 | CPMK04.2 / UTS pekan 8 | CPMK04.3 / T2 pekan 12 | CPMK04.4 / UAS pekan 16 | Total |
|---|---:|---:|---:|---:|---:|
| KOM-312 | 20% | 25% | 25% | 30% | 100% |
| KOM-526 | 20% | 25% | 25% | 30% | 100% |
| KFC-506 | 20% | 25% | 25% | 30% | 100% |

Setiap instrumen berisi lima butir minimum yang dinyatakan pada bagian MK masing-masing, masing-masing 20% dari skor instrumen. Target 4/5 adalah **rencana demonstrasi**; keputusan ketuntasan, teknik sampling, rubrik lebih rinci dan agregasi CPL tetap menunggu ketentuan prodi. Formatif dan diagnostik tidak menambah bobot sumatif. Bukti hasil individu tetap diperlukan untuk kerja kelompok.

## 7. Daftar validasi sebelum penetapan

| No. | Pertanyaan / keputusan yang diperlukan | Status |
|---:|---|---|
| 1 | Peroleh RPS/workbook dan CPMK/Sub-CPMK yang berlaku untuk ketiga MK; bandingkan dengan usulan dan putuskan penerimaan/perubahan. | Belum tersedia / [K] |
| 2 | Konfirmasi kode, 3 SKS, semester, tipe `+P`, status MC dan terutama prasyarat serta pembagian teori/praktik. | Identitas Tabel 18 tersedia [S]; rincian lain [K] |
| 3 | Tentukan durasi TM, praktik, PT dan BM, serta slot ujian untuk setiap MK; sesuaikan A/E dan periksa beban total. | Belum ditetapkan / [K] |
| 4 | Rekonsiliasi Tabel 14/15/16/18 dan pemeriksaan Tabel 19; khusus KOM-526 tentukan relevansi BK03–BK08 dan apakah pembebanan CPL perlu keputusan tersendiri. | [K]; tidak mengubah data sumber |
| 5 | Koordinasikan KOM-312, KOM-526, KFC-506, serta pengampu MK terkait seperti KOM-524/KFC-601; tetapkan overlap yang sengaja berjenjang, handoff dan prasyarat formal. | Usulan [U], perlu [K] |
| 6 | Tetapkan pilihan stack, SDK/emulator, dua target, fasilitas, aksesibilitas, sumber daya dan data dummy; sesuaikan materi/asesmen jika fasilitas tidak tersedia. | Belum ditetapkan / [K] |
| 7 | Tinjau target 4/5, bobot, kasus uji, bukti individu, rubrik dan waktu evaluasi; tetapkan aturan penilaian dan agregasi capaian. | Usulan [U], perlu [K] |
| 8 | Validasi rencana mingguan, CPL–CPMK–Sub-CPMK–BK–asesmen, sumber dan batas materi oleh pengampu, RMK, prodi dan penjaminan mutu. | Belum disahkan |

Tidak ada perubahan kurikulum, prasyarat atau pengesahan yang ditetapkan oleh dokumen rancangan ini.

---

## 8. Usulan prasyarat dan diagnostik awal

### 8.1 Status dan usulan untuk keputusan prodi

**[K] Prasyarat akademik resmi untuk ketiga MK belum ditemukan/terverifikasi pada sumber yang diperiksa.** Pembacaan teks XML tubuh buku KPT menemukan ketentuan umum tentang prasyarat, tetapi tidak menemukan daftar per-MK pada bagian itu. Ini tidak membuktikan tidak adanya ketentuan lain di SIAKAD, peraturan prodi, workbook, gambar atau RPS yang belum diperiksa. Jangan menulis usulan berikut sebagai syarat KRS atau syarat kelulusan sebelum ada keputusan prodi.

| MK tujuan | Usulan MK prasyarat [U] | Dasar pemilihan dan kemampuan awal yang perlu dibuktikan [U] | Status resmi [K] |
|---|---|---|---|
| KOM-312 | **FST-102 Algoritma dan Pemrograman (+P)** | FST-102 tercantum di semester 1; variabel, percabangan, fungsi dan penelusuran kesalahan menunjang JavaScript semester 3. | Belum terverifikasi. |
| KOM-526 | **KOM-312 Pemrograman Web (+P) dan FST-207 Basis Data (+P)** | KOM-312 di semester 3 dan FST-207 di semester 2; HTML/formulir, alur web, entitas dan operasi data menunjang aplikasi server–database semester 5. | Belum terverifikasi. |
| KFC-506 | **FST-102 Algoritma dan Pemrograman (+P) dan KOM-311 Pemrograman Berorientasi Objek (+P)** | FST-102 di semester 1 dan KOM-311 di semester 3; fungsi, kondisi, struktur objek dan debugging menunjang komponen serta state semester 5. | Belum terverifikasi. |

Usulan di atas adalah **kombinasi “dan”**, bukan pilihan salah satu. Kondisi nilai minimum, ekivalensi, pengecualian dan dampak KRS perlu diputuskan prodi. **KOM-312 adalah bekal yang dianjurkan**, bukan tambahan syarat usulan KFC-506. KOM-526 dan KFC-506 sama-sama semester 5, sehingga **tidak saling dijadikan prasyarat**; kebutuhan data KFC-506 disediakan dengan mock mandiri. Kode, nama dan semester calon MK merujuk [004 Tabel 18](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md), sedangkan penetapan hubungan adalah usulan baru.

### 8.2 Diagnostik dan tindak lanjut [U]

Diagnostik tidak berbobot, tidak menentukan izin KRS, dan tidak menggantikan ketetapan prasyarat. Siapkan tiga butir berikut untuk minggu 1, maksimal **40 menit di dalam waktu A**, bukan beban tambahan. Setiap butir dicatat **terpenuhi / perlu penguatan** berdasarkan demonstrasi individu; mahasiswa menerima umpan balik. Ambang ini bukan ketuntasan resmi.

| MK | Tiga tugas diagnostik | Bukti dan tindak lanjut jika perlu penguatan |
|---|---|---|
| KOM-312 | (1) Jelaskan variabel dan tipe data pada contoh; (2) buat kondisi untuk menolak nilai kosong; (3) tulis fungsi sederhana dan telusuri satu kesalahan. | Berkas/jawaban dan penjelasan; latihan pengayaan fungsi dan kondisi dengan umpan balik sebelum minggu 9. |
| KOM-526 | (1) Jelaskan peran formulir klien dan respons server; (2) buat model dua entitas dan relasi sederhana; (3) jelaskan operasi tambah dan baca data beserta contoh input. | Sketsa dan penjelasan; pengayaan HTML/HTTP, entitas dan CRUD menggunakan data dummy sebelum minggu 5–6. |
| KFC-506 | (1) Buat fungsi dan percabangan; (2) jelaskan objek, atribut dan pemanggilan metode sederhana; (3) telusuri perubahan nilai sebuah state pada contoh. | Kode/jawaban dan penjelasan; pengayaan pemrograman/objek serta latihan setup sebelum minggu 4. |

Pengampu menyediakan materi alternatif yang dapat diakses, memberi kesempatan konsultasi, lalu mencatat perbaikan. Durasi pengayaan di luar sesi dan aturan tindak lanjut menunggu kebijakan PT/BM prodi; tidak secara otomatis menambah nilai atau menghalangi KRS.

## 9. Paket dasar RPS dan otorisasi

### 9.1 Identitas dan status bersama

| Bidang RPS | Data yang dapat diisi sekarang | Data yang masih perlu ditetapkan [K] |
|---|---|---|
| Institusi | Universitas Widyagama Malang; Program Studi S1 Teknik Informatika [S]. | Nama fakultas yang digunakan pada RPS resmi dan nomor/kode dokumen. |
| MK, semester, total SKS, tipe | Lihat bagian 2 dan identitas tiap MK [S]. | Pembagian teori–praktik, rincian waktu PT/BM, kelas dan tahun ajaran. |
| Prasyarat | **Belum terverifikasi**; usulan terpisah pada bagian 8 [U]. | Keputusan resmi, nilai minimum dan ekivalensi bila ada. |
| CPL, BK, CPMK/Sub-CPMK | CPL/BK dari buku KPT; rumusan CPMK/Sub-CPMK sebagai rancangan bagian 3–5. | Konfirmasi RPS/workbook, CPL, BK, rumusan, kode dan bukti ketercapaian. |
| Otorisasi | Status draf. | Nama/NIDN atau NUPTK pengembang, dosen pengampu, koordinator RMK, ketua prodi, pejabat penjaminan mutu, tanggal penyusunan dan pengesahan. Jangan mengarang nama, nomor atau tanda tangan. |
| Asesmen dan kelulusan | Rancangan empat instrumen dan bobot pada bagian 3–6. | Persetujuan bentuk, bobot, target, kebijakan kelas, remedial dan agregasi CPL. |

### 9.2 Deskripsi singkat dan bahan kajian usulan per MK

**KOM-312 [U].** Mata kuliah membangun dasar antarmuka web melalui HTML semantik, konten dan formulir, CSS/Flexbox responsif, JavaScript dasar serta DOM/event. Mahasiswa menyelesaikan halaman lokal, menguji navigasi, responsivitas dan interaksi, serta mendokumentasikan perbaikannya. Kegiatan berupa demonstrasi, latihan dan proyek sesuai bagian 3; validasi klien tidak menggantikan validasi server. **Bahan kajian:** struktur/semantik HTML; konten, tabel, formulir; CSS dan responsivitas; logika JavaScript dan DOM; integrasi dan pengujian halaman.

**KOM-526 [U].** Mata kuliah melatih perancangan dan pengembangan sistem aplikasi web berbasis kasus melalui kebutuhan, model data, rute server, CRUD, autentikasi dan pembatasan akses dasar, validasi server, integrasi, uji dan dokumentasi. Proyek memakai data dummy dan berjalan lokal; latihan keamanan dasar bukan jaminan siap produksi. **Bahan kajian:** kebutuhan dan alur; model entitas/relasi; HTTP, rute dan server; penyimpanan data dan CRUD; sesi/akses dan validasi; integrasi dan pengujian. Penetapan rincian BK tambahan tetap mengikuti proses validasi bagian 4.1.

**KFC-506 [U].** Mata kuliah melatih pembangunan satu basis kode untuk dua target platform berbeda melalui konfigurasi, antarmuka adaptif, aksesibilitas dasar, navigasi, state, penyimpanan lokal serta uji lintas target. Pasangan target, framework dan sumber daya dipilih pengampu; mock lokal disediakan agar tidak bergantung pada MK lain. **Bahan kajian:** konsep lintas platform dan setup; layout adaptif; navigasi/state; persistensi lokal; integrasi, pengujian dan keterbatasan platform.

### 9.3 Bentuk pembelajaran, moda dan fasilitas [U]

- **Luring:** teori/demonstrasi dan diskusi diikuti praktikum terbimbing; gunakan kegiatan, bukti dan waktu A/E pada tabel pertemuan tiap MK. Formatif dinilai melalui observasi/checklist dan umpan balik, tanpa bobot sumatif tambahan.
- **Daring jika disetujui:** alternatif setara berupa demonstrasi dan diskusi jarak jauh, praktik terbimbing/mandiri, serta unggah kode dan hasil uji melalui media yang diputuskan prodi. Bukan pertemuan atau beban ekstra. Evaluasi daring hanya jika mekanisme integritas, akses dan jadwal disetujui; sediakan cara setara bagi mahasiswa dengan kendala akses.
- **PT/BM:** isi berupa latihan, dokumentasi hasil dan membaca pustaka terkait; durasi dan pengaturannya **belum ditetapkan**, sehingga tidak dimasukkan ke 270 menit A dan tidak diklaim sebagai beban final.
- **KOM-312:** komputer, editor teks dan browser dengan alat pengembang; aset berizin atau dummy. Praktik dasar dapat berjalan lokal.
- **KOM-526:** editor, runtime/framework dan sistem basis data yang dipilih pengampu, server dan dataset dummy di lingkungan lokal/terisolasi; akses laboratorium dan lisensi diverifikasi. Kata sandi latihan tidak digunakan ulang; gunakan pustaka hashing yang sesuai dan jangan menyimpan data pribadi nyata.
- **KFC-506:** editor, SDK, perangkat/emulator dan dua target berbeda yang didukung satu basis kode. Siapkan perangkat bersama atau akses lab jika komputer mahasiswa tidak mampu menjalankan emulator; cek SDK, lisensi, aksesibilitas, kapasitas dan kebutuhan internet sebelum mengunci target. Jika framework berbeda dari contoh Flutter, ganti pustakanya dengan dokumentasi setara dan pertahankan dua target.
- **Integritas dan akses:** aset harus berizin; dokumentasikan penggunaan bantuan/kolaborasi sesuai aturan pengampu. Bila kelompok, nilai bukti individu; jangan mewajibkan unggahan publik berisi kredensial, data pribadi atau rahasia.

### 9.4 Teknik, rubrik minimum, dan tindak lanjut [U]

Tabel instrumen 3.4, 4.4, 5.4 adalah **kisi-kisi dan rubrik checklist analitik minimum**: lima butir masing-masing berbobot **20% dari skor instrumen**, bukan tambahan ke bobot MK. Untuk **setiap butir** pengampu menyiapkan kondisi, data/input, tindakan, hasil yang diharapkan dan kriteria sebagai berikut:

| Status butir | Skor butir usulan | Deskriptor |
|---|---:|---|
| Terpenuhi | 100 | Semua komponen butir terpenuhi dan bukti hasil aktual dapat diverifikasi; jika butir memuat beberapa komponen, semuanya harus terpenuhi. |
| Belum terpenuhi | 0 | Satu atau lebih komponen butir gagal/tidak ditunjukkan, atau bukti tidak dapat diverifikasi. |

Skor instrumen = jumlah lima skor butir × 20%. **Target usulan CPMK ≥4 butir terpenuhi dari 5**; target ini sama dengan skor checklist ≥80/100 bila lima bobot sama, tetapi bukan ambang resmi prodi. Rekap instrumen ke nilai akhir memakai bobot di bagian 6 **satu kali**. Jika prodi memilih rubrik bertingkat/parsial, rubrik dan definisi ketercapaian CPMK harus dirumuskan ulang bersama, tidak diam-diam disamakan dengan aturan biner ini.

Pengampu menyimpan daftar cek, kondisi uji, hasil, penjelasan individu, umpan balik dan perbaikan. Rekap CPMK per kelas dan identifikasi kesulitan dipakai untuk rencana **CQI** semester berikutnya; remedial, ambang dan agregasi ke CPL lintas MK mengikuti keputusan prodi. Penetapan indikator keberhasilan program atau klaim capaian tidak dilakukan tanpa data pelaksanaan.

### 9.5 Contoh instruksi instrumen sumatif [U]

Instruksi berikut melengkapi lima butir dan bukti pada tabel 3.4/4.4/5.4; lima butir tersebut tetap menjadi satu-satunya kriteria checklist usulan. Durasi, pengumpulan, kasus final dan aturan alat ditetapkan pengampu. Semua pekerjaan memakai data dummy/berizin. Varian teknis dan skenario lima cek KOM-526 dijabarkan pada [bagian 13](#13-empat-varian-implementasi-kom-526-u).

| MK | Instrumen | Instruksi pokok dan keluaran |
|---|---|---|
| KOM-312 | Tugas 1 | Buat halaman informasi HTML untuk kasus yang disediakan; sertakan konten, navigasi, tabel dan formulir. Serahkan HTML, aset dan daftar cek; CSS tidak dinilai. |
| KOM-312 | UTS | Terapkan CSS/Flexbox dan media query pada HTML yang disediakan; tampilkan dua lebar layar. Serahkan berkas dan tangkapan yang mendukung lima cek 3.4. |
| KOM-312 | Tugas 2 | Buat formulir interaktif dengan JavaScript untuk input valid, kosong dan tidak valid, aksi dan reset. Sertakan lima hasil uji dan jelaskan kode. |
| KOM-312 | UAS | Bangun halaman responsif interaktif dari kasus yang disepakati; serahkan proyek lokal, petunjuk, hasil uji/perbaikan dan demonstrasi individu. |
| KOM-526 | Tugas 1 | Rancang kebutuhan dan model data untuk kasus sistem yang disediakan; serahkan aktor, kebutuhan, alur, entitas/relasi dan keterlacakan rancangan. |
| KOM-526 | UTS | Implementasikan rute server dan CRUD pada database dummy; perlihatkan empat operasi serta penanganan data yang tidak ditemukan, disertai lima uji. |
| KOM-526 | Tugas 2 | Terapkan login, logout, sesi/peran dan validasi server pada aplikasi latihan; gunakan kueri terparameter, data dummy, matriks peran dan lima uji. |
| KOM-526 | UAS | Integrasikan antarmuka, server, data dan akses sesuai rancangan; serahkan aplikasi lokal, petunjuk, uji alur normal/gagal dan demonstrasi individu. |
| KFC-506 | Tugas 1 | Siapkan satu proyek dengan aksi sederhana pada dua target yang disepakati; serahkan kode bersama, konfigurasi dan bukti berjalan pada masing-masing target. |
| KFC-506 | UTS | Buat UI adaptif pada dua target dan buktikan label, fokus/keyboard pada target yang mendukung, serta umpan balik interaksi sesuai lima cek. |
| KFC-506 | Tugas 2 | Bangun navigasi, state dan penyimpanan lokal dengan penanganan data invalid/kegagalan; serahkan proyek dan lima uji, termasuk pemulihan setelah aplikasi dibuka ulang. |
| KFC-506 | UAS | Integrasikan aplikasi satu basis kode pada dua target; serahkan proyek, petunjuk, hasil uji lintas target, keterbatasan, perbaikan dan demonstrasi individu. |

## 10. Pustaka dasar untuk penyusunan RPS [U]

Nomor berikut **usulan penyusun**, bukan daftar pustaka resmi prodi. Pengelompokan utama/pendukung di bawah dimaksudkan untuk format RPS; dosen memverifikasi kelayakan, ketersediaan, versi/akses dan dokumen setara yang sesuai stack terpilih. Dokumentasi daring dapat berubah; tidak diklaim sebagai buku cetak ber-ISBN.

| Nomor | Sumber resmi dan topik | Kelompok usulan |
|---|---|---|
| R1 | MDN, [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) — struktur, konten dan formulir. | Utama KOM-312 |
| R2 | MDN, [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) — layout, Flexbox dan responsivitas. | Utama KOM-312 |
| R3 | MDN, [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) — fungsi, kontrol alur dan bahasa. | Utama KOM-312 |
| R4 | MDN, [Introduction to the server side](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction) — interaksi klien, server dan data. | Utama KOM-526 |
| R5 | [SQLite Documentation](https://www.sqlite.org/docs.html) — contoh basis data lokal dan referensi SQL; pengampu dapat mengganti sesuai DB yang dipilih. | Pendukung KOM-526 |
| R6 | OWASP, [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) dan [SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — autentikasi dan parameterisasi. | Pendukung KOM-526 |
| R7 | Flutter, [Adaptive and responsive design](https://docs.flutter.dev/ui/adaptive-responsive) dan [Web support](https://docs.flutter.dev/platform-integration/web) — contoh satu framework dengan target berbeda. | Contoh utama KFC-506 jika Flutter dipilih |
| R8 | Flutter, [Navigation basics](https://docs.flutter.dev/cookbook/navigation/navigation-basics) dan [Store key-value data on disk](https://docs.flutter.dev/cookbook/persistence/key-value) — contoh navigasi dan penyimpanan lokal. | Contoh pendukung KFC-506 jika Flutter dipilih |
| R9 | MDN, [Accessibility on the web](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) — label dan interaksi keyboard pada konten web. | Pendukung KOM-312; konsep umum untuk KFC-506 |

R7/R8 hanyalah contoh, **tidak mewajibkan Flutter**. Dokumentasi R8 mencatat keterbatasan penyimpanan key-value, termasuk tidak menjamin persistensi di semua keadaan; untuk uji buka ulang pilih implementasi yang cocok pada kedua target, jelaskan keterbatasannya, dan jangan simpan informasi sensitif. Pengampu menyediakan bahan offline/alternatif yang sah bila akses daring atau SDK terbatas.

## 11. Indikator mingguan dan rujukan RPS [U]

Bagian ini **melengkapi**, bukan mengganti, tabel 16 minggu pada bagian 3.3/4.3/5.3. Pada setiap minggu gunakan Sub-CPMK, topik, metode, waktu A/E dan bukti/bobot dari tabel MK yang bersangkutan; kolom di bawah memasok indikator dan nomor pustaka untuk tabel RPS delapan kolom. Teknik: **formatif** = observasi/checklist hasil praktik dan umpan balik; **T1/UTS/T2/UAS** = unjuk kerja/dokumen serta checklist pada bagian 9.4–9.5. Moda luring/daring dan batas waktu mengikuti 9.3 dan 1.2.

### 11.1 KOM-312

| Minggu | Indikator yang diamati | Pustaka |
|---:|---|---|
| 1 | Struktur dasar dokumen dan hierarki heading tampak pada halaman profil. | R1 |
| 2 | Elemen semantik, tautan dan gambar dengan alt berfungsi sesuai kasus. | R1, R9 |
| 3 | Tabel memiliki header dan label terhubung ke input; validasi HTML diuji. | R1 |
| 4 | Lima butir HTML Tugas 1 dapat diperiksa; CSS tidak dinilai pada T1. | R1, R2 |
| 5 | Selektor dan box model menghasilkan kartu sesuai spesifikasi. | R2 |
| 6 | Pengaturan container/item Flexbox menghasilkan navigasi dan kartu fleksibel. | R2 |
| 7 | Layout terbaca dan overflow utama diuji pada dua lebar. | R2 |
| 8 | Lima cek UTS CSS, Flexbox dan dua lebar dapat dibuktikan. | R2 |
| 9 | Fungsi menggunakan variabel dan operator menghasilkan nilai sesuai contoh. | R3 |
| 10 | Fungsi membedakan masukan valid, kosong dan tidak valid. | R3 |
| 11 | Event membaca input dan memperbarui elemen keluaran DOM. | R3 |
| 12 | Lima kasus interaksi dan validasi Tugas 2 dijalankan dan dicatat. | R1, R3 |
| 13 | Sketsa, konten berizin dan kerangka HTML sesuai kasus. | R1, R9 |
| 14 | HTML, CSS dan JavaScript terhubung pada purwarupa. | R1, R2, R3 |
| 15 | Hasil uji navigasi, interaksi, keyboard dan dua lebar mencatat perbaikan. | R2, R3, R9 |
| 16 | Lima cek integrasi, fungsi dan dokumentasi UAS dibuktikan. | R1, R2, R3, R9 |

### 11.2 KOM-526

Indikator bersama di bawah digunakan bersama rincian teknis dan rujukan pilihan varian pada [bagian 13](#13-empat-varian-implementasi-kom-526-u).

| Minggu | Indikator yang diamati | Pustaka |
|---:|---|---|
| 1 | Aktor dan alur klien–server awal dijelaskan untuk kasus dummy. | R4 |
| 2 | Kebutuhan dan peran dituliskan dengan kondisi penerimaan yang dapat diuji. | R4 |
| 3 | Entitas, relasi dan contoh data konsisten dengan kebutuhan. | R5 |
| 4 | Lima cek rancangan Tugas 1 tersedia; pengantar rute tidak dinilai pada T1. | R4, R5 |
| 5 | Rute menerima permintaan dan memberi respons sesuai kasus. | R4 |
| 6 | Data dummy dapat dibuat dan dibaca melalui server dan database. | R4, R5 |
| 7 | Update/delete serta kondisi data tidak ditemukan diuji. | R4, R5 |
| 8 | Lima kasus CRUD dan data tidak ditemukan pada UTS dibuktikan. | R4, R5 |
| 9 | Login valid/tidak valid dan logout dapat didemonstrasikan. | R6 |
| 10 | Peran yang tidak berwenang ditolak mengakses fitur terbatas. | R6 |
| 11 | Input invalid ditolak server dan kueri menggunakan parameter. | R5, R6 |
| 12 | Lima cek autentikasi, akses dan validasi Tugas 2 dibuktikan. | R5, R6 |
| 13 | Antarmuka, rute, data dan akses terhubung pada purwarupa. | R4, R5, R6 |
| 14 | Alur end-to-end menggunakan data dummy sesuai kebutuhan. | R4, R5 |
| 15 | Uji alur normal/gagal dan perbaikan dicatat dengan hasil aktual. | R4, R6 |
| 16 | Lima cek integrasi, akses, data dan dokumentasi UAS dibuktikan. | R4, R5, R6 |

### 11.3 KFC-506

R7/R8 berlaku sebagai **contoh hanya jika Flutter dipilih**; jika stack berbeda, pengampu memilih dokumen setara sebelum RPS ditetapkan.

| Minggu | Indikator yang diamati | Pustaka |
|---:|---|---|
| 1 | Mahasiswa menjelaskan satu basis kode dan dua target yang direncanakan. | R7 |
| 2 | Proyek dan konfigurasi untuk dua target dapat disiapkan. | R7 |
| 3 | Aksi sederhana dijalankan pada kedua target. | R7 |
| 4 | Lima cek basis kode/aksi pada dua target Tugas 1 dibuktikan. | R7 |
| 5 | Layout dan komponen menyesuaikan target yang disepakati. | R7 |
| 6 | Perbedaan ukuran/kemampuan target dicatat bersama hasil uji layout. | R7 |
| 7 | Label, fokus dan umpan balik dasar diuji sesuai kemampuan target. | R7, R9 |
| 8 | Lima cek UI adaptif dan aksesibilitas dasar UTS dibuktikan. | R7, R9 |
| 9 | Aksi mengubah state dan tampilan sesuai contoh. | R8 |
| 10 | Navigasi maju/kembali mempertahankan state sesuai kasus. | R8 |
| 11 | Data lokal dipulihkan pada kondisi yang diuji dan kesalahan ditangani. | R8 |
| 12 | Lima kasus state, navigasi dan persistensi Tugas 2 dicatat. | R8 |
| 13 | Rancangan proyek menunjukkan kasus dan fitur bersama. | R7, R8 |
| 14 | Fitur terintegrasi berjalan pada dua target berbeda. | R7, R8 |
| 15 | Matriks hasil uji, perbedaan target dan perbaikan tersedia. | R7, R8 |
| 16 | Lima cek integrasi lintas target dan dokumentasi UAS dibuktikan. | R7, R8 |

## 12. Daftar kesiapan pengisian template RPS

Gunakan struktur [template SWO](../KURIKULUM2026_REVISI/Template_RPS_GEN_2026_20092026-SWO.docx) dan [analisis format 052](../KURIKULUM2026_REVISI/052_ANALISIS_FORMAT_DAN_LAYOUT_TEMPLATE_RPS_OBE.md) sebagai rujukan format, bukan untuk menyalin identitas atau kebijakan SISTEKIN.

| Komponen | Bahan dari 010 | Tindak lanjut |
|---|---|---|
| Sampul, identitas, otorisasi dan pengesahan | Identitas masing-masing MK pada 3.1/4.1/5.1; bidang belum diketahui pada 9.1. | Isi pejabat, NIDN/NUPTK, tanggal, nomor, rumpun dan penandatangan setelah ditetapkan. |
| CPL, CPMK, Sub-CPMK, korelasi | CPL04 bagian 1.1 dan tabel capaian tiap MK; semua CPMK usulan ditautkan ke CPL04. | Cocokkan rumusan dengan RPS/workbook serta keputusan prodi; jangan menganggap pemetaan tambahan disahkan. |
| Deskripsi, bahan kajian dan pustaka | Bagian 9.2 dan 10, serta BK UWG di tiap identitas MK. | Pilih pustaka per MK dan stack, verifikasi versi dan klasifikasi utama/pendukung. |
| Tabel 16 minggu, delapan kolom | Rencana 3.3/4.3/5.3, indikator/pustaka 11.1–11.3, teknik dan moda 9.3–9.4, bobot bagian 6. | Satukan kolom dalam template; tetapkan pembagian T/P, durasi PT/BM, moda dan waktu ujian terlebih dahulu. |
| Empat soal dan rubrik | Kisi-kisi lima butir pada 3.4/4.4/5.4 serta instruksi dan rubrik minimum 9.4–9.5. | Kembangkan naskah soal lengkap, contoh data, lembar penilaian dan rubrik yang disetujui; uji kelayakan waktu. |
| CQI dan rekam capaian | Alur tindak lanjut 9.4. | Tetapkan ambang, formulir, penanggung jawab, remedial, kebijakan rekam bukti dan pelaporan. |

**Belum siap disahkan:** prasyarat resmi, identitas pejabat/otorisasi, tahun ajaran, komposisi SKS dan semua durasi, stack dan fasilitas, CPMK resmi, kelengkapan instrumen serta kebijakan penilaian masih memerlukan konfirmasi dan, jika diperlukan, keputusan pengampu/RMK/prodi. Dokumen 010 ini adalah bahan penyusunan RPS, bukan RPS final atau bukti pelaksanaan.

---

## 13. Empat varian implementasi KOM-526 [U]

### 13.1 Aturan bersama dan batas kesetaraan

**KOM-526a, KOM-526b, KOM-526c dan KOM-526d** adalah label usulan untuk empat jalur alternatif di dalam **satu mata kuliah resmi KOM-526**; sufiks a–d bukan kode kurikulum/KRS resmi yang telah ditemukan atau disahkan. Mahasiswa memilih **satu** jalur sesuai kesiapan dan minat, bila prodi menyetujui pembukaan/penempatan, pengampu, fasilitas dan pencatatan akademiknya. Semua jalur, urutan belajar dan RPS-nya masih rancangan, bukan empat MK baru atau kewajiban mengambilnya secara berurutan.

Seluruh varian menggunakan identitas semester 5/3 SKS/+P dan CPL04 dari 4.1; BK Tabel 15, catatan ketidaksesuaian Tabel 14/16/18, usulan prasyarat pada 8, kerangka empat CPMK dan delapan Sub-CPMK pada 4.2, redaksi spesifik tiap jalur pada 13.1B, serta batas 4.5 tetap berlaku. Waktu **A/E** tetap mengikuti asumsi bersyarat 1.2; pembagian T/P dan PT/BM belum ditetapkan. Minggu, kode capaian, waktu dan bobot mengikuti 4.3/4.4; tabel masing-masing jalur di bawah merinci teknik, bukti dan metode. Metode jalur d disesuaikan menjadi mandiri terarah dengan bimbingan dosen, bukan menambah pertemuan.

| Aspek | KOM-526a PHP Native | KOM-526b PHP OOP | KOM-526c PHP Laravel | KOM-526d Python Web Flask |
|---|---|---|---|---|
| Gaya implementasi [U] | PHP prosedural tanpa framework aplikasi; fungsi/file terstruktur, PDO untuk data. Objek PDO bawaan tidak mengubah fokus prosedural. | PHP berbasis kelas tanpa framework aplikasi; pisahkan controller, service/repository dan view sederhana dengan PDO. | Laravel, rute, controller, Blade, validasi, Eloquent/migration dan fasilitas autentikasi/otorisasi framework. | Python, Flask, rute/view function dan Jinja; `sqlite3` sebagai contoh penyimpanan dan Flask-WTF untuk CSRF. |
| Fokus pembeda [U] | Memahami alur request, validasi dan operasi data secara langsung. | Menerapkan enkapsulasi, pembagian tanggung jawab dan pengujian kelas. | Memanfaatkan konvensi dan komponen framework PHP, serta menjelaskan kode yang digunakan. | Menerapkan framework mikro Python dan pemisahan rute, template, data dan akses. |
| Fondasi tambahan yang didiagnosis [U] | Sintaks dasar PHP. | Sintaks PHP serta kelas, objek dan metode. | Sintaks PHP, kelas/objek dan dasar Composer. | Sintaks Python, fungsi, struktur data dan lingkungan virtual. |

Fondasi bahasa adalah **materi diagnostik/penguatan**, bukan prasyarat akademik formal baru. KOM-311 Pemrograman Berorientasi Objek bermanfaat terutama untuk KOM-526b dan KOM-526c, tetapi tidak ditambahkan sebagai prasyarat formal maupun syarat KRS. Diagnostik minggu 1 bagian 8.2 tetap digunakan; pemeriksaan bahasa dilakukan di dalam alokasi yang sama. Pengampu menyiapkan pengayaan sebelum minggu 5 jika diperlukan. Tidak diasumsikan bahwa seluruh mahasiswa sudah menguasai PHP, OOP, Laravel, Python atau Flask.

**Rumusan CPMK per jalur:** kerangka capaian dan target 4/5 pada 4.2 menjadi dasar; redaksi operasional, Sub-CPMK dan bahan kajian yang berbeda untuk masing-masing jalur dirumuskan di 13.1B–13.1C. CPMK04.1 tetap rancangan kebutuhan/model data, bukan tes bahasa. Misalnya, rute pada KOM-526a dapat berupa endpoint berkas PHP; tidak mewajibkan router framework. Semua jalur membuktikan capaian inti yang sebanding meskipun fokus dan struktur kodenya berbeda.

### 13.1A Inti RPS dan pemilihan jalur [U]

| Label rancangan / topik | Sasaran peserta dan fokus | Strategi belajar |
|---|---|---|
| **KOM-526a — Jalur 1: PHP Native** | Jalur paling dasar bagi mahasiswa yang mulai belajar sistem aplikasi web. Memahami request–response, form, logika prosedural dan hubungan langsung PHP–database sebelum abstraksi framework. | Praktik bertahap dan demonstrasi terbimbing; kode prosedural tanpa framework aplikasi. |
| **KOM-526b — Jalur 2: PHP OOP** | Pilihan setelah mahasiswa pernah mempelajari/menguasai dasar jalur 1, baik dari jalur tersebut maupun pengalaman setara; pendalaman kelas, enkapsulasi dan pemisahan tanggung jawab. | Praktik perancangan kelas dan refactoring menuju controller/service/repository; tanpa framework aplikasi. |
| **KOM-526c — Jalur 3: PHP Laravel** | Pilihan alternatif setelah mahasiswa pernah mempelajari/menguasai dasar jalur 1 atau pengalaman setara; membangun aplikasi dengan konvensi dan layanan framework. | Praktik route, controller, Blade, migration/Eloquent dan otorisasi framework; bukan lanjutan wajib dari jalur 2. |
| **KOM-526d — Jalur 4: Python Web Flask** | Pilihan khusus bagi mahasiswa yang benar-benar ingin meningkatkan keterampilan secara mandiri dan siap mendalami Python serta Flask. Bukan label kemampuan bawaan atau keistimewaan administratif. | Pembelajaran mandiri terarah, studi dokumentasi resmi, eksperimen dan proyek dengan checkpoint serta bimbingan dosen. |

**Alur yang diusulkan:** pemula → **a**; mahasiswa yang sudah belajar dasar a atau kompetensi setaranya → dapat memilih **b atau c**, tidak harus keduanya dan b bukan prasyarat c. Untuk **d**, mahasiswa mengajukan minat belajar mandiri dan menunjukkan kesiapan dasar Python/web atau menyepakati pengayaan; tidak diwajibkan terlebih dahulu mengambil b/c. Pengalaman setara dapat berasal dari mata kuliah, kursus, proyek atau belajar mandiri, **bukan hanya pernah tercatat mengambil KOM-526a**. Karena keempat label masih berada di bawah satu MK KOM-526, penyelesaian a tidak otomatis membuka KRS ulang untuk b/c: pengakuan, pengambilan ulang/kredit, perpindahan jalur, kelas paralel dan pencatatan akademik harus diputuskan prodi. Jalur lanjutan juga dapat dipilih sejak awal oleh mahasiswa yang telah menguasai dasar secara setara.

**Diagnostik dan penempatan [U]:** sebelum atau pada minggu 1, dosen memeriksa konsep request/response, form, alur prosedural PHP dan CRUD database dengan contoh kecil serta penjelasan mandiri mahasiswa. Untuk b tambahkan pemeriksaan kelas/objek PHP; untuk c dasar PHP/OOP dan penggunaan Composer; untuk d dasar Python, fungsi, lingkungan virtual, motivasi, dan rencana belajar mandiri. Portofolio/proyek boleh menjadi bukti pelengkap. Dosen memberi umpan balik dan rekomendasi: masuk a untuk yang butuh fondasi; b/c untuk yang dasar a-nya memadai; d untuk yang berminat dan siap dengan dukungan yang disepakati. Jika ada kesenjangan, tawarkan materi pengayaan dan diagnostik ulang atau jalur a; bila berpindah kelas, mekanisme dan tenggat mengikuti persetujuan prodi. **Ini mekanisme bimbingan usulan, bukan seleksi resmi atau nilai sumatif**, dan tidak mengubah prasyarat KRS pada bagian 8. Jangan menolak berdasarkan label “spesial” atau kepemilikan perangkat pribadi; dukungan akses lab dan kesempatan konsultasi harus setara.

**Pelaksanaan d yang terarah:** pada minggu 1 mahasiswa menyepakati rencana belajar per pekan, sumber R12, target hasil dan waktu konsultasi dengan dosen. Mahasiswa membawa log ringkas berisi sumber, percobaan, hasil dan hambatan; dosen memeriksa kemajuan pada pertemuan mingguan, memberi umpan balik dan membantu pemulihan saat terhambat. Checkpoint minggu 4/8/12/16 tetap instrumen bersama, bukan nilai tambahan untuk log atau kecepatan. Fasilitas, bahan yang dapat diakses dan waktu bimbingan disediakan; pembelajaran mandiri tidak berarti tanpa dosen atau menambahkan SKS/PT/BM yang belum disahkan. Pilihan studi kasus atau eksperimen lanjutan harus tetap memenuhi cek inti 13.3 dan digunakan sebagai pengayaan, bukan syarat penilaian tersembunyi.

### 13.1B Rumusan inti CPMK dan Sub-CPMK spesifik jalur [U]

Rumusan di bawah adalah **usulan redaksi operasional RPS per jalur**, bukan tambahan empat CPMK ke beban MK. Pilih satu kolom/jalur untuk RPS kelas/mahasiswa sesuai keputusan prodi. Nomor dasar dan pemetaan ke CPL04 tetap sama seperti 4.2: masing-masing baris berisi dua Sub-CPMK yang berurutan (misalnya **.1.1/.1.2** untuk CPMK04.1). **Ambang usulan untuk setiap CPMK ≥4/5 cek instrumen 4.4**, dengan kondisi, metode, waktu, bobot dan rubrik 13.3; penekanan teknis diperlihatkan pada bukti/penjelasan, bukan cek berbobot tambahan. Jika prodi menghendaki capaian teknis spesifik sebagai syarat nilai tersendiri, revisi kisi-kisi dan rubrik sebelum perkuliahan.

| Jalur | CPMK04.1 dan Sub-CPMK .1.1 / .1.2 — T1 | CPMK04.2 dan Sub-CPMK .2.1 / .2.2 — UTS | CPMK04.3 dan Sub-CPMK .3.1 / .3.2 — T2 | CPMK04.4 dan Sub-CPMK .4.1 / .4.2 — UAS |
|---|---|---|---|---|
| **a Native** | Merancang kebutuhan dan data untuk aplikasi PHP prosedural: identifikasi aktor/kebutuhan/alur / modelkan entitas, relasi dan keterlacakan. | Menerapkan endpoint dan CRUD prosedural PHP–PDO: buat handler/request/response / buat operasi create/read/update/delete dan tangani ID hilang. | Menerapkan akses dan validasi pada file/fungsi PHP: buat login, logout, sesi dan pemeriksaan peran / validasi server serta parameterisasi PDO. | Mengintegrasikan dan menguji aplikasi prosedural: hubungkan form, endpoint, fungsi, data dan akses / uji normal-gagal serta dokumentasikan perbaikan. |
| **b OOP** | Merancang kebutuhan, data dan pembagian tanggung jawab aplikasi OOP: identifikasi aktor/kebutuhan/alur / modelkan relasi data dan calon kelas. | Mengimplementasikan endpoint dan CRUD melalui kelas PHP: gunakan controller/handler / repository PDO untuk CRUD dan ID hilang. | Menerapkan akses dan validasi berbasis kelas: layanan login/logout dan pembatasan peran / validator dan query PDO terparameter. | Mengintegrasikan dan menguji aplikasi berbasis objek: hubungkan controller, service/repository, view, data dan akses / uji alur serta dokumentasikan perbaikan. |
| **c Laravel** | Merancang kebutuhan dan data aplikasi Laravel: identifikasi aktor/kebutuhan/alur / modelkan relasi entitas dan rencana migration. | Mengimplementasikan rute dan CRUD Laravel: route/controller dan respons / migration/Eloquent untuk CRUD dan ID hilang. | Menerapkan autentikasi dan validasi Laravel: login/logout dan otorisasi peran / validasi request dan query terparameter. | Mengintegrasikan dan menguji aplikasi Laravel: hubungkan Blade, route, controller, model dan akses / uji alur serta dokumentasikan perbaikan. |
| **d Flask** | Merancang kebutuhan dan data untuk proyek Flask yang dipelajari secara mandiri terarah: identifikasi aktor/kebutuhan/alur / modelkan entitas dan relasi SQLite. | Mengimplementasikan rute dan CRUD Flask: route/view function dan respons / `sqlite3` untuk CRUD dan ID hilang. | Menerapkan akses dan validasi Flask: login/logout, sesi dan pemeriksaan peran / validasi server dan query `sqlite3` terparameter. | Mengintegrasikan dan menguji proyek Flask: hubungkan Jinja, route, data dan akses / uji alur serta dokumentasikan perbaikan dan proses belajar. |

Penamaan teknis tidak mengubah delapan Sub-CPMK inti: rencana minggu 13.5 memakai kode 04.1.1–04.4.2 dari 4.2, dan kolom di atas memberikan konteks implementasi masing-masing. T1 tetap menilai kebutuhan/model data, bukan kemampuan coding. Catatan proses belajar pada d adalah bahan bimbingan/umpan balik; UAS tetap dinilai melalui lima butir 4.4.

### 13.1C Diferensiasi bahan kajian dan hasil kerja [U]

| Jalur | Bahan kajian inti yang berbeda | Hasil kerja khas (sebagai bukti lima cek bersama) |
|---|---|---|
| **a** | Siklus HTTP, form dan endpoint file PHP; fungsi prosedural; sesi; PDO dan SQL. | Berkas PHP/fungsi dan view sederhana; uji CRUD, peran dan integrasi secara lokal. |
| **b** | Class/object, enkapsulasi dan pemisahan controller–service–repository; PDO; tanggung jawab kelas dan pengujian. | Kelas controller/service/repository dan penjelasan interaksi objek, selain uji perilaku bersama. |
| **c** | Siklus Laravel, route/controller/Blade, migration/Eloquent, validasi, middleware dan otorisasi. | Proyek Laravel yang menjelaskan penggunaan fasilitas framework dan kode sendiri, selain uji perilaku bersama. |
| **d** | Python dan Flask/Jinja, lingkungan virtual, `sqlite3`, sesi dan Flask-WTF; membaca dokumentasi serta pengelolaan belajar mandiri. | Proyek Flask, petunjuk dependensi dan bukti eksperimen/refleksi untuk bimbingan, selain uji perilaku bersama. |

Proyek kasus dummy dan lima cek sama agar penguasaan inti dapat dibandingkan. Setiap jalur punya teknologi, keluaran dan redaksi CPMK berbeda; kesetaraan ini tidak berarti materi lanjutan b/c/d identik dengan materi dasar a.

### 13.2 Lingkungan, data dan keamanan [U]

- **Kasus bersama:** contoh inventaris peralatan kampus, dengan entitas `kategori` dan `barang` yang berelasi; data barang minimal nama, kategori dan stok. Dua peran dummy: **admin** dapat mengelola data dan **petugas** dapat membaca data. Kasus lain boleh dipilih asalkan kompleksitas, hak akses dan lima cek tiap instrumen tetap setara. Tidak menggunakan data pribadi nyata.
- **KOM-526a/KOM-526b:** PHP, web server lokal dan ekstensi PDO dengan driver database; SQLite (`pdo_sqlite`) adalah contoh. Database dan berkas konfigurasi disimpan di luar direktori publik. KOM-526b dapat memakai `spl_autoload_register` atau Composer untuk autoload, sesuai kesiapan kelas; tidak menggunakan framework aplikasi.
- **KOM-526c:** PHP dengan ekstensi yang disyaratkan versi Laravel terpilih, Composer, SQLite/driver atau DB lain. Pengampu memilih dan mencatat versi yang kompatibel, menyiapkan dependensi dan kunci aplikasi pada lingkungan latihan. Gunakan Blade dan layanan Laravel; starter kit autentikasi **opsional**, bukan prasyarat. Bila memilih starter kit yang membutuhkan Node/tooling aset, siapkan dan verifikasi pula dependensinya; tidak otomatis diperlukan untuk semua proyek Laravel.
- **KOM-526d:** Python, virtual environment, Flask, `sqlite3` dan Flask-WTF (`CSRFProtect` atau `FlaskForm`) yang kompatibel. Pengampu memilih dan mencatat versi serta dependensi, termasuk cara memulai server dan inisialisasi data; Flask-WTF bukan bagian bawaan Flask. Kunci sesi/CSRF dari konfigurasi lingkungan lokal, **tidak** disematkan sebagai rahasia nyata di source code.
- Paket Composer/pip, runtime, driver, emulator lingkungan, lisensi dan akses jaringan harus **disiapkan dan diuji pengampu sebelum kuliah**. Rencanakan salinan paket atau repositori lokal yang sah bila internet terbatas; jangan menganggap instalasi otomatis offline. Catat versi dan dependensi untuk reproduksi, tanpa mewajibkan versi yang belum disetujui.
- **Baseline praktik aman [U]:** validasi sisi server; query terparameter untuk **nilai** (nama kolom/tabel dinamis harus dari allow-list); escape output HTML; library hashing dan verifikasi kata sandi; otorisasi per-permintaan di server; data dummy; sesi dan logout; serta proteksi CSRF pada formulir yang mengubah data. KOM-526a/KOM-526b mengelola token CSRF sesi dan memverifikasinya dengan `hash_equals`, meregenerasi ID sesi setelah login dan mengakhiri sesi saat logout; KOM-526c memakai mekanisme CSRF Laravel pada rute web/formulir; KOM-526d mengaktifkan Flask-WTF dan menyertakan token pada form. Sesuaikan dengan dokumentasi versi terpilih. Kontrol ini tidak membuktikan kesiapan produksi.
- KOM-526d perlu perhatian: sesi default Flask menggunakan cookie bertanda tangan. `session.clear()` dan respons logout menghapus state dari **browser yang diuji**, tetapi tidak otomatis membatalkan salinan cookie lama yang masih valid; kebutuhan pembatalan salinan memerlukan mekanisme revokasi/server-side yang disetujui. T2 butir logout di 4.4 menguji sesi browser saat ini, bukan mengklaim revokasi seluruh salinan.

### 13.3 Skenario dan kriteria asesmen setara [U]

Bobot tetap **T1 20%, UTS 25%, T2 25%, UAS 30%**, target 4 dari 5 butir, masing-masing 20% dari skor instrumen dan skor biner bagian 9.4; belum merupakan kebijakan resmi. Lima butir di 4.4 **tidak diganti**, implementasi diadaptasi dengan alat varian.

| Instrumen | Skenario contoh dengan kondisi dan hasil minimum | Bukti / kesetaraan |
|---|---|---|
| **Tugas 1, minggu 4 — CPMK04.1** | Jelaskan dua peran dan haknya; susun ≥3 kebutuhan teruji, alur utama, ≥2 entitas berelasi, serta keterlacakan kebutuhan–data/alur. Tidak menilai framework atau kode sebagai butir tambahan. | Dokumen kebutuhan, diagram, model data dan penjelasan individu; lima cek sama untuk semua varian. |
| **UTS, minggu 8 — CPMK04.2** | Dalam lab terisolasi dan database dummy, (1) buat barang baru; (2) baca barang tersebut; (3) ubah stok dan baca ulang; (4) hapus barang dan pastikan hilang; (5) minta ID yang tidak ada dan tampilkan respons/pesan tidak ditemukan. Autentikasi/role belum menjadi butir UTS. | Kode rute/handler dan penyimpanan, langkah menjalankan, tabel input–hasil diharapkan–hasil aktual untuk lima cek. Pada Laravel dan Flask, tangani not-found melalui mekanisme framework. |
| **Tugas 2, minggu 12 — CPMK04.3** | (1) Login admin dengan kredensial dummy valid; (2) sandi salah ditolak; (3) petugas ditolak mengubah data admin; (4) logout dan permintaan berikutnya dari browser yang sama tidak lagi mendapat akses terlindungi; (5) stok negatif ditolak server **dan** kueri data yang menerima input memakai parameter. | Kode, matriks peran, lima hasil uji dan penjelasan individu. Petugas dan admin harus benar-benar berbeda izin; pemeriksaan validasi dan parameterisasi keduanya termasuk butir 5. |
| **UAS, minggu 16 — CPMK04.4** | (1) Alur sesuai rancangan terintegrasi; (2) data tersimpan dan terbaca; (3) akses sesuai peran; (4) alur gagal ditangani dan dicatat; (5) petunjuk lokal, hasil uji serta perbaikan tersedia. | Proyek, data dummy atau seed, petunjuk, hasil lima cek dan demonstrasi individu. Nilai integrasi sebagai CPMK04.4, bukan menghitung kembali bobot CPMK04.2/04.3. |

**Kondisi implementasi khusus jalur untuk instrumen 4.4 [U]:** pada UTS, T2 dan UAS, cek dinyatakan terpenuhi hanya bila perilaku yang dicek dapat dibuktikan menggunakan implementasi jalur yang dipilih; ini adalah kondisi uji pada lima butir yang sama, bukan butir keenam. T1 tetap memeriksa rancangan, tidak mensyaratkan kode berjalan. Jika ketentuan ini disetujui, sampaikan kepada mahasiswa sebelum evaluasi.

| Jalur | Kondisi bukti implementasi yang dinilai pada cek terkait |
|---|---|
| **a** | Handler/fungsi prosedural PHP dan PDO untuk operasi data; pemeriksaan akses dilakukan dalam alur PHP. |
| **b** | Handler/controller dan repository berbasis kelas PHP/PDO digunakan dalam alur yang sedang diuji; cek akses dibuktikan pada aplikasi OOP. |
| **c** | Rute/controller Laravel dan Eloquent dipakai pada alur data yang diuji; cek akses menggunakan mekanisme Laravel yang dipilih. |
| **d** | Route/view Flask dan `sqlite3` digunakan pada alur data yang diuji; cek akses dibuktikan pada aplikasi Flask. Kemandirian/log tidak diberi skor tambahan. |

Kondisi implementasi diperiksa pada butir yang relevan, misalnya CRUD pada UTS dan akses pada T2; tidak mensyaratkan fitur akses pada UTS. Kegagalan teknologi/struktur pada alur yang diperiksa berarti cek terkait belum terpenuhi, sesuai rubrik biner 9.4. Kelayakan dan ketepatan bukti tiap jalur tetap perlu dikonfirmasi RMK.

**Perlakuan CSRF dan kontrol tambahan:** kontrol keamanan pada 13.2 merupakan pengayaan/ketentuan rancangan pengampu. Lima butir sumatif dan bobot pada 4.4 tetap sama; jika prodi ingin menjadikan cek CSRF atau praktik lain sebagai butir berbobot yang terpisah, revisi kisi-kisi, rubrik dan bobot secara eksplisit sebelum evaluasi. Kegagalan keamanan tetap harus dicatat dalam umpan balik, tanpa klaim audit menyeluruh.

### 13.4 Pustaka teknis varian [U]

- **R10 — PHP dasar dan PDO:** [PHP Manual: PDO](https://www.php.net/manual/en/book.pdo.php); [PHP Manual: Classes and Objects](https://www.php.net/manual/en/language.oop5.php). PDO memerlukan driver untuk database yang dipilih.
- **R11 — Laravel:** [Routing Laravel 12.x](https://laravel.com/docs/12.x/routing) dan [Authentication Laravel 12.x](https://laravel.com/docs/12.x/authentication). Halaman versi ini adalah **contoh rujukan**, bukan mandat memakai Laravel 12; cocokkan dengan versi terpilih dan status dukungannya.
- **R12 — Flask:** [Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) dan [Flask-WTF CSRF Protection 1.2.x](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/); cocokkan versi yang terpasang. Flask-WTF memerlukan secret key untuk token.
- **Lintas varian:** R4–R6 di bagian 10 untuk klien–server, contoh SQLite, autentikasi dan kueri terparameter. Semua rujukan dan versi adalah usulan pengampu, bukan bukti perangkat lunak sudah terpasang atau ditetapkan prodi.

### 13.5 Rencana 16 minggu per varian [U]

Kode Sub-CPMK, waktu A/E, pekan instrumen dan bobot mengikuti rencana bersama 4.3; metode a–c mengikuti 4.3, sedangkan d menggunakan metode mandiri terarah dengan bimbingan dosen sebagaimana dirinci pada tabelnya. Bukti formatif tidak menambah bobot. Rujukan teknis KOM-526a/KOM-526b: **R10**; KOM-526c: **R11**; KOM-526d: **R12**. Gunakan juga R4–R6 sesuai indikator 11.2 dan materi; pustaka teknis pada tabel tidak menggantikan referensi tersebut.

#### KOM-526a — Jalur 1: PHP Native (dasar)

| Pekan | Sub-CPMK | Kegiatan teknis varian | Metode | Waktu | Bukti / asesmen |
|---:|---|---|---|---|---|
| 1 | 04.1.1 | Diagnostik web dan sintaks PHP; jalankan respons PHP lokal dan jelaskan alur request. | Diskusi, demonstrasi | A | Diagnostik, pengayaan bahasa dan bukti lingkungan. |
| 2 | 04.1.1 | Aktor/kebutuhan inventaris; latihan variabel, kondisi dan fungsi prosedural pada data dummy. | Studi kasus, lokakarya | A | Aktor dan kebutuhan awal. |
| 3 | 04.1.2 | Entitas/relasi kategori–barang dan keterlacakan kebutuhan; fungsi membaca data contoh. | Praktik perancangan | A | Diagram/model data dan jejak kebutuhan. |
| 4 | 04.1.1, 04.1.2, 04.2.1 | Presentasi Tugas 1; pengantar endpoint file PHP dan metode GET/POST. | Presentasi, praktik | A | **Tugas 1: 20% — CPMK04.1.** |
| 5 | 04.2.1 | Endpoint PHP prosedural: GET/POST, parameter, validasi dasar dan respons. | Kuliah, praktik | A | Bukti request dan respons. |
| 6 | 04.2.2 | PDO dengan driver SQLite: koneksi, create/read dan parameter binding. | Demonstrasi, praktik | A | Bukti create/read menggunakan data dummy. |
| 7 | 04.2.2 | Fungsi update/delete dan penanganan ID tidak ditemukan menggunakan PDO. | Praktik, uji | A | Bukti update/delete dan not-found. |
| 8 | 04.2.1, 04.2.2 | UTS praktik: endpoint PHP prosedural dan lima kasus CRUD/not-found. | Ujian praktik | E | **UTS: 25% — CPMK04.2.** |
| 9 | 04.3.1 | Pustaka password_hash/password_verify; login/logout dan sesi PHP. | Demonstrasi, praktik | A | Bukti login/logout dengan data dummy. |
| 10 | 04.3.1 | Pemeriksaan sesi dan peran admin/petugas pada tiap endpoint server. | Studi kasus, praktik | A | Bukti uji dua peran. |
| 11 | 04.3.2 | Validasi server, PDO prepared statements, escape output dan pengenalan token CSRF. | Praktik, uji kasus | A | Bukti validasi, parameterisasi dan penjelasan kontrol. |
| 12 | 04.3.1, 04.3.2 | Tugas 2: demonstrasi autentikasi, peran dan validasi dalam PHP prosedural. | Praktik, demonstrasi | A | **Tugas 2: 25% — CPMK04.3.** |
| 13 | 04.4.1 | Integrasi halaman, fungsi, endpoint, data dan akses dalam proyek inventaris. | Praktik proyek | A | Purwarupa terintegrasi. |
| 14 | 04.4.1 | Penyelesaian alur role dan data; tinjau perbedaan endpoint dan fungsi. | Praktik, konsultasi | A | Alur kasus dan penjelasan kode. |
| 15 | 04.4.2 | Uji normal/gagal, cek CSRF pengayaan dan dokumentasi setup PHP/DB lokal. | Pengujian, umpan balik | A | Hasil uji, temuan, perbaikan dan petunjuk lokal. |
| 16 | 04.4.1, 04.4.2 | UAS: demonstrasi proyek PHP prosedural dan bukti lima cek integrasi. | Ujian proyek | E | **UAS: 30% — CPMK04.4.** |

#### KOM-526b — Jalur 2: PHP OOP

| Pekan | Sub-CPMK | Kegiatan teknis varian | Metode | Waktu | Bukti / asesmen |
|---:|---|---|---|---|---|
| 1 | 04.1.1 | Diagnostik web, sintaks PHP dan konsep kelas/objek; jalankan contoh kelas lokal. | Diskusi, demonstrasi | A | Diagnostik, pengayaan bahasa dan bukti lingkungan. |
| 2 | 04.1.1 | Aktor/kebutuhan inventaris; atribut, metode dan pembagian tanggung jawab kelas. | Studi kasus, lokakarya | A | Aktor dan kebutuhan awal. |
| 3 | 04.1.2 | Entitas/relasi kategori–barang dan usulan kelas model/repository. | Praktik perancangan | A | Diagram/model data dan jejak kebutuhan. |
| 4 | 04.1.1, 04.1.2, 04.2.1 | Presentasi Tugas 1; pengantar controller/endpoint dan siklus request. | Presentasi, praktik | A | **Tugas 1: 20% — CPMK04.1.** |
| 5 | 04.2.1 | Controller/handler, request/response dan pemisahan view; autoload sederhana. | Kuliah, praktik | A | Bukti request dan respons. |
| 6 | 04.2.2 | Repository PDO: koneksi terpisah dan operasi create/read terparameter. | Demonstrasi, praktik | A | Bukti create/read menggunakan data dummy. |
| 7 | 04.2.2 | Metode update/delete repository dan exception/not-found pada controller. | Praktik, uji | A | Bukti update/delete dan not-found. |
| 8 | 04.2.1, 04.2.2 | UTS praktik: controller, repository PDO dan lima kasus CRUD/not-found. | Ujian praktik | E | **UTS: 25% — CPMK04.2.** |
| 9 | 04.3.1 | Kelas layanan autentikasi dengan password_hash/password_verify dan sesi. | Demonstrasi, praktik | A | Bukti login/logout dengan data dummy. |
| 10 | 04.3.1 | Penjagaan peran admin/petugas dalam controller atau middleware sederhana. | Studi kasus, praktik | A | Bukti uji dua peran. |
| 11 | 04.3.2 | Validator dan repository: validasi server, binding, escape output dan token CSRF. | Praktik, uji kasus | A | Bukti validasi, parameterisasi dan penjelasan kontrol. |
| 12 | 04.3.1, 04.3.2 | Tugas 2: demonstrasi layanan autentikasi, peran dan validasi berbasis kelas. | Praktik, demonstrasi | A | **Tugas 2: 25% — CPMK04.3.** |
| 13 | 04.4.1 | Integrasi controller, service/repository, view, data dan akses. | Praktik proyek | A | Purwarupa terintegrasi. |
| 14 | 04.4.1 | Penyelesaian alur dan penjelasan enkapsulasi serta tanggung jawab kelas. | Praktik, konsultasi | A | Alur kasus dan penjelasan kode. |
| 15 | 04.4.2 | Uji normal/gagal kelas dan alur aplikasi; cek CSRF pengayaan dan dokumentasi. | Pengujian, umpan balik | A | Hasil uji, temuan, perbaikan dan petunjuk lokal. |
| 16 | 04.4.1, 04.4.2 | UAS: demonstrasi proyek OOP dan bukti lima cek integrasi. | Ujian proyek | E | **UAS: 30% — CPMK04.4.** |

#### KOM-526c — Jalur 3: PHP Laravel

| Pekan | Sub-CPMK | Kegiatan teknis varian | Metode | Waktu | Bukti / asesmen |
|---:|---|---|---|---|---|
| 1 | 04.1.1 | Diagnostik PHP/OOP dan Composer; orientasi proyek Laravel dan rute sederhana. | Diskusi, demonstrasi | A | Diagnostik, pengayaan bahasa dan bukti lingkungan. |
| 2 | 04.1.1 | Aktor/kebutuhan inventaris; konvensi controller, view dan struktur proyek. | Studi kasus, lokakarya | A | Aktor dan kebutuhan awal. |
| 3 | 04.1.2 | Model kategori–barang, relasi dan rancangan migration dari kebutuhan. | Praktik perancangan | A | Diagram/model data dan jejak kebutuhan. |
| 4 | 04.1.1, 04.1.2, 04.2.1 | Presentasi Tugas 1; pengantar route dan controller Laravel. | Presentasi, praktik | A | **Tugas 1: 20% — CPMK04.1.** |
| 5 | 04.2.1 | Route web, controller, request/response dan Blade. | Kuliah, praktik | A | Bukti request dan respons. |
| 6 | 04.2.2 | Konfigurasi database, migration dan Eloquent create/read. | Demonstrasi, praktik | A | Bukti create/read menggunakan data dummy. |
| 7 | 04.2.2 | Eloquent update/delete, validasi dasar dan penanganan not-found. | Praktik, uji | A | Bukti update/delete dan not-found. |
| 8 | 04.2.1, 04.2.2 | UTS praktik: route/controller, Eloquent dan lima kasus CRUD/not-found. | Ujian praktik | E | **UTS: 25% — CPMK04.2.** |
| 9 | 04.3.1 | Fasilitas autentikasi Laravel atau starter kit pilihan; login/logout dan sesi. | Demonstrasi, praktik | A | Bukti login/logout dengan data dummy. |
| 10 | 04.3.1 | Middleware/otorisasi peran admin dan petugas pada route/controller. | Studi kasus, praktik | A | Bukti uji dua peran. |
| 11 | 04.3.2 | Validasi Request, Eloquent/query builder dan CSRF pada Blade. | Praktik, uji kasus | A | Bukti validasi, parameterisasi dan penjelasan kontrol. |
| 12 | 04.3.1, 04.3.2 | Tugas 2: demonstrasi autentikasi, peran dan validasi dengan Laravel. | Praktik, demonstrasi | A | **Tugas 2: 25% — CPMK04.3.** |
| 13 | 04.4.1 | Integrasi Blade, route, controller, model dan otorisasi. | Praktik proyek | A | Purwarupa terintegrasi. |
| 14 | 04.4.1 | Penyelesaian alur dan penjelasan kontribusi kode sendiri serta komponen framework. | Praktik, konsultasi | A | Alur kasus dan penjelasan kode. |
| 15 | 04.4.2 | Feature test atau uji terdokumentasi normal/gagal; cek CSRF pengayaan dan setup. | Pengujian, umpan balik | A | Hasil uji, temuan, perbaikan dan petunjuk lokal. |
| 16 | 04.4.1, 04.4.2 | UAS: demonstrasi proyek Laravel dan bukti lima cek integrasi. | Ujian proyek | E | **UAS: 30% — CPMK04.4.** |

#### KOM-526d — Jalur 4: Python Web Flask (mandiri terarah)

| Pekan | Sub-CPMK | Kegiatan teknis varian | Metode | Waktu | Bukti / asesmen |
|---:|---|---|---|---|---|
| 1 | 04.1.1 | Diagnostik sintaks Python dan web; siapkan virtual environment dan respons Flask; sepakati rencana belajar dan jadwal konsultasi. | Diagnostik, kontrak belajar dan konsultasi | A | Diagnostik, pengayaan bahasa dan bukti lingkungan. |
| 2 | 04.1.1 | Aktor/kebutuhan inventaris; variabel, kondisi dan fungsi Python pada data dummy. | Studi mandiri, lokakarya bimbingan | A | Aktor dan kebutuhan awal. |
| 3 | 04.1.2 | Model kategori–barang, relasi dan rancangan penyimpanan SQLite. | Rancang mandiri, konsultasi | A | Diagram/model data dan jejak kebutuhan. |
| 4 | 04.1.1, 04.1.2, 04.2.1 | Presentasi Tugas 1; pengantar route dan view function Flask. | Presentasi rancangan dan umpan balik | A | **Tugas 1: 20% — CPMK04.1.** |
| 5 | 04.2.1 | Flask route, metode GET/POST, request/response dan template Jinja; baca dokumentasi dan catat eksperimen. | Studi dokumentasi, praktik dan konsultasi | A | Bukti request dan respons. |
| 6 | 04.2.2 | SQLite via sqlite3: koneksi, create/read dan placeholder parameter. | Eksperimen mandiri, bimbingan | A | Bukti create/read menggunakan data dummy. |
| 7 | 04.2.2 | Update/delete, penanganan ID tidak ditemukan dan respons 404 Flask. | Praktik mandiri, uji dan konsultasi | A | Bukti update/delete dan not-found. |
| 8 | 04.2.1, 04.2.2 | UTS praktik: route Flask/sqlite3 dan lima kasus CRUD/not-found. | Ujian praktik | E | **UTS: 25% — CPMK04.2.** |
| 9 | 04.3.1 | Hash/verifikasi kata sandi Werkzeug, login/logout dan sesi Flask. | Studi dokumentasi, praktik dan konsultasi | A | Bukti login/logout dengan data dummy. |
| 10 | 04.3.1 | Dekorator atau pemeriksaan peran admin/petugas pada route terlindungi. | Studi kasus mandiri, konsultasi | A | Bukti uji dua peran. |
| 11 | 04.3.2 | Validasi server, sqlite3 parameter binding, autoescape Jinja dan Flask-WTF CSRF. | Praktik mandiri, uji dan umpan balik | A | Bukti validasi, parameterisasi dan penjelasan kontrol. |
| 12 | 04.3.1, 04.3.2 | Tugas 2: demonstrasi login, peran, validasi dan sesi browser dengan Flask. | Praktik dan demonstrasi | A | **Tugas 2: 25% — CPMK04.3.** |
| 13 | 04.4.1 | Integrasi route, Jinja, data dan akses dalam proyek inventaris. | Proyek mandiri terarah, konsultasi | A | Purwarupa terintegrasi. |
| 14 | 04.4.1 | Penyelesaian alur dan pemisahan fungsi akses data serta handler. | Proyek mandiri terarah, konsultasi | A | Alur kasus dan penjelasan kode. |
| 15 | 04.4.2 | Flask test client atau uji terdokumentasi normal/gagal; cek CSRF pengayaan, setup dan refleksi proses belajar. | Uji mandiri dan umpan balik | A | Hasil uji, temuan, perbaikan dan petunjuk lokal. |
| 16 | 04.4.1, 04.4.2 | UAS: demonstrasi proyek Flask dan bukti lima cek integrasi. | Ujian proyek | E | **UAS: 30% — CPMK04.4.** |

### 13.6 Validasi sebelum memilih varian [K]

1. Prodi/RMK menyetujui mekanisme pilihan dan penempatan a–d, pengakuan pengalaman setara, status kode resmi/KRS, kapasitas kelas, akses lab, dosen pembimbing d dan ketersediaan runtime/driver, database serta paket; tidak ada jalur otomatis menjadi standar prodi.
2. Pastikan kesiapan bahasa mahasiswa dan atur pengayaan; catat dampak pada waktu tanpa mengubah prasyarat resmi atau menambah beban otomatis.
3. Periksa T/P, slot A/E dan durasi PT/BM; validasi kelayakan materi, instrumen, rubrik dan bobot terhadap RPS/pedoman prodi.
4. Tinjau penggunaan seed dummy, parameterisasi, pengelolaan rahasia, peran, output, sesi dan CSRF pada lingkungan lokal. Validasi fungsi bukan audit keamanan produksi.
5. Catat versi yang diuji, cara penyediaan paket dan bukti reproduksi; tentukan RPS, dosen, otorisasi dan penanggung jawab tiap kelas. Rencana di atas **belum diuji menjalankan aplikasi** dan belum disahkan.

---

## 14. Dua jalur implementasi KFC-506: Dart + Flutter dan React Native + Expo [U]

### 14.1 Aturan bersama dan batas kesetaraan

**KFC-506a** dan **KFC-506b** adalah label usulan untuk dua jalur alternatif di dalam **satu mata kuliah resmi KFC-506 Sistem Aplikasi Lintas Platform**; sufiks a–b bukan kode kurikulum/KRS resmi yang telah ditemukan atau disahkan. Mahasiswa mengambil **satu** jalur bila prodi menyetujui pembukaan/penempatan, pengampu, fasilitas, lisensi alat dan pencatatan akademiknya. Keduanya bukan MK baru dan bukan urutan wajib.

| Aspek | KFC-506a — Dart + Flutter | KFC-506b — React Native + Expo |
|---|---|---|
| Gaya implementasi [U] | Satu basis kode **Dart** dengan widget Flutter; build web dan build Android dari proyek yang sama. | Satu basis kode **JavaScript/TypeScript** dengan komponen React Native dalam proyek **Expo**; target web dan Android dari proyek yang sama. |
| Alat utama [U] | Flutter SDK stabil, `flutter doctor`, editor dengan ekstensi Flutter, browser, Android SDK/emulator. | Node.js LTS, `create-expo-app`, Expo CLI (`npx expo start`), Expo Go atau development build, Android SDK/emulator. |
| Navigasi dan state [U] | `Navigator`/route Flutter; `StatefulWidget` dan `setState`. | Expo Router atau React Navigation; `useState`/`useReducer`. |
| Penyimpanan lokal [U] | `sqflite`/`path` di Android; mekanisme alternatif untuk web dicatat keterbatasannya. | `expo-sqlite` (basis data yang bertahan setelah restart) atau async storage (key-value tidak terenkripsi). |
| Aksesibilitas [U] | `Semantics`, label kontrol, ukuran target sentuh, uji pembaca layar/fokus. | `accessibilityLabel`, `accessibilityRole`, `accessibilityHint`, `accessible`, uji TalkBack/VoiceOver. |
| Uji [U] | `flutter test` dan integration test. | `jest-expo` dengan Testing Library dan uji manual per target. |
| Fondasi yang didiagnosis [U] | Dasar pemrograman dan objek; Dart diperkenalkan pada jalur ini. | Dasar pemrograman, JavaScript/React dan ekosistem Node/npm. |

Yang **tidak berubah** antarpjalur: CPL04, BK02, kerangka CPMK04.1–04.4 dan delapan Sub-CPMK pada 5.2 (redaksi teknis disesuaikan), pekan 1–15 serta evaluasi pekan 8/16, instrumen T1/UTS/T2/UAS dengan bobot 20/25/25/30, lima cek biner bernilai sama per instrumen, target usulan ≥4/5, syarat dua **runtime/platform** berbeda, kasus dummy, serta larangan menambah butir/bobot. Perbedaan hanya pada teknologi, alat dan bukti yang wajar. Fondasi bahasa adalah materi diagnostik/penguatan pada minggu 1–4, **bukan prasyarat akademik baru**.

### 14.2 Dua target: definisi operasional [U]

Dua target berarti dua **runtime/platform** berbeda yang dihasilkan dari satu basis kode, misalnya **web di browser desktop** dan **Android di emulator atau perangkat**. Dua ukuran layar, dua orientasi, atau dua tab browser pada satu target **bukan** dua target. Jika perangkat/emulator tidak tersedia, pengampu menyediakan akses lab atau perangkat pinjaman sebelum mengunci jalur; alternatif target lain (misalnya iOS pada macOS atau desktop native) hanya jika fasilitasnya terverifikasi.

### 14.3 Skenario dan kriteria asesmen setara [U]

Lima butir 5.4 **tidak diganti**; kondisi uji diadaptasi dengan alat jalur. Perangkat rinci ada di dokumen turunan.

| Instrumen | Kondisi uji jalur a (Flutter) | Kondisi uji jalur b (Expo) |
|---|---|---|
| **Tugas 1, minggu 4 — CPMK04.1** | Proyek Flutter berjalan di web dan Android; aksi tambah data dummy bekerja pada keduanya; `lib`/`pubspec.yaml` dan konfigurasi target ditunjukkan. | Proyek Expo berjalan di web (`npx expo start`) dan Android (Expo Go/development build); aksi tambah bekerja; `app`/`package.json` dan konfigurasi target ditunjukkan. |
| **UTS, minggu 8 — CPMK04.2** | Layout adaptif dengan `MediaQuery`/`LayoutBuilder` terbaca di kedua target; `Semantics`/label kontrol; fokus keyboard di web dan TalkBack di Android; umpan balik aksi. | Layout adaptif dengan `useWindowDimensions`/`Platform`; `accessibilityLabel`/`accessibilityRole`; fokus keyboard di web dan TalkBack di Android; umpan balik aksi. |
| **Tugas 2, minggu 12 — CPMK04.3** | State/`setState`, `Navigator` dua halaman, penyimpanan lokal yang didukung kedua target (atau keterbatasan dicatat), pemulihan setelah buka ulang, pesan data invalid/gagal. | State React, Expo Router/React Navigation, `expo-sqlite` atau async storage, pemulihan setelah buka ulang, pesan data invalid/gagal. |
| **UAS, minggu 16 — CPMK04.4** | Satu basis kode terintegrasi; fitur utama jalan di web dan Android; hasil `flutter test`/integration test, perbedaan dan perbaikan dicatat; petunjuk dan demonstrasi. | Satu basis kode terintegrasi; fitur utama jalan di web dan Android; hasil `jest-expo` dan uji manual, perbedaan (termasuk batas Expo Go) dan perbaikan dicatat; petunjuk dan demonstrasi. |

Kegagalan alat pada alur yang diperiksa berarti cek terkait belum terpenuhi, sesuai rubrik biner; namun kendala fasilitas yang terdokumentasi harus diselesaikan pengampu sebelum penilaian, bukan menjadi penalti mahasiswa.

### 14.4 Pustaka teknis jalur [U]

- **R13–R15 — Flutter:** [Install and set up Flutter](https://docs.flutter.dev/install), [Flutter learning pathway](https://docs.flutter.dev/learn/pathway), [Adaptive and responsive design](https://docs.flutter.dev/ui/adaptive-responsive), [Navigation basics](https://docs.flutter.dev/cookbook/navigation/navigation-basics), [Accessibility](https://docs.flutter.dev/ui/accessibility), [Testing Flutter apps](https://docs.flutter.dev/testing/overview). Halaman dokumentasi menampilkan versi Flutter terkini saat diakses; cocokkan dengan versi yang dipasang.
- **R16–R18 — React Native + Expo:** [Create a project](https://docs.expo.dev/get-started/create-a-project/), [Set up your environment](https://docs.expo.dev/get-started/set-up-your-environment/), [Expo Router](https://docs.expo.dev/router/introduction/), React Native [Accessibility](https://reactnative.dev/docs/accessibility), [expo-sqlite](https://docs.expo.dev/versions/latest/sdk/sqlite/), [AsyncStorage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Unit testing with Jest](https://docs.expo.dev/develop/unit-testing/). SDK Expo bergerak cepat (dokumentasi saat diakses menyebut SDK 58 sebagai versi terbaru); jangan mengunci versi yang belum disetujui pengampu.
- R7–R9 pada bagian 10 tetap rujukan konsep lintas platform; R13–R15 dan R16–R18 adalah rujukan teknis per jalur.

### 14.5 Perangkat rinci dan rencana 16 minggu [U]

| Jalur | Paket RPS/SAP/asesmen | Outline 14 bab | Rencana evaluasi | Rubrik |
|---|---|---|---|---|
| KFC-506a Dart + Flutter | [037](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md) | [036](036_OUTLINE_MODUL_KFC-506A_DART_FLUTTER_09112026_1339.md) | [038](038_RENCANA_EVALUASI_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md) | [039](039_RUBRIK_PENILAIAN_KFC-506A_DART_FLUTTER_09112026_1339.md) |
| KFC-506b React Native + Expo | [041](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) | [040](040_OUTLINE_MODUL_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) | [042](042_RENCANA_EVALUASI_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) | [043](043_RUBRIK_PENILAIAN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md) |

Rencana mingguan, SAP 16 pertemuan dan tabel 14 modul untuk masing-masing jalur ada di paket 037/041; isinya mengikuti Sub-CPMK, pekan dan bobot pada 5.2–5.4 dengan kegiatan teknis yang berbeda. **Dokumen netral** [017](017_PAKET_RPS_SAP_ASESMEN_KFC-506_SISTEM_APLIKASI_LINTAS_PLATFORM_07112026_1328.md), [033](033_OUTLINE_MODUL_KFC-506_07112026_1332.md), [034](034_RENCANA_EVALUASI_ASESMEN_KFC-506_07112026_1332.md) dan [035](035_RUBRIK_PENILAIAN_KFC-506_07112026_1332.md) tetap berlaku sebagai rencana dasar tanpa mengunci framework.

### 14.6 Validasi sebelum membuka jalur [K]

1. Prodi/RMK menyetujui mekanisme pilihan a–b, status kode/KRS, kapasitas kelas, dosen, serta pencatatan nilai.
2. Pastikan ketersediaan Flutter SDK **dan** Node/npm/Expo beserta paket offline yang sah; catat versi, lisensi dan cara instalasi. Emulator Android atau perangkat fisik tersedia untuk semua mahasiswa, termasuk opsi pinjaman.
3. Periksa kesiapan dasar mahasiswa (pemrograman, objek, JavaScript/React untuk jalur b) dan sediakan pengayaan minggu 1–4 tanpa mengubah prasyarat resmi.
4. Uji kelayakan waktu build/refresh pada kedua target, terutama Flutter web dan Expo Go, agar durasi ujian praktik realistis.
5. Validasi instrumen dan rubrik terhadap RPS/pedoman prodi; jangan menambah butir atau bobot tanpa revisi kisi-kisi.
6. Catat versi SDK yang diuji dan bukti reproduksi. Rencana ini **belum diuji menjalankan aplikasi** dan belum disahkan.
