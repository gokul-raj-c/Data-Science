#Sort the list [5,2,9,1,7] in ascending order using nested while loops. (Do not use sort() or sorted().)

a=[5,2,9,1,7]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
print(a)