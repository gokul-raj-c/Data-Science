#Find and print the smallest number in the list [23,7,91,45,18] using a while loop.

a=[23,7,91,45,18]
small=a[0]
i=1
while i<len(a):
    if a[i]<small:
        small=a[i]
    i=i+1
print("small =",small)