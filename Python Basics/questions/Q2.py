#Count the number of digits in a given number (e.g., 4587 -> 4 digits)

a=int(input("enter a number: "))
if a==0:
    print(1)
else:
    c=0
    while a>0:
        a=a//10
        c=c+1
    print("no of digits =",c)