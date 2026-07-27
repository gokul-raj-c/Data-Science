#From (2, 3, 4, 5, 6, 7, 8, 9), create a list containing only prime numbers.

a=(2,3,4,5,6,7,8,9)
print(a)
prime=[]
i=0
while i<len(a):
    if a[i]>1:
        j=2
        f=0
        while j<a[i]:
            if a[i]%j==0:
                f=1
            j=j+1
        if f==0:
            prime.append(a[i])
    i=i+1
print(prime)
