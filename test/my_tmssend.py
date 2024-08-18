import socket


OUTBOUND_INTERFACE = b'enx0a003ec8e4e3' 
UDP_IP = "12.0.35.130" # Radio ID 9090
UDP_PORT = 4007

MESSAGE = b'\x00\x12\xe0\x00\x88\x04\r\x00\n\x00h\x00e\x00l\x00l\x00o\x00'
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

# Setup the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

# Attemping to bind to interface, i.e. use this network interface
sock.setsockopt(socket.SOL_SOCKET, 25, OUTBOUND_INTERFACE)

# Send the Packet
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
