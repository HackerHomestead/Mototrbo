# This needs to be adapted to send an ARS query to the remote radio
# Given the correct bytes should be about the same

import socket
import datetime
import binascii
import sys
from Protocol import *

protocol = Protocol()
OUTBOUND_INTERFACE = b'enx0a003ec8e4e3' 
OUTBOUND_INTERFACE = b'enx0a003e2044dd'
TARGET_RADIO_ID = 5050
CAI = 12

UDP_IP = "12.0.35.130" # Radio ID 9090
UDP_IP = "12.0.19.186" # Radio ID 5050
UDP_PORT = 4005

# This is a example message MESSAGE = b'\x00\x12\xe0\x00\x88\x04\r\x00\n\x00h\x00e\x00l\x00l\x00o\x00'
MESSAGE = b'\x00\x01\x74' # ARS Query

print ("UDP target IP:", UDP_IP)
print ("Target Radio ID", protocol.ip2id(UDP_IP), " -> ", protocol.id2ip(CAI, TARGET_RADIO_ID))
print ("UDP target port:", UDP_PORT)
print ("message:", binascii.hexlify(MESSAGE))

# Setup the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# Attemping to bind to interface, i.e. use this network interface
sock.setsockopt(socket.SOL_SOCKET, 25, OUTBOUND_INTERFACE)

# Send the Packet
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
