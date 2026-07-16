#Find the largest digit in a number (e.g., 4729 -> 9)

a=int(input("enter a number: "))
large=0
while a>0:
    d=a%10
    if d>large:
        large=d
    a=a//10
print(large)