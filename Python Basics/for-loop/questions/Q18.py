#Count how many even numbers are present in a list.

a=[12,3,4,10,9,7]
print(a)
c=0
for i in a:
    if i%2==0:
        c=c+1
print(c)