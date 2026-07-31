#Write a function that sums all numbers in a list.

def find_sum(a):
    s=0
    for i in a:
        s=s+i
    print(s)

a=[1,2,3,4,5]
find_sum(a)