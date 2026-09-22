import ctypes
from ctypes import wintypes
import os

user32 = ctypes.windll.user32

def enum_windows_proc(hwnd, lparam):
    if user32.IsWindowVisible(hwnd):
        length = user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            buff = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buff, length + 1)
            pid = wintypes.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            title = buff.value
            if "chrome" in title.lower() or "google" in title.lower() or "siakad" in title.lower():
                print(f"PID: {pid.value} | Title: {title}")
    return True

WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
user32.EnumWindows(WNDENUMPROC(enum_windows_proc), 0)
print("Done checking visible windows.")
