#Print a triangle of odd numbers, where row N shows the first N odd numbers: 
# 1 
# 1 3 
# 1 3 5 
# 1 3 5 7 
# 1 3 5 7 9

n=int(input("enter no of rows: "))
i=1
while i<=n:
    j=1
    k=1
    while j<=i:
        print(k,end=" ")
        k=k+2
        j=j+1
    print()
    i=i+1