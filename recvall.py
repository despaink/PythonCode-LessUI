import socket

def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = ''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part.decode()
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break        
    return data