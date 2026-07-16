"""
Print the pattern
555555555
 4444444
  33333
   222
    1
"""

i=9
j=5
while i>=1:
    print(" "*((9-i)//2) + str(j)*(i))
    j=j-1
    i=i-2