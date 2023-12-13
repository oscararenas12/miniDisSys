import socket
import random

def start_bc_master():
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12346
    master_socket.bind((host, port))
    master_socket.listen(4)
    master_socket.settimeout(10)  # Set a timeout for accepting connections

    print(f"Listening for connections on {host}:{port}...")
    responses = {"yes": 0, "no": 0}

    try:
        while True:
            try:
                client_socket, addr = master_socket.accept()
                print(f"Connection from {addr} established!")

                # Handle client interaction
                poll_question = "Master 2 Do you like Python? (yes/no)"
                client_socket.sendall(poll_question.encode())
                response = client_socket.recv(1024).decode().lower()
                if response in responses:
                    responses[response] += 1

                # Send final results to client
                final_results = f"Master 2 Current Poll Results: Yes: {responses['yes']}, No: {responses['no']}"
                client_socket.sendall(final_results.encode())

                # Close client connection
                client_socket.close()

            except socket.timeout:
                break  # Break out of the loop if no new connections within timeout

    finally:
        print("Master 2 Final Poll Results:")
        print(f"Yes: {responses['yes']}, No: {responses['no']}")
        master_socket.close()

if __name__ == "__main__":
    start_bc_master()
