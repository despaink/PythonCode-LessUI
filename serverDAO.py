import socket
from dao import dao, MacInfo, remove_prefix

UDP_IP = "127.0.0.1"
UDP_PORT = 2880

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

#It is assumed that messages will be of the format: **OPERATION** mac,hostname,watch
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    message = data.decode()
    
    print ("received message: ", data.decode())