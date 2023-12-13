import socket
import random

def start_bc_poll2():
    poll2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12346
    poll2_socket.bind((host, port))
    poll2_socket.listen(4)
    poll2_socket.settimeout(10)  # Set a timeout for accepting connections

    print(f"Listening for connections on {host}:{port}...")
    responses = {"yes": 0, "no": 0}

    try:
        while True:
            try:
                node_socket, addr = poll2_socket.accept()
                print(f"Connection from {addr} established!")

                # Handle client interaction
                poll_question = "(Poll 2) Do you like Cats? (yes/no)"
                node_socket.sendall(poll_question.encode())
                response = node_socket.recv(1024).decode().lower()
                if response in responses:
                    responses[response] += 1

                # Send final results to client
                final_results = f"Current Poll 2 Results: Yes: {responses['yes']}, No: {responses['no']}"
                node_socket.sendall(final_results.encode())

                # Close client connection
                node_socket.close()

            except socket.timeout:
                break  # Break out of the loop if no new connections within timeout

    finally:
        print("Final Poll 2 Results:")
        print(f"Yes: {responses['yes']}, No: {responses['no']}")
        poll1_socket.close()

if __name__ == "__main__":
    start_bc_poll2()
