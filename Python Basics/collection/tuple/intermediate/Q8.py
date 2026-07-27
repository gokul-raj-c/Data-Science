#Convert (5, -3, 8, -12, 0, -1) into a tuple where every negative number is replaced with 0

a=(5,-3,8,-12,0,-1)
print(a)
a=list(a)
i=0
while i<len(a):
    if a[i]<0:
        a[i]=0
    i=i+1
print(tuple(a))


