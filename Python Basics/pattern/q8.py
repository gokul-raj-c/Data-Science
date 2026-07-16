"""
Print the pattern
*********
 *******
  *****
   ***
    *
"""

i=9
while i>=1:
    print(" "*((9-i)//2) + "*"*(i))
    i=i-2