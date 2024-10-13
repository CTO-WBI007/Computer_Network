import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind(('0.0.0.0', 8080))

    server_socket.settimeout(30)

    print('Ready to receive')

    cnt = 0

    while cnt < 100:
        try:
            message, addr = server_socket.recvfrom(1024)
            if isinstance(message, bytes):
                result = message.decode().upper()
                cnt += 1
                server_socket.sendto(result.encode(), addr)
        
        except socket.timeout:
            break

    print(f"loss: {100 - cnt}")   
        
start_server()       
