# -*- coding: utf-8 -*-
"""
update_005_id_en.py
Menambahkan kolom Nama Mata Kuliah (Bahasa Indonesia) dan Course Name (English)
ke seluruh tabel di 005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md.
"""

import json
import re
import os

courses = json.load(open("courses_id_en_master.json", encoding="utf-8"))

path_005 = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI\005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md"
with open(path_005, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    # 1. Check Table Headers
    if re.search(r'\|\s*No\s*\|\s*Kode MK\s*\|\s*Nama Mata Kuliah\s*\|\s*SKS\s*\|\s*Tipe\s*\|\s*Semester\s*\|\s*Prasyarat\s*\|\s*Catatan', line):
        # Tabel 1.1 MKWU
        new_lines.append("| No | Kode MK | Nama Mata Kuliah (Indonesia) | Course Name (English) | SKS | Tipe | Semester | Prasyarat | Catatan / Kebijakan |\n")
        continue
    elif re.search(r'\|\s*No\s*\|\s*Kode MK\s*\|\s*Nama Mata Kuliah\s*\|\s*SKS\s*\|\s*Tipe\s*\|\s*Semester\s*\|\s*Prasyarat\s*\|\s*Jalur Peminatan', line):
        # Tabel 1.4 Elektif
        new_lines.append("| No | Kode MK | Nama Mata Kuliah (Indonesia) | Course Name (English) | SKS | Tipe | Semester | Prasyarat | Jalur Peminatan |\n")
        continue
    elif re.search(r'\|\s*No\s*\|\s*Kode MK\s*\|\s*Nama Mata Kuliah\s*\|\s*SKS\s*\|\s*Tipe\s*\|\s*Semester\s*\|\s*Prasyarat\s*\|', line):
        # Tabel 1.2 FSTI & 1.3 Core
        new_lines.append("| No | Kode MK | Nama Mata Kuliah (Indonesia) | Course Name (English) | SKS | Tipe | Semester | Prasyarat |\n")
        continue
    elif re.search(r'\|\s*No\s*\|\s*Kode MK\s*\|\s*Nama Mata Kuliah\s*\|\s*SKS\s*\|\s*Tipe\s*\|\s*Kategori\s*\|\s*Prasyarat\s*\|', line):
        # Tabel Semester 1-8
        new_lines.append("| No | Kode MK | Nama Mata Kuliah (Indonesia) | Course Name (English) | SKS | Tipe | Kategori | Prasyarat |\n")
        continue
    elif re.search(r'\|\s*No\s*\|\s*Kode MK\s*\|\s*Nama Mata Kuliah\s*\|\s*SKS\s*\|\s*Tipe\s*\|\s*Semester\s*\|\s*Prasyarat Akademik\s*\|\s*Bahan Kajian Utama\s*\|', line):
        # Tabel 4.1, 4.2, 4.3 Peminatan
        new_lines.append("| No | Kode MK | Nama Mata Kuliah (Indonesia) | Course Name (English) | SKS | Tipe | Semester | Prasyarat Akademik | Bahan Kajian Utama |\n")
        continue

    # Separator rows
    if re.search(r'\|:---:\|:---:\|---\|:---:\|:---:\|:---:\|---\|---\|', line):
        # 8 columns -> 9 columns
        new_lines.append("|:---:|:---:|---|---|:---:|:---:|:---:|---|---|\n")
        continue
    elif re.search(r'\|:---:\|:---:\|---\|:---:\|:---:\|:---:\|---\|', line):
        # 7 columns -> 8 columns
        new_lines.append("|:---:|:---:|---|---|:---:|:---:|:---:|---|\n")
        continue

    # Total / Subtotal rows
    if "| **TOTAL** |" in line or "| **SUBTOTAL** |" in line:
        parts = [p.strip() for p in line.strip().split("|")[1:-1]]
        # If parts has column for Nama, expand it to 2 columns
        # Original 7 cols: [No, Kode, Nama, SKS, Tipe, Sem/Kat, Pra]
        # Original 8 cols: [No, Kode, Nama, SKS, Tipe, Sem, Pra, Cat/Jalur/BK]
        if len(parts) == 7:
            # expand after index 1
            new_parts = [parts[0], parts[1], parts[2], "—"] + parts[3:]
            new_lines.append("| " + " | ".join(new_parts) + " |\n")
            continue
        elif len(parts) == 8:
            new_parts = [parts[0], parts[1], parts[2], "—"] + parts[3:]
            new_lines.append("| " + " | ".join(new_parts) + " |\n")
            continue

    # Course rows
    # Check if line contains a course code: `([A-Z]{3}-\d{3})` or `(STA/B/C)` or `(\d+\.B)`
    m_code = re.search(r'\|\s*([\d\.]+(?:\.B)?)\s*\|\s*`([A-Z]{3}-\d{3}|STA/B/C)`\s*\|\s*([^|]+)\|(.*)', line)
    if m_code:
        no_str = m_code.group(1).strip()
        code = m_code.group(2).strip()
        name_orig = m_code.group(3).strip()
        rest = m_code.group(4)
        
        if code in courses:
            c = courses[code]
            name_id = c["nama_id"]
            name_en = f"*{c['nama_en']}*"
        elif code == "STA/B/C":
            name_id = name_orig
            if "Peminatan 1" in name_orig:
                name_en = "*Elective Specialization Course 1*"
            elif "Peminatan 2" in name_orig:
                name_en = "*Elective Specialization Course 2*"
            elif "Peminatan 3" in name_orig:
                name_en = "*Elective Specialization Course 3*"
            elif "Peminatan 4" in name_orig:
                name_en = "*Elective Specialization Course 4*"
            elif "Peminatan 5" in name_orig:
                name_en = "*Elective Specialization Course 5*"
            elif "Peminatan 6" in name_orig:
                name_en = "*Elective Specialization Course 6*"
            else:
                name_en = "*Elective Specialization Course*"
        else:
            name_id = name_orig
            name_en = f"*{name_orig}*"
            
        new_line = f"| {no_str} | `{code}` | {name_id} | {name_en} |{rest}\n"
        new_lines.append(new_line)
        continue

    new_lines.append(line)

out_path = path_005 + ".new"
with open(out_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Generated new Dokumen 005 at: {out_path}")
print(f"Total lines: {len(new_lines)}")
