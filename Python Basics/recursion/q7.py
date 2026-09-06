#check all elements in list is prime or not

def check_prime(arr,i=0,j=2):
    if i==len(arr):
        return True
    if arr[i] < 2:
        return False
    if j*j > arr[i]:
        return check_prime(arr,i+1,2)
    if arr[i] % j == 0:
        return False
    return check_prime(arr,i,j+1)

print(check_prime([2,3,5,7,9]))
