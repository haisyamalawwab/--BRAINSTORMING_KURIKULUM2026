# -*- coding: utf-8 -*-
"""Builder 045 HTML Template Master KPT FSTI v3
Sumber: KURIKULUM2026_REVISI/045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md
Output: KURIKULUM2026_REVISI/HTML/045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.html
Gaya: replika resmi Template_KPT_2024.docx / PDF (A4, Calibri/Inter, navy #244061, header abu kanan, footer Halaman X).
Pembaruan v3:
  - Eliminasi artefak BOM & judul ganda setelah sampul.
  - Transformasi penuh 4 paragraf §7.4 (Kelompok MKWU, FSTI, Core STI, Elektif) menjadi 4 tabel formal lengkap (Tabel 7.4c s.d. 7.4f).
  - Penambahan anchor ID otomatis pada setiap Bab & Sub-bab serta link interaktif pada Daftar Isi.
  - Responsive table wrapper (overflow-x auto) & styling cetak A4 presisi.
"""

import re
import html as ihtml
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md")
DST = os.path.join(BASE, "HTML", "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.html")

CSS = """*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact;scroll-behavior:smooth}
body{font-family:Calibri,'Segoe UI',Inter,Arial,sans-serif;color:#262626;background:#8a8f98;margin:0;font-size:11pt;line-height:1.5}
a{color:#244061;text-decoration:none}
a:hover{text-decoration:underline}
.kpt-toolbar{max-width:210mm;margin:14px auto 0;padding:0 12px;display:flex;gap:10px;align-items:center;justify-content:space-between;font-size:10pt}
.kpt-toolbar a,.kpt-toolbar button{font-family:inherit;font-size:9.5pt;font-weight:600;padding:7px 14px;border:1px solid #cbd5e1;background:#fff;border-radius:6px;cursor:pointer;color:#244061;box-shadow:0 1px 3px rgba(0,0,0,.08);transition:all .15s}
.kpt-toolbar a:hover,.kpt-toolbar button:hover{background:#f1f5f9;border-color:#94a3b8}
.kpt-sheet{background:#fff;max-width:210mm;margin:12px auto 32px;box-shadow:0 4px 24px rgba(0,0,0,.22);border-radius:3px}
.kpt-page{padding:22mm 20mm 18mm 20mm}
.kpt-running{text-align:right;font-size:9pt;font-style:italic;color:#808080;margin:0 0 12pt 0;border-bottom:1px solid #e2e8f0;padding-bottom:4pt}
.kpt-cover{text-align:center;margin:24mm 0 10mm 0}
.kpt-cover .t1{font-size:18pt;font-weight:700;color:#244061;letter-spacing:.5px;margin:0}
.kpt-cover .t2{font-size:16pt;font-weight:700;color:#244061;margin:3pt 0 12pt 0}
.kpt-cover .t3{font-size:13pt;font-weight:700;color:#333;margin:0}
.kpt-cover .t4{font-size:13pt;font-weight:700;color:#333;margin:0 0 16pt 0}
.kpt-cover table{margin:0 auto;width:88%}
.kpt-cover .fac{margin-top:24mm;font-weight:700;font-size:12pt;line-height:1.6;color:#244061}
h1.bab{font-size:13pt;color:#244061;text-transform:uppercase;margin:22pt 0 6pt 0;line-height:1.35;page-break-after:avoid;border-bottom:1.5px solid #244061;padding-bottom:3pt;scroll-margin-top:14px}
h2.sub{font-size:12pt;color:#244061;margin:14pt 0 4pt 0;line-height:1.35;page-break-after:avoid;scroll-margin-top:14px}
h3.sub3{font-size:11pt;color:#2E75B6;margin:10pt 0 3pt 0;scroll-margin-top:14px}
p{margin:0 0 6pt 0;text-align:justify}
ul,ol{margin:4pt 0 8pt 0;padding-left:22px}
li{margin:0 0 3pt 0;text-align:justify}
hr{border:none;border-top:1px solid #b9c2cc;margin:14pt 0}
.table-wrap{overflow-x:auto;margin:8pt 0 12pt 0}
table{width:100%;border-collapse:collapse;font-size:9.5pt;line-height:1.4}
.kpt-cap{font-weight:700;font-size:10pt;color:#244061;text-align:left;margin:12pt 0 3pt 0;scroll-margin-top:14px}
th{background:#244061;color:#fff;text-align:left;padding:6px 8px;border:1px solid #244061;font-weight:700}
td{padding:5px 8px;border:1px solid #c0c8d0;vertical-align:top}
tbody tr:nth-child(even) td{background:#F2F5F9}
table.cover-ident td:first-child{background:#D9E1F2;font-weight:700;width:32%}
.kpt-quote{border-left:4px solid #244061;background:#EEF4FB;padding:8px 14px;margin:10pt 0;font-style:italic;color:#1F3864;font-size:10pt;border-radius:0 4px 4px 0}
.kpt-quote p{margin:0;text-align:left}
.kpt-tag{display:inline-block;font-size:8.5pt;font-weight:700;border:1px solid #94a3b8;color:#475569;border-radius:4px;padding:1px 6px;vertical-align:middle;letter-spacing:.3px;background:#f8fafc}
.kpt-tag.upps{border-color:#b45309;color:#92400e;background:#fef3c7}
.kpt-toc{list-style:none;padding:0;margin:8pt 0}
.kpt-toc li{font-size:10.5pt;margin:0 0 4pt 0;text-transform:uppercase}
.kpt-toc a{color:#244061;display:inline-block;padding:2pt 0}
.kpt-toc a:hover{color:#1d4ed8}
.kpt-fig{border:1px solid #94a3b8;background:#F8FAFC;margin:10pt 0;padding:10px 14px;page-break-inside:avoid;border-radius:4px}
.kpt-fig .fig-title{font-weight:700;color:#244061;font-size:10.5pt;margin:0 0 4pt 0}
.kpt-fig .fig-desc{font-size:10pt;margin:0 0 4pt 0;text-align:justify}
.kpt-fig details{font-size:9pt}
.kpt-fig summary{cursor:pointer;color:#244061;font-weight:700}
.kpt-fig pre{background:#0f172a;color:#dbeafe;font-size:8pt;overflow:auto;max-height:220px;padding:8px;white-space:pre-wrap;border-radius:3px}
pre.kpt-code{background:#F1F5F9;border:1px solid #cbd5e1;font-size:9pt;overflow:auto;padding:8px;white-space:pre-wrap;border-radius:3px}
.kpt-pagenum{text-align:center;font-size:9.5pt;margin:20pt 0 0 0;color:#808080;border-top:1px solid #e2e8f0;padding-top:6pt}
code{font-family:Consolas,monospace;font-size:9.5pt;color:#7a2828}
.sig{display:flex;gap:24px;margin:10pt 0} .sig>div{flex:1;text-align:center} .sig .nm{margin-top:26pt}
@page{size:A4;margin:25mm 20mm 20mm 20mm;@top-right{content:"Template Master KPT FSTI - Universitas Widya Gama Malang";font-family:Calibri,Arial,sans-serif;font-size:9pt;font-style:italic;color:#808080}@bottom-center{content:"Halaman " counter(page);font-family:Calibri,Arial,sans-serif;font-size:10pt;color:#000}}
@media print{.kpt-toolbar{display:none}body{background:#fff;margin:0}.kpt-sheet{box-shadow:none;max-width:none;margin:0;border-radius:0}.kpt-page{padding:0}thead{display:table-header-group}tr{page-break-inside:avoid}h1.bab,h2.sub{page-break-after:avoid}.kpt-fig{break-inside:avoid}.table-wrap{overflow:visible}}
"""

JENIS_KEYS = ["+Praktik", "+P", "Proyek", "Magang", "Mandiri", "Seminar", "Elektif", "Praktik", "Teori"]

def esc(s):
    return ihtml.escape(s, quote=False)

def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    s = s.replace("**", "")
    return s

def tag_status(s):
    def rep(m):
        inner = (m.group(2) or "").strip()
        cls = "kpt-tag upps" if "UPPS" in inner.upper() else "kpt-tag"
        return f'<span class="{cls}">{esc(inner)}</span>'
    return re.sub(r"\[(\*\*)?(TERISI[^]]*?|PERLU DATA UPPS[^]]*?|TERISI SEBAGIAN[^]]*?|KERANGKA[^]]*?)(\*\*)?\]", rep, s, flags=re.IGNORECASE)

def rich(s):
    s = tag_status(inline(s))
    s = s.replace("⭐⭐⭐", "★★★").replace("⭐⭐", "★★").replace("⭐", "★")
    return s

def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def parse_details(det):
    parts = [p.strip() for p in det.split(",")]
    m0 = re.search(r"(\d+)", parts[0])
    sks = int(m0.group(1)) if m0 else 0
    sem = ""
    ms = re.search(r"Sem\s*(\d)", det)
    if ms:
        sem = ms.group(1)
    jenis = "Teori"
    for k in JENIS_KEYS:
        if k in det:
            jenis = {"+Praktik": "+Praktik", "+P": "+P"}.get(k, k)
            break
    ket = ", ".join(parts[1:]).strip()
    ket = re.sub(r"^(prasyarat|syarat)\s+", "", ket, flags=re.I)
    return sks, sem, jenis, ket if ket else "—"

def parse_items(text):
    """Mengurai daftar MK berformat: KODE Nama (SKS, Sem, Jenis, Prasyarat); ..."""
    rows, notes = [], []
    jalur = ""
    text = re.sub(r"\)\.\s*(P[123]\s*[—–-])", r"); \1", text)
    text = re.sub(r"\)\.\s*(Mahasiswa menempuh)", r"); \1", text)
    for raw in [c.strip() for c in text.split(";") if c.strip()]:
        ch = raw.rstrip().rstrip(".")
        mj = re.match(r"^(P[123])\s*[—–-]\s*(.*)$", ch)
        if mj:
            jalur = mj.group(1)
            ch = mj.group(2).strip().rstrip(".")
        mc = re.search(r"([A-Z]{2,3}-\d{3})\s+([^()]+?)\s*\(([^)]+)\)\s*$", ch)
        if not mc:
            notes.append(ch)
            continue
        kode, nama, det = mc.group(1), mc.group(2).strip(), mc.group(3)
        sks, sem, jenis, ket = parse_details(det)
        rows.append((kode, nama, sks, sem, jenis, ket, jalur))
    return rows, notes

def jalur_name(j):
    return {"P1": "P1 — Integrated Smart Systems",
            "P2": "P2 — Cloud Infrastructure & Cybersecurity",
            "P3": "P3 — Digital Platform Engineering"}.get(j, j)

def build_table(caption, headers, rows, total_sks=None):
    o = [f"<div class=\"kpt-cap\">{esc(caption)}</div>", "<div class=\"table-wrap\"><table><thead><tr>"]
    o += [f"<th>{esc(h)}</th>" for h in headers]
    o += ["</tr></thead><tbody>"]
    last_j = None
    for r in rows:
        if len(r) == 7 and r[6] and r[6] != last_j:
            last_j = r[6]
            o.append(f"<tr><td colspan=\"{len(headers)}\" style=\"background:#d9e1f2;color:#1f3864;font-weight:700;\"><strong>{esc(jalur_name(last_j))}</strong></td></tr>")
        cells = r[:len(headers)]
        o.append("<tr>" + "".join(f"<td>{esc(str(c))}</td>" for c in cells) + "</tr>")
    if total_sks is not None:
        o.append(f"<tr style=\"background:#eef4fb;font-weight:700;\"><td></td><td><strong>Total</strong></td><td><strong>{total_sks} SKS</strong></td>"
                 + "<td></td>" * (len(headers) - 3) + "</tr>")
    o += ["</tbody></table></div>"]
    return "\n".join(o)

def md_table_to_html(lines, caption=None):
    rows = []
    for ln in lines:
        if re.match(r"^\s*\|[-| :]+\|\s*$", ln):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return ""
    ncols = max(len(r) for r in rows)
    out = []
    if caption:
        out.append(f"<div class=\"kpt-cap\">{esc(caption)}</div>")
    out.append("<div class=\"table-wrap\"><table><thead><tr>")
    for h in rows[0] + [""] * (ncols - len(rows[0])):
        out.append(f"<th>{rich(h)}</th>")
    out.append("</tr></thead><tbody>")
    for r in rows[1:]:
        r = r + [""] * (ncols - len(r))
        out.append("<tr>")
        for c in r:
            out.append(f"<td>{rich(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)

def simple_table(headers, rows, caption=None):
    out = []
    if caption:
        out.append(f"<div class=\"kpt-cap\">{esc(caption)}</div>")
    out.append("<div class=\"table-wrap\"><table><thead><tr>")
    for h in headers:
        out.append(f"<th>{esc(h)}</th>")
    out.append("</tr></thead><tbody>")
    for r in rows:
        out.append("<tr>")
        for c in r:
            out.append(f"<td>{rich(c)}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)

def convert(md_text):
    lines = md_text.splitlines()
    blocks = []
    i = 0
    buf_para = []
    def flush_para():
        if buf_para:
            t = " ".join(buf_para).strip()
            buf_para.clear()
            if t:
                blocks.append(("p", t))
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if s.startswith("```"):
            flush_para()
            lang = s[3:].strip()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            blocks.append(("mermaid" if lang == "mermaid" else "code", (lang, "\n".join(code))))
            continue
        if not s:
            flush_para(); i += 1; continue
        if s.startswith("|") and s.endswith("|"):
            flush_para()
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i].strip()); i += 1
            blocks.append(("table", tbl)); continue
        if s in ("---", "***", "___"):
            flush_para(); blocks.append(("hr", "")); i += 1; continue
        if s.startswith("# "):
            flush_para(); blocks.append(("h1", s[2:].strip())); i += 1; continue
        if s.startswith("## "):
            flush_para(); blocks.append(("h2", s[3:].strip())); i += 1; continue
        if s.startswith("### "):
            flush_para(); blocks.append(("h3", s[4:].strip())); i += 1; continue
        if s.startswith(">"):
            flush_para()
            q = []
            while i < len(lines) and (lines[i].strip().startswith(">") or lines[i].strip() == ""):
                if lines[i].strip().startswith(">"):
                    q.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
                if i < len(lines) and lines[i].strip() != "" and not lines[i].strip().startswith(">"):
                    break
            blocks.append(("quote", " ".join(q))); continue
        m = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m:
            flush_para()
            items = []
            while i < len(lines):
                m2 = re.match(r"^(\d+)\.\s+(.*)$", lines[i].strip())
                if not m2: break
                items.append(m2.group(2)); i += 1
            blocks.append(("ol", items)); continue
        if s.startswith(("* ", "- ", "+ ")):
            flush_para()
            items = []
            while i < len(lines) and lines[i].strip()[:2] in ("* ", "- ", "+ "):
                items.append(lines[i].strip()[2:]); i += 1
            blocks.append(("ul", items)); continue
        buf_para.append(s); i += 1
    flush_para()
    return blocks

def split_rubric_aspects(body):
    parts = re.findall(r"([^:;()]+?)\s+(\d+%)\s*\(([^)]+)\)", body)
    out = []
    for name, bobot, levels_raw in parts:
        levels = [lv.strip() for lv in levels_raw.split(";") if lv.strip()]
        while len(levels) < 4:
            levels.append("—")
        out.append((name.strip(), bobot, levels[:4]))
    return out

APP_E15 = ("Tabel 7.2a — Ringkasan kategori ekivalensi K2025 → K2026 (sumber Dok. 024)",
           ["Kategori", "Jumlah MK", "Perlakuan", "Keterangan"],
           [["E1 Penuh", "34 MK", "Alih nilai langsung", "Diakui penuh"],
            ["E2 Bersyarat", "11 MK", "Uji penyetaraan", "Diakui bersyarat"],
            ["E3 Gabungan", "8 MK", "Peleburan 4 klaster G-1 s.d. G-4", "Efisiensi −7 SKS"],
            ["E4 Pecah", "1 MK", "Dipecah menjadi beberapa MK", "Diakui per bagian"],
            ["E5 Tanpa Padanan", "2 MK", "Wajib tempuh baru", "STI-423, STI-638 — status dipertahankan (Dok. 026)"]])

APP_MKBARU = ("Tabel 7.3a — Lima MK wajib baru K2026 (sumber Dok. 004–005)",
              ["Kode MK", "Nama Mata Kuliah", "SKS", "Semester", "Peran"],
              [["STI-103", "Arsitektur dan Organisasi STI", "3", "1", "Menggantikan Logika Informatika lama; prasyarat berantai"],
               ["STI-204", "Matematika Diskrit dan Logika", "3", "2", "Terpadu proposisi & aljabar boolean"],
               ["STI-312", "Jaringan Komputer", "3", "3", "Fondasi IoT / Cloud / Security"],
               ["STI-418", "Dasar Keamanan Informasi", "2", "4", "Baseline keamanan siber"],
               ["STI-625", "Smart City & Pemerintahan Digital", "2", "6", "Sistem cerdas terapan"]])

APP_MBKM = ("Tabel 10.1a — Skema konversi MBKM per semester (sumber Dok. 006)",
            ["Semester", "Paket Konversi", "Setara SKS"],
            [["6", "Peminatan-2 + Peminatan-3 + STI-624 + STI-627 + STI-625 + STI-626 + FST-611 (Magang MSIB)", "20 SKS"],
             ["7", "Peminatan-4/5/6 + STI-728 + FST-610 + FST-612 + FST-613 (Magang / Studi Independen / Wirausaha)", "20 SKS"]])

def transform_para(val, h1, h2, h3):
    # 7.4 Paragraf Kelompok MK -> Transformasi ke Tabel Formal
    if "7.4" in h2 and val.startswith("Kelompok "):
        m_kel = re.match(r"^Kelompok\s+(MKWU|FSTI|Core STI|Elektif)\s*\((.*?)\):\s*(.*)$", val, re.DOTALL)
        if m_kel:
            kel = m_kel.group(1)
            body = m_kel.group(3)
            rows, notes = parse_items(body)
            if rows:
                heads = ["No", "Kode MK", "Mata Kuliah", "SKS", "Semester", "Jenis", "Prasyarat / Keterangan"]
                tot = sum(r[2] for r in rows)
                if kel == "Elektif":
                    numbered = [(i + 1, r[0], r[1], r[2], r[3], r[4], (r[6] + " | " + r[5]).strip(" |"), r[6]) for i, r in enumerate(rows)]
                    tbl = build_table("Tabel 7.4f — Kelompok Elektif / Peminatan (18 ditawarkan; ditempuh 6 MK / 18 SKS)",
                                      heads, numbered)
                else:
                    numbered = [(i + 1,) + r[:6] for i, r in enumerate(rows)]
                    cap = {"MKWU": "Tabel 7.4c — Kelompok Mata Kuliah Wajib Universitas (8 MK / 13 SKS)",
                           "FSTI": "Tabel 7.4d — Kelompok Mata Kuliah Wajib Fakultas (13 MK / 36 SKS)",
                           "Core STI": "Tabel 7.4e — Kelompok Mata Kuliah Inti Prodi (28 MK / 79 SKS)"}[kel]
                    tbl = build_table(cap, heads, numbered, total_sks=tot)
                note_html = "".join(f"<p>{esc(x)}</p>" for x in notes) if notes else ""
                return (tbl + note_html, None)

    # 10.5 rantai panah -> ol
    if "10.5" in h2 and "→" in val:
        steps = [s.strip() for s in val.split("→") if s.strip()]
        return ("<ol>" + "".join(f"<li>{rich(s)}</li>" for s in steps) + "</ol>", None)
    # Daftar Pustaka -> ol
    if "DAFTAR PUSTAKA" in h1 and re.match(r"^\d+\.\s", val):
        items = [s.strip() for s in re.split(r"(?=\d+\.\s)", val) if s.strip()]
        items = [re.sub(r"^\d+\.\s*", "", s) for s in items]
        return ("<ol>" + "".join(f"<li>{rich(s)}</li>" for s in items) + "</ol>", None)
    # 9.5 sampul RPS -> tabel 1 kolom
    if "9.5" in h2 and val.startswith("Sampul RPS wajib memuat:"):
        intro, _, rest = val.partition(":")
        comps = [c.strip().rstrip(".") for c in rest.split(";") if c.strip()]
        t = simple_table(["Komponen Sampul RPS"], [[c] for c in comps],
                         "Tabel 9.5a — Komponen sampul RPS (sumber Dok. 007)")
        return (f"<p>{rich(intro + ':')}</p>" + t, None)
    # 10.6 empat opsi TA -> tabel
    if "10.6" in h2 and "(1)" in val and "(4)" in val:
        pre, _, rest = val.partition("(1)")
        rest = "(1)" + rest
        items = [s.strip() for s in re.split(r";\s*(?=\(\d\))", rest) if s.strip()]
        rows = []
        for it in items:
            m = re.match(r"\((\d)\)\s*([^()]+)\(([^)]+)\)(.*)", it)
            if m:
                rows.append([f"Opsi {m.group(1)}", m.group(2).strip(), (m.group(3) + m.group(4)).strip(" ;")])
            else:
                rows.append([f"Opsi {len(rows)+1}", it, "—"])
        t = simple_table(["Opsi", "Bentuk Tugas Akhir", "Luaran & Kaitan PL/PEO"], rows,
                         "Tabel 10.6a — Empat opsi Tugas Akhir FST-714 (sumber Dok. 009)")
        return (f"<p>{rich(pre.strip())}</p>" + t, None)
    # 11.2 teknik penilaian -> tabel ranah
    if "11.2" in h2 and "Sikap:" in val:
        sents = [s.strip() for s in re.split(r"\.\s+", val) if s.strip()]
        rows = []
        for sn in sents:
            if ":" in sn:
                a, _, b = sn.partition(":")
                rows.append([a.strip(), b.strip().rstrip(".")])
        t = simple_table(["Ranah", "Teknik & Instrumen"], rows, "Tabel 11.2a — Teknik penilaian per ranah")
        return (t, None)
    # 11.3 rubrik 1-3 -> tabel aspek x level
    if "11.3" in h2 and re.match(r"Rubrik\s+[123]\b", val):
        title, _, body = val.partition(":")
        aspects = split_rubric_aspects(body)
        if aspects:
            rows = [[n, b] + lv for (n, b, lv) in aspects]
            t = simple_table(["Aspek", "Bobot", "Sangat Baik", "Baik", "Cukup", "Kurang"], rows,
                             f"Tabel — {title.strip()} (sumber Dok. 008 §4)")
            return (f"<p><strong>{rich(title.strip())}</strong></p>" + t, None)
    # skema baku 4 titik -> tabel
    if "11.3" in h2 and val.startswith("Skema baku 4 titik"):
        intro, _, rest = val.partition(":")
        items = [s.strip() for s in rest.split(";") if s.strip()]
        rows = []
        for it in items:
            if "(" in it:
                a, _, b = it.partition("(")
                rows.append([a.strip(), "(" + b.strip()])
            else:
                rows.append([it, "—"])
        t = simple_table(["Titik Asesmen (= 1 CPMK)", "Ketentuan"], rows, "Tabel 11.3a — Skema baku 4 titik asesmen (= 100%)")
        return (f"<p>{rich(intro.strip() + ':')}</p>" + t, None)
    # 12.2 manajemen prose -> list
    if "12.2" in h2 and val.startswith("Tabel Manajemen 7 kolom"):
        intro, _, rest = val.partition(":")
        items = [s.strip().rstrip(".") for s in rest.split(";") if s.strip()]
        lis = "".join(f"<li>{rich(s)}</li>" for s in items)
        return (f"<p>{rich(intro.strip() + ':')}</p><ul>{lis}</ul>", None)
    # generik: paragraf pemisah '·' >=2 -> list interaktif
    if val.count("·") >= 2 and len(val) > 40:
        upper = "HALAMAN SAMPUL" in val and "LAMPIRAN" in val
        parts = [p.strip() for p in val.split("·") if p.strip()]
        lis = []
        for p in parts:
            p_slug = slugify(p)
            if upper:
                lis.append(f'<li><a href="#{p_slug}">{rich(p)}</a></li>')
            else:
                lis.append(f'<li>{rich(p)}</li>')
        cls = "kpt-toc" if upper else ""
        return (f"<ul class=\"{cls}\">{''.join(lis)}</ul>", None)

    extra = None
    key = None
    if "Ground truth K2025 dari Laporan SIAKAD" in val:
        extra = simple_table(APP_E15[1], APP_E15[2], APP_E15[0]); key = "e15"
    elif "18 MK baru K2026 (5 wajib/14 SKS + 13 elektif)" in val and "## " not in val:
        extra = simple_table(APP_MKBARU[1], APP_MKBARU[2], APP_MKBARU[0]); key = "mkbaru"
    elif "Magang MSIB Sem 6 mengonversi" in val:
        extra = simple_table(APP_MBKM[1], APP_MBKM[2], APP_MBKM[0]); key = "mbkm"
    return (f"<p>{rich(val)}</p>", extra, key)

def split_table_74(lines):
    rows = []
    for ln in lines:
        if re.match(r"^\s*\|[-| :]+\|\s*$", ln):
            continue
        rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
    if not rows:
        return ""
    head, body = rows[0], rows[1:]
    real = [r for r in body if not (r and r[1].strip() == "—")]
    recap = [r for r in body if r and r[1].strip() == "—"]
    out = []
    if real:
        out.append(md_table_to_html(["| " + " | ".join(head) + " |",
                                     "|---|---|---|---|---|---|---|"] + ["| " + " | ".join(r) + " |" for r in real],
                                    "Tabel 7.4a — Contoh entri daftar MK (Semester 1, 8 MK; daftar 55 baris penuh lihat Dok. 005)"))
    if recap:
        rec_head = ["Uraian Semester", "Ringkasan Beban", "SKS", "Semester", "Sumber"]
        rec_rows = [[r[2], r[3], r[4], r[5] if len(r) > 5 else "", r[6] if len(r) > 6 else ""] for r in recap]
        out.append(simple_table(rec_head, rec_rows,
                                "Tabel 7.4b — Rekapitulasi beban per semester (ringkas; rinci §8.2–§8.3)"))
    return "\n".join(out)

def render_mermaid(code, caption, h1=""):
    nodes = set(re.findall(r"(\w+)\[", code))
    edges = len(re.findall(r"-->|-\.->|---", code))
    if "DAFTAR PUSTAKA" in h1:
        return (f"<figure class=\"kpt-fig\"><p class=\"fig-title\">Arsip — Draf diagram prasyarat (tidak termasuk naskah formal)</p>"
                f"<p class=\"fig-desc\">Blok diagram mentah peninggalan draf ({len(nodes)} simpul, {edges} relasi) dengan penamaan MK era lama; "
                f"diarsipkan di sini dan tidak menjadi bagian naskah buku. Acuan resmi: Gambar 8.1–8.2 dan Dok. 012.</p>"
                f"<details><summary>Kode sumber diagram (arsip, {len(code.splitlines())} baris)</summary>"
                f"<pre>{esc(code)}</pre></details></figure>")
    cap = caption if caption else "Diagram alir kurikulum"
    desc = (f"Diagram ini dimodelkan sebagai bagan alir prasyarat / progresi kurikulum "
            f"({len(nodes)} simpul, {edges} relasi). Pada dokumen cetak formal, bagan "
            f"ditampilkan sebagai gambar statis; versi interaktif (diperbesar, pencarian) tersedia pada portal HTML.")
    return (f"<figure class=\"kpt-fig\"><p class=\"fig-title\">{rich(cap)}</p>"
            f"<p class=\"fig-desc\">{desc} Rujukan penuh: Dok. 005 (struktur), Dok. 012 (tree prasyarat).</p>"
            f"<details><summary>Kode sumber diagram (arsip, {len(code.splitlines())} baris)</summary>"
            f"<pre>{esc(code)}</pre></details></figure>")

def render(blocks):
    out = []
    last_h1, last_h2, last_h3 = "", "", ""
    done_extra = set()
    for kind, val in blocks:
        if kind == "h1":
            last_h1 = val
            s_id = slugify(val)
            out.append(f"<h1 class=\"bab\" id=\"{s_id}\">{rich(val)}</h1>")
        elif kind == "h2":
            last_h2 = val
            s_id = slugify(val)
            out.append(f"<h2 class=\"sub\" id=\"{s_id}\">{rich(val)}</h2>")
        elif kind == "h3":
            last_h3 = val
            s_id = slugify(val)
            out.append(f"<h3 class=\"sub3\" id=\"{s_id}\">{rich(val)}</h3>")
        elif kind == "p":
            res = transform_para(val, last_h1, last_h2, last_h3)
            html_p, extra = res[0], res[1]
            key = res[2] if len(res) > 2 else None
            out.append(html_p)
            if extra and key not in done_extra:
                out.append(extra)
                done_extra.add(key)
        elif kind == "ul":
            out.append("<ul>" + "".join(f"<li>{rich(x)}</li>" for x in val) + "</ul>")
        elif kind == "ol":
            out.append("<ol>" + "".join(f"<li>{rich(x)}</li>" for x in val) + "</ol>")
        elif kind == "quote":
            out.append(f"<div class=\"kpt-quote\"><p>{rich(val)}</p></div>")
        elif kind == "table":
            if "7.4" in last_h2 and "Daftar Mata Kuliah" in last_h2:
                out.append(split_table_74(val))
            else:
                out.append(md_table_to_html(val))
        elif kind == "hr":
            out.append("<hr/>")
        elif kind == "mermaid":
            out.append(render_mermaid(val[1], last_h3 or last_h2, last_h1))
        elif kind == "code":
            out.append(f"<pre class=\"kpt-code\">{esc(val[1])}</pre>")
    return "\n".join(out)

def build_045_html():
    with open(SRC, encoding="utf-8", errors="ignore") as f:
        md = f.read()
        
    # Bersihkan BOM dan baris judul duplikat cover
    md = md.lstrip('\ufeff').strip()
    md = re.sub(r"^#\s+DOKUMEN KURIKULUM PENDIDIKAN TINGGI.*?\n+", "", md, flags=re.IGNORECASE)
    md = re.sub(r"^\*\*Fakultas Sains.*?\n+", "", md, flags=re.IGNORECASE)
    md = re.sub(r"^\*\*Program Sarjana.*?\n+", "", md, flags=re.IGNORECASE)
    
    blocks = convert(md)
    content = render(blocks)
    
    cover = """<div class="kpt-cover" id="halaman-sampul">
<p class="t1">TEMPLATE MASTER</p>
<p class="t2">DOKUMEN KURIKULUM PENDIDIKAN TINGGI</p>
<p class="t3">FAKULTAS SAINS, TEKNOLOGI, DAN INFORMATIKA</p>
<p class="t4">UNIVERSITAS WIDYA GAMA MALANG</p>
<table class="cover-ident"><tbody>
<tr><td>Program Studi</td><td>Sistem dan Teknologi Informasi (SISTEKIN)</td></tr>
<tr><td>Jenjang</td><td>Sarjana (S1) — KKNI Level 6</td></tr>
<tr><td>Tahun Kurikulum</td><td>2026</td></tr>
<tr><td>Status Dokumen</td><td>Draf Buku KPT SISTEKIN 2026 Mengikuti Template Master KPT FSTI</td></tr>
</tbody></table>
<p class="fac">FAKULTAS SAINS, TEKNOLOGI, DAN INFORMATIKA<br/>UNIVERSITAS WIDYA GAMA MALANG<br/>2026</p>
</div>"""
    
    running = "Template Master KPT FSTI - Universitas Widya Gama Malang"
    
    html_doc = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>045 Draft Buku KPT SISTEKIN 2026 — Template Master KPT FSTI</title>
<style>{CSS}</style>
</head>
<body>
<div class="kpt-toolbar no-print">
  <a href="index.html">&#8592; Kembali ke Portal Kurikulum</a>
  <span><strong>Dokumen 045</strong> — Format Resmi Template Master KPT FSTI (A4 Siap Cetak / PDF)</span>
  <button onclick="window.print()">🖨️ Cetak / Simpan PDF</button>
</div>
<div class="kpt-sheet"><div class="kpt-page">
<p class="kpt-running">{running}</p>
{cover}
{content}
<p class="kpt-pagenum">Buku Kurikulum KPT-OBE SISTEKIN 2026 &bull; FSTI Universitas Widyagama Malang</p>
</div></div>
</body>
</html>"""

    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"[SUKSES] Berhasil men-generate: {DST} ({os.path.getsize(DST):,} bytes)")

if __name__ == "__main__":
    build_045_html()
