import urllib.request
import json
import asyncio
import websockets

async def inspect_select2():
    targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8"))
    page = next((t for t in targets if t.get("type") == "page" and "list_mkkurikulum" in t.get("url", "")), None)
    
    ws_url = page["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url) as ws:
        script = """
        (() => {
            const s2 = $('#idmk').data('select2');
            let ajaxUrl = null;
            if (s2 && s2.options && s2.options.options && s2.options.options.ajax) {
                ajaxUrl = s2.options.options.ajax.url;
            }
            
            // Check button click event or form submission handler
            const btn = $('button[data-type="insert"]');
            
            return {
                hasJQuery: typeof $ !== 'undefined',
                select2Options: s2 ? {
                    ajaxUrl: ajaxUrl,
                    ajax: s2.options.options.ajax
                } : null
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

asyncio.run(inspect_select2())
