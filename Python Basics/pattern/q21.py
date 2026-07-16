"""
Print the pattern
*****
*   *
*   *
*   *
*****
"""

i=1
while i<=5:
    if i==1 or i==5:
        print("*"*5)
    else:
        print("*"*1 + " "*3 + "*"*1)
    i=i+1
