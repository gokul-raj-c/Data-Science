#Find the average of the list [45,12, 78,34,90], then print all the elements that are greater than the average.

a=[45,12, 78,34,90]
n=len(a)
i=0
s=0
while i<n:
    s=s+a[i]
    i=i+1
avg=s/n
print("average =",avg)
i=0
while i<n:
    if avg<a[i]:
        print(a[i])
    i=i+1