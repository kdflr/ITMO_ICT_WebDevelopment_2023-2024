import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 2076))
s.listen(1)

while 1:
    conn, addr = s.accept()
    data = conn.recv(2048)
    print(data.decode())
    with open('index.html') as file:
        content = file.read()
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + content
    response = response.encode('utf-8')
    conn.send(response)
    conn.close()