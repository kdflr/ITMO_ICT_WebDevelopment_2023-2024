import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 2024))
s.settimeout(5)
try:
    while 1:
        data, addr = s.recvfrom(256)
        print(data.decode())
        s.sendto(b'Hello, client', addr)
except socket.timeout:
    s.close()

