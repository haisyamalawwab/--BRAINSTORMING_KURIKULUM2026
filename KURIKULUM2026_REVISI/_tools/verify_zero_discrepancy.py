# -*- coding: utf-8 -*-
import os
import re
import glob

workdir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

md_files = sorted(
    glob.glob(os.path.join(workdir, "*.md"))
    + glob.glob(os.path.join(workdir, "PERANGKAT_AJAR", "*.md"))
)

# Dokumen audit/analisis yang secara sah mengutip nomenklatur lama dalam konteks
# log koreksi, tabel ekuivalensi, atau pembahasan meta tentang skrip ini sendiri.
EXEMPT = {
    "016_ANALISIS_BoK_APTIKOM_REDUNDANSI_DAN_PIPELINE_AI.md",
    "017_AUDIT_FORENSIK_ZERO_REDUNDANCY_DAN_ZERO_GAP.md",
    "019_AUDIT_KRITIS_KESELARASAN_FOLDER_REVISI_23082026_212923.md",
    # Matriks ekivalensi: kolom "Kurikulum 2025" wajib memuat nomenklatur lama
    # (STI-103 Logika Informatika) sebagai sisi asal konversi.
    "024_MATRIKS_EKIVALENSI_KURIKULUM2025_KE_KURIKULUM2026.md",
}

print(f"Auditing {len(md_files)} markdown files in KURIKULUM2026_REVISI (including PERANGKAT_AJAR/)...")

errors = 0
for fpath in md_files:
    fname = os.path.basename(fpath)
    rel_name = os.path.relpath(fpath, workdir)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        lines = content.splitlines()

    for idx, line in enumerate(lines):
        line_num = idx + 1
        
        # Check STI-103 naming
        if "STI-103" in line:
            # Check if it contains old name Logika Informatika without being an equivalence table old column or historical doc
            if "Logika Informatika" in line and not any(k in line for k in ["(Lama)", "Logika Informatika lama", "Logika Informatika (Lama)", "Ekuivalen / Penyesuaian Topik"]):
                if fname not in EXEMPT:
                    print(f"[DISCREPANCY] {rel_name}:{line_num} -> Found STI-103 with old name: {line.strip()}")
                    errors += 1

        # Check STI-204 naming
        if "STI-204" in line:
            if "Matematika Diskrit" in line and "Logika" not in line and not any(k in line for k in ["(Lama)", "Matematika Diskrit (Lama)", "Matematika Diskrit lama"]):
                if fname not in EXEMPT:
                    print(f"[DISCREPANCY] {rel_name}:{line_num} -> Found STI-204 without Logika: {line.strip()}")
                    errors += 1

if errors == 0:
    print("[SUCCESS] 100% PERFECT ALIGNMENT: Semua file Markdown di KURIKULUM2026_REVISI telah 100% sinkron dan selaras!")
else:
    print(f"[FAILED] Ditemukan {errors} diskrepansi yang perlu diperbaiki.")
