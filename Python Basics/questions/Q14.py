#Keep asking the user for numbers and find the largest number entered, stopping when they enter 0.

a=int(input("enter number: "))
large=0
while a!=0:
    if a>large:
        large=a
    a=int(input("enter number: "))
print(large)