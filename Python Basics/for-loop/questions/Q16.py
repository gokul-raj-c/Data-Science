#Find the largest number in a list.

a=[12,3,4,10,9,7]
print(a)
large=a[0]
for i in a:
    if i>large:
        large=i
print(large)