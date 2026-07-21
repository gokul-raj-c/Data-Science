#Check whether a number is a perfect square without using sqrt — keep squaring 1, 2, 3, ... and compare.

a=int(input("enter number: "))
i=1
flag=0
while i**2<=a:
    if i**2==a:
        flag=1
    i=i+1

if flag==0:
    print("not perfect square")
else:
    print("perfect square")
