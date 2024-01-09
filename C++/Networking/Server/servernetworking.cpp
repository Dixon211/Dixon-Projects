#include <iostream>
#include <winsock2.h>

int main () {


    int portnum = 5000;
    const char* addr = "127.0.0.1";
    bool connection_check = false;
    const char* file_path= "C:\\Users\\Assoc\\OneDrive\\Documents\\GitHub\\Dixon-Projects\\C++\\Networking\\Server\\servernetworking.exe";

    std::cout << file_path << std::endl;

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

    //bind the socket
    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr(addr);
    serverAddress.sin_port = htons(portnum);

    if (bind(mysocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress))  == SOCKET_ERROR) {
        std::cerr << "Error binding socket: " << WSAGetLastError() << std::endl;
        closesocket(mysocket);
        WSACleanup();
        return 3;
    }

    //listen on the socket
    if (listen(mysocket, 10) == SOCKET_ERROR) {
        std::cerr << "Error listening on socket: " << WSAGetLastError() << std::endl;
        closesocket(mysocket);
        WSACleanup();
        return 4;
    }

    std::cout << "Server listening on address "<< addr <<" ... \n"<<"Listening on port "<< portnum << " ..." << std::endl;

    //Accept connection
    while(true) {
        std::cout << "entering Loop" << std::endl;
        SOCKET clientsocket = accept(mysocket, NULL, NULL);
        if (clientsocket == INVALID_SOCKET) {
            std::cerr << "Error accepting connection: " <<WSAGetLastError() << std::endl;
            continue;
        }
    
    //receive data from client
        char buffer[1024];
        int bytesRead = recv(clientsocket, buffer, sizeof(buffer), 0);
        if (bytesRead > 0) {
            //print data to console
            buffer[bytesRead] = '\0';
            std::cout << "Received Message: " << buffer << '\n' << std::endl;

            const char* response = "Hello from the server!";
            send(clientsocket, response, strlen(response), 0);
        }

        std::cout << "loop running" << std::endl;
    }

    closesocket(mysocket);
    WSACleanup();
    std::cout<< "exiting program" << std::endl;

   return 0; 
}