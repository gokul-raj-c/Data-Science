#Calculate the average of numbers in a list.

a=[1,2,3,4,5,6,7,8,9,10]
c=0
s=0
for i in a:
    s=s+i
    c=c+1
print(s/c)