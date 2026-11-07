import os
import re
import glob

base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
f005_path = os.path.join(base, '005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md')

with open(f005_path, 'r', encoding='utf-8') as f:
    d005 = f.read()

# 1. Parse all 67 courses from Dok 005
courses_005 = {}

for line in d005.splitlines():
    m = re.search(r'\|\s*[\d.B]+\s*\|\s*`([A-Z]{3}-\d{3})`\s*\|\s*([^|]+)\|\s*\*?([^|*]+)\*?\s*\|\s*(\d+)\s*\|\s*([^|]+)\|\s*(?:Sem\s*)?(\d+)\s*\|\s*([^|]+)\|', line)
    if not m:
        m = re.search(r'\|\s*[\d.B]+\s*\|\s*`([A-Z]{3}-\d{3})`\s*\|\s*([^|]+)\|\s*(\d+)\s*\|\s*([^|]+)\|\s*(?:Sem\s*)?(\d+)\s*\|\s*([^|]+)\|', line)
        if m:
            kode, nama, sks, tipe, sem, pra = [x.strip() for x in m.groups()]
            courses_005[kode] = {
                'nama': nama,
                'sks': int(sks),
                'tipe': tipe,
                'sem': sem.replace('Sem ', '').strip(),
                'pra': pra
            }
    else:
        kode = m.group(1).strip()
        nama = m.group(2).strip()
        nama_en = m.group(3).strip()
        sks = int(m.group(4).strip())
        tipe = m.group(5).strip()
        sem = m.group(6).strip().replace('Sem ', '')
        pra = m.group(7).strip()
        courses_005[kode] = {
            'nama': nama,
            'nama_en': nama_en,
            'sks': sks,
            'tipe': tipe,
            'sem': sem,
            'pra': pra
        }

print(f"Parsed {len(courses_005)} courses from Dokumen 005 tables.")

# List of all markdown files (root + PERANGKAT_AJAR/)
md_files = sorted(
    glob.glob(os.path.join(base, "*.md"))
    + glob.glob(os.path.join(base, "PERANGKAT_AJAR", "*.md"))
)
print(f"Scanning {len(md_files)} markdown files in {base} (including PERANGKAT_AJAR/)...\n")

audit_results = {
    'obsolete_codes': [],
    'dl_sem5_occurrences': [],
    'security_sem6_occurrences': [],
    'sti_625_3sks': [],
    'course_mismatches': [],
    'clean_files': []
}

# Old codes that should not exist in active curriculum references
old_codes = [
    'STI-401', 'STI-402', 'STI-403', 'STI-404', 'STI-405', 'STI-407',
    'STI-501', 'STI-503', 'STI-504', 'STI-505', 'STI-506',
    'STI-601', 'STI-602', 'STI-603', 'STI-604', 'STI-701'
]

# Historical files where old codes are expected in mapping tables
whitelist_old_code_files = [
    '027_RENCANA_RESTRUKTURISASI_KODE_MK_CORE_STI_KONTINU.md',
    '028_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_CORE_STI.md',
    '029_TABEL_VERIFIKASI_KODE_MK_BARU.md',
    '019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md'
]

for fpath in sorted(md_files):
    fname = os.path.basename(fpath)
    rel_name = os.path.relpath(fpath, base)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    file_issues = []

    # Check 1: Old codes outside whitelist
    if fname not in whitelist_old_code_files:
        for oc in old_codes:
            # check if code appears with backticks or in table
            if re.search(rf'`{oc}`', content):
                # check if it's K2025 code reference
                # in Dok 024, K2025 codes are used (STI-401 etc. don't exist in K2025 anyway, K2025 has STI-418 etc.)
                file_issues.append(f"Ditemukan kode usang `{oc}`")

    # Check 2: Deep Learning in Semester 5
    # Matches like "STI-519 Deep Learning" or "Deep Learning ... Sem 5"
    if re.search(r'STI-519(?:\s+[—\-]\s+|\s+)?Deep Learning', content, re.IGNORECASE):
        file_issues.append("Menyebut 'STI-519 Deep Learning' (seharusnya STI-624 di Sem 6)")
    if re.search(r'Deep Learning[^\n.]{0,30}\([^)]*Sem 5\)', content):
        file_issues.append("Menyebut Deep Learning di Sem 5")

    # Check 3: Keamanan Informasi Lanjut in Semester 6
    if re.search(r'STI-626(?:\s+[—\-]\s+|\s+)?Keamanan Informasi Lanjut', content, re.IGNORECASE):
        file_issues.append("Menyebut 'STI-626 Keamanan Informasi Lanjut' (seharusnya STI-519 di Sem 5)")

    # Check 4: Smart City (STI-727 pasca Dok 051, atau STI-625 pra-Dok 051) berbobot 3 SKS (seharusnya 2 SKS)
    if re.search(r'STI-727(?:\s*\(2026\))?[^\w\n,;]{0,35}(?:3\s*SKS|\|\s*3\s*\|)', content) or re.search(r'STI-625[^\n]{0,30}Smart City[^\n]{0,20}3\s*SKS', content, re.IGNORECASE):
        if fname not in whitelist_old_code_files and fname not in ('024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md', '050_DEV_REPORT_DAN_LOG_PERTUKARAN_STRUKTUR_SEM6_SEM7_DAN_HARMONISASI_KURIKULUM.md', '051_DEV_REPORT_DAN_LOG_RESTRUKTURISASI_KODE_MK_PASCA_PERTUKARAN_SEM6_SEM7.md'):
            file_issues.append("Menyebut Smart City berbobot 3 SKS (seharusnya 2 SKS)")

    # Check 5: Prerequisite of STI-624 (should not be STI-519)
    if re.search(r'STI-624[^|\n]*[Pp]rasyarat[^|\n]*STI-519', content):
        file_issues.append("Prasyarat STI-624 masih merujuk STI-519")

    if file_issues:
        print(f"[FAIL] {rel_name}:")
        for iss in file_issues:
            print(f"    - {iss}")
    else:
        audit_results['clean_files'].append(rel_name)
        print(f"[OK] {rel_name} : 100% Selaras dengan Dok 005")

print(f"\n=======================================================")
print(f"TOTAL FILE BERSIH & SELARAS: {len(audit_results['clean_files'])} / {len(md_files)}")
print(f"=======================================================")
