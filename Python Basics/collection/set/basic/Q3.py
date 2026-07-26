#Create the union of {10, 20, 30} and {30, 40, 50} manually using while loops and add().

a={10,20,30}
b={30,40,50}
x=list(a)
y=list(b)
res=set()
i=0
while i<len(x):
    res.add(x[i])
    i=i+1
i=0
while i<len(y):
    res.add(y[i])
    i=i+1
print(res)