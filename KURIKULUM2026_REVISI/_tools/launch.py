import subprocess
import time
import urllib.request

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--remote-debugging-port=9222",
    r"--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data",
    "--profile-directory=Profile 2",
    "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"
]

proc = subprocess.Popen(cmd, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
print("Launched Chrome, PID:", proc.pid)

for i in range(10):
    time.sleep(1)
    try:
        data = urllib.request.urlopen("http://localhost:9222/json", timeout=2).read().decode()
        print("Success! CDP responding!")
        break
    except Exception as e:
        print(f"Waiting for CDP... ({e})")
