import socket
import time

def info(packet_type, time_ms, src_ip, src_port, dest_ip, dest_port, protocol, length, flags=None):
    #prints network logs to terminal
    print(f"Type: {packet_type}")
    print(f"Time (ms): {time_ms}")
    print(f"Source IP: {src_ip}")
    print(f"Source Port: {src_port}")
    print(f"Destination IP: {dest_ip}")
    print(f"Destination Port: {dest_port}")
    print(f"Protocol: {protocol}")
    print(f"Length: {length} bytes")
    if flags:
        print(f"Flags: {flags}")
    print("----")

def start_bc_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'master'
    port = 12345
    
    client_socket.connect((host, port))
    start_time = time.time() * 1000  # Start time in ms
    message = client_socket.recv(1024)
    end_time = time.time() * 1000  # End time in ms
    time_ms = end_time - start_time # time to receive message

    info('Broadcast', time_ms, client_socket.getsockname()[0], client_socket.getsockname()[1], client_socket.getpeername()[0], client_socket.getpeername()[1], 'TCP', len(message))
    print(f"Received broadcast message: {message.decode()}")
    client_socket.close()

def start_mc_client():
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind((MCAST_GRP, MCAST_PORT))

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
