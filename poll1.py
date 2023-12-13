import socket
import random

def start_bc_poll1():
    poll1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345
    poll1_socket.bind((host, port))
    poll1_socket.listen(4)
    poll1_socket.settimeout(10)  # Set a timeout for accepting connections

    print(f"Listening for connections on {host}:{port}...")
    responses = {"yes": 0, "no": 0}

    try:
        while True:
            try:
                node_socket, addr = poll1_socket.accept()
                print(f"Connection from {addr} established!")

                # Handle client interaction
                poll_question = "Master 1 Do you like Python? (yes/no)"
                node_socket.sendall(poll_question.encode())
                response = node_socket.recv(1024).decode().lower()
                if response in responses:
                    responses[response] += 1

                # Send final results to client
                final_results = f"Master 1 Current Poll Results: Yes: {responses['yes']}, No: {responses['no']}"
                node_socket.sendall(final_results.encode())

                # Close client connection
                node_socket.close()

            except socket.timeout:
                break  # Break out of the loop if no new connections within timeout

    finally:
        print("Master 1 Final Poll Results:")
        print(f"Yes: {responses['yes']}, No: {responses['no']}")
        poll1_socket.close()

if __name__ == "__main__":
    start_bc_poll1()
