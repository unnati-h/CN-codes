msg=input("enter message:")
sf=input("enter start flag:")
ef=input("enter end flag:")
esc=input("enter esc flag:")
final=""
for i in msg:
    if i==sf:
        final+=esc
    elif i==ef:
        final+=esc
    elif i==esc:
        final+=esc
    final+=i
final=sf+final+ef
print(final)
        
