# Simple Calculator

a=int(input("enter number 1: "))
b=int(input("enter number c: "))
x=input("choose operator (+, -, *, /): ")
if x=='+':
    print(a+b)
elif x=='-':
    print(a-b)
elif x=='*':
    print(a*b)
elif x=='/':
    if b==0:
        print("Cannot divide by zero")
    else:
        print(a/b)
else:
    print("Invalid operator")