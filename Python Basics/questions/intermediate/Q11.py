#Calculate the sum of the series 1! + 2! + 3! + ... + N! for a given N.

n=int(input("enter limit: "))
i=1
summ=0
while i<=n:
    j=i
    f=1
    while j>=1:
        f=f*j
        j=j-1
    summ=summ+f
    i=i+1
print(summ)
