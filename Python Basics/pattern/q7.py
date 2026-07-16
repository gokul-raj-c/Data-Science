"""
Print the pattern
    *
   ***
  *****
 *******
*********
"""

i=1
while i<=9:
    print(" "*((9-i)//2) + "*"*i)
    i=i+2