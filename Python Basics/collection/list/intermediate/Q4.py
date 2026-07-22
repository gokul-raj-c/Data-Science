#Reverse the list [1,2,3,4,5] by building a new list using a while loop. Do not use reverse() or slicing.) 

a=[1,2,3,4,5]
b=[]
i=len(a)-1
while i>=0:
    b.append(a[i])
    i=i-1
print(b)