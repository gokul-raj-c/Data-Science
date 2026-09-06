#Count prime numbers

def count_prime(arr,i=0,j=2):

    if i == len(arr):
        return 0
    if arr[i] < 2:
        return count_prime(arr,i+1,2)
    if j * j > arr[i]:
        return 1 + count_prime(arr,i+1,2)
    if arr[i] % j == 0:
        return count_prime(arr,i+1,2)
    return count_prime(arr,i,j+1)

print(count_prime([2,3,5,7,9]))