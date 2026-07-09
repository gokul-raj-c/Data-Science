#Right-Angled Triangle

a=int(input("enter side 1: "))
b=int(input("enter side 2: "))
c=int(input("enter side 3: "))

if (a+b>c) and (b+c>a) and (a+c>b):
    if a >= b and a >= c:
        if b*b + c*c == a*a:
            print("Right-angled triangle")
        else:
            print("Not right-angled")
    elif b >= a and b >= c:
        if a*a + c*c == b*b:
            print("Right-angled triangle")
        else:
            print("Not right-angled")
    else:
        if a*a + b*b == c*c:
            print("Right-angled triangle")
        else:
            print("Not right-angled")
else:
    print("Not a triangle")