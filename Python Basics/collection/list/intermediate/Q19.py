#Find the average of the list [45,12, 78,34,90], then print all the elements that are greater than the average.

a=[45,12,78,34,90]
print(a)
s=0
i=0
n=len(a)
while i<len(a):
    s=s+a[i]
    i=i+1
avg=s/n
print("average:",avg)
print("elements that are greater than the average")
i=0
while i<len(a):
    if avg<a[i]:
        print(a[i],end=" ")
    i=i+1
