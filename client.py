import socket
import random

def interact_with_master(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        poll_question = client_socket.recv(1024).decode()
        print(poll_question)

        response = random.choice(["yes", "no"])
        client_socket.sendall(response.encode())

        final_results = client_socket.recv(1024).decode()
        print(final_results)

def start_bc_client():
    master_choice = random.choice(['master', 'master2'])
    print(f"Connecting to {master_choice}")

    if master_choice == 'master':
        interact_with_master('master', 12345)
    else:
        interact_with_master('master2', 12346)  # Adjust the port if necessary

if __name__ == "__main__":
    start_bc_client()
