#include <iostream>
#include <windows.h>

int main () {
    OSVERSIONINFO osVersionInfo;
    osVersionInfo.dwOSVersionInfoSize =sizeof(OSVERSIONINFO);

    if (GetVersionEx(&osVersionInfo)) {
        std::cout << "Windows Version: " << osVersionInfo.dwMajorVersion << "." << osVersionInfo.dwMinorVersion << std::endl;
} else {
    std::cerr << "Error gettting system information." << std::endl;
}
return 0;
}