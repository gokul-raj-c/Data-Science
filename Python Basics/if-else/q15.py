# Triangle Type by Sides

a=int(input("enter side 1: "))
b=int(input("enter side 2: "))
c=int(input("enter side 3: "))
if (a + b > c) and (b + c > a) and (a + c > b):
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")