#Print all prime numbers between 1 and N.
n=int(input("enter number: "))
for i in range(1,n+1):
    if i>1:
        f=0
        for j in range(2,i):
            if i%j==0:
                f=1
        if f==0:
            print(i)
        