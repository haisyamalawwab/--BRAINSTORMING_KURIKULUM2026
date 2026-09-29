@echo off
REM ===================================================================
REM  GENERATOR RPS STI-416 VERSI 2 (SIMPLIFIED PYTHON FOCUS) - DOCX
REM  One-Click Generator untuk RPS Markdown ke Microsoft Word
REM ===================================================================

echo.
echo ====================================================================
echo   GENERATOR RPS STI-416 VERSI 2 (SIMPLIFIED PYTHON FOCUS) - DOCX
echo ====================================================================
echo.

REM Pindah ke direktori KURIKULUM2026_REVISI
cd /d "%~dp0"

REM Jalankan Python script
python _tools\generate_rps_sti416_v2_docx.py

REM Cek hasil eksekusi
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ====================================================================
    echo   ✅ SUKSES! File DOCX telah di-generate
    echo ====================================================================
    echo.
    echo 📁 Membuka folder DOCX...
    start "" "DOCX"
) else (
    echo.
    echo ====================================================================
    echo   ❌ GAGAL! Terjadi error saat generate DOCX
    echo ====================================================================
    echo.
    pause
    exit /b 1
)

echo.
echo Tekan tombol apapun untuk menutup...
pause >nul
