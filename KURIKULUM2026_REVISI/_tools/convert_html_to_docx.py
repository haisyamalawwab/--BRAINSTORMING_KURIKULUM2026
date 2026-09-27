# -*- coding: utf-8 -*-
"""
HTML to DOCX Converter Engine — Standar Template KPT FSTI (A4 Portrait)
Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG
Mengonversi dokumen HTML portal menjadi Microsoft Word (.docx) dengan tata letak
rapi, formal, terstandarisasi A4 Portrait dan tabel proporsional.
"""

import os
import re
import sys
import glob
import html
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT_DIR)
HTML_DIR = os.path.join(WORKDIR, "HTML")
DOCX_DIR = os.path.join(WORKDIR, "DOCX")

# Palet Warna FSTI KPT
COLOR_PRIMARY_NAVY = RGBColor(31, 78, 121)    # #1F4E79
COLOR_SECONDARY_BLUE = RGBColor(46, 117, 182) # #2E75B6
COLOR_DARK_TEXT = RGBColor(38, 38, 38)        # #262626
COLOR_MUTED_GRAY = RGBColor(128, 128, 128)    # #808080
COLOR_CODE_RED = RGBColor(160, 40, 40)

HEX_PRIMARY_NAVY = "1F4E79"
HEX_LIGHT_ROW = "F9FAFC"
HEX_BORDER = "C0C8D0"
HEX_CALLOUT_BG = "EEF4FB"
HEX_CODE_BG = "F4F6F9"

PRINTABLE_WIDTH_IN = 6.30

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=90, right=90):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="C0C8D0", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def clean_inline_html(text):
    text = html.unescape(text)
    return text.replace('\xa0', ' ').strip()

def render_inline_runs(p, html_text, base_font_size=10.5, is_italic=False, default_color=COLOR_DARK_TEXT):
    html_text = re.sub(r'<br\s*/?>', '\n', html_text)
    html_text = re.sub(r'<a\s+[^>]*>(.*?)</a>', r'\1', html_text, flags=re.DOTALL | re.I)
    
    pattern = r'(<strong>.*?</strong>|<b>.*?</b>|<em>.*?</em>|<i>.*?</i>|<code>.*?</code>|<span[^>]*>.*?</span>)'
    tokens = re.split(pattern, html_text, flags=re.DOTALL | re.I)
    
    for token in tokens:
        if not token:
            continue
            
        # CODE
        if token.lower().startswith('<code>') and token.lower().endswith('</code>'):
            inner_txt = clean_inline_html(token[6:-7])
            if inner_txt:
                run = p.add_run(inner_txt)
                run.font.name = 'Consolas'
                run.font.size = Pt(base_font_size - 0.5)
                run.font.color.rgb = COLOR_CODE_RED
            continue
            
        # STRONG / B
        if (token.lower().startswith('<strong>') and token.lower().endswith('</strong>')) or \
           (token.lower().startswith('<b>') and token.lower().endswith('</b>')):
            inner = token[8:-9] if token.lower().startswith('<strong>') else token[3:-4]
            inner_txt = clean_inline_html(re.sub(r'<[^>]+>', '', inner))
            if inner_txt:
                run = p.add_run(inner_txt)
                run.font.name = 'Calibri'
                run.font.size = Pt(base_font_size)
                run.font.bold = True
                run.font.color.rgb = default_color
                if is_italic:
                    run.font.italic = True
            continue
            
        # EM / I
        if (token.lower().startswith('<em>') and token.lower().endswith('</em>')) or \
           (token.lower().startswith('<i>') and token.lower().endswith('</i>')):
            inner = token[4:-5] if token.lower().startswith('<em>') else token[3:-4]
            inner_txt = clean_inline_html(re.sub(r'<[^>]+>', '', inner))
            if inner_txt:
                run = p.add_run(inner_txt)
                run.font.name = 'Calibri'
                run.font.size = Pt(base_font_size)
                run.font.italic = True
                run.font.color.rgb = default_color
            continue
            
        # SPAN
        if token.lower().startswith('<span') and token.lower().endswith('</span>'):
            inner_txt = clean_inline_html(re.sub(r'<[^>]+>', '', token))
            if inner_txt:
                run = p.add_run(inner_txt)
                run.font.name = 'Calibri'
                run.font.size = Pt(base_font_size)
                run.font.color.rgb = default_color
            continue
            
        # REGULAR TEXT
        clean_txt = clean_inline_html(re.sub(r'<[^>]+>', '', token))
        if clean_txt:
            run = p.add_run(clean_txt)
            run.font.name = 'Calibri'
            run.font.size = Pt(base_font_size)
            run.font.color.rgb = default_color
            if is_italic:
                run.font.italic = True

def compute_col_widths_from_cells(rows_cells, total_width_in=PRINTABLE_WIDTH_IN):
    n_cols = max(len(r) for r in rows_cells) if rows_cells else 0
    if n_cols == 0:
        return []
    max_lens = []
    for c in range(n_cols):
        lens = [len(r[c]) if c < len(r) else 0 for r in rows_cells]
        max_lens.append(max(lens) if lens else 1)
    weights = [max(float(l)**0.65, 2.5) for l in max_lens]
    total_w = sum(weights)
    return [(w / total_w) * total_width_in for w in weights]

def convert_html_file_to_docx(html_path, docx_path):
    print(f"  -> Mengonversi: {os.path.basename(html_path)} -> {os.path.basename(docx_path)}")
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ekstrak judul dokumen dari <title> atau <h1>
    m_title = re.search(r'<title>(.*?)</title>', content, re.I)
    doc_title = m_title.group(1).split('|')[0].strip() if m_title else "Dokumen Kurikulum SISTEKIN 2026"

    # Ekstrak bagian konten utama (<main class="content">...</main>)
    m_main = re.search(r'<main[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</main>', content, re.DOTALL | re.I)
    if not m_main:
        m_main = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL | re.I)
    if not m_main:
        m_main = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL | re.I)
    if not m_main:
        m_main = re.search(r'<div class="container">(.*?)</div>\s*</body>', content, re.DOTALL | re.I)
    
    body_html = m_main.group(1) if m_main else content

    doc = Document()

    # Section A4 Portrait
    section = doc.sections[0]
    section.orientation = WD_ORIENT.PORTRAIT
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(25)
    section.bottom_margin = Mm(20)
    section.left_margin = Mm(25)
    section.right_margin = Mm(20)

    # Header & Footer
    hdr = section.header
    p_hdr = hdr.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_hdr = p_hdr.add_run("FSTI — Universitas Widyagama Malang  |  Kurikulum SISTEKIN 2026")
    r_hdr.font.name = 'Calibri'
    r_hdr.font.size = Pt(8.5)
    r_hdr.font.italic = True
    r_hdr.font.color.rgb = COLOR_MUTED_GRAY

    ftr = section.footer
    p_ftr = ftr.paragraphs[0]
    p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_ftr = p_ftr.add_run(doc_title[:65])
    r_ftr.font.name = 'Calibri'
    r_ftr.font.size = Pt(8.5)
    r_ftr.font.color.rgb = COLOR_MUTED_GRAY

    # Tokenisasi elemen blok
    block_pattern = re.compile(
        r'(<h1[^>]*>.*?</h1>|'
        r'<h2[^>]*>.*?</h2>|'
        r'<h3[^>]*>.*?</h3>|'
        r'<h4[^>]*>.*?</h4>|'
        r'<div[^>]*class="[^"]*alert[^"]*"[^>]*>.*?</div>|'
        r'<pre[^>]*><code[^>]*>.*?</code></pre>|'
        r'<pre[^>]*>.*?</pre>|'
        r'<div[^>]*class="[^"]*table-container[^"]*"[^>]*>.*?</table>\s*</div>|'
        r'<table.*?>.*?</table>|'
        r'<ul[^>]*>.*?</ul>|'
        r'<ol[^>]*>.*?</ol>|'
        r'<blockquote[^>]*>.*?</blockquote>|'
        r'<hr/?>|'
        r'<p[^>]*>.*?</p>)',
        re.DOTALL | re.IGNORECASE
    )

    blocks = block_pattern.findall(body_html)

    for b in blocks:
        b_clean = b.strip()
        if not b_clean:
            continue

        # 1. H1
        if re.match(r'^<h1', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            inner = re.sub(r'^<h1[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</h1>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=14, default_color=COLOR_PRIMARY_NAVY)
            if p.runs:
                p.runs[0].font.bold = True
            continue

        # 2. H2
        if re.match(r'^<h2', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            inner = re.sub(r'^<h2[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</h2>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=12, default_color=COLOR_PRIMARY_NAVY)
            if p.runs:
                p.runs[0].font.bold = True
            continue

        # 3. H3
        if re.match(r'^<h3', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            inner = re.sub(r'^<h3[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</h3>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=11, default_color=COLOR_SECONDARY_BLUE)
            if p.runs:
                p.runs[0].font.bold = True
            continue

        # 4. H4
        if re.match(r'^<h4', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            inner = re.sub(r'^<h4[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</h4>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=10.5, default_color=COLOR_DARK_TEXT)
            if p.runs:
                p.runs[0].font.bold = True
            continue

        # 5. ALERT / CALLOUT
        if 'class="alert' in b_clean:
            inner = re.sub(r'^<div[^>]*class="[^"]*alert[^"]*"[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</div>$', '', inner, flags=re.I)
            inner_ps = re.findall(r'<p[^>]*>(.*?)</p>', inner, re.DOTALL | re.I)
            if not inner_ps:
                inner_ps = [inner]

            tbl_a = doc.add_table(rows=1, cols=1)
            tbl_a.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl_a.autofit = False
            cell_a = tbl_a.cell(0, 0)
            cell_a.width = Inches(PRINTABLE_WIDTH_IN)
            set_cell_background(cell_a, HEX_CALLOUT_BG)
            set_cell_margins(cell_a, top=80, bottom=80, left=140, right=100)

            tcPr = cell_a._tc.get_or_add_tcPr()
            borders = parse_xml(
                f'<w:tcBorders {nsdecls("w")}>'
                f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_PRIMARY_NAVY}"/>'
                f'<w:top w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/>'
                f'</w:tcBorders>'
            )
            tcPr.append(borders)

            for idx_p, p_text in enumerate(inner_ps):
                pa = cell_a.paragraphs[0] if idx_p == 0 else cell_a.add_paragraph()
                pa.paragraph_format.space_before = Pt(1)
                pa.paragraph_format.space_after = Pt(1)
                pa.paragraph_format.line_spacing = 1.15
                render_inline_runs(pa, p_text, base_font_size=9.5, is_italic=True, default_color=COLOR_PRIMARY_NAVY)

            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            continue

        # 6. CODE BLOCK
        if '<pre' in b_clean:
            m_code = re.search(r'<code[^>]*>(.*?)</code>', b_clean, re.DOTALL | re.I)
            code_text = m_code.group(1) if m_code else re.sub(r'</?pre[^>]*>', '', b_clean)
            clean_code = clean_inline_html(code_text)

            tbl_c = doc.add_table(rows=1, cols=1)
            tbl_c.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl_c.autofit = False
            cell_c = tbl_c.cell(0, 0)
            cell_c.width = Inches(PRINTABLE_WIDTH_IN)
            set_cell_background(cell_c, HEX_CODE_BG)
            set_cell_margins(cell_c, top=70, bottom=70, left=90, right=90)
            set_table_borders(tbl_c, color="CBD5E1", sz="4")

            p_code = cell_c.paragraphs[0]
            p_code.paragraph_format.space_before = Pt(0)
            p_code.paragraph_format.space_after = Pt(0)
            r_c = p_code.add_run(clean_code)
            r_c.font.name = 'Consolas'
            r_c.font.size = Pt(8.5)
            r_c.font.color.rgb = RGBColor(30, 41, 59)

            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            continue

        # 7. TABLE
        if '<table' in b_clean:
            m_th = re.search(r'<thead.*?>(.*?)</thead>', b_clean, re.DOTALL | re.I)
            m_tb = re.search(r'<tbody.*?>(.*?)</tbody>', b_clean, re.DOTALL | re.I)

            head_rows = re.findall(r'<tr.*?>(.*?)</tr>', m_th.group(1), re.DOTALL | re.I) if m_th else []
            body_rows = re.findall(r'<tr.*?>(.*?)</tr>', m_tb.group(1), re.DOTALL | re.I) if m_tb else []

            if not head_rows and not body_rows:
                # Direct tr
                all_rows = re.findall(r'<tr.*?>(.*?)</tr>', b_clean, re.DOTALL | re.I)
            else:
                all_rows = head_rows + body_rows

            if not all_rows:
                continue

            # Parse all cells
            rows_data = []
            for r_h in all_rows:
                c_matches = re.findall(r'<t[hd].*?>(.*?)</t[hd]>', r_h, re.DOTALL | re.I)
                clean_cells = [clean_inline_html(re.sub(r'<[^>]+>', '', c)) for c in c_matches]
                rows_data.append(clean_cells)

            n_cols = max(len(r) for r in rows_data) if rows_data else 0
            n_rows = len(rows_data)

            if n_cols == 0 or n_rows == 0:
                continue

            tbl = doc.add_table(rows=n_rows, cols=n_cols)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl.autofit = False
            set_table_borders(tbl, color=HEX_BORDER, sz="4")

            col_widths = compute_col_widths_from_cells(rows_data, total_width_in=PRINTABLE_WIDTH_IN)

            if len(head_rows) > 0:
                trPr = tbl.rows[0]._tr.get_or_add_trPr()
                trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

            for r_idx, row_html in enumerate(all_rows):
                row = tbl.rows[r_idx]
                r_trPr = row._tr.get_or_add_trPr()
                r_trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

                is_header = (r_idx < len(head_rows))
                cells_html = re.findall(r'<t[hd].*?>(.*?)</t[hd]>', row_html, re.DOTALL | re.I)

                for c_idx in range(n_cols):
                    cell = row.cells[c_idx]
                    cell_html = cells_html[c_idx] if c_idx < len(cells_html) else ""
                    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

                    if c_idx < len(col_widths):
                        cell.width = Inches(col_widths[c_idx])

                    if is_header:
                        set_cell_background(cell, HEX_PRIMARY_NAVY)
                        set_cell_margins(cell, top=80, bottom=80, left=70, right=70)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.paragraph_format.space_before = Pt(1)
                        p.paragraph_format.space_after = Pt(1)
                        render_inline_runs(p, cell_html, base_font_size=9.5, default_color=RGBColor(255, 255, 255))
                        if p.runs:
                            p.runs[0].font.bold = True
                    else:
                        bg_color = HEX_LIGHT_ROW if r_idx % 2 == 1 else "FFFFFF"
                        set_cell_background(cell, bg_color)
                        set_cell_margins(cell, top=60, bottom=60, left=70, right=70)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.space_before = Pt(0)
                        p.paragraph_format.space_after = Pt(1)
                        render_inline_runs(p, cell_html, base_font_size=9.0)

            doc.add_paragraph().paragraph_format.space_after = Pt(3)
            continue

        # 8. LIST (UL / OL)
        if re.match(r'^<(ul|ol)', b_clean, re.I):
            is_ol = b_clean.lower().startswith('<ol')
            lis = re.findall(r'<li[^>]*>(.*?)</li>', b_clean, re.DOTALL | re.I)
            style_name = 'List Number' if is_ol else 'List Bullet'
            for idx_li, li_text in enumerate(lis):
                p = doc.add_paragraph(style=style_name)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.line_spacing = 1.15
                render_inline_runs(p, li_text, base_font_size=10)
            continue

        # 9. HR
        if re.match(r'^<hr', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run("―" * 45)
            r.font.color.rgb = COLOR_MUTED_GRAY
            continue

        # 10. PARAGRAPH
        if re.match(r'^<p', b_clean, re.I):
            inner = re.sub(r'^<p[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</p>$', '', inner, flags=re.I).strip()
            if not inner:
                continue
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            render_inline_runs(p, inner, base_font_size=10.5)

    try:
        doc.save(docx_path)
        print(f"     [SUKSES] Tersimpan: {docx_path} ({os.path.getsize(docx_path):,} bytes)")
        return docx_path
    except PermissionError:
        alt = docx_path.replace('.docx', '_NEW.docx')
        doc.save(alt)
        print(f"     [PERINGATAN] Berkas sedang dikunci Word! Tersimpan di: {alt} ({os.path.getsize(alt):,} bytes)")
        return alt

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "052"
    os.makedirs(DOCX_DIR, exist_ok=True)
    
    print("=====================================================================")
    print("  HTML TO DOCX CONVERTER ENGINE — STANDAR TEMPLATE FSTI (A4 PORTRAIT)")
    print(f"  Direktori Sumber: {HTML_DIR}")
    print(f"  Direktori Keluaran: {DOCX_DIR}")
    print(f"  Kata Kunci Target: {target}")
    print("=====================================================================")

    pattern = os.path.join(HTML_DIR, f"*{target}*.html")
    matches = glob.glob(pattern)

    if not matches:
        print(f"[GAGAL] Tidak ditemukan berkas HTML dengan kata kunci '{target}' di {HTML_DIR}")
        return

    for html_file in matches:
        base_name = os.path.splitext(os.path.basename(html_file))[0]
        # Keluarkan nama docx yang sesuai
        docx_file = os.path.join(DOCX_DIR, f"{base_name}.docx")
        convert_html_file_to_docx(html_file, docx_file)

    print("\n[SELESAI] Konversi HTML ke DOCX tuntas!")

if __name__ == '__main__':
    main()
