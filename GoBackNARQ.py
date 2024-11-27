import time,random
len=int(input("enter number of frames to transmit:"))
n=int(input("enter window size:"))
tout=float(input("enter timeout:"))

curr=0

while curr<len:
    ack=True
    if curr+n<=len:
        for i in range(0,n):
            print(f"sending packet {curr+i+1}...")
            time.sleep(1)
            if random.random()>tout:
                print("timeout!")
                ack=False
            else:
                print(f"packet {curr+i+1} successfully sent!")
           
        if ack==False:
            print(f"ACK lost or timeout occoured! retransmitting from frame {curr+1}")
        else:
            print(f"Ack for frames transmitted")
            curr+=n
    else:
        for i in range (curr,len):
            print(f"sending packet {i+1}...")
            time.sleep(1)
            if random.random()<tout:
                print("timeout!")
                ack=False
            else:
                print(f"packet {i+1} successfully sent!")
        if ack==False:
            print(f"ACK lost or timeout occoured! retransmitting from frame {curr}")
        else:
            print(f"Ack for frames transmitted")
            curr=len

            

