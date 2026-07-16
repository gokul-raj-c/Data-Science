#Find the sum of all even numbers between 1 and 100.

i=1
s=0
while i<=100:
    if i%2==0:
        s=s+i
    i=i+1
print("sum:",s)