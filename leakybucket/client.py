import socket
import time 

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    x=int(input("Enter packet size to send:"))
    msg=str(x)
    cs.sendto(msg.encode(),('localhost',12345))
    print("packet sent!")
    time.sleep(1)