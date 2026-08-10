#Write a function second_largest(nums) that returns the second largest value in a list without using max() or sort(). 
# Test it with [14, 62, 8, 45, 62, 33] (answer: 45).

def second_largest(nums):
    large=nums[0]
    for i in nums:
        if i > large:
            large=i
    second_large=nums[0]
    for i in nums:
        if i > second_large and i != large:
            second_large=i
    return second_large

a=[14, 62, 8, 45, 62, 33]
print(a)
res=second_largest(a)
print("second largest value in list:",res)