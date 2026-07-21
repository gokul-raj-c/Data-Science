# Keep asking the user for numbers until they enter 0, then print the average of all the numbers entered.

a=int(input("enter number: "))
c=0
s=0
while a!=0:
    c=c+1
    s=s+a
    a=int(input("enter number: "))
print("average=",s/c)

