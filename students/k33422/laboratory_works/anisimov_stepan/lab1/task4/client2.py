import socket
import threading


def receive(skt):
    while 1:
        try:
            data = skt.recv(1024).decode()
            if not data:
                break
            else:
                print(data)
        except:
            break


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 2030))

username = input("Enter username: ")
s.send(username.encode())

get_thread = threading.Thread(target=receive, args=(s,))
get_thread.daemon = True
get_thread.start()

while 1:
    message = input()
    s.send(message.encode())
    if message == "done":
        break

s.close()
