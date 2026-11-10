# PKR-2026 — Pemetaan Kurikulum dan Bahan Kajian per Klaster Ranting Ilmu (Bidang Ilmu Kepakaran) terhadap CS2023 dan APTIKOM

> **Status: DRAF [U], belum disahkan.** Dokumen ini memetakan kurikulum Program Studi **Sistem dan Teknologi Informasi (SISTEKIN)** ke **tiga klaster peminatan** yang sudah ada pada Dokumen 005, lalu membandingkannya dengan **APTIKOM** (SI v2.0 dan TI 2023) dan **[Computer Science Curricula 2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)**. Pembanding eksternal **tidak menggantikan** BoK SISTEKIN dan **tidak menambah MK atau SKS**.
>
> **Kode dokumen: PKR-2026** (*Pemetaan Klaster Ranting*). Berkas ini sengaja **tidak** memakai nomor `000`–`054` (namespace dokumen induk buku kurikulum) maupun `055`–`100` (namespace perangkat ajar), sesuai aturan penomoran di `PERANGKAT_AJAR/README.md` butir 2 dan `AGENTS.md` butir 9.
>
> Berkas pendukung: [003 CPL & BoK](003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md) · [004 Keterlacakan OBE](004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md) · [005 Struktur & Peminatan](005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md) · [016 Audit BoK](016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md) · [021 Panduan KPT DIKTI](021_PANDUAN_KPT2024_DIKTI_FULLTEXT.md) · [025 Rekomendasi Cross-Track 2027](025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md) · [037 Boundary Guardrails](037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md)

## 1. Ringkasan

| Klaster [S] | Kode | 6 MK (18 SKS) [S] | Ranting ilmu inti | Padanan APTIKOM [K] | Padanan CS2023 [K] | Celah utama |
|---|---|---|---|---|---|---|
| **Integrated Smart Systems** | P1 | STA-501, STA-601, STA-602, STA-701, STA-702, STA-703 | Kecerdasan artifisial terapan, rekayasa data, agen cerdas, MLOps, LLM, visi tepi | APT-IT02, APT-IT22, APT-IT09, APT-IS13 | AI (12/18), DM (10/26), PDC (9/26), GIT-Image, SPD-Embedded | **7 dari 36 BK** (5 primer) — klaster paling sempit; tidak menyentuh SEC/NC/OS |
| **Cloud Infrastructure & Cybersecurity** | P2 | STB-501, STB-601, STB-602, STB-701, STB-702, STB-703 | Infrastruktur, keamanan siber, cloud/DevOps, tata kelola & arsitektur enterprise | APT-IT01, APT-IT07, APT-IT12, APT-IT14, APT-IS06, APT-IS16 | NC (7/24), OS (8/13), SEC (6/35), SF (18/8), SPD-Web | **13 dari 36 BK**, tetapi 4 MK teori murni bertumpu pada kerangka sertifikasi (COBIT/ITIL/TOGAF) |
| **Digital Platform Engineering** | P3 | STC-501, STC-601, STC-602, STC-701, STC-702, STC-703 | UX berbasis riset, proses bisnis, rekayasa platform, XR, SaaS, produk digital | APT-IT04, APT-IT06, APT-IT11, APT-IT05, APT-IS15, APT-IS04 | SDF (43), SE (6/21), HCI (8/16), SPD, GIT-Immersion | **13 dari 36 BK**, tetapi **3 dari 6 MK hanya BK sekunder** — tidak ada BK yang mereka bina secara primer |

Kesimpulan pokok (rincian §8):

1. **Untuk SISTEKIN, APTIKOM adalah pembanding utama; CS2023 pembanding sekunder.** Silsilah BoK prodi adalah IS2020 + IT2017 + CC2020 (Dokumen 003), bukan CS2023. Memakai CS2023 sebagai tolok ukur tunggal menghasilkan "celah" palsu: tidak adanya MK kompilasi atau grafika lanjut bukan kekurangan prodi Sistem dan Teknologi Informasi.
2. **Tiga klaster menyentuh 30 dari 36 BK SISTEKIN.** Enam BK yang tidak tersentuh klaster mana pun — `BK-IS01`, `BK-IS10`, `BK-IS11`, `BK-IS21`, `BK-IT01`, `BK-IT15` — semuanya ditanggung MK wajib. **Tidak ada BK yang hilang dari kurikulum** (§5.5).
3. **Klaster bukan partisi yang saling lepas.** Tiga BK (`BK-IS19`, `BK-IT05`, `BK-IT07`) menjadi bukti BoK untuk dua klaster sekaligus, karena keduanya berbagi MK wajib.
4. **BK-IT02 (*Applied AI & Intelligent Technologies*) — penopang seluruh klaster P1 — tidak punya padanan dalam 27 BK APTIKOM TI 2023.** AI hanya muncul di radar CC2020 (area 3.2), tidak diangkat menjadi BK dalam Tabel 6. Ini **bukan kesalahan**: panduan TI 2023 hlm. PDF 32 secara eksplisit mengizinkan prodi menambah BK sesuai domain penciri, tetapi statusnya perlu dinyatakan (§6.2, U-13).
5. **Ditemukan 8 salah label kode BoK pada 005 §4, 1 kesalahan aritmetika pada 004 §6.2, dan 3 konflik identitas MK antar-dokumen induk** yang harus dibereskan sebelum pemetaan dipakai untuk akreditasi (§8.2, §8.3). Semua terverifikasi, bukan dugaan.

## 2. Status bukti, penandaan, dan aturan anti-kolisi notasi

| Tanda | Arti |
|---|---|
| **[S]** | Tertulis pada dokumen induk repo: 003 (CPL/BoK), 004 (keterlacakan), 005 (struktur & peminatan). Identitas MK, kode, SKS, semester, CPL per MK, dan komposisi peminatan berasal dari sini. |
| **[K]** | Pembanding eksternal: APTIKOM SI v2.0 (Tabel 4, hlm. 19–20); APTIKOM TI 2023 (Tabel 6, hlm. PDF 32–39); CS2023 (Januari 2024, DOI 10.1145/3664191; Tabel 2 jam dan 17 knowledge area). |
| **[K–tafsir]** | Padanan yang saya turunkan dari judul MK + ruang lingkup BoK, belum diverifikasi terhadap RPS/isi 16 pertemuan. |
| **[U]** | Usulan atau keputusan yang belum ada di sumber mana pun. |

### 2.1 Empat keluarga kode `BK` hidup berdampingan — wajib berprefiks

| Prefiks | Pemilik | Jumlah | Contoh |
|---|---|---|---|
| `BK-IS01…BK-IS21` | BoK internal SISTEKIN, turunan IS2020 | 21 | `BK-IS06` *Information Security and Risk Management* |
| `BK-IT01…BK-IT15` | BoK internal SISTEKIN, turunan IT2017/CC2020 | 15 | `BK-IT05` *Cloud Computing & Virtualization* |
| `APT-IS01…19` | APTIKOM Panduan **SI v2.0** Tabel 4 | 11 Utama + 1 Umum + 7 Pendukung | `APT-IS02` *Data / Information Management* |
| `APT-IT01…27` | APTIKOM Panduan **TI 2023** Tabel 6 | 14 Penciri Utama + 13 Penciri Pendukung | `APT-IT01` *Virtual Systems and Services* |
| `BK-P1/P2/P3/PL-xx` | Bahan kajian klaster — **usulan dokumen ini** | 9 + 9 + 9 + 6 | `BK-P1-08` MLOps, agen cerdas, dan AI generatif |

`BK01` **tidak boleh ditulis tanpa prefiks**: `APT-IS01` = *Foundation of Information Systems*, `APT-IT01` = *Virtual Systems and Services*, `BK-IS01` = *Foundations of Information Systems*, `BK-IT01` = *Information Technology Fundamentals*. Empat entitas berbeda dengan notasi mirip.

### 2.2 Batasan yang harus dibaca sebelum mengutip tabel

- Simbol ●/○ pada 004 §6 dan seluruh isi §5 dokumen ini adalah **hasil kurasi di repo**, bukan tabel resmi APTIKOM. APTIKOM hanya menerbitkan daftar BK; pemetaan BK→MK adalah kewajiban prodi (SI v2.0 hlm. 21–22; TI 2023 hlm. PDF 41–42).
- Jam CS2023 (CS Core / KA Core) **tidak dikonversi ke SKS**, dan bobot APTIKOM **tidak digabung** dengan jam CS2023. Satuannya berbeda.
- APTIKOM SI v2.0 Tabel 4 hanya memuat kode, nama, deskripsi, kategori, dan referensi — **tidak memuat jam**. Klaim "X jam APTIKOM" tidak dapat dibuat.
- CS2023 menuntut pemeriksaan *skill level* per topik; itu hanya bisa dilakukan pada RPS. Seluruh kolom CS2023 di sini berada pada tingkat **judul MK**.
- Dokumen ini **tidak** memakai `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md` di root repo sebagai sumber identitas: versi root masih memuat kode lama (§8.3 C-3).

## 3. Kerangka klaster dan ranting ilmunya

### 3.1 Komposisi klaster [S]

Setiap mahasiswa menempuh **satu paket peminatan penuh: 6 MK / 18 SKS** — 1 MK di Semester 5, 1 MK di Semester 6, 4 MK di Semester 7 (005 §1.4 dan §4). Portofolio yang ditawarkan 18 MK / 54 SKS.

| Klaster | Kode | Semester 5 | Semester 6 | Semester 7 (4 MK) | SKS |
|---|---|---|---|---|---|
| **P1 Integrated Smart Systems** *(Flagship)* | `STA-` | STA-501 Sistem Pendukung Keputusan | STA-601 Rekayasa Big Data dan Komputasi Terdistribusi | STA-602 Sistem Agen Cerdas · STA-701 MLOps dan Alur Pipa AI · STA-702 AI Percakapan dan Asisten Cerdas · STA-703 Pengawasan Cerdas dan Analitika IoT | 18 |
| **P2 Cloud Infrastructure & Cybersecurity** *(Volume)* | `STB-` | STB-501 Keamanan Jaringan dan Forensik Digital | STB-601 Arsitektur Cloud & DevOps | STB-602 Manajemen Risiko Keamanan Siber · STB-701 Tata Kelola & Kepatuhan TI (COBIT 2019) · STB-702 Manajemen Layanan TI (ITIL 4) · STB-703 Arsitektur Enterprise (TOGAF) | 18 |
| **P3 Digital Platform Engineering** *(Niche & Techno)* | `STC-` | STC-501 Riset & Desain Pengalaman Pengguna (UX) | STC-601 Rekayasa & Otomasi Proses Bisnis (BPA) | STC-602 Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) · STC-701 Media Imersif & Pengembangan XR · STC-702 Arsitektur SaaS & Multi-Tenansi · STC-703 Manajemen Produk Digital & Praktik Agile | 18 |

Catatan komposisi:

- **Distribusinya 1/1/4, bukan 1/2/3.** [025](025_REKOMENDASI_PENGEMBANGAN_MK_PEMINATAN_DAN_CROSS_TRACK_2027.md) §2 menulis "AS-IS 2026: Sem 6 ambil 2 MK, Sem 7 ambil 3 MK". Itu **tidak sesuai** dengan 005, yang hanya menyediakan satu slot pilihan di Semester 6 (baris 45) dan empat slot di Semester 7 (baris 49–52). 005 yang berlaku (U-10).
- **Tipe MK [S]:** 13 dari 18 MK peminatan bertipe `+P` (praktikum). Yang teori murni hanya STB-602, STB-701, STB-702, STB-703, dan STC-703. Artinya bagian hulu P2 (tata kelola) dan bagian hilir P3 (manajemen produk) **paling lemah bukti praktiknya** — relevan untuk LAM INFOKOM kriteria 4 dan IKU 7.
- **Tidak ada MK pilihan lintas peminatan** pada Kurikulum 2026 (model *fixed-track cohort*). Usulan *cross-track* maksimal 6 SKS baru diajukan untuk siklus 2027 (025).

### 3.2 Ranting ilmu per klaster [U]

Pengelompokan berikut **memecah klaster menjadi ranting** tanpa menambah MK. Tanda `*` = MK wajib; klaster adalah pendalaman di atas inti, bukan pengganti.

| Klaster | Ranting ilmu | MK |
|---|---|---|
| **P1** | P1-a Penalaran simbolik, pencarian, dan sistem pakar | STI-307* |
| | P1-b Pembelajaran mesin dan pembelajaran mendalam | STI-413*, STI-624* |
| | P1-c NLP dan temu balik informasi | STI-414* |
| | P1-d Penambangan data dan visualisasi | STI-520* |
| | P1-e Sistem pendukung keputusan & MCDM | STA-501 |
| | P1-f Rekayasa big data dan komputasi terdistribusi | STA-601 |
| | P1-g Sistem multi-agen dan pembelajaran penguatan | STA-602 |
| | P1-h MLOps dan operasionalisasi model | STA-701 |
| | P1-i LLM generatif, RAG, dan asisten percakapan | STA-702 |
| | P1-j Visi komputer tepi dan analitika IoT | STA-703 |
| **P2** | P2-a Arsitektur & organisasi sistem TI | STI-103* |
| | P2-b Sistem operasi | STI-310* |
| | P2-c Jaringan komputer | STI-312* |
| | P2-d Komputasi awan | STI-417* |
| | P2-e Keamanan informasi dasar dan lanjut | STI-418*, STI-519* |
| | P2-f IoT dan sistem tertanam | STI-521*, STI-727* |
| | P2-g Keamanan jaringan dan forensik digital | STB-501 |
| | P2-h Arsitektur cloud, DevOps, dan IaC | STB-601 |
| | P2-i Manajemen risiko dan ketahanan siber | STB-602 |
| | P2-j Tata kelola, layanan, dan arsitektur enterprise | STB-701, STB-702, STB-703 |
| **P3** | P3-a Analisis & perancangan sistem informasi | STI-306* |
| | P3-b Desain & prototyping UI/UX | STI-308* |
| | P3-c Web front end dan back end | STI-311*, STI-416* |
| | P3-d Pemrograman aplikasi mobile | STI-522* |
| | P3-e Rekayasa platform digital | STI-625* |
| | P3-f Integrasi layanan cerdas berbasis AI | STI-726* |
| | P3-g Manajemen proyek TI dan produk digital | STI-523*, STC-703 |
| | P3-h Otomasi dan pemodelan proses bisnis | STC-601 |
| | P3-i Rekayasa aplikasi domain vertikal | STC-602 |
| | P3-j Media imersif, XR, dan arsitektur SaaS | STC-701, STC-702 |

Ranting P1-e sampai P1-j, P2-g sampai P2-j, dan P3-h sampai P3-j **hanya berisi MK pilihan** — inilah yang membedakan klaster, karena sisanya ditanggung MK wajib.

## 4. Bahan Kajian per klaster (rumusan turunan)

Rumusan di bawah adalah **usulan bahan kajian tingkat klaster [U]** — lebih rinci daripada 21+15 BK SISTEKIN, tetapi tetap dilacak ke CPL dan MK yang ada. Kolom APTIKOM dan CS2023 adalah **[K–tafsir]**.

### 4.1 Klaster P1 — Integrated Smart Systems (9 bahan kajian)

| Kode | Rumusan bahan kajian | Cakupan topik | MK pengampu [S] | CPL [S] | BK primer (004 §6) [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|---|
| BK-P1-01 | Fondasi sistem cerdas: pencarian, representasi pengetahuan, penalaran | Heuristic search, A*, minimax, forward/backward chaining, ontologi, logika fuzzy | STI-307 | CPL-06, CPL-09 | BK-IS16 | APT-IS18, APT-IT02 | AI-Search, AI-KRR, AI-LRR, AI-Introduction |
| BK-P1-02 | Pembelajaran mesin: supervised, unsupervised, evaluasi model | Regresi, klasifikasi, klaster, cross-validation, metrik, bias-varians | STI-413 | CPL-06, CPL-09 | BK-IS13, BK-IS18 | APT-IS13 | AI-ML, MSF-Probability, MSF-Statistics |
| BK-P1-03 | Pembelajaran mendalam dan arsitektur jaringan saraf | CNN, RNN, transformer, regularisasi, optimasi, transfer learning | STI-624 | CPL-09, CPL-10 | BK-IS18 | APT-IT02 | AI-ML, AI-Vision, MSF-Linear |
| BK-P1-04 | NLP dan temu balik informasi | Tokenisasi, embedding, model bahasa, indeks terbalik, peringkat, evaluasi IR | STI-414 | CPL-06, CPL-09 | BK-IS16 | APT-IT02 | AI-NLP, DM-Querying, DM-Unstructured |
| BK-P1-05 | Penambangan data dan visualisasi analitik | EDA, asosiasi, klaster, dashboard, persepsi visual, narasi data | STI-520 | CPL-06, CPL-10 | BK-IS13, BK-IT09 | APT-IS13, APT-IT22 | DM-Analytics, GIT-Visualization, HCI-Design |
| BK-P1-06 | Sistem pendukung keputusan dan pengambilan keputusan multikriteria | MCDM, AHP, TOPSIS, PROMETHEE, integrasi fuzzy, DSS berbasis web | STA-501 | CPL-06, CPL-09, CPL-10 | BK-IS13 | APT-IS13 | AI-KRR, DM-Analytics, MSF-Discrete |
| BK-P1-07 | Rekayasa big data dan komputasi terdistribusi | Spark/PySpark, Kafka, Delta Lake, lakehouse, pemrosesan aliran, S3/MinIO | STA-601 | CPL-06, CPL-10 | BK-IS02 | APT-IT22, APT-IT15 | DM-NoSQL, DM-Distributed, DM-Processing, PDC-Programs, PDC-Evaluation |
| BK-P1-08 | MLOps, agen cerdas, dan AI generatif | MLflow, model registry, CI/CD model, Q-learning/PPO, FIPA-ACL, LLM, LoRA/QLoRA, RAG, LangChain | STA-602, STA-701, STA-702 | CPL-06, CPL-08, CPL-09, CPL-10 | BK-IS16, BK-IS18 | APT-IT02 | AI-ML, AI-Agents, AI-NLP, AI-Planning, SF-Evaluation |
| BK-P1-09 | Visi komputer tepi dan analitika IoT | YOLO/OpenCV, TensorRT, Edge TPU, Jetson, streaming video, telemetri sensor | STA-703 | CPL-07, CPL-09, CPL-11 | BK-IT14 | APT-IT02, APT-IT22 | AI-Vision, GIT-Image, SF-Performance, SPD-Embedded |

### 4.2 Klaster P2 — Cloud Infrastructure & Cybersecurity (9 bahan kajian)

| Kode | Rumusan bahan kajian | Cakupan topik | MK pengampu [S] | CPL [S] | BK primer (004 §6) [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|---|
| BK-P2-01 | Arsitektur dan organisasi sistem TI | Digital logic, representasi data, ISA, memori, I/O, kinerja-energi | STI-103 | CPL-02, CPL-05, CPL-07 | BK-IS03 | APT-IT05 | AR-Logic, AR-Representation, AR-Assembly, AR-Memory |
| BK-P2-02 | Sistem operasi dan virtualisasi | Proses, penjadwalan, memori, sistem berkas, kontainer, hipervisor | STI-310 | CPL-07, CPL-11 | BK-IS03, BK-IT05 | APT-IT01, APT-IT05 | OS-Principles, OS-Concurrency, OS-Memory, OS-Files, OS-Virtualization |
| BK-P2-03 | Jaringan komputer dan komunikasi data | TCP/IP, routing, switching, QoS, IPv6, socket | STI-312 | CPL-07, CPL-11 | BK-IS03, BK-IT03 | APT-IT03, APT-IT19 | NC-Fundamentals, NC-Routing, NC-SingleHop, NC-Mobility |
| BK-P2-04 | Komputasi awan dan arsitektur cloud-native | IaaS/PaaS/SaaS, elastisitas, Kubernetes, Terraform/Ansible, CI/CD | STI-417, STB-601 | CPL-07, CPL-08, CPL-11 | BK-IS19, BK-IT05 | APT-IT01, APT-IT20 | OS-Virtualization, PDC-Coordination, SPD-Common, SF-Resource |
| BK-P2-05 | Keamanan informasi: prinsip, kriptografi, kontrol akses | CIA triad, kriptografi, otentikasi, otorisasi, non-repudiasi, manajemen akses | STI-418, STI-519 | CPL-07, CPL-11, CPL-12 | BK-IS06, BK-IT06 | APT-IT07, APT-IT14 | SEC-Foundations, SEC-Crypto, SEC-Coding, OS-Protection |
| BK-P2-06 | Keamanan jaringan dan forensik digital | Wireshark/Zeek, Snort/Suricata, IDS/IPS, Autopsy, Volatility, rantai bukti | STB-501 | CPL-07, CPL-11, CPL-12 | BK-IS06, BK-IT06 | APT-IT07, APT-IT14, APT-IT21 | SEC-Forensics, NC-Security, SEC-Engineering |
| BK-P2-07 | Manajemen risiko dan ketahanan siber | ISO/IEC 27005, NIST CSF, BCP/DRP, penilaian risiko, mitigasi | STB-602 | CPL-07, CPL-12 | BK-IS06, BK-IS14, BK-IT12 | APT-IT12, APT-IT21 | SEC-Governance, SF-Reliability, SEP-Professional-Ethics |
| BK-P2-08 | Tata kelola, layanan, dan arsitektur enterprise | COBIT 2019 (EDM/APO/BAI/DSS/MEA), ITIL 4 SVS/SLA, TOGAF ADM, ArchiMate, UU PDP | STB-701, STB-702, STB-703 | CPL-06, CPL-07, CPL-12 | BK-IS04, BK-IS05, BK-IS14, BK-IT08, BK-IT12 | APT-IS06, APT-IS16, APT-IT08, APT-IT12 | **Tidak ada padanan langsung** — hanya SEP-Economies dan SF-Design secara parsial |
| BK-P2-09 | IoT, sistem tertanam, dan kota cerdas | MQTT, LPWAN, edge gateway, telemetri, arsitektur layanan kota, tata kelola digital | STI-521, STI-727 | CPL-07, CPL-11 | BK-IS03, BK-IT14 | APT-IT02, APT-IT03 | NC-Mobility, SF-Design, SPD-Embedded, SEP-Sustainability |

### 4.3 Klaster P3 — Digital Platform Engineering (9 bahan kajian)

| Kode | Rumusan bahan kajian | Cakupan topik | MK pengampu [S] | CPL [S] | BK primer (004 §6) [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|---|
| BK-P3-01 | Analisis dan perancangan sistem informasi | Elisitasi kebutuhan, DFD/UML, use case, spesifikasi, traceability | STI-306 | CPL-02, CPL-06 | BK-IS07 | APT-IS05 | SE-Requirements, SE-Design, SDF-Practices |
| BK-P3-02 | Desain pengalaman pengguna berbasis riset | Riset kualitatif/kuantitatif, persona, usability testing, design system, WCAG | STI-308, STC-501 | CPL-08, CPL-13 | BK-IS17, BK-IT10 | APT-IT11 | HCI-User, HCI-Design, HCI-Evaluation, HCI-Accessibility, HCI-Accountability |
| BK-P3-03 | Rekayasa web front end dan back end | HTML/CSS/JS, framework, REST/GraphQL, ORM, keamanan aplikasi, deployment | STI-311, STI-416 | CPL-08, CPL-13 | BK-IS12, BK-IT04 | APT-IT06, APT-IT16, APT-IT23 | SPD-Web, SDF-Practices, SEC-Coding, SE-Construction |
| BK-P3-04 | Rekayasa aplikasi mobile dan lintas platform | Arsitektur mobile, state management, offline-first, distribusi, kinerja perangkat | STI-522 | CPL-08, CPL-13 | BK-IS12, BK-IT04 | APT-IT06, APT-IT23 | SPD-Mobile, SE-Validation, AR-Performance-Energy |
| BK-P3-05 | Rekayasa platform digital, microservices, SaaS multi-tenancy | API gateway, container, database-per-tenant vs shared-schema, billing, caching, micro-frontend | STI-625, STC-702 | CPL-08, CPL-13 | BK-IS12, BK-IS19, BK-IT05, BK-IT11 | APT-IT04, APT-IT01 | SPD-Common, PDC-Communication, OS-Virtualization, SE-Design |
| BK-P3-06 | Otomasi dan pemodelan proses bisnis | BPMN 2.0, process mining, workflow engine (Camunda/Temporal), RPA | STC-601 | CPL-06, CPL-08, CPL-13 | BK-IS09 | APT-IS15 | SE-Requirements, DM-Analytics, SEP-Economies |
| BK-P3-07 | Rekayasa aplikasi domain vertikal | Domain-Driven Design, FinTech (payment gateway, ledger), EdTech (LMS, SCORM/xAPI) | STC-602 | CPL-08, CPL-13 | BK-IS12, BK-IT04 | APT-IT06 | SE-Design, SE-Construction, SPD-Web |
| BK-P3-08 | Media imersif dan pengembangan XR | WebXR, Three.js, AR mobile, interaksi spasial, aset 3D, performa render | STC-701 | CPL-08, CPL-13 | BK-IT04, BK-IT10 | APT-IT06, APT-IT11, APT-IT24 | GIT-Immersion, GIT-Interaction, GIT-Animation, HCI-Design |
| BK-P3-09 | Manajemen produk digital, agile, dan integrasi layanan cerdas | Roadmap, OKR, RICE/Kano/MoSCoW, A/B testing, Scrum, integrasi API AI/LLM | STC-703, STI-726 | CPL-06, CPL-08, CPL-14 | BK-IS08, BK-IS16, BK-IT02 | APT-IS04, APT-IS19, APT-IT13 | SEP-Economies, SEP-Communication, AI-Agents, SE-Teamwork |

### 4.4 Bahan kajian lintas klaster (wajib bagi semua jalur)

| Kode | Rumusan bahan kajian | MK pengampu [S] | CPL [S] | BK primer (004 §6) [S] | APTIKOM [K] | CS2023 KA/KU [K] |
|---|---|---|---|---|---|---|
| BK-PL-01 | Algoritma, struktur data, dan paradigma pemrograman | FST-102, FST-203, FST-205 | CPL-08 | BK-IS11, BK-IT10 | APT-IT10 | SDF-Fundamentals, SDF-Data-Structures, SDF-Algorithms, AL-Foundational |
| BK-PL-02 | Matematika terapan: kalkulus, aljabar, diskrit, logika, statistika | STI-102, STI-204, STI-205, FST-408 | CPL-05 | BK-IS10 | APT-IT17, APT-IT18 | MSF-Calculus, MSF-Linear, MSF-Discrete, MSF-Probability, MSF-Statistics |
| BK-PL-03 | Rekayasa perangkat lunak dan manajemen proyek | STI-309, STI-523, FST-610 | CPL-02, CPL-08, CPL-14 | BK-IS07, BK-IS08, BK-IT11 | APT-IS04, APT-IT13 | SE-Teamwork, SE-Tools, SE-Validation, SE-Refactoring, SEP-Economies |
| BK-PL-04 | Etika, hukum digital, dan tanggung jawab sosial | FST-206, MKU-101, MKU-102, MKU-405, MKU-507 | CPL-01, CPL-04 | BK-IS20, BK-IT15 | APT-IS09, APT-IT25, APT-IT26 | SEP-Context, SEP-Professional-Ethics, SEP-Privacy, SEP-Sustainability |
| BK-PL-05 | Komunikasi profesional dan praktik kerja global | FST-205, FST-612, MKU-103 | CPL-03 | BK-IT15, BK-IS21 | APT-IT08 | SEP-Communication, SEP-History, SEP-DEIA |
| BK-PL-06 | Riset, inovasi, dan kewirausahaan digital | FST-611, FST-613, FST-714, STI-728, MKU-204, MKU-508 | CPL-03, CPL-14 | BK-IS15, BK-IT13 | APT-IS12, APT-IS19, APT-IT13, APT-IT27 | SEP-Economies, SDF-Practices |

`BK-PL-01` dan `BK-PL-05` sama-sama memuat `FST-205` — konsekuensi konflik identitas MK pada §8.3 C-1.

## 5. Pemetaan kurikulum: MK × klaster × dua pembanding

Kolom **BK Primer/Sekunder** disalin apa adanya dari 004 §6.1–6.2. Kolom **CS2023** adalah **[K–tafsir]**.

### 5.1 Klaster P1 — Integrated Smart Systems

| MK [S] | SKS | Sem | Tipe | CPL [S] | BK Primer [S] | BK Sekunder [S] | APTIKOM [K] | CS2023 KA/KU [K] | BK-klaster |
|---|---|---|---|---|---|---|---|---|---|
| STA-501 Sistem Pendukung Keputusan | 3 | 5 | +P | CPL-06, CPL-09, CPL-10 | BK-IS13 | BK-IS02, BK-IT09 | APT-IS13 | AI-KRR, DM-Analytics | BK-P1-06 |
| STA-601 Rekayasa Big Data dan Komputasi Terdistribusi | 3 | 6 | +P | CPL-06, CPL-10 | BK-IS02 | BK-IS18 | APT-IT22, APT-IT15 | DM-NoSQL, DM-Distributed, PDC-Evaluation | BK-P1-07 |
| STA-602 Sistem Agen Cerdas | 3 | 7 | +P | CPL-06, CPL-09 | BK-IS16 | BK-IT02 | APT-IT02 | AI-Agents, AI-Planning, AI-KRR | BK-P1-08 |
| STA-701 MLOps dan Alur Pipa AI | 3 | 7 | +P | CPL-08, CPL-09, CPL-10 | BK-IS18 | BK-IS02, BK-IS13, BK-IT02, BK-IT09 | APT-IT02, APT-IT22 | AI-ML, SF-Evaluation, PDC-Evaluation | BK-P1-08 |
| STA-702 AI Percakapan dan Asisten Cerdas | 3 | 7 | +P | CPL-06, CPL-09 | BK-IS16 | — | APT-IT02 | AI-NLP, AI-Agents | BK-P1-08 |
| STA-703 Pengawasan Cerdas dan Analitika IoT | 3 | 7 | +P | CPL-07, CPL-09, CPL-11 | BK-IT14 | BK-IS16, BK-IS18 | APT-IT02, APT-IT22 | AI-Vision, GIT-Image, SPD-Embedded | BK-P1-09 |

### 5.2 Klaster P2 — Cloud Infrastructure & Cybersecurity

| MK [S] | SKS | Sem | Tipe | CPL [S] | BK Primer [S] | BK Sekunder [S] | APTIKOM [K] | CS2023 KA/KU [K] | BK-klaster |
|---|---|---|---|---|---|---|---|---|---|
| STB-501 Keamanan Jaringan dan Forensik Digital | 3 | 5 | +P | CPL-07, CPL-11, CPL-12 | BK-IS06, BK-IT06 | BK-IS03, BK-IT03 | APT-IT07, APT-IT14, APT-IT21 | SEC-Forensics, NC-Security | BK-P2-06 |
| STB-601 Arsitektur Cloud & DevOps | 3 | 6 | +P | CPL-07, CPL-08, CPL-11 | BK-IS19, BK-IT05 | BK-IS03 | APT-IT01, APT-IT20 | OS-Virtualization, PDC-Coordination, SPD-Common | BK-P2-04 |
| STB-602 Manajemen Risiko Keamanan Siber | 3 | 7 | Teori | CPL-07, CPL-12 | BK-IS06, BK-IS14, BK-IT12 | BK-IS05, BK-IT06 | APT-IT12, APT-IT21 | SEC-Governance, SF-Reliability | BK-P2-07 |
| STB-701 Tata Kelola & Kepatuhan TI (COBIT 2019) | 3 | 7 | Teori | CPL-07, CPL-12 | BK-IS05, BK-IS14, BK-IT08, BK-IT12 | BK-IS20 | APT-IS06, APT-IT08 | **tidak ada padanan langsung** | BK-P2-08 |
| STB-702 Manajemen Layanan TI (ITIL 4) | 3 | 7 | Teori | CPL-06, CPL-12 | BK-IS05, BK-IT08 | BK-IS14 | APT-IS06, APT-IT08 | **tidak ada padanan langsung** | BK-P2-08 |
| STB-703 Arsitektur Enterprise (TOGAF) | 3 | 7 | Teori | CPL-06, CPL-07, CPL-12 | BK-IS04 | BK-IT07 | APT-IS16, APT-IT04 | SF-Design (parsial) | BK-P2-08 |

### 5.3 Klaster P3 — Digital Platform Engineering

| MK [S] | SKS | Sem | Tipe | CPL [S] | BK Primer [S] | BK Sekunder [S] | APTIKOM [K] | CS2023 KA/KU [K] | BK-klaster |
|---|---|---|---|---|---|---|---|---|---|
| STC-501 Riset & Desain Pengalaman Pengguna (UX) | 3 | 5 | +P | CPL-08, CPL-13 | BK-IS17, BK-IT10 | — | APT-IT11 | HCI-User, HCI-Design, HCI-Evaluation | BK-P3-02 |
| STC-601 Rekayasa & Otomasi Proses Bisnis (BPA) | 3 | 6 | +P | CPL-06, CPL-08, CPL-13 | BK-IS09 | BK-IS07, BK-IT07 | APT-IS15 | SE-Requirements, DM-Analytics | BK-P3-06 |
| STC-602 Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech) | 3 | 7 | +P | CPL-08, CPL-13 | **— (tidak ada)** | BK-IS12, BK-IT04 | APT-IT06 | SE-Design, SE-Construction, SPD-Web | BK-P3-07 |
| STC-701 Media Imersif & Pengembangan XR | 3 | 7 | +P | CPL-08, CPL-13 | **— (tidak ada)** | BK-IT04, BK-IT10 | APT-IT06, APT-IT11, APT-IT24 | GIT-Immersion, GIT-Interaction, GIT-Animation | BK-P3-08 |
| STC-702 Arsitektur SaaS & Multi-Tenansi | 3 | 7 | +P | CPL-08, CPL-13 | **— (tidak ada)** | BK-IS12, BK-IS19, BK-IT05, BK-IT11 | APT-IT04, APT-IT01 | SPD-Common, OS-Virtualization, SE-Design | BK-P3-05 |
| STC-703 Manajemen Produk Digital & Praktik Agile | 3 | 7 | Teori | CPL-06, CPL-14 | BK-IS08 | BK-IS15, BK-IT13 | APT-IS04, APT-IS19, APT-IT13 | SEP-Economies, SE-Teamwork | BK-P3-09 |

**Tiga dari enam MK klaster P3 (STC-602, STC-701, STC-702) tidak memiliki BK primer.** Ketiganya hanya muncul sebagai pembina sekunder pada 004 §6, artinya tidak ada satu pun BK SISTEKIN yang "dimiliki" oleh MK tersebut. Ini temuan tersendiri (§8.1 G-09).

### 5.4 Cakupan BK SISTEKIN per klaster (dihitung ulang dari 004 §6)

| Klaster | BK tersentuh (primer + sekunder) | Dari 36 | BK primer saja | Kode BK tersentuh |
|---|---:|---:|---:|---|
| **P1** | **7** | 19,4% | **5** | IS02, IS13, IS16, IS18 · IT02†, IT09†, IT14 |
| **P2** | **13** | 36,1% | **9** | IS03†, IS04, IS05, IS06, IS14, IS19, IS20† · IT03†, IT05, IT06, IT08, IT12 |
| **P3** | **13** | 36,1% | **4** | IS07†, IS08, IS09, IS12†, IS15†, IS17, IS19 · IT04†, IT05, IT07†, IT10, IT11†, IT13† |
| **Gabungan** | **30** | 83,3% | **18** | 3 BK dipakai dua klaster (`BK-IS19`, `BK-IT05`, `BK-IT07`) |

† hanya tersentuh lewat peran **sekunder** untuk klaster tersebut.

Pembacaan yang benar:

- **P1 paling sempit**: 7 BK, dan hanya 5 yang benar-benar dibina secara primer. Seluruh P1 bertumpu pada dua keluarga BK — AI (`BK-IS16`, `BK-IS18`, `BK-IT02`) dan data (`BK-IS02`, `BK-IS13`, `BK-IT09`).
- **P2 dan P3 sama luas (13 BK)**, tetapi P2 jauh lebih "padat primer" (9 vs 4). P3 memperoleh luasnya dari peran sekunder, bukan dari kepemilikan BK.
- **Klaster bukan partisi yang saling lepas.** Tiga BK dibina dua klaster karena MK wajibnya sama — konsekuensi desain *fixed-track*.

### 5.5 Enam BK yang tidak tersentuh klaster mana pun

| BK | Nama | Ditanggung oleh (MK wajib) | Penilaian |
|---|---|---|---|
| BK-IS01 | *Foundations of Information Systems* | STI-101, FST-101 | wajar — fondasi |
| BK-IS10 | *Applied Mathematics and Logic* | STI-102, STI-204, STI-205, FST-408 | wajar — fondasi |
| BK-IS11 | *Programming Fundamentals & OOP* | FST-102, FST-203, FST-205 | wajar — fondasi |
| BK-IS21 | *Internship and Professional Practice* | FST-612 | wajar — magang |
| BK-IT01 | *Information Technology Fundamentals* | FST-101, STI-101 | wajar — fondasi |
| BK-IT15 | *Global Professional Practice* | FST-205, FST-612 | wajar — praktik profesional |

Semuanya BK fondasi dan BK praktik profesional. **Tidak ada BK SISTEKIN yang hilang dari kurikulum**; yang tidak tersentuh peminatan justru lapisan yang memang dirancang untuk semua jalur.

## 6. Silang APTIKOM resmi ↔ BK SISTEKIN ↔ CS2023

Bagian ini membandingkan **daftar BK resmi APTIKOM** (bukan daftar internal repo) dengan **BK SISTEKIN** dan **CS2023**.

### 6.1 APTIKOM SI v2.0 — 19 BK (Tabel 4, hlm. 19–20) vs 21 BK-IS SISTEKIN

| APTIKOM SI [K] | Nama resmi | Kategori | BK-IS SISTEKIN [S] | Status | CS2023 [K] |
|---|---|---|---|---|---|
| APT-IS01 | *Foundation of Information Systems* | Utama | BK-IS01 | ✅ sepadan | — (khas IS) |
| APT-IS02 | *Data / Information Management* | Utama | BK-IS02 | ✅ sepadan | DM-Data, DM-Modeling |
| APT-IS03 | *IT Infrastructure* | Utama | BK-IS03 | ✅ sepadan | SF-Overview, OS-Purpose, NC-Fundamentals |
| APT-IS04 | *IS Project Management* | Utama | BK-IS08 | ✅ sepadan | SE-Teamwork (parsial) |
| APT-IS05 | *Systems Analysis & Design* | Utama | BK-IS07 | ✅ sepadan | SE-Requirements, SE-Design |
| APT-IS06 | *IS Management and Strategy* | Utama | BK-IS05 | ✅ sepadan | — (khas IS) |
| APT-IS07 | *Application Development / Programming* | Utama | BK-IS11 | ✅ sepadan | SDF-Fundamentals, FPL-OOP |
| APT-IS08 | *Secure Computing* | Utama | BK-IS06 | ✅ sepadan | SEC-Foundations, SEC-Coding |
| APT-IS09 | *Ethics, use and implications for society* | Utama | BK-IS20 | ✅ sepadan | SEP-Context, SEP-Professional-Ethics |
| APT-IS10 | *Internship* | Utama (IABEE) | BK-IS21 | ✅ sepadan | — (di luar 17 KA) |
| APT-IS11 | *Mathematics and statistics* | Utama (IABEE) | BK-IS10 | ✅ sepadan | MSF-Calculus, MSF-Linear, MSF-Discrete, MSF-Statistics |
| APT-IS12 | *Research Methodology* | Umum | — | ❌ **tidak ada entri** | SDF-Practices (parsial) |
| APT-IS13 | *Data / Business Analytics* | Pendukung | BK-IS13, BK-IS18 | ✅ sepadan | DM-Analytics, AI-ML |
| APT-IS14 | *Personality Development* | Pendukung | — | ❌ **tidak ada entri** (ditutup BK-IT15) | SEP-DEIA (parsial) |
| APT-IS15 | *Business Process Management* | Pendukung | BK-IS09 | ✅ sepadan | SE-Requirements (parsial) |
| APT-IS16 | *Enterprise Architecture* | Pendukung | BK-IS04 | ✅ sepadan | SF-Design (parsial) |
| APT-IS17 | *User Interface Design* | Pendukung | BK-IS17 | ✅ sepadan | HCI-User, HCI-Design |
| APT-IS18 | *Emerging Technologies* | Pendukung | BK-IS16 | ✅ sepadan | AI-Introduction (parsial) |
| APT-IS19 | *Digital Innovation* | Pendukung | BK-IS15 | ✅ sepadan | SEP-Economies |

**17 dari 19 BK resmi SI v2.0 punya padanan setara.**

- **Dua celah nyata:** `APT-IS12 Research Methodology` (kategori Umum) dan `APT-IS14 Personality Development` (Pendukung) tidak memiliki entri BK-IS. Substansinya ditanggung FST-611/FST-613 dan MKU/PKPM, tetapi **belum dinyatakan sebagai BK** (U-04).
- **Tiga BK-IS tidak berasal dari Tabel 4 SI:** `BK-IS12` (Web & Mobile), `BK-IS14` (IT Audit), `BK-IS19` (Cloud & DevOps) — diambil dari IT2017/CC2020. **Bukan kesalahan**: SI v2.0 hlm. 19 mengizinkan prodi menambah BK sesuai *domain of practice*.
- **Instruksi wajib dipenuhi:** SI v2.0 mensyaratkan adopsi seluruh BK Utama (11 entri) — semuanya bertemu padanan. ✅

### 6.2 APTIKOM TI 2023 — 27 BK (Tabel 6, hlm. PDF 32–39) vs 15 BK-IT SISTEKIN

Tabel 6 TI 2023 memuat **14 BK Penciri Utama** (BK01–BK14) dan **13 BK Penciri Pendukung** (BK15–BK27). Panduan (hlm. PDF 32) mewajibkan prodi "mengadopsi 14 BK Penciri Utama".

| APTIKOM TI [K] | Nama resmi | Kategori | BK-IT SISTEKIN [S] | Status |
|---|---|---|---|---|
| APT-IT01 | Virtual Systems and Services | Utama | BK-IT05 *Cloud Computing & Virtualization* | ⚠️ sepadan, nama berbeda |
| APT-IT02 | Internet of Things | Utama | BK-IT14 *IoT and Embedded Smart Systems* | ✅ sepadan |
| APT-IT03 | Jaringan Komputer | Utama | BK-IT03 *Networking & Communications* | ✅ sepadan |
| APT-IT04 | Teknologi Sistem Terintegrasi | Utama | BK-IT07 *System Integration and Architecture* | ✅ sepadan |
| APT-IT05 | Teknologi Platform | Utama | BK-IT04 *Platform Technologies & Web/Mobile* | ⚠️ sepadan, tercampur Web/Mobile |
| APT-IT06 | Pengembangan Aplikasi Berbasis Platform | Utama | BK-IT11 *Software Development Practices* | ✅ sepadan |
| APT-IT07 | Prinsip-prinsip Keamanan Siber | Utama | BK-IT06 *Cybersecurity Principles & Defense* | ✅ sepadan |
| APT-IT08 | Praktek Profesional Global | Utama | BK-IT15 *Global Professional Practice* | ✅ sepadan |
| APT-IT09 | Manajemen Data dan Informasi | Utama | BK-IT09 *Data Analytics & Information Visualization* | ⚠️ sebagian — BK09 lebih luas daripada analitik |
| APT-IT10 | Fundamental Perangkat Lunak | Utama | BK-IT11 | ⚠️ **ganda** dengan APT-IT06 |
| APT-IT11 | Desain User Experience | Utama | BK-IT10 *User Experience & Interaction Design* | ✅ sepadan |
| APT-IT12 | Tata kelola dan Kebijakan Keamanan Siber | Utama | BK-IT08 *IT Service Management & Governance* | ⚠️ bergeser ke layanan TI; substansi keamanan ada di BK-IT12 |
| APT-IT13 | Manajemen Proyek | Utama | BK-IT12 *IT Risk Management and Compliance* | ❌ **tidak setara** |
| APT-IT14 | Teknologi dan Implementasi Keamanan Siber | Utama | BK-IT06 | ⚠️ **ganda** dengan APT-IT07 |
| APT-IT15 | Paradigma-paradigma Sistem | Pendukung | BK-IT01 (parsial) | ⚠️ |
| APT-IT16 | Sistem Web dan Mobile | Pendukung | BK-IT04 | ✅ |
| APT-IT17 | Struktur Diskrit | Pendukung | — (ditutup BK-IS10) | ❌ tidak diadopsi |
| APT-IT18 | Matematika | Pendukung | — (ditutup BK-IS10) | ❌ tidak diadopsi |
| APT-IT19 | Jaringan Komputer Terapan | Pendukung | BK-IT03 | ✅ |
| APT-IT20 | Cloud Computing | Pendukung | BK-IT05 | ✅ |
| APT-IT21 | Tantangan Baru Keamanan Siber | Pendukung | BK-IT06 | ✅ |
| APT-IT22 | Skalabilitas dan Analitik Data | Pendukung | BK-IT09 | ✅ |
| APT-IT23 | Aplikasi Mobile | Pendukung | BK-IT04 | ✅ |
| APT-IT24 | Pengembangan dan Manajemen Perangkat Lunak | Pendukung | BK-IT11 | ✅ |
| APT-IT25 | Tanggung Jawab Sosial | Pendukung | — (ditutup BK-IS20) | ❌ tidak diadopsi |
| APT-IT26 | Pembentukan Karakter | Pendukung | — (MKU/PKPM) | ❌ tidak diadopsi |
| APT-IT27 | Penelitian dan Pengembangan | Pendukung | — (BK-IT13 parsial) | ❌ tidak diadopsi |

**Lima temuan:**

1. **`APT-IT13 Manajemen Proyek` (penciri utama) belum punya BK-IT setara.** `BK-IT12` adalah *IT Risk Management and Compliance*. Substansinya ditanggung STI-523 dan STC-703, tetapi BK-nya tidak ada. **Ini celah nyata terhadap instruksi "adopsi 14 BK Penciri Utama"** (U-05).
2. **`BK-IT02` (*Applied AI & Intelligent Technologies*) tidak punya padanan di Tabel 6.** AI hanya muncul pada radar CC2020 (area 3.2 *Intelligent Systems*), tidak diangkat menjadi BK resmi TI 2023. Karena BK-IT02 adalah penopang utama klaster P1, statusnya **BK tambahan prodi** perlu dinyatakan eksplisit — sah menurut hlm. PDF 32 (U-13).
3. **Kode ganda:** `BK-IT06` menampung APT-IT07 + APT-IT14; `BK-IT11` menampung APT-IT06 + APT-IT10. Kepatuhan pada 14 BK utama karena itu **tampak** lebih baik daripada kenyataannya: 14 slot resmi dipetakan ke hanya 12 BK-IT.
4. **`BK-IT` SISTEKIN bukan salinan daftar TI 2023.** Nama `BK-IT01` (*Information Technology Fundamentals*), `BK-IT02` (*Applied AI*), dan `BK-IT05` (*Cloud Computing & Virtualization*) tidak terdapat dalam Tabel 6. Redaksi yang akurat: "**15 BK-IT SISTEKIN, dirumuskan ulang dari 27 BK APTIKOM TI 2023 / CC2020**" — bukan "15 dari 27".
5. **8 dari 13 BK Penciri Pendukung punya padanan; 5 tidak diadopsi** (APT-IT17, 18, 25, 26, 27). Substansinya ada pada MK wajib/MKU, tetapi tidak pada lapisan BK. Sah, karena BK pendukung bersifat pilihan.

### 6.3 Knowledge area CS2023 dan padanannya

17 KA CS2023 dengan jam **CS Core / KA Core** (Tabel 2 laporan), dipetakan ke MK SISTEKIN.

| CS2023 KA | CS Core | KA Core | MK pengampu SISTEKIN [S] | Status cakupan [K–tafsir] |
|---|---:|---:|---|---|
| **AI** Artificial Intelligence | 12 | 18 | STI-307, STI-413, STI-414, STI-520, STI-624, STI-726; STA-602, STA-701–703 | **Kuat** — inti P1 |
| **AL** Algorithmic Foundations | 32 | 32 | FST-203, STI-204 | **Tipis** — 6 SKS untuk 64 jam |
| **AR** Architecture and Organization | 9 | 16 | STI-103 | **Tipis** — 3 SKS (§8.3 C-2) |
| **DM** Data Management | 10 | 26 | FST-207, STI-415, STI-520, STA-601, STC-702 | CS Core ✅; KA Core lewat P1/P3 |
| **FPL** Foundations of Programming Languages | 21 | 19 | FST-205 | **Tipis** — 2 SKS (§8.3 C-1) |
| **GIT** Graphics and Interactive Techniques | 4 | 70 | STC-701 | **Sangat tipis** — 1 MK pilihan |
| **HCI** Human-Computer Interaction | 8 | 16 | STI-308, STC-501, STC-701 | Cukup |
| **MSF** Mathematical and Statistical Foundations | 55 | 145 | STI-102, STI-204, STI-205, FST-408 | **Tipis** — 12 SKS |
| **NC** Networking and Communication | 7 | 24 | STI-312, STI-417, STI-521, STB-501 | CS Core ✅; KA Core lewat P2 |
| **OS** Operating Systems | 8 | 13 | STI-310 | Cukup |
| **PDC** Parallel and Distributed Computing | 9 | 26 | STA-601, STC-702, STI-417 | CS Core berpeluang kurang |
| **SDF** Software Development Fundamentals | 43 | — | FST-102, FST-203, FST-205, STI-311, STI-416, STI-522 | **Kuat** |
| **SE** Software Engineering | 6 | 21 | STI-306, STI-309, STI-523, STC-601, FST-610 | Cukup |
| **SEC** Security | 6 | 35 | STI-418, STI-519, STB-501, STB-602, STB-701 | CS Core ✅; KA Core kuat di P2 |
| **SEP** Society, Ethics, and the Profession | 18 | 14 | FST-206, MKU-101/102/405, FST-612 | Cukup, tersebar |
| **SF** Systems Fundamentals | 18 | 8 | STI-103, STI-310, STI-312 | Cukup |
| **SPD** Specialized Platform Development | 4 | — | STI-311, STI-416, STI-522, STC-701, STC-702 | **Kuat** |

**Pembacaan yang benar:** SISTEKIN **bukan** program ilmu komputer. Empat KA tipis (AL, AR, FPL, MSF) dan satu sangat tipis (GIT) adalah **konsekuensi wajar** profil IS/IT, bukan cacat. Hal yang justru perlu diwaspadai adalah **ketimpangan ke arah sebaliknya**: SPD dan AI sangat kuat sementara AL dan MSF tipis, sehingga kemampuan rekayasa platform dan penerapan AI berpotensi melampaui kedalaman fondasi algoritmik dan matematis. Itu risiko mutu yang sah untuk dibahas, bukan pelanggaran CS2023.

## 7. Keterlacakan CPL-01…CPL-14 → klaster

Kode baku `CPL-01`–`CPL-14` dengan alias kategori lama `S1`, `KU1`–`KU3`, `P1`–`P4`, `KK1`–`KK6` (004 §0).

| CPL [S] | Alias | Ringkasan | P1 | P2 | P3 | Ditanggung inti (MK wajib) |
|---|---|:---:|:---:|:---:|---|
| CPL-01 | S1 | Integritas, etika, spiritualitas | — | — | — | ✅ MKU, FST-206 |
| CPL-02 | KU1 | Berpikir kritis & pemecahan masalah | — | — | — | ✅ FST-101/102, STI-204 |
| CPL-03 | KU2 | Komunikasi & kolaborasi | — | — | — | ✅ MKU-103, FST-611 |
| CPL-04 | KU3 | Tanggung jawab etis & kepatuhan | — | — | — | ✅ FST-206, MKU-405 |
| CPL-05 | P1 | Fondasi matematika & sains | — | — | — | ✅ STI-102/204/205, FST-408 |
| CPL-06 | P2 | Konsep SI, arsitektur, tata kelola | ✅ ×4 | ✅ ×2 | ✅ ×2 | ✅ STI-101, STI-306 |
| CPL-07 | P3 | Infrastruktur, cloud, jaringan, keamanan | ✅ ×1 | ✅ ×5 | — | ✅ STI-103/310/312/417/418 |
| CPL-08 | P4 | RPL, basis data, platform, UI/UX | ✅ ×1 | ✅ ×1 | ✅ ×5 | ✅ FST-203/207, STI-309 |
| CPL-09 | KK1 | Model ML/AI & sistem cerdas | ✅ ×4 | — | — | ✅ STI-307/413 |
| CPL-10 | KK2 | Rekayasa data, DWH/BI, MLOps | ✅ ×3 | — | — | ✅ STI-415/520 |
| CPL-11 | KK3 | Cloud infra, jaringan, IoT | ✅ ×1 | ✅ ×3 | — | ✅ STI-521 |
| CPL-12 | KK4 | Risiko siber, audit, tata kelola | — | ✅ ×5 | — | ✅ STI-519 |
| CPL-13 | KK5 | UI/UX & platform digital | — | — | ✅ ×5 | ✅ STI-311/416/522/625 |
| CPL-14 | KK6 | Proyek agile & technopreneurship | — | — | ✅ ×1 | ✅ STI-728, MKU-204 |

`×n` = jumlah MK dalam klaster yang dibebani CPL tersebut (dihitung dari 004 §4.1–4.3; total 18 sel, sesuai 18 MK peminatan).

**Tiga pola yang perlu diputuskan:**

1. **CPL-01 sampai CPL-05 tidak pernah menjadi CPL MK peminatan mana pun.** Wajar untuk sikap, keterampilan umum, dan fondasi matematika — tetapi berarti **peminatan tidak menambah capaian sikap/komunikasi sama sekali**, padahal COBIT/ITIL/TOGAF di P2 dan Scrum di P3 kaya muatan etika dan kolaborasi (U-03).
2. **CPL-12 (KK4) hanya hidup di P2.** Mahasiswa P1 dan P3 tidak pernah mendapat MK peminatan ber-CPL-12; capaian KK4 mereka bergantung penuh pada STI-519 (wajib). Sah, tetapi membuat **P1 dan P3 lemah pada tata kelola dan audit** — isu bila PL-4 (*IT Project Manager*) diarahkan ke sana.
3. **CPL-14 (KK6) hanya bersandar pada STC-703** di tingkat peminatan, sementara STI-728 (wajib) juga ber-CPL-14. Technopreneurship karena itu **tidak bergantung pada P3**; klaim "P3 = jalur technopreneurship" perlu dirumuskan hati-hati di materi promosi prodi.

## 8. Temuan, celah, dan risiko

### 8.1 Celah dan risiko terhadap pembanding eksternal

| # | Temuan | Bukti | Tingkat |
|---|---|---|---|
| G-01 | **CS2023 AL (32 + 32 jam) hanya dilayani FST-203 (3 SKS) + STI-204 (3 SKS)**; tidak ada MK algoritma lanjut, kompleksitas, atau strategi algoritmik | CS2023 Tabel 2; 005 §1.2–1.3 | Sedang — wajar untuk IS/IT, tetapi membatasi P1 |
| G-02 | **CS2023 MSF (55 CS Core + 145 KA Core jam) vs 12 SKS matematika/statistika**; statistika hanya FST-408 (3 SKS) sebelum STI-413 | CS2023 Tabel 2; 005 | Tinggi untuk P1 |
| G-03 | **CS2023 GIT KA Core 70 jam dilayani satu MK pilihan (STC-701)**; tidak ada MK grafika di inti | CS2023 Tabel 2; 005 | Rendah — di luar ciri IS/IT |
| G-04 | **APT-IT13 Manajemen Proyek (penciri utama) tidak punya BK-IT setara**; BK-IT12 berisi manajemen risiko | TI 2023 Tabel 6, hlm. PDF 35; 003 | Tinggi — menyangkut instruksi 14 BK utama |
| G-05 | **APT-IS12 Research Methodology dan APT-IS14 Personality Development tidak punya entri BK-IS** | SI v2.0 Tabel 4, hlm. 19–20; 003 | Sedang |
| G-06 | **Lima MK peminatan bertipe Teori murni** (STB-602, STB-701, STB-702, STB-703, STC-703) sehingga bukti praktik P2/P3 lemah | 005 §1.4 | Sedang — IKU 7 & LAM INFOKOM kriteria 4 |
| G-07 | **Tidak ada MK peminatan yang membawa CPL-01…CPL-05**, termasuk etika | 004 §4.1–4.3; §7 dokumen ini | Sedang |
| G-08 | **P1 tidak menyentuh BK jaringan (BK-IS03/IT03) dan P3 tidak menyentuh BK data (BK-IS02/IT09)**; tidak ada jalur silang | 004 §6 vs 005 §1.4 | Rendah — desain *fixed-track*, diusulkan dibuka 2027 (025) |
| G-09 | **Tiga MK klaster P3 (STC-602, STC-701, STC-702) tidak memiliki BK primer**; P3 hanya membina 4 BK secara primer vs 9 di P2 | 004 §6.1–6.2; §5.4 dokumen ini | Sedang — klaster P3 tampak luas tetapi tidak "memiliki" BK |
| G-10 | **`BK-IT02` (Applied AI) tidak punya padanan dalam 27 BK APTIKOM TI 2023**, padahal ia penopang utama P1 | TI 2023 Tabel 6, hlm. PDF 32–39 | Sedang — status "BK tambahan prodi" perlu dinyatakan |

### 8.2 Salah label kode BoK pada Dokumen 005 §4 (terverifikasi)

Pada 005 §4, kolom BoK untuk MK peminatan memuat kode yang **namanya tidak sesuai** Tabel 6.1/6.2 di 004 (yang konsisten dengan nomenklatur 003). Teks pendamping di 005 justru menggambarkan topik yang benar — jadi yang salah adalah kodenya.

| MK | Kode di 005 §4 | Teks topik di 005 §4 | Nama resmi kode itu menurut 003 | Seharusnya (per 004 §6) |
|---|---|---|---|---|
| STA-501 | `BK-IS17` | "Business Analytics, AHP/TOPSIS" | BK-IS17 = *Human-Computer Interaction & UX* | `BK-IS13` |
| STB-701 | `BK-IS07` | "IT Governance, COBIT 2019 Focus" | BK-IS07 = *Systems Analysis and Design* | `BK-IS05`, `BK-IS14`, `BK-IT08`, `BK-IT12` |
| STB-702 | `BK-IS08` | "Service Management, ITIL 4 Foundation" | BK-IS08 = *Project Management* | `BK-IS05`, `BK-IT08` |
| STC-501 | `BK-IS13` | "Human-Centered Design, Usability" | BK-IS13 = *Data Analytics and Business Intelligence* | `BK-IS17`, `BK-IT10` |
| STC-602 | `BK-IS05` | "Application Domains, Microservices" | BK-IS05 = *IS Management and Governance* | `BK-IS12`, `BK-IT04` (sekunder) |
| STC-701 | `BK-IT14` | "Computer Graphics, Unity/WebXR" | BK-IT14 = *IoT and Embedded Smart Systems* | `BK-IT04`, `BK-IT10` (sekunder) |
| STC-702 | `BK-IT08` | "Distributed Systems, Multi-Tenancy" | BK-IT08 = *IT Service Management & Governance* | `BK-IS12`, `BK-IS19`, `BK-IT05`, `BK-IT11` (sekunder) |
| STC-703 | `BK-IS14` | "Product Management, Scrum, Lean" | BK-IS14 = *IT Audit and Compliance* | `BK-IS08`, `BK-IS15`, `BK-IT13` |

Delapan baris. Dampaknya nyata: matriks BoK↔MK yang dibaca dari 005 §4 menghasilkan hitungan cakupan yang salah — misalnya `BK-IT14` tampak dibina STC-701 (padahal bukan) sehingga P3 terlihat menyentuh IoT. **Dokumen ini memakai versi 004 §6** dan mencatat perbedaannya. Perbaikan 005 §4 adalah pekerjaan terpisah (U-01).

Verifikasi cepat:

```bash
cd KURIKULUM2026_REVISI
python3 -B _tools/verify_pemetaan_klaster_ranting.py
# nama resmi tiap kode BK menurut 003, lalu bandingkan dengan kolom BoK 005 §4
grep -n 'BK-IS17\|BK-IS13\|BK-IT08\|BK-IT14' 003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md
sed -n '346,381p' 005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md
```

### 8.3 Konflik identitas MK antar-dokumen induk (terverifikasi)

| # | Konflik | Bukti | Dampak pada pemetaan |
|---|---|---|---|
| **C-1** | `FST-205` dinamai **"Bahasa Inggris Dasar untuk TI"** (2 SKS, Sem 2) di 005, tetapi **"Pemrograman Lanjut / Advanced OOP"** di 007 §13 dan di 003 — sekaligus dipakai sebagai pembina `BK-IT15` (*Global Professional Practice* *dan* `BK-IS11` (*Programming Fundamentals & OOP*) | 005 baris 89 & 210; 007 baris 573–578; 003 baris 166; 004 §6.1–6.2 | `BK-PL-01` vs `BK-PL-05` tidak dapat ditetapkan; CS2023 **FPL** (21 jam) hanya tertopang MK ini |
| **C-2** | `FST-204` dinamai **"Pengantar Kecerdasan Artifisial & Data"** (2 SKS) di 005, tetapi **"Organisasi & Arsitektur Komputer"** di 004 baris 101 dan 007 §12 — 004 juga memakainya sebagai pembina sekunder `BK-IT01` | 005 baris 88; 004 baris 101; 007 baris 531–536 | CS2023 **AR** (9 CS Core jam) tidak dapat dipastikan pengampunya |
| **C-3** | `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md` **di root repo** masih memakai kode lama (`STI-201/202/301…701`, `STA-01..06`), sedangkan salinan di `KURIKULUM2026_REVISI/` memakai `STI-101…728`. Selain itu 004 baris 144–145 memakai `STI-726`/`STI-727` untuk Deep Learning & Digital Platform Engineering, lalu baris 159–160 memakai kode yang sama untuk Integrasi AI & Smart City; 005 menetapkan Deep Learning = `STI-624`, Digital Platform Engineering = `STI-625` | `grep -o 'STI-[0-9]\{3\}' BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md \| sort -u`; 004 baris 144–145 vs 005 §1.3 | Nama MK pada §5 dokumen ini **tidak** boleh diambil dari BUKU root atau dari 004 baris 144–160 |
| **C-4** | 004 §6.2 baris `BK-IT02` menulis `` `STI-726`, `STI-726` `` (kode ganda) dan mengklaim "9 MK", padahal kode uniknya hanya **8**. Ini satu-satunya selisih aritmetika "Total MK" di seluruh Tabel 6.1–6.2 | 004 Tabel 6.2 baris BK-IT02 | Angka "Total MK" pada baris itu perlu dikoreksi menjadi 8 (U-14) |

C-3 juga menjelaskan mengapa `_tools/verify_all_mk_aligned_with_005.py` melaporkan "LULUS 100%": skrip itu memeriksa **keberadaan kode**, bukan **kesesuaian nama** per baris.

### 8.4 Risiko implementasi per klaster

| Klaster | Risiko | Dampak | Mitigasi yang mungkin [U] |
|---|---|---|---|
| P1 | Statistika hanya 3 SKS (FST-408) sebelum STI-413 | Mahasiswa gagal pada kedalaman AI-ML dan MSF KA Core | Modul penyegaran + prasyarat eksplisit (U-06) |
| P1 | 4 dari 6 MK bertumpu pada AI/DM, dan 3 di antaranya `+P` di Semester 7 | Beban praktikum Semester 7 berat | Menyebar satu MK ke Semester 6 — butuh perubahan 005 |
| P1 | BK-IT02 tidak berakar pada BK resmi APTIKOM TI | Sulit dipertanggungjawabkan saat asesmen lapangan | Nyatakan sebagai BK tambahan prodi (U-13) |
| P2 | Empat MK teori murni bertumpu pada kerangka sertifikasi (COBIT/ITIL/TOGAF) | Sulit dinilai sebagai capaian OBE; risiko hafalan | Asesmen berbasis dokumen/portofolio nyata; tegaskan batas dengan STI-523 |
| P2 | Tumpang tindih STI-519 (Keamanan Lanjut, wajib) dengan STB-501/STB-602 | Duplikasi asesmen | Guardrails 037: STI-519 = fundamental, STB-501 = operasional/forensik, STB-602 = risiko/manajemen |
| P3 | STC-702 (SaaS) beririsan dengan STI-625 (Rekayasa Platform Digital, wajib) | Redundansi | STI-625 = arsitektur platform; STC-702 = multi-tenancy, billing, caching |
| P3 | Tiga MK tanpa BK primer (G-09) | Klaster tidak punya "rumah" BoK; sulit menilai kedalaman | Tetapkan BK primer pada 004 §6 untuk STC-602/701/702 |
| P3 | STC-701 (XR) bergantung perangkat keras/lab | Mutu asesmen tidak seragam | Batasi pada WebXR (tanpa perangkat khusus) + rubrik portofolio |
| Semua | Model *fixed-track* tidak memberi ruang lintas klaster | Lulusan P1 tak pernah menyentuh cloud; lulusan P3 tak pernah menyentuh data | Buka *cross-track* maksimal 6 SKS sesuai 025 |
| Semua | 18 SKS peminatan = 12,3% dari 146 SKS | Klaster bukan spesialisasi penuh | Nyatakan eksplisit di dokumen promosi prodi |

## 9. Butir keputusan yang masih terbuka [U]

| Kode | Butir | Mengapa perlu keputusan | Pemilik yang wajar |
|---|---|---|---|
| U-01 | Perbaikan 8 salah label BoK di 005 §4 (§8.2) | Matriks BoK↔MK saat ini menghasilkan hitungan cakupan yang salah | Koordinator kurikulum |
| U-02 | Penyelesaian konflik identitas FST-204 dan FST-205 (§8.3 C-1, C-2) | Menentukan pengampu CS2023 AR dan FPL, serta BK-PL-01 vs BK-PL-05 | RMK FSTI + prodi |
| U-03 | Penambahan CPL-03/CPL-04 pada STB-701 dan STC-703 | Peminatan saat ini tidak menambah capaian komunikasi/etika | Tim CPL |
| U-04 | Pendaftaran BK untuk *Research Methodology* dan *Personality Development* (APT-IS12, APT-IS14) | Dua BK APTIKOM belum berentri di 003 | Tim BoK |
| U-05 | Penetapan BK-IT untuk *Manajemen Proyek* (APT-IT13, penciri utama) | Satu dari 14 BK utama belum punya padanan setara | Tim BoK |
| U-06 | Prasyarat FST-408 → STI-413 dan STI-413 → STI-624 | Kedalaman AI bergantung urutan | Prodi + pengampu |
| U-07 | Apakah istilah resmi tetap **"peminatan"** atau ditambah **"klaster ranting ilmu/bidang ilmu kepakaran"** | Istilah "ranting ilmu" hanya muncul di Panduan KPT DIKTI (021 baris 985), belum di dokumen prodi | Prodi + Senat Fakultas |
| U-08 | Sinkronisasi `BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md` root vs `KURIKULUM2026_REVISI/` (§8.3 C-3) | Dua versi dengan kode MK berbeda beredar | Pengelola repo |
| U-09 | Perbaikan kode `STI-726`/`STI-727` ganda pada 004 baris 144–160 | Master matriks memuat dua MK berbeda dengan kode sama | Pengelola 004 |
| U-10 | Koreksi klaim "AS-IS Sem 6 = 2 MK" pada 025 §2 | Bertentangan dengan 005 (1/1/4) | Penulis 025 |
| U-11 | Penetapan status `+P` atau Teori untuk 5 MK teori murni peminatan (§8.1 G-06) | Menentukan bukti praktik untuk IKU 7 | Prodi |
| U-12 | Pemetaan isi (bukan judul) 18 MK peminatan ke knowledge unit CS2023 | Saat ini seluruhnya [K–tafsir] | Tim RPS |
| U-13 | Pernyataan resmi bahwa `BK-IT02` (*Applied AI*) adalah **BK tambahan prodi**, bukan adopsi APTIKOM TI | Klaster P1 bertumpu pada BK ini (§8.1 G-10) | Tim BoK + Senat |
| U-14 | Koreksi "9 MK" → "8 MK" dan hapus `STI-726` ganda pada 004 Tabel 6.2 baris BK-IT02 | Kesalahan aritmetika tunggal pada master matriks (§8.3 C-4) | Pengelola 004 |
| U-15 | Penetapan BK primer untuk STC-602, STC-701, STC-702 pada 004 §6 | Tiga MK peminatan belum memiliki BK primer (§8.1 G-09) | Tim BoK |

## 10. Cara memakai dan memelihara

1. **Identitas MK hanya dari 005.** Setelah 003/004/005 berubah, jalankan `python3 -B _tools/verify_pemetaan_klaster_ranting.py` (memeriksa 18 MK, SKS/semester/tipe, CPL per MK, 36 kode BK, angka cakupan §5.4, dan klaim salah label §8.2).
2. **Jangan mengutip kolom APTIKOM/CS2023 sebagai bukti pemenuhan.** Kolom itu menunjukkan *ke mana* isi MK dapat dipetakan; bukti pemenuhan menuntut RPS/CPMK per MK (U-12).
3. **Selalu berprefiks.** `BK-IS*`/`BK-IT*` = internal SISTEKIN; `APT-IS*`/`APT-IT*` = APTIKOM resmi; `BK-P1/P2/P3/PL-*` = usulan dokumen ini (§2.1).
4. **Untuk SISTEKIN, dahulukan APTIKOM.** Bila APTIKOM dan CS2023 bertentangan, APTIKOM yang menang karena silsilah BoK prodi adalah IS2020/IT2017/CC2020. CS2023 dipakai untuk memeriksa kedalaman KA, bukan menilai kelengkapan.
5. **Berkas ini tidak menggantikan 003.** 21 BK-IS + 15 BK-IT tetap daftar resmi BoK prodi; `BK-P1/P2/P3/PL-*` adalah rincian tingkat klaster yang masih usulan.
6. Jika laporan CS2023 diperbarui, periksa ulang Tabel 2 dan daftar knowledge unit; nomor halaman berubah antar edisi.

## 11. Rujukan

1. **[S]** Dokumen 003 — Standar 14 CPL, Genealogi Sumber, dan Pemetaan BoK APTIKOM (21 BK-IS + 15 BK-IT beserta nama resmi).
2. **[S]** Dokumen 004 — Matriks Keterlacakan OBE: VMTS ↔ 3 PEO ↔ 4 PL ↔ 14 CPL ↔ 55 MK; §0 tabel persamaan kode CPL; §4 CPL per MK peminatan; §6 Tabel 6.1–6.2 matriks BoK ↔ MK (primer ●/sekunder ○).
3. **[S]** Dokumen 005 — Struktur Kurikulum 8 Semester dan Peminatan; §1.1–1.4 komposisi MK; §3 sebaran semester; §4 skema 3 peminatan dan kolom BoK per MK.
4. **[K]** APTIKOM. *Buku Panduan Kurikulum Berbasis OBE/KKNI/SKKNI, Program Studi S1 Sistem Informasi, versi 2.0*. Tabel 4 (Rumusan Bahan Kajian, 19 BK: 11 Utama, 1 Umum, 7 Pendukung), hlm. 19–20; instruksi adopsi dan pemetaan, hlm. 21–22. Berkas `BUKU_OBE/OBE_SISTEM_INFORMASI_2.0_APTIKOM_837172072-S1-SI-APTIKOM.md`.
5. **[K]** APTIKOM. *Panduan Kurikulum OBE Prodi S1 Teknologi Informasi 2023*. Bab VI §6.1 "Rumusan Bahan Kajian": Tabel 6 memuat 27 BK (14 Penciri Utama BK01–BK14 + 13 Penciri Pendukung BK15–BK27), hlm. PDF 31–39; instruksi "mengadopsi 14 BK Penciri Utama", hlm. PDF 31; pemetaan CPL↔BK (Tabel 7) dan BK↔MK (Tabel 8), hlm. PDF 39–42. Berkas `BUKU_OBE/716903001-PANDUAN-KURIKULUM-OBE-PRODI-S1-TEKNOLOGI-INFORMASI-2023.pdf`.
6. **[K]** Kumar, A., Raj, R. K., Aly, S. G., et al. *Computer Science Curricula 2023 (CS2023)*. ACM/IEEE-CS/AAAI, Januari 2024. DOI [10.1145/3664191](https://doi.org/10.1145/3664191), ISBN 979-8-4007-1033-9. Teks lengkap: <https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm>. Dipakai: Bab 2 (model pengetahuan, Tabel 2 jam CS Core/KA Core, *sunflower model*, langkah desain kurikulum) dan Bab 3 (17 knowledge area beserta knowledge unit). Tautan ResearchGate pada permintaan merujuk laporan yang sama; yang dibaca adalah salinan ACM.
7. **[S]** Dokumen 016, 021, 025, 037 — audit BoK, Panduan KPT DIKTI, rekomendasi *cross-track* 2027, dan *boundary guardrails* antar-MK.
8. **[S]** Dokumen 021 baris 985: "bahan kajian tersebut dapat berupa satu atau lebih cabang ilmu beserta **ranting ilmunya**" — satu-satunya sumber istilah "ranting ilmu" di repo.
