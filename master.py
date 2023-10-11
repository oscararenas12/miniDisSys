import socket

def start_broadcast_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(4)
    print(f"Listening for connections on {host}:{port}...")

    clients = []  # Store clients

    try:
        for i in range(4):
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr} established!")
            clients.append(client_socket)

        
        for client in clients:
            message = b"Broadcast message from the server!"
            client.sendall(message)

    finally:
        for client in clients:
            client.close()
        server_socket.close()

def start_multicast_server():
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = b"Multicast message from the server!"
    server_socket.sendto(message, (MCAST_GRP, MCAST_PORT))
    server_socket.close()

if __name__ == "__main__":
    start_broadcast_server()
    start_multicast_server()
