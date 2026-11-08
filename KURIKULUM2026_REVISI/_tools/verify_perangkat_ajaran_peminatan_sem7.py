#!/usr/bin/env python3
"""Audit struktural paket 089–100, bukan pengganti validasi akademik."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'PERANGKAT_AJAR'
SOURCE = (ROOT / '043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md').read_text()
CODES = ('STA-602 STA-701 STA-702 STA-703 STB-602 STB-701 '
         'STB-702 STB-703 STC-602 STC-701 STC-702 STC-703').split()
errors = []
for number, code in enumerate(CODES, 89):
    files = []
    for kind in range(1, 6):
        paths = list(FOLDER.glob(f'{number:03}_{kind}_*_{code}_*.md'))
        if len(paths) != 1:
            errors.append(f'{code}: jenis {kind}, ditemukan {len(paths)} berkas')
            break
        files.append(paths[0].read_text())
    if len(files) != 5:
        continue
    match = re.search(rf'^#### {code}[^\n]*\n(.*?)(?=\n#### [A-Z]|\n### |\Z)', SOURCE, re.M | re.S)
    if not match:
        errors.append(f'{code}: tidak ditemukan di Dok 043')
        continue
    source = match.group(1).split('**Formulasi CPMK', 1)[1].split('**Sub-CPMK', 1)[0]
    rows = re.findall(r'^\| `(CPMK-\d+)` \| (.*?) \|', source, re.M)
    if not rows:
        errors.append(f'{code}: CPMK sumber kosong')
    for cpmk, statement in rows:
        if files[0].count(f'| {cpmk} | {statement} |') != 1:
            errors.append(f'{code}: rumusan {cpmk} tidak identik atau duplikat')
    displayed = re.findall(r'^\| (CPMK-\d+) \| Mahasiswa', files[0], re.M)
    if displayed != [name for name, _ in rows]:
        errors.append(f'{code}: urutan atau jumlah CPMK salah')
    if re.findall(r'^### Pertemuan (\d+)\b', files[1], re.M) != list(map(str, range(1, 17))):
        errors.append(f'{code}: SAP bukan 16 pertemuan berurutan')
    if re.findall(r'^### Bab (\d+)\b', files[2], re.M) != list(map(str, range(1, 15))):
        errors.append(f'{code}: outline bukan 14 bab berurutan')
    points = re.findall(r'^### (Tugas 1|UTS|Tugas 2|UAS) — pekan (\d+), (\d+)%', files[3], re.M)
    expected = ['Tugas 1', 'UTS', 'Tugas 2', 'UAS']
    if [x[0] for x in points] != expected or [x[1] for x in points] != ['4', '8', '12', '16'] or sum(int(x[2]) for x in points) != 100:
        errors.append(f'{code}: titik evaluasi atau bobot tidak valid')
    if re.findall(r'^### (Tugas 1|UTS|Tugas 2|UAS) — pekan', files[4], re.M) != expected:
        errors.append(f'{code}: empat rubrik belum tersedia')
    for idx, text in enumerate(files, 1):
        if '…' in text:
            errors.append(f'{code}: tanda elipsis di dokumen {idx} perlu diperiksa')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('Lulus struktur 12 paket: CPMK Dok 043, 16 SAP, 14 bab, empat asesmen dan bobot 100%.')
print('Tidak memvalidasi mutu akademik, kecocokan sumber, kegiatan, rubrik, atau pengesahan.')
