import socket
import threading


def handle_client(skt, username):
    try:
        while 1:
            data = skt.recv(1024).decode()
            if not data:
                break

            for client, user in members.items():
                if client != skt:
                    client.send(f"{username}: {data}".encode())

    except:
        skt.close()

    finally:
        del members[skt]
        skt.close()
        print(username, "left the chat")


members = {}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 2030))
s.listen(10)
s.settimeout(20)

while 1:
    try:
        conn, addr = s.accept()
        username = conn.recv(2048).decode()
        members[conn] = username

        dedicated_thread = threading.Thread(target=handle_client, args=(conn, username))
        dedicated_thread.start()
    except:
        s.close()