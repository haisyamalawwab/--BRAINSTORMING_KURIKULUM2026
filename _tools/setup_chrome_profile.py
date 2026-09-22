import os
import shutil
import subprocess
import time
import socket

src_dir = r"C:\Users\admin\AppData\Local\Google\Chrome\User Data"
dst_dir = r"C:\Users\admin\AppData\Local\Google\Chrome\User Data Temp"

os.makedirs(dst_dir, exist_ok=True)

local_state_src = os.path.join(src_dir, "Local State")
local_state_dst = os.path.join(dst_dir, "Local State")
if os.path.exists(local_state_src):
    try:
        shutil.copy2(local_state_src, local_state_dst)
        print("Copied Local State")
    except Exception as e:
        print("Error copying Local State:", e)

profile_src = os.path.join(src_dir, "Profile 2")
profile_dst = os.path.join(dst_dir, "Profile 2")

print("Syncing Profile 2 directory...")
cmd = f'robocopy "{profile_src}" "{profile_dst}" /MIR /R:0 /W:0 /XF lockfile *lock* *Journal* *journal* /NDL /NFL'
res = subprocess.run(cmd, shell=True)
print("Robocopy exit code:", res.returncode)

print("Launching Chrome...")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
proc = subprocess.Popen([
    chrome_path,
    f"--user-data-dir={dst_dir}",
    "--profile-directory=Profile 2",
    "--remote-debugging-port=9222",
    "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"
])

time.sleep(3)
s = socket.socket()
try:
    s.connect(('127.0.0.1', 9222))
    print("Port 9222 is OPEN successfully!")
except Exception as e:
    print("Port 9222 check failed:", e)
