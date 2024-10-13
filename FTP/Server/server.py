# Implement of FTP server
import socketserver
import json, os

class MyTCPHandler(socketserver.BaseRequestHandler):
    
    def put(self, *args):
        # getting file
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['size']
        if os.path.isfile(filename): # if existing, create a new one
            f = open(filename + '.new', 'wb')
        else:
            # if not
            f = open(filename, 'wb')
        self.request.send(b'200 ok') # give client reponse
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print('file[%s] has overload'%filename)
    
    # interact with client
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{}wrote:'.format(self.client_address[0]))  
                print(self.data)

                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic['action']

                if hasattr(self, action): 
                    func = getattr(self , action)
                    func(cmd_dic)
        
            except ConnectionResetError as e:
                print(e)
                break

if __name__  == '__main__':
    HOST, POST = 'localhost', 8080
    
    server = socketserver.ThreadingTCPServer((HOST, POST), MyTCPHandler)  
    
    server.serve_forever()