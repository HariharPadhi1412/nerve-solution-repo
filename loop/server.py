import socket
from datetime import datetime
import time

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)

    server_socket.bind(server_address)
    server_socket.listen(1)

    data_dict = {"SetA":[{"One":1,"Two":2}],"SetB":[{"Three":3,"Four":4}],"SetC":[{"Five":5,"Six":6}],"SetD":[
{"Seven":7,"Eight":8}],"SetE":[{"Nine":9,"Ten":10}]}


    print(f"Server listening on {server_address}")

    while True:
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        try:
            # while True:
            #     # Send a message to the client in a loop
            #     message = "Hello from the server!"
            #     client_socket.sendall(message.encode())
            #     time.sleep(1)  # Sleep for 1 second before sending the next message
            data = client_socket.recv(1024)
            print(data)

            if not data:
                break

            message = data.decode()
            message_split = str(message).split("-")
            print(message_split)
            if message_split[0] in data_dict:
                for key, value in data_dict.items():
                    
                    if key == message_split[0]:
                        for sub_dict in value:
                                if message_split[1] in sub_dict:
                                    result = sub_dict[message_split[1]]
                                    print(result)
                                    counter = 0
                                    while counter < result:
                                        current_datetime = datetime.now()
                                        date_format = "%m-%d-%Y %H:%M:%S"
                                        formatted_datetime = current_datetime.strftime(date_format)
                                        print(f"Sending to {client_address}: {formatted_datetime}")

                                        client_socket.sendall(formatted_datetime.encode())
                                        time.sleep(1)
                                        
                                        counter += 1

                                                                        
                    else:   
                        client_socket.sendall(str("").encode())

        except Exception:
            print(Exception.message)
            print(f"Connection closed from {client_address}")

        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
