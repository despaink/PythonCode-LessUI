import socket
import time
import dao
from functools import reduce
import operator

#run with sudo, else port 67 is not allowed.

LESS_IP = "<broadcast>"
LESS_PORT = 2880

UDP_IP = ""
UDP_PORT = 2880
DHCP_PORT = 67
UDP_RECEIVE_LENGTH = 1024

broadcastSocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Enable broadcasting mode
broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

listeningSocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
listeningSocket.bind((UDP_IP, DHCP_PORT))

outFile = open("dhcpOut.txt","w")
outFile.write("")
outFile.close()
errFile = open("errorLog67.txt","w")
errFile.write("")
errFile.close()

while True:
    
        data, addr = listeningSocket.recvfrom(UDP_RECEIVE_LENGTH) # buffer size is 1024 bytes
        print ("received message.")
        print ("length of data: " , len(data))
        try:
            MAC_ADDR = "{0:x}:{1:x}:{2:x}:{3:x}:{4:x}:{5:x}".format(data[28],data[29],data[30],data[31],data[32],data[33])# 28-33
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

            watched = dao.dao(dao.MacInfo('select',None,None,None,"select * from address_book where mac = '{}'".format(MAC_ADDR)))
            
            #notify listening devices
            if watched is None:
                broadcastSocket.sendto(MAC_ADDR.encode(),(LESS_IP,LESS_PORT))
            else:
                if watched[1] == 1:
                    print("Watching: {}".format(watched))
                    msg = "{} who you wanted to **watch**, has connected to your WI-FI".format(watched[2])
                    broadcastSocket.sendto(msg.encode(),(LESS_IP,LESS_PORT))
                else:
                    print("Ignoring: " + watched[2])


            #leave a trace
            outFile = open("dhcpOut.txt","a")    
            outFile.write(time.asctime(time.localtime()))
            outFile.write(MAC_ADDR)
            outFile.close()
        
    
