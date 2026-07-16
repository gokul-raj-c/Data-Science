# Print the Fibonacci series up to 10 terms (0, 1, 1, 2, 3, 5, 8, ...).

x=int(input("enter limit: "))
a=0
b=1
i=1
while i<=x:
    print(a,end=" ")
    c= a+b
    a=b
    b=c
    i=i+1