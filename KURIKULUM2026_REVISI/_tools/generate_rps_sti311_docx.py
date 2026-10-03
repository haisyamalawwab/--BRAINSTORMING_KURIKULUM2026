# -*- coding: utf-8 -*-
"""RPS Batch Generator (unit pilot ke-2): MK STI-311 Pengembangan Web Front End.

Mengisi Template_RPS_GEN_2026_20092026-SWO.docx (12 tabel, 18 tag {{...}} +
25 tag [...]) dengan data resmi Kurikulum SISTEKIN 2026:
  - Identitas MK        : Dok 005 (baris MK no. 11) & Dok 007 Tabel 22.A
  - CPL P4 / KK5        : Dok 003 (rumusan resmi)
  - CPMK & Sub-CPMK     : Dok 007 Tabel 22.B & Dok 043 (verbatim, ABCD + Bloom)
  - Rencana 16 pekan    : Dok 007 Tabel 22.C (backbone pekan) x Sub-CPMK Dok 043
  - Skema asesmen       : 4x Titik Baku Dok 008 (T1 20%, UTS 25%, T2 25%, UAS 30%)
  - Boundary Guardrails : Dok 043 / 037 (handoff backend -> STI-416)

Keluaran:
  - DOCX/RPS_STI-311_Web_Front_End_Development.docx  (template terisi penuh)
  - RPS_STI-311_Web_Front_End_Development.md         (pendamping markdown)
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
OUT_DOCX = os.path.join(WORKDIR, "DOCX", "RPS_STI-311_Web_Front_End_Development.docx")
OUT_MD = os.path.join(WORKDIR, "RPS_STI-311_Web_Front_End_Development.md")

TGL_SUSUN = "30 September 2026"

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
        "yang membekali mahasiswa dengan kemampuan membangun antarmuka web modern, responsif, dan "
        "interaktif. Mahasiswa membangun struktur halaman semantik dengan HTML5, tata letak "
        "responsif multi-device dengan CSS3 (Flexbox, Grid, variabel CSS), serta logika "
        "interaktivitas client-side dengan JavaScript modern (ES6+, DOM Manipulation, Async/Await, "
        "Fetch API). Pembelajaran berlanjut ke pembangunan Single Page Application (SPA) berbasis "
        "komponen menggunakan React.js — Hooks, Context API untuk state global, dan React Router "
        "untuk navigasi client-side — hingga integrasi dengan RESTful API eksternal, manajemen form "
        "kompleks (React Hook Form & Zod), optimasi performa berbasis Google Lighthouse (skor "
        "minimal 85), dan deployment ke platform cloud (Vercel/Netlify). Pembelajaran menekankan "
        "praktikum dan project-based learning melalui milestone proyek SPA berkesinambungan. Sesuai "
        "Boundary Guardrails Dok 043, mata kuliah ini menyerahkan penyediaan data backend API "
        "kepada STI-416 Web Back End Development."
    ),
    "{{bahankajian}}": (
        "1. BK-IS12 Web and Mobile Application Development — pemrograman web sisi klien "
        "(client-side), arsitektur web client-server, UI responsif, dan SPA.\n"
        "2. BK-IT04 Platform Technologies — platform web modern, tooling front-end, build & "
        "deployment cloud (Vercel/Netlify).\n"
        "Pokok Bahasan: (1) Pengantar Web Frontend & arsitektur client-server; (2) Semantic HTML5 "
        "& DOM; (3) CSS3 Modern: Box Model, Flexbox, Media Queries, CSS Tokens; (4) CSS Grid System "
        "& Responsive Dashboard; (5) JavaScript ES6+: Scope, Closure, Modules; (6) DOM Manipulation, "
        "Event Handling & Form Validation; (7) Asynchronous JavaScript: Promises, Async/Await, Fetch "
        "API; (8) React.js: JSX, Virtual DOM, Components, Props; (9) React Hooks: useState, "
        "useEffect, useRef; (10) Global State: Context API & Custom Hooks; (11) React Router v6: "
        "Dynamic & Protected Routes; (12) REST API Integration: Axios, Loading Skeletons, Error "
        "Boundary; (13) React Hook Form & Validasi Skema Zod; (14) Web Performance: Code Splitting, "
        "Lazy Loading, Lighthouse; (15) Production Build & Cloud Deployment."
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
               "komponen (B) menggunakan framework React.js (Hooks, Context API, React Router) (C) "
               "dengan arsitektur state terpusat (D). [C6]"),
    ("CPMK-4", "Mahasiswa (A) mampu mengintegrasikan aplikasi front-end dengan RESTful API "
               "eksternal (B) serta mengoptimalkan performa loading (C) dengan skor Google "
               "Lighthouse \u2265 85 (D). [C5]"),
]

SUBCPMKS = [
    ("Sub-CPMK-1.1", "Membangun struktur halaman web responsif menggunakan HTML5 semantik. (C3)"),
    ("Sub-CPMK-1.2", "Mengimplementasikan tata letak responsif menggunakan CSS3 Flexbox, Grid, dan "
                     "variabel CSS. (C3)"),
    ("Sub-CPMK-2.1", "Mengimplementasikan interaktivitas client-side menggunakan JavaScript ES6+ "
                     "(DOM, Async/Await). (C3)"),
    ("Sub-CPMK-2.2", "Mengelola state dan komunikasi data menggunakan Fetch API secara modular. (C3)"),
    ("Sub-CPMK-3.1", "Membangun Single Page Application berbasis komponen menggunakan React "
                     "(Hooks, Context API). (C6)"),
    ("Sub-CPMK-3.2", "Mengimplementasikan routing antar halaman pada aplikasi SPA. (C6)"),
    ("Sub-CPMK-4.1", "Mengintegrasikan front-end dengan RESTful API eksternal. (C5)"),
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
    "3. Banks, A., & Porcello, E. (2020). Learning React: Modern Patterns for Developing React "
    "Apps (2nd ed.). Sebastopol: O'Reilly Media.",
    "4. MDN Web Docs (2024). MDN Web Docs — Resources for Developers. https://developer.mozilla.org",
    "5. React Team (2024). React — The Library for Web and Native User Interfaces. https://react.dev",
]
PUSTAKA_PENDUKUNG = [
    "1. Grant, K. (2018). CSS in Depth. Shelter Island: Manning Publications.",
    "2. Haverbeke, M. (2018). Eloquent JavaScript: A Modern Introduction to Programming (3rd ed.). "
    "San Francisco: No Starch Press. https://eloquentjavascript.net",
    "3. React Router Team (2024). React Router Documentation. https://reactrouter.com",
    "4. Hookform (2024). React Hook Form Documentation. https://react-hook-form.com",
    "5. Zod (2024). Zod — TypeScript-first Schema Validation. https://zod.dev",
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
        "Pengantar Web Frontend, Protokol HTTP, DOM, Semantic HTML5 [1][4]", "\u2014"),
    (2, "Sub-CPMK-1.2: Mampu merancang layout responsif via CSS Flexbox dan Media Queries (C3)",
        "Layout multi-kolom adaptif pada \u2265 3 breakpoint (mobile/tablet/desktop)",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: video tutorial CSS; commit repo mingguan",
        "CSS3 Modern: Box Model, Flexbox, Media Queries, CSS Tokens [1][2]", "\u2014"),
    (3, "Sub-CPMK-1.2: Mampu merancang grid kompleks multi-layar dengan CSS Grid System (C3)",
        "Dashboard responsif grid 12-kolom berfungsi di multi-layar",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: contoh kasus dashboard; forum diskusi",
        "Advanced Layout: CSS Grid System & Responsive Dashboard Layout [1][2]", "\u2014"),
    (4, "Sub-CPMK-2.1: Mampu menerapkan sintaks ES6+: Arrow Functions, Destructuring, Modules (C3)",
        "Skrip JS modular memakai fitur ES6+ tanpa error console",
        "Rubrik analitik Tugas 1; penilaian milestone proyek",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: kuis sintaks; pengumpulan Tugas 1 via Edlink",
        "JavaScript Modern: ES6+ Features, Scope, Closure, Modules [3][4]",
        "Tugas 1: 20% (Milestone Proyek 1 — evaluasi Sub-CPMK Pekan 2\u20133)"),
    (5, "Sub-CPMK-2.1: Mampu memanipulasi DOM secara dinamis dan menangani event interaktif (C3)",
        "Aplikasi interaktif (to-do) berfungsi: manipulasi DOM, event, validasi form client-side",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: starter code; GitHub Classroom: latihan DOM",
        "DOM Manipulation, Event Handling, Form Validation Client-Side [3][4]", "\u2014"),
    (6, "Sub-CPMK-2.2: Mampu menangani operasi asinkron via Promises dan Async/Await (C3)",
        "Aplikasi konsumsi API publik menampilkan data tanpa blocking UI; error fetch tertangani",
        "Rubrik kompilasi praktikum formatif",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: studi kasus API publik; forum troubleshooting",
        "Asynchronous JavaScript: Promises, Async/Await, Fetch API [3][4]", "\u2014"),
    (7, "Sub-CPMK-3.1: Mampu merancang komponen antarmuka modular dalam React.js (C3)",
        "UI tersusun \u2265 5 functional components dengan aliran props yang benar",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: modul React dasar; repo proyek SPA dimulai",
        "Pengantar React.js: JSX, Virtual DOM, Functional Components, Props [5][6]", "\u2014"),
    "UTS",
    (9, "Sub-CPMK-3.1: Mampu mengelola state lokal komponen via React Hook useState & useEffect (C3)",
        "Komponen stateful bereaksi benar terhadap perubahan data (re-render tepat)",
        "Rubrik kompilasi praktikum formatif",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: modul React Hooks; commit repo proyek",
        "React Hooks Fundamental: useState, useEffect, useRef [5][6]", "\u2014"),
    (10, "Sub-CPMK-3.1: Mampu mengelola state global lintas komponen via Context API (C4)",
        "State global (tema/otentikasi) terbagi lintas \u2265 3 komponen tanpa prop drilling",
        "Rubrik kompilasi praktikum formatif",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: studi kasus state global; forum diskusi",
        "Global State Management: Context API & Custom Hooks [5][6]", "\u2014"),
    (11, "Sub-CPMK-3.2: Mampu mengonfigurasi navigasi SPA via React Router (C3)",
        "Rute multi-halaman, dynamic route, dan protected route berfungsi",
        "Rubrik kompilasi praktikum formatif",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: modul routing; repo proyek diperbarui",
        "Client-Side Routing: React Router v6, Dynamic & Protected Routes [6][7]", "\u2014"),
    (12, "Sub-CPMK-4.1: Mampu mengonsumsi REST API backend, menangani loading & error state (C4)",
        "SPA terintegrasi API eksternal: loading skeleton & error boundary berfungsi",
        "Rubrik analitik Tugas 2; penilaian milestone integrasi sistem",
        "Case Method 100'; Lab Coding 170'",
        "Edlink: spesifikasi milestone; pengumpulan Tugas 2",
        "REST API Integration: Axios, Loading Skeletons, Error Boundary [5][6]",
        "Tugas 2: 25% (Milestone Proyek 2 — evaluasi Sub-CPMK Pekan 9\u201311)"),
    (13, "Sub-CPMK-4.1: Mampu mengelola form kompleks menggunakan React Hook Form & Zod (C4)",
        "Form multi-field tervalidasi skema Zod; pesan error aksesibel",
        "Rubrik kompilasi praktikum formatif",
        "Kuliah 100'; Lab Hands-on 170'",
        "Edlink: dokumentasi RHF & Zod; konsultasi proyek",
        "Form Management: React Hook Form & Validasi Skema Zod [5][8]", "\u2014"),
    (14, "Sub-CPMK-4.2: Mampu mengoptimalkan performa web SPA dan audit Google Lighthouse (C5)",
        "Skor Lighthouse Performance \u2265 85 pada build produksi",
        "Rubrik kompilasi audit Lighthouse",
        "Case Method Workshop 270'",
        "Edlink: laporan audit performa; forum optimasi",
        "Web Performance Optimization: Code Splitting, Lazy Loading, Lighthouse [4][9]", "\u2014"),
    (15, "Sub-CPMK-4.2: Mampu mendeploy aplikasi SPA ke platform cloud Vercel/Netlify (C4)",
        "URL produksi aktif; pipeline build otomatis dari repo GitHub",
        "Rubrik kompilasi deployment; verifikasi URL produksi",
        "PjBL Studio 270'",
        "Edlink: panduan deploy; submission URL produksi",
        "Production Build & Cloud Deployment (Vercel/Netlify/GitHub Actions) [9][10]", "\u2014"),
    "UAS",
]

UTS_LABEL = ("Evaluasi Tengah Semester (UTS) — Ujian Koding Terjadwal: Responsive Layout "
             "CSS Grid & JavaScript ES6+ (CPMK-1 s.d. CPMK-3)")
UAS_LABEL = ("Evaluasi Akhir Semester (UAS) — Sidang Demonstrasi Produk Aplikasi Web "
             "Single Page Application / SPA (Seluruh CPMK)")

UTS_CELL = (
    "Indikator: Skor ujian praktik \u2265 70; solusi responsive layout + skrip ES6+ berjalan tanpa "
    "error.\n"
    "Kriteria & Teknik: Rubrik analitik UTS; ujian praktik live coding (170').\n"
    "Luring: Live Coding Lab Test (170').\n"
    "Daring: Edlink — pengumuman ruang ujian & unggah berkas.\n"
    "Materi: Cakupan Mg 1\u20137 — HTML5, CSS3 Flexbox/Grid, JavaScript ES6+ [1][2][3].\n"
    "Bobot Penilaian: UTS 25%."
)
UAS_CELL = (
    "Indikator: Produk SPA terdeploy dan terintegrasi API; skor demo & portofolio \u2265 70.\n"
    "Kriteria & Teknik: Rubrik analitik UAS; Demo Day & defense (170').\n"
    "Luring: Sidang demonstrasi produk SPA.\n"
    "Daring: Edlink — berkas final proyek & tautan deploy.\n"
    "Materi: Cakupan seluruh Sub-CPMK — SPA React terintegrasi, optimal, terdeploy [5][6][9].\n"
    "Bobot Penilaian: UAS 30%."
)

# ------------------------------------------------------------- lampiran
def rub(title, header, rows):
    return ("table", title, header, rows)

LAMPIRAN = [
    # [penugasan1]
    [
        ("p", "TUGAS 1 — MILESTONE PROYEK 1: HALAMAN WEB RESPONSIF MULTI-DEVICE (Pekan 4, Bobot 20%)"),
        ("p", "Mahasiswa membangun satu halaman web (landing/dashboard) responsif multi-device "
              "menggunakan Semantic HTML5 dan CSS3 modern (Flexbox, Grid, Variabel CSS) tanpa "
              "framework CSS wajib."),
        ("p", "Spesifikasi wajib: (1) struktur semantic minimal 5 area (header, nav, main, section, "
              "footer) dan lolos validator W3C; (2) layout dashboard responsif berbasis CSS Grid "
              "12-kolom dengan minimal 3 breakpoint (mobile \u2264 640px, tablet \u2264 1024px, "
              "desktop); (3) komponen kartu/daftar menggunakan Flexbox; (4) theming via CSS custom "
              "properties; (5) aksesibilitas dasar (alt text, kontras, label form)."),
        ("p", "Deliverable: repository GitHub + halaman live (GitHub Pages) + laporan singkat 1\u20132 "
              "halaman (keputusan layout, breakpoint, screenshot 3 viewport). Penilaian menggunakan "
              "rubrik analitik berikut; cakupan Sub-CPMK-1.1 & 1.2 (CPMK-1 \u2192 CPL P4)."),
    ],
    # [rubriktugas1]
    [
        rub("Rubrik Penilaian Tugas 1 (Total 100)",
            ["Kriteria", "Bobot", "Sangat Baik (86\u2013100)", "Baik (76\u201385)",
             "Cukup (66\u201375)", "Kurang (56\u201365)", "Sangat Kurang (0\u201355)"],
            [["Semantic HTML5 & Validitas W3C", "20%", "Struktur semantic lengkap & valid",
              "Semantic tepat, 1\u20132 warning", "Semantic dasar, beberapa error",
              "Banyak div/span tanpa makna", "Tidak semantic & tidak valid"],
             ["Layout Flexbox", "20%", "Komponen fleksibel rapi di semua ukuran",
              "Flexbox tepat, minor misalignment", "Flexbox dasar berfungsi",
              "Layout sering bergeser", "Tidak menggunakan Flexbox"],
             ["CSS Grid & Responsive 3 Breakpoint", "25%", "Grid 12-kolom adaptif sempurna",
              "Grid benar, 1 breakpoint kurang", "Grid dasar berfungsi",
              "Responsif tidak konsisten", "Tidak responsif"],
             ["Kualitas Kode & Organisasi CSS", "15%", "CSS terstruktur, custom properties rapi",
              "Terstruktur, minor duplikasi", "Dapat dipahami", "Berantakan",
              "Tidak terstruktur"],
             ["Aksesibilitas Dasar", "10%", "Alt, kontras, label lengkap",
              "1\u20132 temuan aksesibilitas", "Sebagian terpenuhi",
              "Banyak temuan", "Tidak diperhatikan"],
             ["Dokumentasi & Deployment", "10%", "Repo rapi + live + laporan lengkap",
              "Repo & live ada, laporan singkat", "Repo ada", "Hanya repo tanpa laporan",
              "Tidak ada deliverable"]]),
    ],
    # [soaluts]
    [
        ("p", "UJIAN TENGAH SEMESTER (Pekan 8, Bobot 25%) — UJIAN PRAKTIK LIVE CODING (170 MENIT)"),
        ("p", "Studi kasus: membangun halaman dashboard responsif dan aplikasi interaktif kecil "
              "dalam satu proyek. Cakupan: Mg 1\u20137 (CPMK-1 s.d. CPMK-3 fase awal)."),
        ("p", "Soal: (1) Bangun layout dashboard CSS Grid 12-kolom responsif (3 breakpoint) sesuai "
              "mockup yang diberikan; (2) implementasi fitur interaktif menggunakan JavaScript ES6+ "
              "modul (arrow function, destructuring, import/export): manipulasi DOM, event handling, "
              "dan validasi form client-side; (3) konsumsi satu REST API publik menggunakan Fetch "
              "API dengan Async/Await lengkap dengan penanganan error dan loading state sederhana."),
        ("p", "Ketentuan: open documentation resmi (MDN/react.dev), dilarang kolaborasi dan AI code "
              "generator; submit repository GitHub pribadi pada akhir sesi. Kriteria ketuntasan "
              "minimal skor 70."),
    ],
    # [rubrikuts]
    [
        rub("Rubrik Penilaian UTS (Total 100)",
            ["Kriteria", "Bobot", "Poin Penuh", "Poin Sebagian", "Poin Minimal", "Tidak Ada"],
            [["Responsive Layout CSS Grid (3 breakpoint)", "30%", "30", "20", "10", "0"],
             ["JavaScript ES6+ & Modularitas", "25%", "25", "17", "9", "0"],
             ["DOM Manipulation & Event Handling", "15%", "15", "10", "5", "0"],
             ["Async/Await, Fetch API & Error Handling", "20%", "20", "13", "7", "0"],
             ["Kualitas Kode & Organisasi", "10%", "10", "7", "4", "0"]]),
    ],
    # [tugas2]
    [
        ("p", "TUGAS 2 — MILESTONE PROYEK 2: SPA REACT TERINTEGRASI REST API (Pekan 12, Bobot 25%)"),
        ("p", "Melanjutkan proyek SPA dari Pekan 7, mahasiswa menambahkan: (1) state lokal dengan "
              "useState/useEffect dan state global dengan Context API + custom hooks (tanpa prop "
              "drilling); (2) navigasi multi-halaman React Router v6 termasuk dynamic route dan "
              "protected route; (3) integrasi REST API eksternal menggunakan Axios dengan loading "
              "skeleton dan error boundary; (4) satu form kompleks dengan React Hook Form + "
              "validasi skema Zod."),
        ("p", "Deliverable: repository GitHub + deployment preview (Vercel/Netlify) + demo video "
              "maksimal 5 menit. Cakupan evaluasi: Sub-CPMK-3.1, 3.2, dan 4.1 (Pekan 9\u201311) "
              "\u2192 CPMK-3 (KK5) dan CPMK-4 (KK5). Penilaian menggunakan rubrik analitik berikut."),
    ],
    # [rubriktugas2]
    [
        rub("Rubrik Penilaian Tugas 2 (Total 100)",
            ["Kriteria", "Bobot", "Sangat Baik (86\u2013100)", "Baik (76\u201385)",
             "Cukup (66\u201375)", "Kurang (56\u201365)", "Sangat Kurang (0\u201355)"],
            [["Arsitektur Komponen React", "20%", "Komposisi komponen bersih & reusable",
              "Komponen tepat, minor duplikasi", "Komponen dasar berfungsi",
              "Komponen monolitik", "Tidak berbasis komponen"],
             ["State Management (Hooks & Context)", "25%", "State global tepat tanpa prop drilling",
              "Context benar, minor re-render", "State lokal berfungsi",
              "State tersebar tak terkelola", "Tidak ada manajemen state"],
             ["Routing SPA (Dynamic & Protected)", "15%", "Semua rute + guard berfungsi",
              "Rute lengkap, guard sebagian", "Rute dasar berfungsi", "Rute tidak konsisten",
              "Tanpa routing"],
             ["Integrasi REST API & UX State", "25%", "Loading skeleton & error boundary sempurna",
              "Integrasi benar, 1 UX state kurang", "Integrasi dasar berfungsi",
              "Error tidak tertangani", "Tidak terintegrasi"],
             ["Kualitas Kode & Deployment", "15%", "Kode bersih + preview aktif",
              "Kode baik, deploy ada isu minor", "Deploy aktif", "Deploy gagal",
              "Tidak deploy"]]),
    ],
    # [soaluas]
    [
        ("p", "UJIAN AKHIR SEMESTER (Pekan 16, Bobot 30%) — SIDANG DEMONSTRASI PRODUK SPA (DEMO DAY & DEFENSE, 170 MENIT)"),
        ("p", "Mahasiswa (individu/kelompok kecil) mempresentasikan produk akhir SPA hasil "
              "pengembangan berkesinambungan Mg 4\u201315: aplikasi Single Page Application React "
              "lengkap — komponen modular, state global Context API, routing protected, integrasi "
              "REST API, form tervalidasi Zod, skor Google Lighthouse \u2265 85, dan terdeploy di "
              "Vercel/Netlify."),
        ("p", "Format sidang: demo live 15 menit (alur utama aplikasi, penanganan error, performa) "
              "+ tanya jawab 5 menit. Deliverable akhir: URL produksi aktif, repository GitHub, "
              "slide presentasi, dan write-up portofolio 2\u20133 halaman (arsitektur, keputusan "
              "teknis, hasil audit Lighthouse). Kriteria ketuntasan minimal skor 70."),
    ],
    # [rubrikuas]
    [
        rub("Rubrik Penilaian UAS (Total 100)",
            ["Kriteria", "Bobot", "Poin"],
            [["Fungsionalitas SPA & kelengkapan fitur", "25%", "25"],
             ["Integrasi REST API & penanganan data", "20%", "20"],
             ["Performa (Lighthouse \u2265 85)", "15%", "15"],
             ["Manajemen form & validasi (Zod)", "10%", "10"],
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
    A("# RPS STI-311 — PENGEMBANGAN WEB FRONT END (*Web Front End Development*)")
    A("")
    A("**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN)  ")
    A("**Fakultas:** Sains dan Teknologi Informasi (FSTI) — Universitas Widyagama Malang  ")
    A(f"**Nomor Dokumen:** 071030.{SCALARS['{{kodeprodi}}']}  ")
    A(f"**Tanggal Penyusunan:** {TGL_SUSUN}  ")
    A("**Sumber:** Template Master RPS Generator FSTI UWG (`Template_RPS_GEN_2026_20092026-SWO.docx`) "
      "— seluruh 18 tag `{{...}}` + 25 tag `[...]` terisi; data dari Dok 003/005/007/008/043.  ")
    A("**Keluaran pendamping:** `DOCX/RPS_STI-311_Web_Front_End_Development.docx`")
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
    A("*RPS STI-311 dibangkitkan dari Template Master RPS Generator FSTI UWG oleh "
      "`_tools/generate_rps_sti311_docx.py` — unit pilot ke-2 RPS Batch Generator "
      "(setelah STI-416 V2).*")

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
            p.add_run("SEPTEMBER, 2026")
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
