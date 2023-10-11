import socket

def start_bc_master():
    # Create a socket for the master node 
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345
    # Bind the server to the specified IP address and port number
    master_socket.bind((host, port))
    # Master node listens for 4 connections
    master_socket.listen(4)
    print(f"Listening for connections on {host}:{port}...")

    clients = []  # Empty list to store connected clients

    try:
        for i in range(4):
            # Master node accepts connection request from a client
            client_socket, addr = master_socket.accept() 
            print(f"Connection from {addr} established!")
            clients.append(client_socket)
        
        for client in clients: # Send the broadcast message to all connected clients
            message = b"Broadcast message from the master!"
            client.sendall(message)

    finally: # Closes all connections after broadcast
        for client in clients:
            client.close()
        master_socket.close()

def start_mc_master():
    # Defines IP address and port number for multicast group
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = b"Multicast message from the master!"
    # Sends a multicast message to the clients registered in the group
    master_socket.sendto(message, (MCAST_GRP, MCAST_PORT))
    master_socket.close()  # Closes the master socket 

if __name__ == "__main__":
    start_bc_master()
    start_mc_master()
