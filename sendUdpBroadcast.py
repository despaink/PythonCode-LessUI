import socket

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Enable broadcasting mode
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

UDP_IP = "192.168.0.82"
UDP_PORT = 2880
MESSAGE = "**INSERT** 123, test, 1".encode()

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE.decode())


sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))