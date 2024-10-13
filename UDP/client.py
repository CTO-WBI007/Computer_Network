import socket
import time
import random
import string

# use random function to generate strings
def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits  
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket

    
    for i in range (0, 100):
        message = generate_random_string()
        print(message)

        client_socket.sendto(message.encode(), ('localhost', 8080)) # encode and send

        result = client_socket.recv(1024) # accept and receive
    
        print(result.decode())

        time.sleep(0.1) # set interval between each sending to control the band width
    
    client_socket.close() # turn the socket down

start_client()
