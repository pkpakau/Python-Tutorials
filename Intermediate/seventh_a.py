# Sockets and Network Programming

# Level4 - Transprot Layer
# Connection Oriented Protocol - TCP ( Chat apps, reliabel sending and receiving )
# Connectionless Protocol - UDP ( Skype, Internet Calling )

import socket
# ( two levels - unix and internet )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
# TCP - socket.SOCK_STREAM
# UDP - socket.SOCK_DGRAM
s.bind(('127.0.0.1', 5555))

# server listening for possible connections
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()