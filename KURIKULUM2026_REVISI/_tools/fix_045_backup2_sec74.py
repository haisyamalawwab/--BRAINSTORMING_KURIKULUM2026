# -*- coding: utf-8 -*-
"""BACKUP2: salin HTML 045 utama -> BACKUP2, rapikan §7.4 (paragraf Kelompok -> tabel formal).
Output: HTML/045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX-BACKUP2.html
"""
import re, html as ihtml, os, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "HTML", "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX.html")
DST = os.path.join(BASE, "HTML", "045_DRAFT_BUKU_KPT_SISTEKIN_2026_MENGIKUTI_TEMPLATE_DOCX-BACKUP2.html")

JENIS_KEYS = ["+Praktik", "+P", "Proyek", "Magang", "Mandiri", "Seminar", "Elektif", "Praktik", "Teori"]

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
    """ -> (rows, notes, jalur_marks). rows: (kode, nama, sks, sem, jenis, ket, jalur)"""
    rows, notes = [], []
    jalur = ""
    # normalisasi batas antar-jalur & kalimat ekor agar split ';' bersih
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

def esc(s):
    return ihtml.escape(s, quote=False)

def build_table(caption, headers, rows, total_sks=None):
    o = [f"<div class=\"kpt-cap\">{esc(caption)}</div>", "<table><thead><tr>"]
    o += [f"<th>{esc(h)}</th>" for h in headers]
    o += ["</tr></thead><tbody>"]
    last_j = None
    for r in rows:
        if len(r) == 7 and r[6] and r[6] != last_j:
            last_j = r[6]
            o.append(f"<tr><td colspan=\"{len(headers)}\"><strong>{esc(jalur_name(last_j))}</strong></td></tr>")
        cells = r[:len(headers)]
        o.append("<tr>" + "".join(f"<td>{esc(str(c))}</td>" for c in cells) + "</tr>")
    if total_sks is not None:
        o.append(f"<tr><td></td><td><strong>Total</strong></td><td><strong>{total_sks}</strong></td>"
                 + "<td></td>" * (len(headers) - 3) + "</tr>")
    o += ["</tbody></table>"]
    return "\n".join(o)

def jalur_name(j):
    return {"P1": "P1 — Integrated Smart Systems", "P2": "P2 — Cloud Infrastructure & Cybersecurity",
            "P3": "P3 — Digital Platform Engineering"}.get(j, j)

def main():
    shutil.copyfile(SRC, DST)
    p = open(DST, encoding="utf-8").read()
    pat = re.compile(r"<p>Kelompok (MKWU|FSTI|Core STI|Elektif) \((.*?)</p>", re.DOTALL)
    n = [0]
    def repl(m):
        kel, inner = m.group(1), m.group(2)
        text = ihtml.unescape(inner)
        # buang klaim "(8 MK / 13 SKS): ..." -> ambil dari ':' pertama
        _, _, body = text.partition(":")
        rows, notes = parse_items(body if body else text)
        if not rows:
            return m.group(0)
        n[0] += 1
        tot = sum(r[2] for r in rows)
        print(f"[{kel}] baris={len(rows)} total_sks={tot}")
        heads = ["No", "Kode MK", "Mata Kuliah", "SKS", "Semester", "Jenis", "Prasyarat / Keterangan"]
        numbered = [(i + 1,) + r[:6] for i, r in enumerate(rows)]
        # sisipkan info jalur ke kolom keterangan utk elektif
        if kel == "Elektif":
            numbered = [(a, b, c, d, e, f, g) for (a, b, c, d, e, f, g) in
                        [(i + 1, r[0], r[1], r[2], r[3], r[4], (r[6] + " | " + r[5]).strip(" |")) for i, r in enumerate(rows)]]
            tbl = build_table(f"Tabel 7.4f — Kelompok Elektif / Peminatan (18 ditawarkan; ditempuh 6 MK / 18 SKS, satu jalur penuh)",
                              heads, numbered)
        else:
            cap = {"MKWU": "Tabel 7.4c — Kelompok Mata Kuliah Wajib Universitas (8 MK / 13 SKS)",
                   "FSTI": "Tabel 7.4d — Kelompok Mata Kuliah Wajib Fakultas (13 MK / 36 SKS)",
                   "Core STI": "Tabel 7.4e — Kelompok Mata Kuliah Inti Prodi (28 MK / 79 SKS)"}[kel]
            tbl = build_table(cap, heads, numbered, total_sks=tot)
        note = "".join(f"<p>{esc(x)}</p>" for x in notes)
        return tbl + note
    p2 = pat.sub(repl, p)
    open(DST, "w", encoding="utf-8").write(p2)
    print(f"[SUKSES] {DST} ({os.path.getsize(DST):,} bytes, {n[0]} paragraf -> tabel)")

if __name__ == "__main__":
    main()
