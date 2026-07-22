#Calculate and print the average of the numbers in the list [10,20, 30,40] using a while loop

a=[10,20, 30,40]
i=0
s=0
n=len(a)-1
while i<n:
    s=s+a[i]
    i=i+1
print(s/n)