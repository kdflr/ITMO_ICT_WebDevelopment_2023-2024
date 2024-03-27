import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 2026))
s.listen(1)
s.settimeout(5)
try:
    while 1:
        conn, addr = s.accept()
        conn.send(b"Enter the triangle's side lengths")
        data = conn.recv(256)
        a = int(data.decode()[0])
        b = int(data.decode()[2])
        c = (a ** 2 + b ** 2) ** 0.5
        conn.send(str(c).encode())
except:
    s.close()