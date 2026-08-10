#Write a function running_total(nums) that returns a new list where each element is the sum of all values up to that position. 
# Test it with [5, 3, 8, 2] (answer: [5, 8, 16, 18]).

def running_total(nums):
    new_list=[]
    s=0
    for i in nums:
        s=s+i
        new_list.append(s)
    return new_list

a=[5, 3, 8, 2]
print(a)
res=running_total(a)
print("new list:",res)