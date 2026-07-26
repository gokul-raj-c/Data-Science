#Find the product (multiplication) of all numbers in the list [2,3,4,5] using a while loop. (Answer should be 120.)

a=[2,3,4,5]
p=1
i=0
while i<len(a):
    p=p*a[i]
    i=i+1
print(p)