import socket
import base64

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 3000)

    print(f"Connecting to {server_address}")
    client_socket.connect(server_address)

    try:
        while True:
            message = input("Enter a message || type 'exit' to close conn: ")

            emsg = base64.b64encode(message.encode())
            #print(emsg)
            client_socket.sendall(emsg)

            if message.lower() == 'exit':
                break

            data = client_socket.recv(1024)
            #print(data)

            dmsg = base64.b64decode(data).decode()
            print(dmsg)
            print(f"Received from server: {dmsg}")
    except Exception:
        client_socket.close()
        print(Exception)
    finally:
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    start_client()
