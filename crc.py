def xor(a,b):
    res=''
    for k in range (0,len(a)):
        if a[k]==b[k]:
            res+='0'
        else:
            res+='1'
    return res
def negate(x):
    y='0'*len(x)
    return y
initialdata=input("Enter Data:")
div=input("Enter Divisor:")
data=initialdata+"0"*(len(div)-1)
div1=""
if data[0]==div[0]:
    div1=div
else:
    div1=negate(div)
temp=data[0:4]
rem=xor(div1,temp)
print(div,rem)
i=4
rem=rem[1:]
while i<len(data):
    rem+=data[i]
    #print(rem)
    if rem[0]==div[0]:
        div1=div
    else:
        div1=negate(div)
    newrem=xor(div1,rem)
    rem=newrem[1:]
    #print(div1,rem,newrem)
    i+=1
print(initialdata+rem)
data=initialdata+rem
