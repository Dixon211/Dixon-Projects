import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 4444)
tcp_socket.connect(server_address)

print("sending data")
tcp_socket.send(b'\nhello server\n')