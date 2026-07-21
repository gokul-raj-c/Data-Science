# Keep doubling a number starting from 1 (1, 2, 4, 8, 16, ...) until it goes above 1000. 
# Print each value, and at the end print how many doublings it took.

i=1
c=0
while i<=1000:
    i=i*2
    c=c+1
print(c)