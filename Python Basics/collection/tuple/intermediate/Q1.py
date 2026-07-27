#Print the frequency of every value in the tuple (2, 4, 2, 6, 4, 2), showing each value only once

a=(2,4,2,6,4,2)
print(a)
i=0
while i<len(a):
    j=0
    f=0
    while j<i:
        if a[j]==a[i]:
            f=1
        j=j+1
    if f==0:
        j=0
        c=0
        while j<len(a):
            if a[i]==a[j]:
                c=c+1
            j=j+1
        print(a[i],"->",c)
    i=i+1
