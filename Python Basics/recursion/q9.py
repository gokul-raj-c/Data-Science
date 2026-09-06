#Check if all elements are even

def check_even(arr,i=0):
    if i==len(arr):
        return True
    if arr[i] % 2 != 0:
        return False
    return check_even(arr,i+1)

print(check_even([1,2,3,4]))