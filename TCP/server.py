#implement of TCP SERVER

import socket

def start_server():
    #create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind
    server_socket.bind(('localhost', 8080))
    server_socket.listen(3)

    print('Ready to receive')

    while True:
        connnectionSocket, addr = server_socket.accept()
        while True:
            sentence = connnectionSocket.recv(1024).decode()
            if not sentence or sentence == 'exit':
                print('exit')
                break
            result = sentence.upper()
            connnectionSocket.send(result.encode())
        
        connnectionSocket.close()

start_server()