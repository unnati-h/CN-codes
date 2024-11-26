import time
import socket
def leak(level):
    if level>0:
        level-=2
        print(f"leaked 2 packets, current level:{level}")
        return level
    else:
        print("bucket empty")
ss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss.bind(('localhost',12345))
capacity=10
clevel=0
i=0
while True:
    data,addr=ss.recvfrom(1024)
    x=int(data.decode())
    if x+clevel<=capacity:
        clevel+=x
        print(f"recieved packet of size {x}, current level: {clevel}")
    else:
        print(f"bucket full!! rejected packet of size {x}")
    time.sleep(0.5)
    clevel=leak(clevel)
    time.sleep(1)


