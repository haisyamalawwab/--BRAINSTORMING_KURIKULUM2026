// Build: Presentasi Perkenalan Prodi SISTEKIN untuk Tim Kerja Sama BINUS (BDSRC)
// Master prompt: 054_MASTER_PROMPT_PRESENTASI_PERKENALAN_PRODI_SISTEKIN_BINUS_BDSRC.md
const pptxgen = require("pptxgenjs");

const A = "ASSETS_PRESENTASI_BINUS_BDSRC/";
const ORANGE = "F26A21", ORANGE_DARK = "D94E12", ORANGE_TINT = "FDEADF";
const PURPLE = "5B2D8E", PURPLE_LIGHT = "7C3AED", PURPLE_TINT = "F0E8F7";
const TEXT = "1F2937", MUTED = "6B7280", WHITE = "FFFFFF", CREAM_TXT = "FFE3D0", HAIR = "E5E7EB";
const F = "Segoe UI";

let p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
p.author = "Prodi SISTEKIN FSTI UWG";
p.title = "Perkenalan SISTEKIN x BINUS BDSRC";

const W = 13.33, M = 0.6;
const shadow = () => ({ type: "outer", color: "9A3412", blur: 7, offset: 2, angle: 90, opacity: 0.18 });

// ---------- helpers ----------
function chrome(s, pageNo) {
  // lambang kecil kanan-atas + footer + nomor halaman (slide isi & penutup)
  s.addImage({ path: A + "lambang_uwg_rgba.png", x: 12.12, y: 0.32, w: 0.6, h: 0.6 });
  s.addText("SISTEKIN FSTI UWG × BINUS BDSRC — 2026", { x: M, y: 7.06, w: 6, h: 0.3, fontFace: F, fontSize: 12, color: pageNo.dark ? "FFE3D0" : MUTED, margin: 0 });
  s.addText(String(pageNo.n), { x: 12.35, y: 7.06, w: 0.38, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: pageNo.dark ? WHITE : ORANGE, align: "right", margin: 0 });
}
function header(s, kicker, title) {
  s.addText(kicker, { x: M, y: 0.5, w: 8, h: 0.32, fontFace: F, fontSize: 12, bold: true, color: ORANGE, charSpacing: 3, margin: 0 });
  s.addText(title, { x: M, y: 0.84, w: 11.2, h: 0.62, fontFace: F, fontSize: 30, bold: true, color: TEXT, margin: 0 });
}

// ================= SLIDE 1 — COVER =================
let s1 = p.addSlide();
s1.background = { path: A + "bg_orange_gradient.png" };
s1.addImage({ path: A + "lambang_uwg_rgba.png", x: 0.6, y: 0.5, w: 1.42, h: 1.42 });
s1.addShape(p.shapes.ROUNDED_RECTANGLE, { x: 9.3, y: 0.62, w: 3.43, h: 1.24, fill: { color: WHITE }, rectRadius: 0.09, shadow: shadow() });
s1.addImage({ path: A + "logo_sistekin.png", x: 9.58, y: 0.79, w: 2.87, h: 0.97 });
s1.addText("FORUM KERJA SAMA FSTI UWG × BINUS BDSRC", { x: 1.67, y: 2.18, w: 10, h: 0.34, align: "center", fontFace: F, fontSize: 13, bold: true, color: WHITE, charSpacing: 3, margin: 0 });
s1.addText("SISTEKIN", { x: 1.67, y: 2.52, w: 10, h: 1.1, align: "center", fontFace: F, fontSize: 64, bold: true, color: WHITE, margin: 0 });
s1.addText("S1 Sistem dan Teknologi Informasi", { x: 1.67, y: 3.68, w: 10, h: 0.5, align: "center", fontFace: F, fontSize: 26, color: WHITE, margin: 0 });
s1.addText("Fakultas Sains dan Teknologi Informasi  ·  Universitas Widyagama Malang", { x: 1.67, y: 4.26, w: 10, h: 0.38, align: "center", fontFace: F, fontSize: 15, color: CREAM_TXT, margin: 0 });
s1.addText("“Integrator AI ke Sistem & Platform Nyata”", { x: 1.67, y: 4.78, w: 10, h: 0.42, align: "center", fontFace: F, fontSize: 18, italic: true, bold: true, color: WHITE, margin: 0 });
s1.addText("Ahmad Fairuzabadi, S.Kom., M.Kom. (Kaprodi)    ·    1 Oktober 2026    ·    Malang", { x: 1.67, y: 5.34, w: 10, h: 0.34, align: "center", fontFace: F, fontSize: 13.5, color: CREAM_TXT, margin: 0 });
s1.addShape(p.shapes.ROUNDED_RECTANGLE, { x: 5.14, y: 6.02, w: 3.05, h: 0.74, fill: { color: WHITE }, rectRadius: 0.09, shadow: shadow() });
s1.addImage({ path: A + "bdsrc_logo.png", x: 5.31, y: 6.2, w: 2.71, h: 0.385 });
s1.addText("Forum Kerja Sama", { x: 4.67, y: 6.86, w: 4, h: 0.3, align: "center", fontFace: F, fontSize: 12, color: WHITE, margin: 0 });
s1.addNotes("Buka dengan salam. Sampaikan: kami datang bukan sebagai prodi lama yang mencari validasi, tetapi partner muda yang lincah untuk riset AI terapan bersama BDSRC. Sebut judul tagline.");

// ================= SLIDE 2 — PROFIL & VISI =================
let s2 = p.addSlide();
s2.background = { color: WHITE };
chrome(s2, { n: 2, dark: false });
header(s2, "PROFIL PRODI", "Profil Singkat & Visi 2045");

const stats = [
  ["2025", "Resmi berdiri 4 September 2025", "SK Kemendiktisaintek No. 747/B/O/2025"],
  ["Baik", "Status akreditasi", "Prodi baru — generasi pertama"],
  ["146", "Total SKS kurikulum", "Problem-solving & project-based learning"],
];
stats.forEach((st, i) => {
  const y = 1.78 + i * 1.18;
  s2.addText(st[0], { x: M, y, w: 2.0, h: 0.95, fontFace: F, fontSize: 44, bold: true, color: ORANGE, margin: 0, valign: "middle" });
  s2.addText(st[1], { x: 2.75, y: y + 0.08, w: 3.45, h: 0.4, fontFace: F, fontSize: 15.5, bold: true, color: TEXT, margin: 0 });
  s2.addText(st[2], { x: 2.75, y: y + 0.5, w: 3.45, h: 0.42, fontFace: F, fontSize: 12.5, color: MUTED, margin: 0 });
});
s2.addShape(p.shapes.LINE, { x: 6.42, y: 1.85, w: 0, h: 3.15, line: { color: HAIR, width: 1 } });

s2.addShape(p.shapes.ROUNDED_RECTANGLE, { x: 6.78, y: 1.78, w: 5.95, h: 2.18, fill: { color: PURPLE_TINT }, rectRadius: 0.1 });
s2.addText("VISI 2045", { x: 7.08, y: 1.98, w: 3, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: PURPLE, charSpacing: 2.5, margin: 0 });
s2.addText("“Unggul dalam pengembangan sistem & teknologi informasi cerdas terintegrasi kecerdasan artifisial serta technopreneurship berbasis kebutuhan masyarakat dan industri.”",
  { x: 7.08, y: 2.32, w: 5.35, h: 1.5, fontFace: F, fontSize: 15, color: TEXT, margin: 0, lineSpacingMultiple: 1.12 });
s2.addText([
  { text: "TI berfokus riset algoritma AI murni — SISTEKIN ", options: {} },
  { text: "mengintegrasikan AI ke sistem & platform nyata", options: { bold: true, color: PURPLE } },
  { text: ": UMKM, pendidikan, layanan publik, industri kreatif.", options: {} },
], { x: 6.78, y: 4.18, w: 5.95, h: 0.95, fontFace: F, fontSize: 14.5, color: TEXT, margin: 0, lineSpacingMultiple: 1.1 });

s2.addText("4 PROFIL LULUSAN — KURIKULUM 2026", { x: M, y: 5.32, w: 6, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: MUTED, charSpacing: 2.5, margin: 0 });
const pls = [
  ["PL-1", "Intelligent Information Systems & Data/AI Engineer"],
  ["PL-2", "Cloud Infrastructure, Cybersecurity & Smart Systems Integrator"],
  ["PL-3", "UI/UX Designer & Digital Platform Engineer"],
  ["PL-4", "Digital Technopreneur & IT Product Innovator"],
];
pls.forEach((t, i) => {
  s2.addShape(p.shapes.ROUNDED_RECTANGLE, { x: M + i * 3.07, y: 5.68, w: 2.95, h: 0.72, fill: { color: ORANGE_TINT }, rectRadius: 0.09 });
  s2.addText([
    { text: t[0] + "  ", options: { fontSize: 11.5, bold: true, color: PURPLE } },
    { text: t[1], options: { fontSize: 12.5, bold: true, color: TEXT } },
  ], { x: M + i * 3.07 + 0.08, y: 5.68, w: 2.79, h: 0.72, align: "center", valign: "middle", fontFace: F, margin: 0, lineSpacingMultiple: 1.0 });
});
s2.addNotes("Tekankan tiga angka: berdiri 2025, akreditasi Baik, 146 SKS. Visi 2045 adalah turunan VMTS universitas. Positioning: kami integrator AI, bukan pesaing riset algoritma murni. 4 Profil Lulusan K2026 (Dok. 002): PL-1 & PL-2 lahir dari peminatan P1/P2, PL-3 dari P3, PL-4 lintas peminatan.");

// ================= SLIDE 3 — KURIKULUM =================
let s3 = p.addSlide();
s3.background = { color: WHITE };
chrome(s3, { n: 3, dark: false });
header(s3, "KURIKULUM", "Kurikulum OBE 2026 Berbasis Proyek");
s3.addText("3 PEMINATAN — MAHASISWA MEMILIH SATU PAKET", { x: M, y: 1.5, w: 8, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: MUTED, charSpacing: 2, margin: 0 });

const trk = [["P1", "Integrated Smart Systems"], ["P2", "Cloud Infrastructure & Cybersecurity"], ["P3", "Digital Platform Engineering"]];
trk.forEach((t, i) => {
  const x = M + i * 4.12;
  s3.addShape(p.shapes.ROUNDED_RECTANGLE, { x, y: 1.86, w: 3.89, h: 1.62, fill: { color: WHITE }, rectRadius: 0.1, shadow: shadow() });
  s3.addText(t[0], { x: x + 0.28, y: 2.02, w: 1.2, h: 0.5, fontFace: F, fontSize: 26, bold: true, color: ORANGE, margin: 0 });
  s3.addText(t[1], { x: x + 0.28, y: 2.52, w: 3.35, h: 0.62, fontFace: F, fontSize: 15.5, bold: true, color: TEXT, margin: 0 });
  s3.addText("Paket peminatan @18 SKS", { x: x + 0.28, y: 3.12, w: 3.3, h: 0.28, fontFace: F, fontSize: 12, bold: true, color: PURPLE, margin: 0 });
});

s3.addShape(p.shapes.RECTANGLE, { x: 0, y: 3.78, w: W, h: 1.5, fill: { color: ORANGE_TINT } });
const facts = [
  ["OBE", "Outcome-Based Education — Permendikbudristek 53/2023"],
  ["Project-Based Learning", "Metode pembelajaran utama"],
  ["MBKM hingga 20 SKS", "Fleksibilitas magang & riset, semester 6-7"],
  ["4 Titik Asesmen Baku", "Skema penilaian seragam per mata kuliah"],
];
facts.forEach((f, i) => {
  const x = M + i * 3.07;
  s3.addText(f[0], { x, y: 3.98, w: 2.9, h: 0.38, fontFace: F, fontSize: 15, bold: true, color: ORANGE_DARK, margin: 0 });
  s3.addText(f[1], { x, y: 4.4, w: 2.85, h: 0.75, fontFace: F, fontSize: 12.5, color: TEXT, margin: 0, lineSpacingMultiple: 1.08 });
});

s3.addText("MK UNGGULAN", { x: M, y: 5.5, w: 4, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: MUTED, charSpacing: 2.5, margin: 0 });
const chips = ["Machine Learning", "Internet of Things", "UI/UX", "Data Warehouse & BI", "Smart City"];
const chipW = [2.25, 2.35, 1.15, 2.65, 1.65];
let cx = M;
chips.forEach((c, i) => {
  s3.addShape(p.shapes.ROUNDED_RECTANGLE, { x: cx, y: 5.84, w: chipW[i], h: 0.46, fill: { color: WHITE }, line: { color: ORANGE, width: 1.25 }, rectRadius: 0.22 });
  s3.addText(c, { x: cx, y: 5.84, w: chipW[i], h: 0.46, align: "center", valign: "middle", fontFace: F, fontSize: 12.5, bold: true, color: TEXT, margin: 0 });
  cx += chipW[i] + 0.18;
});
s3.addText([
  { text: "Mahasiswa lulus dengan ", options: {} },
  { text: "portofolio proyek nyata", options: { bold: true, color: ORANGE_DARK } },
  { text: ", bukan sekadar transkrip.", options: {} },
], { x: M, y: 6.5, w: 11.5, h: 0.42, fontFace: F, fontSize: 16.5, color: TEXT, margin: 0 });
s3.addNotes("Kurikulum OBE selaras Permendikbudristek 53/2023. Tiga peminatan @18 SKS; MBKM hingga 20 SKS di semester 6-7 dapat dikonversi ke magang/riset — termasuk riset bersama BDSRC.");

// ================= SLIDE 4 — RISET & SINERGI =================
let s4 = p.addSlide();
s4.background = { color: WHITE };
chrome(s4, { n: 4, dark: false });
header(s4, "RISET & SINERGI", "Kapasitas Riset & Sinergi dengan BDSRC");

s4.addShape(p.shapes.OVAL, { x: M, y: 1.66, w: 0.2, h: 0.2, fill: { color: ORANGE } });
s4.addText("SISTEKIN — FSTI UWG", { x: 0.95, y: 1.56, w: 4.5, h: 0.4, fontFace: F, fontSize: 16, bold: true, color: TEXT, margin: 0 });
const left = [
  ["Keahlian dosen", "Machine learning, image processing, text mining, fuzzy logic, VR/AR, audio signal processing"],
  ["Fasilitas lab", "Lab komputer, lab multimedia & IoT, ruang kolaborasi"],
  ["Fokus penerapan", "Smart city Malang, UMKM, pendidikan, industri kreatif"],
];
left.forEach((r, i) => {
  const y = 2.18 + i * 1.14;
  s4.addShape(p.shapes.ROUNDED_RECTANGLE, { x: M, y: y + 0.03, w: 0.34, h: 0.34, fill: { color: ORANGE_TINT }, rectRadius: 0.07 });
  s4.addShape(p.shapes.OVAL, { x: M + 0.12, y: y + 0.15, w: 0.1, h: 0.1, fill: { color: ORANGE } });
  s4.addText(r[0], { x: 1.12, y, w: 4.9, h: 0.36, fontFace: F, fontSize: 15, bold: true, color: TEXT, margin: 0 });
  s4.addText(r[1], { x: 1.12, y: y + 0.38, w: 4.9, h: 0.66, fontFace: F, fontSize: 13, color: MUTED, margin: 0, lineSpacingMultiple: 1.08 });
});

s4.addShape(p.shapes.RIGHT_ARROW, { x: 6.12, y: 2.62, w: 1.05, h: 0.42, fill: { color: ORANGE } });
s4.addShape(p.shapes.LEFT_ARROW, { x: 6.12, y: 3.28, w: 1.05, h: 0.42, fill: { color: PURPLE } });
s4.addText("SINERGI", { x: 6.02, y: 3.82, w: 1.25, h: 0.3, align: "center", fontFace: F, fontSize: 11.5, bold: true, color: MUTED, charSpacing: 2, margin: 0 });

s4.addShape(p.shapes.OVAL, { x: 7.5, y: 1.66, w: 0.2, h: 0.2, fill: { color: PURPLE } });
s4.addText("BINUS — BDSRC", { x: 7.85, y: 1.56, w: 4.5, h: 0.4, fontFace: F, fontSize: 16, bold: true, color: TEXT, margin: 0 });
const right = [
  ["Big Data & IIoT Sensor Analytics", "Bidang riset inti BDSRC"],
  ["AI R&D", "Riset & pengembangan kecerdasan artifisial"],
  ["Bioinformatics & Data Science", "Data science untuk sains & industri"],
];
right.forEach((r, i) => {
  const y = 2.18 + i * 1.14;
  s4.addShape(p.shapes.ROUNDED_RECTANGLE, { x: 7.5, y: y + 0.03, w: 0.34, h: 0.34, fill: { color: PURPLE_TINT }, rectRadius: 0.07 });
  s4.addShape(p.shapes.OVAL, { x: 7.62, y: y + 0.15, w: 0.1, h: 0.1, fill: { color: PURPLE } });
  s4.addText(r[0], { x: 8.02, y, w: 4.7, h: 0.36, fontFace: F, fontSize: 15, bold: true, color: TEXT, margin: 0 });
  s4.addText(r[1], { x: 8.02, y: y + 0.38, w: 4.7, h: 0.66, fontFace: F, fontSize: 13, color: MUTED, margin: 0, lineSpacingMultiple: 1.08 });
});

s4.addShape(p.shapes.RECTANGLE, { x: 0, y: 5.82, w: W, h: 1.02, fill: { color: ORANGE_TINT } });
s4.addText([
  { text: "SISTEKIN membawa ", options: {} },
  { text: "use case & implementasi", options: { bold: true, color: ORANGE_DARK } },
  { text: " — BDSRC membawa ", options: {} },
  { text: "kedalaman riset & data", options: { bold: true, color: PURPLE } },
  { text: ": riset terapan dari hulu (model) ke hilir (sistem nyata).", options: {} },
], { x: 0.9, y: 5.82, w: 11.53, h: 1.02, align: "center", valign: "middle", fontFace: F, fontSize: 15.5, color: TEXT, margin: 0 });
s4.addNotes("Pesan kunci: komplementer, bukan kompetitor. SISTEKIN kuat di implementasi sistem nyata (smart city Malang, UMKM); BDSRC kuat di kedalaman riset AI/Big Data.");

// ================= SLIDE 5 — KOLABORASI =================
let s5 = p.addSlide();
s5.background = { path: A + "bg_orange_gradient.png" };
s5.addImage({ path: A + "lambang_uwg_rgba.png", x: 12.12, y: 0.32, w: 0.6, h: 0.6 });
s5.addText("FORUM KERJA SAMA", { x: M, y: 0.52, w: 8, h: 0.32, fontFace: F, fontSize: 12, bold: true, color: WHITE, charSpacing: 3, margin: 0 });
s5.addText("5 Peluang Kolaborasi SISTEKIN × BDSRC", { x: M, y: 0.86, w: 11.5, h: 0.62, fontFace: F, fontSize: 30, bold: true, color: WHITE, margin: 0 });

const ops = [
  ["MBKM", " — magang & riset mahasiswa SISTEKIN di BDSRC (konversi hingga 20 SKS)"],
  ["Riset & publikasi bersama", " — AI terapan, big data, smart systems"],
  ["Guest lecture & dosen praktisi", " — lintas kampus"],
  ["Proyek nyata bersama", " — capstone berbasis use case Malang"],
  ["Community engagement", " — pemberdayaan digital UMKM & layanan publik"],
];
ops.forEach((o, i) => {
  const y = 1.86 + i * 0.8;
  s5.addShape(p.shapes.OVAL, { x: M, y, w: 0.5, h: 0.5, fill: { color: PURPLE } });
  s5.addText(String(i + 1), { x: M, y, w: 0.5, h: 0.5, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: WHITE, margin: 0 });
  s5.addText([
    { text: o[0], options: { bold: true } },
    { text: o[1], options: {} },
  ], { x: 1.32, y: y - 0.04, w: 11.3, h: 0.6, valign: "middle", fontFace: F, fontSize: 15.5, color: WHITE, margin: 0 });
});

s5.addText("sistekin.widyagama.ac.id    ·    @fsti.uwg    ·    Kampus II Jl. Borobudur No. 35 Malang", { x: M, y: 5.98, w: 11.5, h: 0.34, fontFace: F, fontSize: 13, color: CREAM_TXT, margin: 0 });
s5.addShape(p.shapes.ROUNDED_RECTANGLE, { x: 3.79, y: 6.48, w: 5.75, h: 0.62, fill: { color: WHITE }, rectRadius: 0.31, shadow: shadow() });
s5.addText("Mari mulai dari satu proyek perintis — semester ini.", { x: 3.79, y: 6.48, w: 5.75, h: 0.62, align: "center", valign: "middle", fontFace: F, fontSize: 15.5, bold: true, color: PURPLE, margin: 0 });
s5.addText("SISTEKIN FSTI UWG × BINUS BDSRC — 2026", { x: M, y: 7.06, w: 6, h: 0.3, fontFace: F, fontSize: 12, color: "FFD9BF", margin: 0 });
s5.addText("5", { x: 12.35, y: 7.06, w: 0.38, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: WHITE, align: "right", margin: 0 });
s5.addNotes("Tutup dengan CTA: satu proyek perintis semester ini. Tawarkan follow-up: penyusunan ruang lingkup riset perintis dan jadwal diskusi teknis bersama BDSRC.");

// ================= SLIDE 6 — TIM DOSEN (OVERVIEW) =================
let s6 = p.addSlide();
s6.background = { color: WHITE };
chrome(s6, { n: 6, dark: false });
header(s6, "RISET & PENGABDIAN", "Tim Dosen Homebase SISTEKIN");

s6.addText("±800", { x: M, y: 1.95, w: 3.6, h: 1.15, fontFace: F, fontSize: 66, bold: true, color: ORANGE, margin: 0 });
s6.addText("sitasi Google Scholar teragregasi", { x: M, y: 3.12, w: 3.4, h: 0.62, fontFace: F, fontSize: 14, bold: true, color: TEXT, margin: 0, lineSpacingMultiple: 1.05 });
s6.addText([
  { text: "6 dosen homebase · snapshot 1 Okt 2026", options: { bold: true, color: PURPLE, breakLine: true } },
  { text: "Angka diverifikasi langsung dari profil Google Scholar & SINTA tiap dosen.", options: { color: MUTED } },
], { x: M, y: 3.9, w: 3.35, h: 1.6, fontFace: F, fontSize: 12, margin: 0, lineSpacingMultiple: 1.12 });
s6.addShape(p.shapes.LINE, { x: 4.35, y: 1.95, w: 0, h: 4.55, line: { color: HAIR, width: 1 } });

const tim = [
  ["Syahroni Wahyu Iriananda, S.Kom., M.T.", "Kaprodi SISTEKIN 2026", "Data Science · AI · NLP · Text Mining", "511"],
  ["Rangga Pahlevi Putra, S.Pd., M.T.", "Dosen Homebase", "Image Processing · Biometric · Computer Vision", "74"],
  ["Ismail Akbar, S.Kom., M.Kom.", "Dosen Homebase", "Text Mining · NLP · Deep Learning · Optimization", "123"],
  ["Affi Nizar Suksmawati, S.Kom., M.Cs.", "Dosen Homebase", "Expert System · Fuzzy Logic · ML · Health Informatics", "82"],
  ["Devi Septiani, S.Kom., M.Kom.", "Dosen Homebase", "Manajemen SI · VR & AR · Multimedia 3D", "—"],
  ["Mamba'us Sa'adah, S.ST., M.T.", "Dosen Homebase", "Audio Signal Processing · Multimedia", "14"],
];
tim.forEach((t, i) => {
  const y = 1.92 + i * 0.79;
  s6.addShape(p.shapes.ROUNDED_RECTANGLE, { x: 4.72, y: y + 0.03, w: 0.66, h: 0.66, fill: { color: i === 0 ? PURPLE_TINT : ORANGE_TINT }, rectRadius: 0.09 });
  s6.addText(String(i + 1), { x: 4.72, y: y + 0.03, w: 0.66, h: 0.66, align: "center", valign: "middle", fontFace: F, fontSize: 17, bold: true, color: i === 0 ? PURPLE : ORANGE, margin: 0 });
  s6.addText(t[0], { x: 5.55, y, w: 5.1, h: 0.32, fontFace: F, fontSize: 14, bold: true, color: TEXT, margin: 0 });
  s6.addText([
    { text: t[2], options: { color: MUTED } },
    { text: "   —   " + t[1], options: { color: i === 0 ? PURPLE : MUTED, bold: i === 0 } },
  ], { x: 5.55, y: y + 0.33, w: 5.4, h: 0.3, fontFace: F, fontSize: 11.5, margin: 0 });
  s6.addText([
    { text: t[3], options: { fontSize: 19, bold: true, color: ORANGE } },
    { text: "  sitasi", options: { fontSize: 11, color: MUTED } },
  ], { x: 11.0, y: y + 0.06, w: 1.7, h: 0.58, align: "right", valign: "middle", fontFace: F, margin: 0 });
});
s6.addNotes("Slide ringkasan tim. Pesan: prodi muda tapi tim riset aktif — ±790 sitasi teragregasi; tiap dosen punya klaster keilmuan yang saling melengkapi. Detail per dosen di 6 slide berikut.");

// ================= SLIDE 7-12 — PROFIL PER DOSEN =================
const bu2 = () => ({ code: "2022", indent: 10, color: "F26A21" });
function profilSlide(no, d) {
  let s = p.addSlide();
  s.background = { color: WHITE };
  chrome(s, { n: no, dark: false });
  s.addText(d.kicker, { x: M, y: 0.5, w: 8.5, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: ORANGE, charSpacing: 3, margin: 0 });
  s.addText(d.nama, { x: M, y: 0.82, w: 9.0, h: 0.62, fontFace: F, fontSize: 26, bold: true, color: TEXT, margin: 0 });
  s.addText(d.fokus, { x: M, y: 1.46, w: 9.0, h: 0.34, fontFace: F, fontSize: 13.5, color: PURPLE, margin: 0 });

  s.addText("SITASI SCHOLAR", { x: 8.85, y: 0.56, w: 2.9, h: 0.26, align: "right", fontFace: F, fontSize: 11, bold: true, color: MUTED, charSpacing: 2, margin: 0 });
  s.addText(d.sitasi, { x: 8.85, y: 0.8, w: 2.9, h: 0.62, align: "right", fontFace: F, fontSize: 36, bold: true, color: ORANGE, margin: 0 });
  s.addText([
    { text: "SINTA ID: ", options: { color: MUTED } },
    { text: d.sinta, options: { bold: true, color: TEXT } },
  ], { x: 8.85, y: 1.44, w: 2.9, h: 0.3, align: "right", fontFace: F, fontSize: 12.5, margin: 0 });
  if (d.extra) s.addText(d.extra, { x: 8.0, y: 1.74, w: 3.75, h: 0.28, align: "right", fontFace: F, fontSize: 11, color: PURPLE, margin: 0 });
  s.addShape(p.shapes.LINE, { x: M, y: 2.0, w: 12.13, h: 0, line: { color: HAIR, width: 1 } });

  s.addText("PENELITIAN", { x: M, y: 2.22, w: 3, h: 0.3, fontFace: F, fontSize: 13, bold: true, color: ORANGE, charSpacing: 2.5, margin: 0 });
  s.addText(d.penelitian, { x: M, y: 2.6, w: 5.9, h: 1.72, fontFace: F, fontSize: 13, color: TEXT, margin: 0, lineSpacingMultiple: 1.12 });
  s.addText(d.pubs.map((t, i) => ({ text: t, options: { bullet: bu2(), breakLine: i < d.pubs.length - 1 } })),
    { x: M, y: 4.42, w: 5.9, h: 2.5, fontFace: F, fontSize: 12, color: "374151", margin: 0, paraSpaceAfter: 7, lineSpacingMultiple: 1.05 });

  s.addText("PENGABDIAN", { x: 6.95, y: 2.22, w: 3, h: 0.3, fontFace: F, fontSize: 13, bold: true, color: PURPLE, charSpacing: 2.5, margin: 0 });
  s.addText(d.pengabdian, { x: 6.95, y: 2.6, w: 5.78, h: 1.72, fontFace: F, fontSize: 13, color: TEXT, margin: 0, lineSpacingMultiple: 1.12 });
  s.addText(d.pkm.map((t, i) => ({ text: t, options: { bullet: { code: "2022", indent: 10, color: "5B2D8E" }, breakLine: i < d.pkm.length - 1 } })),
    { x: 6.95, y: 4.42, w: 5.78, h: 2.5, fontFace: F, fontSize: 12, color: "374151", margin: 0, paraSpaceAfter: 7, lineSpacingMultiple: 1.05 });
  return s;
}

// ================= SLIDE SUMMARY CARD PER DOSEN =================
function summarySlide(no, d) {
  let s = p.addSlide();
  s.background = { color: WHITE };
  chrome(s, { n: no, dark: false });
  s.addText(d.kicker, { x: M, y: 0.5, w: 8.5, h: 0.3, fontFace: F, fontSize: 12, bold: true, color: ORANGE, charSpacing: 3, margin: 0 });
  s.addText("SUMMARY", { x: 10.15, y: 0.5, w: 1.8, h: 0.3, align: "right", fontFace: F, fontSize: 12, bold: true, color: PURPLE, charSpacing: 3, margin: 0 });

  // placeholder foto: lingkaran putus-putus + inisial
  s.addShape(p.shapes.OVAL, { x: 0.85, y: 1.62, w: 2.55, h: 2.55, fill: { color: ORANGE_TINT }, line: { color: ORANGE, width: 1.5, dashType: "dash" } });
  s.addText(d.inisial, { x: 0.85, y: 1.62, w: 2.55, h: 2.55, align: "center", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: ORANGE, margin: 0 });
  s.addText("placeholder foto dosen", { x: 0.55, y: 4.3, w: 3.15, h: 0.28, align: "center", fontFace: F, fontSize: 11, italic: true, color: MUTED, margin: 0 });

  s.addText(d.nama, { x: 4.05, y: 1.62, w: 8.7, h: 0.66, fontFace: F, fontSize: 29, bold: true, color: TEXT, margin: 0 });
  s.addText(d.sub, { x: 4.05, y: 2.32, w: 8.7, h: 0.32, fontFace: F, fontSize: 13.5, color: MUTED, margin: 0 });
  s.addText(d.fokusLabel, { x: 4.05, y: 2.88, w: 8.7, h: 0.28, fontFace: F, fontSize: 11.5, bold: true, color: MUTED, charSpacing: 2.5, margin: 0 });

  // chips: primary (Scholar) oranye, secondary (direktori) ungu
  let cx = 4.05, cy = 3.24;
  const chips = d.chips.map(c => ({ ...c, w: 0.36 + c.t.length * 0.088 }));
  chips.forEach(c => {
    if (cx + c.w > 12.75) { cx = 4.05; cy += 0.68; }
    s.addShape(p.shapes.ROUNDED_RECTANGLE, { x: cx, y: cy, w: c.w, h: 0.52, fill: { color: c.sec ? PURPLE_TINT : ORANGE_TINT }, rectRadius: 0.26 });
    s.addText(c.t, { x: cx, y: cy, w: c.w, h: 0.52, align: "center", valign: "middle", fontFace: F, fontSize: 12.5, bold: true, color: c.sec ? PURPLE : TEXT, margin: 0 });
    cx += c.w + 0.16;
  });
  if (d.catatan) s.addText(d.catatan, { x: 4.05, y: cy + 0.62, w: 8.7, h: 0.28, fontFace: F, fontSize: 10.5, italic: true, color: MUTED, margin: 0 });

  s.addText("SOROTAN", { x: 4.05, y: 5.06, w: 3, h: 0.28, fontFace: F, fontSize: 11.5, bold: true, color: ORANGE, charSpacing: 2.5, margin: 0 });
  s.addText([
    { text: d.sorotan[0], options: { bold: true, color: PURPLE } },
    { text: d.sorotan[1], options: { color: TEXT } },
  ], { x: 4.05, y: 5.36, w: 8.7, h: 0.62, fontFace: F, fontSize: 13.5, margin: 0, lineSpacingMultiple: 1.1 });

  // mini-stats row
  d.stats.forEach((st, i) => {
    const x = 4.05 + i * 2.95;
    s.addText([
      { text: st[0] + "  ", options: { fontSize: 20, bold: true, color: ORANGE } },
      { text: st[1], options: { fontSize: 12, color: MUTED } },
    ], { x, y: 6.22, w: 2.85, h: 0.5, fontFace: F, margin: 0, valign: "middle" });
  });
  s.addNotes("Ganti placeholder foto: klik kanan lingkaran → Format Shape → Fill → Picture fill → pilih foto dosen. Fokus bidang diambil dari interest profil Google Scholar dosen (chip oranye); chip ungu = bidang keahlian tambahan dari direktori FSTI.");
  return s;
}

const summaries = [
  {
    kicker: "KAPRODI SISTEKIN 2026", inisial: "SW",
    nama: "Syahroni Wahyu Iriananda, S.Kom., M.T.",
    sub: "Kaprodi SISTEKIN 2026 · M.T. Universitas Brawijaya (2018)",
    fokusLabel: "FOKUS BIDANG PENELITIAN — GOOGLE SCHOLAR",
    chips: [{ t: "Data Science" }, { t: "Artificial Intelligence" }, { t: "Machine Learning" }, { t: "NLP" }, { t: "Information Retrieval" }],
    sorotan: ["Gamifikasi: Konsep dan Penerapan (JOINTECS 2020) — ", "214 sitasi, salah satu karya paling disitasi di lingkungan FSTI."],
    stats: [["511", "Sitasi Scholar"], ["7", "h-index"], ["259792", "SINTA ID"]],
  },
  {
    kicker: "DOSEN HOMEBASE SISTEKIN", inisial: "RP",
    nama: "Rangga Pahlevi Putra, S.Pd., M.T.",
    sub: "Dosen Homebase · Lektor · M.T. Universitas Brawijaya (2018)",
    fokusLabel: "FOKUS BIDANG PENELITIAN — GOOGLE SCHOLAR",
    chips: [{ t: "Image Processing" }, { t: "Biometric System" }, { t: "Digital Marketing" }, { t: "Informatics" }],
    sorotan: ["Identifikasi anggrek dengan Tapis Gabor & M-SVM — ", "akurasi 95,4% (JOINTECS 2021); ekspansi ke deteksi deepfake wajah (2026)."],
    stats: [["74", "Sitasi Scholar"], ["5", "h-index"], ["6729051", "SINTA ID"]],
  },
  {
    kicker: "DOSEN HOMEBASE SISTEKIN", inisial: "IA",
    nama: "Ismail Akbar, S.Kom., M.Kom.",
    sub: "Dosen Homebase · M.Kom. UIN Maulana Malik Ibrahim Malang (2023)",
    fokusLabel: "FOKUS BIDANG PENELITIAN — GOOGLE SCHOLAR",
    chips: [{ t: "Natural Language Processing" }, { t: "Text Classification" }, { t: "Deep Learning" }, { t: "Machine Learning" }],
    sorotan: ["Deteksi depresi & kecemasan pengguna Twitter dengan BiLSTM — ", "29 sitasi, karya terdisitasi tertinggi (2021)."],
    stats: [["123", "Sitasi Scholar"], ["6", "h-index"], ["6973267", "SINTA ID"]],
  },
  {
    kicker: "DOSEN HOMEBASE SISTEKIN", inisial: "AN",
    nama: "Affi Nizar Suksmawati, S.Kom., M.Cs.",
    sub: "Dosen Homebase · M.Cs. Universitas Gadjah Mada (2022)",
    fokusLabel: "FOKUS BIDANG PENELITIAN — GOOGLE SCHOLAR + DIREKTORI FSTI",
    chips: [{ t: "Machine Learning" }, { t: "Expert System", sec: 1 }, { t: "Fuzzy Logic", sec: 1 }, { t: "Health Informatics", sec: 1 }],
    catatan: "Chip oranye = interest profil Google Scholar; chip ungu = bidang keahlian direktori FSTI.",
    sorotan: ["Mamdani Fuzzy Expert System untuk diagnosis penyakit infeksius — ", "Jurnal RESTI (SINTA 2); hilirisasi HKI DBXs & ELREST."],
    stats: [["82", "Sitasi Scholar"], ["5", "h-index"], ["6", "Dokumen Scopus"]],
  },
  {
    kicker: "DOSEN HOMEBASE SISTEKIN", inisial: "DS",
    nama: "Devi Septiani, S.Kom., M.Kom.",
    sub: "Dosen Homebase · S3 (tugas belajar) ITS · M.Kom. Universitas Brawijaya (2023)",
    fokusLabel: "BIDANG KEAHLIAN — DIREKTORI FSTI",
    chips: [{ t: "Manajemen Sistem Informasi", sec: 1 }, { t: "VR & AR", sec: 1 }, { t: "Multimedia 3D", sec: 1 }],
    catatan: "Profil Google Scholar & SINTA belum terbentuk — publikasi dipetakan seiring pembentukan prodi (2025/2026).",
    sorotan: ["Agenda riset: media imersif VR/AR untuk edukasi & promosi — ", "serta visualisasi 3D interaktif dan evaluasi UX sistem informasi."],
    stats: [["2026", "Dosen baru"], ["S3", "Tugas belajar ITS"], ["S2", "M.SI. UB 2023"]],
  },
  {
    kicker: "DOSEN HOMEBASE SISTEKIN", inisial: "MS",
    nama: "Mamba'us Sa'adah, S.ST., M.T.",
    sub: "Dosen Homebase · M.T. Teknik Elektro ITS (2019) · D4 PENS (2015)",
    fokusLabel: "FOKUS BIDANG PENELITIAN — GOOGLE SCHOLAR + DIREKTORI FSTI",
    chips: [{ t: "Audio Signal Processing" }, { t: "Multimedia", sec: 1 }, { t: "Pengolahan Sinyal", sec: 1 }],
    catatan: "Chip oranye = interest profil Google Scholar; chip ungu = bidang keahlian direktori FSTI.",
    sorotan: ["Noise cancellation sinyal gamelan dengan filter adaptif LMS — ", "tesis M.T. ITS (2019); riset terkini: suara pernapasan untuk AI diagnostik."],
    stats: [["14", "Sitasi Scholar"], ["3", "h-index"], ["7", "Publikasi Scholar"]],
  },
];

summarySlide(7, summaries[0]);

profilSlide(8, {
  kicker: "KAPRODI SISTEKIN 2026",
  nama: "Syahroni Wahyu Iriananda, S.Kom., M.T.",
  fokus: "Data Science · Artificial Intelligence · Machine Learning · NLP · Information Retrieval · Text Mining",
  sitasi: "511", sinta: "259792", extra: "h-index 7 · Rekam jejak tertinggi di FSTI",
  penelitian: "Rekam jejak terkuat di klaster Data Science & NLP: text mining, ensemble learning, dan deep learning untuk problem riil — diagnosis diabetes, deteksi outlier kredit, klasifikasi penyakit tanaman, analisis sentimen, hingga information retrieval dokumen pengaduan.",
  pubs: [
    "Gamifikasi: Konsep dan Penerapan (JOINTECS 2020 — 214 sitasi)",
    "Integrating SMOTE-Tomek & Fusion Learning with XGBoost Meta-Learner — Diabetes Recognition (2024)",
    "Outlier Detection using GMM Clustering to Optimize XGBoost for Credit Approval (2024)",
    "Analyzing InceptionV3 & InceptionResNetV2 — Rice Leaf Disease Classification (2024)",
    "Optimasi Klasifikasi Sentimen Komentar Game Bergerak — SVM, Grid Search, N-Gram (2024)",
  ],
  pengabdian: "Digitalisasi UMKM, pemberdayaan guru PAUD, dan transfer teknologi ke peternakan serta industri rumahan — dari pendampingan kemasan & pemasaran digital hingga inovasi mesin produksi berbasis IoT.",
  pkm: [
    "Inovasi Mesin Tempering Cokelat Berbasis IoT — UKM Tithiek Tenger (2024)",
    "Pelatihan Pengembangan Kompetensi Guru KB-TA Amanah Bunda Lawang (2023)",
    "Implementasi Sinici Kudo Apps — Peternakan Kelinci Peci P'Rama, Tulungagung (2022)",
    "Diversifikasi Produk & Inovasi Kemasan — Usaha Daun Rempah Catering (2021)",
    "Inovasi Kemasan & Pemasaran Digital UMKM Tisya Herbal, Desa Mulyoarjo (2020)",
  ],
});

summarySlide(9, summaries[1]);

profilSlide(10, {
  kicker: "DOSEN HOMEBASE SISTEKIN",
  nama: "Rangga Pahlevi Putra, S.Pd., M.T.",
  fokus: "Image Processing · Biometric System · Digital Marketing · Computer Vision · IoT",
  sitasi: "74", sinta: "6729051", extra: "h-index 5 · Lektor · M.T. UB 2018",
  penelitian: "Pengolahan citra digital & computer vision: tekstur Gabor + M-SVM (identifikasi anggrek akurasi 95,4%), klasifikasi kanker prostat dari citra MRI, deteksi kerusakan permukaan jalan, hingga deteksi deepfake wajah berbasis YOLOv9+CNN (2026). Kontributor paper Scopus Q2 pemilihan pemasok industri pangan halal (metode ANP).",
  pubs: [
    "Identifikasi Jenis Tanaman Anggrek — Tapis Gabor & M-SVM (JOINTECS 2021)",
    "Deteksi Deepfake pada Citra Biometrik Wajah — YOLOv9 & CNN (CIASTECH 2026)",
    "Klasifikasi Kanker Prostat melalui Citra MRI — Pengolahan Citra Digital (2024)",
    "Identification of Road Surface Defects using Multiclass SVM (2023)",
    "Supplier Selection for Halal Instant Food Industry: A Case Study Using ANP (EEJET 2024)",
  ],
  pengabdian: "Digitalisasi UMKM & pertanian kota: pemasaran digital produk herbal, aplikasi mobile urban farming Balearjosari, HKI Teknologi IoT Urban Farming Alam Lestari, serta sistem informasi keuangan PAUD. Penerima hibah PkM LLDIKTI.",
  pkm: [
    "Aplikasi Mobile Pemasaran & Penjualan Urban Farming — Kel. Balearjosari, Malang (2023)",
    "Teknologi IoT Urban Farming Alam Lestari (2023)",
    "Sistem Informasi Keuangan PAUD IT Putera Zaman, Kota Malang (2023)",
    "Inovasi Kemasan & Pemasaran Digital UMKM Tisya Herbal, Desa Mulyoarjo (2020)",
  ],
});

summarySlide(11, summaries[2]);

profilSlide(12, {
  kicker: "DOSEN HOMEBASE SISTEKIN",
  nama: "Ismail Akbar, S.Kom., M.Kom.",
  fokus: "Learning-Augmented Optimization · Text Mining · Artificial Intelligence · NLP · Deep Learning",
  sitasi: "123", sinta: "6973267", extra: "h-index 6 · M.Kom. UIN Malang 2023",
  penelitian: "Text mining, deep learning & learning-augmented optimization: klasifikasi multi-label terjemahan Al-Qur'an Indonesia (Bi-LSTM, CNN+FastText), deteksi depresi & kecemasan pengguna Twitter, sistem pakar kesehatan (Certainty Factor & Fuzzy) terintegrasi rekam medis dan e-learning, hingga speech emotion recognition.",
  pubs: [
    "Deteksi Depresi & Kecemasan Pengguna Twitter — BiLSTM (2021 · 29 sitasi)",
    "Multi-label Classification of Indonesian Al-Qur'an Translation — CNN, BiLSTM, FastText (Techno.Com 2024)",
    "Perbandingan Analisis Sentimen PLN Mobile — ML vs Deep Learning (JOINTECS 2024)",
    "Penerapan CNN — Deteksi Kualitas Telur Berdasarkan Warna Cangkang (2024)",
    "Expert System Integrated with Medical Record — Certainty Factor (IEEE CyberneticsCom 2022)",
  ],
  pengabdian: "Transfer teknologi ke masyarakat: implementasi & pelatihan aplikasi Sinici Kudo untuk peternakan kelinci Peci P'Rama (Tulungagung), HKI sistem pakar e-learning berinferensi fuzzy, serta digitalisasi UMKM (POS, branding & digital marketing).",
  pkm: [
    "Strategi Digital Marketing — Kemandirian Ekonomi Pengrajin Selop Manten (J. SOLMA 2024)",
    "Implementasi Sistem POS & Transformasi Digital UMKM Baba Brewok (2026)",
    "Optimalisasi Branding & Digital Marketing UMKM (2026)",
    "Implementasi Sinici Kudo Apps — Peternakan Kelinci Peci P'Rama (2022)",
  ],
});

summarySlide(13, summaries[3]);

profilSlide(14, {
  kicker: "DOSEN HOMEBASE SISTEKIN",
  nama: "Affi Nizar Suksmawati, S.Kom., M.Cs.",
  fokus: "Machine Learning · Expert System · Fuzzy Logic · CBR · Health Informatics",
  sitasi: "82", sinta: "6937019", extra: "Scopus: 6 dokumen · M.Cs. UGM 2022",
  penelitian: "Sistem pakar, fuzzy logic & machine learning untuk domain kesehatan: Mamdani Fuzzy Expert System diagnosis penyakit infeksius (J. RESTI — SINTA 2), perbandingan CBR vs Dempster-Shafer, serta machine learning sebagai inference engine untuk diagnosis DBD & faringitis (IEEE). Karya terdisitasi: deteksi depresi Twitter berbasis Bi-LSTM.",
  pubs: [
    "Mamdani Fuzzy Expert System for Online Learning — Infectious Diseases (J. RESTI 2022)",
    "Perbandingan Metode CBR dan Dempster-Shafer — Sistem Pakar Layanan Kesehatan (J. RESTI 2021)",
    "Comparison of ML as Inference Engine — Dengue Disease (JOIV 2025 · Q2)",
    "Investigation of ML as Inference Engine — Pharyngitis (IEEE ISRITI 2024)",
    "Expert System Integrated with Medical Record — Certainty Factor (IEEE 2022)",
  ],
  pengabdian: "Hilirisasi riset ke produk HKI (DBXs — diagnosis DBD berbasis ML; ELREST) dan pemberdayaan UMKM minuman herbal melalui inovasi QR Code edukatif, teknologi produksi, serta pendampingan sertifikasi halal. Editor buku referensi inovasi teknologi pendukung SDGs.",
  pkm: [
    "Inovasi QR Code Edukatif & Teknologi Produksi UMKM Minuman Herbal (PROPENMAS 2025 — ketua)",
    "Penguatan Kapasitas UMKM Minuman Herbal — Sertifikasi Halal & Diversifikasi Produk (2026)",
    "Pemberdayaan Budidaya Cacing ANC — Website Sistem Informasi & Digital Marketing (2025)",
  ],
});

summarySlide(15, summaries[4]);

profilSlide(16, {
  kicker: "DOSEN HOMEBASE SISTEKIN",
  nama: "Devi Septiani, S.Kom., M.Kom.",
  fokus: "Manajemen Sistem Informasi · Virtual Reality · Augmented Reality · Multimedia 3D · UX",
  sitasi: "—", sinta: "—", extra: "Dosen baru 2026 · S3 (tugas belajar) ITS",
  penelitian: "Homebase keilmuan Manajemen Sistem Informasi, VR & AR, serta Multimedia 3D. Agenda riset SISTEKIN yang diampu: perancangan sistem informasi manajemen berbasis pengguna, pengembangan media imersif (VR/AR) untuk edukasi dan promosi, visualisasi 3D interaktif, serta evaluasi UX sistem informasi organisasi. Publikasi terindeks SINTA/Scholar sedang dipetakan seiring pembentukan prodi baru.",
  pubs: [
    "Agenda Riset: Perancangan Manajemen Sistem Informasi Berorientasi Pengguna (2026)",
    "Agenda Riset: Integrasi VR & AR pada Media Pembelajaran dan Promosi (2026)",
    "Agenda Riset: Multimedia 3D & Visualisasi Interaktif untuk Sistem Informasi (2026)",
  ],
  pengabdian: "Literasi digital, digitalisasi layanan organisasi, dan pemanfaatan media imersif untuk UMKM serta institusi pendidikan: pelatihan perancangan sistem informasi, prototipe AR untuk katalog produk, dan pendampingan konten multimedia 3D sebagai media komunikasi publik.",
  pkm: [
    "Pendampingan Digitalisasi Sistem Informasi untuk Institusi Pendidikan & UMKM (2026)",
    "Pelatihan Media AR/VR dan Multimedia 3D — Sarana Promosi Produk Lokal (2026)",
  ],
});

summarySlide(17, summaries[5]);

profilSlide(18, {
  kicker: "DOSEN HOMEBASE SISTEKIN",
  nama: "Mamba'us Sa'adah, S.ST., M.T.",
  fokus: "Multimedia · Audio Signal Processing · Adaptive Filter · Digital Signal Processing",
  sitasi: "14", sinta: "—", extra: "h-index 3 · M.T. Teknik Elektro ITS 2019",
  penelitian: "Pengolahan sinyal audio & multimedia: filter adaptif Least Mean Square (LMS) dan Recursive Least Square (RLS) untuk noise cancellation sinyal gamelan, deteksi instrumen identik, serta pengurangan noise RTL-SDR siaran radio FM (J. RESTI 2020 — SINTA 2). Riset terkini merambah klasifikasi suara pernapasan berbasis deep learning untuk AI diagnostik.",
  pubs: [
    "Noise Cancellation in Gamelan Signal — LMS Based Adaptive Filter (IJSST 2018)",
    "Noise Reduction in RTL-SDR using LMS & RLS (J. RESTI 2020)",
    "Identical Instruments Detection — LMS Based Adaptive Filter (J. Physics Conf. Series 2019)",
    "Feature Engineering & Deep Learning in Respiratory Sound Classification — SLR (JOINTECS 2025)",
    "Philosophical Ontology of Signal & Information (JSAE 2026)",
  ],
  pengabdian: "Hilirisasi keahlian audio/multimedia: peningkatan kualitas siaran komunitas, analisis QoS layanan digital masyarakat, dan pendampingan UMKM melalui analitik transaksi (Apriori). Potensi lanjutan: restorasi audio tradisional gamelan & sistem multimedia edukatif.",
  pkm: [
    "Kajian Etik Pengumpulan Dataset Suara Pernapasan untuk Model AI Diagnostik (2025)",
    "Analisis Transaksi Penjualan UMKM menggunakan Algoritma Apriori (2025)",
  ],
});

p.writeFile({ fileName: "PRESENTASI_PERKENALAN_SISTEKIN_BINUS_BDSRC.pptx" }).then(f => console.log("OK", f));
