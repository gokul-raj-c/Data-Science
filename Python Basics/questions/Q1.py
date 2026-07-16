# Find the sum of the digits of a given number (e.g., 456 -> 4 + 5 + 6 = 15).

a=int(input("enter a number: "))
s=0
while a>0:
    d=a%10
    s=s+d
    a=a//10
print("sum =",s)