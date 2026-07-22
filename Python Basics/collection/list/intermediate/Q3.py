#Find the second largest number in the list [14, 62,8, 45,62, 33] using while loops.

a=[14, 62,8, 45,62, 33]
large=a[0]
i=1
while i<len(a):
    if a[i]>large:
        large=a[i]
    i=i+1

second=a[0]
i=0
while i<len(a):
    if a[i]!=large and a[i]>second:
        second=a[i]
    i=i+1
print(second)