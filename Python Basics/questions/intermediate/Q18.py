# Print a 5 × 5 checkerboard of 1s and 0s, where each row starts with the opposite digit of the row above: 
# 1 0 1 0 1 
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1

i=1
while i<=25:
    if i%2==0:
        print(0,end=" ")
    else:
        print(1,end=" ")
    if i%5==0:
        print()
    i=i+1