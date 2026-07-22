#remove even numbers in the list

a=[11,22,44,66,88,22,33,44,55,66,88]
i=0
while i<len(a):
    if a[i]%2==0:
        a.pop(i)
    else:
        i=i+1
print(a)