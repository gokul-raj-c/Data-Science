# Count how many vowels (a, e, i, o, u) are in the string "education" using a while loop and an if condition

s="education"
n=len(s)-1
i=0
c=0
while i<=n:
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        c=c+1
    i=i+1
print("no of vowels:",c)