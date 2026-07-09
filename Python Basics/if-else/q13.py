# Triangle Valid?

a=int(input("enter side 1: "))
b=int(input("enter side 2: "))
c=int(input("enter side 3: "))
if (a + b > c) and (b + c > a) and (a + c > b):
    print("Valid triangle")
else:
    print("Not a triangle")