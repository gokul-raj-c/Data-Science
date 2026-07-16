#Calculate the factorial of a number (e.g., 5! = 120).

a=int(input("enter number: "))
f=1
while a>=1:
    f=f*a
    a=a-1
print(f)