#For the list [10,20, 30,40, 50,60], print the sum of elements at even indexes and the sum of elements at odd indexes separately.

a=[10,20,30,40,50,60]
even_sum=0
odd_sum=0
i=0
while i<len(a):
    if i%2==0:
        even_sum=even_sum+a[i]
    else:
        odd_sum=odd_sum+a[i]
    i=i+1
print("sum of elements at even indexes:",even_sum)
print("sum of elements at odd indexes:",odd_sum)