# -*- coding: utf-8 -*-
"""
wait_and_navigate_siakad.py
Menunggu pengguna menyelesaikan login Google di browser Chrome (port 9222),
lalu otomatis mengarahkan ke halaman:
https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ
dan menginspeksi elemen tombol 'Tambah' / 'Import' serta form yang ada.
"""

import asyncio
import json
import time
import urllib.request
import websockets

TARGET_URL = "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"

async def main():
    print("Menghubungkan ke Chrome di port 9222...")
    while True:
        try:
            pages = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
            break
        except Exception as e:
            print(f"Menunggu Chrome siap... ({e})")
            time.sleep(2)
            
    page = next((p for p in pages if p.get("type") == "page" and ("siakad" in p.get("url", "") or "google" in p.get("url", ""))), None)
    if not page:
        page = next((p for p in pages if p.get("type") == "page"), None)
        
    print(f"Halaman aktif ditemukan: {page.get('title')} ({page.get('url')[:60]}...)")
    ws_url = page["webSocketDebuggerUrl"]
    
    async with websockets.connect(ws_url) as ws:
        msg_id = 1
        
        # 1. Loop menunggu login selesai
        print("Menunggu proses login Google oleh pengguna selesai...")
        while True:
            # Dapatkan URL terkini
            cmd = {"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": "window.location.href", "returnByValue": True}}
            msg_id += 1
            await ws.send(json.dumps(cmd))
            res = json.loads(await ws.recv())
            curr_url = res.get("result", {}).get("result", {}).get("value", "")
            
            # Jika sudah kembali ke siakad dan bukan di gate/login atau sso
            if "siakad.widyagama.ac.id" in curr_url and "/gate/login" not in curr_url and "accounts.google.com" not in curr_url:
                print(f"\nLogin terdeteksi sukses! URL saat ini: {curr_url}")
                break
            
            print(f"Menunggu login... (Halaman saat ini: {curr_url[:50]}...)", end="\r")
            await asyncio.sleep(2)
            
        # 2. Arahkan ke TARGET_URL jika belum di sana
        if curr_url != TARGET_URL:
            print(f"\nMengarahkan ke halaman target: {TARGET_URL}")
            cmd = {"id": msg_id, "method": "Page.navigate", "params": {"url": TARGET_URL}}
            msg_id += 1
            await ws.send(json.dumps(cmd))
            await ws.recv()
            await asyncio.sleep(4)
            
        # 3. Inspeksi elemen di halaman TARGET_URL
        print("Menginspeksi struktur halaman target...")
        inspect_code = """
        (() => {
            const buttons = Array.from(document.querySelectorAll('button, a.btn, a[href*="tambah"], a[href*="import"], a[href*="salin"]')).map(b => ({
                tag: b.tagName,
                text: b.innerText.trim().replace(/\\s+/g, ' '),
                href: b.href || '',
                id: b.id || '',
                class: b.className || ''
            }));
            
            const tableHeaders = Array.from(document.querySelectorAll('table thead th')).map(th => th.innerText.trim());
            const rowsCount = document.querySelectorAll('table tbody tr').length;
            
            return {
                title: document.title,
                url: window.location.href,
                buttons: buttons,
                tableHeaders: tableHeaders,
                rowsCount: rowsCount
            };
        })()
        """
        cmd = {"id": msg_id, "method": "Runtime.evaluate", "params": {"expression": inspect_code, "returnByValue": True}}
        msg_id += 1
        await ws.send(json.dumps(cmd))
        res = json.loads(await ws.recv())
        data = res.get("result", {}).get("result", {}).get("value", {})
        
        print("\n=== HASIL INSPEKSI HALAMAN SIAKAD ===")
        print(f"Judul: {data.get('title')}")
        print(f"URL: {data.get('url')}")
        print(f"Jumlah Baris MK yang sudah ada: {data.get('rowsCount')}")
        print("Header Tabel:", data.get('tableHeaders'))
        print("\nTombol Aksi Ditemukan:")
        for b in data.get("buttons", []):
            if b.get("text"):
                print(f"  - [{b.get('text')}] (href: {b.get('href')}, class: {b.get('class')})")

if __name__ == "__main__":
    asyncio.run(main())
