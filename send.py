import socket

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Enable broadcasting mode
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

UDP_IP = "<broadcast>"
UDP_PORT = 2880
MESSAGE = "Hello, from Pi broadcast 3.".encode()

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE.decode())


sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))