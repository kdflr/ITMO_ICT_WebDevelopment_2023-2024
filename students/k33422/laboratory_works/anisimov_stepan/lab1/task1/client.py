import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Hello, server", ("localhost", 2024))

data, addr = s.recvfrom(2048)
print(data.decode())
s.close()