# Check whether a list contains duplicate elements.

def check_duplicates(arr,i=0,j=1):
    if i==len(arr)-1:
        return False
    if j==len(arr):
        return check_duplicates(arr,i+1,i+2)
    if arr[i]==arr[j]:
        return True
    return check_duplicates(arr,i,j+1)

print(check_duplicates([1,2,3,4]))