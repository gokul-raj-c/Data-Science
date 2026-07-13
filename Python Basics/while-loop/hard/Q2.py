#Ask the user for a number and check if it is a prime number using a while loop (test divisibility from 2 upward)

n=int(input("enter a number: "))
if n<=1:
    print("not prime")
else:
    i=2
    flag=0
    while i<n:
        if n%i==0:
            flag=1
        i=i+1
    if flag==0:
        print("prime")
    else:
        print("not prime")