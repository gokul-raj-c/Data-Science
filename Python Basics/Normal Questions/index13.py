a=int(input("enter num 1: "))
b=int(input("enter num 2: "))
c=int(input("enter num 3: "))
if a>b:
    if a>c:
        print(a," is greater")
    else:
        print(c, " is greater")
else:
    if b>c:
        print(b, " is greater")
    else:
        print(c, " is greater")