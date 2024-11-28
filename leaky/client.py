import socket
address=('localhost',12345)
cs=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=""
while msg!="bye":
    x=input("enter size of data packet to send:")
    cs.sendto(x.encode(),address)
    print("packet sent!")