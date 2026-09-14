# -*- coding: utf-8 -*-
"""Inject Sub-CPMK for a specific semester into both 043 docs."""
import re, os, sys, importlib

SCRIPT = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT)

# Load all Sub-CPMK data
mods = [importlib.import_module(f"_043_subcpmk_{n}") for n in ("s1", "s23", "s45", "s67", "p56", "p7")]
SUBCPMK = {}
for m in mods:
    name = [x for x in dir(m) if x.startswith("SUBCPMK")][0]
    SUBCPMK.update(getattr(m, name))

# Semester mapping
SEMESTER_MAP = {
    1: ["STI-101", "STI-102", "STI-103"],
    2: ["STI-204", "STI-205"],
    3: ["STI-306", "STI-307", "STI-308", "STI-309", "STI-310", "STI-311", "STI-312"],
    4: ["STI-413", "STI-414", "STI-415", "STI-416", "STI-417", "STI-418"],
    5: ["STI-519", "STI-520", "STI-521", "STI-522", "STI-523", "STA-501", "STB-501", "STC-501"],
    6: ["STI-624", "STI-625", "STI-626", "STI-627", "STA-601", "STA-602", "STB-601", "STB-602", "STC-601", "STC-602"],
    7: ["STI-728", "STA-701", "STA-702", "STA-703", "STB-701", "STB-702", "STB-703", "STC-701", "STC-702", "STC-703"],
}

def render_block(code):
    subs = SUBCPMK[code]
    L = ["**Sub-CPMK (penjabaran operasional CPMK, selaras IN-SCOPE Boundary Guardrails):**", "", "| Kode | Kompetensi Spesifik | CPMK | Bloom |", "|---:|---|:--:|:--:|"]
    for sub, txt, src, bloom in subs:
        L.append(f"| **Sub-CPMK-{sub}** | {txt} | CPMK-{src} | **{bloom}** |")
    return "\n".join(L) + "\n\n"

def inject(path, heading_pat, anchor_pat, codes):
    s = open(path, encoding="utf-8").read()
    changed = 0
    for code in codes:
        if code not in SUBCPMK:
            print(f"  !! {code} not in SUBCPMK data")
            continue
        hm = re.search(heading_pat.format(code=re.escape(code)), s)
        if not hm:
            print(f"  !! heading not found for {code} in {os.path.basename(path)}")
            continue
        gm = re.search(anchor_pat, s[hm.end():])
        if not gm:
            print(f"  !! guardrails anchor not found for {code} in {os.path.basename(path)}")
            continue
        pos = hm.end() + gm.start()
        if "Sub-CPMK-" in s[hm.start():pos]:
            print(f"  [skip] {code} already injected")
            continue
        block = render_block(code)
        s = s[:pos] + block + s[pos:]
        changed += 1
    open(path, "w", encoding="utf-8").write(s)
    return changed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gen_043_subcpmk_semester.py <semester_number>")
        sys.exit(1)
    
    sem = int(sys.argv[1])
    if sem not in SEMESTER_MAP:
        print(f"Invalid semester: {sem}. Valid: {list(SEMESTER_MAP.keys())}")
        sys.exit(1)
    
    codes = SEMESTER_MAP[sem]
    print(f"Injecting Sub-CPMK for Semester {sem}: {', '.join(codes)}")
    
    per = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md")
    dan = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md")
    
    c1 = inject(per, r"\n### \d+\. {code} \u2014 ", r"\*\*Boundary Guardrails\*\*", codes)
    c2 = inject(dan, r"\n#### {code} \u2014 ", r"\*\*Boundary Guardrails:\*\*", codes)
    
    print(f"PER_SEMESTER injected: {c1}/{len(codes)}")
    print(f"DAN_BOUNDARY injected: {c2}/{len(codes)}")
