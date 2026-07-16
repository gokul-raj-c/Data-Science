"""
Print the pattern
11111
2222
333
44
5
"""

i=5
k=1
while i>=1:
    j=1
    while j<=i:
        print(k,end="")
        j=j+1
    k=k+1
    print()
    i=i-1

