#print all numbers that has last digit 4

a=[14,22,34,44,55,46]
i=0
while i<len(a):
    if a[i]%10==4:
        print(a[i])
    i=i+1
