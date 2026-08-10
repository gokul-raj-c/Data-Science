#Write a function rotate_left(nums, n) that rotates a list to the left n times and returns the result. 
# Test it with [1, 2, 3, 4, 5] and n = 2 (answer: [3, 4, 5, 1, 2]).

def rotate_left(nums, n):
    for i in range(0,n):
        first=nums.pop(0)
        nums.append(first)
    return nums

a=[1, 2, 3, 4, 5]
print(a)
res=rotate_left(a,2)
print(res)