import socket,random,time
address=('localhost',12345)
ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss.bind(address)
msg=""
curr=0
capacity=10
while msg!='bye':
    ss.settimeout(2)
    try:
        data,addr=ss.recvfrom(1024)
        msg=data.decode()
        x=int(msg)
        if x+curr<=capacity:
            curr+=x
            print(f"packet of size {x} recieved, current level:{curr}")
        else:
            print(f"bucket overflow,packet of size {x} rejected")
        curr-=2
        print(f"bucket leaked! current level:{curr}")
    except:
        if curr>0:
            curr-=2
            print(f"bucket leaked! current level:{curr}")
