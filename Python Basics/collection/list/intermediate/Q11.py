#Find the common elements between the two lists [1,2,3,4,5] and [3,5,7,9,1] and store them in a third list.

a=[1,2,3,4,5]  
b=[3,5,7,9,1]
c=[]
i=0
while i<len(a):
    j=0
    while j<len(b):
        if a[i]==b[j]:
            c.append(a[i])
        j=j+1
    i=i+1
print(c)