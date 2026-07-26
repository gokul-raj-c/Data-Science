# Check whether every item in {2, 4} is also present in {2, 4, 6, 8} without using issubset()

a={2,4}
b={2,4,6,8}
x=list(a)
y=list(b)
flag=1
i=0
while i<len(x):
    j=0
    found=0
    while j<len(y):
        if x[i]==y[j]:
            found=1
        j=j+1
    if found==0:
        flag=0
    i=i+1
if flag==1:
    print("present")
else:
    print("not present")