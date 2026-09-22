"""
SIAKAD Automation: Inspect & Input MK Kurikulum 2026
- Launches fresh Chrome with remote debugging port 9222 (fresh profile so no login cookie conflict)
- User must manually login via the opened Chrome window
- Script waits for user to confirm login, then proceeds
- Reads current MK from SIAKAD table and inputs missing ones
"""

import subprocess
import time
import urllib.request
import json
import sys
import os
from playwright.sync_api import sync_playwright

# ─────────────────────────────────────────────
# FULL MK LIST from 005_STRUKTUR_KURIKULUM...md
# ─────────────────────────────────────────────
COURSES_2026 = [
    # MKWU (8)
    {"kode": "MKU-101", "nama": "Agama I",                                              "sks": 2, "sem": 1, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "MKU-102", "nama": "Pancasila",                                             "sks": 2, "sem": 1, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "MKU-103", "nama": "Bahasa Indonesia",                                      "sks": 2, "sem": 1, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "MKU-204", "nama": "Kewirausahaan I",                                       "sks": 2, "sem": 2, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "MKU-405", "nama": "Kewarganegaraan",                                       "sks": 2, "sem": 4, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "MKU-406", "nama": "Agama II",                                              "sks": 0, "sem": 4, "sks_tm": 0, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "MKU-507", "nama": "Kuliah Pengabdian Kepada Masyarakat (KPM)",             "sks": 3, "sem": 5, "sks_tm": 0, "sks_p": 3, "jenis": "Wajib"},
    {"kode": "MKU-508", "nama": "Kewirausahaan II",                                      "sks": 0, "sem": 5, "sks_tm": 0, "sks_p": 0, "jenis": "Wajib"},
    # FSTI (13)
    {"kode": "FST-101", "nama": "Dasar Teknologi Digital",                               "sks": 2, "sem": 1, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "FST-102", "nama": "Algoritma dan Pemrograman",                             "sks": 3, "sem": 1, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "FST-203", "nama": "Struktur Data dan Algoritma",                           "sks": 3, "sem": 2, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "FST-204", "nama": "Pengantar Kecerdasan Artifisial & Data",                "sks": 2, "sem": 2, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "FST-205", "nama": "Basic English for IT",                                  "sks": 2, "sem": 2, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "FST-206", "nama": "Etika Profesi & Hukum Digital",                         "sks": 2, "sem": 2, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "FST-207", "nama": "Sistem Basis Data",                                     "sks": 3, "sem": 2, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "FST-408", "nama": "Probabilitas dan Statistika",                           "sks": 3, "sem": 4, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "FST-611", "nama": "Metodologi Penelitian",                                 "sks": 2, "sem": 6, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "FST-610", "nama": "Capstone Project FSTI",                                 "sks": 3, "sem": 7, "sks_tm": 0, "sks_p": 3, "jenis": "Wajib"},
    {"kode": "FST-612", "nama": "Praktik Kerja Lapangan (PKL)",                          "sks": 3, "sem": 7, "sks_tm": 0, "sks_p": 3, "jenis": "Wajib"},
    {"kode": "FST-613", "nama": "Pra-Skripsi / Seminar Proposal",                        "sks": 2, "sem": 7, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "FST-714", "nama": "Skripsi / Tugas Akhir",                                 "sks": 6, "sem": 8, "sks_tm": 0, "sks_p": 6, "jenis": "Wajib"},
    # Core STI (28)
    {"kode": "STI-101", "nama": "Pengantar Sistem dan Teknologi Informasi",              "sks": 2, "sem": 1, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-102", "nama": "Kalkulus",                                              "sks": 3, "sem": 1, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-103", "nama": "Arsitektur dan Organisasi Sistem Teknologi Informasi",  "sks": 3, "sem": 1, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-204", "nama": "Matematika Diskrit dan Logika",                         "sks": 3, "sem": 2, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-205", "nama": "Aljabar Linear dan Matriks",                            "sks": 3, "sem": 2, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-306", "nama": "Analisis dan Perancangan Sistem Informasi",             "sks": 3, "sem": 3, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-307", "nama": "Sistem Cerdas",                                         "sks": 2, "sem": 3, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-308", "nama": "UI/UX Design & Prototyping",                            "sks": 3, "sem": 3, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-309", "nama": "Rekayasa Perangkat Lunak",                              "sks": 3, "sem": 3, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-310", "nama": "Sistem Operasi",                                        "sks": 3, "sem": 3, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-311", "nama": "Web Front End Development",                             "sks": 3, "sem": 3, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-312", "nama": "Jaringan Komputer",                                     "sks": 3, "sem": 3, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-413", "nama": "Machine Learning",                                      "sks": 3, "sem": 4, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-414", "nama": "Pengantar NLP & Information Retrieval",                 "sks": 2, "sem": 4, "sks_tm": 1, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-415", "nama": "Data Warehouse & Business Intelligence",                "sks": 3, "sem": 4, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-416", "nama": "Web Back End Development",                              "sks": 3, "sem": 4, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-417", "nama": "Komputasi Awan (Cloud Computing)",                      "sks": 3, "sem": 4, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-418", "nama": "Dasar Keamanan Informasi",                              "sks": 2, "sem": 4, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-519", "nama": "Keamanan Informasi Lanjut",                             "sks": 3, "sem": 5, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-520", "nama": "Data Mining & Visualisasi Data",                        "sks": 3, "sem": 5, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-521", "nama": "Internet of Things (IoT)",                              "sks": 3, "sem": 5, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-522", "nama": "Pemrograman Aplikasi Mobile",                           "sks": 3, "sem": 5, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-523", "nama": "Manajemen Proyek TI",                                   "sks": 3, "sem": 5, "sks_tm": 3, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-624", "nama": "Integrasi Layanan Cerdas Berbasis AI",                  "sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-625", "nama": "Smart City & Pemerintahan Digital",                     "sks": 2, "sem": 6, "sks_tm": 2, "sks_p": 0, "jenis": "Wajib"},
    {"kode": "STI-626", "nama": "Deep Learning & Neural Networks",                       "sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-627", "nama": "Digital Platform Engineering",                          "sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    {"kode": "STI-728", "nama": "Inovasi Teknologi dan Startup Digital",                 "sks": 3, "sem": 7, "sks_tm": 2, "sks_p": 1, "jenis": "Wajib"},
    # Elektif P1
    {"kode": "STA-501", "nama": "Decision Support Systems",                              "sks": 3, "sem": 5, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STA-601", "nama": "Rekayasa Big Data dan Komputasi Terdistribusi",         "sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STA-602", "nama": "Intelligent Agent Systems",                             "sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STA-701", "nama": "MLOps and AI Pipeline",                                 "sks": 3, "sem": 7, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STA-702", "nama": "Conversational AI and Intelligent Assistant",           "sks": 3, "sem": 7, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STA-703", "nama": "Smart Surveillance and IoT Analytics",                  "sks": 3, "sem": 7, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    # Elektif P2
    {"kode": "STB-501", "nama": "Network Security and Digital Forensics",                "sks": 3, "sem": 5, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STB-601", "nama": "Cloud Architecture & DevOps",                           "sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STB-602", "nama": "Cybersecurity Risk Management",                         "sks": 3, "sem": 6, "sks_tm": 3, "sks_p": 0, "jenis": "Pilihan"},
    {"kode": "STB-701", "nama": "IT Governance & Compliance (COBIT 2019)",               "sks": 3, "sem": 7, "sks_tm": 3, "sks_p": 0, "jenis": "Pilihan"},
    {"kode": "STB-702", "nama": "IT Service Management (ITIL 4)",                        "sks": 3, "sem": 7, "sks_tm": 3, "sks_p": 0, "jenis": "Pilihan"},
    {"kode": "STB-703", "nama": "Enterprise Architecture (TOGAF)",                       "sks": 3, "sem": 7, "sks_tm": 3, "sks_p": 0, "jenis": "Pilihan"},
    # Elektif P3
    {"kode": "STC-501", "nama": "User Experience Research & Design",                     "sks": 3, "sem": 5, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STC-601", "nama": "Rekayasa & Otomasi Proses Bisnis (BPA)",                "sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STC-602", "nama": "Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech)","sks": 3, "sem": 6, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STC-701", "nama": "Immersive Media & XR Development",                      "sks": 3, "sem": 7, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STC-702", "nama": "SaaS Architecture & Multi-Tenancy",                     "sks": 3, "sem": 7, "sks_tm": 2, "sks_p": 1, "jenis": "Pilihan"},
    {"kode": "STC-703", "nama": "Digital Product Management & Agile Practices",          "sks": 3, "sem": 7, "sks_tm": 3, "sks_p": 0, "jenis": "Pilihan"},
]

TARGET_URL = "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"

def launch_chrome():
    """Launch Chrome with remote debugging on port 9222."""
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    fresh_dir = r"C:\Users\admin\AppData\Local\Temp\chrome_fresh_siakad"
    DETACHED_PROCESS = 0x00000008
    subprocess.Popen([
        chrome_path,
        f"--user-data-dir={fresh_dir}",
        "--remote-debugging-port=9222",
        TARGET_URL
    ], creationflags=DETACHED_PROCESS)
    print("Chrome launched. Waiting for CDP...")
    for i in range(10):
        time.sleep(1)
        try:
            with urllib.request.urlopen("http://127.0.0.1:9222/json/version") as resp:
                print(f"CDP active! ({i+1}s)")
                return True
        except Exception:
            print(f"  Waiting... ({i+1}s)")
    return False

def get_existing_mk(page):
    """Parse the existing MK table from SIAKAD and return set of kode_mk."""
    rows = page.query_selector_all("table tbody tr")
    existing = set()
    for row in rows:
        cells = row.query_selector_all("td")
        if cells:
            # Usually kode is in second or third column - try all cells
            for cell in cells:
                txt = cell.inner_text().strip()
                # Match codes like MKU-101, FST-102, STI-103, STA-501, STB-601, STC-701
                import re
                if re.match(r'^(MKU|FST|STI|STA|STB|STC)-\d{3}$', txt):
                    existing.add(txt)
                    break
    return existing

def find_add_button(page):
    """Find the 'Tambah' or similar add button."""
    for sel in ["a:has-text('Tambah')", "button:has-text('Tambah')",
                "a:has-text('+ Tambah')", "a.btn-primary", "button.btn-primary",
                "a:has-text('Add')", ".btn-success"]:
        btn = page.query_selector(sel)
        if btn:
            return btn
    return None

def fill_form_and_submit(page, mk):
    """Fill in the add-MK form and submit."""
    print(f"  Filling form for {mk['kode']} - {mk['nama'][:40]}...")
    
    # Wait for form to load
    page.wait_for_load_state("networkidle", timeout=15000)
    time.sleep(0.5)
    
    # Helper: try multiple selectors
    def fill(selectors, value):
        for sel in selectors:
            el = page.query_selector(sel)
            if el:
                el.triple_click()
                el.fill(str(value))
                return True
        print(f"    WARNING: Could not find field for value '{value}'")
        return False
    
    def select_option(selectors, value, by_text=None):
        for sel in selectors:
            el = page.query_selector(sel)
            if el:
                if by_text:
                    el.select_option(label=by_text)
                else:
                    el.select_option(value=str(value))
                return True
        return False
    
    # Save the page HTML for inspection
    with open("_tools/form_page.html", "w", encoding="utf-8") as f:
        f.write(page.content())
    print("    Saved form HTML to _tools/form_page.html")
    
    return False  # Will be implemented after inspecting form HTML

def main():
    # Check if Chrome CDP is already active
    try:
        with urllib.request.urlopen("http://127.0.0.1:9222/json/version") as resp:
            print("CDP already active!")
    except Exception:
        print("CDP not active, launching Chrome...")
        if not launch_chrome():
            print("ERROR: Could not start Chrome with CDP. Exiting.")
            sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0]
        pages = context.pages
        page = pages[0] if pages else context.new_page()

        print(f"Connected! Current URL: {page.url}")
        print(f"Title: {page.title()}")

        # Navigate to target page
        if TARGET_URL not in page.url:
            print(f"Navigating to {TARGET_URL}")
            page.goto(TARGET_URL)
            page.wait_for_load_state("networkidle", timeout=30000)

        print(f"Page URL after nav: {page.url}")
        print(f"Page title: {page.title()}")

        # Save page HTML for inspection
        with open("_tools/siakad_page.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        print("Saved page HTML to _tools/siakad_page.html")

        # Check if login is needed
        current_url = page.url
        if "login" in current_url.lower() or "auth" in current_url.lower():
            print("\n⚠️  LOGIN REQUIRED!")
            print("Please login manually in the opened Chrome browser.")
            print("Press ENTER here after logging in...")
            input()
            page.goto(TARGET_URL)
            page.wait_for_load_state("networkidle", timeout=30000)

        # Get existing courses
        existing = get_existing_mk(page)
        print(f"\nFound {len(existing)} existing MK codes in table:")
        for code in sorted(existing):
            print(f"  - {code}")

        # Find missing
        missing = [mk for mk in COURSES_2026 if mk["kode"] not in existing]
        print(f"\nMissing MK ({len(missing)} courses to add):")
        for mk in missing:
            print(f"  - {mk['kode']}: {mk['nama'][:50]}")

        # Save inspection report
        report = {
            "existing": sorted(list(existing)),
            "missing": [{"kode": m["kode"], "nama": m["nama"]} for m in missing],
            "total_expected": len(COURSES_2026),
        }
        with open("_tools/siakad_inspection.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print("\nSaved inspection report to _tools/siakad_inspection.json")

if __name__ == "__main__":
    main()
