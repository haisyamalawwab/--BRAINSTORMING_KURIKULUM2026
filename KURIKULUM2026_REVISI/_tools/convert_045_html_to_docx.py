# -*- coding: utf-8 -*-
"""
Converter Khusus: 045 HTML to DOCX (Replika Template Master KPT FSTI)
Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG

Membaca: KURIKULUM2026_REVISI/HTML/045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.html
Menghasilkan: KURIKULUM2026_REVISI/DOCX/045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.docx
"""

import os
import re
import html
from html.parser import HTMLParser
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(BASE, "HTML", "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.html")
DOCX_DIR = os.path.join(BASE, "DOCX")
PRIMARY_DOCX = os.path.join(DOCX_DIR, "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.docx")
FALLBACK_DOCX = os.path.join(DOCX_DIR, "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX_FROM_HTML.docx")

# Palet Warna Master KPT FSTI
COLOR_NAVY = RGBColor(36, 64, 97)        # #244061
COLOR_BLUE = RGBColor(46, 117, 182)      # #2E75B6
COLOR_TEXT = RGBColor(38, 38, 38)        # #262626
COLOR_GRAY = RGBColor(128, 128, 128)     # #808080
COLOR_UPPS = RGBColor(180, 83, 9)        # Amber #B45309
COLOR_TERISI = RGBColor(71, 85, 105)     # Slate #475569

HEX_NAVY = "244061"
HEX_LIGHT_BLUE = "F2F5F9"
HEX_BORDER = "C0C8D0"
HEX_QUOTE_BG = "EEF4FB"
HEX_COVER_IDENT = "D9E1F2"
HEX_FIG_BG = "F8FAFC"

def set_cell_background(cell, fill_hex):
    """Menyetel warna latar belakang cell tabel."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=100, right=100):
    """Menyetel margin dalam cell tabel (dxa)."""
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

def set_table_borders(table, color="B0B8C0", sz="4", val="single"):
    """Menyetel garis batas tabel yang rapi dan tipis."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def clean_inline_html(text):
    """Membersihkan entitas HTML dasar."""
    text = html.unescape(text)
    return text.replace('\xa0', ' ').strip()

def render_inline_runs(p, html_text, base_font_size=10.5, is_italic=False, default_color=COLOR_TEXT):
    """Memecah token tag inline (strong, em, code, kpt-tag) ke dalam runs docx secara rekursif dan rapi."""
    html_text = re.sub(r'<br\s*/?>', '\n', html_text)
    html_text = re.sub(r'<a\s+[^>]*>(.*?)</a>', r'\1', html_text, flags=re.DOTALL | re.I)
    
    pattern = r'(<span class="kpt-tag[^"]*">.*?</span>|<strong>.*?</strong>|<b>.*?</b>|<em>.*?</em>|<i>.*?</i>|<code>.*?</code>)'
    tokens = re.split(pattern, html_text, flags=re.DOTALL | re.I)
    
    for token in tokens:
        if not token:
            continue
            
        # 1. KPT-TAG
        if 'class="kpt-tag' in token.lower():
            is_upps = 'upps' in token.lower()
            inner_txt = clean_inline_html(re.sub(r'<[^>]+>', '', token))
            if inner_txt:
                run = p.add_run(f" [{inner_txt}] ")
                run.font.name = 'Calibri'
                run.font.size = Pt(base_font_size * 0.9)
                run.font.bold = True
                run.font.color.rgb = COLOR_UPPS if is_upps else COLOR_TERISI
            continue
            
        # 2. CODE
        if token.lower().startswith('<code>') and token.lower().endswith('</code>'):
            inner_txt = clean_inline_html(token[6:-7])
            if inner_txt:
                run = p.add_run(inner_txt)
                run.font.name = 'Consolas'
                run.font.size = Pt(base_font_size - 0.5)
                run.font.color.rgb = RGBColor(160, 40, 40)
            continue
            
        # 3. STRONG / B
        if (token.lower().startswith('<strong>') and token.lower().endswith('</strong>')) or \
           (token.lower().startswith('<b>') and token.lower().endswith('</b>')):
            inner = token[8:-9] if token.lower().startswith('<strong>') else token[3:-4]
            if '<span' in inner.lower():
                render_inline_runs(p, inner, base_font_size=base_font_size, is_italic=is_italic, default_color=default_color)
            else:
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
            
        # 4. EM / I
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
            
        # 5. REGULAR TEXT
        clean_txt = clean_inline_html(re.sub(r'<[^>]+>', '', token))
        if clean_txt:
            run = p.add_run(clean_txt)
            run.font.name = 'Calibri'
            run.font.size = Pt(base_font_size)
            run.font.color.rgb = default_color
            if is_italic:
                run.font.italic = True

def build_docx_from_html(html_file):
    print("=====================================================================")
    print("  KONVERSI 045 HTML KE MICROSOFT WORD (.DOCX) — SISTEKIN 2026")
    print(f"  Sumber: {os.path.basename(html_file)}")
    print("=====================================================================")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        full_html = f.read()

    # Ambil isi kpt-page
    m_body = re.search(r'<div class="kpt-page">(.*?)</div>\s*</div>\s*</body>', full_html, re.DOTALL)
    if not m_body:
        # Fallback cari body
        m_body = re.search(r'<body>(.*?)</body>', full_html, re.DOTALL)
        body_html = m_body.group(1) if m_body else full_html
    else:
        body_html = m_body.group(1)

    doc = Document()
    
    # -------------------------------------------------------------
    # 1. Konfigurasi Halaman & Section (A4 Portrait, Margin KPT)
    # -------------------------------------------------------------
    section1 = doc.sections[0]
    section1.orientation = WD_ORIENT.PORTRAIT
    section1.page_width = Mm(210)
    section1.page_height = Mm(297)
    section1.top_margin = Mm(25)
    section1.bottom_margin = Mm(20)
    section1.left_margin = Mm(25)
    section1.right_margin = Mm(20)
    
    # Unlink cover header & footer
    section1.header.is_linked_to_previous = False
    section1.footer.is_linked_to_previous = False

    # Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = COLOR_TEXT

    # -------------------------------------------------------------
    # 2. Proses Bagian Halaman Sampul (Cover)
    # -------------------------------------------------------------
    m_cover = re.search(r'<div class="kpt-cover">(.*?)</div>', body_html, re.DOTALL)
    if m_cover:
        cover_content = m_cover.group(1)
        
        # Space top
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(24)
        
        p1 = doc.add_paragraph()
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run("TEMPLATE MASTER\n")
        r1.font.name = 'Calibri'
        r1.font.size = Pt(18)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_NAVY
        
        r2 = p1.add_run("DOKUMEN KURIKULUM PENDIDIKAN TINGGI\n")
        r2.font.name = 'Calibri'
        r2.font.size = Pt(16)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_NAVY
        
        p2 = doc.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(18)
        r3 = p2.add_run("FAKULTAS SAINS, TEKNOLOGI, DAN INFORMATIKA\nUNIVERSITAS WIDYA GAMA MALANG")
        r3.font.name = 'Calibri'
        r3.font.size = Pt(13)
        r3.font.bold = True
        r3.font.color.rgb = RGBColor(50, 50, 50)
        
        # Tabel Cover Identitas
        m_cover_table = re.search(r'<table class="cover-ident">(.*?)</table>', cover_content, re.DOTALL)
        if m_cover_table:
            c_rows = re.findall(r'<tr>(.*?)</tr>', m_cover_table.group(1), re.DOTALL)
            tbl_c = doc.add_table(rows=len(c_rows), cols=2)
            tbl_c.alignment = WD_TABLE_ALIGNMENT.CENTER
            set_table_borders(tbl_c, color=HEX_NAVY, sz="6")
            
            for r_idx, r_html in enumerate(c_rows):
                tds = re.findall(r'<td>(.*?)</td>', r_html, re.DOTALL)
                if len(tds) >= 2:
                    cell0 = tbl_c.cell(r_idx, 0)
                    cell1 = tbl_c.cell(r_idx, 1)
                    
                    cell0.width = Inches(2.2)
                    cell1.width = Inches(4.2)
                    
                    set_cell_background(cell0, HEX_COVER_IDENT)
                    set_cell_margins(cell0, top=100, bottom=100, left=120, right=100)
                    set_cell_margins(cell1, top=100, bottom=100, left=120, right=100)
                    
                    p0 = cell0.paragraphs[0]
                    p0.paragraph_format.space_before = Pt(1)
                    p0.paragraph_format.space_after = Pt(1)
                    r_c0 = p0.add_run(clean_inline_html(tds[0]))
                    r_c0.font.bold = True
                    r_c0.font.color.rgb = COLOR_NAVY
                    
                    p1 = cell1.paragraphs[0]
                    p1.paragraph_format.space_before = Pt(1)
                    p1.paragraph_format.space_after = Pt(1)
                    p1.add_run(clean_inline_html(tds[1]))
                    
        p_fac = doc.add_paragraph()
        p_fac.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_fac.paragraph_format.space_before = Pt(40)
        p_fac.paragraph_format.space_after = Pt(12)
        r_f = p_fac.add_run("FAKULTAS SAINS, TEKNOLOGI, DAN INFORMATIKA\nUNIVERSITAS WIDYA GAMA MALANG\n2026")
        r_f.font.name = 'Calibri'
        r_f.font.size = Pt(12)
        r_f.font.bold = True
        r_f.font.color.rgb = COLOR_NAVY
        
        # Section break / Page break setelah sampul
        doc.add_page_break()
        
    # Setup Running Header & Footer untuk Halaman Isi (Section 2 atau section 1 setelah cover)
    body_section = doc.sections[0]
    header = body_section.header
    p_hdr = header.paragraphs[0]
    p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_hdr = p_hdr.add_run("Template Master KPT FSTI - Universitas Widya Gama Malang")
    r_hdr.font.name = 'Calibri'
    r_hdr.font.size = Pt(8.5)
    r_hdr.font.italic = True
    r_hdr.font.color.rgb = COLOR_GRAY
    
    footer = body_section.footer
    p_ftr = footer.paragraphs[0]
    p_ftr.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_ftr = p_ftr.add_run("Buku Kurikulum KPT-OBE SISTEKIN 2026  |  FSTI Universitas Widyagama Malang")
    r_ftr.font.name = 'Calibri'
    r_ftr.font.size = Pt(8.5)
    r_ftr.font.color.rgb = COLOR_GRAY

    # Potong isi setelah cover
    content_after_cover = body_html[m_cover.end():] if m_cover else body_html
    
    # -------------------------------------------------------------
    # 3. Tokenisasi Elemen Blok Dokumen
    # -------------------------------------------------------------
    # Pola mendeteksi: H1, H2, H3, table-wrap/table, kpt-quote, kpt-fig, kpt-cap, hr, ul, ol, p
    block_pattern = re.compile(
        r'(<h1[^>]*>.*?</h1>|'
        r'<h2[^>]*>.*?</h2>|'
        r'<h3[^>]*>.*?</h3>|'
        r'<div class="kpt-quote">.*?</div>|'
        r'<figure class="kpt-fig".*?</figure>|'
        r'<div class="table-wrap">.*?</table>\s*</div>|'
        r'<table.*?>.*?</table>|'
        r'<div class="kpt-cap"[^>]*>.*?</div>|'
        r'<ul[^>]*>.*?</ul>|'
        r'<ol[^>]*>.*?</ol>|'
        r'<hr/?>|'
        r'<p[^>]*>.*?</p>)',
        re.DOTALL | re.IGNORECASE
    )
    
    blocks = block_pattern.findall(content_after_cover)
    print(f"  -> Terdeteksi {len(blocks)} blok elemen dokumen utama...")
    
    bab_counter = 0
    
    for b in blocks:
        b_clean = b.strip()
        if not b_clean:
            continue
            
        # 1. BAB (H1)
        if re.match(r'^<h1', b_clean, re.I):
            bab_counter += 1
            if bab_counter > 1:
                # Setiap bab baru mulai di halaman baru
                doc.add_page_break()
                
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(18)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            
            inner = re.sub(r'^<h1[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</h1>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=13, default_color=COLOR_NAVY)
            p.runs[0].font.bold = True
            continue
            
        # 2. SUB-BAB (H2)
        if re.match(r'^<h2', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            
            inner = re.sub(r'^<h2[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</h2>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=12, default_color=COLOR_NAVY)
            if p.runs:
                p.runs[0].font.bold = True
            continue
            
        # 3. SUB-SUB-BAB (H3)
        if re.match(r'^<h3', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            
            inner = re.sub(r'^<h3[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</h3>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=11, default_color=COLOR_BLUE)
            if p.runs:
                p.runs[0].font.bold = True
            continue
            
        # 4. CAPTION TABEL
        if re.match(r'^<div class="kpt-cap"', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            
            inner = re.sub(r'^<div class="kpt-cap"[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</div>$', '', inner, flags=re.I)
            render_inline_runs(p, inner, base_font_size=10, default_color=COLOR_NAVY)
            if p.runs:
                p.runs[0].font.bold = True
            continue
            
        # 5. CALLOUT / QUOTE
        if 'class="kpt-quote"' in b_clean:
            inner = re.sub(r'^<div class="kpt-quote"[^>]*>', '', b_clean, flags=re.I)
            inner = re.sub(r'</div>$', '', inner, flags=re.I)
            inner_ps = re.findall(r'<p[^>]*>(.*?)</p>', inner, re.DOTALL | re.I)
            if not inner_ps:
                inner_ps = [inner]
                
            tbl_q = doc.add_table(rows=1, cols=1)
            tbl_q.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl_q.autofit = False
            c_q = tbl_q.cell(0, 0)
            c_q.width = Inches(6.5)
            set_cell_background(c_q, HEX_QUOTE_BG)
            set_cell_margins(c_q, top=100, bottom=100, left=180, right=140)
            
            # Thick left border
            tcPr = c_q._tc.get_or_add_tcPr()
            borders = parse_xml(
                f'<w:tcBorders {nsdecls("w")}>'
                f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_NAVY}"/>'
                f'<w:top w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/>'
                f'</w:tcBorders>'
            )
            tcPr.append(borders)
            
            for p_idx, p_text in enumerate(inner_ps):
                pq = c_q.paragraphs[0] if p_idx == 0 else c_q.add_paragraph()
                pq.paragraph_format.space_before = Pt(2)
                pq.paragraph_format.space_after = Pt(2)
                pq.paragraph_format.line_spacing = 1.15
                render_inline_runs(pq, p_text, base_font_size=9.5, is_italic=True, default_color=COLOR_NAVY)
                
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
            continue
            
        # 6. FIGURE
        if re.match(r'^<figure class="kpt-fig"', b_clean, re.I):
            tbl_f = doc.add_table(rows=1, cols=1)
            tbl_f.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl_f.autofit = False
            cf = tbl_f.cell(0, 0)
            cf.width = Inches(6.5)
            set_cell_background(cf, HEX_FIG_BG)
            set_cell_margins(cf, top=100, bottom=100, left=150, right=150)
            set_table_borders(tbl_f, color="94A3B8", sz="4")
            
            # Title
            m_ft = re.search(r'<div class="fig-title">(.*?)</div>', b_clean, re.DOTALL)
            pf = cf.paragraphs[0]
            pf.paragraph_format.space_before = Pt(2)
            pf.paragraph_format.space_after = Pt(2)
            if m_ft:
                render_inline_runs(pf, m_ft.group(1), base_font_size=10, default_color=COLOR_NAVY)
                if pf.runs:
                    pf.runs[0].font.bold = True
                    
            # Desc
            m_fd = re.search(r'<div class="fig-desc">(.*?)</div>', b_clean, re.DOTALL)
            if m_fd:
                pfd = cf.add_paragraph()
                pfd.paragraph_format.space_before = Pt(1)
                pfd.paragraph_format.space_after = Pt(2)
                render_inline_runs(pfd, m_fd.group(1), base_font_size=9.5)
                
            # Pre
            m_pre = re.search(r'<pre[^>]*>(.*?)</pre>', b_clean, re.DOTALL)
            if m_pre:
                p_pre = cf.add_paragraph()
                p_pre.paragraph_format.space_before = Pt(2)
                p_pre.paragraph_format.space_after = Pt(2)
                r_pre = p_pre.add_run(clean_inline_html(m_pre.group(1)))
                r_pre.font.name = 'Consolas'
                r_pre.font.size = Pt(8)
                r_pre.font.color.rgb = RGBColor(40, 40, 40)
                
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
            continue
            
        # 7. TABEL
        if '<table' in b_clean:
            # Ambil thead & tbody
            m_th = re.search(r'<thead.*?>(.*?)</thead>', b_clean, re.DOTALL | re.I)
            m_tb = re.search(r'<tbody.*?>(.*?)</tbody>', b_clean, re.DOTALL | re.I)
            
            head_rows = re.findall(r'<tr.*?>(.*?)</tr>', m_th.group(1), re.DOTALL | re.I) if m_th else []
            body_rows = re.findall(r'<tr.*?>(.*?)</tr>', m_tb.group(1), re.DOTALL | re.I) if m_tb else []
            
            all_rows = head_rows + body_rows
            if not all_rows:
                continue
                
            # Hitung kolom
            cols_sample = re.findall(r'<t[hd].*?>(.*?)</t[hd]>', all_rows[0], re.DOTALL | re.I)
            n_cols = len(cols_sample)
            n_rows = len(all_rows)
            
            if n_cols == 0:
                continue
                
            tbl = doc.add_table(rows=n_rows, cols=n_cols)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl.autofit = True
            set_table_borders(tbl, color=HEX_BORDER, sz="4")
            
            # Repeat Header
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
                    cell_text = cells_html[c_idx] if c_idx < len(cells_html) else ""
                    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    
                    if is_header:
                        set_cell_background(cell, HEX_NAVY)
                        set_cell_margins(cell, top=100, bottom=100, left=90, right=90)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.space_before = Pt(1)
                        p.paragraph_format.space_after = Pt(1)
                        p.paragraph_format.line_spacing = 1.05
                        
                        clean_th = re.sub(r'</?[a-z]+.*?>', '', cell_text).strip()
                        r = p.add_run(clean_th)
                        r.font.name = 'Calibri'
                        r.font.size = Pt(8.5 if n_cols > 7 else 9.5)
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(255, 255, 255)
                    else:
                        if (r_idx - len(head_rows)) % 2 == 1:
                            set_cell_background(cell, HEX_LIGHT_BLUE)
                        else:
                            set_cell_background(cell, "FFFFFF")
                            
                        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.space_before = Pt(1)
                        p.paragraph_format.space_after = Pt(1)
                        p.paragraph_format.line_spacing = 1.05
                        
                        font_sz = 8.0 if n_cols > 8 else (8.5 if n_cols > 5 else 9.5)
                        render_inline_runs(p, cell_text, base_font_size=font_sz)
                        
            p_after = doc.add_paragraph()
            p_after.paragraph_format.space_after = Pt(5)
            continue
            
        # 8. LIST (UL / OL)
        if re.match(r'^<(ul|ol)', b_clean, re.I):
            is_ordered = b_clean.startswith('<ol')
            lis = re.findall(r'<li[^>]*>(.*?)</li>', b_clean, re.DOTALL | re.I)
            style_name = 'List Number' if is_ordered else 'List Bullet'
            
            for li_text in lis:
                p = doc.add_paragraph(style=style_name)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.15
                render_inline_runs(p, li_text, base_font_size=10)
            continue
            
        # 9. HORIZONTAL RULE
        if re.match(r'^<hr', b_clean, re.I):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run("—" * 75)
            r.font.color.rgb = RGBColor(200, 210, 225)
            r.font.size = Pt(7)
            continue
            
        # 10. REGULAR PARAGRAPH
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

    # -------------------------------------------------------------
    # 4. Simpan Dokumen secara Aman (Bebas Kunci Word)
    # -------------------------------------------------------------
    candidates = [
        PRIMARY_DOCX,
        FALLBACK_DOCX,
        os.path.join(DOCX_DIR, "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX_V2.docx"),
        os.path.join(DOCX_DIR, "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX_LATEST.docx")
    ]
    
    saved_path = None
    for c in candidates:
        try:
            doc.save(c)
            print(f"\n[SUKSES] Dokumen berhasil disimpan di:\n  {c} ({os.path.getsize(c):,} bytes)")
            saved_path = c
            break
        except PermissionError:
            print(f"  [INFO] File {os.path.basename(c)} sedang dibuka di MS Word, mencoba alternatif...")
            
    if not saved_path:
        import time
        ts_path = os.path.join(DOCX_DIR, f"045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX_{int(time.time())}.docx")
        doc.save(ts_path)
        print(f"\n[SUKSES] Dokumen berhasil disimpan di:\n  {ts_path} ({os.path.getsize(ts_path):,} bytes)")
        saved_path = ts_path
        
    return saved_path

if __name__ == '__main__':
    build_docx_from_html(HTML_PATH)
