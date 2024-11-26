import socket,time
#this is done using udp protocol-connectionless-uses DGRAM
cs=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

message=""
while message!='end':
    message=input("Enter data to send here:")
    cs.sendto(message.encode(),('localhost',12346))

    cs.settimeout(5)
    try:
        data,addr=cs.recvfrom(1024)
        print(data.decode())
    except socket.timeout:
        print("ACK not recieved, retransmitting.....")
        cs.sendto(message.encode(),('localhost',12346))

cs.close()
