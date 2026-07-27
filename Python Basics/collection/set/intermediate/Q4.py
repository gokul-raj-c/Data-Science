#Check whether {2, 4} is a subset of {2, 4, 6, 8} without using issubset().

a={2,4}
b={2,4,6,8}

x=list(a)
y=list(b)

i=0
found=1
while i<len(x):
    flag=0
    j=0
    while j<len(y):
        if x[i]==y[j]:
            flag=1
        j=j+1
    if flag==0:
        found=0
    i=i+1
if found==1:
    print("subset")
else:
    print("not subset")