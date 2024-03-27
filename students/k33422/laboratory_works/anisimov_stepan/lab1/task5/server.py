import socket


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.journal = {}


    def serve_forever(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        while 1:
            conn, addr = s.accept()
            self.serve_client(conn)
            conn.close()


    def serve_client(self, conn):
        data = conn.recv(16384).decode()
        url, method, headers, body = self.parse_request(data)
        response = self.handle_request(url, method, body)
        if response:
            self.send_response(conn, response)


    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        headers_end = lines.index('')
        headers = lines[1:headers_end]
        body = lines[-1]

        return url, method, headers, body


    def handle_request(self, url, method, body):
        if url == '/':
            if method == 'GET':
                with open('index.html') as file:
                    content = file.read()
                return 'HTTP/1.1 200 OK \n\n' + content
            if method == 'POST':
                response = "HTTP/1.1 200 OK \n\n"
                parameters = body.split('&')
                subj, grd = [x.split('=')[1] for x in parameters]
                self.journal[subj] = grd
                response += "<html><head><title>Journal</title></head><body><ul>"
                response += f"<b>Subject{' ' * 10}Grades</b>"
                for subj, grd in self.journal.items():
                    response += f"<p>{subj}{' ' * (10 + 7 - len(subj))}{','.join(grd)}</p>"
                response += '<a href="/">Go back</a>'
                response += "</ul></body></html>"
                return response

    def send_response(self, conn, response):
        conn.send(response.encode())


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 2030
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass






