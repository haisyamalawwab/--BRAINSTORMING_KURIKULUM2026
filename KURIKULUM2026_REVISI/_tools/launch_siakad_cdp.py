import subprocess
import time
import urllib.request
import json

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--remote-debugging-port=9222",
    "--remote-allow-origins=*",
    r"--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\SIAKAD_Automation",
    "--profile-directory=Profile 2",
    "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"
]

proc = subprocess.Popen(cmd)
print("Launched PID:", proc.pid)
time.sleep(3)
try:
    data = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json", timeout=3).read().decode())
    print(f"SUCCESS! Connected to Chrome port 9222! Total targets: {len(data)}")
    for p in data:
        print(f" - [{p.get('type')}] {p.get('title')} -> {p.get('url')}")
except Exception as e:
    print("Failed:", e)
