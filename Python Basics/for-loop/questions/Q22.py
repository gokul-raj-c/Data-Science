#Check whether a string is a palindrome.

s="malayalam"
y=""
for i in range(len(s)-1,-1,-1):
    y=y+s[i]
print(s)

if s==y:
    print("pallindrome")
else:
    print("not pallindrome")