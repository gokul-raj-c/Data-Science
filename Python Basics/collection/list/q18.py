#count of names start with a

a=["arun","ann","vidya","noel","anagha"]
c=0
i=0
while i<len(a):
    if a[i][0]=="a":
        c=c+1
    i=i+1
print(c)