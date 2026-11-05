#Find the common elements between two lists without duplicates.

arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7]
c=[]
for i in arr1:
    if i in arr2:
        c.append(i)
print(arr1)
print(arr2)
print(c)