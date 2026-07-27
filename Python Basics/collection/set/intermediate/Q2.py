#Find the symmetric difference of {1, 2, 3} and {3, 4, 5} manually using while loops.

a={1,2,3}
b={3,4,5}
c=set()

x=list(a)
y=list(b)

i=0
while i<len(x):
    f=0
    j=0
    while j<len(y):
        if x[i]==y[j]:
            f=1
        j=j+1
    if f==0:
        c.add(x[i])
    i=i+1

i=0
while i<len(y):
    f=0
    j=0
    while j<len(x):
        if y[i]==x[j]:
            f=1
        j=j+1
    if f==0:
        c.add(y[i])
    i=i+1

print(a)
print(b)
print(c)