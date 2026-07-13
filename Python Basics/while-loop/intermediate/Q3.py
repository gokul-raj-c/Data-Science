#Take an integer from the user and print its digits in reverse using a while loop (e.g. 1234 -> 4 3 2 1)

n=int(input("enter number: "))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)