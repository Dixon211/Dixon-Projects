#include <windows.h>

LRESULT CALLBACK WndProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

//window and instance
HWND hMainWindow;
HINSTANCE hMainInstance;

//handles
HWND hTxtInput;
HWND hbutton;
HWND htblOutput;
HWND parentwindow;

//objects
#define IDC_TEXTBOX 1000
#define IDC_Button 1001
#define IDC_STATIC 1002

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	MSG uMSG = { 0 };
	WNDCLASS chat = { 0 };
	chat.lpfnWndProc = WindowProc;
	chat.hInstance = hInstance;
	chat.hbrBackground = (HBRUSH)(COLOR_BACKGROUND);
	chat.lpszClassName = "MyWindowsApp";
	if 

}