#Find the largest and smallest number in the tuple (23, 7, 91, 45, 18) using one while loop

a=(23,7,91,45,18)
i=0
large=a[0]
small=a[0]
while i<len(a):
    if a[i]>large:
        large=a[i]
    if a[i]<small:
        small=a[i]
    i=i+1
print(a)
print("largest:",large)
print("smallest:",small)