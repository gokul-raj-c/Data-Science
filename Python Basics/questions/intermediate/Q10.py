#Calculate the series 1 − 2 + 3 − 4 + ... up to N terms (alternating signs) for a given N.

n=int(input("enter limit: "))
i=1
summ=0
while i<=n:
    if i%2==0:
        summ=summ-i
    else:
        summ=summ+i
    i=i+1
print(summ)
