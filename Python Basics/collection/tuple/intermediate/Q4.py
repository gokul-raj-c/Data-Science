#Split the tuple (10, 20, 30, 40, 50) into two halves. If there is an extra item, put it in the first half.

a=(10,20,30,40,50)
print(a)
mid=(len(a)+1)//2
first=[]
last=[]
i=0
while i<mid:
    first.append(a[i])
    i=i+1
j=mid
while j<len(a):
    last.append(a[j])
    j=j+1
print(tuple(first))
print(tuple(last))

