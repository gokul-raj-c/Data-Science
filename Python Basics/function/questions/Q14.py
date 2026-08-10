# Write a function replace_negatives(nums) that changes the list in place so every negative number becomes 0, 
# and returns nothing. Test it with [5, -3, 8, -12, 0, -1] and print the list after the call to show it was modified.

def replace_negatives(nums):
    for i in range(0,len(nums)):
        if nums[i] < 0:
            nums[i]=0

a=[5, -3, 8, -12, 0, -1]
print(a)
replace_negatives(a)
print(a)