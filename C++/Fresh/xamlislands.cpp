#include <Windows.h>
#include <winrt/Windows.UI.Xaml.Hosting.h>
#include <winrt/Windows.UI.Xaml.Controls.h>

using namespace winrt;
using namespace Windows::UI::Xaml::Hosting;
using namespace Windows::UI::Xaml::Controls;

int main () {
    init_apartment();

    WindowsXamlManager xamlManager;
    WINRT_Windows_UI_Xaml_H xamlHost;


}