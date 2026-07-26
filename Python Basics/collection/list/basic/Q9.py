#Print only the even numbers from the list [3,8,15,22,7,40] using a while loop and an if statement.

a=[3,8,15,22,7,40]
i=0
while i<len(a):
    if a[i]%2==0:
        print(a[i],end=" ")
    i=i+1