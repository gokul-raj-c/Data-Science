#Ask the user for a number n. Rotate the list loop. (Example: rotating twice gives [1,2,3,4,5] to the left n times 
# using a while [3,4,5,1,2].)

a=[1,2,3,4,5]
n=int(input("enter number: "))
i=0
while i<n:
    b=a[0]
    a.pop(0)
    a.append(b)
    i=i+1
print(a)