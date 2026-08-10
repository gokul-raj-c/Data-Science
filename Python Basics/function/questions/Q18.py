# Write a function is_prime(n) that returns True or False, and a function only_primes(nums) that uses is_prime() 
# to return all prime values from a list. Test it with [10, 7, 15, 23, 9, 2].

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True 

def only_primes(nums):
    res=[]
    for j in nums:
        if is_prime(j):
            res.append(j)
    return res

a=[10, 7, 15, 23, 9, 2]
print(a)
b=only_primes(a)
print(b)