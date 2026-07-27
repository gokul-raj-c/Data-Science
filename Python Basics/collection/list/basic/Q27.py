# A shop stores prices in [50, 120, 80, 200, 30]. Find the total cost of only the items priced above 75.

a=[50,120,80,200,30]
i=0
s=0
while i<len(a):
    if a[i]>75:
        s=s+a[i]
    i=i+1
print("total cost of items priced above 75:",s)