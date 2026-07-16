"""
Print the pattern
ABCDE
ABCD
ABC
AB
A
"""

i=5
while i>=1:
    j=1
    while j<=i:
        print(chr(64+j),end="")
        j=j+1
    print()
    i=i-1

