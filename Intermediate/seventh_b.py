# Client Code

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 5555))
message = s.recv(1024)

print(message.decode())