import shutil
import os

base = r"d:\!!MYDOCUMENTS2026\!!!SISTEKIN2026\!!BRAINSTORMING_KURIKULUM2026\KURIKULUM2026_REVISI"
f005 = os.path.join(base, "005_STRUKTUR_KURIKULUM_8_SEMESTER_DAN_PEMINATAN.md")
f005_new = f005 + ".new"
f005_bak = f005 + ".bak"

if os.path.exists(f005_new):
    shutil.copy2(f005, f005_bak)
    shutil.copy2(f005_new, f005)
    os.remove(f005_new)
    print("Dokumen 005 berhasil diperbarui dengan kolom Nama Indonesia dan English!")
    print(f"Backup tersimpan di: {f005_bak}")
else:
    print("File .new tidak ditemukan!")
