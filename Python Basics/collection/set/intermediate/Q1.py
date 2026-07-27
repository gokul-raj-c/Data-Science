#Find the intersection of {2, 4, 6, 8} and {1, 2, 3, 4} manually using a while loop.

a={2,4,6,8}
b={1,2,3,4}
c=set()

x=list(a)
y=list(b)
i=0
while i<len(x):
    j=0
    while j<len(y):
        if x[i]==y[j]:
            c.add(x[i])
        j=j+1
    i=i+1

print(a)
print(b)
print(c)