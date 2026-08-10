# Write a function top_n(nums, n=3) that returns the largest n values of a list. 
# Call it once without n and once with n = 2 for [5, 20, 9, 41, 17, 33].

def top_n(nums, n=3):
    res=[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j]:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    for j in range(0,n):
        res.append(nums[j])
    return res

a=[5, 20, 9, 41, 17, 33]
print(a)
res1=top_n(a)
print("top 3 values:",res1)
res2=top_n(a,2)
print("top 2 values:",res2)