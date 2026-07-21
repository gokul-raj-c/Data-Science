#Ask the user for a number and print its multiplication table in reverse, from N x 10 down to N x 1.

a=int(input("enter number: "))
i=10
while i>=1:
    print(a,"*",i,"=",a*i)
    i=i-1