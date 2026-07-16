#Check whether a given number is prime or not.

a=int(input("enter a number: "))
if a<=1:
    print("not prime")
else:
    i=2
    flag=0
    while i<a//2:
        if a%i==0:
            flag=1
        i=i+1
    if flag==0:
        print("prime")
    else:
        print("not prime")