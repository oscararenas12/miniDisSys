import socket
import random

def start_bc_master():
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345
    master_socket.bind((host, port))
    master_socket.listen(4)  # Listen for up to 4 connections
    master_socket.settimeout(10)  # Set a timeout of 10 seconds

    print(f"Listening for connections on {host}:{port}...")
    clients = []
    responses = {"yes": 0, "no": 0}

    try:
        while True:
            try:
                client_socket, addr = master_socket.accept()
                print(f"Connection from {addr} established!")
                clients.append(client_socket)
            except socket.timeout:
                print("Connection from timed Out on Master 1")
                break  # Break out of the loop if no new connections within timeout

        poll_question = "Master 1 Do you like Python? (yes/no)"
        for client in clients:
            client.sendall(poll_question.encode())

        for client in clients:
            response = client.recv(1024).decode().lower()
            if response in responses:
                responses[response] += 1
            print(f"Master 1 Current Poll Results: Yes: {responses['yes']}, No: {responses['no']}")

    finally:
        print("Master 1 Final Poll Results:")
        print(f"Yes: {responses['yes']}, No: {responses['no']}")
        for client in clients:
            client.close()
        master_socket.close()

if __name__ == "__main__":
    start_bc_master()
