#Find the smalles number in a list.

a=[12,3,4,10,9,7]
print(a)
small=a[0]
for i in a:
    if i<small:
        small=i
print(small)