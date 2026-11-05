#Reverse a list without using reverse() or slicing.

arr=[1,2,3,4,5,6,7]
arr_rev=[]
i=len(arr)-1
while i >= 0:
    arr_rev.append(arr[i])
    i-=1
print(arr)
print(arr_rev)