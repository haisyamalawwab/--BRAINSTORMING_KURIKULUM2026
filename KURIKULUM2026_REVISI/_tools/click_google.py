import urllib.request
import json
import asyncio
import websockets

async def click_google_login():
    targets = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read().decode("utf-8"))
    page = next((t for t in targets if t.get("type") == "page" and "siakad" in t.get("url", "")), None)
    if not page:
        print("Page not found")
        return
    
    ws_url = page["webSocketDebuggerUrl"]
    async with websockets.connect(ws_url) as ws:
        msg = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": """
                (() => {
                    const btn = document.querySelector('a[href*="google"], a.btn-default');
                    if (btn) {
                        btn.click();
                        return "Clicked Google button: " + btn.href;
                    }
                    return "Button not found";
                })()
                """,
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        print(res.get("result", {}).get("result", {}).get("value"))

asyncio.run(click_google_login())
