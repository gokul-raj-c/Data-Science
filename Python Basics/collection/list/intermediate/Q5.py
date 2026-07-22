#Separate the list [4,9, 12,7,20,15] into two lists- one for even numbers and one for odd numbers. Print both.

a=[4,9, 12,7,20,15]
even=[]
odd=[]
i=0
while i<len(a):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
    i=i+1
print(even)
print(odd)