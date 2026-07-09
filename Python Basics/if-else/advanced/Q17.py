# Full Calculator with Errors

a=int(input("enter first number: "))
b=int(input("enter second number: "))
x=input("choose operator(+, -, *, /, %): ")
if x=="+":
    print(a+b)
elif x=="-":
    print(a-b)
elif x=="*":
    print(a*b)
elif x=="/":
    if b==0:
        print("math error")
    else:
        print(a/b)
elif x=="%":
    if b==0:
        print("math error")
    else:
        print(a%b)
else:
    print("invalid input")