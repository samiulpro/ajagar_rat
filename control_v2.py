import socket

address = ('0.0.0.0', 8080)
c2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c2.connect(address)

print(c2.recv(1024).decode('utf-8'))
c2.send('<bravo>'.encode('utf-8'))

while True:
    cmd = input("> ")
    c2.send(cmd.encode('utf-8'))
    print(c2.recv(4096).decode('utf-8'))
    if cmd == '<close>':
        print('SOCKET IS CLOSING')
        c2.close()
        break