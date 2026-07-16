#Check whether a number is a palindrome (e.g., 121 is a palindrome, 123 is not).

a=int(input("enter a number: "))
num=a
rev=0
while a>0:
    d=a%10
    rev=rev*10+d
    a=a//10
if num==rev:
    print("pallindrome")
else:
    print("not pallindrome")