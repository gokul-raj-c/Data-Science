#Count how many times a specific digit appears in a number (e.g., digit 2 in 12252-> 3 times).

a=int(input("enter number: "))
b=int(input("enter number to check: "))
c=0
while a>0:
    d=a%10
    a=a//10
    if d==b:
        c=c+1
print("count of",b,"=",c)