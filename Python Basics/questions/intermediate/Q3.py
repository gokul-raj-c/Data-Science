# Swap the first and last digits of a number (e.g., 1234 → 4231).

a=int(input("enter number: "))
c=0
last=a%10

temp=a
while temp>0:
    c=c+1
    temp=temp//10

temp=a
while temp>10:
    temp=temp//10
first=temp

mid=(a%(10**(c-1)))//10

num=last*(10**(c-1))+(mid*10)+first

print(num)

