# -*- coding: utf-8 -*-
"""Generate Rencana 16 Pertemuan + Asesmen for 043 docs.
Assessment scheme per Dok 008:
  Teori:  Tugas1(20%) UTS(30%) Tugas2(20%) UAS(30%)
  +P:     Tugas1(20%) UTS(25%) Tugas2(25%) UAS(30%)
1-to-1 mapping: Tugas1→CPMK-1, UTS→CPMK-2, Tugas2→CPMK-3, UAS→CPMK-4 (or CPMK-3 for 3-CPMK courses)
"""
import re, os, sys, json, importlib

SCRIPT = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT)

mods = [importlib.import_module(f"_043_subcpmk_{n}") for n in ("s1","s23","s45","s67","p56","p7")]
SUBCPMK = {}
for m in mods:
    name = [x for x in dir(m) if x.startswith("SUBCPMK")][0]
    SUBCPMK.update(getattr(m, name))

mk_info = json.load(open(os.path.join(SCRIPT, "_043_mk_info.json"), encoding="utf-8"))

SEMESTER_MAP = {
    1: ["STI-101","STI-102","STI-103"],
    2: ["STI-204","STI-205"],
    3: ["STI-306","STI-307","STI-308","STI-309","STI-310","STI-311","STI-312"],
    4: ["STI-413","STI-414","STI-415","STI-416","STI-417","STI-418"],
    5: ["STI-519","STI-520","STI-521","STI-522","STI-523","STA-501","STB-501","STC-501"],
    6: ["STI-624","STI-625","STI-626","STI-627","STA-601","STA-602","STB-601","STB-602","STC-601","STC-602"],
    7: ["STI-728","STA-701","STA-702","STA-703","STB-701","STB-702","STB-703","STC-701","STC-702","STC-703"],
}

def derive_topik(sub_text):
    """Extract concise topic from Sub-CPMK competence text."""
    t = sub_text.strip()
    # Remove trailing period
    t = t.rstrip(".")
    # Truncate at first occurrence of limiting prepositions
    for cut in [" menggunakan ", " melalui ", " secara ", " dengan ", " pada ", " untuk ", " berdasarkan "]:
        idx = t.find(cut)
        if idx > 10:
            t = t[:idx]
    # If still long, truncate at comma
    if len(t) > 80:
        idx = t.find(",")
        if idx > 15:
            t = t[:idx]
    # Capitalize first letter
    if t:
        t = t[0].upper() + t[1:]
    return t

def get_weights(tipe):
    if tipe == "+P":
        return {"t1":"20%","uts":"25%","t2":"25%","uas":"30%"}
    return {"t1":"20%","uts":"30%","t2":"20%","uas":"30%"}

def get_metode(tipe, is_assessment=False):
    if is_assessment:
        return "Ujian" if tipe == "Teori" else "Ujian Praktikum"
    if tipe == "+P":
        return "Praktikum / PjBL"
    return "Kuliah Interaktif / Diskusi"

def gen_16weeks(code):
    subs = SUBCPMK[code]
    tipe = mk_info.get(code, {}).get("tipe", "Teori")
    sks = mk_info.get(code, {}).get("sks", 3)
    w = get_weights(tipe)
    
    # Group sub-CPMK by parent CPMK
    cpmk_groups = {}
    for sub, txt, src, bloom in subs:
        cpmk_groups.setdefault(int(src), []).append((sub, txt, bloom))
    cpmk_count = len(cpmk_groups)
    cpmk_nums = sorted(cpmk_groups.keys())
    
    rows = []
    
    def add(pekan, topik, subcpmk, metode, asesmen):
        rows.append((pekan, topik, subcpmk, metode, asesmen))
    
    # Pekan 1: Intro
    add(1, "Pengantar MK & Kontrak Belajar", "—", "Kuliah Interaktif", "—")
    
    if cpmk_count == 4:
        # 4 CPMK template: Tugas1→CPMK-1, UTS→CPMK-2, Tugas2→CPMK-3, UAS→CPMK-4
        subs1 = cpmk_groups[1]
        subs2 = cpmk_groups[2]
        subs3 = cpmk_groups[3]
        subs4 = cpmk_groups[4]
        
        add(2, derive_topik(subs1[0][1]), f"Sub-CPMK-{subs1[0][0]}", get_metode(tipe), "—")
        add(3, derive_topik(subs1[1][1]), f"Sub-CPMK-{subs1[1][0]}", get_metode(tipe), "—")
        add(4, f"Tugas 1: Evaluasi {subs1[0][0]} & {subs1[1][0]}", f"Sub-CPMK-{subs1[0][0]}, Sub-CPMK-{subs1[1][0]}", "Workshop / Latihan Soal", f"**Tugas 1** ({w['t1']})")
        add(5, derive_topik(subs2[0][1]), f"Sub-CPMK-{subs2[0][0]}", get_metode(tipe), "—")
        add(6, derive_topik(subs2[1][1]), f"Sub-CPMK-{subs2[1][0]}", get_metode(tipe), "—")
        add(7, "Review & Latihan Soal CPMK-2", "CPMK-2", "Diskusi / Latihan", "—")
        add(8, "Ujian Tengah Semester", "CPMK-2", get_metode(tipe, True), f"**UTS** ({w['uts']})")
        add(9, derive_topik(subs3[0][1]), f"Sub-CPMK-{subs3[0][0]}", get_metode(tipe), "—")
        add(10, derive_topik(subs3[1][1]), f"Sub-CPMK-{subs3[1][0]}", get_metode(tipe), "—")
        add(11, "Studi Kasus / Proyek Terapan CPMK-3", "CPMK-3", "PjBL / Case Method", "—")
        add(12, f"Tugas 2: Evaluasi {subs3[0][0]} & {subs3[1][0]}", f"Sub-CPMK-{subs3[0][0]}, Sub-CPMK-{subs3[1][0]}", "Workshop / Latihan Soal", f"**Tugas 2** ({w['t2']})")
        add(13, derive_topik(subs4[0][1]), f"Sub-CPMK-{subs4[0][0]}", get_metode(tipe), "—")
        add(14, derive_topik(subs4[1][1]), f"Sub-CPMK-{subs4[1][0]}", get_metode(tipe), "—")
        add(15, "Review & Konsultasi UAS", "CPMK-4", "Diskusi / Konsultasi", "—")
        add(16, "UAS / Tugas Akhir / Proyek", "CPMK-4", "Ujian / Proyek Akhir", f"**UAS** ({w['uas']})")
    
    elif cpmk_count == 3:
        # 3 CPMK template: Tugas1→CPMK-1, UTS→CPMK-2, Tugas2→CPMK-3, UAS→CPMK-3
        subs1 = cpmk_groups[1]
        subs2 = cpmk_groups[2]
        subs3 = cpmk_groups[3]
        
        add(2, derive_topik(subs1[0][1]), f"Sub-CPMK-{subs1[0][0]}", get_metode(tipe), "—")
        add(3, derive_topik(subs1[1][1]), f"Sub-CPMK-{subs1[1][0]}", get_metode(tipe), "—")
        add(4, f"Tugas 1: Evaluasi {subs1[0][0]} & {subs1[1][0]}", f"Sub-CPMK-{subs1[0][0]}, Sub-CPMK-{subs1[1][0]}", "Workshop / Latihan Soal", f"**Tugas 1** ({w['t1']})")
        add(5, derive_topik(subs2[0][1]), f"Sub-CPMK-{subs2[0][0]}", get_metode(tipe), "—")
        add(6, derive_topik(subs2[1][1]), f"Sub-CPMK-{subs2[1][0]}", get_metode(tipe), "—")
        add(7, "Review & Latihan Soal CPMK-2", "CPMK-2", "Diskusi / Latihan", "—")
        add(8, "Ujian Tengah Semester", "CPMK-2", get_metode(tipe, True), f"**UTS** ({w['uts']})")
        add(9, derive_topik(subs3[0][1]), f"Sub-CPMK-{subs3[0][0]}", get_metode(tipe), "—")
        add(10, derive_topik(subs3[1][1]), f"Sub-CPMK-{subs3[1][0]}", get_metode(tipe), "—")
        add(11, "Studi Kasus / Proyek Terapan CPMK-3", "CPMK-3", "PjBL / Case Method", "—")
        add(12, f"Tugas 2: Evaluasi {subs3[0][0]} & {subs3[1][0]}", f"Sub-CPMK-{subs3[0][0]}, Sub-CPMK-{subs3[1][0]}", "Workshop / Latihan Soal", f"**Tugas 2** ({w['t2']})")
        add(13, "Proyek / Tugas Akhir Terapan", "Seluruh CPMK", "PjBL", "—")
        add(14, "Penyempurnaan Proyek / Portofolio", "Seluruh CPMK", "PjBL / Diskusi", "—")
        add(15, "Presentasi & Review", "Seluruh CPMK", "Presentasi", "—")
        add(16, "UAS / Tugas Akhir / Proyek", "CPMK-3", "Ujian / Proyek Akhir", f"**UAS** ({w['uas']})")
    
    return rows

def render_rps_block(code):
    rows = gen_16weeks(code)
    tipe = mk_info.get(code, {}).get("tipe", "Teori")
    sks = mk_info.get(code, {}).get("sks", 3)
    L = [f"**Rencana 16 Pertemuan & Asesmen** ({sks} SKS, {tipe}):", "",
         "| Pekan | Topik Pembelajaran | Sub-CPMK Terkait | Metode | Asesmen |",
         "|:---:|---|:---:|---|:---:|"]
    for pekan, topik, subcpmk, metode, asesmen in rows:
        L.append(f"| {pekan} | {topik} | {subcpmk} | {metode} | {asesmen} |")
    return "\n".join(L) + "\n\n"

def inject(path, heading_pat, anchor_pat, codes):
    s = open(path, encoding="utf-8").read()
    changed = 0
    for code in codes:
        if code not in SUBCPMK:
            continue
        hm = re.search(heading_pat.format(code=re.escape(code)), s)
        if not hm:
            print(f"  !! heading not found: {code}")
            continue
        gm = re.search(anchor_pat, s[hm.end():])
        if not gm:
            print(f"  !! anchor not found: {code}")
            continue
        pos = hm.end() + gm.start()
        if "Rencana 16 Pertemuan" in s[hm.start():pos]:
            print(f"  [skip] {code} already has RPS")
            continue
        block = render_rps_block(code)
        s = s[:pos] + block + s[pos:]
        changed += 1
    open(path, "w", encoding="utf-8").write(s)
    return changed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gen_043_rps_semester.py <semester_number>")
        sys.exit(1)
    sem = int(sys.argv[1])
    codes = SEMESTER_MAP.get(sem)
    if not codes:
        print(f"Invalid semester: {sem}"); sys.exit(1)
    
    per = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md")
    dan = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md")
    
    print(f"Semester {sem}: {', '.join(codes)}")
    c1 = inject(per, r"\n### \d+\. {code} \u2014 ", r"\*\*Boundary Guardrails\*\*", codes)
    c2 = inject(dan, r"\n#### {code} \u2014 ", r"\*\*Boundary Guardrails:\*\*", codes)
    print(f"PER_SEMESTER: {c1}/{len(codes)} | DAN_BOUNDARY: {c2}/{len(codes)}")
