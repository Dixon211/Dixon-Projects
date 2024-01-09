#include <windows.h>
#include "Accessinfo.h"
#include "string"
#include <iostream>
#include <winreg.h>

std::string Accessinfo() {
    HKEY hkey;
    if (RegOpenKeyEx(HKEY_LOCAL_MACHINE, L"Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall", 0, KEY_READ, &hkey ) == ERROR_SUCCESS) {
        DWORD index = 0;
        WCHAR subkeyName[255];
        while(RegEnumKeyEx(hkey, index, subkeyName, nullptr, nullptr, nullptr, nullptr, nullptr) == ERROR_SUCCESS) {
            HKEY programKey;
            if(RegOpenKeyEx(hkey, subkeyName, 0, KEY_READ, &programKey) == ERROR_SUCCESS) {
                WCHAR displayName[255];
                DWORD size = sizeof(displayName);
                if (RegQueryValueEx(programKey, L"displayName", nullptr, nullptr, reinterpret_cast<LPBYTE>(displayName), &size) == ERROR_SUCCESS) {

                }
            }
        }
    }

std::string message = "this is from accessinfo";

return message;

}