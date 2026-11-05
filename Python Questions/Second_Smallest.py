#Find the second-smallest element in a list without sorting

arr=[23,22,35,2,19,40]
small=arr[0]
for i in arr:
    if i < small:
        small=i
s_small=arr[0]
for i in arr:
    if i > s_small and i != small:
        s_large=i
print(small)
print(s_small)