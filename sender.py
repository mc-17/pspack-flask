import socket


def send(ip: str, port: int, file: str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    client_socket.settimeout(3000)
    client_socket.connect((ip, port))

    try:
        with open(file, "rb") as fp:
            client_socket.sendfile(fp)
            client_socket.close()
    finally:
        client_socket.close()
