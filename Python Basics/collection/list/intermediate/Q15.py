#Ask the user for a number n and generate the first n terms of the Fibonacci series 
# into a list using a while loop (0,1,1,2,3,5, ...).

n=int(input("enter limit: "))
i=1
arr=[]
a=0
b=1
while i<=n:
    arr.append(a)
    c=a+b
    a=b
    b=c
    i=i+1
print(arr)
