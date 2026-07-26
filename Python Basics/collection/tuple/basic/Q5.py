# Check whether the tuple (1, 2, 3, 2, 1) is a palindrome using a while loop.

a=(1,2,3,2,1)
i=0
j=len(a)-1
flag=0
while i<j:
    if a[i]!=a[j]:
        flag=1
    i=i+1
    j=j-1
print(a)
if flag==0:
    print("pallindrome")
else:
    print("not pallindrome")