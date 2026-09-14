# -*- coding: utf-8 -*-
"""Batch MD -> print-ready HTML -> PDF (proper tables + images).
Writes HTML to HTML/ and PDF to PDF/ using headless Chrome.
"""
import os
import re
import glob
import html as ihtml
import subprocess
import sys

WORKDIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(WORKDIR, "HTML")
PDF_DIR = os.path.join(WORKDIR, "PDF")
os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

import markdown

PRINT_CSS = """
@page { size: A4; margin: 15mm 12mm 16mm 12mm; }
* { box-sizing: border-box; }
body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; line-height: 1.5; color: #1a1a1a; margin: 0; }
h1 { font-size: 18pt; color: #1F3864; border-bottom: 3px solid #2E75B6; padding-bottom: 6px; page-break-after: avoid; }
h2 { font-size: 14pt; color: #1F3864; border-bottom: 1px solid #BDD7EE; padding-bottom: 4px; page-break-after: avoid; margin-top: 18px; }
h3 { font-size: 11.5pt; color: #2E75B6; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
code { font-family: 'Consolas', 'Fira Code', monospace; font-size: 8.5pt; background: #f2f5f9; padding: 1px 4px; border-radius: 3px; word-break: break-word; }
pre { background: #f2f5f9; border: 1px solid #d3d3d3; border-radius: 6px; padding: 10px 12px; white-space: pre-wrap; word-break: break-word; page-break-inside: avoid; }
pre code { background: transparent; padding: 0; }
blockquote { border-left: 4px solid #2E75B6; background: #eef4fb; margin: 12px 0; padding: 8px 14px; border-radius: 0 6px 6px 0; page-break-inside: avoid; }
img { max-width: 100%; height: auto; display: block; margin: 10px auto; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 10px 0 14px 0; font-size: 8.2pt; line-height: 1.4; page-break-inside: auto; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th { background: #1F3864; color: #ffffff; font-weight: 700; text-align: left; }
th, td { border: 1px solid #8a8a8a; padding: 4px 5px; vertical-align: top; word-break: break-word; }
tbody tr:nth-child(even) td { background: #f2f5f9; }
.table-wrapper { width: 100%; overflow: visible; }
.cover { text-align: center; margin: 0 0 18px 0; padding: 18px; background: #1F3864; color: #fff; border-radius: 10px; }
.cover h1 { color: #fff; border: none; margin: 0; }
.cover p { color: #dce8f7; margin: 4px 0 0 0; }
.footer-note { margin-top: 22px; font-size: 8pt; color: #595959; border-top: 1px solid #ccc; padding-top: 8px; }
"""

HTML_SHELL = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="cover"><h1>{title}</h1><p>Program Studi Sistem dan Teknologi Informasi (S1) — FSTI Universitas Widyagama Malang — Kurikulum OBE 2026</p></div>
{content}
<div class="footer-note">Dokumen PDF dihasilkan otomatis dari Markdown sumber ({src}). Tabel dan gambar diformat print-ready A4. Tim Pengembang Kurikulum FSTI UWG — 2026.</div>
</body>
</html>
"""

def find_chrome():
    cands = [
        r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        r"C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
        r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    ]
    for c in cands:
        if os.path.exists(c):
            return c
    return None

def md_to_html(md_text, title, src):
    md_text = md_text.replace("$\\leftrightarrow$", "\u2194").replace("\\leftrightarrow", "\u2194")
    md_text = md_text.replace("$\\rightarrow$", "\u2192").replace("\\rightarrow", "\u2192")
    md = markdown.Markdown(extensions=["extra", "tables", "fenced_code", "toc", "sane_lists"])
    content = md.convert(md_text)
    content = re.sub(r"<table>", '<div class="table-wrapper"><table>', content)
    content = re.sub(r"</table>", "</table></div>", content)
    safe_title = ihtml.escape(title)
    return HTML_SHELL.format(title=safe_title, css=PRINT_CSS, content=content, src=ihtml.escape(src))

def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    if only:
        md_files = [os.path.join(WORKDIR, f) if not os.path.isabs(f) else f for f in only]
    else:
        md_files = sorted(glob.glob(os.path.join(WORKDIR, "*.md")))
        md_files = [f for f in md_files if not os.path.basename(f).startswith("_tmp")]
    print(f"[INFO] {len(md_files)} markdown ditemukan.")
    chrome = find_chrome()
    if not chrome:
        print("[ERROR] Chrome/Edge tidak ditemukan.")
        sys.exit(1)
    print(f"[INFO] Browser: {chrome}")
    ok_html = 0
    ok_pdf = 0
    for idx, md_path in enumerate(md_files, 1):
        base = os.path.splitext(os.path.basename(md_path))[0]
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()
        except Exception as e:
            print(f"[{idx}/{len(md_files)}] {base}: GAGAL baca ({e})")
            continue
        title = base.replace("_", " ")
        m = re.search(r"^#\s+(.+)$", md_text, re.M)
        if m:
            title = m.group(1).strip()[:140]
        html_str = md_to_html(md_text, title, os.path.basename(md_path))
        html_path = os.path.join(HTML_DIR, base + ".html")
        pdf_path = os.path.join(PDF_DIR, base + ".pdf")
        try:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_str)
            ok_html += 1
        except Exception as e:
            print(f"[{idx}/{len(md_files)}] {base}: GAGAL tulis HTML ({e})")
            continue
        url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
               "--run-all-compositor-stages-before-draw", "--virtual-time-budget=4000",
               f"--print-to-pdf={os.path.abspath(pdf_path)}", url]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if res.returncode == 0 and os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
                ok_pdf += 1
                print(f"[{idx}/{len(md_files)}] {base}: OK html={os.path.getsize(html_path):,}B pdf={os.path.getsize(pdf_path):,}B")
            else:
                print(f"[{idx}/{len(md_files)}] {base}: GAGAL pdf err={res.stderr[:300]}")
        except Exception as e:
            print(f"[{idx}/{len(md_files)}] {base}: ERROR pdf ({e})")
    print(f"[SELESAI] HTML {ok_html}/{len(md_files)}, PDF {ok_pdf}/{len(md_files)}")

if __name__ == "__main__":
    main()

