#Find the second-largest element in a list without sorting

arr=[23,22,35,2,19,40]
large=arr[0]
for i in arr:
    if i > large:
        large=i
s_large=arr[0]
for i in arr:
    if i > s_large and i != large:
        s_large=i
print(large)
print(s_large)