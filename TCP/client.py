#implement of consistent TCP CLIENT

import socket

def start_client():
    #create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect
    client_socket.connect(('localhost', 8080))
    while True:
        sentence = input('Input lowercase sentence: ')
        
        client_socket.send(sentence.encode())
        
        if sentence == 'exit':
            break

        result = client_socket.recv(1024)
        print(result.decode())

    
    client_socket.close()
    
start_client()
