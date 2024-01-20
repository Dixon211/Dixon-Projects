#include <iostream>
#include <string>
#include <windows.h>

int create_window (HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow) {

    

    const wchar_t CLASS_NAME[] = L"Just Chatting";
    
    WNDCLASS window = { };

    window.lpfnWndProc = WindowProc;
    window.hInstance = hInstance;
    window.lpszClassName = CLASS_NAME;

    RegisterClass(&window);

    HWND hwnd = CreateWindowEX(
        0,   //option styles
        CLASS_NAME, //class
        L"Just Chatting", //title
        WS_OVERLAPPEDWINDOW, //style

        //size + position
        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,

        NULL, //Parent Window
        NULL, //Menu
        hInstance, //Instance handle
        NULL, //addition app data
    );
if (hwnd = NULL) {
    return 0;
}

ShowWindow(hwnd, nCmdShow);
}

int main () {
    LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    create_window(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow);
    return 0;

}