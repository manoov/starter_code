import socket
import json

def send_msg(sock, data):
    message = json.dumps(data).encode('utf-8')
    sock.sendall(message)

def recv_msg(sock):
    data = sock.recv(1024).decode('utf-8')
    if not data: return None
    return json.loads(data)
