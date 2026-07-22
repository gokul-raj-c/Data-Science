#prime number count in the list

a=[2,3,5,7,11,22]
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
            c=c+1
    i=i+1
print(c)