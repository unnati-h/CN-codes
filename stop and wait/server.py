import time,socket,random
#this is done using udp protocol-connectionless-uses DGRAM
ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss.bind(("localhost",12346))
x=" "
while x!='end':
    data,addr=ss.recvfrom(1024)
    x=data.decode()
    print(f'packet recieved is {x}')
    time.sleep(0.5)
    if random.random()<0.3:
        print("ACK lost!")
        continue
    else:
        print("sending ACK for packet")
        ack=f'ACK for:{x}'
        ss.sendto(ack.encode(),addr)
ss.close()