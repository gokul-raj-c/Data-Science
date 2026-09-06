# Find the sum of only even numbers.

def sum_of_even(arr,i=0):
    if i==len(arr):
        return 0
    if arr[i] % 2 == 0:
        return arr[i] + sum_of_even(arr,i+1)
    return sum_of_even(arr,i+1)

print(sum_of_even([1,2,3,4,5,6]))

# Find the product of all elements.

def product_of_even(arr,i=0):
    if i==len(arr):
        return 1
    if arr[i] % 2 == 0:
        return arr[i] * product_of_even(arr,i+1)
    return product_of_even(arr,i+1)

print(product_of_even([1,2,3,4,5,6]))