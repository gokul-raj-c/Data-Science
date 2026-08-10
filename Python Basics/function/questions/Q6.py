#Write a function average(nums) that returns the average of a list, and a second function above_average(nums) 
# that calls average() and returns all elements greater than it. Test with [45, 12, 78, 34, 90].

def average(nums):
    n=len(nums)
    s=0
    for i in nums:
        s=s+i
    avg=s/n
    return avg

def above_average(nums):
    a=average(nums)
    print("average:",a)
    res=[]
    for i in nums:
        if i > a:
            res.append(i)
    return res

a=[45, 12, 78, 34, 90]
print(a)
elements=above_average(a)
print("elements greater than average:",elements)