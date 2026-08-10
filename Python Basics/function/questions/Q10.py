#Write a function min_max(nums) that returns both the smallest and the largest value in a single return statement. 
# Test it with [23, 7, 45, 12, 39] and print them as Min = 7, Max = 45.

def min_max(nums):
    min_val=nums[0]
    max_val=nums[0]
    for i in nums:
        if i > max_val:
            max_val=i
        if i < min_val:
            min_val=i
    return min_val,max_val

a=[23, 7, 45, 12, 39]
print(a)
small,large=min_max(a)
print("min:",small)
print("max:",large)