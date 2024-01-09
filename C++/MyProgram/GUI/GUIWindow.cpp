#ifndef UNICODE
#define UNICODE
#endif
#include "GUIWindow.h"


LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow)
{
    //Register the window
    const wchar_t CLASS_NAME[] = L"Mike's Program";
     WNDCLASS wc = {};

    //constructor info
     wc.lpfnWndProc = WindowProc;
     wc.hInstance = hInstance;
     wc.lpszClassName = CLASS_NAME;

     RegisterClass(&wc);

     //create window
    HWND hwnd = CreateWindowEx(
        0, //option window styles
        CLASS_NAME, //class name
        L"My Program", //window text
        WS_OVERLAPPEDWINDOW, //Window style

        //size and position
        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,

        NULL, //parent window
        NULL, //menu
        hInstance, //Instance handle
        NULL //additional app data
        );

    if (hwnd == NULL) //error checking
    {
        return 0;
    }

    HWND displaybox = CreateWindowEx(
        0,
        L"STATIC", //class
        L"This is the display box", //display text
        WS_CHILD | WS_VISIBLE,
        10,10,300,25,
        hwnd,
        NULL,
        hInstance,
        NULL

    );

    ShowWindow(hwnd, nCmdShow);
    
    //run loop

    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0) > 0)
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);

    }
    return 0;
    
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;

        case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            //ALL paint occurs here, between BeginPaint and EndPaint

            FillRect(hdc, &ps.rcPaint, (HBRUSH) (COLOR_WINDOW+1));

            EndPaint(hwnd, &ps);
        }
        return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}