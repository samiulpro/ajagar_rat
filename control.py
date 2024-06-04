import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 8080
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            print(self.sock.recv(1024).decode())
            msg = input("> ")
            self.sock.send(msg.encode('utf-8'))
            if msg == "<close>":
                self.sock.send(msg.encode('utf-8'))
                self.sock.close()
                print("SERVER SHUTTING DOWN.")
                break
        
        print("turned off")
        return 0

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)