import socketserver
import datetime
import binascii

OUTBOUND_INTERFACE = b'enx0a003e6acab4'


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]

        ct = datetime.datetime.now()

        print("{}\t{}\twrote: {}\t({})".format( ct, self.client_address[0], data,binascii.hexlify(data)))

        ## Not sure why these are here but I suspect that they are part of an ack
        #.decode(encoding='UTF-8')
        #socket.sendto(data.upper(), self.client_address)

        # Let's give it a go
        # Except arent we just echoing back? 

        # Disabled to see what happens
        ACK = b'\x00\x01\x3f\x00\x00'
        socket.sendto(ACK, self.client_address)
        print("\tSent ACK {} to {}".format(binascii.hexlify(ACK), self.client_address))

if __name__ == "__main__":
    HOST, PORT = "192.168.10.2", 4005
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
