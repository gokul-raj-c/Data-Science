# Count how many times a particular number occurs.

def number_count(arr,val,i=0):
    if i==len(arr):
        return 0
    if arr[i] == val:
        return 1+ number_count(arr,val,i+1)
    return number_count(arr,val,i+1)

print(number_count([2,3,4,2,6,2],10))