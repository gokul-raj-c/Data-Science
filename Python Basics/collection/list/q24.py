#remove prime numbers from the list

a=[0,1,22,2,3,5,7,24,11]
c=0
i=0
while i<len(a):
    if a[i]>1:
        j=2
        flag=0
        while j<a[i]:
            if a[i]%j==0:
                flag=1
            j=j+1
        if flag==0:
            a.pop(i)
        else:
            i=i+1
    else:
        i=i+1
print(a)