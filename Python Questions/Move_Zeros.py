#Move all zeros to the end of the list while maintaining the order of other elements.

a=[0,2,0,5,3,0,8]
b=[]
c=0
i=0
print(a)
for i in a:
    if i == 0:
        c+=1
    else:
        b.append(i)
print(b)
while c>0:
    b.append(0)
    c-=1
print(b)
        
