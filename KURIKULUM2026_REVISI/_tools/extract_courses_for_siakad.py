# -*- coding: utf-8 -*-
"""
extract_courses_for_siakad.py
Mengekstrak 67 Mata Kuliah lengkap dari Dokumen 005 untuk kebutuhan input ke SIAKAD.
"""

import re
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
f005_path = os.path.join(base_dir, "..", "005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")

with open(f005_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

courses = []
seen_codes = set()

for line in lines:
    m = re.search(r'\|\s*\d+\s*\|\s*`([A-Z]{3}-\d{3})`\s*\|\s*([^|]+)\|\s*\*?([^|*]+)\*?\s*\|\s*(\d+)\s*\|\s*([^|]+)\|\s*(?:Sem\s*)?(\d+)\s*\|\s*([^|]+)\|', line)
    if m:
        code = m.group(1).strip()
        if code in seen_codes:
            continue
        seen_codes.add(code)
        
        name = m.group(2).strip()
        name_en = m.group(3).strip()
        sks = int(m.group(4).strip())
        tipe = m.group(5).strip()
        sem = int(m.group(6).strip())
        pra = m.group(7).strip()
        
        # Detail breakdown sks teori & praktik
        # Di Dok 005 tipe bisa: 'Teori', '+P' (Teori + Praktikum), 'Praktik', 'Proyek', 'Magang', 'Seminar', 'Mandiri'
        # Biasanya di SIAKAD:
        # Jika '+P' dengan 3 SKS -> Teori 2, Praktikum 1 (atau Teori 1, Praktikum 2)
        # Jika 'Praktik', 'Proyek', 'Magang', 'Seminar', 'Mandiri' -> SKS Praktikum
        sks_teori = sks
        sks_praktek = 0
        sks_lapangan = 0
        
        if tipe == "+P":
            if sks == 3:
                sks_teori = 2
                sks_praktek = 1
            elif sks == 2:
                sks_teori = 1
                sks_praktek = 1
            elif sks == 4:
                sks_teori = 3
                sks_praktek = 1
        elif tipe in ["Praktik", "Proyek", "Mandiri", "Seminar"]:
            sks_teori = 0
            sks_praktek = sks
        elif tipe in ["Magang"]:
            sks_teori = 0
            sks_praktek = 0
            sks_lapangan = sks
            
        if code.startswith("MKU-"):
            cat = "Wajib Umum"
            is_wajib = True
        elif code.startswith("FST-"):
            cat = "Wajib Fakultas"
            is_wajib = True
        elif code.startswith("STI-"):
            cat = "Wajib Inti Program Studi"
            is_wajib = True
        elif code.startswith("STA-"):
            cat = "Pilihan Peminatan P1 (Smart Systems)"
            is_wajib = False
        elif code.startswith("STB-"):
            cat = "Pilihan Peminatan P2 (Cloud & Cyber)"
            is_wajib = False
        elif code.startswith("STC-"):
            cat = "Pilihan Peminatan P3 (Digital Platform)"
            is_wajib = False
        else:
            cat = "Lainnya"
            is_wajib = True
            
        courses.append({
            "kode": code,
            "nama": name,
            "nama_en": name_en,
            "sks": sks,
            "sks_teori": sks_teori,
            "sks_praktek": sks_praktek,
            "sks_lapangan": sks_lapangan,
            "tipe": tipe,
            "semester": sem,
            "prasyarat": pra,
            "kategori": cat,
            "is_wajib": is_wajib,
            "sifat": "W" if is_wajib else "P"
        })

# Urutkan berdasarkan semester dan kode
courses.sort(key=lambda x: (x["semester"], not x["is_wajib"], x["kode"]))

out_json = os.path.join(base_dir, "kurikulum_2026_siakad_data.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(courses, f, indent=2, ensure_ascii=False)

print(f"Berhasil mengekstrak {len(courses)} Mata Kuliah!")
print(f"Tersimpan di: {out_json}")
