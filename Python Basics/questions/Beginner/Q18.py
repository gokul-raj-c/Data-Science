#Print a number triangle where each row starts lower and counts up to 5:
# 5 
# 4 5 
# 3 4 5 
# 2 3 4 5 
# 1 2 3 4 5

i=5
while i>=1:
    j=i
    while j<=5:
        print(j,end=" ")
        j=j+1
    print()
    i=i-1
