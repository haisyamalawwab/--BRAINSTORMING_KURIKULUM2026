#!/usr/bin/env python3
"""Regression checks for the revised STI-311 Markdown, not academic approval."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'PERANGKAT_AJAR'
DRAFT = ROOT / '043_STI-311_WEB_FRONT_END_DEVELOPMENT_DASAR_USULAN_07112026.md'
s = DRAFT.read_text()

def part(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0]

def numbered_rows(text, pattern):
    return re.findall(pattern, text, re.M)

cp = part(s, '## 3. Usulan formulasi CPMK (ABCD dan Bloom)', '### Sub-CPMK usulan')
subs = part(s, '### Sub-CPMK usulan', '\n---')
cp_rows = re.findall(r'^\| `CPMK-[1-4]` .*$', cp, re.M)
sub_rows = re.findall(r'^\| `Sub-CPMK-\d\.\d` .*$', subs, re.M)
assert len(cp_rows) == 4 and len(sub_rows) == 9
sections = [
    ('043 induk', ROOT / '043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md', '#### STI-311', '\n#### STI-312'),
    ('043 per semester', ROOT / '043_MATRIKS_CPL_CPMK_BoK_BOUNDARY_GUARDRAILS_PER_SEMESTER.md', '### 11. STI-311', '\n### 12. STI-312'),
    ('007', ROOT / '007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md', '### 22. STI-311', '\n### 23. STI-312'),
    ('buku', ROOT / 'BUKU_KURIKULUM_OBE_SISTEKIN_2026_FINAL.md', '### 22. STI-311', '\n### 23. STI-312'),
]
for name, path, start, end in sections:
    text = part(path.read_text(), start, end)
    for row in cp_rows + sub_rows:
        assert text.count(row) == 1, f'{name}: CPMK/sub tidak sama dengan turunan'
    assert numbered_rows(text, r'^\| (\d+) \|') == list(map(str, range(1, 17))), f'{name}: 16 minggu'
    assert 'OUT-OF-SCOPE' in text and 'React' in text and 'Fetch' in text, f'{name}: guardrail'
extract = (ROOT / '043_STI-311_WEB_FRONT_END_DEVELOPMENT_30092026.md').read_text()
for row in cp_rows + sub_rows:
    assert extract.count(row) == 1, 'ekstraksi tidak sesuai'
assert numbered_rows(extract, r'^\| (\d+) \|') == list(map(str, range(1, 17)))
files = []
for i in range(1, 6):
    matches = list(P.glob(f'065_{i}_*STI-311*.md'))
    assert len(matches) == 1, f'065_{i}: berkas tidak unik'
    files.append(matches[0].read_text())
for row in cp_rows + sub_rows:
    assert files[0].count(row) == 1, 'RPS: CPMK/sub tidak sama dengan turunan'
assert numbered_rows(files[0], r'^\| (\d+) \|') == list(map(str, range(1, 17)))
assert numbered_rows(files[1], r'^### Pertemuan (\d+)\b') == list(map(str, range(1, 17)))
assert numbered_rows(files[2], r'^### Bab (\d+)\b') == list(map(str, range(1, 15)))
for text in (s, files[0], files[3]):
    assert re.search(r'\*\*Total nilai MK\*\* \| \*\*20%\*\* \| \*\*25%\*\* \| \*\*25%\*\* \| \*\*30%\*\* \| \*\*100%\*\*', text)
for text in (s, files[3], files[4]):
    assert all(v.casefold() in text.casefold() for v in ('kalkulator', 'landing page', 'Bootstrap', 'Tailwind'))
rubrics = re.findall(r'^### (Tugas 1|UTS|Tugas 2|UAS) — minggu (\d+), (\d+)% MK, CPMK-(\d+)\n\n(.*?)(?=\n### |\n## |\Z)', files[4], re.M | re.S)
assert [(x[0], x[1], x[2], x[3]) for x in rubrics] == [('Tugas 1','4','20','1'),('UTS','8','25','2'),('Tugas 2','12','25','3'),('UAS','16','30','4')]
for label, _, _, _, body in rubrics:
    weights = [int(x) for x in re.findall(r'^\| [^|]+ \| (\d+)% \|', body, re.M)]
    assert sum(weights) == 100, f'{label}: bobot kriteria'
identity = (ROOT / '005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md').read_text()
assert re.search(r'\| `STI-311` \| Pengembangan Web Front End \| \*Web Front End Development\* \| 3 \| \+P \| Sem 3 \| `FST-102` \|', identity)
print('Lulus: identitas Dok 005; CPMK/Sub-CPMK sinkron 043/007/buku/RPS; 16 minggu, 14 bab, proyek dan bobot asesmen/rubrik.')
print('Pemeriksaan ini tidak memverifikasi kualitas akademik, persetujuan prodi, file non-Markdown, atau semua dokumen historis.')
