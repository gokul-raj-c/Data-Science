#Ask the user to enter 5 numbers one by one and print both the largest and the smallest of them.

a=int(input("enter number: "))
large=a
small=a
i=1
while i<5:
    a=int(input("enter number: "))
    if a>large:
        large=a
    if a<small:
        small=a
    i=i+1
print("large:",large)
print("small:",small)