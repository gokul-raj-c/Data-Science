"""
2
2 2
6 6 6 
4 4 4 4
"""

i=1
while i<=4:
    if i%2!=0:
        print(str(i*2)*i)
    else:
        print(str(i)*i)
    i=i+1