import socket
from dao import dao, parsePacket
from recvall import recvall

SERVER_IP = "127.0.0.1"
LISTENING_PORT = 28801

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (SERVER_IP, LISTENING_PORT)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print ('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print ('connection from', client_address)
        
        message = recvall(connection)
        print('recieved',message)

        if message.startswith('**'):
            macInfo = parsePacket(message)
            if macInfo:
                dao(macInfo)
        else:
            print ("Invalid Request")
            
    finally:
        # Clean up the connection
        connection.close()