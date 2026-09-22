# -*- coding: utf-8 -*-
import json

data005 = json.load(open("kurikulum_2026_siakad_data.json", encoding="utf-8"))

# Definisi nama Indonesia dan nama Inggris baku untuk seluruh 67 MK
TRANSLATIONS = {
    # MKWU (8 MK)
    "MKU-101": ("Agama I", "Religious Education I"),
    "MKU-102": ("Pancasila", "Pancasila Education"),
    "MKU-103": ("Bahasa Indonesia", "Indonesian Language"),
    "MKU-204": ("Kewirausahaan I", "Entrepreneurship I"),
    "MKU-405": ("Kewarganegaraan", "Civic Education"),
    "MKU-406": ("Agama II", "Religious Education II"),
    "MKU-507": ("Kuliah Pengabdian Kepada Masyarakat (KPM)", "Community Service Program (KPM)"),
    "MKU-508": ("Kewirausahaan II", "Entrepreneurship II"),

    # FSTI (13 MK)
    "FST-101": ("Dasar Teknologi Digital", "Fundamentals of Digital Technology"),
    "FST-102": ("Algoritma dan Pemrograman", "Algorithms and Programming"),
    "FST-203": ("Struktur Data dan Algoritma", "Data Structures and Algorithms"),
    "FST-204": ("Pengantar Kecerdasan Artifisial & Data", "Introduction to Artificial Intelligence and Data"),
    "FST-205": ("Bahasa Inggris Dasar untuk TI", "Basic English for IT"),
    "FST-206": ("Etika Profesi & Hukum Digital", "Professional Ethics & Cyber Law"),
    "FST-207": ("Sistem Basis Data", "Database Systems"),
    "FST-408": ("Probabilitas dan Statistika", "Probability and Statistics"),
    "FST-610": ("Capstone Project FSTI", "FSTI Multidisciplinary Capstone Project"),
    "FST-611": ("Metodologi Penelitian", "Research Methodology"),
    "FST-612": ("Praktik Kerja Lapangan (PKL)", "Field Work Practice / Internship"),
    "FST-613": ("Pra-Skripsi / Seminar Proposal", "Pre-Thesis / Proposal Seminar"),
    "FST-714": ("Skripsi / Tugas Akhir", "Undergraduate Thesis / Final Project"),

    # CORE STI (28 MK)
    "STI-101": ("Pengantar Sistem dan Teknologi Informasi", "Introduction to Systems and Information Technology"),
    "STI-102": ("Kalkulus", "Calculus"),
    "STI-103": ("Arsitektur dan Organisasi Sistem Teknologi Informasi", "Information Technology Systems Architecture and Organization"),
    "STI-204": ("Matematika Diskrit dan Logika", "Discrete Mathematics and Logic"),
    "STI-205": ("Aljabar Linear dan Matriks", "Linear Algebra and Matrices"),
    "STI-306": ("Analisis dan Perancangan Sistem Informasi", "Information Systems Analysis and Design"),
    "STI-307": ("Sistem Cerdas", "Intelligent Systems"),
    "STI-308": ("Desain & Prototyping UI/UX", "UI/UX Design & Prototyping"),
    "STI-309": ("Rekayasa Perangkat Lunak", "Software Engineering"),
    "STI-310": ("Sistem Operasi", "Operating Systems"),
    "STI-311": ("Pengembangan Web Front End", "Web Front End Development"),
    "STI-312": ("Jaringan Komputer", "Computer Networks"),
    "STI-413": ("Pembelajaran Mesin", "Machine Learning"),
    "STI-414": ("Pengantar NLP & Temu Balik Informasi", "Introduction to NLP & Information Retrieval"),
    "STI-415": ("Gudang Data & Kecerdasan Bisnis", "Data Warehouse & Business Intelligence"),
    "STI-416": ("Pengembangan Web Back End", "Web Back End Development"),
    "STI-417": ("Komputasi Awan", "Cloud Computing"),
    "STI-418": ("Dasar Keamanan Informasi", "Fundamentals of Information Security"),
    "STI-519": ("Keamanan Informasi Lanjut", "Advanced Information Security"),
    "STI-520": ("Penambangan Data & Visualisasi Data", "Data Mining & Data Visualization"),
    "STI-521": ("Internet untuk Segala (IoT)", "Internet of Things (IoT)"),
    "STI-522": ("Pemrograman Aplikasi Mobile", "Mobile Application Programming"),
    "STI-523": ("Manajemen Proyek TI", "IT Project Management"),
    "STI-624": ("Integrasi Layanan Cerdas Berbasis AI", "AI-Based Smart Service Integration"),
    "STI-625": ("Smart City & Pemerintahan Digital", "Smart City & Digital Governance"),
    "STI-626": ("Pembelajaran Mendalam & Jaringan Saraf", "Deep Learning & Neural Networks"),
    "STI-627": ("Rekayasa Platform Digital", "Digital Platform Engineering"),
    "STI-728": ("Inovasi Teknologi dan Startup Digital", "Technology Innovation and Digital Startup"),

    # PEMINATAN 1: INTEGRATED SMART SYSTEMS (6 MK)
    "STA-501": ("Sistem Pendukung Keputusan", "Decision Support Systems"),
    "STA-601": ("Rekayasa Big Data dan Komputasi Terdistribusi", "Big Data Engineering and Distributed Systems"),
    "STA-602": ("Sistem Agen Cerdas", "Intelligent Agent Systems"),
    "STA-701": ("MLOps dan Alur Pipa AI", "MLOps and AI Pipeline"),
    "STA-702": ("AI Percakapan dan Asisten Cerdas", "Conversational AI and Intelligent Assistant"),
    "STA-703": ("Pengawasan Cerdas dan Analitika IoT", "Smart Surveillance and IoT Analytics"),

    # PEMINATAN 2: CLOUD INFRASTRUCTURE & CYBERSECURITY (6 MK)
    "STB-501": ("Keamanan Jaringan dan Forensik Digital", "Network Security and Digital Forensics"),
    "STB-601": ("Arsitektur Cloud & DevOps", "Cloud Architecture & DevOps"),
    "STB-602": ("Manajemen Risiko Keamanan Siber", "Cybersecurity Risk Management"),
    "STB-701": ("Tata Kelola & Kepatuhan TI (COBIT 2019)", "IT Governance & Compliance (COBIT 2019)"),
    "STB-702": ("Manajemen Layanan TI (ITIL 4)", "IT Service Management (ITIL 4)"),
    "STB-703": ("Arsitektur Enterprise (TOGAF)", "Enterprise Architecture (TOGAF)"),

    # PEMINATAN 3: DIGITAL PLATFORM ENGINEERING (6 MK)
    "STC-501": ("Riset & Desain Pengalaman Pengguna (UX)", "User Experience Research & Design"),
    "STC-601": ("Rekayasa & Otomasi Proses Bisnis (BPA)", "Business Process Engineering & Automation (BPA)"),
    "STC-602": ("Rekayasa Aplikasi Industri Vertikal (FinTech & EdTech)", "Vertical Industry Application Engineering (FinTech & EdTech)"),
    "STC-701": ("Media Imersif & Pengembangan XR", "Immersive Media & XR Development"),
    "STC-702": ("Arsitektur SaaS & Multi-Tenansi", "SaaS Architecture & Multi-Tenancy"),
    "STC-703": ("Manajemen Produk Digital & Praktik Agile", "Digital Product Management & Agile Practices")
}

courses_dict = {}
for c in data005:
    code = c["kode"]
    if code in TRANSLATIONS:
        nama_id, nama_en = TRANSLATIONS[code]
    else:
        nama_id = c["nama"]
        nama_en = c["nama"]

    courses_dict[code] = {
        "kode": code,
        "nama_id": nama_id,
        "nama_en": nama_en,
        "sks": c["sks"],
        "tipe": c["tipe"],
        "semester": c["semester"],
        "prasyarat": c["prasyarat"],
        "kategori": c["kategori"]
    }

with open("courses_id_en_master.json", "w", encoding="utf-8") as f:
    json.dump(courses_dict, f, indent=2, ensure_ascii=False)

print(f"Master 67 MK ID & EN berhasil diperbarui. Total: {len(courses_dict)}")
