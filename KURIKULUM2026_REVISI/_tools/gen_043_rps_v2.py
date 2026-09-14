# -*- coding: utf-8 -*-
"""RPS v2: 7-column table, Tugas 1/2 integrated into Sub-CPMK rows.
Columns: Pekan | Sub-CPMK | Topik Pembelajaran | Kompetensi/Keterangan (ABCD) | Metode | Jam | Asesmen
Assessment: Tugas1→Pekan4 (integrated, evaluates Pekan 2-3), UTS→Pekan8,
            Tugas2→Pekan12 (integrated, evaluates Pekan 9-11), UAS→Pekan16.
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
    t = sub_text.strip().rstrip(".")
    for cut in [" menggunakan "," melalui "," secara "," dengan "," pada "," untuk "," berdasarkan "]:
        idx = t.find(cut)
        if idx > 10: t = t[:idx]
    if len(t) > 80:
        idx = t.find(",")
        if idx > 15: t = t[:idx]
    return t[0].upper() + t[1:] if t else t

def kompetensi_abcd(sub_text, cpmk_num):
    """Brief ABCD competency from Sub-CPMK text."""
    return f"Mahasiswa (*A*) mampu {sub_text[0].lower() + sub_text[1:].rstrip('.')} (*B*) melalui pembelajaran terstruktur (*C*) secara tepat dan terukur (*D*). Selaras CPMK-{cpmk_num}."

def get_weights(tipe):
    return {"t1":"20%","uts":"25%","t2":"25%","uas":"30%"} if tipe=="+P" else {"t1":"20%","uts":"30%","t2":"20%","uas":"30%"}

def jam(sks): return f"{sks*50}'"

def gen_16weeks(code):
    subs = SUBCPMK[code]
    info = mk_info.get(code, {})
    tipe = info.get("tipe","Teori")
    sks = info.get("sks",3)
    w = get_weights(tipe)
    J = jam(sks)
    
    groups = {}
    for sub, txt, src, bloom in subs:
        groups.setdefault(int(src), []).append((sub, txt, bloom))
    n_cpmk = len(groups)
    
    rows = []
    def R(pekan, subcpmk, topik, komp, metode, asesmen):
        rows.append((pekan, subcpmk, topik, komp, metode, J, asesmen))
    
    # Pekan 1: Intro
    R(1, "—", "Pengantar MK, Kontrak Belajar & Orientasi",
      "Mahasiswa (*A*) memahami ruang lingkup MK, capaian pembelajaran, dan skema asesmen (*B*) melalui penjelasan dosen (*C*) secara jelas (*D*).",
      "Kuliah Interaktif", "—")
    
    if n_cpmk == 4:
        s1, s2, s3, s4 = groups[1], groups[2], groups[3], groups[4]
        # Pekan 2-3: CPMK-1
        R(2, f"Sub-{s1[0][0]}", derive_topik(s1[0][1]), kompetensi_abcd(s1[0][1],1),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        R(3, f"Sub-{s1[1][0]}", derive_topik(s1[1][1]), kompetensi_abcd(s1[1][1],1),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        # Pekan 4: CPMK-2 start + Tugas 1 (evaluates Pekan 2-3)
        R(4, f"Sub-{s2[0][0]}", derive_topik(s2[0][1]), kompetensi_abcd(s2[0][1],2),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL",
          f"**Tugas 1** ({w['t1']}) — evaluasi Sub-CPMK Pekan 2–3")
        # Pekan 5-7: CPMK-2 finish + CPMK-3
        R(5, f"Sub-{s2[1][0]}", derive_topik(s2[1][1]), kompetensi_abcd(s2[1][1],2),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        R(6, f"Sub-{s3[0][0]}", derive_topik(s3[0][1]), kompetensi_abcd(s3[0][1],3),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        R(7, f"Sub-{s3[1][0]}", derive_topik(s3[1][1]), kompetensi_abcd(s3[1][1],3),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        # Pekan 8: UTS
        R(8, "CPMK-1 s.d. 3", "**Ujian Tengah Semester (UTS)**",
          "Mahasiswa (*A*) mendemonstrasikan penguasaan CPMK-1 s.d. CPMK-3 (*B*) melalui ujian tertulis/praktikum (*C*) dengan kriteria ketuntasan minimal (*D*).",
          "Ujian" if tipe=="Teori" else "Ujian Praktikum", f"**UTS** ({w['uts']})")
        # Pekan 9-10: CPMK-4
        R(9, f"Sub-{s4[0][0]}", derive_topik(s4[0][1]), kompetensi_abcd(s4[0][1],4),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        R(10, f"Sub-{s4[1][0]}", derive_topik(s4[1][1]), kompetensi_abcd(s4[1][1],4),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        # Pekan 11: Studi kasus
        R(11, "CPMK-3, CPMK-4", "Studi Kasus / Proyek Terapan",
          "Mahasiswa (*A*) menerapkan CPMK-3 dan CPMK-4 (*B*) pada studi kasus/proyek nyata (*C*) secara kolaboratif dan terukur (*D*).",
          "PjBL / Case Method", "—")
        # Pekan 12: Proyek lanjut + Tugas 2 (evaluates Pekan 9-11)
        R(12, "CPMK-4", "Proyek Terapan Lanjut & Presentasi Antara",
          "Mahasiswa (*A*) menyajikan progres proyek/tugas akhir (*B*) dalam forum kelas (*C*) dengan argumen yang valid (*D*).",
          "PjBL / Presentasi", f"**Tugas 2** ({w['t2']}) — evaluasi Sub-CPMK Pekan 9–11")
        # Pekan 13-15: Finalisasi
        R(13, "Seluruh CPMK", "Penyempurnaan Proyek / Tugas Akhir",
          "Mahasiswa (*A*) menyempurnakan hasil proyek/tugas akhir (*B*) berdasarkan umpan balik (*C*) secara mandiri dan berkualitas (*D*).",
          "PjBL / Konsultasi", "—")
        R(14, "Seluruh CPMK", "Review & Konsultasi UAS",
          "Mahasiswa (*A*) mengonsolidasikan seluruh capaian pembelajaran (*B*) melalui review dan konsultasi (*C*) secara komprehensif (*D*).",
          "Diskusi / Konsultasi", "—")
        R(15, "Seluruh CPMK", "Presentasi Final / Demonstrasi",
          "Mahasiswa (*A*) mempresentasikan hasil akhir proyek/tugas (*B*) di hadapan dosen dan rekan (*C*) secara profesional (*D*).",
          "Presentasi", "—")
        # Pekan 16: UAS
        R(16, "Seluruh CPMK", "**UAS / Tugas Akhir / Proyek**",
          "Mahasiswa (*A*) mendemonstrasikan penguasaan seluruh CPMK (*B*) melalui ujian/proyek akhir (*C*) dengan kriteria ketuntasan minimal (*D*).",
          "Ujian / Proyek Akhir", f"**UAS** ({w['uas']})")
    
    elif n_cpmk == 3:
        s1, s2, s3 = groups[1], groups[2], groups[3]
        # Pekan 2-3: CPMK-1
        R(2, f"Sub-{s1[0][0]}", derive_topik(s1[0][1]), kompetensi_abcd(s1[0][1],1),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        R(3, f"Sub-{s1[1][0]}", derive_topik(s1[1][1]), kompetensi_abcd(s1[1][1],1),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        # Pekan 4: CPMK-2 start + Tugas 1
        R(4, f"Sub-{s2[0][0]}", derive_topik(s2[0][1]), kompetensi_abcd(s2[0][1],2),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL",
          f"**Tugas 1** ({w['t1']}) — evaluasi Sub-CPMK Pekan 2–3")
        # Pekan 5-7: CPMK-2 finish + CPMK-3
        R(5, f"Sub-{s2[1][0]}", derive_topik(s2[1][1]), kompetensi_abcd(s2[1][1],2),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        R(6, f"Sub-{s3[0][0]}", derive_topik(s3[0][1]), kompetensi_abcd(s3[0][1],3),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        R(7, f"Sub-{s3[1][0]}", derive_topik(s3[1][1]), kompetensi_abcd(s3[1][1],3),
          "Kuliah / Diskusi" if tipe=="Teori" else "Praktikum / PjBL", "—")
        # Pekan 8: UTS
        R(8, "CPMK-1 s.d. 2", "**Ujian Tengah Semester (UTS)**",
          "Mahasiswa (*A*) mendemonstrasikan penguasaan CPMK-1 dan CPMK-2 (*B*) melalui ujian tertulis/praktikum (*C*) dengan kriteria ketuntasan minimal (*D*).",
          "Ujian" if tipe=="Teori" else "Ujian Praktikum", f"**UTS** ({w['uts']})")
        # Pekan 9-11: Aplikasi CPMK-3
        R(9, "CPMK-3", "Aplikasi & Pendalaman CPMK-3 (Bagian 1)",
          "Mahasiswa (*A*) menerapkan kompetensi CPMK-3 (*B*) pada kasus/proyek nyata (*C*) secara mandiri dan terukur (*D*).",
          "PjBL / Case Method", "—")
        R(10, "CPMK-3", "Aplikasi & Pendalaman CPMK-3 (Bagian 2)",
          "Mahasiswa (*A*) mengembangkan solusi berbasis CPMK-3 (*B*) dalam konteks proyek (*C*) secara kolaboratif (*D*).",
          "PjBL / Case Method", "—")
        R(11, "CPMK-3", "Studi Kasus Integratif",
          "Mahasiswa (*A*) menganalisis kasus integratif (*B*) yang menghubungkan seluruh CPMK (*C*) secara kritis (*D*).",
          "Case Method / Diskusi", "—")
        # Pekan 12: Proyek + Tugas 2
        R(12, "Seluruh CPMK", "Proyek Terapan & Presentasi Antara",
          "Mahasiswa (*A*) menyajikan progres proyek (*B*) dalam forum kelas (*C*) dengan argumen yang valid (*D*).",
          "PjBL / Presentasi", f"**Tugas 2** ({w['t2']}) — evaluasi Sub-CPMK Pekan 9–11")
        # Pekan 13-15: Finalisasi
        R(13, "Seluruh CPMK", "Penyempurnaan Proyek / Tugas Akhir",
          "Mahasiswa (*A*) menyempurnakan hasil proyek (*B*) berdasarkan umpan balik (*C*) secara mandiri (*D*).",
          "PjBL / Konsultasi", "—")
        R(14, "Seluruh CPMK", "Review & Konsultasi UAS",
          "Mahasiswa (*A*) mengonsolidasikan seluruh capaian (*B*) melalui review (*C*) secara komprehensif (*D*).",
          "Diskusi / Konsultasi", "—")
        R(15, "Seluruh CPMK", "Presentasi Final / Demonstrasi",
          "Mahasiswa (*A*) mempresentasikan hasil akhir (*B*) di hadapan dosen dan rekan (*C*) secara profesional (*D*).",
          "Presentasi", "—")
        # Pekan 16: UAS
        R(16, "Seluruh CPMK", "**UAS / Tugas Akhir / Proyek**",
          "Mahasiswa (*A*) mendemonstrasikan penguasaan seluruh CPMK (*B*) melalui ujian/proyek akhir (*C*) dengan kriteria ketuntasan minimal (*D*).",
          "Ujian / Proyek Akhir", f"**UAS** ({w['uas']})")
    
    return rows

def render_rps(code):
    rows = gen_16weeks(code)
    info = mk_info.get(code, {})
    tipe = info.get("tipe","Teori")
    sks = info.get("sks",3)
    L = [f"**Rencana 16 Pertemuan & Asesmen** ({sks} SKS, {tipe} — 1 SKS = 50 menit):", "",
         "| Pekan | Sub-CPMK | Topik Pembelajaran Terkait | Kompetensi / Keterangan (ABCD) | Metode | Jumlah Jam | Asesmen |",
         "|:---:|:---:|---|---|---|:---:|:---:|"]
    for pekan, subcpmk, topik, komp, metode, j, asesmen in rows:
        L.append(f"| {pekan} | {subcpmk} | {topik} | {komp} | {metode} | {j} | {asesmen} |")
    return "\n".join(L) + "\n\n"

def remove_old_rps(s):
    """Remove old RPS v1 blocks (5-col: Pekan|Topik|Sub-CPMK|Metode|Asesmen)."""
    return re.sub(
        r"\*\*Rencana 16 Pertemuan & Asesmen\*\*[^\n]*\n\n"
        r"\| Pekan \| Topik Pembelajaran \| Sub-CPMK Terkait \| Metode \| Asesmen \|\n"
        r"\|[^\n]*\n(?:\|[^\n]*\n)*\n", "", s)

def inject(path, heading_pat, anchor_pat, codes):
    s = open(path, encoding="utf-8").read()
    s = remove_old_rps(s)  # clean old v1 RPS
    changed = 0
    for code in codes:
        if code not in SUBCPMK: continue
        hm = re.search(heading_pat.format(code=re.escape(code)), s)
        if not hm:
            print(f"  !! heading not found: {code}"); continue
        gm = re.search(anchor_pat, s[hm.end():])
        if not gm:
            print(f"  !! anchor not found: {code}"); continue
        pos = hm.end() + gm.start()
        block = render_rps(code)
        s = s[:pos] + block + s[pos:]
        changed += 1
    open(path, "w", encoding="utf-8").write(s)
    return changed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gen_043_rps_v2.py <semester|all>"); sys.exit(1)
    arg = sys.argv[1]
    per = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md")
    dan = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md")
    
    if arg == "all":
        sems = sorted(SEMESTER_MAP.keys())
    else:
        sems = [int(arg)]
    
    for sem in sems:
        codes = SEMESTER_MAP[sem]
        print(f"Semester {sem}: {len(codes)} MK")
        c1 = inject(per, r"\n### \d+\. {code} \u2014 ", r"\*\*Boundary Guardrails\*\*", codes)
        c2 = inject(dan, r"\n#### {code} \u2014 ", r"\*\*Boundary Guardrails:\*\*", codes)
        print(f"  PER: {c1}/{len(codes)} | DAN: {c2}/{len(codes)}")
