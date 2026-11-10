# 044 — Pemetaan Kurikulum dan Bahan Kajian per Klaster Ranting Ilmu (Kepakaran) terhadap CS2023 dan APTIKOM

> **Status: DRAF [U], belum disahkan.** Dokumen ini memetakan kurikulum Teknik Informatika UWG 2026 ke **tiga klaster ranting ilmu/kepakaran** yang sudah ada pada sumber (`Intelligent Multimedia`, `Data Science`, `Mobile Computing`) dan membandingkannya dengan **[CS2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)** dan **[APTIKOM Informatika v2.0](../BUKU_OBE/839193049-Buku-Kurikulum-Prodi-S1-Informatika-atau-Ilmu-Komputer-Versi-2-0-aptikom.pdf)**. Pembanding eksternal **tidak menggantikan** BoK UWG; keduanya dipakai sebagai cermin untuk menilai kelengkapan, bukan sebagai kewajiban prodi.
>
> Berkas pendukung: [001 CPL](001_CPL_TEKNIK_INFORMATIKA_07112026_0859.md) · [003 BoK UWG](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md) · [004 pemetaan MK–CPL–BK](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md) · [005 kandidat APTIKOM](005_PEMETAAN_APTIKOM_MK_INFORMATIKA_07112026_0910.md) · [006 analisis](006_ANALISIS_DAN_SURVEI_PUSTAKA_INFORMATIKA_07112026_0910.md) · [008 Tabel 4 APTIKOM](008_TABEL_4_RUMUSAN_BAHAN_KAJIAN_APTIKOM_INFORMATIKA_07112026_0942.md) · [011 indeks perangkat ajar](011_INDEKS_PERANGKAT_AJAR_INFORMATIKA_07112026_1328.md).

## 1. Ringkasan

| Klaster (nama pada sumber) | 3 MK wajib konsentrasi [S] | Ranting ilmu inti (usulan) | Padanan APTIKOM terdekat | Padanan CS2023 terdekat | Celah utama |
|---|---|---|---|---|---|
| **Intelligent Multimedia (IM)** | KFM-506, KFM-601, KFM-707 | Grafika–animasi–visi–media digital–interaksi imersif | APT-BK17 GIT, APT-BK18 AI, APT-BK09 HCI, APT-BK04 UX | GIT (4 CS Core / **70 KA Core** jam), HCI, AI-Vision, AI-NLP, SEP-IP | KA Core GIT sangat besar; media produksi belum tentu tercakup sebagai jam akademik; tidak ada MK etika media/hak cipta khusus |
| **Data Science (DS)** | KFD-506, KFD-601, KFD-707 | Statistika terapan–rekayasa data–analitik–ML–visualisasi | APT-BK06 DM, APT-BK18 AI, APT-BK20 MSF, APT-BK22 Metodologi | DM (10/**26**), MSF-Probability/Statistics (55/**145**), AI-ML, GIT-Visualization | Kedalaman statistika (KA Core MSF 145 jam) hanya ditopang 3 SKS Statistika; pilihan analitik tersebar di dua jalur |
| **Mobile Computing (MC)** | KFC-506, KFC-601, KFC-707 | Rekayasa aplikasi mobile–UX–sistem terdistribusi/cloud–jaringan–IoT–keamanan mobile | APT-BK19 SPD, APT-BK08 NC, APT-BK11 OS, APT-BK15 SF, APT-BK04 UX | SPD-Web/Mobile, PDC, NC-Mobility, OS-Virtualization, SEC-Coding, HCI | Beban KFC-506/KFC-601 beririsan dengan KOM-524; keamanan mobile hanya 1 MK pilihan; tidak ada MK khusus arsitektur aplikasi mobile lanjut |

Kesimpulan pokok (rincian di §7):

1. Ketiga klaster **bukan partisi yang saling lepas** — 5 MK pilihan dipakai bersama (KOM-625, KOM-626, KOM-627, KOM-729, KOM-730), dan semuanya bertumpu pada CPL04/UWG-BK02.
2. Ketiga klaster sudah punya **padanan yang jelas** di CS2023 (GIT untuk IM, DM+MSF+AI untuk DS, SPD+NC+OS untuk MC) dan di APTIKOM (Tabel 4 APTIKOM memang menyalin KA CS2023 menjadi BK, sehingga padanannya lebih rapat ke CS2023 daripada ke UWG-BK).
3. Yang **tidak punya padanan CS2023** justru kekuatan lokal UWG: **UWG-BK10 Manajemen Proyek dan Technopreneurship** (APT-BK03 + APT-BK21) dan **UWG-BK08 Riset dan Inovasi** (APT-BK22). Ini bukan celah.
4. Yang **relatif tipis terhadap kedua pembanding**: keamanan (CS2023 SEC 6 CS Core + 35 KA Core), statistika untuk DS, dan kedalaman GIT untuk IM. Ini butir keputusan, bukan kesalahan otomatis (§7).
5. **Kode `BK01…BK10` UWG dan `BK01…BK22` APTIKOM tidak boleh ditulis tanpa prefiks** — `BK01` UWG = Matematika, `BK01` APTIKOM = Society, Ethics and Professionalism. Dokumen ini memakai prefiks **`UWG-BK`**, **`APT-BK`**, dan **`BK-<klaster>`** untuk bahan kajian turunan.

## 2. Status bukti dan penandaan

| Tanda | Arti | Contoh dalam berkas ini |
|---|---|---|
| **[S]** | Tertulis pada sumber primer UWG (Buku KPT OBE TI UWG 2026, 11 Sep 2026) — nama klaster, kode MK, SKS, CPL, UWG-BK per MK (Tabel 15), CPL–BK (Tabel 14) | Tabel 3.1, §4 kolom [S] |
| **[K]** | Pembanding eksternal (CS2023 Jan 2024; APTIKOM Informatika v2.0). Bukan mandat prodi, bukan bukti bahwa MK UWG mengajarkan isi tersebut | Kolom CS2023/APTIKOM |
| **[K–tafsir]** | Padanan yang **saya turunkan dari judul MK dan ruang lingkup BK**, belum diverifikasi terhadap RPS/isi pertemuan | Seluruh kolom KA/KU di §4–§6 |
| **[U]** | Usulan/keputusan yang belum ada di sumber: prasyarat, kedalaman, bobot, penetapan klaster, penamaan | §7 |

Batasan yang harus dibaca sebelum memakai tabel:

- Pemetaan MK → knowledge unit CS2023 di §5–§6 adalah **tafsir judul**. CS2023 sendiri menuntut pengecekan *skill level* dan *illustrative learning outcomes* per unit; itu hanya bisa dilakukan pada RPS, yang belum ada untuk seluruh 83 MK.
- Angka jam **tidak dikonversi ke SKS** dan bobot APTIKOM (Min–Max) **tidak digabung** dengan CS Core/KA Core. Ketiganya unit yang berbeda.
- Tabel 15 sumber memuat 83 baris MK–BK; sebagian baris memberi BK yang lebih sempit daripada isi MK (contoh KFC-707 dan KFD-709, lihat §8.2). Kutipan [S] tetap dipertahankan apa adanya, dengan catatan.
- Struktur tiga klaster berasal dari §8.6 "Mata Kuliah Pilihan / Konsentrasi" dan Lampiran B Tabel 36–38. Label *"ranting ilmu/kepakaran"* adalah istilah pada permintaan ini, **bukan** istilah yang dipakai sumber; sumber menyebut *konsentrasi* dan *tiga jalur penguatan keilmuan*.

## 3. Kerangka klaster dan ranting ilmunya

### 3.1 Komposisi klaster [S]

Sumber menetapkan setiap mahasiswa mengambil **3 MK wajib konsentrasi (9 SKS)** dan **4 MK pilihan konsentrasi (12 SKS)** dari daftar Lampiran B — total 21 SKS jalur. Daftar pilihan memuat 10 MK per klaster, 5 bertanda `[pilihan ganjil]` dan 5 `[pilihan genap]`.

| Klaster | MK wajib [S] | SKS | Semester | CPL [S] | MK pilihan ganjil [S] | MK pilihan genap [S] |
|---|---|---|---|---|---|---|
| **IM** | KFM-506 Animasi Komputer dan Pemodelan 3D (+P) | 3 | 5 | CPL06 | KFM-708, KFM-709, KFM-710, KOM-729, KOM-730 | KFM-602, KFM-603, KOM-625, KOM-626, KOM-627 |
| | KFM-601 Fotografi dan Videografi (+P) | 3 | 6 | CPL06 | | |
| | KFM-707 Visi Komputer | 3 | 7 | CPL06 | | |
| **DS** | KFD-506 Analisis Data Multivariat (+P) | 3 | 5 | CPL05 | KFD-708, KFD-709, KFD-710, KFD-711, KOM-730 | KFD-602, KFD-603, KFD-604, KOM-625, KOM-626 |
| | KFD-601 Rekayasa Data dan Data Warehouse (+P) | 3 | 6 | CPL05 | | |
| | KFD-707 Metodologi dan Eksperimen Data Science | 3 | 7 | CPL09 | | |
| **MC** | KFC-506 Sistem Aplikasi Lintas Platform (+P) | 3 | 5 | CPL04 | KFC-708, KFC-709, KFC-710, KFC-711, KOM-729 | KFC-602, KFC-603, KFC-604, KFC-605, KOM-627 |
| | KFC-601 Sistem Aplikasi Mobile (+P) | 3 | 6 | CPL04, CPL07 | | |
| | KFC-707 Desain Pengalaman Pengguna (UX) | 3 | 7 | CPL04 | | |

Catatan struktur [S]:

- **IM adalah satu-satunya klaster yang seluruh MK wajibnya ber-CPL06.** Akibatnya CPL06 pada jalur IM ditanggung 9 SKS wajib + sekurang-kurangnya 12 SKS pilihan, sementara CPL05/CPL04 hanya lewat pilihan. Sebaliknya **DS tidak menyentuh CPL06 sama sekali pada MK wajib**, dan **MC tidak menyentuh CPL05** pada MK wajib.
- **KFD-707 satu-satunya MK wajib konsentrasi ber-CPL09** (riset), sehingga jalur DS bergantung pada BK08/UWG-BK08 untuk capaian metodologinya.
- Irisan antar klaster [S]: KOM-729 (IM, MC), KOM-730 (IM, DS), KOM-625 (IM, DS), KOM-626 (IM, DS), KOM-627 (IM, MC). **Tidak ada MK pilihan yang dipakai ketiga klaster.**
- Kode MK pilihan memakai prefiks konsentrasi (KFM/KFD/KFC) tetapi KOM-625/626/627/729/730 tidak — konsisten dengan sifat berbagi di atas.

### 3.2 Ranting ilmu per klaster (usulan **[U]**, diturunkan dari isi MK [S])

Pembagian berikut mengelompokkan MK yang sudah ada; ia **tidak menambah MK** dan **tidak menetapkan** bahwa setiap ranting harus punya MK wajib.

| Klaster | Ranting ilmu (usulan) | MK pada ranting tersebut | CPL dominan |
|---|---|---|---|
| **IM** | IM-a Grafika, animasi dan pemodelan 3D | KFM-506 | CPL06 |
| | IM-b Produksi media digital (fotografi, videografi) | KFM-601 | CPL06 |
| | IM-c Pengolahan citra dan visi komputer | KOM-525, KFM-707 | CPL06 |
| | IM-d Pengolahan sinyal multimedia dan biometrika | KFM-708, KFM-709 | CPL06 |
| | IM-e Interaksi imersif, game dan gamifikasi | KOM-628, KOM-729, KOM-627 | CPL04, CPL06 |
| | IM-f Multimedia spasial/geospasial | KFM-710 | CPL06 |
| | IM-g Kecerdasan untuk media (NLP, deep learning, fuzzy, optimasi) | KOM-625, KOM-626, KFM-602, KOM-730 | CPL05, CPL06 |
| | IM-h Informatika biomedis | KFM-603 | CPL06 |
| **DS** | DS-a Fondasi matematika dan statistika terapan | KOM-103, KOM-201, KOM-202, KOM-316, FST-408 | CPL03 |
| | DS-b Rekayasa data dan gudang data | FST-207, KFD-601 | CPL05 |
| | DS-c Analitik multivariat dan eksperimen | KFD-506, KFD-707 | CPL05, CPL09 |
| | DS-d Big data dan temu kembali informasi | KFD-602, KFD-603 | CPL05, CPL06 |
| | DS-e Pembelajaran mesin dan sistem cerdas | KOM-527, KOM-629, KOM-626, KFD-711 | CPL05 |
| | DS-f Peramalan dan optimasi | KFD-604, KOM-730 | CPL05 |
| | DS-g Visualisasi dan komunikasi data | KFD-709 | CPL05 |
| | DS-h Analitik jejaring dan spasial | KFD-708, KFD-710 | CPL06 |
| | DS-i Metodologi penelitian data science | KFD-707, FST-611, FST-613, FST-713 | CPL09 |
| **MC** | MC-a Aplikasi lintas platform dan web | KOM-312, KOM-524, KOM-526, KFC-506 | CPL04 |
| | MC-b Rekayasa aplikasi mobile | KFC-601 | CPL04, CPL07 |
| | MC-c UX dan desain interaksi | KOM-419, KFC-707 | CPL04 |
| | MC-d Game dan media interaktif bergerak | KFC-710, KOM-627, KOM-729 | CPL04, CPL06, CPL07 |
| | MC-e Komputasi terdistribusi dan cloud | KOM-315, KFC-711 | CPL07 |
| | MC-f Jaringan nirkabel, sensor dan IoT | KOM-314, KFC-603, KFC-708 | CPL07 |
| | MC-g Keamanan dan privasi perangkat mobile | KOM-631, KFC-602 | CPL07, CPL08 |
| | MC-h Sistem cerdas tertanam dan kota cerdas | KFC-604, KFC-709, KFC-605 | CPL05, CPL07 |

Catatan: **DS-a, MC-a, MC-c, IM-e berisi MK wajib kurikulum, bukan MK konsentrasi** — ranting ilmu karena itu tidak identik dengan "MK berprefiks KF*". Ini penting agar pemetaan tidak dibaca sebagai usulan menambah SKS.

## 4. Bahan Kajian per klaster (rumusan turunan)

Rumusan di bawah adalah **usulan bahan kajian tingkat klaster [U]**, disusun agar setiap klaster punya daftar bahan kajian yang lebih rinci daripada 10 UWG-BK, tetapi tetap dapat dilacak ke CPL dan MK yang sudah ada. Kolom APTIKOM/CS2023 adalah **[K–tafsir]**.

### 4.1 Klaster Intelligent Multimedia — 8 bahan kajian

| Kode | Rumusan bahan kajian | Cakupan topik | MK pengampu [S] | CPL [S] | UWG-BK [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|---|
| BK-IM-01 | Prinsip grafika komputer, pemodelan geometri 3D, dan animasi | Pipeline grafika, transformasi, kurva/permukaan, mesh, rigging, keyframe, rendering dasar | KFM-506 | CPL06 | BK04, BK05 | APT-BK17 | GIT-Fundamentals, GIT-Modeling, GIT-Animation, GIT-Shading |
| BK-IM-02 | Produksi media digital: fotografi, videografi, dan estetika visual | Komposisi, pencahayaan, color grading, alur produksi, penyuntingan, distribusi | KFM-601 | CPL06 | BK04, BK05 | APT-BK17 | GIT-Rendering, GIT-Immersion (parsial), SEP-IP |
| BK-IM-03 | Pengolahan citra dan visi komputer | Representasi citra, filter, segmentasi, ekstraksi fitur, deteksi/pengenalan, evaluasi model visi | KOM-525, KFM-707 | CPL06 | BK04, BK05 | APT-BK17, APT-BK18 | GIT-Image, AI-Vision |
| BK-IM-04 | Pengolahan sinyal multimedia dan biometrika | Sampling/kuantisasi, transformasi, kompresi, fitur biometrik, akurasi dan spoofing | KFM-708, KFM-709 | CPL06 | BK04, BK05 | APT-BK17, APT-BK18 | GIT-Image, AI-Vision, SEC-Foundations (parsial) |
| BK-IM-05 | Interaksi imersif, game, dan gamifikasi | VR/AR, interaksi 3D, desain mekanika game, playtesting, gamifikasi non-game | KOM-628, KOM-729, KOM-627 | CPL04, CPL06 | BK02, BK04, BK05 | APT-BK17, APT-BK09 | GIT-Interaction, GIT-Immersion, HCI-Design, SPD-Game |
| BK-IM-06 | Multimedia spasial dan geospasial | Sistem koordinat, raster/vektor, metadata, visualisasi peta, analitik spasial multimedia | KFM-710 | CPL06 | BK04, BK05 | APT-BK17, APT-BK06 | GIT-Visualization, DM-Unstructured |
| BK-IM-07 | Kecerdasan buatan untuk media | NLP, deep learning, logika fuzzy, optimasi evolusioner untuk konten dan fitur media | KOM-625, KOM-626, KFM-602, KOM-730 | CPL02, CPL05, CPL06 | BK03, BK04, BK05, BK09 | APT-BK18 | AI-NLP, AI-ML, AI-Probability, AI-KRR |
| BK-IM-08 | Informatika biomedis dan bioinformatika | Sekuens, basis data biologi, analitik sinyal medis, etika data kesehatan | KFM-603 | CPL06 | BK04, BK05 | APT-BK18 | AI-ML (terapan), DM-Data |

### 4.2 Klaster Data Science — 9 bahan kajian

| Kode | Rumusan bahan kajian | Cakupan topik | MK pengampu [S] | CPL [S] | UWG-BK [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|---|
| BK-DS-01 | Fondasi matematika dan statistika untuk analitik data | KALKULUS, aljabar linear, diskrit, peluang, statistika inferensial, numerik | KOM-103, KOM-201, KOM-202, KOM-316, FST-408 | CPL03 | BK01 | APT-BK20 | MSF-Calculus, MSF-Linear, MSF-Discrete, MSF-Probability, MSF-Statistics |
| BK-DS-02 | Rekayasa data dan gudang data | Pemodelan dimensional, ETL/ELT, skema bintang, kualitas data, tata kelola data | FST-207, KFD-601 | CPL05 | BK03 | APT-BK06 | DM-Data, DM-Core, DM-Modeling, DM-Processing, DM-Internals |
| BK-DS-03 | Analitik multivariat dan rancangan eksperimen | PCA/faktor, klaster, MANOVA, uji hipotesis, validitas, replikasi | KFD-506, KFD-707 | CPL05, CPL09 | BK03, BK08 | APT-BK06, APT-BK20, APT-BK22 | MSF-Statistics, DM-Analytics, SDF-Practices |
| BK-DS-04 | Big data dan temu kembali informasi | Penyimpanan terdistribusi, NoSQL, pemrosesan aliran, indeks dan peringkat, evaluasi IR | KFD-602, KFD-603 | CPL05, CPL06 | BK03, BK04, BK05 | APT-BK06, APT-BK07 | DM-NoSQL, DM-Distributed, DM-Unstructured, DM-Querying |
| BK-DS-05 | Pembelajaran mesin dan sistem cerdas | Supervised/unsupervised, deep learning, representasi, rekomendasi, evaluasi model | KOM-527, KOM-629, KOM-626, KFD-711 | CPL05 | BK03, BK04, BK05 | APT-BK18 | AI-ML, AI-Probability, AI-KRR, AI-Agents |
| BK-DS-06 | Peramalan dan optimasi | Deret waktu, stasioneritas, ARIMA/ETS, optimasi evolusioner, tuning | KFD-604, KOM-730 | CPL05 | BK03 | APT-BK18, APT-BK20 | MSF-Probability, AI-Probability, AL-Strategies |
| BK-DS-07 | Visualisasi dan komunikasi data | Tata kelola visual, persepsi, dashboards, narasi data, aksesibilitas | KFD-709 | CPL05 | BK03 | APT-BK17, APT-BK09 | GIT-Visualization, HCI-Design, SEP-Communication |
| BK-DS-08 | Analitik jejaring dan data spasial | Graf sosial, metrik sentralitas, deteksi komunitas, statistik spasial | KFD-708, KFD-710 | CPL06 | BK04, BK05 | APT-BK06, APT-BK18 | DM-Unstructured, GIT-Visualization, AI-ML (terapan) |
| BK-DS-09 | Metodologi penelitian dan pelaporan data science | Perumusan masalah, etika data, privasi, reproducibility, publikasi | KFD-707, FST-611, FST-613, FST-713 | CPL09 | BK08 | APT-BK22 | SEP-Professional-Ethics, SEP-Privacy, SF-Evaluation |

### 4.3 Klaster Mobile Computing — 8 bahan kajian

| Kode | Rumusan bahan kajian | Cakupan topik | MK pengampu [S] | CPL [S] | UWG-BK [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|---|
| BK-MC-01 | Pengembangan aplikasi lintas platform dan web | Arsitektur klien-server, state management, API, build/release, uji perangkat | KOM-312, KOM-524, KOM-526, KFC-506 | CPL04 | BK02, BK06 | APT-BK19, APT-BK05, APT-BK14 | SPD-Common, SPD-Web, SPD-Mobile, SDF-Practices |
| BK-MC-02 | Arsitektur dan rekayasa aplikasi mobile | Pola arsitektur mobile, offline-first, sinkronisasi, kinerja, distribusi | KFC-601 | CPL04, CPL07 | BK02, BK06 | APT-BK19, APT-BK10 | SPD-Mobile, SE-Design, SE-Construction, SE-Validation |
| BK-MC-03 | UX dan desain interaksi | Riset pengguna, persona, wireframe, prototipe, evaluasi usability, aksesibilitas | KOM-419, KFC-707 | CPL04 | BK02 | APT-BK04, APT-BK09 | HCI-User, HCI-Design, HCI-Evaluation, HCI-Accessibility, HCI-Accountability |
| BK-MC-04 | Game mobile dan media interaktif | Game loop, fisika, aset, monetisasi, performa perangkat, XR | KFC-710, KOM-627, KOM-729 | CPL04, CPL06, CPL07 | BK02, BK04, BK05, BK06 | APT-BK17, APT-BK19 | SPD-Game, GIT-Interaction, GIT-Immersion, GIT-Animation |
| BK-MC-05 | Komputasi terdistribusi dan cloud | Model paralel, konsistensi, container, orkestrasi, elastisitas, biaya | KOM-315, KFC-711 | CPL07 | BK06 | APT-BK07, APT-BK19 | PDC-Programs, PDC-Communication, PDC-Coordination, PDC-Evaluation, OS-Virtualization |
| BK-MC-06 | Jaringan nirkabel, sensor, dan IoT | Protokol MAC/routing, LPWAN, edge, manajemen energi, arsitektur IoT | KOM-314, KFC-603, KFC-708 | CPL07 | BK06 | APT-BK08, APT-BK15, APT-BK19 | NC-Mobility, NC-SingleHop, NC-Routing, SF-Resource, SPD-Embedded |
| BK-MC-07 | Keamanan dan privasi perangkat mobile | Model ancaman, penyimpanan aman, otentikasi, OWASP Mobile, kepatuhan privasi | KOM-631, KFC-602 | CPL07, CPL08 | BK06, BK07 | APT-BK02, APT-BK08 | SEC-Foundations, SEC-Coding, SEC-Governance, NC-Security |
| BK-MC-08 | Sistem cerdas pada perangkat dan kota cerdas | Agen, sistem pakar, penalaran, perencanaan, integrasi layanan kota | KFC-604, KFC-709, KFC-605 | CPL05, CPL07 | BK03, BK06 | APT-BK18, APT-BK19 | AI-KRR, AI-Agents, AI-Planning, SF-Design |

### 4.4 Bahan kajian lintas klaster (wajib bagi semua jalur)

| Kode | Rumusan bahan kajian | MK pengampu [S] | CPL [S] | UWG-BK [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|
| BK-L-01 | Algoritma, struktur data, dan pemrograman | FST-102, FST-203, KOM-311 | CPL04 | BK02 | APT-BK05, APT-BK12, APT-BK14 | SDF-Fundamentals, SDF-Data-Structures, SDF-Algorithms, AL-Foundational |
| BK-L-02 | Rekayasa perangkat lunak dan manajemen proyek | KOM-313, KOM-417, KOM-317, FST-610 | CPL01, CPL04, CPL08, CPL10 | BK02, BK07, BK09, BK10 | APT-BK03, APT-BK10 | SE-Requirements, SE-Design, SE-Validation, SE-Teamwork, SEP-Economies |
| BK-L-03 | Etika, hukum digital, keamanan, dan privasi | FST-206, KOM-631, MKU-101, MKU-102, MKU-405 | CPL01, CPL07, CPL08 | BK07 | APT-BK01, APT-BK02 | SEP-Context, SEP-Professional-Ethics, SEP-Privacy, SEC-Foundations |
| BK-L-04 | Riset, inovasi, dan komunikasi ilmiah | FST-611, FST-613, FST-713, MKU-103, FST-205, FST-409 | CPL02, CPL09 | BK08, BK09 | APT-BK22, APT-BK21 | SEP-Communication, SEP-History, SE-Tools |
| BK-L-05 | Kewirausahaan teknologi dan dampak sosial komputasi | MKU-204, MKU-508, MKU-507, FST-612 | CPL02, CPL10 | BK09, BK10 | APT-BK21, APT-BK03 | SEP-Economies, SEP-Sustainability, SEP-DEIA |

## 5. Pemetaan kurikulum: MK × klaster × dua pembanding

Kolom **UWG-BK [S]** disalin dari Tabel 15. Kolom **APT-BK** dan **CS2023 KU** adalah **[K–tafsir]** tingkat judul MK.

### 5.1 Klaster Intelligent Multimedia

| MK [S] | SKS | CPL [S] | UWG-BK [S] | APT-BK [K] | CS2023 KA/KU [K] | BK-klaster |
|---|---|---|---|---|---|---|
| KFM-506 Animasi Komputer dan Pemodelan 3D (+P) | 3 | CPL06 | BK04, BK05 | 17 | GIT-Modeling, GIT-Animation | BK-IM-01 |
| KFM-601 Fotografi dan Videografi (+P) | 3 | CPL06 | BK04, BK05 | 17 | GIT-Rendering, GIT-Immersion, SEP-IP | BK-IM-02 |
| KFM-707 Visi Komputer | 3 | CPL06 | BK04, BK05 | 17, 18 | GIT-Image, AI-Vision | BK-IM-03 |
| KFM-708 Pengolahan Sinyal Multimedia | 3 | CPL06 | BK04, BK05 | 17, 20 | GIT-Image, MSF-Linear | BK-IM-04 |
| KFM-709 Sistem Biometrika | 3 | CPL06 | BK04, BK05 | 17, 02 | GIT-Image, AI-Vision, SEC-Foundations | BK-IM-04 |
| KFM-710 Multimedia Geospasial | 3 | CPL06 | BK04, BK05 | 17, 06 | GIT-Visualization, DM-Unstructured | BK-IM-06 |
| KOM-729 Virtual dan Augmented Reality | 3 | CPL06 | BK04, BK05 | 17, 19 | GIT-Interaction, GIT-Immersion, SPD-Interactive | BK-IM-05 |
| KOM-730 Optimasi Evolusioner | 3 | CPL05 | BK03 | 18, 12 | AI-Probability, AL-Strategies | BK-IM-07 |
| KFM-602 Komputasi Berbasis Logika Fuzzy | 3 | CPL05 | BK03 | 18 | AI-KRR, AI-Probability | BK-IM-07 |
| KFM-603 Bioinformatika | 3 | CPL06 | BK04, BK05 | 18 | AI-ML (terapan), DM-Data | BK-IM-08 |
| KOM-625 Pemrosesan Bahasa Alami | 3 | CPL02, CPL06 | BK04, BK05, BK09 | 18 | AI-NLP | BK-IM-07 |
| KOM-626 Deep Learning | 3 | CPL05 | BK03 | 18 | AI-ML, AI-Vision | BK-IM-07 |
| KOM-627 Desain dan Pemrograman Game | 3 | CPL04 | BK02 | 17, 19 | SPD-Game, GIT-Interaction, SE-Construction | BK-IM-05 |

### 5.2 Klaster Data Science

| MK [S] | SKS | CPL [S] | UWG-BK [S] | APT-BK [K] | CS2023 KA/KU [K] | BK-klaster |
|---|---|---|---|---|---|---|
| KFD-506 Analisis Data Multivariat (+P) | 3 | CPL05 | BK03 | 06, 20 | MSF-Statistics, DM-Analytics | BK-DS-03 |
| KFD-601 Rekayasa Data dan Data Warehouse (+P) | 3 | CPL05 | BK03 | 06 | DM-Data, DM-Modeling, DM-Processing, DM-Internals | BK-DS-02 |
| KFD-707 Metodologi dan Eksperimen Data Science | 3 | CPL09 | BK08 | 22, 20 | MSF-Statistics, SDF-Practices | BK-DS-09 |
| KFD-708 Analisis Jejaring Sosial | 3 | CPL06 | BK04, BK05 | 06, 18 | DM-Unstructured, AI-ML (terapan) | BK-DS-08 |
| KFD-709 Visualisasi Data | 3 | CPL05 | BK03 | 17, 09 | GIT-Visualization, HCI-Design | BK-DS-07 |
| KFD-710 Analitik Data Geospasial | 3 | CPL06 | BK04, BK05 | 06, 17 | GIT-Visualization, DM-Unstructured | BK-DS-08 |
| KFD-711 Sistem Rekomendasi | 3 | CPL06 | BK04, BK05 | 18 | AI-ML, AI-Agents | BK-DS-05 |
| KOM-730 Optimasi Evolusioner | 3 | CPL05 | BK03 | 18, 12 | AI-Probability, AL-Strategies | BK-DS-06 |
| KFD-602 Information Retrieval | 3 | CPL06 | BK04, BK05 | 06, 18 | DM-Querying, DM-Unstructured, AI-NLP | BK-DS-04 |
| KFD-603 Big Data Analytic | 3 | CPL05 | BK03 | 06, 07 | DM-NoSQL, DM-Distributed, DM-Internals | BK-DS-04 |
| KFD-604 Analisis Deret Waktu dan Peramalan | 3 | CPL05 | BK03 | 20, 18 | MSF-Probability, AI-Probability | BK-DS-06 |
| KOM-625 Pemrosesan Bahasa Alami | 3 | CPL02, CPL06 | BK04, BK05, BK09 | 18 | AI-NLP | BK-DS-04 |
| KOM-626 Deep Learning | 3 | CPL05 | BK03 | 18 | AI-ML | BK-DS-05 |

### 5.3 Klaster Mobile Computing

| MK [S] | SKS | CPL [S] | UWG-BK [S] | APT-BK [K] | CS2023 KA/KU [K] | BK-klaster |
|---|---|---|---|---|---|---|
| KFC-506 Sistem Aplikasi Lintas Platform (+P) | 3 | CPL04 | BK02 | 19, 05 | SPD-Common, SPD-Mobile, SPD-Web, SDF-Practices | BK-MC-01 |
| KFC-601 Sistem Aplikasi Mobile (+P) | 3 | CPL04, CPL07 | BK02, BK06 | 19, 10 | SPD-Mobile, SE-Design, SE-Construction, AR-Organization | BK-MC-02 |
| KFC-707 Desain Pengalaman Pengguna (UX) | 3 | CPL04 | BK02 | 04, 09 | HCI-User, HCI-Design, HCI-Evaluation, HCI-Accessibility | BK-MC-03 |
| KFC-708 Internet of Things | 3 | CPL07 | BK06 | 08, 15, 19 | NC-Mobility, SF-Resource, SPD-Embedded | BK-MC-06 |
| KFC-709 Komputasi Berbasis Agen | 3 | CPL05 | BK03 | 18 | AI-Agents, AI-KRR | BK-MC-08 |
| KFC-710 Mobile Game | 3 | CPL04, CPL07 | BK02, BK06 | 17, 19 | SPD-Game, GIT-Interaction, AR-Performance-Energy | BK-MC-04 |
| KFC-711 Cloud Computing | 3 | CPL07 | BK06 | 07, 19 | OS-Virtualization, PDC-Evaluation, SPD-Common | BK-MC-05 |
| KOM-729 Virtual dan Augmented Reality | 3 | CPL06 | BK04, BK05 | 17, 19 | GIT-Immersion, SPD-Interactive | BK-MC-04 |
| KFC-602 Keamanan Perangkat Mobile | 3 | CPL07, CPL08 | BK06, BK07 | 02, 08 | SEC-Coding, SEC-Foundations, SEC-Governance | BK-MC-07 |
| KFC-603 Jaringan Sensor Nirkabel | 3 | CPL07 | BK06 | 08, 15 | NC-SingleHop, NC-Routing, SF-Resource | BK-MC-06 |
| KFC-604 Expert System | 3 | CPL05 | BK03 | 18 | AI-KRR, AI-LRR | BK-MC-08 |
| KFC-605 Smart City | 3 | CPL07 | BK06 | 19, 08 | SF-Design, NC-Applications, SEP-Sustainability | BK-MC-08 |
| KOM-627 Desain dan Pemrograman Game | 3 | CPL04 | BK02 | 17, 19 | SPD-Game, GIT-Interaction | BK-MC-04 |

### 5.4 Cakupan BK APTIKOM per klaster (dihitung dari tabel di atas)

Hitungan berikut dihitung langsung dari kolom **APT-BK [K]** pada §5.1–§5.3; ia mengukur **jangkauan judul MK**, bukan kepatuhan.

| Klaster | Jumlah BK APTIKOM tersentuh | Kode yang tersentuh | Kode yang tidak tersentuh |
|---|---:|---|---|
| **IM** | 7 dari 22 | 02, 06, 12, 17, 18, 19, 20 | 01, 03, 04, 05, 07, 08, 09, 10, 11, 13, 14, 15, 16, 21, 22 |
| **DS** | 8 dari 22 | 06, 07, 09, 12, 17, 18, 20, 22 | 01, 02, 03, 04, 05, 08, 10, 11, 13, 14, 15, 16, 19, 21 |
| **MC** | 11 dari 22 | 02, 04, 05, 07, 08, 09, 10, 15, 17, 18, 19 | 01, 03, 06, 11, 12, 13, 14, 16, 20, 21, 22 |

Tujuh BK yang **tidak tersentuh ketiga klaster** adalah APT-BK01 Society/Ethics, APT-BK03 Project Management, APT-BK11 Operating Systems, APT-BK13 Foundations of Programming Languages, APT-BK14 Programming Fundamentals, APT-BK16 Architecture & Organization, dan APT-BK21 Pengembangan Diri. Semuanya ditanggung **MK wajib non-konsentrasi** (BK-L-01, BK-L-02, BK-L-03, BK-L-05), sehingga **tidak boleh disimpulkan bahwa klaster tidak mencakup etika, OS, atau arsitektur**. Klaster adalah pendalaman di atas kurikulum inti, bukan pengganti.

Dua hal yang menonjol dari tabel ini [U]:

- **MC paling lebar (11 BK), IM paling sempit (7 BK)** meskipun IM punya KA Core GIT terbesar (70 jam) di CS2023. Artinya IM sangat terkonsentrasi pada GIT/AI dan tipis pada spektrum APTIKOM, sedangkan MC tersebar dan berpotensi kurang fokus.
- **APT-BK06 Data Management tidak tersentuh MC sama sekali** dan **APT-BK19 SPD tidak tersentuh DS** — wajar secara akademik, tetapi keduanya membuat "Mobile Computing" dan "Data Science" tidak saling silang pada jalur pilihan (kecuali KOM-625/626/627/729/730 yang generik).

## 6. Pemetaan kurikulum inti ke CS2023 (17 knowledge area)

Data jam **[K]** dari Tabel 2 laporan CS2023; MK pengampu **[S]** dari Tabel 15/18; status **[K–tafsir]** berdasarkan judul MK, bukan audit RPS.

| CS2023 KA | CS Core | KA Core | MK pengampu di kurikulum UWG [S] | Status [K–tafsir] |
|---|---:|---:|---|---|
| AI Artificial Intelligence | 12 | 18 | FST-204, KOM-527, KOM-629, KOM-625, KOM-626, KFM-602, KFC-604 | tercakup, kuat pada pilihan |
| AL Algorithmic Foundations | 32 | 32 | FST-102, FST-203, KOM-201, KOM-630, KOM-316 | tercakup |
| AR Architecture and Organization | 9 | 16 | KOM-102, FST-101, KOM-310 | tercakup tipis (7 SKS, 2 di antaranya 2 SKS) |
| DM Data Management | 10 | 26 | FST-207, KOM-523, KFD-601, KFD-603 | CS Core tercakup; KA Core hanya di jalur DS |
| FPL Foundations of Programming Languages | 21 | 19 | KOM-311, KOM-418, KOM-630 | CS Core berpeluang kurang: tidak ada MK khusus konsep bahasa |
| GIT Graphics and Interactive Techniques | 4 | 70 | KOM-525, KFM-506, KFM-601, KFM-707 (+pilihan IM) | KA Core hanya di jalur IM; lihat §8.1 |
| HCI Human-Computer Interaction | 8 | 16 | KOM-419, KFC-707, KOM-628 | tercakup |
| MSF Mathematical and Statistical Foundations | 55 | 145 | KOM-103, KOM-201, KOM-202, KOM-316, FST-408 | CS Core kemungkinan tertutup (14 SKS); KA Core statistika tipis |
| NC Networking and Communication | 7 | 24 | KOM-314, KFC-603, KFC-708 | CS Core tercakup; KA Core di jalur MC |
| OS Operating Systems | 8 | 13 | KOM-420 | tercakup |
| PDC Parallel and Distributed Computing | 9 | 26 | KOM-315, KFC-711 | tercakup |
| SDF Software Development Fundamentals | 43 | — | FST-102, FST-203, KOM-311, KOM-312, KOM-418 (+P) | tercakup lewat banyak MK dan praktikum |
| SE Software Engineering | 6 | 21 | KOM-313, KOM-417, KOM-317, FST-610 | tercakup |
| SEC Security | 6 | 35 | KOM-631, FST-206, KFC-602 | CS Core berpeluang kurang; KA Core sangat tipis |
| SEP Society, Ethics, and the Profession | 18 | 14 | MKU-101, MKU-102, MKU-405, FST-206, KOM-317, FST-612, MKU-507 | tercakup, tersebar |
| SF Systems Fundamentals | 18 | 8 | KOM-102, FST-101, KOM-310, KOM-420 | tercakup |
| SPD Specialized Platform Development | 4 | — | KOM-312, KOM-524, KOM-526, KFC-506, KFC-601, KFC-708 | tercakup, kuat |

Angka **CS Core total 270 jam** pada Tabel 2 CS2023. UWG tidak menghitung jam kuliah per topik, sehingga tabel di atas **tidak dapat** diterjemahkan menjadi "UWG memenuhi X% CS2023". Yang dapat dikatakan: **setiap KA CS2023 punya MK pengampu berjudul relevan**, dan **dua KA (GIT, DM) mencapai kedalaman KA Core hanya melalui jalur konsentrasi** — konsekuensi desain kurikulum berbasis konsentrasi, bukan cacat.

## 7. Keterlacakan CPL → klaster → BK-klaster

| CPL [S] | UWG-BK utama [S] | Jalur yang menanggung | BK-klaster terkait | Catatan [U] |
|---|---|---|---|---|
| CPL01 | BK07, BK09 | semua (MKU, FST-206, KOM-317) | BK-L-02, BK-L-03 | tidak ada di MK konsentrasi mana pun |
| CPL02 | BK09 | semua (MKU-103, FST-205, FST-409) + KOM-625 | BK-L-04 | hanya satu MK konsentrasi ber-CPL02 (KOM-625, dua jalur) |
| CPL03 | BK01 | semua (KOM-103, KOM-201, KOM-202, KOM-316, FST-408) | BK-DS-01 | **tidak ada MK konsentrasi ber-CPL03** |
| CPL04 | BK02 | KOM-311/312/418/419/526, KFC-506/601/707, KOM-627 | BK-L-01, BK-MC-01/02/03/04 | CPL04 paling sering dibebankan; risiko duplikasi asesmen |
| CPL05 | BK03 | KOM-523/527/629, KFD-506/601/707, KFD-709/603/604, KFC-604/709 | BK-DS-02/03/05/06/07, BK-IM-07 | inti jalur DS dan sebagian IM |
| CPL06 | BK04, BK05 | KOM-525/628, KFM-506/601/707, KFD-708/710, KFC-710 | BK-IM-01…08, BK-DS-07/08, BK-MC-04 | seluruh MK wajib IM ber-CPL06 |
| CPL07 | BK06 | KOM-310/314/315/420, KFC-601/708/711/603/605/602 | BK-MC-05/06/07/08 | inti jalur MC |
| CPL08 | BK07 | KOM-631, FST-206, KFC-602 | BK-MC-07, BK-L-03 | hanya satu MK konsentrasi ber-CPL08 |
| CPL09 | BK08 | FST-611/613/713, KFD-707 | BK-DS-09, BK-L-04 | hanya satu MK konsentrasi ber-CPL09 |
| CPL10 | BK09, BK10 | MKU-204/508/507, KOM-317, FST-610/612 | BK-L-02, BK-L-05 | **tidak ada MK konsentrasi ber-CPL10** |

Pola yang perlu diputuskan prodi [U]: **CPL03 dan CPL10 tidak pernah menjadi CPL langsung MK konsentrasi mana pun**, dan CPL02/CPL08/CPL09 hanya sekali. Jika konsentrasi dimaksudkan sebagai wahana pendalaman yang tetap menanggung capaian lulusan secara seimbang, komposisi CPL per jalur perlu ditinjau (lihat U-04).

## 8. Temuan, celah, dan risiko

### 8.1 Celah terhadap pembanding eksternal

| # | Temuan | Bukti | Tingkat |
|---|---|---|---|
| G-01 | **GIT KA Core 70 jam** — KA dengan KA Core terbesar ketiga di CS2023 — hanya dilayani penuh pada jalur IM; mahasiswa DS/MC hanya mendapat KOM-525 (3 SKS) dan pilihan terbatas | CS2023 Tabel 2; Tabel 18 | Sedang — sesuai desain konsentrasi |
| G-02 | **MSF KA Core 145 jam** (terbesar) vs 14 SKS matematika/statistika wajib; statistika hanya 3 SKS (FST-408) | CS2023 Tabel 2; Tabel 18 | Tinggi untuk DS |
| G-03 | **SEC KA Core 35 jam** vs 2 SKS KOM-631 + 2 SKS FST-206; keamanan mobile hanya 1 MK pilihan (KFC-602, genap) | CS2023 Tabel 2; Lampiran B | Sedang-tinggi (mobility ke CPL08) |
| G-04 | **FPL 21 CS Core jam** hanya lewat KOM-311 dan KOM-630; tidak ada MK konsep bahasa pemrograman/kompilasi | CS2023 Tabel 2; Tabel 18 | Sedang |
| G-05 | **AR 9 CS Core jam** dilayani KOM-102 (2 SKS), FST-101 (2 SKS), KOM-310 (2 SKS) = 6 SKS | Tabel 18 | Sedang |
| G-06 | APTIKOM menyarankan **maksimal dua peminatan**; UWG menetapkan tiga | 006 §73 | Kebijakan [U], bukan pelanggaran |

### 8.2 Ketidakkonsistenan internal sumber [S] vs [S]

Ini bukan salah kutip: Tabel 15 memberi UWG-BK yang lebih sempit daripada ruang lingkup UWG-BK itu sendiri (Tabel 13).

| MK | UWG-BK pada Tabel 15 | Isi yang tampak dari judul | Usulan [U] |
|---|---|---|---|
| KFC-707 Desain Pengalaman Pengguna (UX) | BK02 | UX secara eksplisit tercantum pada ruang lingkup **BK04** (Tabel 13) dan HCI pada CS2023 | tinjau menjadi BK02, BK04 |
| KOM-419 Interaksi Manusia dan Komputer | BK02 | idem | tinjau menjadi BK02, BK04 |
| KFD-709 Visualisasi Data | BK03 | visualisasi berada pada GIT/HCI di CS2023; BK04 memuat "interaksi digital" | tinjau menjadi BK03, BK04 |
| KOM-527 Sistem Kecerdasan Buatan | BK03 saja | AI tersebar di BK03 dan BK05 | tinjau menjadi BK03, BK05 |
| KOM-526 Sistem Aplikasi Web | BK02–BK08 (7 BK) | jangkauan BK paling luas di seluruh Tabel 15 | periksa ulang; 7 BK untuk 3 SKS sulit dipertanggungjawabkan |
| KOM-630 Teori Bahasa dan Automata | BK09, BK01 | BK09 (komunikasi) tidak lazim untuk automata | tinjau menjadi BK01 (+BK02) |

Catatan metode: Tabel 15 adalah **salinan tiga kali identik dari 83 baris** pada sumber; tidak ada versi alternatif yang bisa dipakai sebagai pembanding internal.

### 8.3 Risiko implementasi per klaster

| Klaster | Risiko | Dampak | Mitigasi yang mungkin [U] |
|---|---|---|---|
| IM | Beban produksi media (KFM-601) sulit dinilai secara akademik dan padat peralatan | Mutu asesmen tidak seragam antar kelas | Tetapkan hasil karya + rubrik portofolio; batasi cakupan praktik pada kompetensi yang dapat diuji |
| IM | Tumpang tindih KOM-525 (wajib, sem 5) dengan KFM-707 (wajib IM, sem 7) pada visi komputer | Duplikasi materi dan asesmen | Bedakan: KOM-525 = pengolahan citra dasar; KFM-707 = visi komputer + evaluasi model |
| DS | Statistika hanya 3 SKS sebelum KFD-506/KFD-604 | Mahasiswa gagal di kedalaman KA Core MSF | Prasyarat eksplisit + modul penyegaran; lihat U-05 |
| DS | KFD-707 ber-CPL09 saja, tanpa CPL teknis | MK metodologi dianggap "ringan" | Tambahkan capaian teknis pada CPMK; lihat U-06 |
| MC | KFC-506 (wajib MC) beririsan dengan KOM-524 (wajib, sem 5) dan KOM-526 | Redundansi lintas platform | Tegaskan pembagian: KOM-524 = mobile native dasar, KFC-506 = lintas platform, KOM-526 = web |
| MC | Dua jalur teknis KFC-506 (Dart+Flutter, React Native+Expo) sudah ada paketnya | Beban dosen dan jaminan kesetaraan CPL | Pakai satu jalur per kelas; samakan asesmen inti (lihat 017/037/041) |
| semua | 5 MK pilihan dipakai lintas klaster, KRS dapat mencampur dua klaster | Klaster tidak lagi menjadi "ranting" yang koheren | Tetapkan aturan: 4 pilihan harus dari daftar klaster yang sama (U-02) |
| semua | 21 SKS jalur dari 146 SKS (≈14%) | Kedalaman klaster terbatas | Nyatakan eksplisit bahwa klaster adalah pendalaman, bukan spesialisasi penuh |

## 9. Butir keputusan yang masih terbuka [U]

| Kode | Butir | Mengapa perlu keputusan | Pemilik yang wajar |
|---|---|---|---|
| U-01 | Apakah istilah resmi tetap **"konsentrasi"** atau diganti **"klaster ranting ilmu/kepakaran"** | Sumber memakai "konsentrasi"; istilah "ranting ilmu" belum ada di dokumen mana pun | Prodi + Senat Fakultas |
| U-02 | Keharusan memilih 4 MK pilihan dari satu klaster yang sama | Tanpa aturan ini, 5 MK berbagi membuat jalur mudah tercampur | Prodi |
| U-03 | Rasional tiga klaster terhadap saran APTIKOM maksimal dua peminatan | Perlu argumen akademik dan sumber daya, atau penyesuaian | Prodi |
| U-04 | Komposisi CPL per jalur (CPL03 dan CPL10 tidak pernah jadi CPL MK konsentrasi) | Menentukan apakah setiap jalur menanggung capaian lulusan secara seimbang | Tim kurikulum |
| U-05 | Prasyarat KFD-506/KFD-601/KFD-604 terhadap FST-408 dan KOM-202 | Kedalaman statistika bergantung pada urutan | Prodi + pengampu |
| U-06 | Penambahan capaian teknis pada KFD-707 | Saat ini hanya CPL09 | Pengampu + tim CPL |
| U-07 | Koreksi UWG-BK untuk KFC-707, KOM-419, KFD-709, KOM-527, KOM-630, KOM-526 (§8.2) | Tabel 15 tidak konsisten dengan Tabel 13 | Tim BoK |
| U-08 | Apakah perlu MK baru untuk menutup G-02 (statistika) dan G-03 (keamanan) | Berdampak pada total SKS 146 | Prodi |
| U-09 | Kedalaman GIT untuk non-IM: cukup KOM-525 atau perlu pilihan wajib | KA Core GIT 70 jam | Prodi |
| U-10 | Status klaster pada transkrip/ijazah dan KRS | Belum diatur sumber | Akademik |
| U-11 | Pemetaan isi (bukan judul) seluruh 83 MK ke KU CS2023 | Saat ini semua [K–tafsir] | Tim RPS |

## 10. Cara memakai dan memelihara berkas ini

1. **Jangan mengutip kolom APTIKOM/CS2023 sebagai bukti pemenuhan.** Kolom itu menunjukkan *ke mana* isi MK dapat dipetakan, bukan bahwa isinya sudah mengajarkannya. Untuk bukti, diperlukan RPS/CPMK per MK (§9 U-11).
2. **Jangan menulis `BK01` tanpa prefiks.** Gunakan `UWG-BK01` (Matematika) atau `APT-BK01` (Society, Ethics) atau `BK-IM-01` (bahan kajian klaster).
3. Jika Tabel 15/18 berubah, perbarui §5 dan §8.2 lebih dulu; §6 dan §7 bergantung padanya. Jalankan `python3 -B INFORMATIKA_2026/analisis_pemetaan.py --check` setelah perubahan yang menyentuh CPL/BK.
4. Jika laporan CS2023 diperbarui (edisi setelah Januari 2024), periksa ulang Tabel 2 dan daftar knowledge unit; nomor halaman di laporan berubah antar edisi.
5. Berkas ini **tidak** menggantikan [003](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md) sebagai daftar resmi bahan kajian prodi. Bahan kajian `BK-IM/DS/MC-*` adalah usulan rincian tingkat klaster.

## 11. Rujukan

1. **[S]** Buku KPT OBE Teknik Informatika UWG 2026 [Update 11 September 2026], Bab VII §8.6 "Mata Kuliah Pilihan / Konsentrasi", Tabel 13–18, Lampiran B Tabel 36–38. SHA-256 `a54a570150d0f7d38d633e72104b326062981818599101017dd3a7b4dfb2601d`. Ekstraksi: [003](003_BOK_DAN_BAHAN_KAJIAN_TEKNIK_INFORMATIKA_07112026_0859.md), [004](004_PEMETAAN_MK_CPL_BK_TEKNIK_INFORMATIKA_07112026_0859.md).
2. **[K]** Kumar, A., Raj, R. K., Aly, S. G., et al. *Computer Science Curricula 2023 (CS2023)*. ACM/IEEE-CS/AAAI, Januari 2024. DOI [10.1145/3664191](https://doi.org/10.1145/3664191), ISBN 979-8-4007-1033-9. Teks lengkap: <https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm>. Dipakai: Bab 2 (model pengetahuan, Tabel 2 jam, sunflower model, langkah desain kurikulum), Bab 3 (knowledge area dan knowledge unit ke-17 KA). Tautan ResearchGate pada permintaan (`publication/381039937`) merujuk laporan yang sama; yang dibaca adalah salinan ACM.
3. **[K]** APTIKOM. *Buku Panduan Kurikulum Berbasis OBE/KKNI/SKKNI, Program Studi Informatika/Ilmu Komputer, versi 2.0*, Tabel 4 (halaman PDF 42). SHA-256 `30f91073c242faf4fc397fef3992d6f1f11241f911ea2cda32d7539fbe344701`. Transkripsi: [008](008_TABEL_4_RUMUSAN_BAHAN_KAJIAN_APTIKOM_INFORMATIKA_07112026_0942.md).
4. **[K]** Perbedaan angka APTIKOM Tabel 4 vs CS2023 Tabel 2 untuk BK yang sama (selisih tercetak, tidak diperbaiki): SEP 17/14 vs 18/14 · Security 6/0 vs 6/35 · SE 6/23 vs 6/21 · DM 9/23 vs 10/26 · FPL 23/21 vs 21/19 · GIT 4/76 vs 4/70 · AI 11/12 vs 12/18 · SF 18/9 vs 18/8 · OS 8/20 vs 8/13 · SPD 3/0 vs 4/—  · MSF 55/0 vs 55/145. Pembacaan lengkap pada [006 §33](006_ANALISIS_DAN_SURVEI_PUSTAKA_INFORMATIKA_07112026_0910.md).
5. **[S]** Paket perangkat ajar yang sudah ada untuk MK yang disebut di sini: KFC-506 jalur Dart+Flutter ([037](037_PAKET_RPS_SAP_ASESMEN_KFC-506A_DART_FLUTTER_09112026_1339.md)) dan React Native+Expo ([041](041_PAKET_RPS_SAP_ASESMEN_KFC-506B_REACT_NATIVE_EXPO_09112026_1339.md)); KOM-526 empat jalur ([013](013_PAKET_RPS_SAP_ASESMEN_KOM-526A_SISTEM_APLIKASI_WEB_PHP_NATIVE_07112026_1328.md)–[016](016_PAKET_RPS_SAP_ASESMEN_KOM-526D_SISTEM_APLIKASI_WEB_PYTHON_FLASK_07112026_1328.md)). Semua masih draf [U].
