import re
import json

path_007 = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI\007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md"
with open(path_007, "r", encoding="utf-8") as f:
    text = f.read()

# Pattern for headings: ### 1. FST-101 — Dasar Teknologi Digital (Fundamentals of Digital Technology)
pattern = r'###\s+\d+\.\s+([A-Z]{3}-\d{3})\s+[—\-]\s+([^(]+)\(([^)]+)\)'
matches = re.findall(pattern, text)

print(f"Total matched courses: {len(matches)}")
courses_dict = {}
for code, name_id, name_en in matches:
    courses_dict[code] = {
        "kode": code,
        "nama_id": name_id.strip(),
        "nama_en": name_en.strip()
    }

for k in sorted(courses_dict.keys())[:15]:
    c = courses_dict[k]
    print(f"{c['kode']}: {c['nama_id']} <---> {c['nama_en']}")

with open("courses_id_en.json", "w", encoding="utf-8") as f:
    json.dump(courses_dict, f, indent=2, ensure_ascii=False)
