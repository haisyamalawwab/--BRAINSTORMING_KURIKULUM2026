#!/usr/bin/env python3
"""Build a navigable Markdown index from the current workspace; use --check in CI."""
from collections import defaultdict
from pathlib import Path
import argparse
import re
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'INDEX.md'
PACKAGES = ROOT / 'PERANGKAT_AJAR'
TYPES = {'1': 'RPS', '2': 'SAP', '3': 'Outline', '4': 'Asesmen', '5': 'Rubrik'}


def link(path: Path, label: str) -> str:
    relative = path.relative_to(ROOT).as_posix()
    # URL-encode spaces and parentheses; the link remains repository-relative.
    return f'[{label}]({quote(relative, safe="/-._~")})'


def build() -> str:
    manifest = (PACKAGES / 'README.md').read_text(encoding='utf-8')
    rows = re.findall(r'^\| `(\d{3})` \| (\d) \| `(STI|STA|STB|STC)-(\d{3})` \| ([^|]+) \|', manifest, re.M)
    courses = {n: (int(sem), f'{prefix}-{code}', name.strip()) for n, sem, prefix, code, name in rows}
    if len(rows) != 46 or len(courses) != 46 or set(courses) != {f'{n:03}' for n in range(55, 101)}:
        raise ValueError('Manifest harus memuat tepat 46 nomor Core STI dan peminatan 055–100.')
    files = defaultdict(dict)
    for path in sorted(PACKAGES.glob('*.md')):
        m = re.match(r'^(\d{3})_([1-5])_', path.name)
        if m:
            number, kind = m.groups()
            if kind in files[number]:
                raise ValueError(f'Duplikat {number}_{kind}: {path.name}')
            files[number][kind] = path
    for number in courses:
        if set(files[number]) != set(TYPES):
            raise ValueError(f'Paket {number} tidak lengkap: {sorted(files[number])}')

    parts = [
        '# Indeks Dokumen Kurikulum SISTEKIN 2026', '',
        '> Indeks ini dibuat dari berkas yang ada, bukan pengesahan akademik. '
        'Gunakan Dokumen 005 untuk identitas MK dan periksa catatan validasi pada setiap dokumen. '
        'HTML, XLSX, DOCX dan PDF dapat tertinggal dari Markdown.', '',
        'Kembali ke [README repositori](../README.md) · '
        '[Panduan perangkat ajar](PERANGKAT_AJAR/README.md) · '
        '[Portal HTML](index.html)', '',
        '## Navigasi cepat', '',
    ]
    quick = [
        ('005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md', '005 — identitas MK dan struktur'),
        ('003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md', '003 — CPL dan BoK'),
        ('004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md', '004 — keterlacakan OBE'),
        ('007_FORMULASI_CPMK_DAN_SUB_CPMK_PORTFOLIO_LENGKAP.md', '007 — CPMK dan silabus'),
        ('037_BOUNDARY_OF_TOPICS_DAN_MATRIKS_ANTI_OVERLAP_KURIKULUM.md', '037 — boundary guardrails'),
        ('043_MATRIKS_CPL_CPMK_BoK_DAN_BOUNDARY_GUARDRAILS.md', '043 — matriks induk'),
        ('043_STI-311_WEB_FRONT_END_DEVELOPMENT_DASAR_USULAN_07112026.md', '043 — rancangan revisi STI-311'),
        ('LAPORAN_AUDIT_DAMPAK_STI-311.md', 'Audit dampak STI-311 dan MK hilir'),
    ]
    for filename, label in quick:
        path = ROOT / filename
        if not path.is_file():
            raise ValueError(f'Dokumen navigasi tidak ada: {filename}')
        parts.append(f'- {link(path, label)}')

    parts.extend(['', '## Perangkat ajar: Core STI dan peminatan', '',
                  'Tersedia **46 mata kuliah × 5 dokumen = 230 berkas** untuk nomor 055–100. '
                  'Status ini menyatakan keberadaan berkas, bukan kelengkapan akademik atau pengesahan.', ''])
    for semester in sorted({row[0] for row in courses.values()}):
        parts.extend([f'### Semester {semester}', '', '| No. | Kode MK | Nama MK | Dokumen Markdown |', '|---|---|---|---|'])
        for number, (sem, code, name) in sorted(courses.items()):
            if sem != semester:
                continue
            links = ' · '.join(link(files[number][k], TYPES[k]) for k in TYPES)
            parts.append(f'| {number} | `{code}` | {name.replace("|", "&#124;")} | {links} |')
        parts.append('')

    parts.extend(['## Paket di luar cakupan 46 MK', ''])
    if '113' in files:
        if set(files['113']) != set(TYPES):
            raise ValueError('Paket 113 FST-714 tidak lengkap.')
        parts.append('- `113` — FST-714 Skripsi / Tugas Akhir (semester 8): ' +
                     ' · '.join(link(files['113'][k], TYPES[k]) for k in TYPES) +
                     '. Paket ini **tidak** termasuk hitungan 46 MK di atas.')
    extras = sorted(n for n in files if n not in courses and n != '113')
    if extras:
        parts.append('- Nomor paket lain yang terdeteksi: ' + ', '.join(f'`{n}`' for n in extras) + '. Periksa manifest sebelum digunakan.')

    parts.extend(['', '## Seluruh dokumen Markdown di folder revisi', '',
                  'Dokumen bertanda **arsip** atau **pilot lama** dapat berisi informasi historis; '
                  'rujuk dokumen induk dan audit terbaru untuk penggunaan aktif.', ''])
    for path in sorted(ROOT.glob('*.md'), key=lambda p: p.name.casefold()):
        if path == OUT:
            continue
        name = path.name
        status = ''
        if 'BACKUP' in name.upper() or name.startswith('RPS_STI-311_'):
            status = ' — arsip/pilot lama'
        elif name == '043_STI-311_WEB_FRONT_END_DEVELOPMENT_DASAR_USULAN_07112026.md':
            status = ' — rancangan; belum disahkan'
        elif name == 'LAPORAN_AUDIT_DAMPAK_STI-311.md':
            status = ' — audit dan keputusan lanjutan'
        parts.append(f'- {link(path, name)}{status}')
    parts.extend(['', '---', '',
                  'Dibuat dengan `python3 -B KURIKULUM2026_REVISI/_tools/update_markdown_index.py`; '
                  'gunakan `--check` untuk memeriksa apakah indeks masih sesuai.', ''])
    return '\n'.join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the generated index differs from the committed file')
    args = parser.parse_args()
    content = build()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8') != content:
            print(f'Indeks perlu diperbarui: {OUT}', file=sys.stderr)
            return 1
        print('Indeks Markdown mutakhir dan seluruh paket 055–100 lengkap.')
    else:
        OUT.write_text(content, encoding='utf-8')
        print(f'Indeks ditulis: {OUT}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
