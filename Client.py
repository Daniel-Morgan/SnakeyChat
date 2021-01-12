import socket

HOST = '127.0.0.1'
PORT = 8181

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('Hello world'.encode('ascii'))
    data = s.recv(1024)

print('recieved', data.decode('ascii'))
