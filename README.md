# SilentKiller-virus

This program is a virus designed to "kill" Windows operating systems. It supports a wide range of Windows versions, from the **9x series** (like Windows 95, Windows 98, and Windows 98 SE) all the way up to **Windows 11**.

---
## Important Notes

* **Compatibility:** This virus **doesn't work** on NT-based Windows versions released before Windows XP, such as Windows 2000 or Windows NT 3.1.
* **Version Naming:** The terms "old" and "new" for the virus versions **don't refer to their release dates**. Instead, the "old" version is designed for older operating systems, and the "new" version is for newer ones. Both versions were released at the same time.
* **Usage:** You should only use **SilentKiller.exe**. This is a self-extracting archive (SFX) that contains both the "old" and "new" virus versions, along with a **dispatcher** program. The dispatcher is a C-based executable designed to work across a broad range of Windows versions. It automatically launches the correct virus version based on the operating system: the "old" version for Windows versions before XP, and the "new" version for Windows XP and later.
* **Repository Files:** Any executable files in this repository other than SilentKiller.exe are simply components already found inside SilentKiller.exe. They're included separately for clarity.
* **UAC (User Account Control):** UAC is crucial for the "new" version of the virus. UAC has been removed from the "old" version, the dispatcher, and the main SFX itself by modifying their manifests.
* **Disclaimer:** I'm not responsible for any harm caused by this program. It was created solely to demonstrate methods and approaches for developing such software.

---
## Files Map in SilentKiller.exe:

````├── SilentKiller.exe (MAIN/top-level SFX file, responsible for initial extraction and execution)
│   ├── silentkiller_old.exe (Nested SFX file; contains components for the older virus version) (this is the virus old version exe, a SFX)
│   │   ├── MSVCR71.dll # Microsoft Visual C++ Runtime Library (v7.1), a common dependency for applications compiled with old Visual C++ versions (and they are the supported/important versions for old OSes like 95, 98, etc.).
│   │   ├── silentkiller.exe # The old version of the virus executable (this is the real executable or program of the virus (old version or 9x series version)).
│   │   ├── unicows.dll # Unicode Common Controls Library, provides Unicode support for applications running on old Windows systems (e.g., Windows 95/98/ME).
│   │   ├── viruslogo.ico # The icon file associated with/used by the virus.
│   │   └── w9xpopen.exe # This program is a crucial component for enabling communication with the operating system and its APIs. It facilitates the execution of various system-level tasks, such as processing command-line instructions (e.g., via cmd.exe). Without W9XPOPEN.exe, certain functionalities requiring direct interaction with the system's core processes and libraries would be unavailable.
│   ├── silentkiller_new.exe # The new version of the virus executable (this is the executable or program of the virus (new version and it's for Windows versions that are XP (NT 5.1) or newer (> NT 5.1)).
│   └── dispatcher.exe # The primary executable launched by the main SFX; determines and executes either the old (pre-Windows XP) or new (Windows XP or later) virus version based on OS detection.````