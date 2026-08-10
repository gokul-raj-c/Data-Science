#Write a function search(nums, target) that returns the index where target is found, or -1 if it is not present. 
# Test it with [11, 24, 36, 47, 58] for both a value that exists and one that does not.

def search(nums, target):
    for i in range(0,len(nums)):
        if nums[i]==target:
            return i
    return -1

a=[11, 24, 36, 47, 58]
print(a)
res1 = search(a, 36)
print("index of 36:",res1)
res2 = search(a, 50)
print("index of 50:",res2)