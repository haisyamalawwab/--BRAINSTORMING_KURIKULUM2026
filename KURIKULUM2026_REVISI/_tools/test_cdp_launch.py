import subprocess
import time
import os

cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--remote-debugging-port=9222",
    "--remote-allow-origins=*",
    r"--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data",
    "--profile-directory=Profile 2",
    "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"
]

print("Launching Chrome...")
proc = subprocess.Popen(cmd)
print("Chrome PID:", proc.pid)

time.sleep(3)

# Check if process is alive
print("Poll proc:", proc.poll())

# Check netstat for 9222
ns = subprocess.check_output("netstat -ano | findstr 9222", shell=True, text=True, stderr=subprocess.STDOUT) if os.system("netstat -ano | findstr 9222 > nul") == 0 else "NO LISTENING PORT 9222"
print("Netstat result:\n", ns)
