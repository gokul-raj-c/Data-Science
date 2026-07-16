# Reverse a number using a while loop (e.g., 123 -> 321).

a=int(input("enter a number: "))
rev=0
while a>0:
    d=a%10
    rev=rev*10+d
    a=a//10
print(rev)