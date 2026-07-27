#From [3, 5, 3, 7, 9, 5, 3, 7], use sets to print values that appear exactly once

a=[3,5,3,7,9,5,3,7]
print(a)
b=set(a)
c=list(b)
d=[]

i=0
while i<len(c):
    j=0
    count=0
    while j<len(a):
        if c[i]==a[j]:
            count=count+1
        j=j+1
    if count==1:
        d.append(c[i])
    i=i+1
print("values that appear exactly once:",d)