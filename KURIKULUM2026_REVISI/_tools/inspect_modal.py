import urllib.request
import json
import asyncio
import websockets

async def inspect_add_modal():
    targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8"))
    page = next((t for t in targets if t.get("type") == "page" and "list_mkkurikulum" in t.get("url", "")), None)
    if not page:
        print("Page not found")
        return
    
    ws_url = page["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url) as ws:
        # Click Tambah button and inspect modal HTML
        script = """
        (() => {
            // Find Tambah button
            const tambahBtn = Array.from(document.querySelectorAll('button, a.btn')).find(b => b.innerText.trim() === 'Tambah');
            if (tambahBtn) {
                tambahBtn.click();
            }
            
            // Wait for modal or inspect all forms
            const modals = Array.from(document.querySelectorAll('.modal')).map(m => ({
                id: m.id,
                class: m.className,
                style: m.getAttribute('style'),
                html: m.innerHTML.slice(0, 1500)
            }));
            
            const formElements = Array.from(document.querySelectorAll('form input, form select, form textarea, .modal input, .modal select')).map(el => ({
                tag: el.tagName,
                type: el.type,
                name: el.name,
                id: el.id,
                class: el.className,
                value: el.value,
                options: el.tagName === 'SELECT' ? Array.from(el.options).map(o => ({val: o.value, text: o.text})) : null
            }));
            
            return {
                clicked: !!tambahBtn,
                modals: modals,
                formElements: formElements
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
        print(json.dumps(val, indent=2))

asyncio.run(inspect_add_modal())
