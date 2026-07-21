#Print a growing word triangle using the string "PYTHON" and indexing:

a="python"
n=len(a)-1
i=0
while i<len(a):
    j=0
    while j<=i:
        print(a[j],end=" ")
        j=j+1
    print()
    i=i+1