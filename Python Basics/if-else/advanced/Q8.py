#Largest AND Smallest of Three

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a>=b and a>=c:
    large = a
elif b>=a and b>=c:
    large = b
else:
    large = c

if a<=b and a<=c:
    small = a
elif b<=a and b<=c:
    small = b
else:
    small = c
    
print("large:", large)
print("small:", small)