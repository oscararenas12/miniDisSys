import socket

def start_bc_master():
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345
    master_socket.bind((host, port))
    master_socket.listen(4) #listening for up to 4 client nodes
    print(f"Listening for connections on {host}:{port}...")

    clients = []  # Store client nodes

    try:
        for i in range(4):
            client_socket, addr = master_socket.accept()
            print(f"Connection from {addr} established!")
            clients.append(client_socket)

        
        for client in clients:
            message = b"Broadcast message from the master!"
            client.sendall(message)

    finally:
        for client in clients:
            client.close()
        master_socket.close()

def start_mc_master():
    mcast_group = '224.1.1.1'
    mcast_port = 5007
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = b"Multicast message from the master!"
    master_socket.sendto(message, (mcast_group, mcast_port))
    master_socket.close()

if __name__ == "__main__":
    start_bc_master()
    start_mc_master()
