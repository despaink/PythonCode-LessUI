import socket
import sys
from recvall import recvall 

insert = '** insert, 123, hostname, 0'
updateHost ='** updateHostname,123,newName,1'
updateWatch = '** updateWatch,     123, hostName,      1'
delete = '** delete, 123, hostname, 0'
select = "** select, 123, hostname, 0, SELECT * from ADDRESS_BOOK where MAC = '123' "

deleteBad= '** delete, 123, hostname, 0, **'
tooFew = "** ?,?"
tooMany = "** 1,2,3 ,4,5,6"
selectBad = '** select 123, hostname, 0'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('kPi', 28801)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:    
    # Send data
    message = select
    print ('sending "%s"' % message)
    sock.sendall(message.encode())
    
    data = recvall(sock)
    print('recieved: {}'.format(data))

finally:
    print ('closing socket')
    sock.close()