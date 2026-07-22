#even numbers in one list and odd numbers in another list

a=[11,22,33,44,55,66,77]
b=[]
c=[]
i=0
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
print(b)
print(c)