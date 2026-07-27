#Reverse the tuple ("p", "y", "t", "h", "o", "n") into a new tuple using a while loop.

a=("p","y","t","h","o","n")
print(a)
b=[]
i=len(a)-1
while i>=0:
    b.append(a[i])
    i=i-1
print(tuple(b))