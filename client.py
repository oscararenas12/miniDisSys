# References:
# https://www.geeksforgeeks.org/socket-programming-python/
# https://www.youtube.com/watch?app=desktop&v=3QiPPX-KeSc
# https://stackoverflow.com/questions/603852/how-do-you-udp-multicast-in-python
# https://www.youtube.com/watch?v=LnvxObLYO-o

import socket
import time

def info(packet_t, time_ms, src_ip, src_p, dest_ip, dest_p, pc, l, flags=None):
    #prints network logs to terminal
    print(f"Type: {packet_t}")
    print(f"Time (ms): {time_ms}")
    print(f"Source IP: {src_ip}")
    print(f"Source Port: {src_p}")
    print(f"Destination IP: {dest_ip}")
    print(f"Destination Port: {dest_p}")
    print(f"Protocol: {pc}")
    print(f"Length: {l} bytes")
    if flags: 
        print(f"Flags: {flags}")
    print("----")

def start_bc_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a TCP socket 
    host = 'master' # Specifying our master node for broadcast
    port = 12345    # Using this port to create our docker container to run mater node
    
    client_socket.connect((host, port)) # Connecting master node to port
    start_time = time.time() * 1000  # Starting time in ms
    message = client_socket.recv(1024) # Receives a messge in 1024 byte size
    end_time = time.time() * 1000  # Ending time in ms
    time_ms = end_time - start_time # Time to receive message

    # Print out our info
    info('Broadcast', time_ms, client_socket.getsockname()[0], client_socket.getsockname()[1], client_socket.getpeername()[0], client_socket.getpeername()[1], 'TCP', len(message))
    # Decode message show it was received
    print(f"Received broadcast message: {message.decode()}")
    # Closes socket to end connnection
    client_socket.close()

def start_mc_client():
    MCAST_GRP = '224.1.1.1' # Specifying our master node for multicast 
    MCAST_PORT = 5007       # Using this port to create our docker container to run mater node
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # Creates a UDP socket 
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows client_socket to bind to address and port
    client_socket.bind((MCAST_GRP, MCAST_PORT)) # Makes client_ready to receive muiltcast communication

    mreq = socket.inet_aton(MCAST_GRP) + socket.inet_aton('0.0.0.0')
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    start_time = time.time() * 1000  # Start time in ms
    message, addr = client_socket.recvfrom(1024)
    end_time = time.time() * 1000  # End time in ms
    time_ms = end_time - start_time # time to receive message 

    info('Multicast', time_ms, client_socket.getsockname()[0], MCAST_GRP, addr[0], MCAST_PORT, 'UDP', len(message))
    print(f"Received multicast message: {message.decode()}")

if __name__ == "__main__":
    start_bc_client()
    start_mc_client()
