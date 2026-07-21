#Keep asking the user for numbers until they enter 0, then print the average of the numbers and the largest number entered.

a=int(input("enter number: "))
large=a
c=0
summ=0
while a!=0:
    c=c+1
    summ=summ+a
    if a>large:
        large=a
    a=int(input("enter number: "))
    
if c>0:
    print("average=",summ/c)
    print("larges=",large)
else:
    print("you enter 0")
    
