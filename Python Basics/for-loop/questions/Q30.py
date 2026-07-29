#Find the frequency of each character in a string.

s=input("enter string: ")
print(s)
b=[]
for i in s:
    if i not in b:
        c=0
        for j in s:
            if i==j:
                c=c+1
        print(i,"->",c)
        b.append(i)
