import socket

c = socket.socket()
name = input('Enter youe Name')
c.connect(('localhost',9999))

c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())