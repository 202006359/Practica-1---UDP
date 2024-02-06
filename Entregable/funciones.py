import pickle
import random
import socket

def ask_IP_address():
    valid_IP = False
    while not valid_IP:
        IP_address = input("Enter the IP address: ")
        try:
            socket.inet_aton(IP_address)
            valid_IP = True
        except:
            print("Invalid IP address")
    return IP_address

def ask_port_number():
    valid_port = False
    while not valid_port:
        port_number = input("Enter the port number: ")
        try:
            port_number = int(port_number)
            if port_number > 0 and port_number < 65535:
                valid_port = True
            else:
                print("Invalid port number")
        except:
            print("Invalid port number")
    return port_number

def ask_message():
    msg = input("Enter a message: ")
    return msg

def ask_number_client():
    number_client = random.randint(1, 1000)
    return number_client

def send_to_server(message, number_client, ip_address, port_number, socket_cliente):
    try:
        # Send message to server
        send_to_server = (message, number_client)
        socket_cliente.sendto(pickle.dumps(send_to_server), (ip_address, port_number))
    except Exception as e:
        print(f"Client: Error occurred while sending message to server: {e}")
    
def receive_from_server(socket_cliente):
    try:
        # Receive message from server
        bytes_rx, _ = socket_cliente.recvfrom(1024)
        return bytes_rx
    except Exception as e:
        print(f"Client: Error occurred while receiving message from server: {e}")
        return None