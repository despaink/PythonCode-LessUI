import socket
import time

#run with sudo, else port 67 is not allowed.

UDP_IP = ""
UDP_PORT = 2880
DHCP_PORT = 67
UDP_RECEIVE_LENGTH = 1024

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, DHCP_PORT))

outFile = open("dhcpOut.txt","w")
outFile.write("")
outFile.close()

while True:
    
        data, addr = sock.recvfrom(UDP_RECEIVE_LENGTH) # buffer size is 1024 bytes
        print ("received message.")
        print ("length of data: " , len(data))
        try:
            MAC_ADDR = " mac Address {0}:{1}:{2}:{3}:{4}:{5}\n".format(hex(data[28]),hex(data[29]),hex(data[30]),hex(data[31]),hex(data[32]),hex(data[33]))# 28-33
            pass
        except TypeError:
            print("****************TYPE ERROR**********")
            errFile = open("errorLog67.txt","ab")
            errFile.write(data)
            errFile.close()
            errFile = open("errorLog67.txt","a")
            errFile.write("\n")
            errFile.close()
            pass
        else:        
            print(MAC_ADDR)
            print ("options: ", data[236:])

            outFile = open("dhcpOut.txt","a")    
            outFile.write(time.asctime(time.localtime()))
            outFile.write(MAC_ADDR)
            outFile.close()
        
    
