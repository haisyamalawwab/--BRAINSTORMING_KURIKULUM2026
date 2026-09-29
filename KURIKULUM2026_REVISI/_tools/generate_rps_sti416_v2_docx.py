#!/usr/bin/env python3
"""
Generator DOCX untuk RPS STI-416 Versi 2 (Simplified Python Focus)
Mengonversi Markdown ke Microsoft Word dengan format Template RPS OBE FSTI UWG 2024
"""

import os
import sys
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_cell_border(cell, **kwargs):
    """
    Set border untuk cell di tabel
    """
    tc = cell._element
    tcPr = tc.get_or_add_tcPr()

    # list of border positions
    positions = ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']
    
    for position in positions:
        if position in kwargs:
            tag = 'w:{}'.format(position)
            element = OxmlElement(tag)
            element.set(qn('w:val'), kwargs[position]['val'])
            element.set(qn('w:sz'), str(kwargs[position]['sz']))
            element.set(qn('w:space'), '0')
            element.set(qn('w:color'), kwargs[position]['color'])
            tcPr.append(element)

def add_styled_heading(doc, text, level=1):
    """Tambahkan heading dengan styling"""
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.name = 'Arial'
        run.font.bold = True
        run.font.size = Pt(14 if level == 1 else 12 if level == 2 else 11)
    return heading

def add_styled_paragraph(doc, text, bold=False, italic=False, font_size=11):
    """Tambahkan paragraph dengan styling"""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    return para

def parse_markdown_table(lines, start_idx):
    """Parse markdown table menjadi list of rows"""
    rows = []
    idx = start_idx
    
    # Skip header separator line (|---|---|)
    if idx < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[idx]):
        idx += 1
    
    # Parse data rows
    while idx < len(lines):
        line = lines[idx].strip()
        if not line.startswith('|'):
            break
        
        # Split by | dan clean
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        rows.append(cells)
        idx += 1
    
    return rows, idx

def convert_md_to_docx(md_path, docx_path):
    """Convert Markdown RPS ke DOCX"""
    
    print("=" * 80)
    print("🚀 GENERATOR RPS DOCX — STI-416 Web Back End Development (Versi 2)")
    print("=" * 80)
    print(f"📄 Input  : {md_path}")
    print(f"📁 Output : {docx_path}")
    print("-" * 80)
    
    # Baca file markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Buat dokumen Word
    doc = Document()
    
    # Set margin A4 Portrait (25mm)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.98)
        section.bottom_margin = Inches(0.98)
        section.left_margin = Inches(0.98)
        section.right_margin = Inches(0.98)
    
    # Header: Logo + Judul
    header_para = doc.add_paragraph()
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = header_para.add_run("RENCANA PEMBELAJARAN SEMESTER (RPS)\n")
    run.font.name = 'Arial'
    run.font.size = Pt(16)
    run.font.bold = True
    
    run2 = header_para.add_run("STI-416 — PENGEMBANGAN WEB BACK END\n")
    run2.font.name = 'Arial'
    run2.font.size = Pt(14)
    run2.font.bold = True
    
    run3 = header_para.add_run("(VERSI 2 — SIMPLIFIED PYTHON FOCUS)\n")
    run3.font.name = 'Arial'
    run3.font.size = Pt(12)
    run3.font.italic = True
    
    run4 = header_para.add_run("\nProgram Studi S1 Sistem dan Teknologi Informasi (SISTEKIN)\n")
    run4.font.name = 'Arial'
    run4.font.size = Pt(11)
    
    run5 = header_para.add_run("Fakultas Sains dan Teknologi Informasi (FSTI)\n")
    run5.font.name = 'Arial'
    run5.font.size = Pt(11)
    
    run6 = header_para.add_run("Universitas Widyagama Malang")
    run6.font.name = 'Arial'
    run6.font.size = Pt(11)
    
    doc.add_paragraph()
    
    # Proses line by line
    i = 0
    in_table = False
    table_start = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Heading Level 1
        if line.startswith('# '):
            text = line[2:].strip()
            add_styled_heading(doc, text, level=1)
            i += 1
            continue
        
        # Heading Level 2
        if line.startswith('## '):
            text = line[3:].strip()
            add_styled_heading(doc, text, level=2)
            i += 1
            continue
        
        # Heading Level 3
        if line.startswith('### '):
            text = line[4:].strip()
            add_styled_heading(doc, text, level=3)
            i += 1
            continue
        
        # Heading Level 4
        if line.startswith('#### '):
            text = line[5:].strip()
            para = doc.add_paragraph()
            run = para.add_run(text)
            run.font.name = 'Arial'
            run.font.size = Pt(11)
            run.font.bold = True
            i += 1
            continue
        
        # Bold text (**text**)
        if line.startswith('**') and line.endswith('**'):
            text = line[2:-2]
            add_styled_paragraph(doc, text, bold=True)
            i += 1
            continue
        
        # List item
        if line.startswith('- ') or line.startswith('* '):
            text = line[2:].strip()
            para = doc.add_paragraph(text, style='List Bullet')
            for run in para.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(11)
            i += 1
            continue
        
        # Numbered list
        if re.match(r'^\d+\.\s+', line):
            text = re.sub(r'^\d+\.\s+', '', line)
            para = doc.add_paragraph(text, style='List Number')
            for run in para.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(11)
            i += 1
            continue
        
        # Table detection (|---|---|)
        if line.startswith('|') and '---' in line:
            # Ambil header dari line sebelumnya
            if i > 0 and lines[i-1].strip().startswith('|'):
                header_line = lines[i-1].strip()
                headers = [h.strip() for h in header_line.split('|')[1:-1]]
                
                # Parse table rows
                table_rows, next_idx = parse_markdown_table(lines, i+1)
                
                if table_rows:
                    # Buat tabel
                    num_cols = len(headers)
                    num_rows = len(table_rows) + 1  # +1 untuk header
                    
                    table = doc.add_table(rows=num_rows, cols=num_cols)
                    table.style = 'Light Grid Accent 1'
                    table.alignment = WD_TABLE_ALIGNMENT.CENTER
                    
                    # Set header
                    header_cells = table.rows[0].cells
                    for idx, header_text in enumerate(headers):
                        cell = header_cells[idx]
                        cell.text = header_text
                        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                        
                        # Style header
                        for paragraph in cell.paragraphs:
                            for run in paragraph.runs:
                                run.font.name = 'Arial'
                                run.font.size = Pt(10)
                                run.font.bold = True
                            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        
                        # Header background color
                        shading_elm = OxmlElement('w:shd')
                        shading_elm.set(qn('w:fill'), '4472C4')
                        cell._element.get_or_add_tcPr().append(shading_elm)
                    
                    # Set data rows
                    for row_idx, row_data in enumerate(table_rows, start=1):
                        cells = table.rows[row_idx].cells
                        for col_idx, cell_text in enumerate(row_data):
                            if col_idx < len(cells):
                                cells[col_idx].text = cell_text
                                cells[col_idx].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                                
                                # Style cell
                                for paragraph in cells[col_idx].paragraphs:
                                    for run in paragraph.runs:
                                        run.font.name = 'Arial'
                                        run.font.size = Pt(9)
                                    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    
                    doc.add_paragraph()  # Spacing after table
                    i = next_idx
                    continue
            
            i += 1
            continue
        
        # Code block (```)
        if line.startswith('```'):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            
            if code_lines:
                para = doc.add_paragraph()
                run = para.add_run('\n'.join(code_lines))
                run.font.name = 'Courier New'
                run.font.size = Pt(9)
                para.paragraph_format.left_indent = Inches(0.5)
            
            i += 1
            continue
        
        # Blockquote (>)
        if line.startswith('> '):
            text = line[2:].strip()
            para = doc.add_paragraph()
            run = para.add_run(text)
            run.font.name = 'Arial'
            run.font.size = Pt(10)
            run.font.italic = True
            para.paragraph_format.left_indent = Inches(0.5)
            i += 1
            continue
        
        # Horizontal rule (---)
        if line.startswith('---'):
            para = doc.add_paragraph()
            run = para.add_run('_' * 80)
            run.font.color.rgb = RGBColor(200, 200, 200)
            i += 1
            continue
        
        # Regular paragraph
        if line and not line.startswith('#'):
            # Remove markdown bold/italic inline
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
            text = re.sub(r'\*(.+?)\*', r'\1', text)
            text = re.sub(r'`(.+?)`', r'\1', text)
            
            add_styled_paragraph(doc, text)
        
        i += 1
    
    # Save DOCX
    doc.save(docx_path)
    
    file_size = os.path.getsize(docx_path) / 1024  # KB
    
    print("⚙️  Memproses konversi Markdown → DOCX...")
    print("=" * 80)
    print("✅ SUKSES! RPS DOCX Versi 2 (Simplified) berhasil di-generate")
    print("=" * 80)
    print(f"📍 Lokasi file: {docx_path}")
    print(f"📊 Ukuran    : {file_size:.2f} KB")
    print("=" * 80)

if __name__ == '__main__':
    # Path relatif dari folder KURIKULUM2026_REVISI
    base_dir = Path(__file__).parent.parent
    md_file = base_dir / 'RPS_STI-416_Web_Back_End_Development_V2_SIMPLIFIED.md'
    docx_dir = base_dir / 'DOCX'
    docx_file = docx_dir / 'RPS_STI-416_Web_Back_End_Development_V2_SIMPLIFIED_UPDATED.docx'
    
    # Buat folder DOCX jika belum ada
    docx_dir.mkdir(exist_ok=True)
    
    if not md_file.exists():
        print(f"❌ ERROR: File {md_file} tidak ditemukan!")
        sys.exit(1)
    
    convert_md_to_docx(str(md_file), str(docx_file))
