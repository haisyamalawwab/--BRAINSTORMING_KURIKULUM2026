import urllib.request
import json

try:
    data = json.loads(urllib.request.urlopen("http://localhost:9222/json").read().decode())
    print(f"Successfully connected to Chrome port 9222! Total targets: {len(data)}")
    for p in data:
        print(f"[{p.get('type')}] {p.get('title')} -> {p.get('url')}")
except Exception as e:
    print(f"Failed to connect to port 9222: {e}")
