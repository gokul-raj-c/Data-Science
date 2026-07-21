#Find the sum of the digits of a number using a while loop (e.g., 472 → 4 + 7 + 2 = 13).

a=int(input("enter a number: "))
s=0
while a>0:
    d=a%10
    s=s+d
    a=a//10
print("sum =",s)