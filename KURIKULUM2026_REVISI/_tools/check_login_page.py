import urllib.request
import json
import asyncio
import websockets

async def check_login_page():
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
                    const googleBtn = document.querySelector('a[href*="google"], button[id*="google"], a.btn-google, .btn-social');
                    const links = Array.from(document.querySelectorAll('a, button')).map(el => ({
                        text: el.innerText.trim(),
                        href: el.href || '',
                        id: el.id || '',
                        class: el.className || ''
                    }));
                    return {
                        url: window.location.href,
                        title: document.title,
                        hasGoogleBtn: !!googleBtn,
                        googleBtnText: googleBtn ? googleBtn.innerText : null,
                        googleBtnHref: googleBtn ? googleBtn.href : null,
                        links: links.filter(l => l.text)
                    };
                })()
                """,
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(msg))
        res = json.loads(await ws.recv())
        val = res.get("result", {}).get("result", {}).get("value", {})
        print(json.dumps(val, indent=2))

asyncio.run(check_login_page())
