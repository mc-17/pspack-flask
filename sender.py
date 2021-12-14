import socket

def send(ip, port, file):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    clientSocket.settimeout(3000)
    clientSocket.connect((ip, port))

    try:
        with open(file, "rb") as fp:
            clientSocket.sendfile(fp)
            clientSocket.close()
    finally:
        clientSocket.close()
