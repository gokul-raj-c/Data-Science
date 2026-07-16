"""
Print the pattern
5
44
333
2222
11111
"""

i=1
k=5
while i<=5:
    j=1
    while j<=i:
        print(k,end=" ")
        j=j+1
    print()
    k=k-1
    i=i+1


