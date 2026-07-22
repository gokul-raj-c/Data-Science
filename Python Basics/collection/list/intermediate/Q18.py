#Replace every negative number in the list [5,-3,8,-12,0,-1] with 0 using a while loop, then print the updated list

a=[5,-3,8,-12,0,-1]
i=0
while i<len(a):
    if a[i]<0:
        a[i]=0
    i=i+1
print(a)