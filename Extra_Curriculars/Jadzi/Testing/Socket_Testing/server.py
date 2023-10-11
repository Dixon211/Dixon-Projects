import socket

#socket details: AF_INET is sending over IPv4, SOCK_STREAM is TCP
my_first_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binds the socket to port 1234, need to check gethostname()
my_first_socket.bind((socket.gethostname(), 1234))
#actually start listening
my_first_socket.listen(5)

while True:
    #when it accepts it will take the tuple and turn it into the clientsocket that we got it from and its IP addess
    clientsocket, address = my_first_socket.accept()
    #confirmation
    print(f"Connectin from {address} has been established!")
    #reply
    clientsocket.send(bytes("Welcome to the server", "UTF-8"))
    