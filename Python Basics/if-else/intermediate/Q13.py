#Closer to 10

a=int(input("enter first number: "))
b=int(input("enter second number: "))
if abs(a-10) < abs(b-10):
    print("first")
elif abs(a-10) > abs(b-10):
    print("second")
else:
    print("same")