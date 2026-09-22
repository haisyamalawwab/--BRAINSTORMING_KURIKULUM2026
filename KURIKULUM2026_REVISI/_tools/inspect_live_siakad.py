import urllib.request
import json
import asyncio
import websockets

async def inspect_live_page():
    targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8"))
    page = next((t for t in targets if t.get("type") == "page" and "list_mkkurikulum" in t.get("url", "")), None)
    if not page:
        print("Mata Kuliah Kurikulum page not found in targets")
        return
    
    print(f"Target found: {page.get('title')} ({page.get('url')})")
    ws_url = page["webSocketDebuggerUrl"]
    
    async with websockets.connect(ws_url) as ws:
        # Evaluate script
        script = """
        (() => {
            const userEl = document.querySelector('.user-menu, .navbar-custom-menu, .username, .user-name');
            const roleEl = document.querySelector('.role, .user-role, .sidebar-menu');
            
            const rows = Array.from(document.querySelectorAll('table tbody tr')).map(tr => {
                return Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim().replace(/\\s+/g, ' '));
            });
            
            const headers = Array.from(document.querySelectorAll('table thead th')).map(th => th.innerText.trim());
            
            // Periksa form modal tambah
            const modal = document.querySelector('#modal-form, .modal, form');
            const formInputs = Array.from(document.querySelectorAll('form input, form select, form textarea, .modal input, .modal select')).map(el => ({
                id: el.id,
                name: el.name,
                type: el.type || el.tagName,
                placeholder: el.placeholder || '',
                value: el.value || ''
            }));
            
            const buttons = Array.from(document.querySelectorAll('button, a.btn')).map(b => ({
                text: b.innerText.trim().replace(/\\s+/g, ' '),
                id: b.id,
                class: b.className,
                href: b.href || '',
                onclick: b.getAttribute('onclick') || ''
            }));
            
            return {
                title: document.title,
                url: window.location.href,
                headers: headers,
                rowCount: rows.length,
                rows: rows,
                buttons: buttons,
                formInputs: formInputs
            };
        })()
        """
        req = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": script,
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(req))
        res = json.loads(await ws.recv())
        val = res.get("result", {}).get("result", {}).get("value", {})
        
        print("=== LIVE PAGE INSPECTION ===")
        print(f"Title: {val.get('title')}")
        print(f"URL: {val.get('url')}")
        print(f"Headers: {val.get('headers')}")
        print(f"Total Rows: {val.get('rowCount')}")
        print("\nAll Rows currently in SIAKAD:")
        for r in val.get('rows', []):
            print("  ", r)
            
        print("\nButtons found:")
        for b in val.get('buttons', []):
            if b.get('text') or 'tambah' in (b.get('class') or '').lower() or 'add' in (b.get('id') or '').lower():
                print("  ", b)
                
        with open("live_siakad_mks.json", "w", encoding="utf-8") as f:
            json.dump(val, f, indent=2, ensure_ascii=False)
            
asyncio.run(inspect_live_page())
