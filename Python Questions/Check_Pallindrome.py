#Check whether a list reads the same forward and backward.

arr=[1,2,3,2,1,2]
p=True
i=0
j=len(arr)-1
while i<j:
    if arr[i] != arr[j]:
        p=False
    i+=1
    j-=1
if p:
    print("pallindome")
else:
    print("not pallindrome")