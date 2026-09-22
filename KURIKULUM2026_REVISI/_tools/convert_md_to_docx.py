# -*- coding: utf-8 -*-
"""
Markdown to DOCX Converter Engine — Standar Template KPT FSTI 2024 (A4 Portrait)
Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG
Mengonversi dokumen Markdown kurikulum menjadi dokumen Microsoft Word (.docx) 
berformat rapi, formal, terstandarisasi A4 Portrait sesuai Template_KPT_2024.docx.
"""

import os
import re
import sys
import glob
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT_DIR)
DOCX_DIR = os.path.join(WORKDIR, "DOCX")

# ==============================================================================
# PALET WARNA & TIPOGRAFI STANDAR TEMPLATE KPT FSTI 2024
# Mengikuti identitas visual resmi Template_KPT_2024.docx
# ==============================================================================
COLOR_PRIMARY_NAVY = RGBColor(31, 78, 121)      # #1F4E79 (FSTI Deep Navy Template 2024)
COLOR_SECONDARY_BLUE = RGBColor(46, 117, 182)   # #2E75B6 (Accent Blue)
COLOR_HEADING3 = RGBColor(47, 47, 47)           # #2F2F2F (Dark Charcoal Template 2024)
COLOR_DARK_TEXT = RGBColor(38, 38, 38)          # #262626 (Body Text)
COLOR_MUTED_GRAY = RGBColor(128, 128, 128)      # #808080 (Header/Footer/Muted)
COLOR_ALERT_RED = RGBColor(192, 0, 0)           # #C00000 (Penting/Warning)
COLOR_ALERT_GREEN = RGBColor(56, 87, 35)        # #385723 (Tips/Sukses)

HEX_PRIMARY_NAVY = "1F4E79"
HEX_LIGHT_ROW = "F9FAFC"
HEX_BORDER_GRAY = "C0C8D0"
HEX_CALLOUT_BG = "EEF4FB"

ALERT_CONFIG = {
    'IMPORTANT': {'color': 'C00000', 'bg': 'FFF5F5', 'title': '⚡ PENTING'},
    'WARNING':   {'color': 'ED7D31', 'bg': 'FFFBF5', 'title': '⚠️ PERINGATAN'},
    'CAUTION':   {'color': 'C00000', 'bg': 'FFF5F5', 'title': '🚨 PERHATIAN'},
    'TIP':       {'color': '385723', 'bg': 'F5FAF5', 'title': '💡 TIPS'},
    'NOTE':      {'color': '1F4E79', 'bg': 'EEF4FB', 'title': 'ℹ️ CATATAN'}
}

# Lebar area cetak A4 Portrait: 210mm - 50mm (margin kiri-kanan 25mm) = 160mm ≈ 6.30 inci
PRINTABLE_WIDTH_IN = 6.30

def set_cell_background(cell, fill_hex):
    """Menyetel warna latar belakang cell tabel."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=70, right=70):
    """Menyetel margin/padding dalam cell tabel (dalam dxa)."""
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
    """Menyetel border tabel tipis, halus dan rapi sesuai template formal."""
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

def compute_col_widths(rows_data, total_width_in=PRINTABLE_WIDTH_IN):
    """Menghitung lebar kolom proporsional agar seluruh tabel pas dalam batas A4 Portrait (6.30 inci)."""
    n_cols = max(len(r) for r in rows_data)
    if n_cols == 0:
        return []
    max_lens = []
    for c in range(n_cols):
        lens = [len(r[c]) if c < len(r) else 0 for r in rows_data]
        max_lens.append(max(lens) if lens else 1)
    
    # Skala non-linear (pangkat 0.65) agar kolom nomor/kode ringkas, dan kolom deskripsi leluasa
    weights = [max(float(l)**0.65, 2.5) for l in max_lens]
    total_w = sum(weights)
    return [(w / total_w) * total_width_in for w in weights]

def make_callout_box(doc, lines):
    """Membuat callout box multi-paragraf berarsir untuk blockquote / alert (A4 Portrait)."""
    if not lines:
        return
        
    first_line = lines[0].strip()
    alert_type = 'NOTE'
    m_alert = re.match(r'^\[\!(IMPORTANT|WARNING|CAUTION|TIP|NOTE)\]\s*(.*)', first_line)
    
    content_lines = []
    if m_alert:
        alert_type = m_alert.group(1).upper()
        if m_alert.group(2):
            content_lines.append(m_alert.group(2))
        content_lines.extend(lines[1:])
    else:
        content_lines = lines
        
    cfg = ALERT_CONFIG.get(alert_type, ALERT_CONFIG['NOTE'])
    
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(PRINTABLE_WIDTH_IN)
    set_cell_background(cell, cfg['bg'])
    set_cell_margins(cell, top=100, bottom=100, left=140, right=120)
    
    # Border kiri tebal
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{cfg["color"]}"/>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p_first = cell.paragraphs[0]
    p_first.paragraph_format.space_before = Pt(2)
    p_first.paragraph_format.space_after = Pt(2)
    p_first.paragraph_format.line_spacing = 1.15
    
    if m_alert:
        r_title = p_first.add_run(cfg['title'] + "\n")
        r_title.font.name = 'Arial'
        r_title.font.size = Pt(9.5)
        r_title.font.bold = True
        r_title.font.color.rgb = COLOR_PRIMARY_NAVY if alert_type == 'NOTE' else (COLOR_ALERT_RED if 'C00000' in cfg['color'] else COLOR_ALERT_GREEN)
        
    for idx, c_line in enumerate(content_lines):
        if idx == 0 and not m_alert:
            p = p_first
        elif idx == 0 and m_alert:
            p = p_first
            format_inline_runs(p, c_line, base_font_size=9.0, is_italic=True)
            continue
        else:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
        format_inline_runs(p, c_line, base_font_size=9.0, is_italic=True)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def format_inline_runs(paragraph, text, base_font_size=10.0, is_italic=False):
    """Memproses format inline markdown (*bold*, _italic_, `code`, math, links) ke runs docx berbasis font Arial."""
    pattern = r'(\[.*?\]\(.*?\)|\*\*.*?\*\*|\*.*?\*|`.*?`|\$.*?\$)'
    tokens = re.split(pattern, text)
    
    for token in tokens:
        if not token:
            continue
            
        run = paragraph.add_run()
        run.font.name = 'Arial'
        run.font.size = Pt(base_font_size)
        run.font.color.rgb = COLOR_DARK_TEXT
        if is_italic:
            run.font.italic = True
            
        if token.startswith('[') and '](' in token and token.endswith(')'):
            m_link = re.match(r'\[(.*?)\]\((.*?)\)', token)
            if m_link:
                run.text = m_link.group(1)
                run.font.color.rgb = COLOR_SECONDARY_BLUE
                run.font.underline = True
            else:
                run.text = token
        elif token.startswith('**') and token.endswith('**') and len(token) >= 4:
            run.text = token[2:-2]
            run.font.bold = True
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            run.text = token[1:-1]
            run.font.italic = True
        elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
            run.text = token[1:-1]
            run.font.name = 'Consolas'
            run.font.size = Pt(base_font_size - 0.5)
            run.font.color.rgb = RGBColor(160, 40, 40)
        elif token.startswith('$') and token.endswith('$') and len(token) >= 2:
            clean_math = token[1:-1].replace(r'\text', '').replace('{', '').replace('}', '').replace(r'\ge', '≥').replace(r'\le', '≤').replace(r'\times', '×').replace(r'\rightarrow', '→')
            run.text = clean_math
            run.font.italic = True
        else:
            run.text = token

def parse_markdown_to_docx(md_path, docx_path):
    """Fungsi utama pengonversi satu file Markdown ke format DOCX profesional A4 Portrait standar Template 2024."""
    filename = os.path.basename(md_path)
    base_name = os.path.splitext(filename)[0]
    print(f"  -> Mengonversi: {filename} -> {os.path.basename(docx_path)}")
    
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
        md_text = f.read()

    doc = Document()
    
    # -------------------------------------------------------------
    # 1. Konfigurasi Halaman & Section: Standar Baku A4 Portrait
    # Ukuran A4: 210 x 297 mm, Margin 25 mm (Template KPT FSTI)
    # -------------------------------------------------------------
    section = doc.sections[0]
    section.orientation = WD_ORIENT.PORTRAIT
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(25)
    section.bottom_margin = Mm(25)
    section.left_margin = Mm(25)
    section.right_margin = Mm(25)
        
    # Header & Footer Institusional Template KPT FSTI 2024
    header = section.header
    p_head = header.paragraphs[0]
    p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hdr_text = "Template Master KPT FSTI - Universitas Widya Gama Malang" if ("TEMPLATE" in filename.upper() or "045" in filename) else "Kurikulum Program Studi Sistem dan Teknologi Informasi (SISTEKIN) — FSTI UWG"
    r_head = p_head.add_run(hdr_text)
    r_head.font.name = 'Arial'
    r_head.font.size = Pt(8.5)
    r_head.font.italic = True
    r_head.font.color.rgb = COLOR_MUTED_GRAY

    footer = section.footer
    p_foot = footer.paragraphs[0]
    p_foot.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_foot1 = p_foot.add_run("Buku Kurikulum KPT-OBE SISTEKIN 2026  |  FSTI Universitas Widyagama Malang")
    r_foot1.font.name = 'Arial'
    r_foot1.font.size = Pt(8.5)
    r_foot1.font.color.rgb = COLOR_MUTED_GRAY
    
    # Normal Style: Arial 10 pt (Standar Template_KPT_2024.docx)
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = COLOR_DARK_TEXT
    
    lines = md_text.splitlines()
    in_table = False
    table_lines = []
    in_code_block = False
    code_lines = []
    in_quote = False
    quote_lines = []
    
    def flush_table():
        nonlocal in_table, table_lines
        if not table_lines:
            in_table = False
            return
            
        rows_data = []
        for t_line in table_lines:
            if re.match(r'^\s*\|[-| :]+\|\s*$', t_line):
                continue
            cells = [c.strip() for c in t_line.strip('|').split('|')]
            rows_data.append(cells)
            
        if rows_data:
            n_rows = len(rows_data)
            n_cols = max(len(r) for r in rows_data)
            
            table = doc.add_table(rows=n_rows, cols=n_cols)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.autofit = False
            set_table_borders(table, color=HEX_BORDER_GRAY, sz="4")
            
            # Hitung alokasi lebar kolom proporsional agar pas 100% dalam A4 Portrait (6.30 in)
            col_widths = compute_col_widths(rows_data, total_width_in=PRINTABLE_WIDTH_IN)
            
            # Font size adaptif berdasarkan kepadatan kolom A4 Portrait
            if n_cols > 10:
                hdr_font_sz, cell_font_sz = 7.0, 6.5
                cell_v_pad, cell_h_pad = 45, 60
            elif n_cols > 7:
                hdr_font_sz, cell_font_sz = 7.5, 7.0
                cell_v_pad, cell_h_pad = 50, 70
            elif n_cols > 4:
                hdr_font_sz, cell_font_sz = 8.5, 8.0
                cell_v_pad, cell_h_pad = 60, 80
            else:
                hdr_font_sz, cell_font_sz = 9.5, 9.0
                cell_v_pad, cell_h_pad = 70, 90

            # Header Row Repeat (CantSplit & TblHeader)
            trPr = table.rows[0]._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
            
            for c_idx in range(n_cols):
                if c_idx < len(col_widths):
                    table.columns[c_idx].width = Inches(col_widths[c_idx])
            
            for r_idx, row_cells in enumerate(rows_data):
                row = table.rows[r_idx]
                is_header = (r_idx == 0)
                
                # CantSplit per baris agar tidak terpotong canggung saat pergantian halaman
                r_trPr = row._tr.get_or_add_trPr()
                r_trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
                
                for c_idx in range(n_cols):
                    cell = row.cells[c_idx]
                    if c_idx < len(col_widths):
                        cell.width = Inches(col_widths[c_idx])
                    cell_text = row_cells[c_idx] if c_idx < len(row_cells) else ""
                    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    
                    if is_header:
                        set_cell_background(cell, HEX_PRIMARY_NAVY)
                        set_cell_margins(cell, top=cell_v_pad + 20, bottom=cell_v_pad + 20, left=cell_h_pad, right=cell_h_pad)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.space_before = Pt(2)
                        p.paragraph_format.space_after = Pt(2)
                        p.paragraph_format.line_spacing = 1.05
                        
                        run = p.add_run(cell_text.replace('**', '').replace('`', ''))
                        run.font.name = 'Arial'
                        run.font.size = Pt(hdr_font_sz)
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)
                    else:
                        if r_idx % 2 == 1:
                            set_cell_background(cell, "FFFFFF")
                        else:
                            set_cell_background(cell, HEX_LIGHT_ROW)
                            
                        set_cell_margins(cell, top=cell_v_pad, bottom=cell_v_pad, left=cell_h_pad, right=cell_h_pad)
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.space_before = Pt(1)
                        p.paragraph_format.space_after = Pt(1)
                        p.paragraph_format.line_spacing = 1.05
                        format_inline_runs(p, cell_text, base_font_size=cell_font_sz)
                        
            # Spasi setelah tabel
            p_after = doc.add_paragraph()
            p_after.paragraph_format.space_after = Pt(4)
            
        table_lines = []
        in_table = False

    def flush_code():
        nonlocal in_code_block, code_lines
        if not code_lines:
            in_code_block = False
            return
            
        text = "\n".join(code_lines)
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        cell = tbl.cell(0, 0)
        cell.width = Inches(PRINTABLE_WIDTH_IN)
        set_cell_background(cell, "F8F9FA")
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        set_table_borders(tbl, color="E2E8F0", sz="4")
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(text)
        run.font.name = 'Consolas'
        run.font.size = Pt(8.5)
        run.font.color.rgb = RGBColor(40, 40, 40)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_after = Pt(4)
        
        code_lines = []
        in_code_block = False

    def flush_quote():
        nonlocal in_quote, quote_lines
        if not quote_lines:
            in_quote = False
            return
        make_callout_box(doc, quote_lines)
        quote_lines = []
        in_quote = False

    for line in lines:
        stripped = line.strip()
        
        # Check code blocks
        if stripped.startswith('```'):
            if in_code_block:
                flush_code()
            else:
                if in_table:
                    flush_table()
                if in_quote:
                    flush_quote()
                in_code_block = True
            continue
            
        if in_code_block:
            code_lines.append(line)
            continue
            
        # Check tables
        if stripped.startswith('|') and stripped.endswith('|'):
            if in_quote:
                flush_quote()
            in_table = True
            table_lines.append(stripped)
            continue
        else:
            if in_table:
                flush_table()
                
        # Check blockquotes / alerts
        if stripped.startswith('>'):
            in_quote = True
            clean_q = re.sub(r'^>\s*', '', stripped)
            quote_lines.append(clean_q)
            continue
        else:
            if in_quote:
                flush_quote()
                
        # Empty line
        if not stripped:
            continue
            
        # Horizontal rule
        if stripped in ['---', '***', '___']:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            hr_text = "—" * 72
            run = p.add_run(hr_text)
            run.font.color.rgb = RGBColor(200, 210, 225)
            run.font.size = Pt(7)
            continue
            
        # Headings (Hierarki Resmi Template_KPT_2024.docx: Arial, #1F4E79, #2F2F2F)
        if stripped.startswith('# '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(stripped[2:])
            run.font.name = 'Arial'
            run.font.size = Pt(14)
            run.font.bold = True
            run.font.color.rgb = COLOR_PRIMARY_NAVY
            continue
        elif stripped.startswith('## '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(stripped[3:])
            run.font.name = 'Arial'
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = COLOR_PRIMARY_NAVY
            continue
        elif stripped.startswith('### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(9)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(stripped[4:])
            run.font.name = 'Arial'
            run.font.size = Pt(11)
            run.font.bold = True
            run.font.color.rgb = COLOR_HEADING3
            continue
        elif stripped.startswith('#### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(stripped[5:])
            run.font.name = 'Arial'
            run.font.size = Pt(10)
            run.font.bold = True
            run.font.italic = True
            run.font.color.rgb = COLOR_PRIMARY_NAVY
            continue
            
        # Bullet list
        if stripped.startswith(('* ', '- ', '+ ')):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            format_inline_runs(p, stripped[2:])
            continue
            
        # Numbered list
        num_match = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if num_match:
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            format_inline_runs(p, num_match.group(2))
            continue
            
        # Regular Paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        format_inline_runs(p, stripped)
        
    if in_table:
        flush_table()
    if in_code_block:
        flush_code()
    if in_quote:
        flush_quote()
        
    try:
        doc.save(docx_path)
        print(f"     [SUKSES] Tersimpan: {os.path.getsize(docx_path):,} bytes (A4 Portrait)")
        # Jika buku kurikulum final, sinkronkan juga ke root dokumen
        if base_name == "BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL":
            root_final = os.path.join(os.path.dirname(WORKDIR), "BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.docx")
            try:
                doc.save(root_final)
                print(f"     [SYNC] Berhasil disinkronkan ke root: {os.path.basename(root_final)}")
            except Exception as e_root:
                print(f"     [WARN] Tidak dapat menyalin ke root: {e_root}")
    except PermissionError:
        alt_path = os.path.join(DOCX_DIR, f"{base_name}_UPDATED.docx")
        try:
            doc.save(alt_path)
            print(f"     [PERINGATAN] File sedang dibuka di MS Word! Tersimpan sebagai: {os.path.basename(alt_path)} ({os.path.getsize(alt_path):,} bytes)")
        except Exception as e_alt:
            print(f"     [ERROR] Gagal menyimpan (file dikunci Word): {e_alt}")

def convert_target(target_arg=None):
    os.makedirs(DOCX_DIR, exist_ok=True)
    print("=====================================================================")
    print("  MARKDOWN TO DOCX CONVERTER ENGINE — STANDAR TEMPLATE 2024 (A4 PORTRAIT)")
    print(f"  Direktori Keluaran: {DOCX_DIR}")
    print("=====================================================================")
    
    if target_arg:
        # Jika argumen berupa pola atau nama file spesifik
        query = target_arg.strip()
        if os.path.isabs(query) and os.path.exists(query):
            target_files = [query]
        else:
            pattern = os.path.join(WORKDIR, f"*{query}*")
            candidates = glob.glob(pattern)
            target_files = [f for f in candidates if f.endswith('.md') and not ('-BACKUP' in f or '_BACKUP' in f)]
            
        if not target_files:
            print(f"[GAGAL] Tidak ditemukan file markdown yang cocok dengan kata kunci: '{query}'")
            return
    else:
        all_md = sorted(glob.glob(os.path.join(WORKDIR, "*.md")))
        # Filter file backup dan file temporary
        target_files = [f for f in all_md if not ('-BACKUP' in f or '_BACKUP' in f or f.startswith('_'))]
        
    print(f"Memproses {len(target_files)} dokumen Markdown (Seluruhnya format A4 Portrait)...\n")
    success_count = 0
    
    for md_path in target_files:
        base_name = os.path.splitext(os.path.basename(md_path))[0]
        docx_path = os.path.join(DOCX_DIR, f"{base_name}.docx")
        try:
            parse_markdown_to_docx(md_path, docx_path)
            success_count += 1
        except Exception as e:
            print(f"     [ERROR] Gagal mengonversi {os.path.basename(md_path)}: {e}")
            
    print(f"\n[SELESAI] Berhasil mengonversi {success_count}/{len(target_files)} file Markdown ke folder DOCX dengan format baku A4 Portrait!")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else None
    convert_target(target)
