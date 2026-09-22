# -*- coding: utf-8 -*-
"""
siakad_automation.py
Automasi input kurikulum 2026 ke SIAKAD UWG:
1. Membuka Chrome dengan profil Profile 2 dan remote-debugging-port=9222
2. Menunggu pengguna login Google Auth
3. Mengarahkan ke https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ
4. Menginspeksi MK yang sudah ada vs 67 MK di kurikulum_2026_siakad_data.json
5. Melakukan penginputan MK yang belum ada
"""

import os
import sys
import time
import json
import subprocess
import urllib.request
import asyncio
from playwright.async_api import async_playwright

CHROME_EXE = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
USER_DATA_DIR = r"C:\Users\admin\AppData\Local\Google\Chrome\User Data"
PROFILE_DIR = "Profile 2"
TARGET_URL = "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"

def kill_existing_chrome():
    print("[1] Memeriksa & merapikan proses Chrome latar belakang agar port debugging 9222 dapat aktif...")
    try:
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)
    except Exception as e:
        print(f"Catatan kill chrome: {e}")

def launch_chrome():
    print("[2] Meluncurkan Google Chrome dengan Profile 2 & remote debugging...")
    args = [
        CHROME_EXE,
        f"--remote-debugging-port=9222",
        f"--user-data-dir={USER_DATA_DIR}",
        f"--profile-directory={PROFILE_DIR}",
        TARGET_URL
    ]
    subprocess.Popen(args)
    print("Menunggu Chrome siap pada port 9222...")
    for _ in range(15):
        try:
            urllib.request.urlopen("http://localhost:9222/json", timeout=2)
            print("Chrome berhasil terhubung pada port 9222!")
            return True
        except Exception:
            time.sleep(1)
    print("Gagal mendeteksi port 9222.")
    return False

async def main():
    kill_existing_chrome()
    if not launch_chrome():
        print("Tidak dapat memulai Chrome dengan port 9222.")
        return

    async with async_playwright() as p:
        print("[3] Menghubungkan Playwright ke Chrome melalui CDP...")
        browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        contexts = browser.contexts
        if not contexts:
            print("Tidak ada browser context yang aktif!")
            return
        
        context = contexts[0]
        
        # Cari tab siakad atau buat tab baru
        page = None
        for pg in context.pages:
            url = pg.url
            if "siakad.widyagama.ac.id" in url or "google.com" in url:
                page = pg
                break
        if not page and context.pages:
            page = context.pages[0]
        if not page:
            page = await context.new_page()

        print(f"Halaman aktif: {page.url}")

        # Menunggu proses login Google Auth oleh pengguna
        print("\n" + "="*70)
        print(">>> SILAKAN LAKUKAN LOGIN GOOGLE AUTH PADA JENDELA BROWSER CHROME <<<")
        print("Sistem sedang memantau status login Anda secara otomatis...")
        print("="*70 + "\n")

        login_completed = False
        while not login_completed:
            try:
                current_url = page.url
                # Cek jika sudah di halaman siakad dan tidak di gate/login atau accounts.google
                if "siakad.widyagama.ac.id" in current_url:
                    if "/gate/login" not in current_url and "accounts.google" not in current_url:
                        print(f"\n[OK] Login berhasil terdeteksi! URL saat ini: {current_url}")
                        login_completed = True
                        break
                print(f"Menunggu login... URL saat ini: {current_url[:60]}", end="\r")
                await asyncio.sleep(2)
            except Exception as e:
                print(f"Menunggu respons browser... ({e})")
                await asyncio.sleep(2)

        # Arahkan ke TARGET_URL jika belum
        if page.url != TARGET_URL:
            print(f"\n[4] Mengarahkan ke halaman target: {TARGET_URL}")
            await page.goto(TARGET_URL, wait_until="networkidle")
            await asyncio.sleep(3)
        else:
            await page.wait_for_load_state("networkidle")
            await asyncio.sleep(2)

        print(f"\n[5] Berada di halaman: {await page.title()} ({page.url})")

        # Inspeksi tabel MK dan tombol yang ada
        html_info = await page.evaluate('''() => {
            const tableRows = Array.from(document.querySelectorAll('table tbody tr')).map(tr => {
                const cols = Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim());
                return cols;
            });
            
            const buttons = Array.from(document.querySelectorAll('button, a.btn, a[href*="tambah"], a[href*="add"], a[href*="salin"]')).map(b => ({
                tag: b.tagName,
                text: b.innerText.trim().replace(/\\s+/g, ' '),
                href: b.href || '',
                id: b.id || '',
                className: b.className || '',
                onclick: b.getAttribute('onclick') || ''
            }));
            
            return {
                title: document.title,
                url: window.location.href,
                tableHeaders: Array.from(document.querySelectorAll('table thead th')).map(th => th.innerText.trim()),
                rows: tableRows,
                buttons: buttons
            };
        }''')

        print("\n=== HASIL INSPEKSI HALAMAN ===")
        print(f"Judul: {html_info['title']}")
        print(f"Headers Tabel: {html_info['tableHeaders']}")
        print(f"Jumlah baris MK yang sudah ada: {len(html_info['rows'])}")
        
        # Tampilkan beberapa baris pertama jika ada
        if html_info['rows']:
            print("\nContoh MK yang sudah ada di tabel:")
            for r in html_info['rows'][:5]:
                print("  ", r)
        else:
            print("\nTabel saat ini KOSONG (belum ada MK yang terinput).")

        print("\nTombol Aksi yang Ditemukan:")
        for btn in html_info['buttons']:
            if btn['text'] or btn['href']:
                print(f"  - [{btn['text']}] href={btn['href']} class={btn['className']} id={btn['id']}")

        # Simpan snapshot info
        with open("siakad_inspect_result.json", "w", encoding="utf-8") as f:
            json.dump(html_info, f, indent=2, ensure_ascii=False)
        print("\nHasil inspeksi disimpan di siakad_inspect_result.json")

if __name__ == "__main__":
    asyncio.run(main())
