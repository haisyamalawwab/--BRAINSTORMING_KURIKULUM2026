# -*- coding: utf-8 -*-
"""T5 Verifikasi Terprogram Independen — RPS STI-311 Pengembangan Web Front End.

4 kelompok cek (master prompt 053 T5):
  1. Zero residual  : 0 dari 18 tag {{...}} + 0 dari 25 tag [...] (kamus Dok 052).
  2. Audit posisi   : isi sel kunci tabel identitas, 16 pekan, lampiran + nested rubrik.
  3. Konsistensi    : identitas = Dok 005; CPMK/Sub-CPMK verbatim = Dok 043 baris 633-686;
                      jangkar asesmen Pekan 4/8/12/16; bobot total 100%; CPMK-CPL = Dok 043.
  4. Cek sampah     : tanpa "TEKNIK MESIN", tanpa LaTeX $...$, tanpa literal \n mentah.

Catatan struktur aktual (hasil dump):
  - Tabel 1: R0 header (3 sel unik; teks institusi di sel ke-2), R3 identitas 7 kolom,
    R5 otorisasi, R7-R8 CPL, R14-R17 CPMK, R21-R28 Sub-CPMK (5 + 3 klon),
    R30 kolerasi (nested table di sel terakhir), R31 deskripsi, R32 bahan kajian,
    R34/R36 pustaka, R37 dosen pengampu, R38 prasyarat.
  - Tabel 2: R3-R9 pekan 1-7, R10 UTS (merge), R11-R17 pekan 9-15, R18 UAS, R19 total.
    Nomor pekan ada di sel pertama tiap baris — dipakai sebagai kunci pencarian.
"""
import os
import re
import sys

from docx import Document
from docx.oxml.ns import qn

WORKDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DOCX = os.path.join(WORKDIR, "DOCX", "RPS_STI-311_Web_Front_End_Development.docx")

SCALAR_TAGS = [
    "{{namamk}}", "{{kodemk}}", "{{rumpunmk}}", "{{skst}}", "{{sksp}}", "{{sms}}",
    "{{tglsusun}}", "{{kodeprodi}}", "{{pengembangrps}}", "{{koordinatormk}}",
    "{{ketuaprodi}}", "{{prodi}}", "{{namadosen}}", "{{nuptk}}", "{{dosenpengampu}}",
    "{{mkprasyarat}}", "{{deskripsimk}}", "{{bahankajian}}",
]
BLOCK_TAGS = [
    "[bobot_nilai]", "[cpl]", "[cpmk]", "[daring]", "[indikator]", "[kemampuan_subcpmk]",
    "[kriteriateknik]", "[luring]", "[materi]", "[mingguke]", "[nocpl]", "[nocpmk]",
    "[nosubcpmk]", "[penugasan1]", "[pustakapendukung]", "[pustakautama]", "[rubriktugas1]",
    "[rubriktugas2]", "[rubrikuas]", "[rubrikuts]", "[soaluas]", "[soaluts]", "[subcpmk]",
    "[tabelkolerasi]", "[tugas2]",
]

CPMK_043 = [
    "Mahasiswa (A) mampu membangun struktur halaman web responsif multi-device (B) menggunakan HTML5 Semantik, CSS3 Flexbox/Grid, dan Variabel CSS (C) dengan tampilan estetik (D).",
    "Mahasiswa (A) mampu mengimplementasikan logika interaktivitas client-side (B) menggunakan JavaScript Modern (ES6+, DOM Manipulation, Async/Await, Fetch API) (C) secara modular (D).",
    "Mahasiswa (A) mampu membangun aplikasi Single Page Application (SPA) berbasis komponen (B) menggunakan framework React.js (Hooks, Context API, React Router) (C) dengan arsitektur state terpusat (D).",
    "Mahasiswa (A) mampu mengintegrasikan aplikasi front-end dengan RESTful API eksternal (B) serta mengoptimalkan performa loading (C) dengan skor Google Lighthouse ≥ 85 (D).",
]
SUBCPMK_043 = [
    "Membangun struktur halaman web responsif menggunakan HTML5 semantik.",
    "Mengimplementasikan tata letak responsif menggunakan CSS3 Flexbox, Grid, dan variabel CSS.",
    "Mengimplementasikan interaktivitas client-side menggunakan JavaScript ES6+ (DOM, Async/Await).",
    "Mengelola state dan komunikasi data menggunakan Fetch API secara modular.",
    "Membangun Single Page Application berbasis komponen menggunakan React (Hooks, Context API).",
    "Mengimplementasikan routing antar halaman pada aplikasi SPA.",
    "Mengintegrasikan front-end dengan RESTful API eksternal.",
    "Mengoptimalkan performa loading aplikasi dengan skor Google Lighthouse minimal 85.",
]
CPL_003 = {
    "P4": "Menguasai prinsip rekayasa perangkat lunak modern (web, mobile, distributed), manajemen basis data relasional/NoSQL, rekayasa data & visualisasi, serta prinsip desain interaksi pengalaman pengguna (UI/UX).",
    "KK5": "Mampu merancang pengalaman pengguna berbasis riset (UI/UX) serta merekayasa platform digital modern yang skalabel (Microservices, Web/Mobile, API, SaaS, BPA).",
}


def norm(s):
    s = s.replace("$\\ge", "≥").replace("$", "")
    return re.sub(r"\s+", " ", s).strip()


def uniq_cells(row):
    seen, out = set(), []
    for c in row.cells:
        if id(c._tc) in seen:
            continue
        seen.add(id(c._tc))
        out.append(c)
    return out


def row_text(row):
    """Seluruh teks sel unik sebuah baris, termasuk tabel nested di dalamnya."""
    parts = []
    for c in uniq_cells(row):
        parts.append(c.text)
        for nt in c.tables:
            for nrow in nt.rows:
                for nc in uniq_cells(nrow):
                    parts.append(nc.text)
    return norm("\n".join(parts))


def cell_with_text(row, needle):
    for c in uniq_cells(row):
        if needle in c.text:
            return c
    return None


def main():
    doc = Document(OUT_DOCX)
    t1, t2 = doc.tables[1], doc.tables[2]
    fails = []

    def check(label, ok):
        print(f"  {label}: {'LULUS' if ok else 'GAGAL'}")
        if not ok:
            fails.append(label)

    # teks menyeluruh (paragraf body + seluruh sel + nested)
    def collect_blob(container):
        parts = [p.text for p in container.paragraphs]
        for t in container.tables:
            for row in t.rows:
                for c in uniq_cells(row):
                    parts.append(c.text)
                    parts.extend(p.text for p in c.paragraphs)
                    for nt in c.tables:
                        for nrow in nt.rows:
                            for nc in uniq_cells(nrow):
                                parts.append(nc.text)
        return "\n".join(parts)

    blob = collect_blob(doc)

    print("=" * 72)
    print("T5 VERIFIKASI TERPROGRAM INDEPENDEN — RPS STI-311")
    print(f"File: {os.path.basename(OUT_DOCX)} | Jumlah tabel: {len(doc.tables)}")
    print("=" * 72)

    # ---------------------------------------------------------- CEK 1: residual
    print("\n[CEK 1] ZERO RESIDUAL (18 scalar + 25 blok, kamus Dok 052)")
    residual = [tag for tag in SCALAR_TAGS + BLOCK_TAGS if tag in blob]
    residual += [m + " (tak dikenal)" for m in re.findall(r"\{\{[^}]+\}\}", blob)
                 if m not in SCALAR_TAGS]
    check(f"Tag tersisa = {len(residual)}", not residual)
    if residual:
        print(f"    Residual: {residual}")

    # ---------------------------------------------------------- CEK 2: posisi
    print("\n[CEK 2] AUDIT POSISI SEL KUNCI")
    rows1 = list(t1.rows)
    rows2 = list(t2.rows)

    check("Header R0 = FSTI + S1 SISTEM DAN TEKNOLOGI INFORMASI",
          "FAKULTAS SAINS DAN TEKNOLOGI INFORMASI" in row_text(rows1[0]) and
          "PROGRAM STUDI S1 SISTEM DAN TEKNOLOGI INFORMASI" in row_text(rows1[0]))

    id_text = row_text(rows1[3]) + " " + row_text(rows1[5])
    for expect in ["Pengembangan Web Front End (Web Front End Development)", "STI-311",
                   "T= 2", "P= 1", "3 (Ganjil)", "30 September 2026",
                   "Tim KBK Rekayasa Perangkat Lunak & Platform",
                   "Dr. Roni Wahyu, S.Kom., M.T."]:
        check(f"Identitas memuat '{expect}'", expect in id_text)
    check("Kode prodi di header R0 memuat 'B4.5.2.RPS-STI311'",
          "B4.5.2.RPS-STI311" in row_text(rows1[0]))

    # CPL R7-R8, CPMK R14-R17, Sub-CPMK R21-R28 — cari di seluruh sel baris
    for code, text in CPL_003.items():
        found = any(norm(text) in row_text(r) and code in row_text(r)
                    for r in rows1[7:13])
        check(f"CPL {code} verbatim Dok 003", found)
    for i, expect in enumerate(CPMK_043, 1):
        found = any(f"CPMK-{i}" in row_text(r) and norm(expect) in row_text(r)
                    for r in rows1[13:20])
        check(f"CPMK-{i} verbatim Dok 043", found)
    for i, expect in enumerate(SUBCPMK_043, 1):
        found = any(norm(expect) in row_text(r) for r in rows1[20:29])
        check(f"Sub-CPMK #{i} verbatim Dok 043", found)

    kol_cell = cell_with_text(rows1[30], "Matriks Korelasi")
    check("Baris 30 memuat [tabelkolerasi] (label + nested)",
          kol_cell is not None and len(kol_cell.tables) == 1)
    kol_text = row_text(rows1[30])
    for expect in ["P4", "KK5", "Tugas 1 (20%) + UTS (25%) = 45%",
                   "Tugas 2 (25%) + UAS (30%) = 55%", "total 100%"]:
        check(f"Kolerasi memuat '{expect}'", expect in kol_text)

    for idx, label, expect in [
        (31, "deskripsimk", "STI-311"),
        (32, "bahankajian", "BK-IS12"),
        (34, "pustakautama", "Duckett"),
        (36, "pustakapendukung", "Eloquent JavaScript"),
        (37, "dosenpengampu", "[Nama Dosen Pengampu 1]"),
        (38, "mkprasyarat", "FST-102"),
    ]:
        check(f"Baris {idx} ({label}) memuat '{expect}'", expect in row_text(rows1[idx]))

    # tabel 16 pekan: petakan nomor Mg dari sel pertama
    week_rows = {}
    for r in rows2:
        first = uniq_cells(r)[0].text.strip()
        if first.isdigit():
            week_rows[int(first)] = r
    check("16 baris pekan lengkap (1-16)", sorted(week_rows) == list(range(1, 17)))
    week_expect = {
        1: "Pengantar Web Frontend", 4: "JavaScript Modern: ES6+",
        7: "Pengantar React.js", 9: "React Hooks Fundamental",
        12: "REST API Integration", 13: "Form Management",
        14: "Web Performance", 15: "Production Build",
        8: "Evaluasi Tengah Semester (UTS)", 16: "Evaluasi Akhir Semester (UAS)",
    }
    for mg, expect in sorted(week_expect.items()):
        check(f"Pekan {mg} memuat '{expect}'", expect in row_text(week_rows[mg]))
    check("Baris total memuat '100%'", "100%" in row_text(rows2[-1]))

    print("  Lampiran (tabel 3-10):")
    lamp_expect = {
        3: ("TUGAS 1 — MILESTONE PROYEK 1", 0), 4: ("Rubrik Penilaian Tugas 1", 1),
        5: ("UJIAN TENGAH SEMESTER", 0), 6: ("Rubrik Penilaian UTS", 1),
        7: ("TUGAS 2 — MILESTONE PROYEK 2", 0), 8: ("Rubrik Penilaian Tugas 2", 1),
        9: ("UJIAN AKHIR SEMESTER", 0), 10: ("Rubrik Penilaian UAS", 1),
    }
    for ti, (expect, nnested) in lamp_expect.items():
        cell0 = doc.tables[ti].rows[0].cells[0]
        check(f"Tabel {ti} memuat '{expect}' (nested={nnested})",
              expect in cell0.text and len(cell0.tables) == nnested)

    # ---------------------------------------------------------- CEK 3: konsistensi
    print("\n[CEK 3] KONSISTENSI SILANG SUMBER")
    check("Jangkar Pekan 4 = Tugas 1 20%",
          "Tugas 1" in row_text(week_rows[4]) and "20%" in row_text(week_rows[4]))
    check("Jangkar Pekan 8 = UTS 25%",
          "UTS" in row_text(week_rows[8]) and "25%" in row_text(week_rows[8]))
    check("Jangkar Pekan 12 = Tugas 2 25%",
          "Tugas 2" in row_text(week_rows[12]) and "25%" in row_text(week_rows[12]))
    check("Jangkar Pekan 16 = UAS 30%",
          "UAS" in row_text(week_rows[16]) and "30%" in row_text(week_rows[16]))
    # struktur fisik baris UTS/UAS: [0]=Mg, [1]=sel merge lebar (label + isi berlabel),
    # [2]=kolom bobot sempit berisi ringkasan — isi panjang TIDAK boleh di kolom sempit.
    for mg, label, bobot in [
        (8, "Evaluasi Tengah Semester (UTS)", "UTS 25%"),
        (16, "Evaluasi Akhir Semester (UAS)", "UAS 30%"),
    ]:
        cells = uniq_cells(week_rows[mg])
        ok = (len(cells) == 3
              and label in cells[1].text and "Indikator:" in cells[1].text
              and cells[2].text.strip() == bobot
              and "Indikator" not in cells[2].text)
        check(f"Struktur sel baris pekan {mg} (merge lebar + bobot ringkas '{bobot}')", ok)
    check("Total bobot = 100%", "100%" in row_text(rows2[-1]))
    check("Skema 4x tipe +P (UTS 25%, T2 25%) per Dok 008",
          "25%" in row_text(week_rows[8]) and "25%" in row_text(week_rows[12]))

    nkol = kol_cell.tables[0]
    grid = [[norm(c.text) for c in uniq_cells(r)] for r in nkol.rows]
    p4row = next((r for r in grid if r and r[0] == "P4"), None)
    kk5row = next((r for r in grid if r and r[0] == "KK5"), None)
    check("CPMK↔CPL (P4→CPMK-1,2; KK5→CPMK-3,4) sesuai Dok 043",
          bool(p4row and p4row[1] == "✓" and p4row[2] == "✓" and p4row[3] == "" and
               kk5row and kk5row[3] == "✓" and kk5row[4] == "✓"))
    check("Handoff anchor STI-416 tercantum (Dok 043)", "STI-416" in blob)

    # ---------------------------------------------------------- CEK 4: sampah
    print("\n[CEK 4] CEK SAMPAH")
    for label, pattern in [
        ("Tanpa 'TEKNIK MESIN'", r"teknik mesin"),
        ("Tanpa residue LaTeX $...$", r"\$\\?[a-z]"),
        ("Tanpa literal '\\n' mentah", r"\\n"),
        ("Tanpa tag mentah {{...}}", r"\{\{"),
    ]:
        hit = re.search(pattern, blob)
        check(label, hit is None)

    placeholders = sorted(set(re.findall(r"\[Nama [^\]]+\]|\[NUPTK[^\]]*\]", blob)))
    print("  Placeholder terdokumentasi (diizinkan → Daftar Butir Konfirmasi):")
    for ph in placeholders:
        print(f"    - {ph}")

    # ---------------------------------------------------------- CEK 5: layout
    print("\n[CEK 5] LAYOUT (perapian dokumen)")
    th_rows, cs_missing = [], []
    for ri, tr in enumerate(t2._tbl.findall(qn("w:tr"))):
        trpr = tr.find(qn("w:trPr"))
        has_hdr = trpr is not None and trpr.find(qn("w:tblHeader")) is not None
        has_cs = trpr is not None and trpr.find(qn("w:cantSplit")) is not None
        if has_hdr:
            th_rows.append(ri)
        if ri >= 3 and not has_cs:
            cs_missing.append(ri)
    check(f"Tabel 2 tblHeader hanya baris 0-2 (aktual {th_rows})", th_rows == [0, 1, 2])
    check("Tabel 2 cantSplit semua baris data", not cs_missing)

    def rubric_layout(tbl):
        tblpr = tbl._tbl.tblPr
        layout = tblpr.find(qn("w:tblLayout"))
        grid = tbl._tbl.find(qn("w:tblGrid"))
        wsum = sum(int(gc.get(qn("w:w"))) for gc in grid.findall(qn("w:gridCol")))
        all_cs = all(
            r.find(qn("w:trPr")) is not None
            and r.find(qn("w:trPr")).find(qn("w:cantSplit")) is not None
            for r in tbl._tbl.findall(qn("w:tr"))
        )
        szs = {s.get(qn("w:val")) for s in tbl._tbl.iter(qn("w:sz"))}
        return (layout is not None and layout.get(qn("w:type")) == "fixed",
                wsum, all_cs, szs)

    for ti in (4, 6, 8, 10):
        nt = doc.tables[ti].rows[0].cells[0].tables[0]
        fixed, wsum, all_cs, szs = rubric_layout(nt)
        ok = fixed and 8490 <= wsum <= 8504 and all_cs and "18" in szs
        check(f"Nested rubrik tabel {ti}: fixed={fixed}, lebar={wsum}, "
              f"cantSplit={all_cs}, font9pt={'18' in szs}", ok)

    kn_flags = []
    for ri in (33, 35):
        for c in uniq_cells(rows1[ri]):
            kn_flags.extend(bool(p.paragraph_format.keep_with_next)
                            for p in c.paragraphs)
    check("Keep-with-next label Pustaka (baris 33 & 35)", kn_flags and all(kn_flags))

    print("\n" + "=" * 72)
    if fails:
        print(f"HASIL: GAGAL — {len(fails)} temuan:")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("HASIL: SELURUH 4 KELOMPOK CEK LULUS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
