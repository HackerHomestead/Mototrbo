# nc -ul 127.0.0.1 5005
import socket
import binascii

OUTBOUND_INTERFACE = b'enx0a003ec8e4e3' 

# Todo allow conversion between radioid and ip 
UDP_IP = "12.0.35.130"
UDP_PORT = 4001

# command 0xf disabled lrrp
#MESSAGE = b'\x2204\x3727\x1707\x0f'
# command 0x9
#MESSAGE = b'\x2204\x3727\x1707\x5074\x6934\x31\x01\x09'
MESSAGE = binascii.unhexlify('1409220541424344453F02')
#print(bytes.fromhex('1409220541424344453F02'))
#MESSAGE = binascii.hexlify(b'130B2305006611')
print(MESSAGE)
print(bytearray.fromhex('1409220541424344453F02'))
print(binascii.b2a_hex( b'\x14\t"\x05ABCDE?\x02'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
# Attemping to bind to interface, i.e. use this network interface
sock.setsockopt(socket.SOL_SOCKET, 25, OUTBOUND_INTERFACE)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.close()
