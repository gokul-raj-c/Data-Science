#Reverse a list using recursion

# def reverse_list(arr, start=0, end=None):
#     if end is None:
#         end = len(arr) - 1

#     if start >= end:
#         return arr

#     arr[start], arr[end] = arr[end], arr[start]

#     return reverse_list(arr, start + 1, end - 1)

def reverse_list(arr,i=0):
    if i == len(arr):
        return []

    return reverse_list(arr,i+1) + [arr[i]]

print(reverse_list([10, 20, 30, 40]))
