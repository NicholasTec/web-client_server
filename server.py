
# Import socket module
import socket

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
        print("socket creation failed with error %s" % (err))

    return skt


def listenClient():
    try:
        # socket listen one clinet each time
        skt.listen(1)
    except socket.error as err:
        print("socket creation failed with error %s" % (err))

    print("socket is listening...")
    # Establish connection with client.
    client, addr = skt.accept()
    print('Conneted with client:', addr)

    # send feedback to client
    client.send('Server 9080: Connected! Hope to serve you again!'.encode())

    # Close connection
    client.close()
    print("Client disconnected!")
    print("##############################")


if __name__ == '__main__':
    skt = initServer()
    listenClient()
