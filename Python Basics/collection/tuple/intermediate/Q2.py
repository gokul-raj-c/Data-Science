#Find the second largest unique value in (12, 45, 67, 23, 89, 45) without sorting.

a=(12,45,67,23,89,45)
large=a[0]
i=0
while i<len(a):
    if a[i]>large:
        large=a[i]
    i=i+1
second_large=a[0]
i=0
while i<len(a):
    if a[i]!=large and a[i]>second_large:
        second_large=a[i]
    i=i+1
print(a)
print("second largest unique value:",second_large)