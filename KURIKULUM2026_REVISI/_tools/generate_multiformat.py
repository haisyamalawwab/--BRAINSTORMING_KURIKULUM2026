# -*- coding: utf-8 -*-
"""
=============================================================================
UNIFIED MULTIFORMAT DOCUMENT GENERATOR — KURIKULUM SISTEKIN 2026
=============================================================================
Mendukung generasi format DOCX, PDF, dan EXCEL secara:
1. PER-FILE INPUT (dinamis berdasarkan nama file, prefix nomor, atau path)
2. BULK (seluruh dokumen .md sekaligus)

Penggunaan CLI:
  python generate_multiformat.py --file 045
  python generate_multiformat.py --file 045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md
  python generate_multiformat.py --file 045 --format docx,pdf,excel
  python generate_multiformat.py --bulk --format docx
  python generate_multiformat.py --all
=============================================================================
"""

import os
import sys
import re
import glob
import time
import argparse
import subprocess
import io

# Pastikan UTF-8 di terminal Windows
if not isinstance(sys.stdout, io.TextIOWrapper) or sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT_DIR)
DOCX_DIR = os.path.join(WORKDIR, "DOCX")
PDF_DIR = os.path.join(WORKDIR, "PDF")
EXCEL_DIR = os.path.join(WORKDIR, "EXCEL")
HTML_DIR = os.path.join(WORKDIR, "HTML")

for d in [DOCX_DIR, PDF_DIR, EXCEL_DIR, HTML_DIR]:
    os.makedirs(d, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. BROWSER FINDER (FOR PDF GENERATION)
# -----------------------------------------------------------------------------
def find_browser():
    candidates = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
        os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe'),
        os.path.expandvars(r'%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe'),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

# -----------------------------------------------------------------------------
# 2. DOCX GENERATOR
# -----------------------------------------------------------------------------
def generate_docx(md_path, out_docx_paths):
    import docx
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
    from docx.oxml import OxmlElement, parse_xml
    from docx.oxml.ns import nsdecls, qn

    # Corporate Colors FSTI UWG
    COLOR_NAVY = RGBColor(31, 56, 100)      # #1F3864
    COLOR_BLUE = RGBColor(46, 117, 182)     # #2E75B6
    COLOR_TEXT = RGBColor(38, 38, 38)       # #262626
    COLOR_MUTED = RGBColor(89, 89, 89)      # #595959

    HEX_NAVY = "1F3864"
    HEX_ALT = "F2F5F9"
    HEX_BORDER = "D3D3D3"
    HEX_CALLOUT = "EEF4FB"

    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
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

    def set_table_borders(table, color="D3D3D3", sz="4"):
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    def format_inline_runs(paragraph, text):
        tokens = re.split(r'(\*\*.*?\*\*|\*.*?\*|`.*?`)', text)
        for token in tokens:
            if not token:
                continue
            if token.startswith('**') and token.endswith('**') and len(token) >= 4:
                run = paragraph.add_run(token[2:-2])
                run.font.bold = True
                run.font.color.rgb = COLOR_TEXT
            elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
                run = paragraph.add_run(token[1:-1])
                run.font.italic = True
                run.font.color.rgb = COLOR_TEXT
            elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
                run = paragraph.add_run(token[1:-1])
                run.font.name = 'Consolas'
                run.font.size = Pt(9.5)
                run.font.color.rgb = COLOR_NAVY
            else:
                run = paragraph.add_run(token)
                run.font.name = 'Calibri'
                run.font.size = Pt(11)
                run.font.color.rgb = COLOR_TEXT

    doc = Document()
    # A4 Margins
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_table = False
    table_rows = []
    in_code = False
    code_lines = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        # Filter divider row
        valid_rows = [r for r in table_rows if not re.match(r'^\s*\|[-| :]+\|\s*$', r)]
        if not valid_rows:
            in_table = False
            table_rows = []
            return

        parsed_rows = []
        for r in valid_rows:
            cells = [c.strip() for c in r.strip('|').split('|')]
            parsed_rows.append(cells)

        n_cols = max(len(r) for r in parsed_rows)
        table = doc.add_table(rows=len(parsed_rows), cols=n_cols)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = True
        set_table_borders(table)

        # Style header
        header_tr = table.rows[0]._tr.get_or_add_trPr()
        header_tr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

        for row_idx, r_data in enumerate(parsed_rows):
            row = table.rows[row_idx]
            is_header = (row_idx == 0)
            fill_hex = HEX_NAVY if is_header else (HEX_ALT if row_idx % 2 == 1 else "FFFFFF")

            for col_idx in range(n_cols):
                val = r_data[col_idx] if col_idx < len(r_data) else ""
                cell = row.cells[col_idx]
                set_cell_background(cell, fill_hex)
                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)

                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.line_spacing = 1.05

                if is_header:
                    run = p.add_run(val)
                    run.font.name = 'Calibri'
                    run.font.bold = True
                    run.font.size = Pt(9.5)
                    run.font.color.rgb = RGBColor(255, 255, 255)
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    format_inline_runs(p, val)
                    # Simple center heuristic
                    if len(val) <= 4 and re.match(r'^\d+$', val.strip()):
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        in_table = False
        table_rows = []

    def flush_code():
        nonlocal in_code, code_lines
        if code_lines:
            tbl = doc.add_table(rows=1, cols=1)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            cell = tbl.cell(0, 0)
            set_cell_background(cell, "F8F9FA")
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            p = cell.paragraphs[0]
            run = p.add_run("\n".join(code_lines))
            run.font.name = 'Consolas'
            run.font.size = Pt(8.5)
            run.font.color.rgb = COLOR_TEXT
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
        in_code = False
        code_lines = []

    for line in lines:
        stripped = line.strip()

        # Code Block
        if stripped.startswith('```'):
            if in_code:
                flush_code()
            else:
                if in_table:
                    flush_table()
                in_code = True
                code_lines = []
            continue

        if in_code:
            code_lines.append(line.rstrip('\r\n'))
            continue

        # Table
        if re.match(r'^\s*\|.+\|\s*$', stripped):
            in_table = True
            table_rows.append(stripped)
            continue
        else:
            if in_table:
                flush_table()

        if not stripped:
            continue

        # Headers
        if stripped.startswith('# '):
            h = doc.add_heading(level=1)
            h.paragraph_format.space_before = Pt(14)
            h.paragraph_format.space_after = Pt(6)
            run = h.add_run(stripped[2:])
            run.font.name = 'Calibri'
            run.font.size = Pt(18)
            run.font.bold = True
            run.font.color.rgb = COLOR_NAVY
            continue

        if stripped.startswith('## '):
            h = doc.add_heading(level=2)
            h.paragraph_format.space_before = Pt(12)
            h.paragraph_format.space_after = Pt(4)
            run = h.add_run(stripped[3:])
            run.font.name = 'Calibri'
            run.font.size = Pt(14)
            run.font.bold = True
            run.font.color.rgb = COLOR_BLUE
            continue

        if stripped.startswith('### '):
            h = doc.add_heading(level=3)
            h.paragraph_format.space_before = Pt(8)
            h.paragraph_format.space_after = Pt(3)
            run = h.add_run(stripped[4:])
            run.font.name = 'Calibri'
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = COLOR_NAVY
            continue

        if stripped.startswith('#### '):
            h = doc.add_heading(level=4)
            h.paragraph_format.space_before = Pt(6)
            h.paragraph_format.space_after = Pt(2)
            run = h.add_run(stripped[5:])
            run.font.name = 'Calibri'
            run.font.size = Pt(11)
            run.font.bold = True
            run.font.italic = True
            run.font.color.rgb = COLOR_NAVY
            continue

        # Blockquote / Callout
        if stripped.startswith('>'):
            clean_text = re.sub(r'^>\s*(\[!.*?\])?\s*', '', stripped)
            tbl = doc.add_table(rows=1, cols=1)
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            cell = tbl.cell(0, 0)
            set_cell_background(cell, HEX_CALLOUT)
            set_cell_margins(cell, top=100, bottom=100, left=180, right=150)
            # Thick left border
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = parse_xml(
                f'<w:tcBorders {nsdecls("w")}>'
                f'<w:left w:val="single" w:sz="24" w:space="0" w:color="2E75B6"/>'
                f'<w:top w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/>'
                f'</w:tcBorders>'
            )
            tcPr.append(tcBorders)
            p = cell.paragraphs[0]
            format_inline_runs(p, clean_text)
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
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
        num_m = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if num_m:
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            format_inline_runs(p, num_m.group(2))
            continue

        # Regular paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        format_inline_runs(p, stripped)

    if in_table:
        flush_table()
    if in_code:
        flush_code()

    for pth in out_docx_paths:
        doc.save(pth)
        print(f"     [SUKSES DOCX] -> {pth} ({os.path.getsize(pth):,} bytes)")

# -----------------------------------------------------------------------------
# 3. HTML & PDF GENERATOR
# -----------------------------------------------------------------------------
def generate_html_and_pdf(md_path, out_pdf_paths, browser_exe=None):
    base_name = os.path.splitext(os.path.basename(md_path))[0]
    out_html = os.path.join(HTML_DIR, f"{base_name}.html")

    # Import convert_md_to_html logic
    sys.path.insert(0, SCRIPT_DIR)
    import convert_md_to_html

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    md_text = md_text.replace(r'$\leftrightarrow$', '↔').replace(r'\leftrightarrow', '↔')
    md_text = md_text.replace(r'$\rightarrow$', '→').replace(r'\rightarrow', '→')
    md_text = md_text.replace(r'$\leftarrow$', '←').replace(r'\leftarrow', '←')
    md_text = re.sub(r'\$\\ge\s*([0-9]+)(?:\\text\{\s*SKS\})?\$', r'≥ \1 SKS', md_text)
    md_text = re.sub(r'\$\\le\s*([0-9]+)(?:\\text\{\s*SKS\})?\$', r'≤ \1 SKS', md_text)
    md_text = md_text.replace(r'$\ge$', '≥').replace(r'$\le$', '≤')
    md_text = md_text.replace(r'\ge', '≥').replace(r'\le', '≤')

    md_text = convert_md_to_html.process_alerts(md_text)
    md_text = convert_md_to_html.process_mermaid_blocks(md_text)
    md_text = convert_md_to_html.process_ascii_tables(md_text)

    convert_md_to_html.md.reset()
    content_html = convert_md_to_html.md.convert(md_text)
    content_html = re.sub(r'<table>', '<div class="table-wrapper"><table>', content_html)
    content_html = re.sub(r'</table>', '</table></div>', content_html)
    content_html = convert_md_to_html.post_process_html(content_html)

    title = base_name.replace('_', ' ')
    full_html = convert_md_to_html.build_full_html(os.path.basename(md_path), title, content_html, None, None)

    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"     [SUKSES HTML] -> {out_html} ({os.path.getsize(out_html):,} bytes)")

    # Generate PDF
    if not browser_exe:
        browser_exe = find_browser()

    if not browser_exe:
        print("     [PERINGATAN PDF] Browser Chrome/Edge tidak ditemukan, skip PDF.")
        return

    html_url = "file:///" + os.path.abspath(out_html).replace("\\", "/")
    tmp_pdf = out_pdf_paths[0]
    cmd = [
        browser_exe,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw',
        '--virtual-time-budget=2000',
        f'--print-to-pdf={os.path.abspath(tmp_pdf)}',
        html_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if res.returncode == 0 and os.path.exists(tmp_pdf) and os.path.getsize(tmp_pdf) > 0:
        print(f"     [SUKSES PDF]  -> {tmp_pdf} ({os.path.getsize(tmp_pdf):,} bytes)")
        # Copy to remaining targets if any
        for other_pdf in out_pdf_paths[1:]:
            with open(tmp_pdf, 'rb') as f_src, open(other_pdf, 'wb') as f_dst:
                f_dst.write(f_src.read())
            print(f"     [SUKSES PDF]  -> {other_pdf} ({os.path.getsize(other_pdf):,} bytes)")
    else:
        print(f"     [GAGAL PDF] Error: {res.stderr}")

# -----------------------------------------------------------------------------
# 4. EXCEL GENERATOR (STRUCTURED & MULTI-TAB)
# -----------------------------------------------------------------------------
def generate_excel(md_path, out_xlsx_paths):
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    COLOR_NAVY = '1F3864'
    COLOR_BLUE = '2E75B6'
    COLOR_ALT = 'EEF4FB'
    COLOR_BORDER = 'B8CCE4'
    COLOR_NOTE = 'FFF2CC'

    thin = Side(style='thin', color=COLOR_BORDER)
    BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    lines = md_text.split('\n')
    tables = []
    current_chapter = "BAB I"
    current_section = "Tabel Data"
    table_lines = []
    in_table = False

    for line in lines:
        if line.startswith('# '):
            current_chapter = re.sub(r'^#+\s*', '', line).strip()
        elif line.startswith('## '):
            current_section = re.sub(r'^#+\s*', '', line).strip()

        if re.match(r'^\s*\|.+\|\s*$', line):
            in_table = True
            table_lines.append(line.strip())
        else:
            if in_table:
                if len(table_lines) >= 2:
                    rows = []
                    for t_line in table_lines:
                        if re.match(r'^\s*\|[-| :]+\|\s*$', t_line):
                            continue
                        cells = [c.strip() for c in t_line.strip('|').split('|')]
                        rows.append(cells)
                    if rows:
                        tables.append({
                            'chapter': current_chapter,
                            'section': current_section,
                            'rows': rows
                        })
                table_lines = []
                in_table = False

    if in_table and len(table_lines) >= 2:
        rows = []
        for t_line in table_lines:
            if re.match(r'^\s*\|[-| :]+\|\s*$', t_line):
                continue
            cells = [c.strip() for c in t_line.strip('|').split('|')]
            rows.append(cells)
        if rows:
            tables.append({
                'chapter': current_chapter,
                'section': current_section,
                'rows': rows
            })

    if not tables:
        print(f"     [INFO EXCEL] Tidak ditemukan tabel markdown di {os.path.basename(md_path)}")
        return

    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # remove default sheet

    # Function to write tables into a worksheet
    def render_tables_to_sheet(ws, sheet_title, table_list):
        ws.sheet_properties.tabColor = COLOR_NAVY
        ws.sheet_view.showGridLines = True

        # Sheet Title Banner
        ws.row_dimensions[1].height = 25
        ws.cell(row=1, column=1, value=f"KURIKULUM SISTEKIN 2026 — {sheet_title}")
        ws.cell(row=1, column=1).font = Font(bold=True, color='FFFFFF', size=12, name='Calibri')
        ws.cell(row=1, column=1).fill = PatternFill('solid', fgColor=COLOR_NAVY)
        ws.cell(row=1, column=1).alignment = Alignment(vertical='center', horizontal='left')

        current_row = 3
        for t_idx, tbl in enumerate(table_list):
            rows = tbl['rows']
            if not rows:
                continue
            n_cols = max(len(r) for r in rows)

            # Table Header Label
            label = f"Tabel {t_idx+1}: {tbl['section']}"
            ws.row_dimensions[current_row].height = 20
            c_lbl = ws.cell(row=current_row, column=1, value=label)
            c_lbl.font = Font(bold=True, color='FFFFFF', size=10, name='Calibri')
            c_lbl.fill = PatternFill('solid', fgColor=COLOR_BLUE)
            c_lbl.alignment = Alignment(vertical='center', horizontal='left')
            try:
                ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=max(n_cols, 4))
            except Exception:
                pass
            current_row += 1

            # Column Headers
            header = rows[0]
            ws.row_dimensions[current_row].height = 24
            for c_i, h_val in enumerate(header, start=1):
                c = ws.cell(row=current_row, column=c_i, value=h_val)
                c.font = Font(bold=True, color='FFFFFF', size=9.5, name='Calibri')
                c.fill = PatternFill('solid', fgColor=COLOR_NAVY)
                c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
                c.border = BORDER
            current_row += 1

            # Data Rows
            for r_i, row in enumerate(rows[1:], start=1):
                row_padded = (row + [''] * n_cols)[:n_cols]
                bg = COLOR_ALT if r_i % 2 == 1 else 'FFFFFF'
                is_summary = bool(re.match(r'^(Total|Jumlah|Ringkasan|Catatan)', str(row_padded[0]), re.IGNORECASE))
                if is_summary:
                    bg = COLOR_NOTE

                ws.row_dimensions[current_row].height = 18
                for c_i, val in enumerate(row_padded, start=1):
                    c = ws.cell(row=current_row, column=c_i, value=val)
                    c.font = Font(bold=is_summary, color='000000', size=9.5, name='Calibri')
                    c.fill = PatternFill('solid', fgColor=bg)
                    halign = 'center' if (len(str(val)) <= 5 and re.match(r'^[0-9A-Za-z\-/]+$', str(val))) else 'left'
                    c.alignment = Alignment(wrap_text=True, vertical='center', horizontal=halign)
                    c.border = BORDER
                current_row += 1

            current_row += 2  # spacing between tables

        # Auto width
        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                if cell.value:
                    val_str = str(cell.value)
                    if len(val_str) < 80:
                        max_len = max(max_len, len(val_str))
            ws.column_dimensions[col_letter].width = max(10, min(max_len * 1.2, 55))

    base_name = os.path.splitext(os.path.basename(md_path))[0]

    # If document 045 (35 tables), create specialized categorized tabs + consolidated tab
    if "045" in base_name:
        # Group tables by thematic domains
        cat_map = {
            "01_Identitas": ["HALAMAN SAMPUL", "LEMBAR PENGESAHAN", "DAFTAR SINGKATAN", "BAB I"],
            "02_Evaluasi_Stakeholder": ["BAB II", "Stakeholder", "Benchmarking"],
            "03_VMTS_PEO_PL": ["BAB IV", "BAB V", "Profil Lulusan", "PEO"],
            "04_CPL_KKNI": ["CPL", "KKNI"],
            "05_Bahan_Kajian": ["BAB VI", "Bahan Kajian", "BoK", "Kedalaman"],
            "06_Struktur_Kurikulum": ["BAB VII", "BAB VIII", "Daftar MK", "Struktur", "Semester"],
            "07_MBKM_RPS": ["BAB IX", "BAB X", "RPS", "MBKM", "Rekognisi"],
            "08_Penilaian_CPL": ["BAB XI", "BAB XII", "BAB XIII", "Penilaian", "Evaluasi"],
        }

        # Sheet 1: Master Consolidated Sheet
        ws_master = wb.create_sheet("Semua_Tabel_Konsolidasi")
        render_tables_to_sheet(ws_master, "Seluruh Tabel Buku KPT 2024", tables)

        # Tab per category
        for cat_name, keywords in cat_map.items():
            matched_tables = []
            for t in tables:
                text_to_check = f"{t['chapter']} {t['section']}"
                if any(k.lower() in text_to_check.lower() for k in keywords):
                    matched_tables.append(t)
            if matched_tables:
                ws_cat = wb.create_sheet(cat_name)
                render_tables_to_sheet(ws_cat, cat_name.replace('_', ' '), matched_tables)
    else:
        # Generic multi-sheet or single sheet
        ws_single = wb.create_sheet("Data_Tabel")
        render_tables_to_sheet(ws_single, base_name.replace('_', ' '), tables)

    for pth in out_xlsx_paths:
        try:
            wb.save(pth)
            print(f"     [SUKSES EXCEL] -> {pth} ({os.path.getsize(pth):,} bytes, {len(wb.sheetnames)} tabs)")
        except PermissionError:
            print(f"     [PERINGATAN EXCEL] File {pth} sedang terkunci oleh aplikasi lain.")

# -----------------------------------------------------------------------------
# 5. CLI DISPATCHER & BULK RESOLVER
# -----------------------------------------------------------------------------
def resolve_target_files(file_arg, bulk_flag):
    all_md_files = sorted(glob.glob(os.path.join(WORKDIR, "*.md")))
    all_md_files = [f for f in all_md_files if not f.endswith("-BACKUP.md")]

    if bulk_flag or not file_arg:
        return all_md_files

    # Match by exact path
    if os.path.isabs(file_arg) and os.path.exists(file_arg):
        return [file_arg]

    # Match by filename in WORKDIR
    direct_path = os.path.join(WORKDIR, file_arg)
    if os.path.exists(direct_path):
        return [direct_path]

    # Match with .md added
    if os.path.exists(direct_path + ".md"):
        return [direct_path + ".md"]

    # Match by prefix or substring (e.g. '045')
    matched = [f for f in all_md_files if file_arg.lower() in os.path.basename(f).lower()]
    if matched:
        return matched

    print(f"[ERROR] Tidak dapat menemukan file Markdown yang cocok dengan input: '{file_arg}'")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Unified Multiformat Generator (DOCX, PDF, EXCEL) — SISTEKIN 2026",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-f', '--file',
        help="Target file input (bisa kode prefix seperti '045', nama file, atau path). Contoh: --file 045"
    )
    parser.add_argument(
        '-a', '--all', '--bulk',
        action='store_true',
        help="Proses seluruh file Markdown di folder secara massal (bulk mode)."
    )
    parser.add_argument(
        '--format',
        default='all',
        help="Pilihan format: 'all' (default), atau kombinasi 'docx', 'pdf', 'excel'. Contoh: --format docx,pdf,excel"
    )

    args = parser.parse_args()

    # Determine formats to generate
    req_formats = [f.strip().lower() for f in args.format.split(',')]
    gen_all = ('all' in req_formats)
    do_docx = gen_all or ('docx' in req_formats)
    do_pdf = gen_all or ('pdf' in req_formats)
    do_excel = gen_all or ('excel' in req_formats)

    targets = resolve_target_files(args.file, args.all)

    print("=====================================================================")
    print("  UNIFIED MULTIFORMAT GENERATOR (DOCX, PDF, EXCEL) — SISTEKIN 2026")
    print("=====================================================================")
    print(f"Mode          : {'BULK (' + str(len(targets)) + ' files)' if (args.all or len(targets)>1) else 'SINGLE FILE INPUT'}")
    print(f"Target Dokumen: {[os.path.basename(t) for t in targets]}")
    print(f"Format Dipilih: DOCX={do_docx}, PDF={do_pdf}, EXCEL={do_excel}")
    print("---------------------------------------------------------------------\n")

    browser_exe = find_browser() if do_pdf else None
    success_stats = {'docx': 0, 'pdf': 0, 'excel': 0}

    for idx, md_path in enumerate(targets, 1):
        base_name = os.path.splitext(os.path.basename(md_path))[0]
        print(f"[{idx}/{len(targets)}] Memproses: {os.path.basename(md_path)}")

        # 1. DOCX
        if do_docx:
            out_docx = [
                os.path.join(DOCX_DIR, f"{base_name}.docx"),
                os.path.join(WORKDIR, f"{base_name}.docx")
            ]
            try:
                generate_docx(md_path, out_docx)
                success_stats['docx'] += 1
            except Exception as e:
                print(f"     [ERROR DOCX]: {e}")

        # 2. PDF (via HTML + Chromium Headless)
        if do_pdf:
            out_pdf = [
                os.path.join(PDF_DIR, f"{base_name}.pdf"),
                os.path.join(WORKDIR, f"{base_name}.pdf")
            ]
            try:
                generate_html_and_pdf(md_path, out_pdf, browser_exe)
                success_stats['pdf'] += 1
            except Exception as e:
                print(f"     [ERROR PDF]: {e}")

        # 3. EXCEL
        if do_excel:
            out_xlsx = [
                os.path.join(EXCEL_DIR, f"{base_name}.xlsx"),
                os.path.join(WORKDIR, f"{base_name}.xlsx")
            ]
            try:
                generate_excel(md_path, out_xlsx)
                success_stats['excel'] += 1
            except Exception as e:
                print(f"     [ERROR EXCEL]: {e}")

        print()

    print("=====================================================================")
    print("  RINGKASAN HASIL GENERASI:")
    print(f"  - DOCX Berhasil : {success_stats['docx']}/{len(targets)}")
    print(f"  - PDF Berhasil  : {success_stats['pdf']}/{len(targets)}")
    print(f"  - EXCEL Berhasil: {success_stats['excel']}/{len(targets)}")
    print("=====================================================================")

if __name__ == '__main__':
    main()
