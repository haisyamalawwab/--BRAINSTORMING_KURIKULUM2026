import subprocess
import json

cmd = ["powershell", "-NoProfile", "-Command", "Get-CimInstance Win32_Process -Filter \"name = 'chrome.exe'\" | Select-Object ProcessId, CommandLine | ConvertTo-Json"]
try:
    res = subprocess.check_output(cmd, text=True)
    data = json.loads(res)
    if isinstance(data, dict):
        data = [data]
    print(f"Total chrome processes: {len(data)}")
    for p in data:
        cmdline = p.get('CommandLine') or ''
        if '--type=' not in cmdline:
            print("MAIN BROWSER PROCESS:", p.get('ProcessId'), cmdline)
except Exception as e:
    print("Error:", e)
