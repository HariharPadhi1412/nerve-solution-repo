import socket
import select
import base64

def start_server():
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('localhost', 3000)

    sockets.bind(address)
    sockets.listen(5)

    print(f"Server running on {address}")

    inputs = [sockets]
    clientsdict = {}

    while True:
        readable, _, _ = select.select(inputs, [], [])
        #print(readable)

        for sock in readable:
            # print(sockets)
            if sock == sockets:
                client_socket, client_address = sockets.accept()
                # print(client_socket)
                # print(client_address)
                print(f"connection from {client_address}")

                inputs.append(client_socket)
                #print(inputs)
                clientsdict[client_socket] = client_address
                #print(clientsdict)
            else:
                data = sock.recv(1024)
                # print(data)
                if not data:
                    print(f"Connection closed {clientsdict[sock]}")
                    inputs.remove(sock)
                    del clientsdict[sock]
                    #print(clientsdict)
                    sock.close()
                else:
                    print(f"Received from {clientsdict[sock]}: {data}")

                    dmsg = base64.b64decode(data).decode()
                    print(f"Decoded message: {dmsg}")

                    emsg = base64.b64encode(dmsg.encode())
                    sock.sendall(emsg)

if __name__ == "__main__":
    start_server()
