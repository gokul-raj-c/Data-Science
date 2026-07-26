#From the list [4, 1, 2, 7, 8, 3], count how many numbers are even and how many are odd using a while loop.

a=[4,1,2,7,8,3]
odd_count=0
even_count=0
i=0
while i<len(a):
    if a[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    i=i+1
print(a)
print("even numbers:",even_count)
print("odd numbers:",odd_count)