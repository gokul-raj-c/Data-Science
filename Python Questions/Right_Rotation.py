#Rotate the list two positions to the right.

a=[1,2,3,4,5]
print(a)
b=a[0]
a.pop(0)
a.append(b)
print(a)