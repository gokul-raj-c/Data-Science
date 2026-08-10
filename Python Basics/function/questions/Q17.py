#Write a function insert_sorted(nums, value) that inserts value into an already sorted list at the correct position 
# so the list stays sorted. Do not use sort(). Test it with [10, 20, 40, 50] and value = 30.

def insert_sorted(nums, value):
    for i in range(0,len(nums)):
        if value < nums[i]:
            nums.insert(i,value)
            return nums
    nums.append(value)
    return nums

a=[10, 20, 40, 50]
print(a)
b=insert_sorted(a,30)
print("value = 30:",b)