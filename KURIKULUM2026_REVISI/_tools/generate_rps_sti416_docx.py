# -*- coding: utf-8 -*-
"""
Generator RPS DOCX Khusus untuk STI-416 Web Back End Development
Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG
Mengonversi RPS Markdown STI-416 menjadi dokumen DOCX formal sesuai Template RPS OBE UWG
"""

import os
import sys

# Setup path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

# Import existing converter engine
from convert_md_to_docx import parse_markdown_to_docx

def main():
    """Generate RPS DOCX untuk STI-416"""
    
    # Input & Output paths
    input_md = os.path.join(WORKDIR, "RPS_STI-416_Web_Back_End_Development.md")
    output_dir = os.path.join(WORKDIR, "DOCX")
    output_file = os.path.join(output_dir, "RPS_STI-416_Web_Back_End_Development.docx")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Check if input file exists
    if not os.path.exists(input_md):
        print(f"❌ ERROR: File tidak ditemukan: {input_md}")
        return 1
    
    print("=" * 80)
    print("🚀 GENERATOR RPS DOCX — STI-416 Web Back End Development")
    print("=" * 80)
    print(f"📄 Input  : {os.path.basename(input_md)}")
    print(f"📁 Output : {output_file}")
    print("-" * 80)
    
    try:
        # Convert MD to DOCX
        print("⚙️  Memproses konversi Markdown → DOCX...")
        parse_markdown_to_docx(input_md, output_file)
        
        print("=" * 80)
        print("✅ SUKSES! RPS DOCX berhasil di-generate")
        print("=" * 80)
        print(f"📍 Lokasi file: {output_file}")
        print(f"📊 Ukuran    : {os.path.getsize(output_file) / 1024:.2f} KB")
        print("=" * 80)
        print()
        print("📋 Dokumen siap untuk:")
        print("   • Review oleh Tim Kurikulum")
        print("   • Validasi Unit Penjaminan Mutu (UPM)")
        print("   • Pengesahan Ketua Program Studi")
        print("   • Distribusi kepada Dosen Pengampu")
        print("   • Upload ke SIAKAD")
        print("=" * 80)
        
        return 0
        
    except Exception as e:
        print("=" * 80)
        print(f"❌ ERROR: Konversi gagal!")
        print(f"   Detail: {str(e)}")
        print("=" * 80)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
