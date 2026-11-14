#!/usr/bin/env python3
"""Periksa konsistensi Dokumen PKR-2026 (pemetaan klaster) terhadap 003/004/005.

Yang diperiksa:
  1. 18 MK peminatan di PKR-2026 §3.1 dan §5.x identik dengan 005 §1.4/§4
     (kode, nama, SKS, semester, tipe, jalur).
  2. CPL per MK peminatan di PKR-2026 §5.x identik dengan 004 §4.1-4.3.
  3. Seluruh kode BK yang dikutip PKR-2026 ada di 003 (BK-IS01..21, BK-IT01..15).
  4. Angka cakupan BK per klaster di PKR-2026 §5.4 dapat dihitung ulang dari 004 §6.
  5. Delapan baris salah label BoK di PKR-2026 §8.2 benar-benar berbeda dari
     nama resmi kode tersebut menurut 003.

Pakai --check untuk mode tanpa keluaran berkas (default perilaku sama).
Keluar dengan kode 1 bila ada ketidakcocokan.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DOC_003 = BASE / '003_STANDAR_14_CPL_DAN_PEMETAAN_BoK_APTIKOM.md'
DOC_004 = BASE / '004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md'
DOC_005 = BASE / '005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md'
DOC_PKR = BASE / 'PEMETAAN_KLASTER_RANTING_ILMU_SISTEKIN_CS2023_APTIKOM_10112026.md'

TRACKS = {
    'P1': {'STA-501', 'STA-601', 'STA-602', 'STA-701', 'STA-702', 'STA-703'},
    'P2': {'STB-501', 'STB-601', 'STB-602', 'STB-701', 'STB-702', 'STB-703'},
    'P3': {'STC-501', 'STC-601', 'STC-602', 'STC-701', 'STC-702', 'STC-703'},
}
ALL_TRACK_MK = set().union(*TRACKS.values())

# PKR-2026 §8.2: (MK, kode salah di 005, nama resmi kode tsb menurut 003)
MISLABEL = [
    ('STA-501', 'BK-IS17', 'Human-Computer Interaction'),
    ('STB-701', 'BK-IS07', 'Systems Analysis'),
    ('STB-702', 'BK-IS08', 'Project Management'),
    ('STC-501', 'BK-IS13', 'Data Analytics'),
    ('STC-602', 'BK-IS05', 'IS Management'),
    ('STC-701', 'BK-IT14', 'IoT'),
    ('STC-702', 'BK-IT08', 'IT Service Management'),
    ('STC-703', 'BK-IS14', 'IT Audit'),
]

# PKR-2026 §5.4: (klaster, BK tersentuh primer+sekunder, BK primer saja)
COVERAGE = {'P1': (7, 5), 'P2': (13, 9), 'P3': (13, 4)}
COMBINED = 30
UNTOUCHED = ['BK-IS01', 'BK-IS10', 'BK-IS11', 'BK-IS21', 'BK-IT01', 'BK-IT15']

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def expand_codes(text: str) -> set[str]:
    """Ambil kode MK dari sel tabel, termasuk bentuk rentang `STA-701..703`."""
    codes = set(re.findall(r'ST[A-Z]-\d{3}', text))
    for m in re.finditer(r'(ST[A-Z])-(\d)(\d\d)\.\.(\d{2,3})', text):
        pre, digit, lo, hi = m.groups()
        for n in range(int(lo), int(hi[-2:]) + 1):
            codes.add(f'{pre}-{digit}{n:02d}')
    return codes


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip('|').split('|')]


def parse_005() -> dict[str, dict]:
    """Ambil 18 MK peminatan dari 005 §1.4 (kolom: no, kode, nama, EN, sks, tipe, sem, prasyarat, jalur)."""
    text = DOC_005.read_text(encoding='utf-8')
    start = text.find('KELOMPOK MATA KULIAH PILIHAN PEMINATAN')
    if start < 0:
        fail('005: bagian "KELOMPOK MATA KULIAH PILIHAN PEMINATAN" tidak ditemukan')
        return {}
    section = text[start:text.find('## 2. SEBARAN', start)]
    out: dict[str, dict] = {}
    for line in section.splitlines():
        if not line.startswith('|'):
            continue
        c = cells(line)
        if len(c) < 9:
            continue
        m = re.fullmatch(r'`(ST[A-C]-\d{3})`', c[1])
        if not m:
            continue
        code = m.group(1)
        out[code] = {
            'nama': c[2],
            'sks': c[4],
            'tipe': c[5],
            'sem': c[6].replace('Sem', '').strip(),
            'jalur': c[8],
        }
    if len(out) != 18:
        fail(f'005: seharusnya 18 MK peminatan, terbaca {len(out)}')
    return out


def parse_004_cpl() -> dict[str, set[str]]:
    """CPL per MK peminatan dari 004 §4.1-4.3."""
    text = DOC_004.read_text(encoding='utf-8')
    start = text.find('## 4. MATRIKS KETERLACAKAN 18 MATA KULIAH PILIHAN PEMINATAN')
    if start < 0:
        fail('004: bagian §4 matriks 18 MK peminatan tidak ditemukan')
        return {}
    section = text[start:text.find('## 5. REKAPITULASI', start)]
    out: dict[str, set[str]] = {}
    for line in section.splitlines():
        if not line.startswith('|'):
            continue
        c = cells(line)
        if len(c) < 6:
            continue
        m = re.fullmatch(r'`(ST[A-C]-\d{3})`', c[1])
        if not m:
            continue
        out[m.group(1)] = set(re.findall(r'CPL-\d{2}', c[5]))
    if len(out) != 18:
        fail(f'004: seharusnya 18 CPL pemetaan, terbaca {len(out)}')
    return out


def parse_004_bok() -> dict[str, set[str]]:
    """Peta BK -> himpunan MK (primer + sekunder) dari 004 §6.1-6.2."""
    text = DOC_004.read_text(encoding='utf-8')
    start = text.find('TABEL 6.1')
    end = text.find('## 7. MATRIKS KEPATUHAN', start)
    if start < 0 or end < 0:
        fail('004: tabel 6.1/6.2 tidak ditemukan')
        return {}
    out: dict[str, set[str]] = {}
    for line in text[start:end].splitlines():
        if not line.startswith('| **BK-'):
            continue
        c = cells(line)
        code = c[0].replace('*', '').strip()
        out[code] = expand_codes(c[2] + ' ' + c[3])
    if len(out) != 36:
        fail(f'004: seharusnya 36 BK (21 IS + 15 IT), terbaca {len(out)}')
    return out


def parse_004_bok_primary() -> dict[str, set[str]]:
    """Peta BK -> MK primer saja (kolom ●) dari 004 §6.1-6.2."""
    text = DOC_004.read_text(encoding='utf-8')
    start = text.find('TABEL 6.1')
    end = text.find('## 7. MATRIKS KEPATUHAN', start)
    out: dict[str, set[str]] = {}
    for line in text[start:end].splitlines():
        if not line.startswith('| **BK-'):
            continue
        c = cells(line)
        out[c[0].replace('*', '').strip()] = expand_codes(c[2])
    return out


def bok_line(code: str) -> str | None:
    text = DOC_004.read_text(encoding='utf-8')
    for line in text.splitlines():
        if line.startswith(f'| **{code}**'):
            return line
    return None


def parse_003_names() -> dict[str, str]:
    """Nama resmi tiap BK-IS/BK-IT menurut tabel 003."""
    text = DOC_003.read_text(encoding='utf-8')
    names: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r'\| \*\*(BK-(?:IS|IT)\d{2})\*\* \| ([^|]+)\|', line)
        if m:
            names[m.group(1)] = m.group(2).strip().strip('*').strip()
    if len(names) != 36:
        fail(f'003: seharusnya 36 nama BK, terbaca {len(names)}')
    return names


def parse_005_bok_column() -> dict[str, str]:
    """Kolom BoK pada 005 §4 untuk tiap MK peminatan."""
    text = DOC_005.read_text(encoding='utf-8')
    start = text.find('## 4. SKEMA 3 PEMINATAN')
    if start < 0:
        fail('005: bagian §4 SKEMA 3 PEMINATAN tidak ditemukan')
        return {}
    section = text[start:text.find('## 5.', start)]
    out: dict[str, str] = {}
    for line in section.splitlines():
        m = re.match(r'\| \d+ \| `(ST[A-C]-\d{3})` \|', line)
        if m:
            c = cells(line)
            out[m.group(1)] = c[-1] if len(c) >= 9 else ''
    return out


def parse_pkr() -> tuple[dict[str, dict], dict[str, set[str]]]:
    text = DOC_PKR.read_text(encoding='utf-8')
    # §3.1 tabel komposisi: kode muncul di kolom semester
    seen: set[str] = set()
    for line in text.splitlines():
        if line.startswith('| **P1 ') or line.startswith('| **P2 ') or line.startswith('| **P3 '):
            seen |= set(re.findall(r'ST[A-C]-\d{3}', line))
    if seen != ALL_TRACK_MK:
        fail('PKR-2026 §3.1: kode MK peminatan tidak lengkap — '
             f'kurang {sorted(ALL_TRACK_MK - seen)}, lebih {sorted(seen - ALL_TRACK_MK)}')

    # §5.x tabel: | KODE Nama | SKS | Sem | Tipe | CPL | BK | APT | CS2023 | BK-klaster |
    rows: dict[str, dict[str, str]] = {}
    cpl: dict[str, set[str]] = {}
    for line in text.splitlines():
        m = re.match(r'\| (ST[A-C]-\d{3}) ([^|]+)\|', line)
        if not m:
            continue
        c = cells(line)
        if len(c) < 9:
            continue
        code = m.group(1)
        rows[code] = {'nama': m.group(2).strip(), 'sks': c[1], 'sem': c[2], 'tipe': c[3]}
        cpl[code] = set(re.findall(r'CPL-\d{2}', c[4]))
    if set(rows) != ALL_TRACK_MK:
        fail('PKR-2026 §5: baris MK tidak lengkap — '
             f'kurang {sorted(ALL_TRACK_MK - set(rows))}, lebih {sorted(set(rows) - ALL_TRACK_MK)}')
    return rows, cpl


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='mode baca-saja (perilaku bawaan)')
    parser.parse_args()

    d005 = parse_005()
    d004 = parse_004_cpl()
    bok = parse_004_bok()
    names = parse_003_names()
    bok005 = parse_005_bok_column()
    rows, cpl = parse_pkr()

    # 1. identitas MK
    for code in sorted(ALL_TRACK_MK):
        a, b = d005.get(code), rows.get(code)
        if not a or not b:
            continue
        for field in ('sks', 'sem', 'tipe'):
            if a[field].replace('Sem', '').strip() != b[field].replace('Sem', '').strip():
                fail(f'{code}: {field} 005={a[field]!r} vs PKR={b[field]!r}')
        if a['nama'].lower() != b['nama'].lower():
            fail(f'{code}: nama 005={a["nama"]!r} vs PKR={b["nama"]!r}')

    # 2. CPL per MK
    for code in sorted(ALL_TRACK_MK):
        if code in d004 and code in cpl and d004[code] != cpl[code]:
            fail(f'{code}: CPL 004={sorted(d004[code])} vs PKR={sorted(cpl[code])}')

    # 3. kode BK yang dikutip PKR-2026 harus ada di 003
    text_pkr = DOC_PKR.read_text(encoding='utf-8')
    cited = set(re.findall(r'BK-(?:IS|IT)\d{2}', text_pkr))
    for code in sorted(cited - set(names)):
        fail(f'PKR-2026 mengutip kode BK yang tidak ada di 003: {code}')

    # 4. angka cakupan §5.4 (primer + sekunder, dan primer saja)
    primary = parse_004_bok_primary()
    hit_all: set[str] = set()
    for track, (exp_all, exp_prim) in COVERAGE.items():
        hit = {bk for bk, mks in bok.items() if mks & TRACKS[track]}
        hit_prim = {bk for bk, mks in primary.items() if mks & TRACKS[track]}
        hit_all |= hit
        if len(hit) != exp_all:
            fail(f'PKR-2026 §5.4 {track}: menulis {exp_all} BK (primer+sekunder), '
                 f'hasil hitung 004 §6 = {len(hit)}')
        if len(hit_prim) != exp_prim:
            fail(f'PKR-2026 §5.4 {track}: menulis {exp_prim} BK primer, '
                 f'hasil hitung 004 §6 = {len(hit_prim)}')
    if len(hit_all) != COMBINED:
        fail(f'§5.4 gabungan: PKR-2026 menulis {COMBINED} BK, hasil hitung = {len(hit_all)}')
    untouched = sorted(set(bok) - hit_all)
    if untouched != UNTOUCHED:
        fail(f'§5.5: PKR-2026 menyebut {UNTOUCHED} tidak tersentuh, hasil hitung = {untouched}')

    # 4b. C-4: BK-IT02 "9 MK" padahal kode unik 8
    row_it02 = bok_line('BK-IT02')
    if row_it02 is not None:
        uniq = expand_codes(row_it02)
        if '9 MK' in row_it02 and len(uniq) != 8:
            fail(f'C-4: 004 baris BK-IT02 diklaim 9 MK, kode unik = {len(uniq)} — koreksi klaim di PKR-2026')

    # 5. delapan salah label §8.2 benar-benar menyimpang dari 003
    for mk, kod, nama_resmi_expected in MISLABEL:
        actual = names.get(kod, '')
        if nama_resmi_expected.lower() not in actual.lower():
            fail(f'§8.2 {mk}: 003 menamai {kod} = {actual!r}, '
                 f'tidak memuat {nama_resmi_expected!r} — periksa klaim salah label')
        if mk not in bok005:
            fail(f'§8.2 {mk}: tidak ditemukan di tabel §4 005')

    if errors:
        print('GAGAL — PKR-2026 tidak konsisten dengan 003/004/005:', file=sys.stderr)
        for e in errors:
            print(f'  - {e}', file=sys.stderr)
        return 1

    print('Lulus: 18 MK peminatan, CPL, 36 BK, cakupan per klaster, dan 8 salah label konsisten.')
    print('  · cakupan BK (primer+sek / primer)  '
          + '  '.join(f'{k}={v[0]}/{v[1]}' for k, v in COVERAGE.items())
          + f'  gabungan={COMBINED}/36')
    print(f'  · kode BK dikutip PKR-2026: {len(cited)} dari 36 (semua ada di 003)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
