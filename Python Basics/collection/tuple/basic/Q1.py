# From the tuple (10, 25, 30, 45, 50), count how many numbers are multiples of 5 and greater than 20.

a=(10,25,30,45,50)
i=0
c=0
while i<len(a):
    if a[i]>20 and a[i]%5==0:
        c=c+1
    i=i+1
print(a)
print("count of numbers that are multiples of 5 and greater than 20:",c)
