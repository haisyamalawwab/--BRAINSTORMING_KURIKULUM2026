# -*- coding: utf-8 -*-
"""Inject Sub-CPMK tables into both 043 docs, after each course's CPMK table
and before its '**Boundary Guardrails:**'. Content is authored, grounded in
each CPMK + IN-SCOPE guardrail topics (2 Sub-CPMK per CPMK)."""
import re, os, sys, importlib

SCRIPT = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT)

mods = [importlib.import_module(f"_043_subcpmk_{n}") for n in ("s1", "s23", "s45", "s67", "p56", "p7")]
SUBCPMK = {}
for m in mods:
    name = [x for x in dir(m) if x.startswith("SUBCPMK")][0]
    SUBCPMK.update(getattr(m, name))

def render_block(code):
    subs = SUBCPMK[code]
    L = ["**Sub-CPMK (penjabaran operasional CPMK, selaras IN-SCOPE Boundary Guardrails):**", "", "| Kode | Kompetensi Spesifik | CPMK | Bloom |", "|---:|---|:--:|:--:|"]
    for sub, txt, src, bloom in subs:
        L.append(f"| **Sub-CPMK-{sub}** | {txt} | CPMK-{src} | **{bloom}** |")
    return "\n".join(L) + "\n\n"

def inject(path, heading_pat, anchor_pat=r"\*\*Boundary Guardrails\*\*"):
    s = open(path, encoding="utf-8").read()
    changed = 0
    for code, subs in SUBCPMK.items():
        # locate this course's heading line
        hm = re.search(heading_pat.format(code=re.escape(code)), s)
        if not hm:
            print(f"  !! heading not found for {code} in {os.path.basename(path)}")
            continue
        # first '**Boundary Guardrails' after the heading
        gm = re.search(anchor_pat, s[hm.end():])
        if not gm:
            print(f"  !! guardrails anchor not found for {code} in {os.path.basename(path)}")
            continue
        pos = hm.end() + gm.start()
        if "Sub-CPMK-" in s[hm.start():pos]:  # already injected
            continue
        block = render_block(code)
        s = s[:pos] + block + s[pos:]
        changed += 1
    open(path, "w", encoding="utf-8").write(s)
    return changed

if __name__ == "__main__":
    per = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md")
    dan = os.path.join(WORKDIR, "043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md")
    only = sys.argv[1:] if len(sys.argv) > 1 else []
    c1 = inject(per, r"\n### \d+\. {code} \u2014 ", r"\*\*Boundary Guardrails\*\*") if (not only or "per" in only) else 0
    c2 = inject(dan, r"\n#### {code} \u2014 ", r"\*\*Boundary Guardrails:\*\*") if (not only or "dan" in only) else 0
    print(f"PER_SEMESTER injected: {c1}/46")
    print(f"DAN_BOUNDARY injected: {c2}/46")
