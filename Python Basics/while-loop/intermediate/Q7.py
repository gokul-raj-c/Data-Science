#Count the number of digits in a given number (e.g., 4587 -> 4 digits)

a=int(input("enter a number: "))
c=0
while a>0:
    c=c+1
    a=a//10
print("no of digits =",c)