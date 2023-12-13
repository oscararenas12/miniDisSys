import socket
import random

def connect_to_master(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def interact_with_master(client_socket):
    poll_question = client_socket.recv(1024).decode()
    print(poll_question)

    # Randomly choose yes or no
    response = random.choice(["yes", "no"])
    client_socket.sendall(response.encode())

    # Receive and print current poll results from master
    poll_results = client_socket.recv(1024).decode()
    print(poll_results)

    client_socket.close()

def start_bc_client():
    # Randomly choose a master to vote on
    master_choice = random.choice(['master', 'master2'])
    
    if master_choice == 'master':
        print("Connecting to master")
        master_socket = connect_to_master('master', 12345)
    else:
        print("Connecting to master2")
        master_socket = connect_to_master('master2', 12346)  # Assuming master2 is on a different port

    interact_with_master(master_socket)

if __name__ == "__main__":
    start_bc_client()
