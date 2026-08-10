#Write a function split_even_odd(nums) that returns two lists — one of even numbers and one of odd numbers. 
#Test it with [4, 9, 12, 7, 20, 15], and unpack the result into two variables when you call it.

def split_even_odd(nums):
    even_list=[]
    odd_list=[]
    for i in nums:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list,odd_list

a=[4, 9, 12, 7, 20, 15]
print(a)
even,odd=split_even_odd(a)
print("even list:",even)
print("odd list:",odd)