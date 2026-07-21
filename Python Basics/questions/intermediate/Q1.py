#Find the sum of the squares of the digits of a number (e.g., 234 → 2² + 3² + 4² = 29).

a=int(input("enter number: "))
s=0
while a>0:
    d=a%10
    s=s+d**2
    a=a//10
print(s)