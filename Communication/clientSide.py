try:
    import TicTacToe.Common.commonVariables as common
except ModuleNotFoundError:
    import Common.commonVariables as common


import socket
import struct
import threading
import time


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
        # Connect the socket to the port where the server is listening
        server_address = (common.SERVER_NAME, common.PORT_NUMBER)
        print('connecting to {} port {}'.format(*server_address))
        self.sock.connect(server_address)
        self.start_thread()

    def end_connection(self):
        print('closing socket')
        self.sock.close()

    def receive_fixed_length_msg(self, msglen):
        message = b''
        while len(message) < msglen:
            chunk = self.sock.recv(msglen - len(message))  # read few bytes
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            message = message + chunk
        return message

    def receive_message(self):
        header = self.receive_fixed_length_msg(common.HEADER_LENGTH)
        message_length = struct.unpack("!H", header)[0]  # length of the message
        message = None
        if message_length > 0:
            message = self.receive_fixed_length_msg(message_length)  # read message
            message = message.decode("utf-8")

        return message

    def send_message(self, message):
        encoded_message = message.encode("utf-8")
        header = struct.pack("!H", len(encoded_message))  # add header
        message = header + encoded_message
        self.sock.sendall(message)

    def message_receiver(self):
        while True:
            msg_received = self.receive_message()
            if len(msg_received) > 0:  # if message exists
                print(msg_received)

    def start_thread(self):
        thread = threading.Thread(target=self.message_receiver)
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    client = Client()
    client.send_message("jebo te")
    time.sleep(4)
    client.send_message("hecam se lubi")
