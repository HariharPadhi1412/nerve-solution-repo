import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)

    print(f"Connecting to {server_address}")
    client_socket.connect(server_address)

    try:
        while True:
            message = input("Enter a message || type 'exit' to close conn: ")
            client_socket.sendall(message.encode())

            if message.lower() == 'exit':
                break

            while True:
                data = client_socket.recv(1024)
                if not data:
                    break

                print(f"Received from server: {data.decode()}")
    finally:
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    start_client()
