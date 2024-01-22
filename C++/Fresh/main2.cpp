#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow) {
    const wchar_t CLASS_NAME[] = L"Just Chatting";
    
    WNDCLASS window = { };

    window.lpfnWndProc = WindowProc;
    window.hInstance = hInstance;
    window.lpszClassName = CLASS_NAME;

    //register
    RegisterClass(&window);

    //parentwindow
    HWND parentwin = CreateWindowEx(
        0,   //option styles
        CLASS_NAME, //class
        L"Just Chatting", //title
        WS_OVERLAPPEDWINDOW, //style

        //size + position: x, y, width, height
        500, 500, 500, 500,

        NULL, //Parent Window
        NULL, //Menu
        hInstance, //Instance handle
        NULL //addition app data
         );
if (parentwin == NULL) {
    return 0;
}

//textbox creation
HWND textbox = CreateWindowEx(
    0,
    L"STATIC",
    L"This is the textbox",
    WS_CHILD | WS_VISIBLE,
    0,0,300,25,
    parentwin,
    NULL,
    hInstance,
    NULL
);



//making message queue
    MSG msg = {};

    ShowWindow(parentwin, nCmdShow);

    while (GetMessage(&msg, NULL, 0, 0)) //(message queue point, which window messages its handles NULL means get all, message range, retreave range )
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);

    }
    return 0;

}

LRESULT CALLBACK WindowProc(HWND parentwin, UINT uMsg, WPARAM wParam, LPARAM lParam){
    switch (uMsg){

        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;

        return 0;
    }
    return DefWindowProc(parentwin, uMsg, wParam, lParam);

}