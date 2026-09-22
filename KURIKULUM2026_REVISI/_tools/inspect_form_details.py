import urllib.request
import json
import asyncio
import websockets

async def inspect_add_form():
    targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8"))
    page = next((t for t in targets if t.get("type") == "page" and "list_mkkurikulum" in t.get("url", "")), None)
    
    ws_url = page["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url) as ws:
        script = """
        (() => {
            const el = document.querySelector('#idmk');
            const form = el ? el.closest('form, .modal, .modal-dialog') : null;
            if (!form) return "Not found";
            
            // Cari tombol di dalam form atau modal
            const btns = Array.from(form.querySelectorAll('button, input[type="submit"], a.btn')).map(b => ({
                tag: b.tagName,
                type: b.type,
                text: b.innerText.trim(),
                value: b.value,
                id: b.id,
                class: b.className,
                onclick: b.getAttribute('onclick')
            }));
            
            return {
                formAction: form.action || '',
                formId: form.id || '',
                formClass: form.className || '',
                innerHtml: form.innerHTML,
                buttons: btns
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
        print("Buttons in form:", val.get('buttons'))
        print("Form ID/Action:", val.get('formId'), val.get('formAction'))
        # Simpan modal html
        with open("modal_add_form.html", "w", encoding="utf-8") as f:
            f.write(val.get('innerHtml', ''))

asyncio.run(inspect_add_form())
