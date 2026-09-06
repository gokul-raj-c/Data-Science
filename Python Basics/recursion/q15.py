# Check whether all elements are divisible by 5.

def check_divisible(arr,i=0):
    if i==len(arr):
        return True
    if arr[i] % 5 != 0:
        return False
    return check_divisible(arr,i+1)

print(check_divisible([15,25,35,45,5]))