#Merge two lists [1,2,3] and [4,5,6] into a single new list using a while loop and append(). (Do not use + or extend().)

a=[1,2,3]
b=[4,5,6]
i=0
while i<len(b):
    a.append(b[i])
    i=i+1
print(a)