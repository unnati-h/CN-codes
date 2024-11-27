def iseven(sum):
    sum=int(sum)
    if sum%2==0:
        return 0
    return 1

data1=input("enter transmitted data (9-bit):")
data1='$'+data1[::-1]
data=['$']*len(data1)
#reversing the data because in hamming code we count bits from right to left 
#adding a dummy charachter to make calculation easy and remove offset
for i in range (1,len(data1)):
    data[i]=int(data1[i])
p1=data[1]+data[3]+data[5]+data[7]+data[9]
p2=data[2]+data[3]+data[6]+data[7]
p4=data[4]+data[5]+data[6]+data[7]
p8=data[8]+data[9]

c1=iseven(p1)
c2=iseven(p2)
c4=iseven(p4)
c8=iseven(p8)

decierror=f"{c8}{c4}{c2}{c1}"
binerror=int(decierror,2)
print(f"error at position:{binerror}")

corrected=""
for i in range (0,len(data1)):
    if i==binerror:
        corrected+='0' if data1[i]=='1' else '1'
    else:
        corrected+=data1[i]

corrected=corrected[1:]
corrected=corrected[::-1]
print(f"corrected data:{corrected}")
