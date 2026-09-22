# -*- coding: utf-8 -*-
"""
siakad_flow.py
Workflow lengkap automasi SIAKAD:
1. Membuka Chrome di port 9222 dengan profil Profile 2 (via junction SIAKAD_Automation)
2. Memantau proses login Google Auth oleh pengguna
3. Setelah login berhasil, navigasi ke https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ
4. Menginspeksi tabel MK dan form Tambah MK
5. Menyiapkan input data MK yang belum ada
"""

import sys
import os
import time
import json
import subprocess
import urllib.request
import websockets
import asyncio

CHROME_EXE = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
AUTO_DIR = r"C:\Users\admin\AppData\Local\Google\Chrome\SIAKAD_Automation"
TARGET_URL = "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"

def ensure_junction():
    os.makedirs(AUTO_DIR, exist_ok=True)
    target_junc = os.path.join(AUTO_DIR, "Profile 2")
    if not os.path.exists(target_junc):
        cmd = ["cmd", "/c", "mklink", "/J", target_junc, r"C:\Users\admin\AppData\Local\Google\Chrome\User Data\Profile 2"]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    src_ls = r"C:\Users\admin\AppData\Local\Google\Chrome\User Data\Local State"
    dst_ls = os.path.join(AUTO_DIR, "Local State")
    if os.path.exists(src_ls) and not os.path.exists(dst_ls):
        import shutil
        shutil.copy2(src_ls, dst_ls)

def is_cdp_ready():
    try:
        res = urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=2).read()
        return True
    except Exception:
        return False

def start_chrome():
    ensure_junction()
    if is_cdp_ready():
        print("[*] Chrome port 9222 sudah aktif.")
        return None
    
    print("[*] Meluncurkan Chrome dengan Profile 2 dan port 9222...")
    cmd = [
        CHROME_EXE,
        "--remote-debugging-port=9222",
        "--remote-allow-origins=*",
        f"--user-data-dir={AUTO_DIR}",
        "--profile-directory=Profile 2",
        "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"
    ]
    proc = subprocess.Popen(cmd, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
    
    for i in range(15):
        time.sleep(1)
        if is_cdp_ready():
            print(f"[+] Chrome berhasil aktif dan mendengarkan port 9222 (PID: {proc.pid})")
            return proc
    print("[-] Peringatan: Port 9222 belum terdeteksi setelah 15 detik.")
    return proc

async def cdp_eval(ws, expr, msg_id):
    req = {
        "id": msg_id,
        "method": "Runtime.evaluate",
        "params": {
            "expression": expr,
            "returnByValue": True,
            "awaitPromise": True
        }
    }
    await ws.send(json.dumps(req))
    while True:
        raw = await ws.recv()
        data = json.loads(raw)
        if data.get("id") == msg_id:
            return data.get("result", {}).get("result", {}).get("value")

async def cdp_navigate(ws, url, msg_id):
    req = {
        "id": msg_id,
        "method": "Page.navigate",
        "params": {"url": url}
    }
    await ws.send(json.dumps(req))
    while True:
        raw = await ws.recv()
        data = json.loads(raw)
        if data.get("id") == msg_id:
            break

async def main():
    start_chrome()
    
    # Ambil daftar target halaman
    targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8"))
    page_target = next((t for t in targets if t.get("type") == "page" and ("siakad" in t.get("url", "") or "google" in t.get("url", ""))), None)
    if not page_target:
        page_target = next((t for t in targets if t.get("type") == "page"), None)
        
    if not page_target:
        print("[-] Tidak ada target halaman Chrome yang ditemukan.")
        return

    ws_url = page_target["webSocketDebuggerUrl"]
    print(f"[*] Terhubung ke halaman: {page_target.get('title')} ({page_target.get('url')})")
    
    async with websockets.connect(ws_url) as ws:
        msg_id = 1
        
        # 1. Tunggu Login Pengguna
        print("\n" + "="*70)
        print(">>> SILAKAN LAKUKAN LOGIN GOOGLE AUTH PADA JENDELA BROWSER CHROME <<<")
        print("Sistem memantau sesi login secara otomatis...")
        print("="*70 + "\n", flush=True)
        
        while True:
            curr_url = await cdp_eval(ws, "window.location.href", msg_id)
            msg_id += 1
            curr_title = await cdp_eval(ws, "document.title", msg_id)
            msg_id += 1
            
            # Cek jika sudah berada di siakad dan bukan di gate login atau accounts.google
            if curr_url and "siakad.widyagama.ac.id" in curr_url:
                if "/gate/login" not in curr_url and "accounts.google.com" not in curr_url:
                    print(f"\n[+] Login terdeteksi berhasil! Judul: '{curr_title}', URL: {curr_url}", flush=True)
                    break
            
            print(f"[*] Menunggu login Google Auth... Halaman saat ini: {str(curr_url)[:65]}", flush=True)
            await asyncio.sleep(3)
            
        # 2. Arahkan ke TARGET_URL jika belum di sana
        if TARGET_URL not in curr_url:
            print(f"[*] Mengarahkan ke halaman target: {TARGET_URL}", flush=True)
            await cdp_navigate(ws, TARGET_URL, msg_id)
            msg_id += 1
            await asyncio.sleep(4)
            
        # 3. Tunggu halaman selesai memuat
        print("[*] Menginspeksi halaman Daftar Mata Kuliah Kurikulum...", flush=True)
        
        # Cek apakah ada tabel dan tombol tambah
        inspect_script = """
        (() => {
            const ths = Array.from(document.querySelectorAll('table thead th, table th')).map(th => th.innerText.trim());
            const rows = Array.from(document.querySelectorAll('table tbody tr')).map(tr => {
                return Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim().replace(/\\s+/g, ' '));
            });
            
            const buttons = Array.from(document.querySelectorAll('button, a.btn, a[href*="tambah"], a[href*="add"], a[href*="salin"], a[href*="insert"]')).map(b => ({
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
                ths: ths,
                rowsCount: rows.length,
                sampleRows: rows.slice(0, 10),
                allRows: rows,
                buttons: buttons
            };
        })()
        """
        data = await cdp_eval(ws, inspect_script, msg_id)
        msg_id += 1
        
        print("\n" + "="*50)
        print("=== STATUS DATA SIAKAD TERKINI ===")
        print(f"Judul: {data.get('title')}")
        print(f"URL: {data.get('url')}")
        print(f"Kolom Tabel: {data.get('ths')}")
        print(f"Jumlah Baris Terdaftar: {data.get('rowsCount')}")
        print("="*50)
        
        if data.get('sampleRows'):
            print("\nSampel 5 Data MK yang sudah ada di SIAKAD:")
            for r in data.get('sampleRows')[:5]:
                print(" -", r)
        else:
            print("\nBelum ada Mata Kuliah yang terdaftar (Tabel Kosong).")
            
        print("\nTombol/Aksi yang Tersedia:")
        for b in data.get('buttons', []):
            if b.get('text') or b.get('href'):
                print(f" - [{b.get('text')}] (href: {b.get('href')}, class: {b.get('className')})")
                
        # Simpan ke file json
        with open("siakad_current_state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("\n[+] Hasil inspeksi disimpan di siakad_current_state.json")

if __name__ == "__main__":
    asyncio.run(main())
