#Ask the user for a number and count how many times it appears in the tuple (3, 5, 3, 7, 9, 5, 3).

a=(3,5,3,7,9,5,3)
print(a)
n=int(input("choose a number: "))
i=0
c=0
while i<len(a):
    if a[i]==n:
        c=c+1
    i=i+1
print("count of",n,"in tuple:",c)