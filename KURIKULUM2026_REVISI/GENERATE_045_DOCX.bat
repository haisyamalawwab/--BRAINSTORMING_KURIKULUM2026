@echo off
chcp 65001 > nul
echo ======================================================================
echo    GENERATE 045 DOKUMEN KPT DOCX DARI HTML (SISTEKIN UWG 2026)
echo ======================================================================
echo.

python "%~dp0_tools\convert_045_html_to_docx.py"

echo.
pause
