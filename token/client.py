import socket
address=('localhost',12345)
cs=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg="hi"
cs.sendto(msg.encode(),address)
while msg!="bye":
    x=input("enter number of tokens to use:")
    cs.sendto(x.encode(),address)
    print("packet sent!")