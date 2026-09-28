@echo off
REM ========================================================================
REM GENERATOR RPS DOCX - STI-416 Web Back End Development
REM Program Studi Sistem dan Teknologi Informasi (SISTEKIN) FSTI UWG
REM ========================================================================

echo.
echo ========================================================================
echo    GENERATOR RPS DOCX - STI-416 Web Back End Development
echo    Kurikulum SISTEKIN 2026 - FSTI Universitas Widyagama Malang
echo ========================================================================
echo.

cd /d "%~dp0"

echo [*] Menjalankan generator RPS DOCX...
echo.

python _tools\generate_rps_sti416_docx.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================================
    echo [SUKSES] RPS DOCX berhasil di-generate!
    echo ========================================================================
    echo.
    echo File tersimpan di: DOCX\RPS_STI-416_Web_Back_End_Development.docx
    echo.
    echo Tekan tombol apapun untuk membuka folder DOCX...
    pause > nul
    explorer DOCX
) else (
    echo.
    echo ========================================================================
    echo [ERROR] Terjadi kesalahan saat generate RPS DOCX!
    echo ========================================================================
    echo.
    pause
)
