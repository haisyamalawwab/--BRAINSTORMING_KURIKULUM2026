# Audit penyelarasan STI-311 dan dampak pada mata kuliah hilir

**Tanggal kerja:** 7 November 2026. **Status:** hasil audit dan rekomendasi kerja, belum merupakan pengesahan atau keputusan resmi prodi.

## 1. Lingkup perubahan dan sumber

Dokumen 005 tetap menjadi sumber identitas: `STI-311` Pengembangan Web Front End (*Web Front End Development*), semester 3, 3 SKS `+P`, prasyarat `FST-102`. Tidak ada perubahan pada struktur SKS atau prasyarat. Pemetaan `CPL-08` (`P4`), `CPL-13` (`KK5`) dan tingkat R tetap mengikuti Dok 003/004; mata kuliah ini hanya memberi kontribusi dasar pada CPL yang cakupannya lebih luas.

Rancangan baru mencakup HTML/CSS dasar–menengah, Flexbox lanjutan, pengenalan Bootstrap dan Tailwind serta JavaScript dasar; tugas kalkulator menggunakan salah satu framework dan UAS berupa landing page interaktif. React/SPA, Fetch/asinkron dan konsumsi API bukan lagi capaian STI-311. Rujukan operasional: `043_STI-311_WEB_FRONT_END_DEVELOPMENT_DASAR_USULAN_07112026.md` dan paket `PERANGKAT_AJAR/065_1`–`065_5`.

## 2. Dokumen yang diperbarui dan yang belum

| Dokumen | Tindakan / status |
|---|---|
| Dok 043 induk dan varian aktif per semester | Rumusan, Sub-CPMK, 16 pertemuan dan batas khusus STI-311 diperbarui; ringkasan STI-311 di induk turut diselaraskan. Mata kuliah lain tidak diubah. |
| Ekstraksi `043_STI-311_...30092026.md` | Diperbarui, dengan catatan bahwa tidak lagi verbatim historis. Versi awal dapat ditelusuri di riwayat Git. |
| Dok 007, Dok 037 dan buku kompilasi | Bagian silabus/guardrails STI-311 diperbarui; dokumen lain tidak otomatis berubah. |
| `PERANGKAT_AJAR/065_1`–`065_5` | RPS, SAP, outline 14 bab, rencana asesmen dan rubrik diselaraskan dengan rancangan 16 pertemuan dan bobot 20/25/25/30. |
| Dok 009D, 012 dan 017 | Klaim bahwa React/Vue merupakan capaian STI-311 dikoreksi; indikator CPL yang lebih luas tetap membutuhkan bukti dan penempatan lanjutan. |
| RPS `070_1`/SAP `070_2` dan RPS pilot STI-416 | Koreksi klaim bahwa Fetch/Axios atau konsumsi API sudah dikuasai dari STI-311. |
| RPS `076_1` dan `098_1` | Tambah peringatan kesenjangan prasyarat, tanpa mengubah CPMK, bobot atau jadwal MK hilir. |
| Dok 043 backup, RPS pilot STI-311 lama | Dipertahankan sebagai artefak historis dan diberi peringatan; isinya bukan rujukan rancangan saat ini. Generator pilot lama juga perlu ditinjau sebelum dipakai. |
| XLSX, DOCX/PDF dan berkas turunan lain | **Belum diperbarui**. Workbook atau ekspor yang masih memuat silabus lama tidak boleh dianggap selaras; perubahan saat ini hanya Markdown. Generator dan ekspor perlu diaudit bila prodi menghendaki regenerasi. |

## 3. Audit langsung MK hilir berdasarkan Dok 005

Ketiga MK di bawah mencantumkan STI-311 sebagai prasyarat. Penilaian dan usulan mitigasi tidak mengubah beban, jadwal atau CPMK mereka secara otomatis.

| MK dan bukti dokumen | Bekal yang aman diasumsikan / kesenjangan | Waktu dan asesmen yang berisiko | Rekomendasi tanpa penambahan beban otomatis |
|---|---|---|---|
| **STI-416** semester 4, 3 SKS +P; prasyarat `FST-207`, `STI-311`. `070_1` dan `070_2`: HTTP/REST dan Async I/O di pertemuan 1. | Ada HTML/CSS/Flexbox dan JS dasar; **tidak** diasumsikan mahasiswa telah mempelajari Fetch/Axios, asinkron atau konsumsi API. Pilihan Node.js juga menuntut kesiapan asinkron yang belum dijamin. | Materi server/API sudah dimulai pertemuan 1 dan Tugas 1 pada minggu 4; praktik klien atau uji API tidak boleh mensyaratkan Fetch yang belum diajarkan. | Diagnosis awal; jelaskan semantik request/response HTTP dan alat uji API pada sesi pengantar yang ada. Gunakan curl/Postman/klien uji untuk asesmen backend; bila jalur Node dipilih, pengampu menilai kesiapan async dan menyiapkan bahan pengantar. Evaluasi kembali ruang dan bukti belajar sebelum menetapkan perubahan SAP. |
| **STI-522** semester 5, 3 SKS +P; prasyarat `STI-311`, `STI-416`. `076_1`: Flutter/Dart, BLoC minggu 7 dan sinkronisasi API. | Dasar logika dan event dapat ditransfer, tetapi React, framework mobile, state dan konsumsi API tidak dijamin dari STI-311; kemampuan API dari STI-416 perlu dibuktikan, terutama aspek konsumsi pada klien. | Praktik BLoC minggu 7 serta asesmen integrasi/persistensi mobile berisiko bila Dart, state atau komunikasi API belum dikuasai. | Diagnostik awal dan bahan pengantar Dart/Flutter pada sesi yang sudah direncanakan; sediakan contoh kontrak dan klien API serta cek kesiapan sebelum asesmen. Tinjau waktu dan rubrik jika hasil diagnostik menunjukkan kesenjangan. |
| **STC-701** semester 7, 3 SKS +P; prasyarat `STI-311`. `098_1`: Three.js minggu 3, Tugas 1 scene 3D minggu 4, AR/VR berikutnya. | STI-311 memberi dasar browser dan JS, bukan modul JS, Three.js, grafika 3D atau WebXR. | Hanya dua pertemuan sebelum praktik Three.js; Tugas 1 minggu 4 berisiko bergantung pada pengetahuan yang belum dijamin. | Lakukan diagnostik awal; sediakan contoh beranotasi dan pengantar objek/modul JS serta scene 3D dalam pertemuan awal yang ada. Tinjau ulang kelayakan Tugas 1, alokasi waktu dan alternatif perangkat sebelum persetujuan RPS. |

**MK hilir tidak langsung:** `STI-625`, `STI-726`, `STC-602` dan `STC-702` memiliki jalur melalui `STI-416` menurut Dok 005. Ketersediaan backend/API dari STI-416 tidak sama dengan bukti kemampuan integrasi klien, React atau asinkron; pengampu perlu mengecek kebutuhan riil masing-masing. Audit ini belum menyatakan seluruh tugas MK hilir sudah direvisi atau aman.

## 4. Usulan penempatan materi yang dihapus

| Materi | Usulan eksplisit | Status / alasan |
|---|---|---|
| HTTP/REST sisi server dan uji endpoint | Tetap diperkenalkan pada pertemuan awal **STI-416** sesuai materi yang sudah ada; uji menggunakan alat klien. | Rekomendasi operasional dalam alokasi yang sudah tercantum, bukan perubahan SKS. |
| Konsumsi API klien, Fetch dan async/await | **Perlu dibekalkan sebelum tugas hilir yang benar-benar memerlukannya**. Usulkan klinik/pengayaan terpisah atau penempatan terbatas pada sesi MK yang memerlukannya; pemilik materi, waktu dan asesmen diputuskan prodi. | Belum ditetapkan sebagai capaian resmi MK tertentu; jangan mengasumsikan sudah diajarkan. |
| React/SPA, routing dan state framework | **Tidak diwajibkan pada STI-311.** Usulkan pengayaan terpisah bersifat opsional atau penempatan pada MK lanjutan jika audit kebutuhan membuktikannya. | Belum dialokasikan ke MK tertentu; tidak boleh disyaratkan tanpa pembelajaran yang tersedia. |
| Lighthouse/optimasi produksi lanjutan | Tidak diperlukan untuk capaian STI-311; bila kebutuhan MK hilir terbukti, dapat dibahas pada MK terkait atau pengayaan terpisah. | Belum ada keputusan menambah pertemuan, SKS atau kewajiban. |
| WebXR/Three.js dan Dart/Flutter | Tetap ranah **STC-701** dan **STI-522** masing-masing; STI-311 tidak menjadi bukti penguasaan. | Pengampu memvalidasi kesiapan, bahan awal dan kecukupan waktu/asesmen. |

Pengayaan yang diusulkan tidak dianggap telah tersedia, wajib, atau disetujui. Koordinator perlu menentukan penyelenggara, materi, jadwal, sumber daya, asesmen dan apakah dapat ditampung dalam waktu yang ada.

## 5. Keputusan dan pengesahan

| Keputusan yang diperlukan | Penanggung jawab | Status / tanggal |
|---|---|---|
| Kelayakan ruang lingkup, CPL/IRM dan 16 pertemuan STI-311 | Koordinator RMK dan prodi | **Belum ditetapkan** |
| Penempatan materi Fetch/asinkron, React dan optimasi; kesiapan MK hilir serta kecukupan waktu | Koordinator MK terkait dan prodi | **Belum ditetapkan** |
| Validasi RPS, SAP, rubrik, asesmen dan beban kerja | Pengampu, koordinator RMK, prodi dan unit mutu | **Belum disahkan** |
| Regenerasi/penandaan versi XLSX, DOCX/PDF dan generator lama | Pengelola dokumen prodi | **Belum ditetapkan** |

Tanda tangan, nama pengesah dan tanggal keputusan diisi oleh pihak berwenang setelah peninjauan; tidak ada persetujuan yang diasumsikan dalam laporan ini.
