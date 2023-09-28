import requests
import socket

def tcp_socket(name = "tcp_socket", ip_num="" port_num="4444"  ):
    try:
        #create TCP tocket
        name = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #create enpoint, in this case locally, with a port# of 4444
        name.bind(('localhost', 4444))
        #listen for requests and can queue up to 5 backlogged requests
        name.listen(5)
        print(f"Socket Created: {name}\nListening: {port_num}")
        return name
    except socket.error as e:
        print(f"")

def create_udp_socket():
    return None

while True:
    print("waiting for connection")
    client_socket, client_address = tcp_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:
        received_data = client_socket.recv(1024) #buffer size is 1024

        if not received_data:
            print(f"Connection from {client_address} closed")
            break
    
        data_line = received_data.decode('utf-8')
        print(f"received from {client_address}: {data_line}", end="")
    client_socket.close()
    break
    
tcp_socket.close()