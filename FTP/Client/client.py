#Implement of FTP client 
import socket
import os
import json

class FTPclient():
    def __init__(self):
        self.client = socket.socket() # use socket to communicate
    
    def help(self):  # assisting function
        msg = '''
        ls
        pwd
        cd../..
        get filename
        put filename
        '''
    
    def connect(self, ip, port):
        self.client.connect((ip, port))

    def interactive(self):
        while True:
            cmd = input('>>').strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0] # cmd_str will always be assistance
            # reflection
            if hasattr(self, 'cmd_%s'%cmd_str):
                func = getattr(self, 'cmd_%s'%cmd_str)
                func(cmd) # attribution is function: cmd_put
            else:
                self.help()

    def cmd_put(self, *args): # upload file
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename): # judge existence
                filesize = os.stat(filename).st_size

                # send size, filename, action to server, written in json for easy extension
                msg_dic = {
                    'action' : 'put',
                    'filename' : filename,
                    'size' : filesize
                }
                self.client.send(json.dumps(msg_dic).encode('utf-8')) # send to server
                server_response = self.client.recv(1024)
                f = open(filename, 'rb')
                for i in f:
                    self.client.send(i)
                else:
                    print('Transfer Ends')
                    f.close()
        else:
            print(filename, 'does not exist')
    
    def cmd_get(self): # download file
        pass

ftp = FTPclient()
ftp.connect('localhost', 8080)
ftp.interactive()

                



    

        

