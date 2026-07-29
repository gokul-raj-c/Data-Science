#Count how many times each element appears in a list.

s=[1,2,3,1,5,6]
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