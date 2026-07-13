#Take a string from the user and check whether it is a palindrome (reads the same forwards and backwards, e.g. "level") using a while loop comparing characters from both ends.

s1=input("enter a string: ")
n=len(s1)-1
s2=""
while n>=0:
    s2=s2+s1[n]
    n=n-1
if s1==s2:
    print("pallindrome")
else:
    print("not pallindrome")
