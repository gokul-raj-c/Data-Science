s=input("enter string: ")
i=0
c=0
while i<len(s):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        c=c+1
    i=i+1
print("count of vowels:",c)