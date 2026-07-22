#sum of odd numbers in the list

a=[11,22,33,44,55,66]
i=0
summ=0
while i<len(a):
    if a[i]%2!=0:
        summ=summ+a[i]
    i=i+1
print(summ)