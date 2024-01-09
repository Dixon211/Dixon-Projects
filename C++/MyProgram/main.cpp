#include <iostream>
#include <windows.h>
#include "cleanup/cleanup.h"
#include "GUI/GUIWindow.h"





int main () {
   

   MyWinMain(GetModuleHandle(nullptr), nullptr, GetCommandLineW(), SW_SHOW);
 
    
    Cleanup ();
    return 0;
}