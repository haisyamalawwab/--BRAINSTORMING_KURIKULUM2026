import os
import shutil
import subprocess
import time
import urllib.request

src_profile = r"C:\Users\admin\AppData\Local\Google\Chrome\User Data\Profile 2"
dst_user_data = r"C:\Users\admin\AppData\Local\Temp\chrome_siakad_user_data"
dst_profile = os.path.join(dst_user_data, "Profile 2")

os.makedirs(dst_user_data, exist_ok=True)

# Copy Local State if exists
local_state = r"C:\Users\admin\AppData\Local\Google\Chrome\User Data\Local State"
if os.path.exists(local_state) and not os.path.exists(os.path.join(dst_user_data, "Local State")):
    try:
        shutil.copy2(local_state, os.path.join(dst_user_data, "Local State"))
    except Exception as e:
        print("Copy Local State error:", e)

if not os.path.exists(dst_profile):
    print("Copying Profile 2 to temp directory...")
    # Fast copy ignoring locks
    cmd = f'robocopy "{src_profile}" "{dst_profile}" /MIR /R:0 /W:0 /XF lockfile *lock* *Journal* *journal* /NDL /NFL'
    subprocess.run(cmd, shell=True)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
args = [
    chrome_path,
    f"--user-data-dir={dst_user_data}",
    "--profile-directory=Profile 2",
    "--remote-debugging-port=9222",
    "https://siakad.widyagama.ac.id/siakad/list_mkkurikulum/MjAyNi81OTIwMQ"
]

print("Launching Chrome as detached process...")
DETACHED_PROCESS = 0x00000008
subprocess.Popen(args, creationflags=DETACHED_PROCESS)

# Wait up to 10 seconds for port 9222
for i in range(10):
    time.sleep(1)
    try:
        with urllib.request.urlopen("http://127.0.0.1:9222/json/version") as resp:
            print("Chrome CDP is active! Output:")
            print(resp.read().decode())
            break
    except Exception as e:
        print(f"Waiting for Chrome ({i+1}/10)...")
