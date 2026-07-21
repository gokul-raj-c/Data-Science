#Check whether a number is a Strong number (sum of the factorials of its digits equals the number, 
# e.g., 145 → 1! + 4! + 5! = 145).

a=int(input("enter number: "))
b=a
summ=0
while a>0:
    d=a%10
    i=d
    fact=1
    while i>1:
        fact=fact*i
        i=i-1
    summ=summ+fact
    a=a//10
if summ==b:
    print("strong")
else:
    print("not strong")