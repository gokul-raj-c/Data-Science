#count of names start with a and end with a

a=["arun","adithya","ann","vidya","noel","anagha"]
c=0
i=0
while i<len(a):
    if a[i][0]=="a" and a[i][-1]=="a":
        c=c+1
        print(a[i])
    i=i+1
print(c)