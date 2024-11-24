def parity(x):
    count=0
    for i in x:
        if i=='1':
            count+=1
    if count%2==0:
        return '0'
    return '1'
    
data=input("Enter data:")
data=data[::-1]
data="$"+data
code=[0]*12
code[0]="$"
code[3]=data[1]
code[5]=data[2]
code[6]=data[3]
code[7]=data[4]
code[9]=data[5]
code[10]=data[6]
code[11]=data[7]
#parity bits
code[1]=parity([code[3],code[5],code[7],code[9],code[11]])
code[2]=parity([code[3],code[6],code[7],code[10],code[11]])
code[4]=parity([code[5],code[6],code[7]])
code[8]=parity([code[9],code[10],code[11]])

print(code[::-1])
        
