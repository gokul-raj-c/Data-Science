#Find the sum of all numbers in the list [5,12,8,20,3] using a while loop.(Do not use sum().)

a=[5,12,8,20,3]
s=0
i=0
while i<len(a):
    s=s+a[i]
    i=i+1
print(s)