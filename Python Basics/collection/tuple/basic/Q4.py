#From the tuple (4, 9, 12, 15, 20, 21), create a list containing only odd numbers.

a=(4,9,12,15,20,21)
odd=[]
i=0
while i<len(a):
    if a[i]%2!=0:
        odd.append(a[i])
    i=i+1
print(a)
print("odd numbers list:",odd)