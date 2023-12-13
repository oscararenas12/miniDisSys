import socket
import random

def start_bc_master():
    master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12346
    master_socket.bind((host, port))
    master_socket.listen(4)
    print(f"Listening for connections on {host}:{port}...")

    clients = []
    responses = {"yes": 0, "no": 0}

    try:
        for i in range(4):
            client_socket, addr = master_socket.accept()
            print(f"Connection from {addr} established!")
            clients.append(client_socket)

        poll_question = "Do you like Python? (yes/no)"
        for client in clients:
            client.sendall(poll_question.encode())

        for client in clients:
            response = client.recv(1024).decode().lower()
            if response in responses:
                responses[response] += 1
                
            results_msg = f"Current Poll Results: Yes: {responses['yes']}, No: {responses['no']}"
            client.sendall(results_msg.encode())
            # Display results after each vote
            # print(f"Current Poll Results: Yes: {responses['yes']}, No: {responses['no']}")

    finally:
        print("Final Poll Results:")
        print(f"Yes: {responses['yes']}, No: {responses['no']}")
        for client in clients:
            client.close()
        master_socket.close()

if __name__ == "__main__":
    start_bc_master()