import socket,random,time
address=('localhost',12345)
ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss.bind(address)
msg=""
curr=10
capacity=10
data,addr=ss.recvfrom(1024)
while msg!='bye':
    ss.settimeout(2)
    try:
        lvl=f"current amount of tokens={curr}"
        ss.sendto(lvl.encode(),addr)
        data,addr=ss.recvfrom(1024)
        msg=data.decode()
        x=int(msg)
        if x<=curr:
            curr-=x
            print(f"{x} tokens used, current level:{curr}")
        else:
            print(f"error! that many tokens not available ,packet of size {x} rejected")
    except:
        if curr<capacity:
            curr+=1
            print(f"token added, tokens available:{curr}")
            y=f"token added, tokens available:{curr}"
            ss.sendto(y.encode(),addr)
