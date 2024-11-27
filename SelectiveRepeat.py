import time,random

def transmit(x):
    ack=True
    print(f"sending packet {x}...")
    time.sleep(1)
    if random.random()>tout:
        print("timeout!")
        ack=False
    else:
        print(f"packet {x} successfully sent!")
    return ack

len=int(input("enter number of frames to transmit:"))
n=int(input("enter window size:"))
tout=float(input("enter timeout:"))

curr=0
ackstat=[0]*len

while curr<len:
    ackreg=[]
    ackacc=[]
    for i in range (curr,min(curr+n,len)):
        ackstat[i]=transmit(i)
    for i in range (curr,min(curr+n,len)):
        if ackstat[i]==False:
            ackreg.append(i)
        else:
            ackacc.append(i)
    print(f"ack for {ackacc}")
    print(f"retransmitting {ackreg}")
    ackacc=[]
    while ackreg!=[]:
        ackacc=[]
        for i in ackreg:
            print(f"retransmitting {i}")
            temp=transmit(i)
            ackreg.remove(i)
            if temp==False:
                ackreg.append(i)
            else:
                ackacc.append(i)
        if ackacc!=[]:
            print(f"ack for {ackacc}")
        if ackreg!=[]:print(f"retransmitting {ackreg}")
    curr+=n
