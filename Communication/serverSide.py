try:
    import TicTacToe.Common.commonVariables as common
except ModuleNotFoundError:
    import Common.commonVariables as common

import socket
import struct
import threading


class Server:
    def __init__(self):
        self.clients = []  # list of players
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
        server_address = (common.SERVER_NAME, common.PORT_NUMBER)  # # Bind the socket to the port
        print('starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)
        self.sock.listen(1)

    def receive_fixed_length_msg(self, sock, msglen):
        message = b''
        while len(message) < msglen:
            try:
                chunk = sock.recv(msglen - len(message))  # read few bytes
                if chunk == b'':
                    raise RuntimeError("socket connection broken")
                message = message + chunk
            except ConnectionResetError:  # someone has disconnected
                break
        return message

    def receive_message(self, sock):
        header = self.receive_fixed_length_msg(sock, common.HEADER_LENGTH)
        if len(header) == 0:  # player has disconnected
            return None
        message_length = struct.unpack("!H", header)[0]  # length of the message
        message = None
        if message_length > 0:  # ce je vse OK
            message = self.receive_fixed_length_msg(sock, message_length)  # read message
            message = message.decode("utf-8")
        return message

    def send_message(self, sock, message):
        encoded_message = message.encode("utf-8")
        header = struct.pack("!H", len(encoded_message))  # add header
        message = header + encoded_message
        sock.sendall(message)

    def client_thread(self, client_sock):
        print("[system] we now have " + str(len(self.clients)) + " players")
        while True:
            msg_received = self.receive_message(client_sock)
            if not msg_received:
                break
            self.procces_message(msg_received)
            print(msg_received)
        self.clients.remove(client_sock)
        print("[system] we now have " + str(len(self.clients)) + " player")
        client_sock.close()

    def start_listening(self):
        while True:
            try:
                # wait for a new connection
                client_sock, client_addr = self.sock.accept()
                self.clients.append(client_sock)
                thread = threading.Thread(target=self.client_thread, args=(client_sock,))
                thread.daemon = True
                thread.start()

            except KeyboardInterrupt:
                break

    def procces_message(self, msg):
        # TODO: proccesing logic
        #for sock in self.clients:
        #    self.send_message(sock, msg.upper())
        pass

    def close(self):
        self.sock.close()


if __name__ == "__main__":
    server = Server()
    server.start_listening()
    server.close()

