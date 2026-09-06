#Count even numbers

def count_even(arr,i=0):
    if i==len(arr):
        return 0
    if arr[i] % 2 == 0:
        return 1 + count_even(arr,i+1)
    return count_even(arr,i+1)
    
print(count_even([1,2,3,4,5]))