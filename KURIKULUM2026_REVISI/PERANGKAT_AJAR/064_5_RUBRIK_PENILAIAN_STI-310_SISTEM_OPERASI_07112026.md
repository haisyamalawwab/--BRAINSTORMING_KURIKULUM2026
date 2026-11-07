# 064_5 — RUBRIK PENILAIAN PEMBELAJARAN BERBASIS OBE
## STI-310 — SISTEM OPERASI (*Operating Systems*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI310` · **Klaster Rubrik Master (Dok 018):** Klaster 3 (`K-3`)  
**CPL:** `CPL-07` (`P3` = 50%) & `CPL-11` (`KK3` = 50%) [Level `R`]  
**Tanggal Penyusunan:** 07 November 2026  

---

## BAGIAN I — PRINSIP PENILAIAN INFRASTRUKTUR & SISTEM OPERASI (`K-3`)

Mengacu **Dokumen 018 §3**, rubrik penilaian Klaster 3 (`K-3`) untuk `STI-310 Sistem Operasi` menimbang secara presisi: (1) akurasi analitis-kuantitatif mekanisme internal kernel (penjadwalan CPU, sinkronisasi/*deadlock*, dan memori virtual), (2) kebenaran fungsional & postur keamanan (*least privilege*) konfigurasi **Linux Server** dan kontainer **Docker**, serta (3) objektivitas pengukuran kinerja memori virtual dan sistem berkas pada beban nyata.

---

## BAGIAN II — RUBRIK ANALITIK 4 TITIK EVALUASI SUMATIF

### 2.1 Rubrik Analitik Tugas 1 (Pekan 4 — Bobot 20% MK · Mengukur `CPMK-1` / `Sub-CPMK-1.1` → `CPL-07` [C4])
**Objek Penilaian:** Studi Kasus Analitis & Simulasi Penjadwalan CPU (*FCFS, SJF, SRTF, Priority, Round Robin*) + Kuis Verifikasi Kelas.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Akurasi *Gantt Chart* & Aturan Preempsi/Antrean** | **35%** | Seluruh *Gantt Chart* (FCFS, SJF, SRTF, Priority, RR 2 variasi $q$) 100% akurat termasuk urutan antrean *ready queue* saat *arrival time* bersamaan dan titik potong preempsi. | *Gantt Chart* seluruh algoritma benar; hanya terdapat 1 kekeliruan urutan tie-break minor pada antrean *Round Robin*. | *Gantt Chart* algoritma non-preemptif benar, namun terdapat kekeliruan titik potong pada SRTF atau RR. | Mencampuradukkan SJF non-preemptif dengan SRTF atau mengabaikan kolom *arrival time*. | Tidak mampu menyusun *Gantt Chart* eksekusi CPU. |
| **2. Presisi Perhitungan AWT, ATAT, *Response Time*, & *Context Switch*** | **35%** | Seluruh tabel *Completion, Turnaround, Waiting, Response Time*, rata-rata, dan jumlah *Context Switch* dihitung 100% tepat sesuai parameter NIM. | Rumus dan langkah perhitungan benar seluruhnya, hanya terselip 1 salah hitung aritmetika kecil. | Menghitung AWT dan ATAT dengan benar, namun melewatkan perhitungan *Response Time* atau jumlah *Context Switch*. | Salah menerapkan rumus dasar (`TAT = CT - AT`, `WT = TAT - BT`) pada sebagian besar tabel. | Angka metrik disalin/ditebak tanpa dasar perhitungan. |
| **3. Analisis *Convoy Effect, Starvation, Quantum* & Rekomendasi** | **20%** | Menganalisis tajam penyebab perbedaan performa antar-algoritma, pengaruh ukuran kuota $q$ terhadap *overhead context switch*, mekanisme *aging*, dan memberi rekomendasi tepat. | Analisis perbandingan kelima algoritma logis dan didukung langsung oleh angka hasil simulasi. | Menyimpulkan algoritma tercepat berdasarkan angka rata-rata, namun analisis penyebabnya masih dangkal. | Kesimpulan bertentangan dengan data tabel perhitungan sendiri. | Tidak ada bagian analisis dan evaluasi kebijakan penjadwalan. |
| **4. Kerapian Dokumentasi & Konsistensi Kuis Verifikasi** | **10%** | Laporan sangat rapi (dilengkapi tabel/grafik jelas) dan mahasiswa menjawab soal kuis verifikasi kelas dengan sempurna. | Laporan terstruktur rapi dan hasil kuis verifikasi selaras baik. | Laporan cukup rapi dan lulus batas minimal kuis verifikasi. | Parameter tidak sesuai NIM atau skor kuis verifikasi jomplang dari laporan. | Plagiarisme atau gagal total saat verifikasi kelas. |

$$\text{Skor Tugas 1} = 0,35(K_1) + 0,35(K_2) + 0,20(K_3) + 0,10(K_4)$$

---

### 2.2 Rubrik Analitik Ujian Tengah Semester / UTS (Pekan 8 — Bobot 30% MK · `CPMK-1` [15%] & `CPMK-3` [15%] → `CPL-07` [C4/C5])
**Objek Penilaian:** Jawaban Ujian Tertulis 150 Menit: Sinkronisasi/*Deadlock* (Bagian A — 50% UTS) & Memori Virtual (Bagian B — 50% UTS).

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Analisis Sinkronisasi (*Mutex / Semaphore*)**<br>(Bagian A1 — `Sub-CPMK-1.2`) | **25%** | Tepat menunjukkan skenario interleaving penyebab *race condition* dan menyusun penempatan `wait()/signal()` atau `lock()/unlock()` yang bebas *race condition* sekaligus bebas *deadlock*. | Diagnosis *race condition* tepat dan perbaikan *semaphore/mutex* memenuhi *mutual exclusion* dengan baik. | Mengenali letak *critical section*, namun nilai inisialisasi *counting semaphore* kurang tepat. | Menempatkan `wait()` terbalik sehingga justru memicu *deadlock* baru. | Tidak memahami cara kerja *mutex* dan *semaphore*. |
| **2. Penanganan *Deadlock* & **Banker's Algorithm****<br>(Bagian A2 — `Sub-CPMK-1.2`) | **25%** | Matriks `Need = Max - Allocation`, simulasi pembaruan vektor `Work`, pembuktian *Safe Sequence*, dan uji kelayakan *Resource Request* baru 100% akurat. | Prosedur *Banker's Algorithm* dan penentuan status aman/tidak aman benar; hanya ada 1 kekeliruan aritmetika kecil. | Mampu menghitung matriks `Need` dan menguji sebagian proses, namun terhenti sebelum memeriksa permintaan baru. | Salah rumus `Need` (`Allocation - Max`) sehingga seluruh analisis status aman keliru. | Gagal mengerjakan soal *deadlock* & *Banker's Algorithm*. |
| **3. Evaluasi Translasi **Paging/Segmentation** & **EAT/TLB****<br>(Bagian B1 — `Sub-CPMK-3.1`) | **25%** | Pemisahan bit halaman/offset, translasi alamat fisik (termasuk cek *limit/invalid bit*), serta perhitungan **Effective Access Time (EAT)** bertingkat TLB + *Page Fault* 100% presisi. | Translasi alamat dan rumus EAT benar; hanya terdapat 1 kekeliruan konversi satuan nanodetik–milidetik. | Mampu menerjemahkan alamat *paging* dasar, namun rumus pembobotan probabilitas *TLB hit/miss* kurang tepat. | Tertukar antara nomor halaman logis dan nomor bingkai fisik serta salah rumus EAT. | Tidak mampu menerjemahkan alamat memori maupun menghitung EAT. |
| **4. Evaluasi *Page Replacement* (**FIFO, OPT, LRU**) & *Thrashing***<br>(Bagian B2 — `Sub-CPMK-3.1`) | **25%** | Tabel jejak bingkai halaman **FIFO, Optimal,** dan **LRU** akurat tanpa salah langkah, *Page Fault / Hit Ratio* eksak, dan evaluasi gejala *Thrashing / Working Set* sangat tajam. | Jejak ketiga algoritma benar dengan selisih maksimal 1 kolom pada untai panjang; evaluasi kinerja tepat. | Mengerjakan FIFO dan LRU dengan cukup benar, namun keliru menentukan halaman terjauh ke depan pada algoritma Optimal. | Bingkai halaman diisi tanpa mengikuti aturan korban (*victim frame*) algoritma yang diminta. | Bagian *Virtual Memory* kosong atau salah konsep total. |

$$\text{Skor UTS} = 0,25(K_1) + 0,25(K_2) + 0,25(K_3) + 0,25(K_4) \quad (\text{Bagian A} = K_1+K_2;\ \text{Bagian B} = K_3+K_4)$$

---

### 2.3 Rubrik Analitik Tugas 2 (Pekan 12 — Bobot 20% MK · Mengukur `CPMK-2` / `Sub-CPMK-2.1` → `CPL-11` [C3])
**Objek Penilaian:** Konfigurasi **Linux Server** (*Bash CLI Scripting, POSIX Permissions, & `systemd` Service*) + Verifikasi Terminal Kelas.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Konfigurasi Identitas & **Permission POSIX** (*Least Privilege*)** | **35%** | Struktur user/group, izin oktal/simbolik, `umask`, bit khusus (`SGID` & *Sticky Bit*), serta ACL dikonfigurasi presisi tanpa celah izin berlebih (*zero `777` abuse*). | Konfigurasi user/group dan izin `chmod/chown` berfungsi benar mengamankan akses antar-divisi. | Izin dasar pemilik/grup/publik berjalan sesuai kebutuhan, namun lupa menerapkan `SGID` atau *Sticky Bit* pada folder kolaborasi. | Memberikan izin tulis publik berlebihan (`777` / `666`) yang melanggar prinsip keamanan sistem operasi. | Gagal mengonfigurasi manajemen akun dan izin berkas Linux. |
| **2. Fungsionalitas & Ketangguhan Skrip Otomasi **Bash CLI**** | **35%** | Skrip Bash modular, memakai `set -euo pipefail`, memvalidasi input, merangkai pipa utilitas Linux secara elegan, dan terjadwal otomatis dengan benar. | Skrip Bash berjalan lancar menghasilkan laporan kesehatan/audit server sesuai spesifikasi tugas. | Skrip Bash berjalan untuk kondisi normal, namun belum menangani galat apabila berkas log kosong/tidak ditemukan. | Skrip mengandung banyak galat sintaks Bash dan gagal berjalan tuntas. | Tidak menyertakan skrip otomasi Bash buatan sendiri. |
| **3. Konfigurasi Layanan Daemon **`systemd`** & Pemulihan** | **20%** | Berkas unit `.service` rapi, berjalan di bawah akun *non-root*, aktif saat *boot* (`enabled`), terbukti bangkit otomatis saat diuji `kill -9`, dan terlacak bersih di `journalctl`. | Unit `systemd` aktif berjalan (`active (running)`) dan fitur *auto-restart* berfungsi baik. | Unit `systemd` berhasil dijalankan manual, namun masih memakai akun `root` atau belum di-*enable* saat *boot*. | Berkas unit gagal dimuat (`failed`) karena kesalahan direktif `[Service]`. | Tidak mengonfigurasi layanan `systemd`. |
| **4. Dokumentasi Reproduksibel & Verifikasi Perintah Langsung** | **10%** | Seluruh langkah terdokumentasi rapi ber-`hostname` NIM dan mahasiswa sigap mengeksekusi modifikasi perintah langsung saat diuji di kelas. | Dokumentasi lengkap dan mahasiswa menjawab verifikasi perintah terminal dengan tepat. | Dokumentasi cukup jelas dan lulus verifikasi dasar di kelas. | Tidak mampu mengulang perintah dasar `chmod` / `systemctl` tanpa menyontek catatan panjang. | Tangkapan layar palsu/milik rekan lain. |

$$\text{Skor Tugas 2} = 0,35(K_1) + 0,35(K_2) + 0,20(K_3) + 0,10(K_4)$$

---

### 2.4 Rubrik Analitik Evaluasi Akhir Semester / UAS (Pekan 16 — Bobot 30% MK · `CPMK-2` [15%] & `CPMK-3` [15%] → `CPL-11` [C3 & C5])
**Objek Penilaian:** Bundel Konfigurasi Server Linux/Docker (`Sub-CPMK-2.2`) + Laporan Evaluasi Kuantitatif Kinerja Memori Virtual & Sistem Berkas (`Sub-CPMK-3.1 & 3.2`) + Sidang Terminal Individu.

| Dimensi Kriteria (`K-3`) | Bobot | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Kurang (56–64) | Sangat Kurang (0–55) |
|---|:---:|---|---|---|---|---|
| **1. Konfigurasi Kontainerisasi Dasar **Docker** & Keamanan OS**<br>(`Sub-CPMK-2.2` — Poros `CPMK-2`) | **40%** | `Dockerfile` ringkas-efisien, wajib berjalan sebagai *non-root*, *Docker Volume* menjaga persistensi berkas dengan izin tepat, dan kuota memori/CPU `cgroups` terkonfigurasi fungsional tanpa celah. | Kontainer Docker terbangun bersih, layanan aplikasi berjalan fungsional dengan *volume* persisten dan pembatasan sumber daya. | Aplikasi berhasil berjalan di dalam kontainer Docker dengan *volume*, namun masih berjalan sebagai `root` atau *image* belum dioptimalkan. | `Dockerfile` gagal di-*build* ulang secara mandiri atau data hilang setiap kontainer di-*restart*. | Tidak berhasil mengonfigurasi kontainer Docker yang fungsional. |
| **2. Evaluasi Kuantitatif Kinerja **Memori Virtual** & **Sistem Berkas****<br>(`Sub-CPMK-3.1 & 3.2` — Poros `CPMK-3`) | **40%** | Menyajikan data eksperimen kuantitatif nyata (*RSS, minor/major page faults, swap si/so, IOPS, throughput MB/s, await latency*) pada variasi beban kerja, membandingkan eksekusi *native* vs kontainer berkuota memori secara tajam dan akurat. | Pengukuran metrik memori virtual dan I/O sistem berkas lengkap, tabel/grafik akurat, dan kesimpulan evaluasi objektif. | Menyajikan hasil pengukuran pemakaian RAM dan kecepatan baca/tulis disk dasar, namun analisis kaitan dengan *page fault* / *caching* masih deskriptif. | Hanya menampilkan tangkapan layar `top` sesaat tanpa skenario beban uji maupun analisis kuantitatif. | Tidak ada pengujian dan evaluasi kuantitatif kinerja memori/berkas. |
| **3. Penguasaan Terminal Langsung & Sidang Individu** | **20%** | Mahasiswa sangat fasih mendemonstrasikan perintah Linux CLI, inspeksi `docker inspect/stats`, dan pembacaan metrik `vmstat/iostat` secara langsung tanpa keraguan. | Mahasiswa lancar mendemonstrasikan kontainer dan menjelaskan makna metrik kinerja hasil eksperimennya. | Mahasiswa mampu menjalankan perintah utama proyeknya dengan sedikit petunjuk penguji. | Gagap mengoperasikan terminal Linux/Docker atas proyek yang diklaim miliknya. | Tidak hadir sidang UAS atau melanggar integritas akademik. |

$$\text{Skor UAS} = 0,40(K_1) + 0,40(K_2) + 0,20(K_3)$$

---

## BAGIAN III — RUBRIK FORMATIF LATIHAN CLI & PEMECAHAN SOAL MINGGUAN

| Kriteria Formatif | Sangat Baik (86–100) | Baik (76–85) | Cukup (65–75) | Perlu Pembinaan (< 65) |
|---|---|---|---|---|
| **Ketepatan Latihan Hitung Kernel (Mg 2–7)** | Menyelesaikan latihan penjadwalan, *Banker's Algorithm*, dan *paging* di kelas secara mandiri dan tepat. | Menyelesaikan latihan dengan langkah benar dan aktif berdiskusi. | Mengikuti penyelesaian soal namun masih memerlukan koreksi rumus. | Pasif dan tidak mengerjakan lembar latihan kelas. |
| **Kedisiplinan Administrasi CLI Aman (Mg 9–15)** | Selalu mempraktikkan *least privilege*, memeriksa manual `man`, dan menguji layanan secara tertib di VM Linux. | Menjalankan seluruh latihan konfigurasi Linux & Docker mingguan dengan tuntas. | Menyelesaikan sebagian besar latihan CLI dengan panduan rekan. | Tidak menyiapkan lingkungan VM Linux sehingga tertinggal latihan. |

---

## BAGIAN IV — RUBRIK HOLISTIK MATA KULIAH (SKALA 5 TINGKAT — KPT 2024 TABEL 18 & DOK 033)

| Skor Holistik | Predikat | Deskriptor Penguasaan Utuh `STI-310` (`CPL-07` & `CPL-11` — Level *Reinforce*) |
|:---:|---|---|
| **5** | **Istimewa (*Outstanding*)** | Mahasiswa menguasai analisis mendalam penjadwalan CPU dan sinkronisasi/*deadlock*, mampu mengonfigurasi server Linux (`Bash, POSIX, systemd`) dan kontainer **Docker** secara aman-andal, serta mengevaluasi kinerja memori virtual dan sistem berkas secara kuantitatif tajam. |
| **4** | **Sangat Baik (*Excellent*)** | Mahasiswa menganalisis mekanisme proses/memori dengan akurat, terampil mengonfigurasi lingkungan Linux dan Docker dasar, serta mampu menyajikan evaluasi kuantitatif beban kerja sistem operasi dengan tepat. |
| **3** | **Baik (*Proficient — Ambang Lulus OBE*)** | Mahasiswa memenuhi ambang ketuntasan minimal OBE ($\ge 65,0$) dalam perhitungan penjadwalan/memori dasar, konfigurasi fungsional Linux CLI/POSIX/`systemd`/Docker, serta pengukuran dasar kinerja sistem. |
| **2** | **Kurang (*Developing*)** | Mahasiswa masih sering keliru menganalisis *deadlock*/memori virtual dan belum mampu mengonfigurasi layanan Linux/Docker secara mandiri dan aman. |
| **1** | **Sangat Kurang (*Inadequate*)** | Mahasiswa gagal menguasai konsep dasar maupun keterampilan konfigurasi sistem operasi atau melanggar kejujuran akademik. |

---

## BAGIAN V — RUBRIK SKALA PERSEPSI & REFLEKSI DIRI MAHASISWA (LIKERT 1–5 — KPT 2024 TABEL 20)

**Skala:** `5 = Sangat Mampu` · `4 = Mampu` · `3 = Cukup Mampu` · `2 = Kurang Mampu` · `1 = Sangat Tidak Mampu`.

| No | Pernyataan Refleksi Penguasaan Kompetensi `STI-310` | Sub-CPMK | Skala |
|:---:|---|---|:---:|
| 1 | Saya mampu menganalisis algoritma penjadwalan prosesor (*FCFS, SJF, Round Robin, Priority*) secara akurat. | `Sub-CPMK-1.1` | 1 – 2 – 3 – 4 – 5 |
| 2 | Saya mampu menganalisis mekanisme sinkronisasi (*mutex, semaphore*) dan penanganan *deadlock* (*Banker's Algorithm*). | `Sub-CPMK-1.2` | 1 – 2 – 3 – 4 – 5 |
| 3 | Saya mampu mengonfigurasi lingkungan Linux Server (*Bash CLI, permission POSIX, systemd service*) secara fungsional dan aman. | `Sub-CPMK-2.1` | 1 – 2 – 3 – 4 – 5 |
| 4 | Saya mampu mengonfigurasi kontainerisasi dasar (**Docker**) beserta persistensi *volume* untuk kebutuhan server aplikasi. | `Sub-CPMK-2.2` | 1 – 2 – 3 – 4 – 5 |
| 5 | Saya mampu mengevaluasi kinerja manajemen memori virtual (*paging, segmentation, page replacement*) secara kuantitatif. | `Sub-CPMK-3.1` | 1 – 2 – 3 – 4 – 5 |
| 6 | Saya mampu mengevaluasi kinerja sistem berkas dan I/O penyimpanan pada skenario beban kerja komputasi nyata. | `Sub-CPMK-3.2` | 1 – 2 – 3 – 4 – 5 |

---

## BAGIAN VI — TEMPLAT LEMBAR PENILAIAN CEPAT DOSEN (*SPEED GRADING SHEET* `STI-310`)

```text
==============================================================================================================================
                 LEMBAR REKAPITULASI PENILAIAN OBE — STI-310 SISTEM OPERASI (3 SKS TEORI)
==============================================================================================================================
Semester / TA  : Semester 3 (Ganjil) / 2026-2027     CPL Dibebankan : CPL-07 (P3: 50%) & CPL-11 (KK3: 50%) [Level: Reinforce]
Klaster Rubrik : K-3 (Infrastruktur & Sistem Operasi) Ambang OBE    : >= 65.0 (Target Ketuntasan Kohor >= 80%)
------------------------------------------------------------------------------------------------------------------------------
No | NIM       | Nama Mahasiswa   | T1 (20%)  | UTS (30%)      | T2 (20%)  | UAS (30%)      | NA    | CPL-07 | CPL-11 | Huruf
   |           |                  | [CPMK-1]  | [C1:15|C3:15]  | [CPMK-2]  | [C2:15|C3:15]  | Akhir | (50%)  | (50%)  | Mutu
------------------------------------------------------------------------------------------------------------------------------
1  | 250101001 | [Nama Mhs 1]     | 86.0      | 84.0 (84|84)   | 88.0      | 86.0 (88|84)   | 85.80 | 84.80  | 86.80  | A
2  | 250101002 | [Nama Mhs 2]     | 78.0      | 74.0 (76|72)   | 80.0      | 76.0 (78|74)   | 76.60 | 75.60  | 77.60  | B+
3  | 250101003 | [Nama Mhs 3]     | 68.0      | 66.0 (66|66)   | 70.0      | 68.0 (70|66)   | 67.80 | 66.80  | 68.80  | C+
------------------------------------------------------------------------------------------------------------------------------
RATA-RATA KELAS                   | 77.33     | 74.67          | 79.33     | 76.67          | 76.73 | 75.73  | 77.73  | >=65:100%
==============================================================================================================================
```
