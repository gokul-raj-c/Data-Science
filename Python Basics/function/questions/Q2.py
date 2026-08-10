#Write a function count_above(nums, limit) that returns how many values in nums are greater than limit. 
# Test it with [12, 45, 7, 89, 30] and limit = 20 (answer: 3).

def count_above(nums, limit):
    c=0
    for i in nums:
        if i > limit:
            c=c+1
    return c

a=[12, 45, 7, 89, 30]
l=20
print(a)
res=count_above(a,l)
print("count of values in list that are greater than",l,":",res)