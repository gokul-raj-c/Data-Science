#Search for the number 25 in the list [10,25,30,45] using a while loop.
# Print "Found" if it exists, otherwise print "Notfound".

a=[10,25,30,45]
i=0
f=0
while i<len(a):
    if a[i]==25:
        f=1
    i=i+1
if f==1:
    print("found")
else:
    print("not found")