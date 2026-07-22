#Check whether a list is a palindrome (same forwards and backwards, e.g.[1,2,3,2, 1]
#  using a while loop that compares elements from both ends.

a=[1,2,3,2, 1]
i=0
j=len(a)-1
p=1
while i<j:
    if a[i]!=a[j]:
        p=0
    i=i+1
    j=j-1
if p==1:
    print("pallindrome")
else:
    print("not pallindrome")