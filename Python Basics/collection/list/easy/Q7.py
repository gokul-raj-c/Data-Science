#Find and print the largest number in the list [23,7,91,45,18] using a while loop.

a=[23,7,91,45,18]
large=a[0]
i=1
while i<len(a):
    if a[i]>large:
        large=a[i]
    i=i+1
print("large =",large)