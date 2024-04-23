import socket

soc = socket.socket() # ipv4, TCP by default
print('Socket Created')

soc.bind(('localhost', 9999)) # Range for portnumber 0 -> 65535

soc.listen(3) #Accepts only 3 conections
print('Waiting for connections')

while(True):
    c, addr = soc.accept() # c -> client, addr -> address
    name = c.recv(1024).decode()
    print('Connected with', addr, name)

    c.send(bytes('Welcome to Socket Programming','utf8'))
    c.close()