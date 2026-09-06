# Find the minimum element recursively.

def find_minimum(arr,i=0):
    if i==len(arr) - 1:
        return arr[i]
    minimum=find_minimum(arr,i+1)
    if arr[i] < minimum:
        return arr[i]
    else:
        return minimum

print(find_minimum([3,4,1,6,8]))