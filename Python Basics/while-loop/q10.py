s=input("enter string: ")
i=0
c=0
while i<len(s):
    if s[i]=="a":
        c=c+1
    i=i+1
print("count of a:",c)