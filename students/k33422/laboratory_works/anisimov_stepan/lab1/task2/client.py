import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 2026))

data = s.recv(256)
print(data.decode())

lengths = str(input())

s.send(lengths.encode())

ans = s.recv(256)
print(ans.decode())
s.close()