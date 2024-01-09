
   // network settings
    bool net_check = false;
    //variables
    const char* ip_addy = "127.0.0.1";
    int port_num = 9000;
    
    //Socket Stuff
    WSADATA wsaData;
    if(WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "\nWSAStartup failed." <<std::endl;
        return 1,
    }

    //create socket
    SOCKET thesocket = socket(AF_INET, SOCK_STREAM, 0);
    if (thesocket == INVALID_SOCKET) {
        std::cerr << "\nerror creating socket: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return 2;
    }

    sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr(ip_addy);
    serverAddress.sin_port = htons(port_num);

    if (connect(thesocket, (struct sockaddr* )&serverAddress, sizeof(serverAddress)) == SOCKET_ERROR) {
        std::cerr << "\nConnection failed: " << WSAGetLastError() << std::endl;
        closesocket(thesocket);
        WSACleanup();
        return 3; 
    }

    //send data
    std::string message = "the data sent from the server";
    if (send(thesocket, message.c_str(), message.length(), 0) == SOCKET_ERROR) {
        std::cerr << "Error sending data: " << WSAGetLastError() << std::endl;
        closesocket(thesocket);
        WSACleanup();
        return 4;
    }
