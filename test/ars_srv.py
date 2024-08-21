# For more information on ARS https://cwh050.blogspot.com/2020/03/mototrbo-ars.html

import socketserver
import datetime
import binascii
import socket

OUTBOUND_INTERFACE = b'enx0a003ed4b8e5'
OUTBOUND_INTERFACE = b'enx0a003e2044dd'


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        #socket = self.request[1]

        ct = datetime.datetime.now()

        print("{}\t{}\twrote: {}\t({})".format( ct, self.client_address[0], data,binascii.hexlify(data)))

        # Check if its a regestration or DEregesteration request
        # REGESTRATION b'\x00\t\xf0 \x044040\x00\x00'   (b'0009f02004343034300000'
        
        # DERegestration (PowerOff)
        #    12.0.19.186     wrote: b'\x00\x011'     (b'000131')
        
        # ACK to ARS Query 00 01 74  from Control
        #   12.0.19.186     wrote: b'\x00\x01?'     (b'00013f')
        
        # HEADER | RADIOID | ????

        # The following are ACK statements to reply to the subscriber radio with
        # Note that the last byte is min to refresh (check back in)
        # In theory the radio will only attemp to "register" again at a random point in between
        #ACK = b'\x00\x02\xbf\x01' #  1min
        #ACK = b'\x00\x02\xbf\x05' #  5min
        #ACK = b'\x00\x02\xbf\x0a' # 10min
        #ACK = b'\x00\x02\xbf\x0f' # 15min
        ACK = b'\x00\x02\xbf\x1e' # 30min
        #ACK = b'\x00\x02\xbf\x3c' # 60min

        # Going to open another socket, this is UDP we have async conversations
        tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        tx_sock.setsockopt(socket.SOL_SOCKET, 25, OUTBOUND_INTERFACE)
        tx_sock.sendto(ACK, self.client_address)
        print("\tSent ACK {} to {}".format(binascii.hexlify(ACK), self.client_address))

if __name__ == "__main__":
    HOST, PORT = "192.168.10.2", 4005
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
