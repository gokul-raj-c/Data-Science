"""
Print the pattern
A
AB
ABC
ABCD
ABCDE
"""

i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(64+j),end="")
        j=j+1
    print()
    i=i+1