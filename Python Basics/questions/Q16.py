#. Print a right-angled triangle pattern of stars using nested while loops:
# * 
# * * 
# * * *
# * * * * 
# * * * * *

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1