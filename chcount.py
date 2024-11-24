n=int(input("Enter number of frames:"))
f=[]
for i in range(0,n):
    x=input(f"Enter frame {i+1}:")
    f.append(x)
final=""
for i in f:
    final+=(str(len(i)+1)+i)
print(final)   
