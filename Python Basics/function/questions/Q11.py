#Write a function stats(nums) that returns the count, total and average of a list as three values. 
# Print each on its own line for [10, 20, 30, 40].

def stats(nums):
    count=0
    total=0
    for i in nums:
        count=count+1
        total=total+i
    avg=total/count
    return count,total,avg

a=[10, 20, 30, 40]
print(a)
c,t,a=stats(a)
print("count:",c)
print("total:",t)
print("average:",a)