# Keep adding 1 + 2 + 3 + ... and stop as soon as the total goes above 100. 
# Print the final total and how many numbers were added.

s=0
i=1
c=0
while s<=100:
    s=s+i
    i=i+1
    c=c+1
print("sum:",s)
print("count",c)