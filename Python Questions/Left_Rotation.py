#Rotate the list one position to the left.

a=[1,2,3,4,5]
print(a)
b=a[0]
a.pop(0)
a.append(b)
print(a)