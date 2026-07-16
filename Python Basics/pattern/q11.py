"""
Print the pattern
5
54
543
5432
54321
"""

i=1
while i<=5:
    j=1
    k=5
    while j<=i:
        print(k,end="")
        k=k-1
        j=j+1
    print()
    i=i+1

