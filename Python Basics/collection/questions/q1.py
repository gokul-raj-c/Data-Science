#Find the largest number in [23, 7, 45, 12, 39] without using max() . Print the number and the position where it is stored.

a=[23,7,45,12,39]
large=a[0]
for i in a:
    if i>large:
        large=i
print(a)
print(large)