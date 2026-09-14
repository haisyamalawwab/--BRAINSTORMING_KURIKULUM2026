# -*- coding: utf-8 -*-
"""Verifikasi jumlah SKS tabel semester pada 045 md."""
import re, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.md")
txt = open(SRC, encoding="utf-8").read()
secs = re.split(r"(?=### Semester \d)", txt)[1:]
tot = 0
ok = True
for s in secs:
    m0 = re.match(r"### Semester (\d)[^\n]*?(\d+) SKS", s)
    sem = m0.group(1)
    klaim = int(m0.group(2))
    body = re.split(r"\n#{1,3} ", s, maxsplit=1)[0]
    baris = re.findall(r"^\| (\d+[^|]*)\|([^|]*)\|([^|]*)\| (\d+) \|", body, re.M)
    hitung = sum(int(b[3]) for b in baris)
    tot += hitung
    mark = "OK" if hitung == klaim else "SULIT"
    if hitung != klaim:
        ok = False
    print("Sem " + sem + ": baris=" + str(len(baris)) + " hitung=" + str(hitung) + " klaim=" + str(klaim) + " " + mark)
print("TOTAL=" + str(tot) + " (target 146) " + ("OK" if tot == 146 and ok else "CEK"))
