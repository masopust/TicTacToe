import socket
import sys


class Server:

    def __init__(self):
        self.HOST = ''  # Symbolic name, meaning all available interfaces
        self.PORT = 8888  # Arbitrary non-privileged port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        # Bind socket to local host and port
        try:
            self.socket.bind((self.HOST, self.PORT))
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        # Start listening on socket
        self.socket.listen(10)
        print('Socket now listening')

        # now keep talking with the client
        while 1:
            # wait to accept a connection - blocking call
            conn, addr = self.socket.accept()
            print('Connected with ' + addr[0] + ':' + str(addr[1]))

