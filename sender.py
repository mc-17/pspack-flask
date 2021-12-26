import socket


def send(ip, port, file):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    client_socket.settimeout(3000)
    client_socket.connect((ip, port))

    try:
        with open(file, "rb") as fp:
            client_socket.sendfile(fp)
    finally:
        client_socket.close()
