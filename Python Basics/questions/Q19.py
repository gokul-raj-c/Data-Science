#Calculate the sum of a number's series: 1 + 2 + 3 + ... + N for a given N.

n=int(input("enter limit: "))
s=0
i=1
while i<=n:
    s=s+i
    i=i+1
print(s)