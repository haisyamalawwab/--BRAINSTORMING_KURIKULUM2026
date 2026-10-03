# -*- coding: utf-8 -*-
"""
apply_004_cpl_baku_codes.py
===========================
Penetapan Kode Baku CPL-01 s.d. CPL-14 pada Dokumen 004 (Matriks Keterlacakan OBE).

Tindakan:
1. Mengganti seluruh kode CPL lama menjadi kode baku:
   S1->CPL-01, KU1->CPL-02, KU2->CPL-03, KU3->CPL-04,
   P1->CPL-05, P2->CPL-06, P3->CPL-07, P4->CPL-08,
   KK1->CPL-09, KK2->CPL-10, KK3->CPL-11, KK4->CPL-12, KK5->CPL-13, KK6->CPL-14.
2. Melindungi notasi NON-CPL agar tidak ikut terganti:
   - "(S1)" pada judul program studi (jenjang Sarjana)
   - "Pilihan P1/P2/P3" (header kolom tabel peminatan, Dok 004 Bagian 4)
   - "MK P1/P2/P3" (rekapitulasi SKS peminatan, Dok 004 Bagian 5)
3. Menyisipkan "Bagian 0: Tabel Persamaan Kode CPL" sebelum Bagian 1 sebagai
   rujukan tunggal konversi kode.

Idempoten: jika penanda Bagian 0 sudah ada, skrip berhenti tanpa mengubah apa pun.
"""
import re
import sys

PATH = "004_MATRIKS_KETERLACAKAN_OBE_VMTS_PEO_PL_CPL_MK.md"
MARKER = "## 0. TABEL PERSAMAAN KODE CPL"
ANCHOR = "## 1. MATRIKS KESELARASAN STRATEGIS"

MAPPING = {
    "S1": "CPL-01",
    "KU1": "CPL-02", "KU2": "CPL-03", "KU3": "CPL-04",
    "P1": "CPL-05", "P2": "CPL-06", "P3": "CPL-07", "P4": "CPL-08",
    "KK1": "CPL-09", "KK2": "CPL-10", "KK3": "CPL-11",
    "KK4": "CPL-12", "KK5": "CPL-13", "KK6": "CPL-14",
}

# Pola non-CPL yang dilindungi (lihat docstring)
PROTECT_PATTERNS = [r"\(S1\)", r"Pilihan P[123]\b", r"MK P[123]\b"]

SECTION_0 = """## 0. TABEL PERSAMAAN KODE CPL: KODE BAKU `CPL-01` s.d. `CPL-14` ↔ KODE KATEGORI LAMA

**Konvensi Penomoran CPL (ditetapkan 2 Oktober 2026):** Seluruh CPL dalam ekosistem OBE SISTEKIN 2026 menggunakan **kode baku berurutan `CPL-01` s.d. `CPL-14`**. Kode lama berbasis klaster kategori (`S1`, `KU1`–`KU3`, `P1`–`P4`, `KK1`–`KK6`) ditetapkan sebagai **alias kategori**, dan seluruh kemunculannya pada dokumen ini telah digantikan kode baku. Tabel berikut merupakan **rujukan tunggal persamaan kode** bagi dosen pengampu, Gugus Penjaminan Mutu (GPM), dan penyusun RPS OBE Generator.

| Kode Baku Baru | Kode Lama (Alias Kategori) | Klaster CPL | Deskripsi Ringkas CPL | Level Bloom | Genealogi Sumber (Dok. 003) |
|:---:|:---:|:---:|---|:---:|---|
| **CPL-01** | `S1` | Sikap (S) | Integritas, etika komputasi, nilai Pancasila & spiritualitas | A3 (Valuing) | SN-Dikti Sikap 1–10; IS2020 CPL-S01–S08 |
| **CPL-02** | `KU1` | Keterampilan Umum (KU) | Berpikir kritis, pemecahan masalah kompleks & logika komputasi | C4 (Analyze) | SN-Dikti KU 1 & 3; IS2020 CPL-KU01 |
| **CPL-03** | `KU2` | Keterampilan Umum (KU) | Komunikasi efektif ilmiah, kepemimpinan & kolaborasi tim | C5 (Evaluate) | SN-Dikti KU 4 & 6; IS2020 CPL-KU02, KU04 |
| **CPL-04** | `KU3` | Keterampilan Umum (KU) | Tanggung jawab etis, kepatuhan regulasi siber & hukum digital | C5 (Evaluate) | SN-Dikti KU 2, 5, 7–9; IS2020 CPL-KU03, KU05–KU08 |
| **CPL-05** | `P1` | Pengetahuan (P) | Fondasi matematika sains komputer, logika, aljabar & kalkulus | C3 (Apply) | IS2020 CPL-P05; IT2017 Pengetahuan P1 |
| **CPL-06** | `P2` | Pengetahuan (P) | Konsep sistem informasi cerdas, arsitektur data & tata kelola | C4 (Analyze) | IS2020 CPL-P01, P04, P09, P16; IT2017 Pengetahuan P2 |
| **CPL-07** | `P3` | Pengetahuan (P) | Infrastruktur komputasi awan, jaringan, IoT & keamanan siber | C4 (Analyze) | IS2020 CPL-P03, P06, P07, P08; IT2017 Pengetahuan P2 |
| **CPL-08** | `P4` | Pengetahuan (P) | Rekayasa perangkat lunak, algoritma pemrograman & platform | C4 (Analyze) | IS2020 CPL-P02, P10–P14; IT2017 Pengetahuan P1 |
| **CPL-09** | `KK1` | Keterampilan Khusus (KK) | Merancang, melatih & mengintegrasikan model Machine Learning/AI | C6 (Create) | IS2020 CPL-K01, K09, K13, K16; IT2017 KK1 |
| **CPL-10** | `KK2` | Keterampilan Khusus (KK) | Rekayasa data end-to-end, data mining, DWH/BI & analitik | C6 (Create) | IS2020 CPL-K01, K13, K16; IT2017 KK1 |
| **CPL-11** | `KK3` | Keterampilan Khusus (KK) | Mengonfigurasi cloud infra, arsitektur jaringan & telemetri IoT | C6 (Create) | IS2020 CPL-K02, K05, K06, K17; IT2017 KK2 & KK3 |
| **CPL-12** | `KK4` | Keterampilan Khusus (KK) | Menganalisis risiko keamanan siber, pentest & tata kelola TI | C5 (Evaluate) | IS2020 CPL-K05, K06, K07, K14; IT2017 KK3 |
| **CPL-13** | `KK5` | Keterampilan Khusus (KK) | Membangun web/mobile multi-platform, UI/UX & microservices | C6 (Create) | IS2020 CPL-K03, K04, K08, K10–K12; IT2017 KK1 |
| **CPL-14** | `KK6` | Keterampilan Khusus (KK) | Mengelola proyek TI secara adaptif, startup digital & bisnis | C6 (Create) | IS2020 CPL-K08, K15; IT2017 KK1 |

> **Catatan Anti-Kolisi Notasi (WAJIB dibaca):**
> 1. **"(S1)" pada judul program studi** adalah jenjang Sarjana — **bukan** kode CPL dan tidak berubah.
> 2. **Label Peminatan P1/P2/P3** (P1 *Integrated Smart Systems*; P2 *Cloud Infrastructure & Cybersecurity*; P3 *Digital Platform Engineering*) adalah penamaan jalur peminatan — **berbeda dari kode CPL-05 s.d. CPL-07** dan tidak berubah.
> 3. Kode genealogi pada kolom sumber (`CPL-S01–S08`, `CPL-KU01–08`, `CPL-P01–P17`, `CPL-K01–K17` milik IS2020, serta `P1–P2` dan `KK1–KK3` milik IT2017) adalah kode baku standar rujukan — **berbeda dari alias CPL lama** meskipun notasinya mirip.
> 4. Rumusan lengkap CPL (ABCD), indikator kinerja, dan pemetaan BoK tetap merujuk **Dokumen 003** serta **Dokumen 009A–009E**; tabel ini hanya menetapkan persamaan kode.
"""


def main():
    with open(PATH, "r", encoding="utf-8", newline="") as f:
        src = f.read()

    if MARKER in src:
        print("SKIP: Bagian 0 (Tabel Persamaan Kode CPL) sudah ada — idempoten, tidak ada perubahan.")
        return

    nl = "\r\n" if "\r\n" in src else "\n"

    # --- Fase 1: lindungi notasi non-CPL ---
    protected = []

    def protect(m):
        protected.append(m.group(0))
        return "\x00{}\x00".format(len(protected) - 1)

    for pat in PROTECT_PATTERNS:
        src = re.sub(pat, protect, src)

    # --- Fase 2: ganti kode CPL lama -> kode baku ---
    counts = {}
    for old in sorted(MAPPING, key=len, reverse=True):
        src, n = re.subn(r"\b{}\b".format(re.escape(old)), MAPPING[old], src)
        counts[old] = n

    # --- Fase 3: kembalikan notasi terlindungi ---
    def unprotect(m):
        return protected[int(m.group(1))]

    src = re.sub(r"\x00(\d+)\x00", unprotect, src)

    # --- Fase 4: sisipkan Bagian 0 sebelum Bagian 1 ---
    idx = src.find(ANCHOR)
    if idx == -1:
        sys.exit("FATAL: anchor '{}' tidak ditemukan — file tidak diubah.".format(ANCHOR))
    section = SECTION_0.replace("\n", nl)
    src = src[:idx] + section + nl + nl + src[idx:]

    with open(PATH, "w", encoding="utf-8", newline="") as f:
        f.write(src)

    total = sum(counts.values())
    print("Penggantian per kode:")
    for old in MAPPING:
        print("  {:<4} -> {:<7} : {}".format(old, MAPPING[old], counts[old]))
    print("Total titik ganti: {}".format(total))
    print("Token dilindungi (tidak diubah): {}".format(protected))


if __name__ == "__main__":
    main()
