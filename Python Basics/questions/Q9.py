#Find the smallest digit in a number (e.g., 4729 -> 2).

a=int(input("enter a number: "))
small=9
while a>0:
    d=a%10
    if d<small:
        small=d
    a=a//10
print(small)