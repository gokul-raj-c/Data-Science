#Roots of a Quadratic

a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
d=(b*b)-(4*a*c)
if d>0:
    print("two real roots")
elif d==0:
    print("one real root")
else:
    print("no real roots")