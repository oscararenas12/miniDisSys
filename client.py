import socket
import time
import random

def start_bc_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'master'
    port = 12345
    client_socket.connect((host, port))

    poll_question = client_socket.recv(1024).decode()
    print(poll_question)

    # Randomly choose yes or no
    response = random.choice(["yes", "no"])
    client_socket.sendall(response.encode())

    client_socket.close()

if __name__ == "__main__":
    start_bc_client()