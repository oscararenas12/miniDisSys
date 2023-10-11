import socket
import time

def print_info(packet_type, src_ip, src_port, dest_ip, dest_port, protocol, length, flags=None):
    timestamp = int(time.time() * 1000)  # Time in milliseconds
    print(f"Type: {packet_type}")
    print(f"Time (ms): {timestamp}")
    print(f"Source IP: {src_ip}")
    print(f"Source Port: {src_port}")
    print(f"Destination IP: {dest_ip}")
    print(f"Destination Port: {dest_port}")
    print(f"Protocol: {protocol}")
    print(f"Length: {length} bytes")
    if flags:
        print(f"Flags: {flags}")
    print("----")

    # Record output to a txt file
    #results = open('/app/mysite/output.txt', 'a')
    #results.write("Hello")
    #results.write(f"Type: {packet_type}, Time: {timestamp}, Source IP: {src_ip}, "
    #              f"Destination IP: {dest_ip}, Source Port: {src_port}, "
    #              f"Destination Port: {dest_port}, Protocol: {protocol}, "
    #              f"Length: {length} bytes")
    #if flags:
    #    results.write(f", Flags: {flags}")
    #results.write("\n")
    #results.close()
    #return 0  

def start_broadcast_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'server'  # Modify this according to your server's address
    port = 12345

    
    client_socket.connect((host, port))
    message = client_socket.recv(1024)
    print_info('Broadcast', client_socket.getsockname()[0], client_socket.getsockname()[1], client_socket.getpeername()[0], client_socket.getpeername()[1], 'TCP', len(message))

    print(f"Received broadcast message: {message.decode()}")
    client_socket.close()

def start_multicast_client():
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007

    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind((MCAST_GRP, MCAST_PORT))

    mreq = socket.inet_aton(MCAST_GRP) + socket.inet_aton('0.0.0.0')
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    message, addr = client_socket.recvfrom(1024)
    print_info('Multicast', client_socket.getsockname()[0], MCAST_GRP, addr[0], MCAST_PORT, 'UDP', len(message))
    print(f"Received multicast message: {message.decode()}")

if __name__ == "__main__":
    start_broadcast_client()
    start_multicast_client()
