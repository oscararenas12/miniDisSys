import socket
import random

def interact_with_poll(host, port):
    # creates a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as node_socket:
        # connects the socket to the specified host and port
        node_socket.connect((host, port))

        # receive and print the poll question from the poll
        poll_question = node_socket.recv(1024).decode()
        print(poll_question)

        # randomly select a response (yes or no) and print it
        response = random.choice(["yes", "no"])
        print(f"Chosen response: {response}")

        # send the chosen response to the poll
        node_socket.sendall(response.encode())

        # receive and print the final poll results from the poll
        final_results = node_socket.recv(1024).decode()
        print(final_results)

def start_bc_node():
    # randomly chooses which poll to connect to (poll1 or poll2)
    poll_choice = random.choice(['poll1', 'poll2'])
    print(f"Connecting to {poll_choice}")

    if poll_choice == 'poll1':
        interact_with_poll('poll1', 12345)
    else:
        interact_with_poll('poll2', 12346)

# main to run everything 
if __name__ == "__main__":
    start_bc_node()
