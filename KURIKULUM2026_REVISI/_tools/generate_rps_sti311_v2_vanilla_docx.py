# -*- coding: utf-8 -*-
"""RPS Batch Generator — MK STI-311 Pengembangan Web Front End, VERSI 2 VANILLA.

Downgrade terarah (arah user, 2 Oktober 2026): TANPA framework React — SPA dibangun
dengan Vanilla JavaScript; API hanya DIKONSUMSI dari API publik yang endpoint &
dokumentasinya tersedia (tidak membangun API).

Dasar penyusunan:
  - Identitas MK, CPL P4/KK5, skema asesmen 4x, guardrails : Dok 003/005/008/043 (tetap)
  - CPMK-1, CPMK-2, Sub-CPMK-1.1/1.2/2.1/2.2/4.2            : verbatim Dok 043/007
  - CPMK-3, Sub-CPMK-3.1/3.2, Sub-CPMK-4.1                 : DEVIASI terarah dari
    Dok 043 CPMK-3 (React.js -> Vanilla JS) & CPMK-4 (dipersempit: konsumsi API
    publik terdokumentasi, bukan membangun API) — jangkar CPL KK5 (SPA) tetap
    terampu; menunggu ratifikasi/sinkronisasi Tim Kurikulum atas Dok 043/007.

Keluaran:
  - DOCX/RPS_STI-311_Web_Front_End_Development_V2_VANILLA.docx
  - RPS_STI-311_Web_Front_End_Development_V2_VANILLA.md
"""
import copy
import os
import re

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Emu, Pt

SCRIPT = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT)
TEMPLATE = os.path.join(WORKDIR, "Template_RPS_GEN_2026_20092026-SWO.docx")
OUT_DOCX = os.path.join(WORKDIR, "DOCX",
                        "RPS_STI-311_Web_Front_End_Development_V2_VANILLA.docx")
OUT_MD = os.path.join(WORKDIR, "RPS_STI-311_Web_Front_End_Development_V2_VANILLA.md")

TGL_SUSUN = "2 Oktober 2026"

# ---------------------------------------------------------------- data inti
SCALARS = {
    "{{namamk}}": "Pengembangan Web Front End (Web Front End Development)",
    "{{kodemk}}": "STI-311",
    "{{rumpunmk}}": "Rekayasa Perangkat Lunak & Platform (Core STI)",
    "{{skst}}": "2",
    "{{sksp}}": "1",
    "{{sms}}": "3 (Ganjil)",
    "{{tglsusun}}": TGL_SUSUN,
    "{{kodeprodi}}": "B4.5.2.RPS-STI311",
    "{{pengembangrps}}": "Tim KBK Rekayasa Perangkat Lunak & Platform",
    "{{koordinatormk}}": "Dr. Roni Wahyu, S.Kom., M.T.",
    "{{ketuaprodi}}": "[Nama Ketua Prodi SISTEKIN]",
    "{{prodi}}": "Sistem dan Teknologi Informasi",
    "{{namadosen}}": "[Nama Dosen Pengampu STI-311]",
    "{{nuptk}}": "[NUPTK Dosen]",
    "{{dosenpengampu}}": "1. [Nama Dosen Pengampu 1] (Koordinator MK)\n2. [Nama Dosen Pengampu 2]",
    "{{mkprasyarat}}": "FST-102 Algoritma dan Pemrograman",
    "{{deskripsimk}}": (
        "Pengembangan Web Front End (STI-311) adalah mata kuliah wajib Core STI pada Semester 3 "
        "yang membekali mahasiswa dengan kemampuan membangun antarmuka web modern, responsif, "
        "aksesibel, dan interaktif tanpa framework, dengan porsi terbesar pada pendalaman HTML5 "
        "dan CSS3 sesuai jangkar BoK BK-IS12 & BK-IT04. Mahasiswa membangun struktur halaman "
        "semantik dengan HTML5 secara mendalam — metadata & SEO dasar, media & gambar responsif "
        "(picture/srcset, lazy loading), forms, serta aksesibilitas (WCAG dasar & ARIA) — lalu "
        "menata layout responsif multi-device dengan CSS3 modern secara bertahap: Box Model, unit "
        "& fungsi, Custom Properties, Flexbox & Media Queries, Grid System untuk dashboard, hingga "
        "transisi/animasi halus. Logika interaktivitas dibangun dengan Vanilla JavaScript modern "
        "(ES6+, DOM & Event, Async/Await, Fetch API), berlanjut ke Single Page Application (SPA) "
        "berbasis komponen fungsi — state Store & Pub/Sub serta Hash Router/History API — dan "
        "konsumsi RESTful API publik yang endpoint dan dokumentasinya sudah tersedia (mahasiswa "
        "tidak membangun API), form dengan Constraint Validation API, optimasi performa Google "
        "Lighthouse (skor minimal 85), dan deployment ke platform cloud (GitHub Pages/Vercel/"
        "Netlify). Pembelajaran menekankan praktikum dan project-based learning melalui milestone "
        "proyek SPA berkesinambungan. Sesuai Boundary Guardrails Dok 043, mata kuliah ini "
        "menyerahkan penyediaan data backend API kepada STI-416 Web Back End Development."
    ),
    "{{bahankajian}}": (
        "1. BK-IS12 Web and Mobile Application Development — fondasi web front-end: HTML5 semantik, "
        "media & forms, aksesibilitas, UI responsif CSS3, client-side scripting, dan SPA.\n"
        "2. BK-IT04 Platform Technologies — platform web modern, tooling front-end, build & "
        "deployment cloud (GitHub Pages/Vercel/Netlify).\n"
        "Pokok Bahasan: (1) Pengantar Web Frontend & arsitektur client-server; (2) Semantic HTML5: "
        "Struktur Dokumen, Metadata & SEO Dasar; (3) HTML5 Media & Gambar Responsif: Audio/Video, "
        "picture/srcset, Lazy Loading; (4) HTML5 Forms & Aksesibilitas: Input Types, WCAG Dasar, "
        "ARIA; (5) CSS3 Modern I: Box Model, Unit & Fungsi, Custom Properties & Theming; (6) CSS3 "
        "Modern II: Flexbox, Media Queries & Responsive Layout; (7) CSS3 Modern III: Grid System & "
        "Responsive Dashboard; (8) JavaScript ES6+: DOM Manipulation & Event Handling; (9) "
        "JavaScript Modular & Asynchronous: Modules, Async/Await, Fetch API; (10) SPA Vanilla: "
        "Komponen Fungsi, Template Literal & State Store; (11) Routing SPA & Konsumsi API Publik "
        "Terdokumentasi: Hash Router/History API, Fetch, Loading & Error State; (12) Form & "
        "Constraint Validation API; (13) Web Performance: Code Splitting, Lazy Loading, "
        "Lighthouse; (14) Production Build & Cloud Deployment."
    ),
}

CPLS = [
    ("P4", "Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), "
           "manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip "
           "desain interaksi pengalaman pengguna (UI/UX)."),
    ("KK5", "Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform "
            "digital modern yang skalabel (Microservices, Web/Mobile, API, SaaS, BPA)."),
]

CPMKS = [
    ("CPMK-1", "Mahasiswa (A) mampu membangun struktur halaman web responsif multi-device (B) "
               "menggunakan HTML5 Semantik, CSS3 Flexbox/Grid, dan Variabel CSS (C) dengan tampilan "
               "estetik (D). [C3]"),
    ("CPMK-2", "Mahasiswa (A) mampu mengimplementasikan logika interaktivitas client-side (B) "
               "menggunakan JavaScript Modern (ES6+, DOM Manipulation, Async/Await, Fetch API) (C) "
               "secara modular (D). [C3]"),
    ("CPMK-3", "Mahasiswa (A) mampu membangun aplikasi Single Page Application (SPA) berbasis "
               "komponen fungsi (B) menggunakan Vanilla JavaScript (modul ES6+, pola Store & "
               "Pub/Sub untuk state terpusat, Hash Router/History API untuk routing) (C) tanpa "
               "framework (D). [C6]"),
    ("CPMK-4", "Mahasiswa (A) mampu mengintegrasikan aplikasi front-end dengan RESTful API publik "
               "eksternal yang endpoint dan dokumentasinya tersedia (B) serta mengoptimalkan "
               "performa loading (C) dengan skor Google Lighthouse \u2265 85 (D). [C5]"),
]

SUBCPMKS = [
    ("Sub-CPMK-1.1", "Membangun struktur halaman web responsif menggunakan HTML5 semantik. (C3)"),
    ("Sub-CPMK-1.2", "Mengimplementasikan tata letak responsif menggunakan CSS3 Flexbox, Grid, dan "
                     "variabel CSS. (C3)"),
    ("Sub-CPMK-2.1", "Mengimplementasikan interaktivitas client-side menggunakan JavaScript ES6+ "
                     "(DOM, Async/Await). (C3)"),
    ("Sub-CPMK-2.2", "Mengelola state dan komunikasi data menggunakan Fetch API secara modular. (C3)"),
    ("Sub-CPMK-3.1", "Membangun Single Page Application berbasis komponen fungsi dengan Vanilla "
                     "JavaScript (render terkontrol, state terpusat pola Store). (C6)"),
    ("Sub-CPMK-3.2", "Mengimplementasikan routing antar halaman SPA menggunakan Hash Router / "
                     "History API. (C6)"),
    ("Sub-CPMK-4.1", "Mengonsumsi RESTful API publik terdokumentasi dengan penanganan loading dan "
                     "error state. (C5)"),
    ("Sub-CPMK-4.2", "Mengoptimalkan performa loading aplikasi dengan skor Google Lighthouse "
                     "minimal 85. (C5)"),
]

KOLERASI = {
    "header": ["CPL", "CPMK-1", "CPMK-2", "CPMK-3", "CPMK-4", "Instrumen & Bobot Asesmen"],
    "rows": [
        ["P4", "\u2713", "\u2713", "", "", "Tugas 1 (20%) + UTS (25%) = 45%"],
        ["KK5", "", "", "\u2713", "\u2713", "Tugas 2 (25%) + UAS (30%) = 55%"],
    ],
    "note": "Skema 4x Titik Evaluasi Baku (Dok 008): Tugas 1 Pekan 4 (20%), UTS Pekan 8 (25%), "
            "Tugas 2 Pekan 12 (25%), UAS Pekan 16 (30%) — total 100%.",
}

PUSTAKA_UTAMA = [
    "1. Duckett, J. (2011). HTML and CSS: Design and Build Websites. Indianapolis: John Wiley & Sons.",
    "2. Robbins, J. N. (2018). Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript, "
    "and Web Graphics (5th ed.). Sebastopol: O'Reilly Media.",
    "3. Mikowski, M. S., & Powell, J. M. (2013). Single Page Web Applications: JavaScript "
    "End-to-End. Shelter Island: Manning Publications.",
    "4. Haverbeke, M. (2018). Eloquent JavaScript: A Modern Introduction to Programming (3rd ed.). "
    "San Francisco: No Starch Press. https://eloquentjavascript.net",
    "5. MDN Web Docs (2024). MDN Web Docs — Resources for Developers. https://developer.mozilla.org",
]
PUSTAKA_PENDUKUNG = [
    "1. Marcotte, E. (2018). Responsive Web Design (4th ed.). New York: A Book Apart.",
    "2. Grant, K. (2018). CSS in Depth. Shelter Island: Manning Publications.",
    "3. W3C (2018). Web Content Accessibility Guidelines (WCAG) 2.1. "
    "https://www.w3.org/TR/WCAG21/",
    "4. REST Countries (2024). REST Countries — API Documentation. https://restcountries.com",
    "5. TheMealDB (2024). TheMealDB — Open API Documentation. https://www.themealdb.com/api.php",
    "6. Google Chrome Team (2024). Lighthouse — Performance Auditing. "
    "https://developer.chrome.com/docs/lighthouse",
    "7. Vercel (2024). Vercel Documentation. https://vercel.com/docs",
]

# ------------------------------------------------------------- 16 pekan
# (minggu, kemampuan/sub-CPMK, indikator, kriteria&teknik, luring, daring, materi, bobot)
WEEKS = [
    (1, "Pengantar MK & Orientasi — Sub-CPMK-1.1: Mampu menguraikan arsitektur web client-server "
        "dan Semantic HTML5 (C2)",
        "Diagram arsitektur client-server benar; halaman HTML5 semantik lolos validator W3C",
        "Checklist praktikum formatif; observasi lab",
        "Kuliah Interaktif 100'; Lab Setup & Praktikum 170'",
        "Edlink: modul pengantar & kontrak belajar; GitHub Classroom: setup repo",
        "Pengantar Web Frontend, Protokol HTTP, DOM, Semantic HTML5 [1][5]", "\u2014"),
    (2, "Sub-CPMK-1.1: Mampu menyusun dokumen HTML5 semantik dengan metadata & SEO dasar (C3)",
        "Dokumen lolos validator W3C; metadata (description, Open Graph) lengkap",
        "Checklist praktikum formatif; observasi lab",
        "Kuliah Interaktif 100'; Lab Praktikum 170'",
        "Edlink: modul HTML5; GitHub Classroom: setup repo",
        "Semantic HTML5: Struktur Dokumen, Metadata & SEO Dasar [1][5]", "\u2014"),
    (3, "Sub-CPMK-1.1: Mampu menyematkan media & gambar responsif HTML5 (C3)",
        "Gambar responsif (srcset/sizes + lazy loading) dan audio/video dengan track berfungsi",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: contoh media; forum diskusi",
        "HTML5 Media & Gambar Responsif: picture/srcset, Lazy Loading [2][5]", "\u2014"),
    (4, "Sub-CPMK-1.1: Mampu membangun form semantik & halaman aksesibel (C3)",
        "Form dengan input types & label tepat; audit mandiri WCAG dasar & ARIA lolos",
        "Rubrik analitik Tugas 1; penilaian milestone proyek",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: kuis HTML; pengumpulan Tugas 1 via Edlink",
        "HTML5 Forms & Aksesibilitas: Input Types, WCAG Dasar, ARIA [1][8]",
        "Tugas 1: 20% (Milestone Proyek 1 — evaluasi Sub-CPMK Pekan 2\u20133)"),
    (5, "Sub-CPMK-1.2: Mampu menata dasar visual dengan Box Model, Unit & Fungsi, dan Custom "
        "Properties (C3)",
        "Tema via custom properties; layout stabil dengan unit relatif (clamp/calc)",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: video tutorial CSS; commit repo mingguan",
        "CSS3 Modern I: Box Model, Unit & Fungsi, Custom Properties & Theming [1][7]", "\u2014"),
    (6, "Sub-CPMK-1.2: Mampu membangun layout responsif via Flexbox & Media Queries (C3)",
        "Layout multi-kolom adaptif pada \u2265 3 breakpoint (mobile/tablet/desktop)",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: video tutorial CSS; commit repo mingguan",
        "CSS3 Modern II: Flexbox, Media Queries & Responsive Layout [2][6]", "\u2014"),
    (7, "Sub-CPMK-1.2: Mampu merancang dashboard responsif multi-layar dengan CSS Grid System "
        "(C3)",
        "Dashboard responsif grid 12-kolom berfungsi di multi-layar",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: contoh kasus dashboard; forum diskusi",
        "CSS3 Modern III: Grid System & Responsive Dashboard [5][7]", "\u2014"),
    "UTS",
    (9, "Sub-CPMK-2.1: Mampu membangun interaktivitas client-side dengan ES6+: DOM & Event "
        "Handling (C3)",
        "Aplikasi interaktif (to-do) berfungsi: manipulasi DOM & event tanpa error console",
        "Rubrik kompilasi praktikum formatif",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: starter code; GitHub Classroom: latihan DOM",
        "JavaScript ES6+: DOM Manipulation & Event Handling [4][5]", "\u2014"),
    (10, "Sub-CPMK-2.2: Mampu memodularisasi kode & mengonsumsi data via Fetch API (Async/Await) "
         "(C3)",
        "Modul ES6 terpisah; konsumsi data API tanpa blocking UI; error fetch tertangani",
        "Rubrik kompilasi praktikum formatif",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: studi kasus API publik; forum troubleshooting",
        "JavaScript Modular & Asynchronous: Modules, Async/Await, Fetch API [4][5]", "\u2014"),
    (11, "Sub-CPMK-3.1: Mampu membangun SPA vanilla dengan komponen fungsi, template literal & "
         "state store (C4)",
        "Aplikasi satu halaman merender \u2265 5 komponen fungsi dari state tanpa reload",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: modul SPA; repo proyek SPA dimulai",
        "SPA Vanilla: Komponen Fungsi, Template Literal & State Store [3][5]", "\u2014"),
    (12, "Sub-CPMK-3.2 & 4.1: Mampu mengonfigurasi routing SPA (Hash Router/History API) dan "
         "mengonsumsi API publik terdokumentasi (C4)",
        "Rute multi-halaman & protected route berfungsi; loading skeleton & error state pada "
        "\u2265 2 endpoint",
        "Rubrik analitik Tugas 2; penilaian milestone integrasi sistem",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: spesifikasi milestone; pengumpulan Tugas 2",
        "Routing SPA & Konsumsi API Publik Terdokumentasi: Hash Router, History API, Fetch [3][9]",
        "Tugas 2: 25% (Milestone Proyek 2 — evaluasi Sub-CPMK Pekan 9\u201311)"),
    (13, "Sub-CPMK-4.1: Mampu mengelola form kompleks dengan Constraint Validation API (C4)",
        "Form multi-field tervalidasi native; pesan error aksesibel",
        "Rubrik kompilasi praktikum formatif",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: dokumentasi MDN form; konsultasi proyek",
        "Form & Constraint Validation API [4][5]", "\u2014"),
    (14, "Sub-CPMK-4.2: Mampu mengoptimalkan performa web SPA dan audit Google Lighthouse (C5)",
        "Skor Lighthouse Performance \u2265 85 pada build produksi",
        "Rubrik kompilasi audit Lighthouse",
        "Case Method Workshop 270'",
        "Edlink: laporan audit performa; forum optimasi",
        "Web Performance Optimization: Code Splitting, Lazy Loading, Lighthouse [5][11]", "\u2014"),
    (15, "Sub-CPMK-4.2: Mampu mendeploy aplikasi SPA ke platform cloud Vercel/Netlify (C4)",
        "URL produksi aktif; pipeline build otomatis dari repo GitHub",
        "Rubrik kompilasi deployment; verifikasi URL produksi",
        "PjBL Studio 270'",
        "Edlink: panduan deploy; submission URL produksi",
        "Production Build & Cloud Deployment (GitHub Pages/Vercel/Netlify) [12]", "\u2014"),
    "UAS",
]

UTS_LABEL = ("Evaluasi Tengah Semester (UTS) — Ujian Praktik Terjadwal: Semantic HTML5 & "
             "Responsive CSS Grid (CPMK-1)")
UAS_LABEL = ("Evaluasi Akhir Semester (UAS) — Sidang Demonstrasi Produk Aplikasi Web "
             "Single Page Application / SPA (Seluruh CPMK)")

UTS_CELL = (
    "Indikator: Skor ujian praktik \u2265 70; halaman semantik-aksesibel + dashboard responsive "
    "Grid berjalan tanpa error.\n"
    "Kriteria & Teknik: Rubrik analitik UTS; ujian praktik live coding (170').\n"
    "Luring: Live Coding Lab Test (170').\n"
    "Daring: Edlink — pengumuman ruang ujian & unggah berkas.\n"
    "Materi: Cakupan Mg 1\u20137 — HTML5 Semantik & Aksesibilitas, CSS3 Flexbox/Grid/Custom "
    "Properties (CPMK-1) [1][2][7].\n"
    "Bobot Penilaian: UTS 25%."
)
UAS_CELL = (
    "Indikator: Produk SPA terdeploy dan terintegrasi API publik; skor demo & portofolio \u2265 70.\n"
    "Kriteria & Teknik: Rubrik analitik UAS; Demo Day & defense (170').\n"
    "Luring: Sidang demonstrasi produk SPA.\n"
    "Daring: Edlink — berkas final proyek & tautan deploy.\n"
    "Materi: Cakupan seluruh Sub-CPMK — SPA Vanilla JavaScript terintegrasi API publik, optimal, "
    "terdeploy [3][9][12].\n"
    "Bobot Penilaian: UAS 30%."
)

# ------------------------------------------------------------- lampiran
def rub(title, header, rows):
    return ("table", title, header, rows)

LAMPIRAN = [
    # [penugasan1]
    [
        ("p", "TUGAS 1 — MILESTONE PROYEK 1: DOKUMEN HTML5 SEMANTIK, MEDIA & AKSESIBEL (Pekan 4, "
              "Bobot 20%)"),
        ("p", "Mahasiswa membangun satu halaman web (artikel/landing) semantik, kaya media, dan "
              "aksesibel menggunakan HTML5 murni (tanpa framework CSS/JS wajib; styling dasar "
              "boleh)."),
        ("p", "Spesifikasi wajib: (1) struktur semantic minimal 5 area (header, nav, main, section, "
              "footer) dan lolos validator W3C; (2) metadata & SEO dasar (meta description, Open "
              "Graph); (3) media & gambar responsif (picture/srcset/sizes, lazy loading, audio/"
              "video dengan track); (4) form semantik dengan input types & label yang tepat; (5) "
              "aksesibilitas dasar (alt text, kontras, ARIA dasar, navigasi keyboard)."),
        ("p", "Deliverable: repository GitHub + halaman live (GitHub Pages) + laporan singkat 1\u20132 "
              "halaman (keputusan struktur, media, dan aksesibilitas). Penilaian menggunakan rubrik "
              "analitik berikut; cakupan Sub-CPMK-1.1 (Pekan 2\u20133) (CPMK-1 \u2192 CPL P4)."),
    ],
    # [rubriktugas1]
    [
        rub("Rubrik Penilaian Tugas 1 (Total 100)",
            ["Kriteria", "Bobot", "Sangat Baik (86\u2013100)", "Baik (76\u201385)",
             "Cukup (66\u201375)", "Kurang (56\u201365)", "Sangat Kurang (0\u201355)"],
            [["Semantic HTML5 & Validitas W3C", "20%", "Struktur semantic lengkap & valid",
              "Semantic tepat, 1\u20132 warning", "Semantic dasar, beberapa error",
              "Banyak div/span tanpa makna", "Tidak semantic & tidak valid"],
             ["Metadata & SEO Dasar", "10%", "Meta description & Open Graph lengkap",
              "Metadata utama ada", "Sebagian metadata", "Metadata minim",
              "Tanpa metadata"],
             ["Gambar & Media Responsif (srcset, Lazy)", "20%", "Semua media adaptif & optimal",
              "srcset tepat, 1 media kurang", "Media dasar berfungsi",
              "Media tidak responsif", "Tanpa penanganan media"],
             ["Form Semantik & Input Types", "10%", "Input types & label tepat di semua field",
              "1\u20132 field kurang tepat", "Form dasar berfungsi",
              "Banyak field tak semantik", "Form tak semantik"],
             ["Aksesibilitas (WCAG Dasar, ARIA, Keyboard)", "25%", "Audit WCAG dasar lolos penuh",
              "1\u20132 temuan aksesibilitas", "Sebagian terpenuhi",
              "Banyak temuan", "Tidak diperhatikan"],
             ["Dokumentasi & Deployment", "15%", "Repo rapi + live + laporan lengkap",
              "Repo & live ada, laporan singkat", "Repo ada", "Hanya repo tanpa laporan",
              "Tidak ada deliverable"]]),
    ],
    # [soaluts]
    [
        ("p", "UJIAN TENGAH SEMESTER (Pekan 8, Bobot 25%) — UJIAN PRAKTIK LIVE CODING (170 MENIT)"),
        ("p", "Studi kasus: membangun halaman web semantik, aksesibel, dan responsif dalam satu "
              "proyek. Cakupan: Mg 1\u20137 — HTML5 & CSS3 (CPMK-1)."),
        ("p", "Soal: (1) bangun struktur semantik & aksesibel sesuai mockup (landmark HTML5, ARIA "
              "dasar, navigasi keyboard); (2) bangun layout dashboard CSS Grid 12-kolom responsif "
              "(3 breakpoint) dengan Custom Properties untuk theming; (3) implementasi komponen "
              "kartu Flexbox, gambar responsif (srcset/sizes + lazy loading), dan transisi/animasi "
              "halus."),
        ("p", "Ketentuan: open documentation resmi (MDN/WCAG 2.1), dilarang kolaborasi dan AI code "
              "generator; submit repository GitHub pribadi pada akhir sesi. Kriteria ketuntasan "
              "minimal skor 70."),
    ],
    # [rubrikuts]
    [
        rub("Rubrik Penilaian UTS (Total 100)",
            ["Kriteria", "Bobot", "Poin Penuh", "Poin Sebagian", "Poin Minimal", "Tidak Ada"],
            [["Semantic HTML5 & Aksesibilitas (ARIA, Keyboard)", "30%", "30", "20", "10", "0"],
             ["CSS Grid Responsive (3 breakpoint)", "30%", "30", "20", "10", "0"],
             ["Custom Properties & Theming", "15%", "15", "10", "5", "0"],
             ["Gambar Responsif & Media (srcset, Lazy)", "15%", "15", "10", "5", "0"],
             ["Kualitas Kode & Organisasi CSS", "10%", "10", "7", "4", "0"]]),
    ],
    # [tugas2]
    [
        ("p", "TUGAS 2 — MILESTONE PROYEK 2: SPA VANILLA JAVASCRIPT TERINTEGRASI API PUBLIK "
              "(Pekan 12, Bobot 25%)"),
        ("p", "Melanjutkan proyek SPA dari Pekan 7, mahasiswa menambahkan: (1) state lokal dengan "
              "re-render terkontrol dan state global dengan pola Store & Pub/Sub (tanpa duplikasi "
              "state); (2) navigasi multi-halaman menggunakan Hash Router / History API termasuk "
              "dynamic route dan protected route; (3) konsumsi minimal dua endpoint dari SATU API "
              "publik yang endpoint dan dokumentasinya tersedia (REST Countries, TheMealDB, atau "
              "setara — mahasiswa TIDAK membangun API) dengan loading skeleton dan error state; "
              "(4) satu form kompleks dengan Constraint Validation API."),
        ("p", "Deliverable: repository GitHub + deployment preview (GitHub Pages/Vercel/Netlify) + "
              "demo video maksimal 5 menit. Cakupan evaluasi: Sub-CPMK-2.1, 2.2, dan 3.1 (Pekan "
              "9\u201311) \u2192 CPMK-2 (P4) dan CPMK-3 (KK5). Penilaian menggunakan rubrik "
              "analitik berikut."),
    ],
    # [rubriktugas2]
    [
        rub("Rubrik Penilaian Tugas 2 (Total 100)",
            ["Kriteria", "Bobot", "Sangat Baik (86\u2013100)", "Baik (76\u201385)",
             "Cukup (66\u201375)", "Kurang (56\u201365)", "Sangat Kurang (0\u201355)"],
            [["Arsitektur Komponen Vanilla & Rendering", "20%", "Komposisi komponen fungsi bersih "
              "& reusable", "Komponen tepat, minor duplikasi", "Komponen dasar berfungsi",
              "Kode monolitik satu berkas", "Tanpa pemisahan komponen"],
             ["State Terpusat (Store & Pub/Sub)", "25%", "State global tepat tanpa duplikasi",
              "Store benar, minor re-render berlebih", "State lokal berfungsi",
              "State tersebar tak terkelola", "Tidak ada manajemen state"],
             ["Routing SPA (Dynamic & Protected)", "15%", "Semua rute + guard berfungsi",
              "Rute lengkap, guard sebagian", "Rute dasar berfungsi", "Rute tidak konsisten",
              "Tanpa routing"],
             ["Integrasi API Publik & UX State", "25%", "Loading skeleton & error state sempurna "
              "pada \u2265 2 endpoint", "Integrasi benar, 1 UX state kurang",
              "Integrasi dasar berfungsi", "Error tidak tertangani", "Tidak terintegrasi"],
             ["Kualitas Kode & Deployment", "15%", "Kode bersih + preview aktif",
              "Kode baik, deploy ada isu minor", "Deploy aktif", "Deploy gagal",
              "Tidak deploy"]]),
    ],
    # [soaluas]
    [
        ("p", "UJIAN AKHIR SEMESTER (Pekan 16, Bobot 30%) — SIDANG DEMONSTRASI PRODUK SPA (DEMO DAY & DEFENSE, 170 MENIT)"),
        ("p", "Mahasiswa (individu/kelompok kecil) mempresentasikan produk akhir SPA Vanilla "
              "JavaScript hasil pengembangan berkesinambungan Mg 4\u201315: aplikasi Single Page "
              "Application berbasis komponen fungsi — state global pola Store & Pub/Sub, routing "
              "Hash Router/History API, integrasi API publik terdokumentasi, form tervalidasi "
              "Constraint Validation API, skor Google Lighthouse \u2265 85, dan terdeploy di "
              "GitHub Pages/Vercel/Netlify."),
        ("p", "Format sidang: demo live 15 menit (alur utama aplikasi, penanganan error, performa) "
              "+ tanya jawab 5 menit. Deliverable akhir: URL produksi aktif, repository GitHub, "
              "slide presentasi, dan write-up portofolio 2\u20133 halaman (arsitektur, keputusan "
              "teknis, hasil audit Lighthouse). Kriteria ketuntasan minimal skor 70."),
    ],
    # [rubrikuas]
    [
        rub("Rubrik Penilaian UAS (Total 100)",
            ["Kriteria", "Bobot", "Poin"],
            [["Fungsionalitas SPA vanilla & kelengkapan fitur", "25%", "25"],
             ["Integrasi API publik & penanganan data", "20%", "20"],
             ["Performa (Lighthouse \u2265 85)", "15%", "15"],
             ["Manajemen form & validasi native", "10%", "10"],
             ["Deployment produksi aktif", "10%", "10"],
             ["Presentasi & defense", "15%", "15"],
             ["Kualitas kode & struktur proyek", "5%", "5"]]),
    ],
]

BLOCK_TAGS = ["[penugasan1]", "[rubriktugas1]", "[soaluts]", "[rubrikuts]",
              "[tugas2]", "[rubriktugas2]", "[soaluas]", "[rubrikuas]"]


# ------------------------------------------------------------------ util
def unique_cells(row):
    seen, out = set(), []
    for c in row.cells:
        if id(c._tc) in seen:
            continue
        seen.add(id(c._tc))
        out.append(c)
    return out


def set_cell_text(cell, text, first_only=False):
    """Ganti isi sel dengan teks (multibaris), pertahankan format run pertama."""
    paras = cell.paragraphs
    p = paras[0]
    for extra in paras[1:]:
        for r in extra.runs:
            r.text = ""
    template_run = p.runs[0] if p.runs else None
    for r in list(p.runs):
        r.text = ""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        run = p.add_run(line)
        if template_run is not None:
            run.font.name = template_run.font.name
            run.font.size = template_run.font.size
            run.font.bold = template_run.font.bold
        if i < len(lines) - 1:
            run.add_break()
    if first_only:
        return
    # hapus paragraf kosong berlebih setelahnya
    for extra in paras[1:]:
        if extra.text == "" and len(extra.runs) == 0:
            continue


def clear_cell(cell):
    for p in cell.paragraphs:
        for r in list(p.runs):
            r.text = ""


def iter_paragraphs(doc):
    def walk_table(t):
        for row in t.rows:
            seen = set()
            for c in row.cells:
                if id(c._tc) in seen:
                    continue
                seen.add(id(c._tc))
                for p in c.paragraphs:
                    yield p
                for nt in c.tables:
                    yield from walk_table(nt)
    yield from doc.paragraphs
    for t in doc.tables:
        yield from walk_table(t)


def replace_scalars(doc):
    hits = 0
    for p in iter_paragraphs(doc):
        for tag, val in SCALARS.items():
            if tag in p.text:
                replace_in_paragraph(p, {tag: val})
                hits += 1
    return hits


def replace_in_paragraph(p, mapping):
    """Ganti semua tag {{...}} pada satu paragraf (teks bisa terpecah antar-run)."""
    text = p.text
    hit = False
    for tag, val in mapping.items():
        if tag in text:
            text = text.replace(tag, val)
            hit = True
    if not hit:
        return False
    lines = text.split("\n")
    proto = p.runs[0] if p.runs else None
    for r in list(p.runs):
        r.text = ""
    for i, line in enumerate(lines):
        run = p.add_run(line)
        if proto is not None:
            run.font.name = proto.font.name
            run.font.size = proto.font.size
            run.font.bold = proto.font.bold
        if i < len(lines) - 1:
            run.add_break()
    return True


def scalar_pass(doc):
    n = 0
    for p in iter_paragraphs(doc):
        if replace_in_paragraph(p, SCALARS):
            n += 1
    return n


RUBRIC_WIDTH = 8497  # twips — lebar sel kontainer lampiran (section portrait)

RUBRIC_FRACTIONS = {
    7: (0.235, 0.08, 0.137, 0.137, 0.137, 0.137, 0.137),
    6: (0.28, 0.12, 0.15, 0.15, 0.15, 0.15),
    3: (0.48, 0.26, 0.26),
}


def _rubric_widths(ncols, total):
    fr = RUBRIC_FRACTIONS.get(ncols, tuple([1.0 / ncols] * ncols))
    w = [int(total * f) for f in fr]
    w[-1] += total - sum(w)
    return w


def style_rubric(tbl, widths):
    """Layout tetap + lebar kolom proporsional + cantSplit + margin sel rapat +
    font 9pt agar tabel rubrik muat utuh di kotak lampiran (tanpa luapor 1 baris)
    dan kolom sempit tidak memenggal kata di tengah."""
    tbl.autofit = False
    tblPr = tbl._tbl.tblPr
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is not None:
        tblW.set(qn("w:w"), str(sum(widths)))
        tblW.set(qn("w:type"), "dxa")
    mar = tblPr.makeelement(qn("w:tblCellMar"), {})
    for side, v in (("top", 20), ("left", 60), ("bottom", 20), ("right", 60)):
        el = mar.makeelement(qn(f"w:{side}"), {})
        el.set(qn("w:w"), str(v))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    look = tblPr.find(qn("w:tblLook"))
    if look is not None:
        look.addprevious(mar)
    else:
        tblPr.append(mar)
    grid = tbl._tbl.find(qn("w:tblGrid"))
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(w))
    for row in tbl.rows:
        trpr = row._tr.get_or_add_trPr()
        if trpr.find(qn("w:cantSplit")) is None:
            trpr.insert(0, trpr.makeelement(qn("w:cantSplit"), {}))
        for cell, w in zip(row.cells, widths):
            cell.width = Emu(w * 635)
            for p in cell.paragraphs:
                pf = p.paragraph_format
                pf.space_before = Pt(0)
                pf.space_after = Pt(0)
                pf.line_spacing = 1.0
                for r in p.runs:
                    r.font.size = Pt(9)


def add_rubric_table(cell, header, rows, fit_width=None):
    tbl = cell.add_table(rows=len(rows) + 1, cols=len(header))
    try:
        tbl.style = "Table Grid"
    except Exception:
        pass
    for j, h in enumerate(header):
        tbl.rows[0].cells[j].text = h
        for r in tbl.rows[0].cells[j].paragraphs[0].runs:
            r.font.bold = True
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            tbl.rows[i].cells[j].text = val
    if fit_width:
        style_rubric(tbl, _rubric_widths(len(header), fit_width))


def fill_lampiran(doc):
    for ti, content in zip(range(3, 11), LAMPIRAN):
        cell = doc.tables[ti].rows[0].cells[0]
        clear_cell(cell)
        proto = None
        first = True
        for item in content:
            if item[0] == "p":
                if first:
                    p = cell.paragraphs[0]
                    run = p.add_run(item[1])
                    run.font.bold = True
                    first = False
                else:
                    p = cell.add_paragraph()
                    run = p.add_run(item[1])
                    if item[1].startswith(("TUGAS", "UJIAN")):
                        run.font.bold = True
            else:
                _, title, header, rows = item
                p = cell.add_paragraph()
                r = p.add_run(title)
                r.font.bold = True
                add_rubric_table(cell, header, rows, fit_width=RUBRIC_WIDTH)


def clone_row_after(table, src_idx, n):
    anchor = table.rows[src_idx]._tr
    made = []
    for _ in range(n):
        new_tr = copy.deepcopy(anchor)
        anchor.addnext(new_tr)
        anchor = new_tr
        made.append(new_tr)
    return made


def write_markdown():
    L = []
    A = L.append
    A("# RPS STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*) — V2 VANILLA")
    A("")
    A("**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  ")
    A("**Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  ")
    A(f"**Nomor Dokumen:** 071030.{SCALARS['{{kodeprodi}}']}  ")
    A(f"**Tanggal Penyusunan:** {TGL_SUSUN}  ")
    A("**Sumber:** Template Master RPS Generator FSTI UWG (`Template_RPS_GEN_2026_20092026-SWO.docx`) "
      "— seluruh 18 tag `{{...}}` + 25 tag `[...]` terisi. **V2 VANILLA (downgrade terarah):** tanpa "
      "framework React — SPA dibangun dengan Vanilla JavaScript; API hanya dikonsumsi dari API "
      "publik yang endpoint & dokumentasinya tersedia. CPMK-1/2 & Sub-CPMK 1.x/2.x/4.2 verbatim "
      "Dok 043/007; CPMK-3, Sub-CPMK 3.1/3.2/4.1 adalah **deviasi terarah** dari Dok 043/007 "
      "(menunggu ratifikasi Tim Kurikulum). Jangkar CPL `KK5 (SPA)` tetap terampu via SPA vanilla.  ")
    A("**Keluaran pendamping:** `DOCX/RPS_STI-311_Web_Front_End_Development_V2_VANILLA.docx`")
    A("")
    A("---")
    A("")
    A("## HALAMAN 1 — IDENTITAS MATA KULIAH")
    A("")
    A("| Atribut | Isi |")
    A("|---|---|")
    A(f"| Mata Kuliah (MK) | {SCALARS['{{namamk}}']} |")
    A(f"| Kode | {SCALARS['{{kodemk}}']} |")
    A(f"| Rumpun MK | {SCALARS['{{rumpunmk}}']} |")
    A(f"| Bobot (sks) | T= {SCALARS['{{skst}}']}, P= {SCALARS['{{sksp}}']} (Total 3 SKS, Tipe +P) |")
    A(f"| Semester | {SCALARS['{{sms}}']} |")
    A(f"| Tgl Penyusunan | {SCALARS['{{tglsusun}}']} |")
    A(f"| Pengembang RPS | {SCALARS['{{pengembangrps}}']} |")
    A(f"| Koordinator RMK | {SCALARS['{{koordinatormk}}']} |")
    A(f"| Ketua Program Studi | {SCALARS['{{ketuaprodi}}']} |")
    A(f"| Matakuliah Syarat | {SCALARS['{{mkprasyarat}}']} |")
    A(f"| Dosen Pengampu | {SCALARS['{{dosenpengampu}}'].replace(chr(10), '<br>')} |")
    A("")
    A("## HALAMAN 2 — CAPAIAN PEMBELAJARAN (CP)")
    A("")
    A("### CPL-PRODI yang Dibebankan pada MK")
    A("")
    A("| No | Capaian Pembelajaran Lulusan (Dok 003) |")
    A("|:--:|---|")
    for code, text in CPLS:
        A(f"| **{code}** | {text} |")
    A("")
    A("### Capaian Pembelajaran Mata Kuliah (CPMK) — Format ABCD & Bloom")
    A("")
    A("| No | Rumusan CPMK |")
    A("|:--:|---|")
    for code, text in CPMKS:
        A(f"| **{code}** | {text} |")
    A("")
    A("### Tahapan Belajar (Sub-CPMK)")
    A("")
    A("| No | Sub-CPMK |")
    A("|:--:|---|")
    for code, text in SUBCPMKS:
        A(f"| **{code}** | {text} |")
    A("")
    A("### Korelasi CPL terhadap CPMK")
    A("")
    A("| " + " | ".join(KOLERASI["header"]) + " |")
    A("|" + ":--:|" * len(KOLERASI["header"]))
    for row in KOLERASI["rows"]:
        A("| " + " | ".join(v if v else " " for v in row) + " |")
    A("")
    A(KOLERASI["note"])
    A("")
    A("### Deskripsi Singkat MK")
    A("")
    A(SCALARS["{{deskripsimk}}"])
    A("")
    A("### Bahan Kajian: Materi Pembelajaran")
    A("")
    A(SCALARS["{{bahankajian}}"].replace(chr(10), chr(10) + chr(10)))
    A("")
    A("### Pustaka")
    A("")
    A("**Utama:**")
    A("")
    for item in PUSTAKA_UTAMA:
        A(item)
    A("")
    A("**Pendukung:**")
    A("")
    for item in PUSTAKA_PENDUKUNG:
        A(item)
    A("")
    A("---")
    A("")
    A("## HALAMAN 3-4 — RENCANA PEMBELAJARAN 16 PEKAN")
    A("")
    A("| Mg ke- | Kemampuan Akhir Tahapan Belajar (Sub-CPMK) | Indikator | Kriteria & Teknik | "
      "Luring (offline) | Daring (online) | Materi Pembelajaran [Pustaka] | Bobot Penilaian (%) |")
    A("|:--:|---|---|---|---|---|---|:--:|")
    for w in WEEKS:
        if w == "UTS":
            A("| **8** | " + UTS_LABEL + " | " + UTS_CELL.replace(chr(10), "<br>")
              + " | UTS 25% |")
        elif w == "UAS":
            A("| **16** | " + UAS_LABEL + " | " + UAS_CELL.replace(chr(10), "<br>")
              + " | UAS 30% |")
        else:
            mg, kem, ind, krit, lur, dar, mat, bobot = w
            A(f"| {mg} | {kem} | {ind} | {krit} | {lur} | {dar} | {mat} | {bobot} |")
    A("| | **Total bobot penilaian** | | | | | | **100%** |")
    A("")
    A("---")
    A("")
    A("## LAMPIRAN — INSTRUMEN ASESMEN")
    A("")
    judul = ["", "", "Lampiran 1 — Penugasan Terstruktur 1 & Rubrik", "Lampiran 2 — UTS & Rubrik",
             "Lampiran 3 — Penugasan Terstruktur 2 & Rubrik", "Lampiran 4 — UAS & Rubrik"]
    for content in LAMPIRAN:
        for item in content:
            if item[0] == "p":
                A(item[1])
                A("")
            else:
                _, title, header, rows = item
                A(f"**{title}**")
                A("")
                A("| " + " | ".join(header) + " |")
                A("|" + "---|" * len(header))
                for row in rows:
                    A("| " + " | ".join(row) + " |")
                A("")
    A("---")
    A("")
    A("## PENGESAHAN")
    A("")
    A("| Memvalidasi, Unit Penjaminan Mutu FSTI | Malang, " + TGL_SUSUN + " — Dosen Pengampu |")
    A("|---|---|")
    A(f"| Nama Pejabat UPM: [Nama Kepala UPM FSTI] | {SCALARS['{{namadosen}}']} / NUPTK. "
      f"{SCALARS['{{nuptk}}']} |")
    A("")
    A(f"Mengesahkan, Ketua Program Studi {SCALARS['{{prodi}}']}: {SCALARS['{{ketuaprodi}}']}")
    A("")
    A("---")
    A("")
    A("*RPS STI-311 V2 VANILLA dibangkitkan dari Template Master RPS Generator FSTI UWG oleh "
      "`_tools/generate_rps_sti311_v2_vanilla_docx.py` — downgrade terarah: SPA vanilla tanpa "
      "framework, konsumsi API publik terdokumentasi (bukan membangun API).*")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"Keluaran Markdown    : {OUT_MD}")


def main():
    doc = Document(TEMPLATE)
    t1, t2 = doc.tables[1], doc.tables[2]

    # 0) perbaikan header institusi (warisan template sumber)
    header_cell = unique_cells(t1.rows[0])[1]
    hdr_paras = [p for p in header_cell.paragraphs if p.text.strip()]
    hdr_paras[1].text = ""  # reset
    for r in list(hdr_paras[1].runs):
        r.text = ""
    hdr_paras[1].add_run("FAKULTAS SAINS DAN TEKNOLOGI INFORMASI")
    for r in list(hdr_paras[2].runs):
        r.text = ""
    hdr_paras[2].add_run("PROGRAM STUDI S1 SISTEM DAN TEKNOLOGI INFORMASI")

    # 1) CPL: baris 7-12 -> isi 2, kosongkan 4
    for i in range(6):
        cells = unique_cells(t1.rows[i + 7])
        if i < len(CPLS):
            set_cell_text(cells[1], CPLS[i][0])
            set_cell_text(cells[2], CPLS[i][1])
        else:
            clear_cell(cells[1])
            clear_cell(cells[2])

    # 2) CPMK: baris 14-19 -> isi 4, kosongkan 2
    for i in range(6):
        cells = unique_cells(t1.rows[i + 14])
        if i < len(CPMKS):
            set_cell_text(cells[1], CPMKS[i][0])
            set_cell_text(cells[2], CPMKS[i][1])
        else:
            clear_cell(cells[1])
            clear_cell(cells[2])

    # 3) Sub-CPMK: baris 21-25 (5) + klon 3 -> isi 8
    clone_row_after(t1, 25, 3)
    for i in range(8):
        cells = unique_cells(t1.rows[i + 21])
        set_cell_text(cells[1], SUBCPMKS[i][0])
        set_cell_text(cells[2], SUBCPMKS[i][1])

    # 4) Tabel kolerasi (baris 30 = 27 asli + 3 baris klon Sub-CPMK)
    kol_cell = unique_cells(t1.rows[30])[1]
    assert "[tabelkolerasi]" in kol_cell.text, "indeks baris kolerasi bergeser!"
    clear_cell(kol_cell)
    kol_cell.paragraphs[0].add_run("Matriks Korelasi CPL terhadap CPMK dan Bobot Asesmen:")
    add_rubric_table(kol_cell, KOLERASI["header"], KOLERASI["rows"])
    kol_cell.add_paragraph(KOLERASI["note"])

    # 5) pustaka (blok multibaris dalam sel; indeks pasca-klon: 31=deskripsi, 34=utama, 36=pendukung)
    assert "{{deskripsimk}}" in unique_cells(t1.rows[31])[1].text, "indeks deskripsi bergeser!"
    assert "{{bahankajian}}" in unique_cells(t1.rows[32])[1].text, "indeks bahan kajian bergeser!"
    set_cell_text(unique_cells(t1.rows[34])[1], "\n".join(PUSTAKA_UTAMA))
    set_cell_text(unique_cells(t1.rows[36])[1], "\n".join(PUSTAKA_PENDUKUNG))
    # 5b) label "Utama :" / "Pendukung :" diikat ke daftarnya (keep-with-next)
    # agar tidak yatim di dasar halaman
    for ri in (33, 35):
        for c in unique_cells(t1.rows[ri]):
            for p in c.paragraphs:
                p.paragraph_format.keep_with_next = True

    # 6) Tabel 16 pekan: baris 3-9 = pekan 1-7; baris 10 = UTS; baris 11-14 = pekan 9-12;
    #    klon 3 baris untuk pekan 13-15; baris UAS tetap.
    clone_row_after(t2, 14, 3)
    weeks = [w for w in WEEKS if w != "UTS" and w != "UAS"]
    tag_rows = list(range(3, 10)) + list(range(11, 15)) + [15, 16, 17]  # 14 baris ter-tag
    idx = 0
    for row_idx, week in zip(tag_rows, weeks):
        cells = unique_cells(t2.rows[row_idx])
        for cell, val in zip(cells, week):
            set_cell_text(cell, str(val))
    # UTS (baris 10) dan UAS (baris 18 pasca-klon). Dump XML template: sel merge lebar
    # = gridcol 1-6, kolom 8 (bobot) terpisah dan kosong — label + isi berlabel multiline
    # wajib satu sel merge (aturan keras 5), kolom bobot diisi ringkas.
    uts_cells = unique_cells(t2.rows[10])
    set_cell_text(uts_cells[1], UTS_LABEL + "\n" + UTS_CELL)
    set_cell_text(uts_cells[2], "UTS 25%")
    uas_cells = unique_cells(t2.rows[18])
    set_cell_text(uas_cells[1], UAS_LABEL + "\n" + UAS_CELL)
    set_cell_text(uas_cells[2], "UAS 30%")

    # 6b) header berulang hanya R0-R2 + cantSplit baris data. Warisan template
    # menandai SEMUA baris data sebagai tblHeader — efek sampingnya Word menolak
    # menempatkan paragraf apa pun setelah tabel di halaman terakhirnya (Catatan
    # TM/PT/BM terdorong ke halaman kosong sendiri).
    for ri, tr in enumerate(t2._tbl.findall(qn("w:tr"))):
        trpr = tr.get_or_add_trPr()
        hdr = trpr.find(qn("w:tblHeader"))
        if ri < 3:
            if hdr is None:
                trpr.append(trpr.makeelement(qn("w:tblHeader"), {}))
        else:
            if hdr is not None:
                trpr.remove(hdr)
            if trpr.find(qn("w:cantSplit")) is None:
                trpr.insert(0, trpr.makeelement(qn("w:cantSplit"), {}))

    # 7) Lampiran (tabel 3-10)
    fill_lampiran(doc)

    # 8) tanggal undangan tanda tangan, cover, & perbaikan typo warisan template
    for p in iter_paragraphs(doc):
        if p.text.strip() == "Malang, Tanggal Bulan Tahun":
            for r in list(p.runs):
                r.text = ""
            p.add_run(f"Malang, {TGL_SUSUN}")
        if p.text.strip() == "AGUSTUS, 2026":
            for r in list(p.runs):
                r.text = ""
            p.add_run("OKTOBER, 2026")
        if p.text.strip() == "Dosen Pengampuh,":
            for r in list(p.runs):
                r.text = ""
            p.add_run("Dosen Pengampu,")

    # 8b) section lanskap ditutup 2 paragraf kosong + paragraf pembawa sectPr;
    # satu paragraf kosong dibuang agar pola "3 kosong berturut" (postcheck)
    # hilang — tata letak tidak berubah karena letaknya di ekor section
    body_children = doc.element.body
    for el in list(body_children):
        if el.tag == qn("w:p"):
            text = "".join(t.text or "" for t in el.iter(qn("w:t")))
            if text.strip().startswith("Catatan :"):
                nxt = el.getnext()
                if (nxt is not None and nxt.tag == qn("w:p")
                        and not "".join(t.text or "" for t in nxt.iter(qn("w:t"))).strip()):
                    el.getparent().remove(nxt)
                break

    # 9) scalar pass terakhir (semua {{tag}} termasuk yang ada di tabel nested)
    n_scalar = scalar_pass(doc)

    os.makedirs(os.path.dirname(OUT_DOCX), exist_ok=True)
    doc.save(OUT_DOCX)

    # 10) verifikasi zero tag tersisa
    chk = Document(OUT_DOCX)
    leftovers = []
    all_text = []
    for p in iter_paragraphs(chk):
        all_text.append(p.text)
    blob = "\n".join(all_text)
    for tag in SCALARS:
        if tag in blob:
            leftovers.append(tag)
    for tag in ["[nocpl]", "[cpl]", "[nocpmk]", "[cpmk]", "[nosubcpmk]", "[subcpmk]",
                "[tabelkolerasi]", "[pustakautama]", "[pustakapendukung]",
                "[mingguke]", "[kemampuan_subcpmk]", "[indikator]", "[kriteriateknik]",
                "[luring]", "[daring]", "[materi]", "[bobot_nilai]"] + BLOCK_TAGS:
        if tag in blob:
            leftovers.append(tag)

    print(f"Scalar terisi        : {n_scalar} paragraf")
    print(f"Tag tersisa          : {leftovers if leftovers else 'NIHIL (zero residual)'}")
    print(f"Keluaran DOCX        : {OUT_DOCX}")
    write_markdown()

    return 0 if not leftovers else 1


if __name__ == "__main__":
    raise SystemExit(main())
