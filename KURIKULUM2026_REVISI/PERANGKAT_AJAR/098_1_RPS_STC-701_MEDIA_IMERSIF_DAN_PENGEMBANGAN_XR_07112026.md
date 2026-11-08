# 098_1 — RENCANA PEMBELAJARAN SEMESTER BERBASIS OBE

## STC-701 — Media Imersif & Pengembangan XR

**Identitas:** `STC-701` Media Imersif & Pengembangan XR · Semester 7 · 3 SKS (+P) · Prasyarat `STI-311` · PL PL-3 · PEO PEO-1, PEO-3 · IRM M.

## Identitas dan pengesahan

Prodi S1 SISTEKIN FSTI UWG. Koordinator, dosen dan tanggal pengesahan diisi oleh program studi. Beban mingguan: TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit. PT = tugas terstruktur; BM = belajar mandiri.

## CPL dibebankan

| CPL | Rumusan resmi Dok 003 | IRM |
| --- | --- | --- |
| CPL-08 (P4) | Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX). | M |
| CPL-13 (KK5) | Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (*Microservices, Web/Mobile, API, SaaS, BPA*). | M |

## CPMK dan Sub-CPMK

| CPMK | Rumusan ABCD Dok 043 | Bloom | CPL |
| --- | --- | --- | --- |
| CPMK-1 | Mahasiswa (*A*) mampu **membangun** adegan grafika 3D interaktif di browser (*B*) menggunakan WebXR dan Three.js (*C*) dengan pemuatan model 3D (glTF/GLB) yang optimal (*D*). | C3 | `CPL-08` (`P4`) |
| CPMK-2 | Mahasiswa (*A*) mampu **merancang dan mengimplementasikan** aplikasi Augmented Reality (AR) mobile (*B*) dengan teknik Marker-Based dan Markerless Plane Detection (*C*) menggunakan ARCore / WebXR (*D*). | C6 | `CPL-13` (`KK5`) |
| CPMK-3 | Mahasiswa (*A*) mampu **membangun** simulasi Virtual Reality (VR) 6DoF interaktif (*B*) dengan audio spasial 3D dan navigasi teleportasi (*C*) dengan performa rendering mulus $\ge 60$ FPS (*D*). | C6 | `CPL-13` (`KK5`) |

| Sub-CPMK | Kompetensi Dok 043 | CPMK sumber | Bloom |
| --- | --- | --- | --- |
| Sub-CPMK-1.1 | Menerapkan teknologi XR (AR, VR, MR) pada aplikasi imersif. | CPMK-1 | C3 |
| Sub-CPMK-1.2 | Membuat dan mengelola 3D asset menggunakan WebGL/Three.js. | CPMK-1 | C3 |
| Sub-CPMK-2.1 | Mengimplementasikan interaksi kontroller dan gestur spasial. | CPMK-2 | C6 |
| Sub-CPMK-2.2 | Mengintegrasikan Computer Vision/AI untuk pengalaman imersif. | CPMK-2 | C6 |
| Sub-CPMK-3.1 | Membangun aplikasi immersive/XR end-to-end yang dapat dijalankan. | CPMK-3 | C6 |
| Sub-CPMK-3.2 | Mengevaluasi kualitas dan performa pengalaman imersif. | CPMK-3 | C6 |

## Matriks CPL–CPMK dan bobot asesmen

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-08` (`P4`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-13` (`KK5`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-13` (`KK5`) | — | — | 25% | 30% | 55% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Bobot merupakan rancangan penilaian MK; CPMK yang mendukung lebih dari satu CPL tidak menggandakan nilai akhir. Nilai CPL tingkat prodi mengikuti formula Dok 008.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana 16 pertemuan

| Mg | Kemampuan | Materi | Metode | Beban | Asesmen |
| --- | --- | --- | --- | --- | --- |
| 1 | Mampu menguraikan spektrum Extended Reality (AR, VR, MR) dan Spatial Computing (C2) | Pengantar Immersive Media, Taksonomi Milgram, Hardware VR/AR Headset | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 2 | Mampu menguraikan fondasi grafika 3D: Ruang Koordinat, Mesh, Tekstur, Material (C2) | Grafika 3D: Vektor 3D, Poligon, Shaders, PBR Materials, Format glTF/GLB | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 3 | Mampu membangun adegan 3D dasar via Three.js: Scene, Camera, Renderer (C3) | WebXR Three.js Fundamentals: Scene Graph, Perspective Camera, Render Loop | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 4 | Mampu mengimplementasikan interaktivitas 3D: Raycasting & Orbit Controls (C3) | Interaksi Grafika: Raycasting, Object Picking, Mouse/Touch Event Handling | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 1 20% |
| 5 | Mampu memprogram pencahayaan dinamis, bayangan, dan Custom GLSL Shaders (C4) | Pencahayaan 3D: Directional Light, Shadow Maps, Custom Vertex/Fragment Shader | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 6 | Mampu menguraikan konsep Augmented Reality: Pelacakan Pose & Estimasi Cahaya (C2) | Pengantar Mobile AR: Arsitektur ARCore/ARKit, SLAM Tracking, Surface Detection | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 7 | Mampu membangun aplikasi AR Marker-Based dengan pengenalan target gambar 2D (C3) | Marker-Based AR: Image Target Tracking & Overlay Objek 3D Interaktif | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 8 | EVALUASI TENGAH SEMESTER (UTS) | Ujian Koding Terjadwal Three.js 3D Web & Aplikasi Marker-Based AR | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UTS 25% |
| 9 | Mampu membangun aplikasi Markerless AR berbasis Plane Detection (C6) | Markerless AR: Deteksi Permukaan Lantai/Meja & Penempatan Objek Spasial | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 10 | Mampu merancang interaksi gestur spasial: Rotasi, Skala, dan Pinch objek AR (C4) | Spatial Gesture Interaction: Two-Finger Pinch Scale, Drag Move, Yaw Rotation | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 11 | Mampu menguraikan prinsip imersi Virtual Reality: 3DoF vs 6DoF & Comfort (C2) | Pengantar VR: 6DoF Head/Hand Tracking, Mencegah Motion Sickness Guidelines | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 12 | Mampu memprogram navigasi VR Teleportasi dan interaksi kontroler 6DoF (C3) | VR Development: WebXR VR Session, Teleport Locomotion, Controller Grab | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Tugas 2 25% |
| 13 | Mampu mengonfigurasi Audio Spasial 3D untuk meningkatkan imersi virtual (C3) | Spatial Audio: Positional Audio 3D, Audio Listener, Reverberation Effect | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 14 | Mampu mengoptimalkan performa rendering grafika XR target $\ge 60$ FPS (C5) | XR Optimization: Draw Calls Reduction, Texture Compression, Level of Detail (LOD) | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 15 | Mampu membangun simulasi pelatihan industri / tur virtual XR terpadu (C6) | PjBL XR Studio: Pengembangan Purwarupa Simulasi VR/AR Interaktif Lengkap | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | Formatif |
| 16 | EVALUASI AKHIR SEMESTER (UAS) | Sidang Demonstrasi Produk Aplikasi Extended Reality (WebXR / Mobile AR) | Analisis kasus / praktik terarah | TM 100 menit + praktik 170 menit + PT 120 menit + BM 120 menit | UAS 30% |

## Ringkasan asesmen

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Bangun scene 3D interaktif dan optimalkan model glTF. Bukti: scene, asset dan hasil uji loading |
| UTS | 8 | 25% | CPMK-2 | Bangun purwarupa AR marker-based atau markerless dan uji interaksi. Bukti: kode, rekaman uji dan spesifikasi perangkat |
| Tugas 2 | 12 | 25% | CPMK-3 | Bangun VR 6DoF, navigasi dan audio spasial pada emulator atau perangkat. Bukti: scene VR, rekaman dan hasil pengukuran FPS |
| UAS | 16 | 30% | CPMK-3 | Evaluasi dan perbaiki purwarupa imersif dari uji kenyamanan dan performa. Bukti: repo, demo, data uji dan analisis |

## Pustaka utama dan pendukung

[WebXR Device API](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API), [Unity Manual](https://docs.unity3d.com/Manual/) dan [glTF](https://www.khronos.org/gltf/).

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS17` *Human-Computer Interaction*, `BK-IT10` *UX Design*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Media Imersif, Dasar Extended Reality (XR: Virtual Reality & Augmented Reality), Framework WebXR / Unity dasar untuk UI spasial, 3D User Interaction Design, Pemanfaatan XR untuk Industri & Edukasi.
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang pembuatan game 3D AAA berskala besar, rigging animasi film animasi profesional, koding driver hardware VR.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Membangun antarmuka interaktif spasial generasi masa depan untuk platform digital modern.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Jika perangkat XR tidak tersedia, gunakan emulator dan catat bahwa FPS headset belum teruji. Ketika relasi Sub-CPMK dan CPMK di Dok 043 tidak sejalan secara substantif, kode sumber dipertahankan dan asesmen mengikuti rumusan CPMK; koordinator perlu memvalidasi pemetaan.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
