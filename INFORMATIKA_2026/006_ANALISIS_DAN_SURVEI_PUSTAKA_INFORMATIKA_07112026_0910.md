# Analisis mendalam dan survei pustaka — Teknik Informatika UWG 2026

## 1. Ringkasan keputusan

Ini adalah **kajian dokumen dan pemetaan awal**, bukan hasil survei lapangan atau pernyataan kesesuaian akreditasi. Pemetaan area APTIKOM terhadap MK hanya berdasarkan judul dan belum divalidasi terhadap RPS, CPMK, asesmen, jam, hasil belajar, atau dokumen pelaksanaan. Tidak dilakukan perubahan SKS, CPL, MK, prasyarat, beban kerja atau kurikulum.

1. [Pemetaan 005](005_PEMETAAN_APTIKOM_MK_INFORMATIKA_07112026_0910.md) mencakup **83 MK berkode** pada Tabel 15 dokumen 004, dengan kandidat untuk 22 area BK APTIKOM. Ini inventaris penawaran, **bukan** 83 MK yang wajib ditempuh seorang mahasiswa.
2. Di antara 83 MK tersebut: 49 muncul sebagai baris non-konsentrasi dalam Tabel 18; sembilan adalah alternatif wajib untuk tiga konsentrasi (masing-masing tiga); dan 25 tidak muncul sebagai MK berkode pada Tabel 18. Tabel 18 memuat empat slot pilihan tambahan tanpa kode. Istilah ini mencerminkan posisi dalam tabel, bukan verifikasi aturan pengambilan resmi.
3. Terdapat **17 MK** yang tidak memperoleh kandidat APTIKOM pada pemetaan konservatif berbasis judul. Artinya **belum dipetakan oleh kajian ini**, bukan tidak memiliki materi, bukan celah kurikulum.
4. Untuk 58 MK berkode yang ada pada kedua tabel, perbandingan turunan Tabel 18 → Tabel 14 dengan BK eksplisit Tabel 15 menemukan 23 set sama dan 35 set dengan BK tambahan; tidak ada set yang kehilangan BK turunan dalam perhitungan tersebut. Tambahan dapat mencerminkan lintas bidang; bukan otomatis kesalahan.
5. Pada versi DOCX yang diekstrak, daftar CPMK per MK tidak ditemukan dalam teks/tabel utama. Pembacaan awal `python-docx` tidak menampilkan tanda relasi Tabel 12/19; pemeriksaan XML terbatas menemukan tanda CPL04 pada tiga baris Tabel 19 ([009](009_ANALISIS_MK_CPL_CPMK_BOK_TEKNIK_INFORMATIKA_07112026_1258.md)); audit penuh Tabel 12/19 belum dilakukan. Keputusan atas ketercapaian CPL dan cakupan BoK harus menunggu **RPS, CPMK/Sub-CPMK dan bukti asesmen**.
6. Survei responden belum dilaksanakan. [Instrumen dan rencana](007_INSTRUMEN_SURVEI_VALIDASI_INFORMATIKA_07112026_0910.md) disiapkan untuk pengampu, mahasiswa, alumni dan pengguna lulusan.

## 2. Sumber dan batas metode

| ID | Sumber | Pemakaian | Batas |
|---|---|---|---|
| S1 | [004 — pemetaan MK, CPL, BK UWG](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md) | Tabel 18 untuk MK, semester dan CPL; Tabel 15 untuk 83 MK–BK. | Turunan DOCX; tidak memuat rincian RPS. Kode BK UWG tidak setara otomatis dengan kode BK APTIKOM. |
| S2 | [003 — BoK dan bahan kajian UWG](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md), [001 — CPL](001_CPL_TEKNIK_INFORMATIKA_07112026_0859.md), [002 — CPMK](002_CPMK_TEKNIK_INFORMATIKA_07112026_0859.md) | Definisi 10 BK, 10 CPL dan status keberadaan CPMK. | Pernyataan materi dalam rumusan BK/CPL bukan bukti pelaksanaan per MK. |
| S3 | [Panduan APTIKOM S1 Informatika/Ilmu Komputer v2.0](../BUKU_OBE/839193049-Buku-Kurikulum-Prodi-S1-Informatika-atau-Ilmu-Komputer-Versi-2-0-aptikom.pdf) | Tabel 4 PDF halaman 42 (22 BK); RPS halaman 56–65; capstone halaman 53–54; Lampiran 6 halaman 116–121. Angka halaman adalah **nomor halaman PDF**, bukan nomor cetak. | Panduan 2024; bukan data implementasi UWG atau bukti status regulasi saat ini. |
| S4 | Laporan ACM/IEEE-CS/AAAI CS2023, knowledge model [3](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm) | Pembanding primer untuk 17 knowledge area dan perbedaan angka pada tabel APTIKOM. | Perlu menelusuri setiap knowledge unit, hasil belajar, versi, dan konteks sebelum digunakan untuk perhitungan. |

**Metode:** (1) baca 004, 003, 001, 002 dan halaman sumber APTIKOM di atas; (2) gunakan alias A01–A22 untuk BK01–BK22 APTIKOM agar tidak tercampur dengan BK01–BK10 UWG; (3) kurasi kandidat MK terhadap nama BK APTIKOM dari judul mata kuliah, bukan penerapan aturan otomatis terhadap semua BK lokal; (4) bandingkan set BK yang eksplisit dan yang diturunkan dari CPL menurut Tabel 14; (5) susun daftar pemeriksaan dan rancangan survei. Daftar seluruh 83 keputusan kandidat disajikan di 005, dengan kode dan kategori statusnya.

**Bukan hasil penelitian ini:** observasi kelas, survei responden, perbandingan lapangan antaruniversitas, audit penuh CSC2023 pada level knowledge unit, bukti pengukuran CPL, verifikasi regulasi terkini, atau putusan kecukupan/kualitas kurikulum.

## 3. Temuan kuantitatif yang dapat ditelusuri

### 3.1 Populasi baris dan simulasi paket

Tabel 18 memuat 62 baris: 58 MK berkode dan 4 slot pilihan 3 SKS tanpa kode. Dari 58, 49 baris tidak memiliki label konsentrasi dan 9 baris memiliki label wajib konsentrasi (IM 3, DS 3, MC 3). Tabel 15 memiliki 83 kode unik; 25 kode tidak muncul sebagai MK berkode pada Tabel 18. Perhitungan tidak menambahkan ketiga alternatif konsentrasi sebagai kewajiban bersamaan.

Jika dan hanya jika satu set tiga MK wajib konsentrasi dipilih, seluruh 49 baris non-konsentrasi dan keempat slot dipenuhi sesuai bobot di Tabel 18, tiap simulasi IM, DS atau MC menghasilkan **146 SKS**, dengan distribusi 20, 20, 21, 21, 21, 21, 16, 6 SKS. Ini **aritmetika Tabel 18**, bukan penetapan aturan kelulusan atau validasi ketersediaan slot. Keputusan resmi, prasyarat, jadwal dan daftar pilihan harus diverifikasi. Statistik Teknik Informatika ini tidak digabung dengan angka prodi SISTEKIN.

### 3.2 BK eksplisit versus turunan dari CPL

Aturan audit: untuk setiap MK berkode yang ada dalam kedua tabel, gabungkan BK utama setiap CPL yang dibebankan di Tabel 18 memakai Tabel 14, lalu bandingkan himpunan ini dengan BK pada Tabel 15. Dari **58** MK: **23** sama; **35** memiliki satu atau lebih BK tambahan; **0** kehilangan BK yang diturunkan. Kategori tambahan berbeda dapat terjadi pada MK yang sama; BK10 muncul sebagai tambahan pada 34 MK dan BK09 pada 26 MK. Ini menghitung **relasi tabel**, bukan beban pengajaran.

| Contoh | CPL Tabel 18 → BK utama Tabel 14 | BK eksplisit Tabel 15 | Pertanyaan validasi |
|---|---|---|---|
| KOM-101 Pengantar Teknik Informatika | CPL03, 04, 07 → BK01, 02, 06 | BK01, 02, 06, 09, 10 | Apakah komunikasi/proyek terukur dalam CPMK dan asesmen atau hanya atribut generik? |
| FST-102 Algoritma dan Pemrograman | CPL04 → BK02 | BK02, 09, 10 | Adakah bukti yang membenarkan tambahan BK09/BK10, tanpa menyimpulkan isinya dari label? |
| KOM-526 Sistem Aplikasi Web | CPL04 → BK02 | BK02, 03, 04, 05, 06, 07, 08 | Tabel 16 juga menyebut nama MK sebagai **contoh** pada CPL05, 06, 08 dan 09; bagaimana contoh tersebut berkaitan dengan pembebanan CPL pada Tabel 18? Tabel 16 tidak harus berupa daftar lengkap. |

**Tindak lanjut:** koordinator MK mengisi rubrik bukti pada instrumen 007; klarifikasi perbedaan antartabel sebelum revisi dan jangan menambah CPL/BK secara otomatis. Bila suatu BK terintegrasi sebagai konteks, tentukan apakah hubungan perlu tertulis sebagai materi, kontribusi CPL, atau hanya penguatan umum.

### 3.3 Perbedaan bobot rujukan

Pemeriksaan visual tabel APTIKOM menunjukkan nilai berikut pada kolom **CS Core / KA Core**. Ini contoh diskrepansi sumber, bukan hasil audit semua angka dan bukan konversi jam menjadi SKS:

| Area | APTIKOM Tabel 4 (PDF 42) | APTIKOM Tabel W (PDF 118) | Laporan CS2023 yang ditautkan |
|---|---|---|---|
| Artificial Intelligence | 11 / 12 | 11 / 13 | 12 / 18 [3](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm) |
| Data Management | 9 / 23 | 9 / 21 | 10 / 26 [3](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm) |
| Foundations of Programming Languages | 23 / 21 | 23 / 20 | 21 / 19 [3](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm) |

Bedakan **draft/versi** dan definisi jam; cek teks primer dan tabel visual sebelum memilih dasar. Bobot min–max pada Tabel 4 juga tidak boleh dicampur dengan kolom jam CS Core/KA Core. Jangan membagi SKS secara proporsional dari angka ini sebelum menilai konteks, beban pembelajaran dan persetujuan prodi.

## 4. Analisis per klaster dan pertanyaan mendalam

Semua kandidat berikut berasal dari 005; `U`/`IM`/`DS`/`MC`/`P` bermakna sesuai legenda 005. **Keberadaan kandidat bukan bukti materi, kedalaman, asesmen, penguasaan, maupun gap.**

| Klaster | Sinyal yang dapat ditelusuri | Risiko/pertanyaan untuk validasi | Bukti yang diperlukan |
|---|---|---|---|
| Algoritma, matematika dan bahasa pemrograman — A12, A13, A14, A20 | FST-102, FST-203, KOM-201, KOM-630 dan lainnya muncul sebagai kandidat U. | Urutan pemrograman → struktur data → analisis kompleksitas; apakah analisis kompleksitas, model komputasi dan konsep bahasa dijangkau dengan tingkat yang terukur? | RPS dan matriks topik per pekan; soal/artefak kompleksitas; prasyarat. |
| Rekayasa perangkat lunak dan platform — A05, A10, A19 | KOM-313, KOM-417, KOM-418, KOM-312, KOM-526, KOM-524 dan FST-610 muncul sebagai kandidat U. | Batas antara pemrograman, analisis, desain, pengujian, integrasi, aplikasi web/mobile dan capstone; hindari duplikasi dan lompatan keterampilan. | RPS berurutan, tugas autentik, rubrik, kontrak antarmata kuliah dan bukti proyek. |
| Arsitektur, OS, jaringan dan sistem terdistribusi — A07, A08, A11, A15, A16 | KOM-102, KOM-310, KOM-314, KOM-315 dan KOM-420 muncul sebagai kandidat U. | Apakah fondasi sistem, jaringan, keamanan dan komputasi terdistribusi terhubung sebelum pilihan cloud/sensor? Penempatan semata bukan bukti prasyarat terpenuhi. | Topik, lab, perangkat, asesmen dan aturan prasyarat terverifikasi. |
| Data dan AI — A06, A18 | FST-204, FST-207, KOM-527 dan KOM-629 merupakan kandidat U; KFD-601 merupakan kandidat wajib DS; sebagian pendalaman berstatus P. | Apa pengalaman minimal yang benar-benar tersedia untuk setiap jalur? Validasi data management, kualitas data, evaluasi model, etika dan sumber daya komputasi tanpa menganggap semua pilihan diambil. | CPMK, proyek data/model, rubrik evaluasi, daftar pilihan per jalur dan penugasan pengampu. |
| HCI, UX, multimedia — A04, A09, A17 | KOM-419 dan KOM-525 adalah kandidat U; KFC-707 berlabel MC; tiga kandidat grafika diberi label IM. | Mana fondasi yang diwajibkan semua mahasiswa dan mana pendalaman? Apakah desain berbasis pengguna dan aksesibilitas betul-betul diukur? | RPS, prototipe, uji pengguna, rubrik; paket konsentrasi. |
| Security dan etika — A01, A02 | FST-206, KOM-317 dan KOM-631 adalah kandidat U; KFC-602 hanya P. | Bagaimana keamanan, privasi dan tanggung jawab profesional dibuktikan dalam MK dasar dan proyek, bukan sekadar judul? | Materi kontrol keamanan dan etika, asesmen, panduan data dan bukti proyek. |
| Capstone, riset, profesionalisme — A03, A21, A22 | FST-610 (3 SKS), FST-611, FST-612, FST-613, FST-713 muncul di Tabel 18. | APTIKOM PDF 54 mencantumkan kriteria capstone termasuk proyek berkelompok, masalah nyata/kompleks, keluaran dan panduan; apakah implementasi UWG memenuhi kriteria yang dipilih prodi? | Panduan capstone, proyek, rubrik tim/individu, bukti mitra dan peta keterkaitan riset/PKL/skripsi. |

APTIKOM PDF 54 menyarankan maksimal dua peminatan, sementara sumber UWG menunjukkan tiga label IM/DS/MC. Ini adalah **perbedaan dengan saran panduan**, bukan kesimpulan pelanggaran atau kewajiban menghapus konsentrasi. Prodi perlu menilai rasional akademik, sumber daya, akses per jalur dan aturan yang berlaku.

### 4.1 Survei sumber eksternal: sinyal, bukan bukti lokal

| Sumber dan populasi | Temuan yang dilaporkan | Implikasi pertanyaan untuk UWG | Batas |
|---|---|---|---|
| World Economic Forum, *Future of Jobs Report 2025*, ekspektasi pemberi kerja global | Responden memproyeksikan AI/big data, jaringan/cybersecurity dan literasi teknologi termasuk keterampilan yang meningkat paling cepat; keterampilan berpikir kreatif dan pembelajaran sepanjang hayat juga meningkat [1](https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/3-skills-outlook/). | Tanyakan relevansi A18, A06, A02, A08 dan kompetensi profesional dalam instrumen 007; cocokkan dengan bukti pembelajaran. | Ekspektasi perusahaan yang disurvei, bukan proyeksi pasti lowongan di Malang/UWG dan bukan instruksi menambah MK. |
| ISC2, studi tenaga kerja cybersecurity 2024 | Studi daring pada 15.852 praktisi/pengambil keputusan; 90% responden melaporkan kesenjangan keterampilan pada tim cybersecurity mereka [2](https://www.isc2.org/Insights/2024/10/ISC2-Workforce-Study-AI-Growth-Opportunity). | Klarifikasi kemampuan keamanan dasar lintas jalur, instrumen praktik dan masukan mitra setempat. | Populasi khusus cybersecurity; angka tersebut tidak dapat dipindahkan menjadi skor kelemahan mahasiswa UWG atau pasar kerja lokal. |
| GitHub, Octoverse 2024 | GitHub melaporkan Python melewati JavaScript dalam aktivitas total pada platformnya pada 2024, bersamaan pertumbuhan penggunaan notebook dan proyek AI [1](https://github.blog/news-insights/octoverse/octoverse-2024/). | Tanyakan literasi data/pemrograman dan kemampuan mengevaluasi alat, sambil mempertahankan prinsip yang tidak bergantung satu bahasa. | Data aktivitas di satu platform, bukan survei seluruh industri, bukan ukuran kompetensi lulusan dan bukan alasan mengganti bahasa kuliah otomatis. |

Ketiga sinyal eksternal digunakan untuk menyusun **pertanyaan survei dan prioritas audit**, bukan untuk menyatakan hasil survei lapangan prodi. Tidak ada data lokal atau respons responden UWG yang digunakan dalam kajian ini.

## 5. Prioritas tindak lanjut yang diusulkan

| Prioritas | Tindakan | Penanggung jawab yang diusulkan | Bukti/hasil yang diharapkan |
|---|---|---|---|
| P1 | Kumpulkan RPS, CPMK/Sub-CPMK, matriks asesmen, bukti tugas dan aturan pilihan untuk seluruh U dan tiap jalur. | Kaprodi, koordinator kurikulum, pengampu | Inventaris versi dan tautan dokumen; daftar yang belum tersedia. |
| P1 | Rekonsiliasi Tabel 14, 15, 16, 18 dan matriks relasi yang belum diaudit; mulai dengan 35 set tambahan dan KOM-526. | RMK dan pengampu | Keputusan tertulis per MK/relasi, dengan alasan; tidak menghapus relasi otomatis. |
| P1 | Telusuri seluruh CS Core per knowledge unit ke MK, CPMK, indikator, materi, asesmen dan bukti per jalur. | RMK/penjaminan mutu | Matriks bukti yang menyatakan terbukti, parsial, tidak ditemukan atau belum diperiksa. |
| P2 | Reviu jalur grafika, AI, keamanan dan bahasa pemrograman serta ketergantungan pilihan tiap konsentrasi. | Koordinator konsentrasi | Peta minimum bersama dan pendalaman tiap jalur, tanpa perubahan SKS otomatis. |
| P2 | Pastikan versi tabel APTIKOM/CS2023 dan regulasi serta kebijakan institusi yang relevan. | Tim kurikulum/GPM | Daftar sumber primer dan keputusan versi yang disetujui. |
| P2 | Jalankan survei pada 007, laporkan n/kelompok dan bukti yang tersedia. | Tim tracer study | Hasil anonim, keterbatasan respons dan rekomendasi untuk rapat prodi. |
| P3 | Putuskan perbaikan materi, asesmen atau penempatan setelah audit dan survei; kaji dampak beban dan persetujuan. | RMK dan prodi | Notulen, versi revisi dan persetujuan sesuai prosedur. |

## 6. Status dan pemeriksaan

Belum ada respons survei atau wawancara. Tidak ada pernyataan bahwa 22 area atau 17 KA telah terpenuhi, ataupun skor kesiapan. Tidak semua butir dalam buku rujukan dibandingkan sampai level knowledge unit. Skrip `analisis_pemetaan.py --check` memeriksa 83 kode, status, 22 alias dan konsistensi berkas 005 dengan dua hash sumber; **tidak membuktikan validitas pemetaan akademik**.
