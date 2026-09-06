#Check if all elements are positive

def check_positive(arr,i=0):
    if i==len(arr):
        return True
    if arr[i] < 0:
        return False
    return check_positive(arr,i+1)

print(check_positive([1,2,3,-4,5]))