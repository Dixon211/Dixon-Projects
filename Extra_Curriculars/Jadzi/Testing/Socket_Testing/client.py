import socket
#prepping the socket for what type of information
my_second_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection information
my_second_socket.connect((socket.gethostname(), 1234))

#how much data to recieve at a time, all is sent as bytes
msg = my_second_socket.recv(1024)
#decode to something
print(msg.decode("utf-8"))
