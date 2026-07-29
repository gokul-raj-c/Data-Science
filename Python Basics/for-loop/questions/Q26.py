#Check whether a number is prime.

a=int(input("enter number: "))
if a>1:
    f=0
    for i in range(2,a//2):
        if a%i==0:
            f=1
    if f==0:
        print("prime")
    else:
        print("not prime")
else:
    print("not prime")