#The list [1, 2, 3, 5, 6, 7, 8, 9, 10] should hold every number from 1 to 10 , but one is missing. 
# Find the missing number using addition, not by checking each number one by one.

a=[1, 2, 3, 5, 6, 7, 8, 9, 10]
list_sum=0
num_sum=0
for i in a:
    list_sum=list_sum+i
for i in range(1,11):
    num_sum=num_sum+i
missing_number=num_sum-list_sum
print(missing_number)