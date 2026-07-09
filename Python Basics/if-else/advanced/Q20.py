#Number Full Report

n=float(input("enter number: "))
if n<0:
    print("negative")
elif n>0:
    print("positive")
else:
    print("zero")

if n%2==0:
    print("even")
else:
    print("odd")

if abs(n)<10:
    print("single digit")
else:
    print("multiple digit")