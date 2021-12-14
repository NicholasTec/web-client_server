
# Import socket module
import socket
import sys

# server ip addr assigned by router
ip = '127.0.0.1'
# default port for socket
port = 9080


def initServer():
    try:
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket was created!")
        skt.bind((ip, port))
        print("socket binded to %s" % (port))
    except socket.error as err:
        print("[!!Server Error!!] %s" % (err))
        sys.exit(-1)
    return skt


def listenClient():
    skt.listen(1)
    print("socket is listening...")
    # Establish connection with client.
    client, addr = skt.accept()
    print('Conneted with client:', addr)

    # send feedback to client
    client.send(
        '[Server 9080]Message: Connected! Hope to serve you again!'.encode())

    # Close connection
    client.close()
    print("Client disconnected!")
    print("##############################")


if __name__ == '__main__':
    skt = initServer()
    while True:
        listenClient()
