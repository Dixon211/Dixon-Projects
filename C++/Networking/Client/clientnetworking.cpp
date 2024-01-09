#include <iostream>
#include <winsock2.h>
#include "Functions/Accessinfo.h"

int main () {
    //initialize Winsock
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr <<"WSAStartup failed." << std::endl;
        return 1;
    }

    //create socket
    SOCKET mysocket = socket(AF_INET, SOCK_STREAM, 0);
    if (mysocket == INVALID_SOCKET) {
        std::cerr << "Error creating socket:" << WSAGetLastError() << '\n' << std::endl;
        WSACleanup();
        return 2;
    }

    //create socket and give server information
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr("127.0.0.1");
    serverAddress.sin_port = htons(9000);

    //connect to the server
    if (connect(mysocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == SOCKET_ERROR) {
        std::cerr << "Connection failed: " << WSAGetLastError() << std::endl;
        closesocket(mysocket);
        WSACleanup();
        return 3;
    };

    //send data
    
    std::string message = Accessinfo();
    if (send(mysocket, message.c_str(), message.length(), 0) == SOCKET_ERROR) {
        std::cerr << "Error sending data: " << WSAGetLastError() << std::endl;
        closesocket(mysocket);
        WSACleanup();
        return 1;
    }

    
    closesocket(mysocket);
    WSACleanup();
    std::cout<< "exiting program" << std::endl;

   return 0; 
}