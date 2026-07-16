"""
Print the pattern
    1
   222
  33333
 4444444
555555555
"""

i=1
j=1
while i<=9:
    print(" "*((9-i)//2) + str(j)*i)
    j=j+1
    i=i+2