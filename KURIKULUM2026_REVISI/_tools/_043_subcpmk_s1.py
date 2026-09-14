# -*- coding: utf-8 -*-
"""Sub-CPMK data for 043 docs — Core STI Semester 1.
2 Sub-CPMK per CPMK, grounded in each CPMK + IN-SCOPE guardrail topics.
Structure: code -> [ (sub_code, text, src_cpmk, bloom), ... ]
"""
SUBCPMK_S1 = {
"STI-101": [
 ("1.1", "Membandingkan konsep data, informasi, dan pengetahuan (DIKW) serta perannya dalam organisasi.", "1", "C2"),
 ("1.2", "Mengidentifikasi komponen pembentuk sistem informasi dan siklus data-ke-informasi pada studi kasus bisnis.", "1", "C2"),
 ("2.1", "Mengklasifikasikan sistem enterprise (TPS, MIS, DSS, ERP, CRM, SCM) berdasarkan fungsi dan penggunanya.", "2", "C4"),
 ("2.2", "Membandingkan peran dan nilai tiap tipe sistem informasi dalam ekosistem industri modern.", "2", "C4"),
 ("3.1", "Menganalisis permasalahan proses bisnis konvensional yang layak ditransformasi digital.", "3", "C5"),
 ("3.2", "Merumuskan usulan solusi transformasi digital berbasis AI, Cloud, dan IoT secara etis dan layak bisnis.", "3", "C5"),
],
"STI-102": [
 ("1.1", "Menghitung limit fungsi aljabar dan transenden serta memeriksa kontinuitas fungsi.", "1", "C3"),
 ("1.2", "Menerapkan teorema limit dan bentuk tak tentu untuk menyelesaikan limit fungsi transenden.", "1", "C3"),
 ("2.1", "Menghitung turunan fungsi univariat dan multivariat beserta gradiennya.", "2", "C3"),
 ("2.2", "Menerapkan turunan pada masalah laju perubahan dan optimasi ekstremum (maksimum/minimum).", "2", "C3"),
 ("3.1", "Menganalisis teknik integrasi substitusi dan parsial untuk integral tentu dan tak tentu.", "3", "C4"),
 ("3.2", "Menghitung integral untuk luasan di bawah kurva dan volume benda putar.", "3", "C4"),
 ("4.1", "Menerapkan turunan parsial dan gradien pada prinsip optimasi Gradient Descent.", "4", "C4"),
 ("4.2", "Menerapkan integral untuk pemodelan luasan data pada fungsi komputasi.", "4", "C4"),
],
"STI-103": [
 ("1.1", "Mengonversi representasi bilangan biner, heksadesimal, dan floating point IEEE 754.", "1", "C3"),
 ("1.2", "Menjelaskan siklus eksekusi instruksi Fetch-Decode-Execute pada arsitektur Von Neumann.", "1", "C3"),
 ("2.1", "Menganalisis gerbang logika biner dan rangkaian kombinasional sebagai dasar ALU.", "2", "C4"),
 ("2.2", "Menganalisis flip-flop dan rangkaian logika sekuensial dasar.", "2", "C4"),
 ("3.1", "Membandingkan karakteristik arsitektur prosesor CISC (x86_64) dan RISC (ARM64/RISC-V).", "3", "C4"),
 ("3.2", "Menganalisis hierarki memori dan cache (L1/L2/L3) serta akselerator GPU/NPU.", "3", "C4"),
 ("4.1", "Mengevaluasi mekanisme bus sistem dan interupsi I/O.", "4", "C5"),
 ("4.2", "Mengevaluasi abstraksi virtualisasi hardware (Hypervisor) dan organisasi server data center untuk cloud.", "4", "C5"),
],
}
