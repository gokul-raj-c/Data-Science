#From the list ["pen", "book", "pen", "bag", "book", "scale"], use sets to find the duplicate items.

a=["pen","book","pen","bag","book","scale"]
res=set()
dup=set()
i=0
while i<len(a):
    if a[i] in res:
        dup.add(a[i])
    else:
        res.add(a[i])
    i=i+1
print(a)
print(dup)