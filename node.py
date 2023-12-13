import socket
import random

def interact_with_poll(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as node_socket:
        node_socket.connect((host, port))

        poll_question = node_socket.recv(1024).decode()
        print(poll_question)

        response = random.choice(["yes", "no"])
        print(f"Chosen response: {response}")
        node_socket.sendall(response.encode())

        final_results = node_socket.recv(1024).decode()
        print(final_results)

def start_bc_node():
    poll_choice = random.choice(['poll1', 'poll2'])
    print(f"Connecting to {poll_choice}")

    if poll_choice == 'poll1':
        interact_with_poll('poll1', 12345)
    else:
        interact_with_poll('poll2', 12346)

if __name__ == "__main__":
    start_bc_node()
