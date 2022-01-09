import time
import socket


def send(ip, port, file):
    for i in range(3):
        print(f"Sending payload: attempt {i}...")
        time.sleep(1)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        client_socket.settimeout(3000)
        client_socket.connect((ip, port))

        try:
            with open(file, "rb") as fp:
                client_socket.sendfile(fp)
            print(f"Sending payload: attempt {i} succeeded!")
            break
        finally:
            client_socket.close()
