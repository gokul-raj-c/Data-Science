#Remove all duplicate values from the list [1,3,1,5,3,7,5] and print the new list containing only unique values.

a=[1,3,1,5,3,7,5]
b=[]
i=0
while i<len(a):
    j=0
    f=0
    while j<len(b):
        if a[i]==b[j]:
            f=1
        j=j+1
    if f==0:
        b.append(a[i])
    i=i+1
print(b)