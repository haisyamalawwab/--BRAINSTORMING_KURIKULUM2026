/**
 * app.js — Modular Frontend Script for Kurikulum KPT-OBE SISTEKIN 2026
 * Program Studi Sistem dan Teknologi Informasi (S1) FSTI UWG Malang
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Management (Dark / Light / Sepia Mode)
    initTheme();

    // 2. Reader Layout & Font Size Controls
    initReaderControls();

    // 3. Dynamic Quick Jump / TOC Generator
    initQuickTOC();

    // 4. Mermaid Diagram Initialization
    initMermaid();

    // 5. Live Table Search Filter (for Document Pages)
    initTableSearch();

    // 6. Live Portal Cards Filter (for index.html)
    initPortalSearch();

    // 7. Print Helper & Triggers
    initPrintHelper();
});

/**
 * Theme Management with 3 states: dark, light, sepia
 */
function initTheme() {
    const themeToggle = document.getElementById('themeToggle');
    const themeBtnDark = document.getElementById('themeBtnDark');
    const themeBtnLight = document.getElementById('themeBtnLight');
    const themeBtnSepia = document.getElementById('themeBtnSepia');

    const themes = ['dark', 'light', 'sepia'];
    let currentTheme = localStorage.getItem('sistekin_theme') || 'light';
    setTheme(currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const nextIdx = (themes.indexOf(currentTheme) + 1) % themes.length;
            setTheme(themes[nextIdx]);
        });
    }

    if (themeBtnDark) themeBtnDark.addEventListener('click', () => setTheme('dark'));
    if (themeBtnLight) themeBtnLight.addEventListener('click', () => setTheme('light'));
    if (themeBtnSepia) themeBtnSepia.addEventListener('click', () => setTheme('sepia'));

    function setTheme(t) {
        currentTheme = t;
        document.documentElement.setAttribute('data-theme', t);
        localStorage.setItem('sistekin_theme', t);

        // Update active class on toolbar buttons if present
        [themeBtnDark, themeBtnLight, themeBtnSepia].forEach(btn => {
            if (btn) btn.classList.remove('active');
        });
        if (t === 'dark' && themeBtnDark) themeBtnDark.classList.add('active');
        if (t === 'light' && themeBtnLight) themeBtnLight.classList.add('active');
        if (t === 'sepia' && themeBtnSepia) themeBtnSepia.classList.add('active');

        // Re-render mermaid if loaded
        if (typeof mermaid !== 'undefined') {
            const mTheme = t === 'dark' ? 'dark' : (t === 'sepia' ? 'neutral' : 'default');
            try {
                mermaid.initialize({ startOnLoad: false, theme: mTheme });
            } catch (e) {}
        }
    }
}

/**
 * Reader Layout Controls: Font size (Small, Normal, Large) & Width Mode (Normal, Wide)
 */
function initReaderControls() {
    const btnFontMinus = document.getElementById('btnFontMinus');
    const btnFontReset = document.getElementById('btnFontReset');
    const btnFontPlus = document.getElementById('btnFontPlus');
    const btnWidthToggle = document.getElementById('btnWidthToggle');

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
    }

    // Width mode toggle (Normal / Wide for multi-column tables)
    let isWide = localStorage.getItem('sistekin_wide_mode') === 'true';
    if (isWide) document.body.classList.add('reading-wide');
    if (btnWidthToggle) {
        updateWidthBtn();
        btnWidthToggle.addEventListener('click', () => {
            isWide = !isWide;
            document.body.classList.toggle('reading-wide', isWide);
            localStorage.setItem('sistekin_wide_mode', isWide);
            updateWidthBtn();
        });
    }

    function updateWidthBtn() {
        if (!btnWidthToggle) return;
        btnWidthToggle.innerHTML = isWide ? '↔️ Lebar Standar' : '↔️ Lebar Penuh (Tabel)';
        btnWidthToggle.classList.toggle('active', isWide);
    }
}

/**
 * Dynamic Quick Jump / TOC Generator from Headings
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
        opt.textContent = prefix + h.innerText.trim().slice(0, 45);
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
 * Initialize Mermaid diagram rendering with responsive styling
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
 * Live Table Search Filter for Document Pages with row matching
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
 * Live Portal Cards Filter for index.html
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
 * Print Helper & Triggers
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
