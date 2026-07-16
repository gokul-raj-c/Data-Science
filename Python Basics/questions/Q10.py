# Count how many even and odd digits a number has (e.g., 2374 -> 2 even, 2 odd).

a=int(input("enter a number: "))
rev=0
ecount=0
ocount=0
while a>0:
    d=a%10
    a=a//10
    if d%2==0:
        ecount=ecount+1
    else:
        ocount=ocount+1
print("even digit count:",ecount)
print("odd digit count:",ocount)