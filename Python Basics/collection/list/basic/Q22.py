#From the list [3, 6, 10, 12, 15, 20], find the sum of only the numbers divisible by 3.

a=[3,6,10,12,15,20]
s=0
i=0
while i<len(a):
    if a[i]%3==0:
        s=s+a[i]
    i=i+1
print(a)
print("sum of numbers in list divisible by 3:",s)
