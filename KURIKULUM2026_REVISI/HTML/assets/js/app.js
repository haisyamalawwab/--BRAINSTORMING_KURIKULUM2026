/**
 * app.js — Master Reader, Layout, and Export Script for Kurikulum KPT-OBE SISTEKIN 2026
 * Program Studi Sistem dan Teknologi Informasi (S1) FSTI UWG Malang
 * Features:
 *  - E-book & Print Ready (A4 PDF & EPUB compatible)
 *  - High-Readability Controls (Font Size, Narrow/Normal/Wide Layout, Sans/Serif Font)
 *  - One-Click Table Export to Excel & Word (HTML + TSV Dual Clipboard)
 *  - One-Click Full Document Copy for Word/Docs
 *  - Toast Notifications & Dynamic Quick Jump TOC
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Management (Light / Dark / Sepia)
    initTheme();

    // 2. Reader Layout & Typography Controls
    initReaderControls();

    // 3. One-Click Table Export (Word & Excel)
    initTableExport();

    // 4. One-Click Full Document Copy (Word Ready)
    initDocExport();

    // 5. Dynamic Quick Jump / TOC Generator
    initQuickTOC();

    // 6. Mermaid Diagram Initialization
    initMermaid();

    // 7. Live Table Search Filter (for Document Pages)
    initTableSearch();

    // 8. Live Portal Cards Filter (for index.html)
    initPortalSearch();

    // 9. Print Helper & Triggers
    initPrintHelper();
});

/**
 * 1. Theme Management with 3 states: light (Executive Academic), dark (OLED), sepia (Eye-Comfort Book)
 */
function initTheme() {
    const themeToggle = document.getElementById('themeToggle');
    const themeBtnLight = document.getElementById('themeBtnLight');
    const themeBtnSepia = document.getElementById('themeBtnSepia');
    const themeBtnDark = document.getElementById('themeBtnDark');

    const themes = ['light', 'sepia', 'dark'];
    let currentTheme = localStorage.getItem('sistekin_theme') || 'light';
    setTheme(currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const nextIdx = (themes.indexOf(currentTheme) + 1) % themes.length;
            setTheme(themes[nextIdx]);
        });
    }

    if (themeBtnLight) themeBtnLight.addEventListener('click', () => setTheme('light'));
    if (themeBtnSepia) themeBtnSepia.addEventListener('click', () => setTheme('sepia'));
    if (themeBtnDark) themeBtnDark.addEventListener('click', () => setTheme('dark'));

    function setTheme(t) {
        currentTheme = t;
        document.documentElement.setAttribute('data-theme', t);
        localStorage.setItem('sistekin_theme', t);

        [themeBtnLight, themeBtnSepia, themeBtnDark].forEach(btn => {
            if (btn) btn.classList.remove('active');
        });
        if (t === 'light' && themeBtnLight) themeBtnLight.classList.add('active');
        if (t === 'sepia' && themeBtnSepia) themeBtnSepia.classList.add('active');
        if (t === 'dark' && themeBtnDark) themeBtnDark.classList.add('active');

        // Re-render mermaid theme if active
        if (typeof mermaid !== 'undefined') {
            const mTheme = t === 'dark' ? 'dark' : (t === 'sepia' ? 'neutral' : 'default');
            try {
                mermaid.initialize({ startOnLoad: false, theme: mTheme });
            } catch (e) {}
        }
    }
}

/**
 * 2. Reader Layout Controls: Font size (A-, A, A+), Width Mode (Narrow, Normal, Wide), & Font Family (Sans / Serif)
 */
function initReaderControls() {
    const btnFontMinus = document.getElementById('btnFontMinus');
    const btnFontReset = document.getElementById('btnFontReset');
    const btnFontPlus = document.getElementById('btnFontPlus');
    const btnFontToggle = document.getElementById('btnFontToggle');

    const btnWidthNarrow = document.getElementById('btnWidthNarrow');
    const btnWidthNormal = document.getElementById('btnWidthNormal');
    const btnWidthWide = document.getElementById('btnWidthWide');
    const btnWidthToggle = document.getElementById('btnWidthToggle'); // Legacy fallback

    // --- A. Font Size Controls ---
    const fontSizes = [
        { name: 'small', base: '14.5px', table: '0.82rem' },
        { name: 'normal', base: '16px', table: '0.88rem' },
        { name: 'large', base: '18px', table: '0.96rem' }
    ];

    let currentFontIdx = parseInt(localStorage.getItem('sistekin_fontsize_idx') || '1', 10);
    applyFontSize(currentFontIdx);

    if (btnFontMinus) {
        btnFontMinus.addEventListener('click', () => {
            if (currentFontIdx > 0) {
                currentFontIdx--;
                applyFontSize(currentFontIdx);
            }
        });
    }

    if (btnFontReset) {
        btnFontReset.addEventListener('click', () => {
            currentFontIdx = 1;
            applyFontSize(currentFontIdx);
        });
    }

    if (btnFontPlus) {
        btnFontPlus.addEventListener('click', () => {
            if (currentFontIdx < fontSizes.length - 1) {
                currentFontIdx++;
                applyFontSize(currentFontIdx);
            }
        });
    }

    function applyFontSize(idx) {
        const conf = fontSizes[idx] || fontSizes[1];
        document.documentElement.style.setProperty('--base-font-size', conf.base);
        document.documentElement.style.setProperty('--table-font-size', conf.table);
        localStorage.setItem('sistekin_fontsize_idx', idx);

        [btnFontMinus, btnFontReset, btnFontPlus].forEach(btn => btn && btn.classList.remove('active'));
        if (idx === 0 && btnFontMinus) btnFontMinus.classList.add('active');
        if (idx === 1 && btnFontReset) btnFontReset.classList.add('active');
        if (idx === 2 && btnFontPlus) btnFontPlus.classList.add('active');
    }

    // --- B. Font Family Toggle (Modern Sans vs Academic Serif) ---
    let isSerif = localStorage.getItem('sistekin_font_serif') === 'true';
    applyFontFamily(isSerif);

    if (btnFontToggle) {
        btnFontToggle.addEventListener('click', () => {
            isSerif = !isSerif;
            applyFontFamily(isSerif);
            showToast(isSerif ? '📖 Tipografi: Academic Book Serif' : '🅰️ Tipografi: Modern Sans-Serif');
        });
    }

    function applyFontFamily(serif) {
        document.body.classList.toggle('font-serif', serif);
        localStorage.setItem('sistekin_font_serif', serif);
        if (btnFontToggle) {
            btnFontToggle.innerHTML = serif ? '📖 Serif' : '🔤 Sans';
            btnFontToggle.classList.toggle('active', serif);
        }
    }

    // --- C. Width Layout Controls (Narrow: 860px | Normal: 1240px | Wide: 98vw) ---
    let currentWidthMode = localStorage.getItem('sistekin_width_mode') || 'normal';
    applyWidthMode(currentWidthMode);

    if (btnWidthNarrow) btnWidthNarrow.addEventListener('click', () => applyWidthMode('narrow'));
    if (btnWidthNormal) btnWidthNormal.addEventListener('click', () => applyWidthMode('normal'));
    if (btnWidthWide) btnWidthWide.addEventListener('click', () => applyWidthMode('wide'));

    // Legacy fallback button support
    if (btnWidthToggle) {
        btnWidthToggle.addEventListener('click', () => {
            const nextMode = currentWidthMode === 'wide' ? 'normal' : 'wide';
            applyWidthMode(nextMode);
        });
    }

    function applyWidthMode(mode) {
        currentWidthMode = mode;
        document.body.classList.remove('reading-narrow', 'reading-normal', 'reading-wide');

        if (mode === 'narrow') {
            document.body.classList.add('reading-narrow');
        } else if (mode === 'wide') {
            document.body.classList.add('reading-wide');
        } else {
            document.body.classList.add('reading-normal');
        }

        localStorage.setItem('sistekin_width_mode', mode);

        [btnWidthNarrow, btnWidthNormal, btnWidthWide].forEach(btn => btn && btn.classList.remove('active'));
        if (mode === 'narrow' && btnWidthNarrow) btnWidthNarrow.classList.add('active');
        if (mode === 'normal' && btnWidthNormal) btnWidthNormal.classList.add('active');
        if (mode === 'wide' && btnWidthWide) btnWidthWide.classList.add('active');

        if (btnWidthToggle) {
            btnWidthToggle.innerHTML = mode === 'wide' ? '↔️ Lebar Standar' : '↔️ Lebar Penuh (Tabel)';
            btnWidthToggle.classList.toggle('active', mode === 'wide');
        }
    }
}

/**
 * 3. One-Click Table Export to Excel and Word (Dual Clipboard: HTML Table + TSV)
 */
function initTableExport() {
    const tables = document.querySelectorAll('main.content table');
    if (tables.length === 0) return;

    tables.forEach((table, idx) => {
        // Check if action bar already exists
        const prevEl = table.previousElementSibling;
        if (prevEl && prevEl.classList.contains('table-header-action')) return;

        // Create Header Action Bar
        const actionBar = document.createElement('div');
        actionBar.className = 'table-header-action no-print';

        const rowCount = table.querySelectorAll('tbody tr').length || table.querySelectorAll('tr').length - 1;
        const countText = rowCount > 0 ? `${rowCount} baris data` : 'Tabel data';

        actionBar.innerHTML = `
            <span class="table-title-text">📊 ${countText}</span>
            <button type="button" class="btn-copy-table" title="Salin tabel ke Clipboard (bisa langsung paste di MS Excel atau MS Word)">
                📋 Salin ke Excel / Word
            </button>
        `;

        try {
            if (table.parentNode) {
                table.parentNode.insertBefore(actionBar, table);
            } else {
                table.insertAdjacentElement('beforebegin', actionBar);
            }

            const copyBtn = actionBar.querySelector('.btn-copy-table');
            copyBtn.addEventListener('click', async () => {
                await copyTableToClipboard(table, copyBtn);
            });
        } catch (e) {
            console.warn('Skipped table export bar insertion for nested table:', e);
        }
    });
}

/**
 * Helper: Copy Table to Clipboard in both HTML format (for Word) and TSV (for Excel)
 */
async function copyTableToClipboard(tableEl, buttonEl) {
    try {
        // 1. Generate Plain Text (TSV for Excel)
        const rows = Array.from(tableEl.querySelectorAll('tr'));
        const tsv = rows.map(row => {
            const cells = Array.from(row.querySelectorAll('th, td'));
            return cells.map(cell => {
                let text = cell.innerText.replace(/[\r\n]+/g, ' ').trim();
                if (text.includes('\t') || text.includes('"')) {
                    text = `"${text.replace(/"/g, '""')}"`;
                }
                return text;
            }).join('\t');
        }).join('\r\n');

        // 2. Generate Clean HTML Table with Inline Styles (for Word & Docs)
        const clonedTable = tableEl.cloneNode(true);
        clonedTable.setAttribute('border', '1');
        clonedTable.setAttribute('style', 'border-collapse: collapse; width: 100%; font-family: Calibri, "Segoe UI", Arial, sans-serif; font-size: 10pt; color: #1a1a1a;');

        clonedTable.querySelectorAll('th').forEach(th => {
            th.setAttribute('style', 'background-color: #1F3864; color: #ffffff; font-weight: bold; border: 1px solid #4a6382; padding: 6px 10px; text-align: left;');
        });

        clonedTable.querySelectorAll('td').forEach(td => {
            td.setAttribute('style', 'border: 1px solid #cbd5e1; padding: 5px 8px; vertical-align: top;');
        });

        clonedTable.querySelectorAll('tbody tr:nth-child(even) td').forEach(td => {
            td.style.backgroundColor = '#f4f8fc';
        });

        let success = false;

        // Try modern Async Clipboard API
        if (navigator.clipboard && window.ClipboardItem) {
            try {
                const blobHtml = new Blob([clonedTable.outerHTML], { type: 'text/html' });
                const blobText = new Blob([tsv], { type: 'text/plain' });
                const item = new ClipboardItem({
                    'text/html': blobHtml,
                    'text/plain': blobText
                });
                await navigator.clipboard.write([item]);
                success = true;
            } catch (e) {
                // Ignore error and fall back to execCommand
            }
        }

        // Fallback using contentEditable element & execCommand
        if (!success) {
            const tempDiv = document.createElement('div');
            tempDiv.contentEditable = 'true';
            tempDiv.style.position = 'fixed';
            tempDiv.style.left = '-9999px';
            tempDiv.style.top = '-9999px';
            tempDiv.innerHTML = clonedTable.outerHTML;
            document.body.appendChild(tempDiv);

            const selection = window.getSelection();
            const range = document.createRange();
            range.selectNodeContents(tempDiv);
            selection.removeAllRanges();
            selection.addRange(range);

            try {
                success = document.execCommand('copy');
            } catch (err) {
                success = false;
            }

            selection.removeAllRanges();
            tempDiv.remove();
        }

        // Ultimate fallback to plain text if HTML copy was blocked
        if (!success && navigator.clipboard && navigator.clipboard.writeText) {
            try {
                await navigator.clipboard.writeText(tsv);
                success = true;
            } catch (e) {}
        }

        if (success) {
            const originalText = buttonEl.innerHTML;
            buttonEl.innerHTML = '✅ Tersalin!';
            buttonEl.classList.add('copied');
            showToast('✅ Tabel berhasil disalin! Silakan paste (Ctrl+V) di Excel atau Word.');

            setTimeout(() => {
                buttonEl.innerHTML = originalText;
                buttonEl.classList.remove('copied');
            }, 2500);
        } else {
            showToast('⚠️ Gagal menyalin otomatis. Silakan blok tabel dan tekan Ctrl+C.');
        }

    } catch (err) {
        console.error('Failed to copy table: ', err);
        showToast('⚠️ Gagal menyalin tabel. Silakan blok tabel dan tekan Ctrl+C.');
    }
}

/**
 * 4. One-Click Full Document Copy for Word/Docs
 */
function initDocExport() {
    const btnCopyDoc = document.getElementById('btnCopyDocument');
    if (!btnCopyDoc) return;

    btnCopyDoc.addEventListener('click', async () => {
        try {
            const mainContent = document.querySelector('main.content');
            if (!mainContent) return;

            // Clone content and remove no-print elements
            const cloned = mainContent.cloneNode(true);
            cloned.querySelectorAll('.no-print, .table-header-action, .doc-nav').forEach(el => el.remove());

            // Add standard Word-friendly inline styling
            cloned.querySelectorAll('table').forEach(t => {
                t.setAttribute('border', '1');
                t.setAttribute('style', 'border-collapse: collapse; width: 100%; font-family: Calibri, Arial, sans-serif; font-size: 10pt;');
                t.querySelectorAll('th').forEach(th => {
                    th.setAttribute('style', 'background-color: #1F3864; color: #ffffff; font-weight: bold; border: 1px solid #4a6382; padding: 6px 10px;');
                });
                t.querySelectorAll('td').forEach(td => {
                    td.setAttribute('style', 'border: 1px solid #cbd5e1; padding: 5px 8px; vertical-align: top;');
                });
            });

            const htmlContent = `
                <div style="font-family: Calibri, 'Segoe UI', Arial, sans-serif; font-size: 11pt; line-height: 1.6; color: #1a1a1a;">
                    ${cloned.innerHTML}
                </div>
            `;
            const textContent = cloned.innerText;
            let success = false;

            if (navigator.clipboard && window.ClipboardItem) {
                try {
                    const blobHtml = new Blob([htmlContent], { type: 'text/html' });
                    const blobText = new Blob([textContent], { type: 'text/plain' });
                    const item = new ClipboardItem({
                        'text/html': blobHtml,
                        'text/plain': blobText
                    });
                    await navigator.clipboard.write([item]);
                    success = true;
                } catch (e) {}
            }

            if (!success) {
                const tempDiv = document.createElement('div');
                tempDiv.contentEditable = 'true';
                tempDiv.style.position = 'fixed';
                tempDiv.style.left = '-9999px';
                tempDiv.style.top = '-9999px';
                tempDiv.innerHTML = htmlContent;
                document.body.appendChild(tempDiv);

                const selection = window.getSelection();
                const range = document.createRange();
                range.selectNodeContents(tempDiv);
                selection.removeAllRanges();
                selection.addRange(range);

                try {
                    success = document.execCommand('copy');
                } catch (err) {
                    success = false;
                }

                selection.removeAllRanges();
                tempDiv.remove();
            }

            if (success) {
                const orig = btnCopyDoc.innerHTML;
                btnCopyDoc.innerHTML = '✅ Dokumen Tersalin!';
                showToast('📋 Seluruh dokumen disalin! Silakan buka MS Word dan tekan Ctrl+V.');
                setTimeout(() => {
                    btnCopyDoc.innerHTML = orig;
                }, 3000);
            } else {
                showToast('⚠️ Gagal menyalin dokumen.');
            }

        } catch (e) {
            console.error(e);
            showToast('⚠️ Gagal menyalin dokumen.');
        }
    });
}

/**
 * 5. Toast Notification System
 */
function showToast(message) {
    let container = document.querySelector('.toast-container');
    if (!container) {
        container = document.createElement('div');
        container.className = 'toast-container no-print';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = message;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(12px)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 2800);
}

/**
 * 6. Dynamic Quick Jump / TOC Generator from Headings
 */
function initQuickTOC() {
    const quickSelect = document.getElementById('quickJumpSelect');
    if (!quickSelect) return;

    const headings = document.querySelectorAll('main.content h2, main.content h3');
    if (headings.length === 0) {
        quickSelect.style.display = 'none';
        return;
    }

    quickSelect.innerHTML = '<option value="">📑 Lompat ke Bagian...</option>';
    headings.forEach((h, idx) => {
        if (!h.id) {
            h.id = 'sec-' + idx + '-' + h.innerText.slice(0, 24).toLowerCase().replace(/[^a-z0-9]+/g, '-');
        }
        const opt = document.createElement('option');
        opt.value = h.id;
        const prefix = h.tagName.toLowerCase() === 'h3' ? '    ↳ ' : '• ';
        opt.textContent = prefix + h.innerText.trim().slice(0, 48);
        quickSelect.appendChild(opt);
    });

    quickSelect.addEventListener('change', (e) => {
        const targetId = e.target.value;
        if (targetId) {
            const targetEl = document.getElementById(targetId);
            if (targetEl) {
                targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    });
}

/**
 * 7. Initialize Mermaid diagram rendering with responsive styling
 */
function initMermaid() {
    if (typeof mermaid !== 'undefined') {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        const mTheme = currentTheme === 'dark' ? 'dark' : (currentTheme === 'sepia' ? 'neutral' : 'default');
        try {
            mermaid.initialize({
                startOnLoad: true,
                theme: mTheme,
                flowchart: { curve: 'basis', useMaxWidth: true },
                securityLevel: 'loose'
            });
        } catch (e) {
            console.warn('Mermaid init deferred', e);
        }
    }
}

/**
 * 8. Live Table Search Filter for Document Pages with row matching
 */
function initTableSearch() {
    const searchInput = document.getElementById('globalTableSearch');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        const tableRows = document.querySelectorAll('main.content table tbody tr');

        if (tableRows.length === 0) {
            const allRows = document.querySelectorAll('main.content table tr');
            allRows.forEach((row, idx) => {
                if (idx === 0 && row.querySelector('th')) return;
                const text = row.innerText.toLowerCase();
                row.style.display = (query === '' || text.includes(query)) ? '' : 'none';
            });
            return;
        }

        tableRows.forEach(row => {
            const text = row.innerText.toLowerCase();
            row.style.display = (query === '' || text.includes(query)) ? '' : 'none';
        });
    });
}

/**
 * 9. Live Portal Cards Filter for index.html
 */
function initPortalSearch() {
    const portalSearchInput = document.getElementById('portalSearchInput');
    if (!portalSearchInput) return;

    portalSearchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        const cards = document.querySelectorAll('.portal-card, .card');

        cards.forEach(card => {
            const text = card.innerText.toLowerCase();
            card.style.display = (query === '' || text.includes(query)) ? '' : 'none';
        });
    });
}

/**
 * 10. Print Helper & Triggers
 */
function initPrintHelper() {
    const printBtns = document.querySelectorAll('.btn-print, [data-action="print"]');
    printBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            window.print();
        });
    });
}
