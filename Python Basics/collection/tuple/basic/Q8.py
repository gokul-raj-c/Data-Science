#Check whether every number in the tuple (5, 10, 15, 20) is divisible by 5.

a=(5,10,15,20)
print(a)
flag=0
i=0
while i<len(a):
    if a[i]%5!=0:
        flag=1
    i=i+1
if flag==0:
    print("every number in the tuple is divisible by 5")
else:
    print("every number in the tuple is not divisible by 5")