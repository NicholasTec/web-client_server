# Client

# Import socket module
import socket

# server info
host = '127.0.0.1'
port = 9080


def connect():
    # create socket
    skt = socket.socket()
    # connect to server
    skt.connect((host, port))

    # receive feedback from server
    print(skt.recv(1024).decode())
    # close connection
    skt.close()


if __name__ == '__main__':
    connect()
