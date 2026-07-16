"""
2
3 5
2 4 6
3 5 7 9
"""

i=1
while i<=4:
    if i%2!=0:
        j=2
        while j<=i*2:
            print(j,end=" ")
            j=j+2
    else:
        k=3
        while k<=(i*2)+1:
            print(k,end=" ")
            k=k+2
    print()
    i=i+1